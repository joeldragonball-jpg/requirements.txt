"""C116: defunciones semanales de España (INE, EDeS, serie EDES52) y exceso de mortalidad estimado, sin descargar el CSV de MoMo (724 MB).
Sin IA y sin claves. Salida: explorador/espana-mortalidad.json.

La tabla 6552 del INE (indicada en la tarea) es de mortalidad infantil por edad; el total semanal sale de la operación EDeS (tabla 35177).
Exceso = defunciones de la semana − media de esa misma semana en el periodo de referencia. NO es el exceso oficial del MoMo (ISCIII), que usa
un modelo con temperatura y edad; aquí no se corrige por envejecimiento, así que el exceso sale algo alto de forma estructural.

Uso:  python scripts/leer_mortalidad_ine.py
"""
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SALIDA = Path(__file__).resolve().parent.parent / "explorador" / "espana-mortalidad.json"
URL = "https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/EDES52?nult=800&det=2"
SEMANAS_MOSTRAR = 26


def media(v):
    return sum(v) / len(v)


def main():
    previo = {}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    try:
        with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "cartera-joel/1.0 (uso personal)"}), timeout=90) as r:
            datos = json.loads(r.read().decode("utf-8", "replace"))["Data"]
        ahora = datetime.now(timezone.utc).timestamp() * 1000
        sem = {}
        for d in datos:
            if d.get("Valor") and d["Valor"] > 0 and d["Fecha"] <= ahora:
                sem[(d["Anyo"], d["Periodo"]["Valor"])] = (d["Valor"], d["TipoDato"]["Nombre"], datetime.fromtimestamp(d["Fecha"] / 1000, timezone.utc).strftime("%Y-%m-%d"))
        if len(sem) < 300:
            raise ValueError(f"solo {len(sem)} semanas con dato")
        ult = sorted(sem)[-SEMANAS_MOSTRAR:]
        anio_actual = ult[-1][0]
        ref_pre = range(2015, 2020)
        ref_rec = [a for a in range(anio_actual - 5, anio_actual) if a != 2020]
        filas = []
        for a, s in ult:
            v, tipo, fecha = sem[(a, s)]
            b1 = [sem[(y, s)][0] for y in ref_pre if (y, s) in sem]
            b2 = [sem[(y, s)][0] for y in ref_rec if (y, s) in sem]
            fila = {"anio": a, "semana": s, "fecha": fecha, "defunciones": v, "tipo_dato": tipo.lower()}
            if len(b1) >= 4:
                fila["media_2015_2019"] = round(media(b1))
                fila["exceso_vs_2015_2019"] = round(v - media(b1))
            if len(b2) >= 3:
                fila["media_5_anios_previos"] = round(media(b2))
                fila["exceso_vs_5_anios"] = round(v - media(b2))
            filas.append(fila)
        acum = [f for f in filas if f["anio"] == anio_actual]
        resumen = {k: sum(f[k] for f in acum if k in f) for k in ("exceso_vs_2015_2019", "exceso_vs_5_anios")}
        salida = {"titulo": "España: defunciones semanales y exceso estimado", "leido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "nivel": "P",
                  "fuente": "https://www.ine.es/jaxiT3/Tabla.htm?t=35177", "serie": "EDES52 (Total nacional, todas las edades)", "desde": min(a for a, _ in sem),
                  "semanas": filas, "resumen_anio_en_curso": {"anio": anio_actual, "semanas": len(acum), **resumen},
                  "referencias": {"2015_2019": "media de la misma semana en 2015-2019 (antes de la pandemia)", "5_anios_previos": f"media de la misma semana en {ref_rec[0]}-{ref_rec[-1]} sin 2020"},
                  "nota": "Estimación del INE (EDeS): las semanas recientes son provisionales y se revisan. Exceso sin corregir por envejecimiento ni temperatura: no es el exceso oficial "
                          "del MoMo (ISCIII). Para el oficial haría falta su CSV de 724 MB (descartado); alternativa: leer solo las últimas filas con peticiones HTTP parciales [VERIFICAR si el servidor las admite].",
                  "fallos": []}
    except Exception as e:
        print(f"AVISO (se conserva lo anterior si existía): {type(e).__name__}: {e}")
        if previo:
            previo["fallos"] = [f"{type(e).__name__}: {e}"]
            SALIDA.write_text(json.dumps(previo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return 1
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    u = filas[-1]
    print(f"Última semana {u['anio']}-S{u['semana']}: {u['defunciones']:.0f} defunciones ({u['tipo_dato']}); exceso vs 2015-2019: {u.get('exceso_vs_2015_2019')}, vs 5 años: {u.get('exceso_vs_5_anios')}")
    print("Acumulado del año en las semanas mostradas:", salida["resumen_anio_en_curso"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
