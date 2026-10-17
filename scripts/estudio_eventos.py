#!/usr/bin/env python3
"""Estudio de eventos noticia -> precio (R48) y washouts (R49). Sin IA, sin claves.

Datos: API publica de mercado de Binance (data-api.binance.vision), pares XRPUSDT, XLMUSDT, BTCUSDT.
Velas de 1 h (serie 2023-01-01 -> hoy) y de 1 min (solo en los instantes de cada evento). Funding: fapi.binance.com.
Los precios son USDT, no USD: la base USDT/USD es otra fuente de diferencia frente a CoinGecko.

Uso:
  python scripts/estudio_eventos.py eventos  [--cache DIR] [--out DIR]
  python scripts/estudio_eventos.py washouts [--cache DIR] [--out DIR]
"""
import argparse, bisect, csv, datetime as dt, json, math, os, statistics, sys, tempfile, time, urllib.request

BASE = "https://data-api.binance.vision/api/v3/klines"
FUND = "https://fapi.binance.com/fapi/v1/fundingRate"
PAIRS = {"XRP": "XRPUSDT", "XLM": "XLMUSDT", "BTC": "BTCUSDT"}
START = dt.datetime(2023, 1, 1, tzinfo=dt.timezone.utc)
H = 3600_000


def ms(s):  # "2025-10-10 20:50" (UTC) -> ms
    return int(dt.datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=dt.timezone.utc).timestamp() * 1000)


def utc(m):
    return dt.datetime.fromtimestamp(m / 1000, dt.timezone.utc)


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "estudio-eventos"}), timeout=30) as r:
                return json.load(r)
        except Exception:
            time.sleep(1.5 * (i + 1))
    raise RuntimeError("fallo al leer " + url)


# ---------- datos ----------
def hourly(sym, cache):
    f = os.path.join(cache, f"h_{sym}.json")
    rows = json.load(open(f)) if os.path.exists(f) else []
    t = rows[-1][0] + H if rows else int(START.timestamp() * 1000)
    now = int(time.time() * 1000)
    while t < now - H:
        b = get(f"{BASE}?symbol={sym}&interval=1h&startTime={t}&limit=1000")
        if not b:
            break
        rows += [[int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4])] for k in b]
        t = int(b[-1][0]) + H
    # quita la vela en curso
    rows = [r for r in rows if r[0] + H <= now]
    json.dump(rows, open(f, "w"))
    return rows


def price_at(sym, t, cache):
    """Cierre de la vela de 1 min que termina en t (precio en t)."""
    f = os.path.join(cache, "m_" + sym + ".json")
    d = json.load(open(f)) if os.path.exists(f) else {}
    k = str(t)
    if k not in d:
        b = get(f"{BASE}?symbol={sym}&interval=1m&startTime={t - 60000}&limit=1")
        if not b or int(b[0][0]) != t - 60000:
            d[k] = None
        else:
            d[k] = float(b[0][4])
        json.dump(d, open(f, "w"))
    return d[k]


def funding(sym, cache):
    f = os.path.join(cache, f"f_{sym}.json")
    rows = json.load(open(f)) if os.path.exists(f) else []
    t = rows[-1][0] + 1 if rows else int(START.timestamp() * 1000)
    now = int(time.time() * 1000)
    while t < now:
        b = get(f"{FUND}?symbol={sym}&startTime={t}&limit=1000")
        if not b:
            break
        rows += [[int(x["fundingTime"]), float(x["fundingRate"])] for x in b]
        t = rows[-1][0] + 1
        if len(b) < 1000:
            break
    json.dump(rows, open(f, "w"))
    return rows


