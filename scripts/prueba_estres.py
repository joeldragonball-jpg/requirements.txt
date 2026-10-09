"""Prueba de estrés histórica de una mezcla XRP/XLM con datos públicos (Yahoo Finance). Sin IA, sin claves.

Uso:  python scripts/prueba_estres.py [peso_XRP]      (por defecto 0.80; el resto va a XLM)
Escribe informes/dossiers/2026-10-09-prueba-de-estres.md. Solo informa del pasado: no predice ni recomienda.
"""
import sys
import time
from pathlib import Path

import warnings

import numpy as np
import pandas as pd
import requests

warnings.filterwarnings("ignore")

SIMBOLOS = {"XRP": "XRP-USD", "XLM": "XLM-USD", "BTC": "BTC-USD", "NASDAQ": "^IXIC", "DXY": "DX-Y.NYB",
            "US10Y": "^TNX", "BRENT": "BZ=F", "ORO": "GC=F"}
SALIDA = Path(__file__).resolve().parent.parent / "informes" / "dossiers" / "2026-10-09-prueba-de-estres.md"


def bajar():
    cols = {}
    for k, v in SIMBOLOS.items():
        j = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{v}", params={"range": "10y", "interval": "1d"},
                         headers={"User-Agent": "Mozilla/5.0"}, timeout=30).json()["chart"]["result"][0]
        s = pd.Series(j["indicators"]["quote"][0]["close"], index=pd.to_datetime(j["timestamp"], unit="s").normalize()).dropna()
        cols[k] = s[~s.index.duplicated(keep="last")]
        time.sleep(0.5)
    return pd.DataFrame(cols)


def caida_max(s):
    dd = s / s.cummax() - 1
    suelo = dd.idxmin()
    pico = s[:suelo].idxmax()
    rec = s[suelo:][s[suelo:] >= s[pico]]
    return dd.min(), pico.date(), suelo.date(), (str(rec.index[0].date()) if len(rec) else "no recuperado")


def pct(x, dec=1):
    return f"{x * 100:.{dec}f} %".replace(".", ",")


