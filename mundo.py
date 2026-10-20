"""Mapamundi de Actualidad (v1): un punto por noticia o evento sobre un mapa de casillas, sin IA ni red.

Datos: eventos/calendario.toml, explorador/regulacion.json (hitos y próximas fechas) y
explorador/datos.json (movimientos). El país se asigna por diccionario de palabras clave
o por la jurisdicción de cada celda. Nada se inventa: lo que no se puede ubicar va a «Internacional».
"""
import json
import tomllib
import unicodedata
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlsplit

import streamlit as st
import streamlit.components.v1 as components

RAIZ = Path(__file__).parent
CARPETA = RAIZ / "explorador"

PAISES = {"us": "EE. UU.", "eu": "Unión Europea", "uk": "Reino Unido", "ch": "Suiza", "sg": "Singapur", "hk": "Hong Kong",
          "cn": "China", "jp": "Japón", "kr": "Corea del Sur", "in": "India", "br": "Brasil", "ru": "Rusia",
          "ae": "Emiratos", "za": "Sudáfrica", "id": "Indonesia", "eg": "Egipto", "et": "Etiopía", "ir": "Irán",
          "sa": "Arabia Saudí", "ca": "Canadá", "int": "Internacional / BIS"}
# Jurisdicciones de regulacion.json y países de datos.json -> casilla
JUR = {"eeuu": "us", "ue": "eu", "sg": "sg", "hk": "hk", "kr": "kr", "jp": "jp", "in": "in", "br": "br", "ru": "ru",
       "ae": "ae", "cn": "cn", "brics": "int", "za": "za", "id": "id"}
NOMBRE_A_PAIS = {"EE. UU.": "us", "Unión Europea": "eu", "Internacional": "int", "Brasil": "br", "Canadá": "ca",
                 "Hong Kong": "hk", "Japón": "jp", "Luxemburgo": "eu", "Rusia": "ru", "Arabia Saudí": "sa",
                 "Corea del Sur": "kr", "Reino Unido": "uk", "Suiza": "ch", "Singapur": "sg", "China": "cn",
                 "India": "in", "Sudáfrica": "za", "Indonesia": "id", "Egipto": "eg", "Etiopía": "et", "Irán": "ir",
                 "Emiratos Árabes Unidos": "ae"}
# Palabras clave (en minúsculas y sin tildes) -> casilla
CLAVES_PAIS = [("us", ["ee. uu", "eeuu", "fed ", "fomc", "sec ", "sec:", "cftc", "genius", "clarity", "senado", "tesoro", "ipc de", "pce",
                       "ripple", "swell", "nueva york", "occ", "brent", "empleo", "dtcc", "eia", "washington"]),
               ("eu", ["bce", "euro digital", "mica", "esma", "dac8", "pontes", "europe", "union europea", "eba"]),
               ("uk", ["reino unido", "bank of england", "fca "]), ("ch", ["suiza", "snb"]),
               ("sg", ["singapur", "nexus"]), ("hk", ["hong kong", "hkma"]),
               ("cn", ["china", "pboc", "e-cny", "yuan"]), ("jp", ["japon", "banco de japon", "boj", "jfsa"]),
               ("kr", ["corea", "bank of korea"]), ("in", ["india", "rbi"]), ("br", ["brasil", "drex"]),
               ("ru", ["rusia", "rublo"]), ("ae", ["emiratos", "dubai", "abu dabi"]), ("za", ["sudafrica"]),
               ("id", ["indonesia"]), ("eg", ["egipto"]), ("et", ["etiopia"]), ("ir", ["iran", "ormuz"]),
               ("sa", ["arabia saudi", "opep", "opec"]), ("ca", ["canada"]),
               ("int", ["bis ", "g20", "apec", "brics", "agora", "fmi", "fsb"])]
TEMA_REG = {"stablecoins": "reg", "ley_marco": "reg", "etf": "fondos", "tokenizacion": "tok", "custodia": "reg",
            "cbdc": "cbdc", "fiscal": "fiscal", "politica": "macro"}
OFICIAL = (".gov", ".europa.eu", "bis.org", "boj.or.jp", "bankofengland.co.uk", "imf.org")