# ---------- eventos (hora UTC; 'prec' = tipo de fuente de la hora) ----------
# prec: A = hora de calendario oficial (Fed/BLS/Senado/mercado); B = hora aproximada o desconocida (ventana +1 h NO fiable)
EVENTOS = [
    ("E01", "2025-03-19 18:00", "A", "FOMC mantiene tipos (14:00 ET)", "federalreserve.gov (calendario FOMC)", "ambos", "macro"),
    ("E02", "2025-08-22 14:00", "A", "Powell en Jackson Hole (10:00 ET)", "federalreserve.gov (discurso)", "ambos", "macro"),
    ("E03", "2025-09-17 18:00", "A", "FOMC baja 25 pb (14:00 ET)", "federalreserve.gov (comunicado FOMC)", "ambos", "macro"),
    ("E04", "2025-10-29 18:00", "A", "FOMC baja 25 pb y fin del QT (14:00 ET)", "federalreserve.gov (comunicado FOMC)", "ambos", "macro"),
    ("E05", "2025-12-10 19:00", "A", "FOMC (14:00 ET)", "federalreserve.gov (calendario FOMC)", "ambos", "macro"),
    ("E06", "2026-09-16 18:00", "A", "FOMC sube 25 pb a 3,75-4,00 % (14:00 ET)", "federalreserve.gov (comunicado FOMC)", "ambos", "macro"),
    ("E07", "2026-10-02 12:30", "A", "Empleo EE. UU. +29.000 (esperado ~89.000) (08:30 ET)", "bls.gov (calendario)", "ambos", "macro"),
    ("E08", "2026-10-07 18:00", "A", "Minutas del FOMC del 16-sep (14:00 ET)", "federalreserve.gov (minutas)", "ambos", "macro"),
    ("E09", "2026-10-14 12:30", "A", "IPC sept 3,7 % a/a, subyacente 0,3 % m/m (08:30 ET)", "bls.gov (IPC)", "ambos", "macro"),
    ("E10", "2026-10-15 12:30", "A", "PPI sept +1,3 % m/m (08:30 ET)", "bls.gov (PPI)", "ambos", "macro"),
    ("E11", "2026-09-15 18:18", "A", "Senado: cloture CLARITY Act fracasa 49-50 (votacion abierta 14:18 ET, resultado 15:00 ET)", "Senate floor log (via prensa)", "ambos", "regulacion"),
    ("E12", "2026-10-12 13:30", "A", "XRPN (Evernorth) empieza a cotizar en Nasdaq (apertura 09:30 ET)", "SEC EDGAR 8-K; Nasdaq", "XRP", "ETF/tesoreria"),
    ("E13", "2025-11-13 14:30", "A", "Debut del primer ETF spot de XRP (Canary XRPC, Nasdaq, apertura 09:30 ET)", "Canary / SEC 8-A (via prensa)", "XRP", "ETF/tesoreria"),
    ("E14", "2026-10-09 09:34", "A", "XRPL: mayoria de validadores para fixCleanup3_4_0 (09:34:30 UTC en el ledger)", "ledger XRPL (R32)", "XRP", "red/tecnologia"),
    ("E15", "2023-07-13 14:00", "B", "Sentencia Torres: XRP no es valor en ventas programaticas (hora aprox., +-2 h)", "CourtListener SEC v. Ripple (hora exacta sin verificar)", "XRP", "demanda"),
    ("E16", "2025-03-02 15:00", "B", "Trump cita XRP, SOL y ADA en la reserva estrategica (hora del 1.er post sin verificar; se usa 15:00 UTC porque XRP estaba plano hasta esa hora y el salto aparece en la vela de 16:00)", "Truth Social (via Fortune/Bloomberg)", "ambos", "politica/anuncio"),
    ("E17", "2025-10-10 20:50", "B", "Trump anuncia arancel adicional del 100 % a China (hora segun una cronologia; otra daba 10:57 ET el primer aviso)", "Truth Social (via prensa)", "ambos", "politica/anuncio"),
    ("E18", "2025-08-07 12:00", "B", "SEC y Ripple desisten de los recursos (dia conocido; hora desconocida: se usa 12:00 UTC)", "CourtListener 2.o Circuito (via Bloomberg Law)", "XRP", "demanda"),
    ("E19", "2026-05-27 14:00", "B", "DTCC anuncia tokenizar activos de DTC en Stellar (dia conocido; hora desconocida: se usa 14:00 UTC)", "dtcc.com (nota no leida; via prensa)", "XLM", "tradfi/tokenizacion"),
]

