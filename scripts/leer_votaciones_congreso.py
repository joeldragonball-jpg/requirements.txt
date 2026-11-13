"""C242: histórico de votaciones del Pleno del Congreso (datos abiertos, sin IA, sin claves).

Lee el ZIP oficial de cada día de votación de la legislatura (congreso.es/opendata/votaciones),
lo procesa en memoria (no guarda los ZIP) y escribe SOLO agregados en
explorador/espana-votaciones.json: por sesión, por año, por tipo de asunto y por grupo.
No se guardan nombres de diputados ni se hace ningún ranking.

Uso: python scripts/leer_votaciones_congreso.py            (incremental: solo sesiones nuevas)
     python scripts/leer_votaciones_congreso.py --todo     (relee toda la legislatura, ~380 MB de tráfico)
"""
import collections
import concurrent.futures as F
import datetime
import io
import json
import os
import re
import sys
import urllib.request as U
import zipfile

H = {'User-Agent': 'Mozilla/5.0'}
RAIZ = 'https://www.congreso.es'
PAG = RAIZ + '/es/opendata/votaciones'
SAL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'explorador', 'espana-votaciones.json')
LEG = 'XV'
VOTOS = {'Sí': 'si', 'No': 'no', 'Abstención': 'abstencion', 'No vota': 'no_vota'}
GRUPOS = {
    'GP': 'Popular (PP)', 'GS': 'Socialista (PSOE)', 'GVOX': 'VOX', 'GSUMAR': 'Plurinacional SUMAR',
    'GR': 'Republicano (ERC)', 'GJxCAT': 'Junts per Catalunya', 'GEH Bildu': 'EH Bildu',
    'GV (EAJ-PNV)': 'Vasco (EAJ-PNV)', 'GMx': 'Mixto'}


def get(url):
    return U.urlopen(U.Request(url, headers=H), timeout=120).read()


def dias_de_votacion():
    t = get(PAG).decode('utf8', 'ignore')
    m = re.search(r'var diasVotaciones = \[([^\]]*)\]', t)
    return sorted(set(re.findall(r'\d{8}', m.group(1)))) if m else []


def lee_dia(d):
    """Devuelve la lista de sesiones (agregadas) de un día AAAAMMDD."""
    u = PAG + '?p_p_id=votaciones&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&targetLegislatura=%s&targetDate=%s/%s/%s' % (
        LEG, d[6:], d[4:6], d[:4])
    t = get(u).decode('utf8', 'ignore')
    out = []
    for z in sorted(set(re.findall(r'href="(/webpublica/opendata/votaciones/[^"]+\.zip)"', t))):
        zf = zipfile.ZipFile(io.BytesIO(get(RAIZ + z)))
        ses = dict(fecha='%s-%s-%s' % (d[:4], d[4:6], d[6:]), sesion=None, votaciones=0, por_asentimiento=0,
                   mas_si=0, mas_no=0, empate=0, ajustadas=0, por_tipo={}, por_grupo={}, zip=RAIZ + z)
        for n in zf.namelist():
            if not n.endswith('.json'):
                continue
            v = json.loads(zf.read(n).decode('utf8'))
            inf, tot = v.get('informacion', {}), v.get('totales', {})
            ses['sesion'] = inf.get('sesion')
            ses['votaciones'] += 1
            tipo = (inf.get('titulo') or 'Sin título').strip().rstrip('.')[:90]
            ses['por_tipo'][tipo] = ses['por_tipo'].get(tipo, 0) + 1
            if (tot.get('asentimiento') or '').lower().startswith('s'):
                ses['por_asentimiento'] += 1
                continue
            si, no = int(tot.get('afavor') or 0), int(tot.get('enContra') or 0)
            lado = 'si' if si > no else ('no' if no > si else None)
            ses['mas_si' if lado == 'si' else ('mas_no' if lado == 'no' else 'empate')] += 1
            if abs(si - no) <= 5:
                ses['ajustadas'] += 1
            g = collections.defaultdict(lambda: collections.Counter())
            for x in v.get('votaciones') or []:
                g[x.get('grupo') or 'sin grupo'][VOTOS.get(x.get('voto'), 'otro')] += 1
            for grupo, c in g.items():
                a = ses['por_grupo'].setdefault(grupo, dict(si=0, no=0, abstencion=0, no_vota=0, otro=0,
                                                              votaciones=0, con_el_lado_mayor=0))
                for k, n_ in c.items():
                    a[k] += n_
                a['votaciones'] += 1
                # postura del grupo = opción más votada dentro del grupo entre sí / no / abstención
                p = max(('si', 'no', 'abstencion'), key=lambda k: c.get(k, 0))
                if lado and c.get(p, 0) > 0 and p == lado:
                    a['con_el_lado_mayor'] += 1
        out.append(ses)
    return out


