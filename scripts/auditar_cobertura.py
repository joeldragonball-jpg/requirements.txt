"""Auditoría local (sin IA, sin red) de huecos, concentraciones y repeticiones en los datos de la Órbita.
Genera research/COBERTURA.md. Uso: python scripts/auditar_cobertura.py"""
import json, collections, datetime, re, pathlib, sys
R = pathlib.Path(__file__).resolve().parent.parent
hoy = datetime.date.today()
d = json.load(open(R/'explorador/datos.json', encoding='utf-8'))
P = json.load(open(R/'explorador/paises.json', encoding='utf-8'))['paises']
m = d['movimientos']; cap = {c['id']: c['nombre'] for c in d['capas']}
def f(x):
    try: return datetime.date.fromisoformat(x['fecha'][:10])
    except Exception: return None
L = [f'# Cobertura, huecos y repeticiones ({hoy})', '', 'Generado por `scripts/auditar_cobertura.py` (local, sin IA). Los hallazgos son datos objetivos; interpretarlos es aparte.', '']
L += ['## 1. Capas sin movimiento reciente en la Línea de tiempo (lo más viejo primero)', '', 'Ojo: solo cuenta la Línea de tiempo; la Matriz de regulación es otro almacén (ver sección 6).', '', '| Capa | Hechos | Último | Días | Niveles |', '|---|---|---|---|---|']
fil = []
for k, n in cap.items():
    v = [x for x in m if x['capa'] == k and f(x) and f(x) <= hoy]
    if not v: fil.append((9999, n, 0, '—', {})); continue
    u = max(f(x) for x in v); fil.append(((hoy-u).days, n, len(v), u.isoformat(), dict(collections.Counter(x.get('nivel') or 'sin nivel' for x in v))))
for dd, n, c, u, nv in sorted(fil, reverse=True):
    L.append(f'| {n} | {c} | {u} | {dd if dd < 9999 else "—"} | {nv} |')
pc = collections.Counter(p for x in m for p in x.get('pais', []))
tot = sum(pc.values())
L += ['', '## 2. Concentración por país en los hechos', '', f'Menciones totales: {tot}. Las 3 primeras: ' + ', '.join(f'{p} {c} ({c*100//tot} %)' for p, c in pc.most_common(3)) + '.', '']
nombres = {p['pais'] for p in P}
sin = [p['pais'] for p in P if pc[p['pais']] == 0]
L += [f'- Países con ficha pero **0 hechos** en la Órbita ({len(sin)}): ' + ', '.join(sin) + '.']
fuera = [p for p in pc if p not in nombres and p not in ('Internacional',)]
L += [f'- Países con hechos pero **sin ficha**: ' + (', '.join(fuera) or 'ninguno') + '.', '']
L += ['## 3. Calidad de los hechos', '']
sn = [x for x in m if not x.get('nivel')]; si = [x for x in m if not x.get('informe')]
L += [f'- Sin nivel de certeza: {len(sn)} de {len(m)}.', f'- Sin informe de respaldo: {len(si)} de {len(m)}.',
      f'- Con fecha futura: {sum(1 for x in m if f(x) and f(x) > hoy)}.', '']
L += ['## 4. Posibles repeticiones (mismo actor y fecha, o texto casi igual)', '']
g = collections.defaultdict(list)
for x in m: g[(x['actor'], x['fecha'])].append(x)
tok = lambda t: set(re.findall(r'\w{5,}', t.lower()))
rep = []
for (a, fe), v in g.items():
    if len(v) > 1: rep.append((a, fe, [y['texto'][:80] for y in v]))
for i, x in enumerate(m):
    for y in m[i+1:]:
        if x['capa'] != y['capa'] and x['fecha'][:7] == y['fecha'][:7]:
            a, b = tok(x['texto']), tok(y['texto'])
            if a and b and len(a & b)/min(len(a), len(b)) > .6: rep.append(('capas distintas', x['fecha'], [x['texto'][:80], y['texto'][:80]]))
for a, fe, t in rep[:15]: L.append(f'- {fe} · {a}: ' + ' ⟷ '.join(t))
if not rep: L.append('- Ninguna.')
L += ['', '## 5. Tensiones entre hechos del mismo tema (revisar a mano)', '']
cnt = collections.Counter()
for x in m:
    t = x['texto'].lower()
    if re.search(r'subid[ao]|subir|sube', t) and 'tipos' in t: cnt['tipos: sube'] += 1
    if re.search(r'recorte|bajar|baja ', t) and 'tipos' in t: cnt['tipos: baja'] += 1
L += [f'- Hechos que hablan de tipos: {dict(cnt)}. Si hay de ambos signos en el mismo mes, comprobar que no se contradicen.', '']