FOMC = ["2023-02-01", "2023-03-22", "2023-05-03", "2023-06-14", "2023-07-26", "2023-09-20", "2023-11-01", "2023-12-13",
        "2024-01-31", "2024-03-20", "2024-05-01", "2024-06-12", "2024-07-31", "2024-09-18", "2024-11-07", "2024-12-18",
        "2025-01-29", "2025-03-19", "2025-05-07", "2025-06-18", "2025-07-30", "2025-09-17", "2025-10-29", "2025-12-10",
        "2026-01-28", "2026-03-18", "2026-04-29", "2026-06-17", "2026-07-29", "2026-09-16", "2026-10-28", "2026-12-09"]


# ---------- estadistica ----------
def series(rows):
    ts = [r[0] for r in rows]
    cl = [r[4] for r in rows]
    return ts, cl


def lr(a, b):
    return math.log(b / a)


def beta_of(cx, cb):
    n = min(len(cx), len(cb))
    rx = [lr(cx[i - 1], cx[i]) for i in range(1, n)]
    rb = [lr(cb[i - 1], cb[i]) for i in range(1, n)]
    mb, mx = statistics.fmean(rb), statistics.fmean(rx)
    cov = sum((a - mb) * (b - mx) for a, b in zip(rb, rx))
    var = sum((a - mb) ** 2 for a in rb)
    return cov / var


def base_dist(cx, cb, beta, step):
    """Exceso (log) sobre BTC*beta en ventanas solapadas de 'step' horas."""
    out, raw = [], []
    for i in range(step, len(cx)):
        rx, rb = lr(cx[i - step], cx[i]), lr(cb[i - step], cb[i])
        out.append(abs(rx - beta * rb))
        raw.append(abs(rx))
    return sorted(out), sorted(raw)


def tail(sorted_vals, x):
    """Proporcion de ventanas con |valor| >= x."""
    i = bisect.bisect_left(sorted_vals, abs(x))
    return (len(sorted_vals) - i) / len(sorted_vals)


def pct(x):
    return None if x is None else (math.exp(x) - 1) * 100


def clasifica(tails, confus1h, confus24, prec):
    """Regla fijada antes de ver los resultados.
    directo probable: cola <=5 % en 1 h (solo si hora tipo A y sin confusor en +-3 h)
                      o cola <=5 % en 24 h sin ningun confusor en la ventana de 24 h;
    dudoso: cola <=5 % pero con confusor, o cola entre 5 y 15 %; sin efecto: resto."""
    t1 = tails.get("1h") if prec == "A" else None
    t24 = tails.get("24h")
    if t1 is not None and t1 <= 0.05 and not confus1h:
        return "efecto directo probable"
    if t24 is not None and t24 <= 0.05 and not confus24:
        return "efecto directo probable"
    m = min([x for x in (t1, t24) if x is not None] or [1])
    if m <= 0.15:
        return "efecto dudoso"
    return "sin efecto detectable"