def suma_grupos(sesiones):
    tot = {}
    for s in sesiones:
        for g, a in s['por_grupo'].items():
            b = tot.setdefault(g, dict(si=0, no=0, abstencion=0, no_vota=0, otro=0, votaciones=0, con_el_lado_mayor=0))
            for k, v in a.items():
                b[k] += v
    for g, b in tot.items():
        n = b['si'] + b['no'] + b['abstencion'] + b['no_vota'] + b['otro']
        b['nombre'] = GRUPOS.get(g, g)
        b['votos_registrados'] = n
        for k in ('si', 'no', 'abstencion', 'no_vota'):
            b[k + '_pct'] = round(100.0 * b[k] / n, 1) if n else None
        b['con_el_lado_mayor_pct'] = round(100.0 * b['con_el_lado_mayor'] / b['votaciones'], 1) if b['votaciones'] else None
    return dict(sorted(tot.items(), key=lambda kv: kv[1]['nombre']))


# ---------------------------------------------------------------- Senado
SEN = 'https://www.senado.es'
VOTOS_SEN = {'SÍ': 'si', 'SI': 'si', 'NO': 'no', 'ABSTENCIÓN': 'abstencion', 'ABSTENCION': 'abstencion', 'NO VOTA': 'no_vota', 'NO VOTAN': 'no_vota'}


def campo(b, t):
    m = re.search(r'(?s)<%s>\s*(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?\s*</%s>' % (t, t), b)
    return m.group(1).strip() if m else ''


def grupo_senado(n):
    n = re.sub(r'(?i)^GRUPO PARLAMENTARIO ', '', n).strip()
    n = re.sub(r'(?i) EN EL SENADO', '', n)
    return n[:60].title()


def lee_sesion_senado(n):
    try:
        x = get('%s/legis15/votaciones/ses_%d.xml' % (SEN, n)).decode('latin-1')
    except Exception:
        return None
    if '<votacion>' not in x:
        return None
    f = campo(x, 'fecha_sesion')
    ses = dict(sesion=n, fecha='%s-%s-%s' % (f[6:], f[3:5], f[:2]) if len(f) == 10 else f, votaciones=0,
               mas_si=0, mas_no=0, empate=0, ajustadas=0, por_grupo={}, fichero='%s/legis15/votaciones/ses_%d.xml' % (SEN, n))
    for v in re.findall(r'(?s)<votacion>(.*?)</votacion>', x):
        si, no = int(campo(v, 'tot_afirmativos') or 0), int(campo(v, 'tot_negativos') or 0)
        ses['votaciones'] += 1
        lado = 'si' if si > no else ('no' if no > si else None)
        ses['mas_si' if lado == 'si' else ('mas_no' if lado == 'no' else 'empate')] += 1
        if abs(si - no) <= 5:
            ses['ajustadas'] += 1
        g = collections.defaultdict(lambda: collections.Counter())
        for s in re.findall(r'(?s)<VotoSenador>(.*?)</VotoSenador>', v):
            g[grupo_senado(campo(s, 'grupo')) or 'sin grupo'][VOTOS_SEN.get(campo(s, 'voto').upper(), 'otro')] += 1
        aus = re.search(r'(?s)<ausentes>(.*?)</ausentes>', v)
        for s in re.findall(r'(?s)<ausencia>(.*?)</ausencia>', aus.group(1) if aus else ''):
            g[grupo_senado(campo(s, 'grupo')) or 'sin grupo']['ausente'] += 1
        for grupo, c in g.items():
            a = ses['por_grupo'].setdefault(grupo, dict(si=0, no=0, abstencion=0, no_vota=0, otro=0, ausente=0,
                                                          votaciones=0, con_el_lado_mayor=0))
            for k, n_ in c.items():
                a[k] += n_
            a['votaciones'] += 1
            p = max(('si', 'no', 'abstencion'), key=lambda k: c.get(k, 0))
            if lado and c.get(p, 0) > 0 and p == lado:
                a['con_el_lado_mayor'] += 1
    return ses