# ---------- 6. Sincronía entre almacenes (Línea de tiempo ↔ Matriz ↔ paneles ↔ voces ↔ CBDC ↔ elecciones) ----------
def cargar(n):
    try: return json.load(open(R/'explorador'/n, encoding='utf-8'))
    except Exception: return None
reg = cargar('regulacion.json'); pan = cargar('paneles.json'); voc = cargar('voces.json'); cb = cargar('cbdc-blockchains.json'); ele = cargar('elecciones.json')
L += ['## 6. Sincronía entre almacenes (para corregir, no para interpretar)', '']
PUE = {'eeuu': 'EE. UU.', 'ue': 'Unión Europea', 'uk': 'Reino Unido', 'jp': 'Japón', 'in': 'India', 'br': 'Brasil', 'ru': 'Rusia', 'kr': 'Corea del Sur', 'sg': 'Singapur', 'hk': 'Hong Kong', 'ca': 'Canadá', 'au': 'Australia', 'ae': 'Emiratos Árabes Unidos', 'cn': 'China', 'za': 'Sudáfrica', 'ch': 'Suiza', 'ir': 'Irán', 'id': 'Indonesia', 'eg': 'Egipto', 'et': 'Etiopía'}
if reg:
    desde = (hoy - datetime.timedelta(days=75)).isoformat()
    sin_linea = []
    for x in reg['celdas']:
        if x.get('etapa') is None or x.get('fuente') != 'P' or not (x.get('fecha') or '') >= desde: continue
        pn = PUE.get(x['jur'], '')
        cerca = [y for y in m if pn and pn in (y.get('pais') or []) and abs((f(y) - datetime.date.fromisoformat(x['fecha'][:10])).days) <= 10] if x.get('fecha') else []
        if not cerca: sin_linea.append(f"{x['fecha']} · {pn or x['jur']} · {x['tema']}")
    L += [f'- Celdas de la Matriz con fuente [P] de los últimos 75 días **sin ningún hecho de la Línea de tiempo cerca** (±10 d, mismo país): {len(sin_linea)}.']
    L += ['  - ' + s for s in sorted(sin_linea, reverse=True)[:25]]
    cad = [f"{PUE.get(x['jur'], x['jur'])} · {x['tema']} (caduca {x['caduca']})" for x in reg['celdas'] if x.get('caduca') and x['caduca'] < hoy.isoformat()]
    L += [f'- Celdas de la Matriz **caducadas**: {len(cad)}.'] + ['  - ' + s for s in cad[:15]]
    rev = [f"{PUE.get(x['jur'], x['jur'])} · {x['tema']} (próxima {x['proxima']['fecha']})" for x in reg['celdas'] if isinstance(x.get('proxima'), dict) and x['proxima'].get('fecha') and x['proxima']['fecha'] < hoy.isoformat()]
    L += [f'- Celdas con «próxima fecha» **ya pasada** (falta anotar qué ocurrió): {len(rev)}.'] + ['  - ' + s for s in rev[:20]]
if pan and isinstance(pan.get('tipos_vivos'), dict):
    mal = [p_['pais'] for p_ in pan['tipos_vivos'].get('paises', []) if p_.get('coincide_radar') is False]
    L += [f"- Tipos oficiales: el panel y la Matriz **no coinciden** en: {', '.join(mal) or 'ninguno'}."]
if voc:
    ven = [f"{v_['id']} {v_['quien']} (prometido {v_['plazo'].get('prometido')})" for v_ in voc['voces'] if v_.get('plazo') and v_['plazo'].get('estado') == 'pendiente' and str(v_['plazo'].get('prometido') or '9999')[:10] < hoy.isoformat()[:len(str(v_['plazo'].get('prometido')))] ]
    L += [f'- Voces con plazo vencido y aún «pendiente»: {len(ven)}.'] + ['  - ' + s for s in ven[:15]]
if cb:
    vac = [x_['proyecto'] for x_ in cb.get('filas', []) if 'VERIFICAR' in (x_.get('estado') or '') or (x_.get('fuente') or '') in ('', '—')]
    L += [f"- Proyectos de CBDC/blockchain sin dato o sin fuente: {', '.join(vac) or 'ninguno'}."]
if ele:
    ec = [f"{p_['pais']} ({p_['fecha']})" for p_ in ele.get('paises', []) if p_.get('estado') == 'en_recuento' and p_['fecha'] < hoy.isoformat()]
    L += [f"- Elecciones aún «en recuento» tras su fecha: {', '.join(ec) or 'ninguna'}."]
L += ['']
(R/'research/COBERTURA.md').write_text('\n'.join(L), encoding='utf-8')
print('research/COBERTURA.md escrito')