def eventos_mode(cache, out):
    H1 = {k: hourly(v, cache) for k, v in PAIRS.items()}
    ts, _ = series(H1["BTC"])
    cl = {k: series(H1[k])[1] for k in H1}
    n = min(len(c) for c in cl.values())
    for k in cl:
        cl[k] = cl[k][:n]
    ts = ts[:n]
    bet = {a: beta_of(cl[a], cl["BTC"]) for a in ("XRP", "XLM")}
    bd = {a: {w: base_dist(cl[a], cl["BTC"], bet[a], s) for w, s in (("1h", 1), ("24h", 24), ("7d", 168))} for a in ("XRP", "XLM")}
    print("beta global horaria vs BTC:", {k: round(v, 2) for k, v in bet.items()}, "| barras:", n, utc(ts[0]).date(), "->", utc(ts[-1]).date())
    # volatilidad anualizada (retornos horarios)
    for a in ("XRP", "XLM", "BTC"):
        r = [lr(cl[a][i - 1], cl[a][i]) for i in range(1, n)]
        print(f"vol anual {a}: {statistics.pstdev(r) * math.sqrt(24 * 365) * 100:.0f} %")
    for a in ("XRP", "XLM"):
        for w in ("1h", "24h", "7d"):
            s = bd[a][w][0]
            print(f"base {a} {w}: |exceso| p50={s[len(s)//2]*100:.2f}% p95={s[int(len(s)*.95)]*100:.2f}% p99={s[int(len(s)*.99)]*100:.2f}%")
    fom = set(FOMC)
    res = []
    for eid, when, prec, texto, fuente, activos, tipo in EVENTOS:
        t0 = ms(when)
        d0 = utc(t0)
        pts = {"m24": t0 - 24 * H, "t0": t0, "p1": t0 + H, "p24": t0 + 24 * H, "p7": t0 + 168 * H}
        px = {a: {k: price_at(PAIRS[a], v, cache) for k, v in pts.items()} for a in PAIRS}
        confus = []
        if d0.weekday() >= 5:
            confus.append("fin de semana")
        confus1h = []
        for dd in (d0.date(), (d0 + dt.timedelta(days=1)).date(), (d0 - dt.timedelta(days=1)).date()):
            if dd.isoformat() in fom and eid not in ("E01", "E03", "E04", "E05", "E06"):
                # decision FOMC a las 18:00 UTC (EDT) o 19:00 UTC (EST): dentro de la ventana de 24 h
                dec = dt.datetime.fromisoformat(dd.isoformat() + "T18:00:00+00:00")
                if abs((dec - d0).total_seconds()) <= 24 * 3600:
                    confus.append(f"FOMC {dd.isoformat()}")
                if abs((dec - d0).total_seconds()) <= 3.5 * 3600:
                    confus1h.append("FOMC")
        if d0.day == 1:
            confus.append("dia 1 (escrow Ripple)")
        # inicio observado (descriptivo, no es causa): hora con mayor |exceso| horario en -6..+6 h
        ix = bisect.bisect_left(ts, t0 - t0 % H)
        onset = {}
        for a in ("XRP", "XLM"):
            best = max(range(max(1, ix - 6), min(n, ix + 7)), key=lambda i: abs(lr(cl[a][i - 1], cl[a][i]) - bet[a] * lr(cl["BTC"][i - 1], cl["BTC"][i])))
            onset[a] = (utc(ts[best]).strftime("%m-%d %H:00"), lr(cl[a][best - 1], cl[a][best]) - bet[a] * lr(cl["BTC"][best - 1], cl["BTC"][best]))
        for a in ("XRP", "XLM", "BTC"):
            row = {"id": eid, "activo": a}
            for w, (p0, p1) in {"pre24": ("m24", "t0"), "1h": ("t0", "p1"), "24h": ("t0", "p24"), "7d": ("t0", "p7")}.items():
                x0, x1 = px[a][p0], px[a][p1]
                row[w] = None if (x0 is None or x1 is None) else lr(x0, x1)
            res.append(row | {"prec": prec})
        by = {r["activo"]: r for r in res if r["id"] == eid}
        eventos_out = []
        for a in ("XRP", "XLM"):
            ex, tails = {}, {}
            for w in ("pre24", "1h", "24h", "7d"):
                if by[a][w] is None or by["BTC"][w] is None:
                    ex[w] = None
                    continue
                ex[w] = by[a][w] - bet[a] * by["BTC"][w]
                if w != "pre24":
                    tails[w] = tail(bd[a][w][0], ex[w])
            cl_ = clasifica(tails, confus1h, confus, prec) if activos in (a, "ambos") else "(no aplica: evento de otro activo)"
            eventos_out.append((a, ex, tails, cl_))
            by[a].update({"exceso": ex, "cola": tails, "clase": cl_, "onset": onset[a]})
        # impresion
        print(f"\n{eid} {when} UTC [{prec}] {texto}")
        print("  confusores:", ", ".join(confus) or "ninguno detectado", "| inicio observado (descriptivo):", {a: (o[0], f"{pct(o[1]):+.1f}%") for a, o in onset.items()})
        for a, ex, tails, cl_ in eventos_out + [("BTC", None, None, None)]:
            r = by[a]
            f = lambda v: "  n/d " if v is None else f"{pct(v):+6.1f}%"
            line = f"  {a}: pre24 {f(r['pre24'])} | 1h {f(r['1h'])} | 24h {f(r['24h'])} | 7d {f(r['7d'])}"
            if ex is not None:
                line += f" || exceso 1h {f(ex['1h'])} 24h {f(ex['24h'])} 7d {f(ex['7d'])} | cola 1h {tails.get('1h', float('nan')):.3f} 24h {tails.get('24h', float('nan')):.3f} 7d {tails.get('7d', float('nan')):.3f} | {cl_}"
            print(line)
        for r in (by["XRP"], by["XLM"], by["BTC"]):
            r["confusores"] = confus
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "R48-eventos.json"), "w") as fh:
        json.dump({"beta": bet, "eventos": res}, fh, indent=1, default=str)


