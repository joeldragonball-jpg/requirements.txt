"""Exposición soberana por banco (ejercicio de transparencia de la EBA, edición 2025) -> explorador/bancos-eba.json.

Sin IA. Baja los CSV de la EBA (el de soberanos pesa ~90 MB), así que se ejecuta A MANO cuando la EBA publique datos nuevos:
    uv run --with pandas --with openpyxl python scripts/preparar_bancos_eba.py
Fechas de referencia de la edición 2025: 30-sep-2024, 31-dic-2024, 31-mar-2025 y 30-jun-2025. La EBA dice que el ejercicio se
interrumpe desde junio de 2025 y remite al Pillar 3 Data Hub, así que 30-jun-2025 es el último corte de este conjunto.
Importes en millones de euros (valor contable bruto de activos financieros no derivados; "Direct exposures - On balance sheet").
"""
import json
import sys
import urllib.request
from pathlib import Path

import pandas as pd

BASE = "https://www.eba.europa.eu/assets/TE2025/Full_database/883401/"
TMP = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("eba_tmp")
SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "bancos-eba.json"
PERIODO, ANTERIOR = "202506", "202412"
ITEM_SOB, ITEM_CET1 = "2520810", "2520102"
ES_NOMBRE = {"Spain": "España", "France": "Francia", "Italy": "Italia", "Germany": "Alemania", "United States": "EE. UU.", "United Kingdom": "Reino Unido",
             "China": "China", "Japan": "Japón", "Netherlands": "Países Bajos", "Belgium": "Bélgica", "Portugal": "Portugal", "Austria": "Austria",
             "Ireland": "Irlanda", "Greece": "Grecia", "Poland": "Polonia", "Sweden": "Suecia", "Denmark": "Dinamarca", "Finland": "Finlandia",
             "Luxembourg": "Luxemburgo", "Czech Republic": "Chequia", "Hungary": "Hungría", "Romania": "Rumanía", "Norway": "Noruega", "Turkey": "Turquía",
             "Brazil": "Brasil", "Mexico": "México", "Switzerland": "Suiza", "Canada": "Canadá", "Russia": "Rusia", "Cyprus": "Chipre",
             "Slovakia": "Eslovaquia", "Slovenia": "Eslovenia", "Croatia": "Croacia", "Lithuania": "Lituania", "Latvia": "Letonia", "Malta": "Malta",
             "Iceland": "Islandia", "Latin America and the Caribbean": "Latinoamérica y Caribe (agregado)", "Other advanced economies non EEA": "Otras economías avanzadas fuera del EEE (agregado)",
             "Other Central and eastern Europe countries non EEA": "Otros países de Europa central y oriental fuera del EEE (agregado)", "Asia": "Asia (agregado)",
             "Africa": "África (agregado)", "Middle East": "Oriente Medio (agregado)", "Other": "Otros (agregado)", "Oceania": "Oceanía (agregado)"}
PRIORIDAD = {"28": "ES", "9": "FR", "15": "IT", "10": "DE", "37": "JP", "43": "US", "33": "CN", "30": "GB"}


def bajar(nombre):
    TMP.mkdir(exist_ok=True)
    ruta = TMP / nombre
    if not ruta.exists():
        req = urllib.request.Request(BASE + nombre, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=300) as r, open(ruta, "wb") as f:
            f.write(r.read())
    return ruta


def main():
    sov = pd.read_csv(bajar("tr_sov.csv"), dtype=str)
    oth = pd.read_csv(bajar("tr_oth.csv"), dtype=str)
    meta = bajar("TR_Metadata.xlsx")
    bancos = pd.read_excel(meta, "List of Institutions", header=1)
    paises = pd.read_excel(meta, "Country")
    nombre_pais = {str(k): ES_NOMBRE.get(v, v) for k, v in zip(paises["Country"], paises["Label"])}
    sov["Amount"] = pd.to_numeric(sov["Amount"], errors="coerce")
    oth["Amount"] = pd.to_numeric(oth["Amount"], errors="coerce")

    s = sov[(sov.Item == ITEM_SOB) & (sov.Maturity == "8") & (sov.Accounting_portfolio == "0")]
    cet = oth[(oth.Item == ITEM_CET1) & (oth.Sheet == "Capital")]
    activos = oth[(oth.Label.str.upper() == "TOTAL ASSETS") & (oth.Sheet == "Assets")]
    out = []
    for _, b in bancos.iterrows():
        lei = b["LEI_Code"]
        fila = {"lei": lei, "nombre": str(b["Name"]).strip(), "pais": b["Country"], "pais_nombre": b["Desc_country"]}
        for tag, per in (("", PERIODO), ("_ant", ANTERIOR)):
            d = s[(s.LEI_Code == lei) & (s.Period == per)].groupby("Country").Amount.sum()
            if d.empty:
                fila["total" + tag] = None
                continue
            fila["total" + tag] = round(float(d.sum()), 0)
            if tag == "":
                fila["por_pais"] = {nombre_pais.get(k, k): round(float(v), 0) for k, v in d.sort_values(ascending=False).head(8).items() if v > 0}
                fila["prioridad"] = {iso: round(float(d.get(k, 0.0)), 0) for k, iso in PRIORIDAD.items()}
            else:
                fila["prioridad_ant"] = {iso: round(float(d.get(k, 0.0)), 0) for k, iso in PRIORIDAD.items()}
        c = cet[(cet.LEI_Code == lei) & (cet.Period == PERIODO)].Amount
        fila["cet1"] = round(float(c.iloc[0]), 0) if len(c) else None
        a = activos[(activos.LEI_Code == lei) & (activos.Period == PERIODO)].Amount
        fila["activos"] = round(float(a.iloc[0]), 0) if len(a) else None
        if fila.get("total"):
            fila["total_sobre_cet1"] = round(fila["total"] / fila["cet1"], 2) if fila["cet1"] else None
            fila["total_sobre_activos"] = round(100 * fila["total"] / fila["activos"], 1) if fila["activos"] else None
            casa = fila["prioridad"].get(b["Country"])
            fila["nacional_pct"] = round(100 * casa / fila["total"], 1) if casa is not None else None
        out.append(fila)
    datos = {
        "fuente": "EBA, ejercicio de transparencia de la UE 2025 (tr_sov.csv, tr_oth.csv, TR_Metadata.xlsx)",
        "url": "https://www.eba.europa.eu/eu-wide-transparency-exercise-0",
        "periodo": "2025-06-30", "periodo_ant": "2024-12-31", "unidad": "millones de euros",
        "nivel": "P",
        "nota": "Exposición directa en balance a deuda soberana: valor contable bruto de los activos financieros no derivados frente a cada país emisor, al mayor nivel de consolidación. "
                "El importe por país incluye bonos y préstamos y NO es solo deuda negociable; el alcance exacto de «soberano» (administraciones centrales, regionales y locales; bancos centrales) está en la guía de la EBA [VERIFICAR]. "
                "La EBA interrumpe el ejercicio desde junio de 2025: este es el último corte de este conjunto.",
        "bancos": [x for x in out if x.get("total")],
    }
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(datos['bancos'])} bancos con datos de {len(out)} en la lista -> {SALIDA}")


if __name__ == "__main__":
    main()