def _plano(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def _paises(texto):
    t = " " + _plano(texto) + " "
    out = [p for p, claves in CLAVES_PAIS if any(k in t for k in claves)]
    return out or ["int"]


def _fecha(s):
    try:
        return date.fromisoformat(str(s)[:10])
    except Exception:
        return None


def _nivel(texto):
    t = str(texto)
    if "VERIFICAR" in t:
        return "VERIFICAR"
    return "P" if "[P]" in t else ("S" if "[S]" in t else "VERIFICAR")


def _leer_json(ruta):
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except Exception:
        return None


def _construir(hoy_iso):
    import explorador
    hoy = date.fromisoformat(hoy_iso)
    pasado, futuro = hoy - timedelta(days=120), hoy + timedelta(days=270)
    ev = []

    def anadir(**k):
        ini = _fecha(k["fecha"])
        if not ini or ini < pasado or ini > futuro:
            return
        k["fecha"] = ini.isoformat()
        k["futuro"] = ini >= hoy
        ev.append(k)

    # (a) calendario
    try:
        with open(RAIZ / "eventos" / "calendario.toml", "rb") as fh:
            for e in tomllib.load(fh).get("eventos", []):
                tit, det = str(e.get("titulo", "")), str(e.get("detalle", ""))
                tema, _ = explorador._tema_y_capa(tit, det)
                dom = urlsplit(str(e.get("fuente", ""))).netloc.replace("www.", "")
                nivel = "VERIFICAR" if e.get("aproximado") else ("P" if dom.endswith(OFICIAL) else "S")
                anadir(fecha=e.get("fecha"), hasta=str(e.get("hasta", "")), tit=tit[:150], que=explorador._limpiar(det)[:400],
                       quien=dom or "—", paises=_paises(tit + " " + det), tema=tema, nivel=nivel, fuente=dom or "—",
                       origen="Calendario", impacto=str(e.get("impacto", "")),
                       contexto="Fecha aproximada: se fijará con la fuente." if e.get("aproximado") else "")
    except Exception:
        pass
    # (b) radar regulatorio
    rad = _leer_json(CARPETA / "regulacion.json")
    if rad:
        jurs = {j["id"]: j["nombre"] for j in rad.get("jurisdicciones", [])}
        temas = {t["id"]: t["nombre"] for t in rad.get("temas", [])}
        escala = rad.get("escala", {})
        for c in rad.get("celdas", []):
            pais, tema_r = JUR.get(c.get("jur")), c.get("tema")
            if not pais:
                continue
            nivel = _nivel("[" + str(c.get("fuente", "")) + "]")
            ctx = (f"{jurs.get(c['jur'], '')} · {temas.get(tema_r, '')}. Etapa {c.get('etapa')}: "
                   f"{escala.get(str(c.get('etapa')), '')}. {c.get('estado', '')}")
            if c.get("falta"):
                ctx += " Pendiente: " + str(c["falta"])
            base = dict(paises=[pais], tema=TEMA_REG.get(tema_r, "reg"), origen="Radar regulatorio", impacto="",
                        contexto=ctx[:900], quien=jurs.get(c["jur"], ""), hasta="",
                        fuente="Radar · " + ", ".join(c.get("informes", [])[:2]))
            for h in c.get("hitos", []):
                que = str(h.get("que", ""))
                anadir(fecha=h.get("fecha"), tit=que[:150], que=que[:400], nivel="VERIFICAR" if "VERIFICAR" in que else nivel, **base)
            p = c.get("proxima")
            if p:
                que = str(p.get("que", ""))
                anadir(fecha=p.get("fecha"), tit="Próxima fecha: " + que[:130], que=que[:400],
                       nivel="VERIFICAR" if "VERIFICAR" in que else nivel, **base)
    # (c) movimientos de datos.json
    dat = _leer_json(CARPETA / "datos.json")
    if dat:
        for m in dat.get("movimientos", []):
            paises = [NOMBRE_A_PAIS.get(p, "int") for p in m.get("pais", [])] or ["int"]
            texto = str(m.get("texto", ""))
            tema, _ = explorador._tema_y_capa(texto, str(m.get("capa", "")))
            anadir(fecha=m.get("fecha"), hasta="", tit=texto[:150], que=texto[:400], quien=str(m.get("actor", "")),
                   paises=list(dict.fromkeys(paises)), tema=tema, nivel=_nivel(m.get("fuente", "")),
                   fuente=str(m.get("fuente", ""))[:120], origen="Movimientos", impacto="",
                   contexto="Estado: " + str(m.get("estado", "")) + ". Nombra a XRP/XLM: " + str(m.get("nombra", "")) + ".")
    # quita duplicados (misma fecha, país y arranque del texto)
    vistos, unicos = set(), []
    for e in ev:
        clave = (e["fecha"], e["paises"][0], e["tit"][:60])
        if clave not in vistos:
            vistos.add(clave)
            unicos.append(e)
    fut = sorted([e for e in unicos if e["futuro"]], key=lambda e: e["fecha"])
    pas = sorted([e for e in unicos if not e["futuro"]], key=lambda e: e["fecha"], reverse=True)
    out = fut + pas
    for i, e in enumerate(out):
        e["id"] = i
    return {"hoy": hoy_iso, "paises": PAISES, "temas": explorador.TEMAS, "eventos": out}


def _version():
    s = 0.0
    for p in (Path(__file__), CARPETA / "mundo.html", CARPETA / "regulacion.json", CARPETA / "datos.json",
              RAIZ / "eventos" / "calendario.toml"):
        try:
            s = max(s, p.stat().st_mtime)
        except Exception:
            pass
    return s


@st.cache_data(ttl=600, show_spinner=False)
def _html(hoy_iso, version):
    datos = _construir(hoy_iso)
    # Dentro de <script type="application/json"> hay que evitar que el texto cierre la etiqueta
    texto = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    return (CARPETA / "mundo.html").read_text(encoding="utf-8").replace("__DATOS__", texto)


def mostrar():
    try:
        html = _html(date.today().isoformat(), _version())
    except Exception as e:
        st.warning(f"No se pudo cargar el mapamundi ({type(e).__name__}).")
        return
    components.html(html, height=920, scrolling=True)