# ---------- washouts ----------
def washouts(cache, out, X=0.07, W=6, REC=0.5, RW=12):
    """Criterio fijado antes de buscar: caida >= X (maximo->minimo, usando high/low horarios) en <= W horas y
    recuperacion >= REC de la caida en <= RW horas tras el minimo. Episodios a < 12 h entre minimos se fusionan."""
    H1 = {k: hourly(v, cache) for k, v in PAIRS.items()}
    resultados = {}
    for a in ("XRP", "XLM"):
        rows = H1[a]
        rb = {r[0]: r for r in H1["BTC"]}
        eps = []
        i = 0
        n = len(rows)
        while i < n:
            # busca desde la barra i el maximo de las ultimas W barras y minimo posterior
            hi = rows[i][2]
            best = None
            for j in range(i, min(i + W, n)):
                lo = rows[j][3]
                if hi > 0 and (hi - lo) / hi >= X:
                    best = (j, hi, lo)
                    break
                hi = max(hi, rows[j][2])
            if best is None:
                i += 1
                continue
            j, hi, lo = best
            # el minimo real: sigue mientras baje en las siguientes 3 barras
            k = j
            for m in range(j, min(j + 3, n)):
                if rows[m][3] < lo:
                    lo, k = rows[m][3], m
            drop = (hi - lo) / hi
            rec_max = max(r[2] for r in rows[k + 1:k + 1 + RW]) if k + 1 < n else lo
            rec = (rec_max - lo) / (hi - lo) if hi > lo else 0
            eps.append({"t_min": rows[k][0], "caida": drop, "recup": rec, "es_washout": rec >= REC})
            i = k + RW  # fusiona
        resultados[a] = eps
    return resultados, H1


