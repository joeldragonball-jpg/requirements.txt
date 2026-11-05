"""Cierres diarios de Yahoo Finance con la fecha de la SESIÓN (hora de la bolsa), no la de la descarga (C132, 5-nov-2026).

Problema que arregla: Yahoo deja a veces vacía o sin actualizar la barra del día y pone la cotización en vivo con su hora UTC.
El 4-nov-2026 el Brent salía a la vez como 104,06 $ «del 4-nov» (barra vieja) y 94,89 $ «del 5-nov» (las 00:12 UTC, que en
Nueva York aún era el 4-nov). Aquí cada cierre se fecha con el desfase horario de la bolsa (meta.gmtoffset) y el último
valor se sustituye por meta.regularMarketPrice cuando es de la misma sesión o posterior.
"""
import math
from datetime import datetime, timedelta, timezone


def _dia(ts, desfase):
    return (datetime.fromtimestamp(ts, timezone.utc) + timedelta(seconds=desfase)).strftime("%Y-%m-%d")


def cierres(resultado):
    """[(fecha_sesión, cierre), …] sin huecos ni fechas repetidas; el último par es el precio de mercado más reciente."""
    meta = resultado.get("meta") or {}
    desfase = int(meta.get("gmtoffset") or 0)
    por_dia = {}
    for ts, c in zip(resultado.get("timestamp") or [], ((resultado.get("indicators") or {}).get("quote") or [{}])[0].get("close") or []):
        if ts and c:
            por_dia[_dia(ts, desfase)] = c          # si una sesión sale dos veces, gana la última barra
    precio, hora = meta.get("regularMarketPrice"), meta.get("regularMarketTime")
    if precio and hora:
        dia = _dia(hora, desfase)
        if not por_dia or dia >= max(por_dia):
            por_dia[dia] = precio
    pares = sorted(por_dia.items())
    # solo acciones y ETF tienen splits; el VIX, los futuros, las divisas y la cripto pueden doblar su valor en un día sin que sea un split
    return sin_splits(pares) if (meta.get("instrumentType") or "") in ("EQUITY", "ETF") else pares


SPLITS = (2, 3, 4, 5, 6, 7, 8, 10, 15, 20)


def sin_splits(pares):
    """Deja la serie en las unidades del ÚLTIMO cierre cuando Yahoo mezcla cierres con y sin ajustar por un split (C142, 5-nov-2026).

    Caso real: SOXX hizo un split 3:1 el 5-nov-2026 y la serie traía 157,17 (ajustado), 453,65, 465,00 y 450,41 (sin ajustar) y 131,90:
    el «cambio de un día» salía -70,7 % cuando el real era -12 %. Se recorre la serie hacia atrás; si entre dos cierres seguidos el cociente se
    parece (±12 %) a 2, 3, 4, 5… (o a 1/2, 1/3…), se entiende que hay un salto de unidades y se reescala lo anterior. Una subida o bajada real
    de más del 40 % en un día en un valor o ETF es tan rara que se prefiere esta lectura."""
    if len(pares) < 2:
        return pares
    esc, salida = 1.0, [pares[-1]]
    siguiente = pares[-1][1]
    for fecha, c in reversed(pares[:-1]):
        rho = siguiente / (c * esc)
        mejor = min(((abs(math.log(rho * k)), 1 / k) for k in SPLITS), default=None)      # bajada de unidades: rho ≈ 1/k
        mejor2 = min(((abs(math.log(rho / k)), k) for k in SPLITS), default=None)         # subida de unidades: rho ≈ k
        for desvio, factor in sorted(x for x in (mejor, mejor2) if x):
            k = factor if factor > 1 else 1 / factor
            if desvio <= (0.14 if k == 2 else 0.22):     # un split se mezcla con el movimiento real de ese día (aquí -12 %)
                esc *= factor
            break
        valor = c * esc
        salida.append((fecha, valor))
        siguiente = valor
    return sorted(salida)