def suma_grupos_senado(sesiones):
    tot = {}
    for s in sesiones:
        for g, a in s['por_grupo'].items():
            b = tot.setdefault(g, dict(si=0, no=0, abstencion=0, no_vota=0, otro=0, ausente=0, votaciones=0, con_el_lado_mayor=0))
            for k, v in a.items():
                b[k] += v
    for g, b in tot.items():
        n = b['si'] + b['no'] + b['abstencion'] + b['no_vota'] + b['otro'] + b['ausente']
        b['votos_registrados'] = n
        for k in ('si', 'no', 'abstencion', 'no_vota', 'ausente'):
            b[k + '_pct'] = round(100.0 * b[k] / n, 1) if n else None
        b['con_el_lado_mayor_pct'] = round(100.0 * b['con_el_lado_mayor'] / b['votaciones'], 1) if b['votaciones'] else None
    return dict(sorted(tot.items()))


def senado(prev):
    """prev: sesiones ya leídas ({numero: sesion}). Lee ses_1.xml, ses_2.xml… hasta 4 huecos seguidos."""
    ses = dict(prev)
    ini_, huecos = 1, 0
    with F.ThreadPoolExecutor(5) as ex:
        while huecos < 8 and ini_ < 600:  # por tandas de 10 hasta 8 huecos seguidos
            tanda = list(range(ini_, ini_ + 10))
            for num, r in zip(tanda, ex.map(lambda k: ses.get(k) or lee_sesion_senado(k), tanda)):
                if r:
                    ses[num] = r
                    huecos = 0
                else:
                    huecos += 1
            ini_ += 10
    orden = [ses[k] for k in sorted(ses)]
    # composición por grupos e iniciativas legislativas (ficheros XML del catálogo)
    g = get(SEN + '/web/ficopendataservlet?tipoFich=4&legis=15').decode('utf8', 'ignore')
    grupos = [dict(siglas=campo(b, 'siglas'), nombre=grupo_senado(campo(b, 'nombre')), total=int(campo(b, 'total') or 0),
                   electos=int(campo(b, 'totalElectos') or 0), designados=int(campo(b, 'totalDesignados') or 0))
              for b in re.findall(r'(?s)<datosCabecera>(.*?)</datosCabecera>', g)]
    i = get(SEN + '/web/ficopendataservlet?tipoFich=9&legis=15').decode('utf8', 'ignore')
    ini = re.findall(r'(?s)<iniciativa>(.*?)</iniciativa>', i)

    def clase(t):
        m = re.match(r'(Proyecto de Ley Orgánica|Proyecto de Ley|Proposición de Ley Orgánica|Proposición de Ley|Proposición de Reforma|Propuesta de reforma del Reglamento|Propuesta de reforma)', t, re.I)
        return m.group(1).capitalize() if m else 'Tratados y otros'
    por_clase = collections.Counter(clase(campo(b, 'titulo')) for b in ini)
    tot = dict(sesiones=len(orden))
    for k in ('votaciones', 'mas_si', 'mas_no', 'empate', 'ajustadas'):
        tot[k] = sum(s[k] for s in orden)
    por_anio = {}
    for s in orden:
        a = por_anio.setdefault(s['fecha'][:4], dict(sesiones=0, votaciones=0, mas_si=0, mas_no=0, empate=0, ajustadas=0))
        a['sesiones'] += 1
        for k in ('votaciones', 'mas_si', 'mas_no', 'empate', 'ajustadas'):
            a[k] += s[k]
    return dict(
        nivel='P', fuente=SEN + '/web/relacionesciudadanos/datosabiertos/catalogodatos/index.html',
        aviso='Datos abiertos del Senado (XML). El listado oficial de sesiones plenarias del catálogo solo enumera hasta la sesión 60; los ficheros de votación existen para sesiones posteriores y se leen uno a uno. «Ausente» lo publica el propio fichero; no indica el motivo (puede ser un permiso o una misión oficial).',
        primer_dia=orden[0]['fecha'] if orden else None, ultimo_dia=orden[-1]['fecha'] if orden else None,
        sesiones_sin_fichero=[k for k in range(1, (max(ses) if ses else 0) + 1) if k not in ses],
        totales=tot, por_anio=por_anio,
        composicion=dict(fuente=SEN + '/web/ficopendataservlet?tipoFich=4&legis=15', grupos=grupos, total=sum(x['total'] for x in grupos),
                         nota='Composición de los grupos de la XV legislatura según el fichero del Senado (electos y designados por las comunidades autónomas). Tras la disolución del 6-oct-2026 los senadores electos cesan; los designados dependen de su parlamento autonómico. El fichero no indica la fecha de corte: [VERIFICAR].'),
        iniciativas=dict(fuente=SEN + '/web/ficopendataservlet?tipoFich=9&legis=15', total=len(ini),
                         con_votacion=sum(1 for b in ini if '<votaciones>' in b), por_clase=dict(por_clase.most_common()),
                         nota='Clasificación propia por las primeras palabras del título oficial. Incluye tratados y convenios internacionales.'),
        por_grupo=suma_grupos_senado(orden),
        por_grupo_2026=suma_grupos_senado([s for s in orden if s['fecha'].startswith('2026')]),
        sesiones=orden)


