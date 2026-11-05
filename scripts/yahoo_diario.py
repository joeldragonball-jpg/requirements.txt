"""Cierres diarios de Yahoo Finance con la fecha de la SESIÓN (hora de la bolsa), no la de la descarga (C132, 5-nov-2026).

Problema que arregla: Yahoo deja a veces vacía o sin actualizar la barra del día y pone la cotización en vivo con su hora UTC.
El 4-nov-2026 el Brent salía a la vez como 104,06 $ «del 4-nov» (barra vieja) y 94,89 $ «del 5-nov» (las 00:12 UTC, que en
Nueva York aún era el 4-nov). Aquí cada cierre se fecha con el desfase horario de la bolsa (meta.gmtoffset) y el último
valor se sustituye por meta.regularMarketPrice cuando es de la misma sesión o posterior.
"""
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
    return sorted(por_dia.items())
