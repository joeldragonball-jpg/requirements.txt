"""C243: genera explorador/espana-empresas.json (empresas públicas + comparador de CCAA).

Sin IA y sin claves. Parte automática: INE (API Tempus) para paro EPA y población por CCAA,
y deuda PDE por CCAA leída de explorador/paneles.json (Banco de España, ya cargada por otro script).
Parte manual: cifras de empresas públicas leídas en la web oficial (ver 'EMPRESAS').
Uso: PYTHONIOENCODING=utf-8 python scripts/leer_espana_empresas.py
"""
import json
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "explorador" / "espana-empresas.json"
API = "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/{t}?nult=1"

# nombre INE -> nombre en paneles.json (deuda BdE)
CCAA = {
    "Andalucía": "Andalucía", "Aragón": "Aragón", "Asturias, Principado de": "Principado de Asturias",
    "Balears, Illes": "Illes Balears", "Canarias": "Canarias", "Cantabria": "Cantabria",
    "Castilla y León": "Castilla y León", "Castilla - La Mancha": "Castilla-La Mancha",
    "Cataluña": "Cataluña", "Comunitat Valenciana": "Comunidad Valenciana",
    "Extremadura": "Extremadura", "Galicia": "Galicia", "Madrid, Comunidad de": "Comunidad de Madrid",
    "Murcia, Región de": "Región de Murcia", "Navarra, Comunidad Foral de": "Comunidad Foral de Navarra",
    "País Vasco": "País Vasco", "Rioja, La": "La Rioja",
}