def main():
    todo = '--todo' in sys.argv
    prev = {}
    prev_sen = {}
    if os.path.exists(SAL) and not todo:
        ant = json.load(io.open(SAL, encoding='utf8'))
        prev = {s['fecha']: s for s in ant.get('sesiones', [])}
        prev_sen = {s['sesion']: s for s in (ant.get('senado') or {}).get('sesiones', [])}
    if '--solo-senado' in sys.argv and os.path.exists(SAL):
        ant = json.load(io.open(SAL, encoding='utf8'))
        ant['senado'] = senado({} if todo else prev_sen)
        ant['generado'] = datetime.date.today().isoformat()
        json.dump(ant, io.open(SAL, 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
        print('ok senado: sesiones', ant['senado']['totales'])
        return
    dias = dias_de_votacion()
    if not dias:
        raise SystemExit('No se pudo leer la lista de días de votación')
    faltan = [d for d in dias if '%s-%s-%s' % (d[:4], d[4:6], d[6:]) not in prev]
    print('dias con votacion:', len(dias), '| por leer:', len(faltan))
    ses = [s for s in prev.values()]
    fallos = []
    with F.ThreadPoolExecutor(5) as ex:
        fut = {ex.submit(lee_dia, d): d for d in faltan}
        for f in F.as_completed(fut):
            try:
                r = f.result()
                if not r:
                    fallos.append(fut[f])
                ses.extend(r)
            except Exception as e:  # un día que falla no rompe el resto
                fallos.append(fut[f])
                print('fallo', fut[f], repr(e)[:120])
    ses.sort(key=lambda s: (s['fecha'], s['sesion'] or 0))
    por_anio = {}
    for s in ses:
        a = por_anio.setdefault(s['fecha'][:4], dict(dias=0, votaciones=0, por_asentimiento=0, mas_si=0, mas_no=0, empate=0, ajustadas=0))
        a['dias'] += 1
        for k in ('votaciones', 'por_asentimiento', 'mas_si', 'mas_no', 'empate', 'ajustadas'):
            a[k] += s[k]
    por_tipo = collections.Counter()
    for s in ses:
        por_tipo.update(s['por_tipo'])
    tot = dict(dias=len(ses))
    for k in ('votaciones', 'por_asentimiento', 'mas_si', 'mas_no', 'empate', 'ajustadas'):
        tot[k] = sum(s[k] for s in ses)
    out = dict(
        generado=datetime.date.today().isoformat(),
        titulo='España · Congreso: histórico de votaciones del Pleno, legislatura %s (datos abiertos)' % LEG,
        nivel='P', fuente=PAG,
        unidad='número de votaciones y de votos individuales (unidades); porcentajes sobre votos registrados', escala='1 (sin escala)',
        aviso='Agregados propios sobre los ficheros oficiales de cada sesión. «Más síes que noes» describe el recuento, no que el texto quedara aprobado (algunas votaciones exigen mayoría absoluta u otra mayoría). «Con el lado mayor» = la postura más votada del grupo coincide con la opción con más votos en el hemiciclo; es una descripción, no una valoración. No se publican nombres ni se ordenan grupos de mejor a peor.',
        legislatura=LEG, primer_dia=ses[0]['fecha'] if ses else None, ultimo_dia=ses[-1]['fecha'] if ses else None,
        dias_en_calendario=len(dias), dias_sin_leer=sorted(fallos),
        totales=tot, por_anio=por_anio,
        por_tipo=dict(por_tipo.most_common(25)),
        por_grupo=suma_grupos(ses),
        por_grupo_2026=suma_grupos([s for s in ses if s['fecha'].startswith('2026')]),
        leyenda_grupos=GRUPOS,
        sesiones=ses,
    )
    try:
        out['senado'] = senado(prev_sen)
    except Exception as e:  # el Senado no debe impedir guardar el Congreso
        print('senado: fallo', repr(e)[:160])
        if os.path.exists(SAL):
            out['senado'] = json.load(io.open(SAL, encoding='utf8')).get('senado')
    json.dump(out, io.open(SAL, 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    print('ok sesiones', len(ses), 'votaciones', tot['votaciones'], 'fallos', len(fallos), '->', SAL)


if __name__ == '__main__':
    main()