def washouts_mode(cache, out):
    fund = {a: funding(PAIRS[a], cache) for a in ("XRP", "XLM")}
    summary = {}
    allrows = None
    for X in (0.05, 0.07, 0.10):
        res, H1 = washouts(cache, out, X=X)
        allrows = H1
        n_h = len(H1["XRP"])
        for a in ("XRP", "XLM"):
            w = [e for e in res[a] if e["es_washout"]]
            summary[(a, X)] = (len(res[a]), len(w))
    print("Criterio: caida >= X en <= 6 h (high/low horarios), recuperacion >= 50 % de la caida en <= 12 h tras el minimo.")
    for (a, X), (ne, nw) in summary.items():
        print(f"  {a} X={X*100:.0f} %: episodios de caida {ne}, de ellos washouts {nw}")
    # analisis principal X=7 %
    res, H1 = washouts(cache, out, X=0.07)
    rowsb = {r[0]: r for r in H1["BTC"]}
    n_hours = len(H1["XRP"])
    t_first, t_last = H1["XRP"][0][0], H1["XRP"][-1][0]
    dias = (t_last - t_first) / (24 * H)
    print(f"Serie: {utc(t_first).date()} -> {utc(t_last).date()} ({dias:.0f} dias, {n_hours} horas)")
    # categorias de calendario (por hora UTC del minimo)
    def last_friday(d):
        ld = (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1) - dt.timedelta(days=1)
        while ld.weekday() != 4:
            ld -= dt.timedelta(days=1)
        return ld.date()

    def cats(m):
        d = utc(m)
        c = set()
        if d.weekday() >= 5:
            c.add("fin de semana")
        if d.day == 1:
            c.add("dia 1 (escrow Ripple 00:00 UTC)")
        nxt = (d + dt.timedelta(days=1))
        if nxt.day == 1:
            c.add("ultimo dia del mes")
            if d.month in (3, 6, 9, 12):
                c.add("ultimo dia del trimestre")
        if d.date() == last_friday(d):
            c.add("ultimo viernes del mes (vto. mensual CME)")
        if d.weekday() == 4:
            c.add("viernes (vto. semanal opciones)")
        if (d.month, d.day) in ((2, 14), (5, 15), (8, 14), (11, 14)):
            c.add("plazo 13F (~45 d tras trimestre)")
        if d.date().isoformat() in set(FOMC):
            c.add("dia de decision FOMC")
        return c

    def hora_cat_all():
        cnt = {}
        for r in H1["XRP"]:
            for c in cats(r[0]):
                cnt[c] = cnt.get(c, 0) + 1
        return cnt
    allc = hora_cat_all()
    for a in ("XRP", "XLM"):
        eps = [e for e in res[a] if e["es_washout"]]
        print(f"\n== {a}: {len(eps)} washouts (X=7 %) en {dias/365:.2f} anios = {len(eps)/(dias/365):.1f}/anio ==")
        cc = {}
        for e in eps:
            for c in cats(e["t_min"]):
                cc[c] = cc.get(c, 0) + 1
        for c, tot in sorted(allc.items(), key=lambda x: -x[1]):
            exp = len(eps) * tot / n_hours
            k = cc.get(c, 0)
            # p-valor binomial aproximado (cola superior) para enriquecimiento
            p = tot / n_hours
            pv = 0.0
            for x in range(k, len(eps) + 1):
                pv += math.comb(len(eps), x) * p ** x * (1 - p) ** (len(eps) - x)
            print(f"  {c:48s} observados {k:3d} | esperados al azar {exp:5.1f} | P(>=obs) {pv:.3f}")
        # hora del dia
        hh = [0] * 24
        for e in eps:
            hh[utc(e["t_min"]).hour] += 1
        print("  por hora UTC (0-23):", hh)
        # con BTC
        mk = 0
        det = []
        for e in eps:
            tb = rowsb.get(e["t_min"])
            if not tb:
                continue
            # caida de BTC en las 6 h previas al minimo
            prev = [rowsb[t][2] for t in range(e["t_min"] - 5 * H, e["t_min"] + H, H) if t in rowsb]
            if prev:
                dropb = (max(prev) - tb[3]) / max(prev)
                if dropb >= 0.03:
                    mk += 1
        print(f"  con BTC cayendo >= 3 % en el mismo tramo de 6 h: {mk} de {len(eps)} (los demas serian mas propios del activo)")
        # funding en el minimo (ultimo funding publicado antes del minimo)
        fts = [f[0] for f in fund[a]]
        fv = []
        for e in eps:
            i = bisect.bisect_right(fts, e["t_min"]) - 1
            if i >= 0:
                fv.append(fund[a][i][1])
        if fv:
            allf = [f[1] for f in fund[a]]
            print(f"  funding (perp {PAIRS[a]}) en el ultimo cobro previo al minimo: mediana {statistics.median(fv)*100:.4f} % | mediana de toda la serie {statistics.median(allf)*100:.4f} %  (n={len(fv)})")
        # lista de los 12 mayores
        big = sorted(eps, key=lambda e: -e["caida"])[:12]
        print("  mayores 12 (minimo UTC | caida | recup. | dia):")
        for e in sorted(big, key=lambda e: e["t_min"]):
            d = utc(e["t_min"])
            print(f"    {d:%Y-%m-%d %H:00} | -{e['caida']*100:4.1f}% | {e['recup']*100:4.0f}% | {d:%a} {', '.join(sorted(cats(e['t_min']))) or '-'}")
    os.makedirs(out, exist_ok=True)
    json.dump({a: [e for e in res[a]] for a in res}, open(os.path.join(out, "R49-washouts.json"), "w"), indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("modo", choices=["eventos", "washouts"])
    ap.add_argument("--cache", default=os.path.join(tempfile.gettempdir(), "estudio_eventos_cache"))
    ap.add_argument("--out", default=os.path.join(tempfile.gettempdir(), "estudio_eventos_out"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    (eventos_mode if a.modo == "eventos" else washouts_mode)(a.cache, a.out)