def main():
    wx = float(sys.argv[1]) if len(sys.argv) > 1 else 0.80
    d = bajar()
    c = d[["XRP", "XLM"]].dropna()
    r = c.pct_change().dropna()
    mezcla_r = r["XRP"] * wx + r["XLM"] * (1 - wx)
    mezcla = (1 + mezcla_r).cumprod()
    hoy = d.index[-1].date()
    f_ini = c.index[0].date()
    L = []
    L += [f"# Dossier: Prueba de estrés histórica de una mezcla XRP/XLM ({hoy:%d-%m-%Y})", "",
          "> Informativo. No es recomendación de compra ni venta, ni una predicción: **describe qué pasó en el pasado**. "
          f"Datos: cierres diarios en USD de Yahoo Finance (fuente no oficial, secundaria) desde {f_ini:%d-%m-%Y} (inicio de datos de XRP y XLM) hasta {hoy:%d-%m-%Y}. "
          f"Mezcla de ejemplo: **{wx * 100:.0f} % XRP / {(1 - wx) * 100:.0f} % XLM**, rebalanceada cada día (un supuesto: en la práctica nadie rebalancea a diario). "
          "Sin comisiones ni impuestos y en dólares (tu coste real está en euros). Se calcula con `scripts/prueba_estres.py` (sin IA).", "",
          "## 1. Resumen ejecutivo"]
    mdd = {k: caida_max(s) for k, s in {"XRP": c["XRP"], "XLM": c["XLM"], "BTC": d["BTC"].dropna(), "Mezcla": mezcla}.items()}
    vol = {k: s.pct_change().std() * np.sqrt(365) for k, s in {"XRP": c["XRP"], "XLM": c["XLM"], "BTC": d["BTC"].dropna(), "Mezcla": mezcla}.items()}
    act = {k: s.iloc[-1] / s.max() - 1 for k, s in {"XRP": c["XRP"], "XLM": c["XLM"], "BTC": d["BTC"].dropna(), "Mezcla": mezcla}.items()}
    L += [f"1. **La mezcla ha llegado a perder {pct(-mdd['Mezcla'][0], 0)} desde su máximo** (pico {mdd['Mezcla'][1]:%d-%m-%Y}, suelo {mdd['Mezcla'][2]:%d-%m-%Y}). XRP y XLM tardaron años en recuperar algo: XRP lo hizo el {mdd['XRP'][3]}; XLM, {mdd['XLM'][3]}.",
          f"2. **Hoy** están a {pct(act['XRP'], 0)} (XRP) y {pct(act['XLM'], 0)} (XLM) de su máximo histórico (BTC: {pct(act['BTC'], 0)}).",
          f"3. **Volatilidad anualizada** de la mezcla: {pct(vol['Mezcla'], 0)} (BTC: {pct(vol['BTC'], 0)}). Un día con caída superior al 10 % ocurrió {int((mezcla_r < -0.10).sum())} veces en {len(mezcla_r)} días.",
          f"4. **Repartir entre XRP y XLM casi no reduce el riesgo**: su correlación diaria es de {str(round(r['XRP'].corr(r['XLM']),2)).replace('.',',')} y la caída máxima es parecida en cualquier reparto (§4).",
          "5. **Con qué se mueve (§5):** la mezcla sigue sobre todo a BTC; con Nasdaq, dólar, Brent y tipos las correlaciones semanales son bajas o moderadas [lee la tabla: depende del periodo].",
          "6. **Esto es historia, no destino.** El pasado incluye la burbuja de 2017-18 y un caso judicial de XRP; el futuro puede no repetirse en ninguna dirección.", ""]
    L += ["## 2. Caída máxima y recuperación (cierres diarios)", "",
          "| Activo | Caída máxima | Pico | Suelo | Recupera el pico |", "|---|---|---|---|---|"]
    for k, (dm, p, s, rec) in mdd.items():
        L.append(f"| {k} | {pct(dm)} | {p:%d-%m-%Y} | {s:%d-%m-%Y} | {rec} |")
    L += ["", f"Nota: la mezcla rebalanceada a diario tiene un efecto estadístico (\"ganar vendiendo lo que sube\") que puede hacerla parecer mejor que lo que obtendría quien no rebalancea. XLM no ha vuelto a su máximo de {mdd['XLM'][1]:%Y}.", ""]
    L += ["## 3. Peores ventanas de la mezcla y qué pasó", "", "| Ventana | Peor caída | Terminó | Mediana | Percentil 5 |", "|---|---|---|---|---|"]
    for n, lab in [(7, "7 días"), (30, "30 días"), (90, "90 días"), (365, "365 días")]:
        rr = mezcla.pct_change(n).dropna()
        L.append(f"| {lab} | {pct(rr.min())} | {rr.idxmin():%d-%m-%Y} | {pct(rr.median())} | {pct(rr.quantile(.05))} |")
    sem = mezcla.pct_change(7).dropna()
    f7 = sem.idxmin()
    f30, f90 = mezcla.pct_change(30).idxmin(), mezcla.pct_change(90).idxmin()
    nota = ("coincide con diciembre de 2020, cuando la SEC demandó a Ripple (ver [dossier 10](2026-10-09-ripple-la-empresa.md)): una caída "
            "ligada a una noticia concreta de XRP, no al mercado en general [VERIFICAR la relación causal día a día]"
            if pd.Timestamp("2020-12-15") <= f7 <= pd.Timestamp("2020-12-31") else "causa no analizada [VERIFICAR]")
    L += ["", f"- **Peor semana (termina el {f7:%d-%m-%Y}):** {nota}.",
          f"- **Peor mes y peor trimestre:** terminan el {f30:%d-%m-%Y} y el {f90:%d-%m-%Y}.", ""]
    L += ["## 4. ¿Cambia el reparto entre XRP y XLM el riesgo?", "", "| Reparto | Caída máxima | Volatilidad anual |", "|---|---|---|"]
    for a in (1, wx, 0.5, 0):
        m = r["XRP"] * a + r["XLM"] * (1 - a)
        L.append(f"| {a * 100:.0f} % XRP / {(1 - a) * 100:.0f} % XLM | {pct(caida_max((1 + m).cumprod())[0])} | {pct(m.std() * np.sqrt(365), 0)} |")
    L += ["", "Lectura: son dos activos muy parecidos en comportamiento (mismo sector, mismas fases del mercado). **No es diversificación en el sentido habitual**; para reducir el riesgo habría que mirar activos de otra naturaleza, algo que este dossier no evalúa.", ""]
    sem_d = d.resample("W-FRI").last()
    wr = sem_d.pct_change()
    wr["US10Y"] = sem_d["US10Y"].diff()
    wr["Mezcla"] = mezcla.resample("W-FRI").last().pct_change()
    L += ["## 5. Con qué se mueve (correlación de retornos semanales)", "",
          "| Periodo | Nasdaq | Dólar (DXY) | Tipo a 10 años (Δ pp) | Brent | Oro | BTC | Semanas |", "|---|---|---|---|---|---|---|---|"]
    for lab, (a, b) in {"Todo el histórico": (str(c.index[0].date()), str(hoy)), "Ciclo de subidas 2022-23": ("2022-03-16", "2023-07-26"),
                        "Últimos 12 meses": (str(pd.Timestamp(hoy) - pd.DateOffset(months=12))[:10], str(hoy)),
                        "Últimos 6 meses": (str(pd.Timestamp(hoy) - pd.DateOffset(months=6))[:10], str(hoy))}.items():
        x = wr[a:b].dropna(subset=["Mezcla"])
        v = lambda k: f"{x['Mezcla'].corr(x[k]):.2f}".replace(".", ",")
        L.append(f"| {lab} | {v('NASDAQ')} | {v('DXY')} | {v('US10Y')} | {v('BRENT')} | {v('ORO')} | {v('BTC')} | {len(x)} |")
    x = wr[str(pd.Timestamp(hoy) - pd.DateOffset(months=12))[:10]:].dropna(subset=["Mezcla", "BTC", "NASDAQ"])
    bb = np.cov(x.Mezcla, x.BTC)[0, 1] / np.var(x.BTC, ddof=1)
    bn = np.cov(x.Mezcla, x.NASDAQ)[0, 1] / np.var(x.NASDAQ, ddof=1)
    L += ["", f"Beta semanal de los últimos 12 meses: **{str(round(bb,2)).replace('.',',')}** frente a BTC y **{str(round(bn,2)).replace('.',',')}** frente al Nasdaq (por cada 1 % que se mueve BTC, la mezcla se movió de media ~{str(round(bb,2)).replace('.',',')} % en el mismo sentido). "
          "Correlación no es causalidad, y con pocas semanas (50-70) el dato es poco estable.", ""]
    L += ["## 6. Qué habría perdido la mezcla en esos episodios (porcentajes, no importes)", "", "| Episodio histórico | Variación de la mezcla | Un 100 pasaría a |", "|---|---|---|"]
    for lab, v in [("Peor semana", mezcla.pct_change(7).min()), ("Peor mes (30 días)", mezcla.pct_change(30).min()), ("Peor trimestre (90 días)", mezcla.pct_change(90).min()),
                   ("Peor año (365 días)", mezcla.pct_change(365).min()), ("Caída máxima desde el pico", mdd["Mezcla"][0])]:
        L.append(f"| {lab} | {pct(v)} | {100 * (1 + v):.0f} |")
    L += ["", "Para convertirlo a euros: multiplica el porcentaje por el valor de tu cartera. Es un **escenario histórico**, no un pronóstico ni un máximo posible.", ""]
    L += ["## 7. Límites y sesgos", "- **Pasado corto y atípico:** XRP y XLM tienen menos de 9 años de datos y una burbuja (2017-18) que domina las peores cifras.",
          "- **Datos:** Yahoo Finance agrega precios de varias plataformas; los cierres de un día pueden diferir del de Kraken.",
          "- **Dólares frente a euros:** tu rentabilidad real depende del tipo EUR/USD, que aquí no se aplica.",
          "- **No incluye** comisiones, impuestos, liquidez al vender ni el riesgo de custodia.",
          "- **No es recomendación**: no dice qué hacer con tu cartera, solo cuánto se ha movido en el pasado.", "",
          "## 8. Lo que no sé", "- Si el futuro se parecerá a algún tramo de este histórico.", "- La causa exacta de cada caída (solo he señalado una).",
          "- El efecto real de rebalancear con costes y la liquidez en los momentos de caída fuerte.", ""]
    SALIDA.write_text("\n".join(L), encoding="utf-8")
    print("Escrito", SALIDA)


if __name__ == "__main__":
    main()