EMPRESAS = [
    {
        "id": "sepi", "nombre": "Grupo SEPI (consolidado)", "ejercicio": 2025,
        "cifra_negocio": 7384, "resultado_neto": 130, "inversiones": 529, "plantilla": "≈87.000 profesionales",
        "deuda": None, "aportaciones_estado": None,
        "fuente": "https://www.sepi.es/es/sala-de-prensa/noticias/el-grupo-sepi-obtiene-130-millones-de-beneficios-en-2025-y-alcanza-una",
        "fecha_fuente": "2026-06-30", "nivel": "P",
        "nota": "Nota de prensa de SEPI sobre las cuentas anuales 2025 aprobadas por su Consejo. Dato de la propia entidad (no auditado por este proyecto). Grupo Correos aporta el 28 % de la cifra de negocio, sin cifra absoluta en la nota. Deuda, plantilla exacta y aportaciones del Estado: no leídas [VERIFICAR].",
    },
    {
        "id": "aena", "nombre": "Aena", "ejercicio": 2025,
        "cifra_negocio": 6379.2, "resultado_neto": None, "ebitda": 3785, "plantilla": None,
        "deuda": None, "aportaciones_estado": None,
        "fuente": "https://www.aena.es/es/accionistas-e-inversores.html", "fecha_fuente": None, "nivel": "P",
        "nota": "La web de inversores indica «ingresos totales 2025» (6.379,2 M€) y «EBITDA reportado 2025» (3.785 M€); la etiqueta puede no coincidir con cifra de negocio estricta. Sin fecha visible del documento. Cotizada: el Estado (vía ENAIRE) posee ≈51 % [VERIFICAR porcentaje actual]. Resultado, deuda y plantilla: no leídos.",
    },
    {
        "id": "ineco", "nombre": "Ineco", "ejercicio": 2025,
        "cifra_negocio": None, "resultado_neto": None, "plantilla": None,
        "deuda": "Sin deuda financiera según su web de transparencia", "aportaciones_estado": None,
        "fuente": "https://www.ineco.com/ineco/transparencia/informacion-economica", "fecha_fuente": "2026-04", "nivel": "S",
        "nota": "La web lista «Cuentas anuales e Informe de Auditoría 2025» y «Detalle Subvenciones 2025» (PDF de abril 2026) que NO se pudieron leer con las herramientas disponibles [VERIFICAR]. Solo consta la afirmación de que no ha requerido deuda financiera.",
    },
    {
        "id": "navantia", "nombre": "Navantia (grupo, 100 % SEPI)", "ejercicio": 2025,
        "cifra_negocio": 1978, "resultado_neto": -149, "plantilla": "6.761 personas (grupo)",
        "deuda": None, "aportaciones_estado": None,
        "fuente": "https://www.sepi.es/es/sala-de-prensa/noticias/navantia-cuadruplica-contratacion-en-2025-y-situa-su-cartera-de-pedidos-en",
        "fecha_fuente": "2026-07-03", "nivel": "P",
        "nota": "Nota de Navantia publicada en la web de SEPI. Cifra de negocio consolidada 1.978 M€ (+30 %); sociedad individual: 1.728,5 M€ y resultado -119 M€; cartera de pedidos 12.826 M€. Pérdidas consolidadas -149 M€ (según la nota; el motivo no se ha leído [VERIFICAR]). Deuda y aportaciones del Estado: no leídas.",
    },
    {
        "id": "correos", "nombre": "Correos (grupo)", "ejercicio": 2025,
        "cifra_negocio": 1658, "resultado_neto": 14.4, "ebitda": 76, "plantilla": None,
        "deuda": None, "aportaciones_estado": None,
        "fuente": "https://www.vozpopuli.com/economia/transporte/correos-anuncia-beneficios-en-2025-tras-diez-anos-en-los-que-ha-superado-los-1000-millones-de-perdidas.html",
        "fecha_fuente": "2026-03-03", "nivel": "S",
        "nota": "Prensa (Vozpópuli, El Debate, 3-mar-2026), sin leer las cuentas de Correos. 1.658 M€ = cifra de negocio sin ingresos extraordinarios por elecciones (+2,5 %); beneficio 14,4 M€ frente a -94 M€ en 2024. Opinión de CCOO (no hecho): lo sostienen los más de 400 M€/año del Servicio Postal Universal y recortes de plantilla; The Objective habla de una inyección pública de 400 M€. Importe oficial de la compensación del Estado: [VERIFICAR].",
    },
    {
        "id": "renfe", "nombre": "Renfe-Operadora (grupo)", "ejercicio": 2025,
        "cifra_negocio": None, "resultado_neto": 60.2, "ebitda": 528.6, "plantilla": None,
        "deuda": None, "aportaciones_estado": None,
        "aportaciones_estado": "Presupuesto (no ejecutado): 1.009 M€ de compensación por obligaciones de servicio público a Renfe Viajeros en los PGE prorrogados; autorización de crédito extraordinario de hasta 671 M€ en 2026; Transportes pagó 307,8 M€ de ayudas al servicio ferroviario de Renfe en 2025 [S: extractos de búsqueda, no leídos en la fuente oficial]",
        "fuente": "https://www.democrata.es/economia/renfe-logra-60-millones-de-beneficio-en-2025-impulsada-por-un-19-mas-de-ingresos-en-billetes/",
        "fecha_fuente": None, "nivel": "S",
        "nota": "Prensa (Demócrata, Cronista), no las cuentas oficiales. Beneficio 60,2 M€ (la cifra provisional era ≈50 M€), EBITDA 528,6 M€, ingresos por billetes ≈2.000 M€ (+19 %), 531,4 millones de viajeros; primer beneficio tras cinco años de pérdidas. Las fuentes discrepan en el resultado de Renfe Viajeros (+70 M€ frente a -2,3 M€). Importes ejecutados de compensación, deuda y plantilla: no leídos [VERIFICAR]. El Tribunal de Cuentas fiscalizó las ayudas a Renfe Viajeros 2022-2023 (BOE 9-jun-2026): informe no leído.",
    },
    {
        "id": "adif", "nombre": "Adif y Adif Alta Velocidad", "ejercicio": None,
        "nota": "adif.es devuelve 403 a scripts y en Chrome las rutas probadas dan 404; cuentas no leídas. Por prensa [S]: Adif AV acumula una deuda superior a 21.300 M€ y pérdidas de 193,4 M€ frente a 100,9 M€ (The Objective; el ejercicio exacto de esa pieza, fechada jul-2025, queda [VERIFICAR]). La CNMC dice que Adif y Adif AV invirtieron 5.230 M€ en 2025 (+16 %) [S: solo extracto]. Aportaciones del Estado: no leídas.",
        "aportaciones_estado": "Previsto 2026: 1.384,2 M€ de la AGE (1.011,7 M€ del MRR + 372,5 M€ otras), adenda al convenio Adif 2021-2025 [S: extracto de búsqueda de BOE/Hacienda, no leído entero]",
        "fuente": "https://theobjective.com/economia/transporte/2025-07-05/adif-dispara-deuda-caos-ferroviario/", "nivel": "S",
    },
    {
        "id": "enaire", "nombre": "Enaire", "ejercicio": 2025,
        "nota": "Cuentas anuales y informe de gestión 2025 existen en enaire.es (PDF) pero son ilegibles con las herramientas (sin capa de texto accesible). Solo consta, del documento «Deuda 2025», una vida media de la deuda de 6,09 años y un coste medio del 2,21 % a 31-dic-2025 (extracto de búsqueda). Ingresos, resultado, saldo de deuda y plantilla: [VERIFICAR]. Gestionó 2.470.604 vuelos en 2025 (+4,7 %, CANSO).",
        "fuente": "https://enaire.es/docs/inline/es_ES/DOC_Cuentas_anuales_ENAIRE_2025.pdf", "nivel": "V",
    },
    {"id": "paradores", "nombre": "Paradores de Turismo", "ejercicio": None, "nota": "paradores.es dio error de certificado a la herramienta; sin cifras leídas. [VERIFICAR]", "fuente": "https://www.sepi.es", "nivel": "V"},
    {"id": "indra", "nombre": "Indra (participada por SEPI)", "ejercicio": None, "nota": "indra.es rechazó la conexión; SEPI la cita como «participación minoritaria» sin porcentaje en la nota leída. [VERIFICAR] % de SEPI y cifras.", "fuente": "https://www.sepi.es", "nivel": "V"},
]


