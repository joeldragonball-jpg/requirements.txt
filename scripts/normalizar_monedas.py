"""Normaliza los importes de los datos del mapa: símbolo delante y magnitudes claras (M = millones, mil M = miles de millones)."""
import json
import re
import sys

NUM = r'(\d{1,3}(?:\.\d{3})*(?:,\d+)?|\d+(?:,\d+)?)'


def a_float(txt):
    return float(txt.replace('.', '').replace(',', '.'))


def fmt(v, dec=None):
    s = f'{v:,.{1 if dec is None else dec}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return s[:-2] if s.endswith(',0') else s


def conv_millones(m, sym):
    ini = m.group(1) or ''
    txt = m.group(2)
    v = a_float(txt)
    if v >= 10000:
        return f'{ini}{sym}{fmt(v / 1000)} mil M'
    return f'{ini}{sym}{txt} M'


def transformar(s, sym):
    orig = s
    # miles de millones: «MM$»
    s = re.sub(r'(≈\s*)?' + NUM + r'\s*MM\$', lambda m: f'{m.group(1) or ""}{sym}{m.group(2)} mil M', s)
    # millones: «M$»
    s = re.sub(r'(≈\s*)?' + NUM + r'\s*M\$', lambda m: conv_millones(m, sym), s)
    # barril y dólares sueltos («126 $», «126 $/barril»)
    s = re.sub(NUM + r'\s*\$/barril', lambda m: f'{sym}{m.group(1)} por barril', s)
    s = re.sub(r'(?<![\w$])' + NUM + r'\s*\$(?![\w/$])', lambda m: f'{sym}{m.group(1)}', s)
    # códigos de moneda detrás del número
    s = re.sub(NUM + r'\s*(?:USD|US\$)(?![\w])', lambda m: f'{sym}{m.group(1)}', s)
    s = re.sub(NUM + r'\s*M KRW', lambda m: f'₩{m.group(1)} M', s)
    s = re.sub(NUM + r' millones de wones', lambda m: f'₩{m.group(1)} millones (wones)', s)
    s = re.sub(NUM + r' billones de RMB', lambda m: f'CN¥{m.group(1)} billones (RMB)', s)
    s = re.sub(NUM + r'\s*R\$', lambda m: f'R${m.group(1)}', s)
    s = s.replace('stablecoins en HKD', 'stablecoins en dólares de Hong Kong (HK$)')
    return s


def recorrer(o, sym, cambios):
    if isinstance(o, str):
        n = transformar(o, sym)
        if n != o:
            cambios.append((o, n))
        return n
    if isinstance(o, dict):
        return {k: recorrer(v, sym, cambios) for k, v in o.items()}
    if isinstance(o, list):
        return [recorrer(v, sym, cambios) for v in o]
    return o


def main(aplicar):
    cambios = []
    p = 'explorador/datos.json'
    raw = open(p, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in raw else '\n'
    d = recorrer(json.loads(raw), '$', cambios)
    n1 = len(cambios)
    if aplicar:
        open(p, 'w', encoding='utf-8', newline='').write(json.dumps(d, ensure_ascii=False, indent=2).replace('\n', nl))
    p = 'explorador/regulacion.json'
    raw = open(p, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in raw else '\n'
    r = json.loads(raw)
    for c in r['celdas']:
        sym = 'US$' if c['jur'] in ('sg', 'hk') else '$'
        for k, v in list(c.items()):
            c[k] = recorrer(v, sym, cambios)
    for k in ('aviso',):
        if isinstance(r.get(k), str):
            r[k] = recorrer(r[k], '$', cambios)
    if aplicar:
        open(p, 'w', encoding='utf-8', newline='').write(json.dumps(r, ensure_ascii=False, indent=2).replace('\n', nl))
    print(f'{len(cambios)} textos cambiados ({n1} en datos.json)')
    for a, b in cambios[: int(sys.argv[2]) if len(sys.argv) > 2 else 400]:
        # muestra solo los trozos que difieren
        i = 0
        while i < min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        j = 0
        while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]:
            j += 1
        print('  -', a[max(0, i - 25): len(a) - j + 20].replace('\n', ' '))
        print('  +', b[max(0, i - 25): len(b) - j + 20].replace('\n', ' '))


if __name__ == '__main__':
    main(len(sys.argv) > 1 and sys.argv[1] == 'aplicar')