def get(url):
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(url, timeout=40, context=ctx) as r:
        return json.load(r)


def ine_paro():
    out = {}
    for s in get(API.format(t=65334)):
        n = s["Nombre"]
        if n.startswith("Tasa de paro de la población. Ambos sexos.") and n.endswith(". Total. ") and s.get("Data"):
            for k in CCAA:
                if f"Ambos sexos. {k}. Total." in n:
                    d = s["Data"][0]
                    out[k] = (d["Valor"], d.get("Anyo"), d.get("FK_Periodo"))
    return out


def ine_poblacion():
    out = {}
    for s in get(API.format(t=56941)):
        n = s["Nombre"]
        if s.get("Data"):
            for k in CCAA:
                if n == f"Todas las edades. {k}. Total. Población. Número. ":
                    out[k] = s["Data"][0]["Valor"]
    return out


def main():
    paneles = json.loads((RAIZ / "explorador" / "paneles.json").read_text(encoding="utf-8"))["espana_deuda"]
    deuda = {c["nombre"]: c for c in paneles["ccaa"] if isinstance(paneles["ccaa"], list)}
    paro = ine_paro()
    pob = ine_poblacion()
    filas = []
    for ine, nom in CCAA.items():
        d = deuda.get(nom)
        p = pob.get(ine)
        fila = {
            "ccaa": nom,
            "paro_pct": paro.get(ine, (None,))[0],
            "poblacion": p,
            "deuda_pde_meur": round(d["deuda"], 1) if d else None,
            "deuda_per_capita_eur": round(d["deuda"] * 1e6 / p) if d and p else None,
        }
        filas.append(fila)
    filas.sort(key=lambda f: f["ccaa"])
    pers = next(iter(paro.values()), (None, None, None))
    res = {
        "generado": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "aviso": "Empresas públicas: cifras de la propia web de cada entidad, solo las que se pudieron leer; el resto queda [VERIFICAR]. Importes en millones de euros (M€). Una cifra grande o una pérdida NO implica mala gestión ni irregularidad: el perímetro y la función de cada empresa difieren.",
        "unidad": "M€", "escala": "millones de euros",
        "empresas": EMPRESAS,
        "comparador_ccaa": {
            "aviso": "Solo tres magnitudes leídas en fuente oficial. Renta por hogar y precio de vivienda por CCAA: no incluidos en este bloque (pendiente; la vivienda nacional ya está en el panel). La deuda PDE es la total del Banco de España, no distingue la parte con el Estado (FLA).",
            "paro": {"fuente": "INE, EPA, tabla 65334 (tasa de paro, ambos sexos)", "periodo": "último trimestre de la API", "anio_periodo": "2T 2026 (fecha 30-jun-2026 en la API)", "nivel": "P"},
            "poblacion": {"fuente": "INE, Estadística Continua de Población, tabla 56941 (1-ene-2025)", "nivel": "P"},
            "deuda": {"fuente": paneles.get("fuente"), "periodo": paneles.get("periodo"), "url": paneles.get("url"), "nivel": paneles.get("nivel"), "unidad": "M€"},
            "filas": filas,
        },
    }
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ok", SALIDA, len(filas), "ccaa; paro", len(paro), "pob", len(pob))


if __name__ == "__main__":
    main()
