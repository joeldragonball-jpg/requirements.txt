"""Lector mínimo de .xlsx (solo biblioteca estándar: no hace falta instalar nada). Devuelve {hoja: [(nº_fila, {columna: valor})]}."""
import zipfile,re,sys
import xml.etree.ElementTree as ET
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def leer(path):
    z=zipfile.ZipFile(path)
    ss=[]
    for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns):
        ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%ns['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    out={}
    for s in wb.find('m:sheets',ns):
        rid=s.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        t=rels[rid]; t=t if t.startswith('xl/') else 'xl/'+t.lstrip('/')
        rows=[]
        for r in ET.fromstring(z.read(t)).iter('{%s}row'%ns['m']):
            d={}
            for c in r.findall('m:c',ns):
                col=re.match(r'[A-Z]+',c.get('r')).group()
                v=c.find('m:v',ns); 
                if v is None:
                    is_=c.find('m:is',ns)
                    val=''.join(x.text or '' for x in is_.iter('{%s}t'%ns['m'])) if is_ is not None else None
                else:
                    val=ss[int(v.text)] if c.get('t')=='s' else v.text
                if val not in (None,''): d[col]=val
            if d: rows.append((int(r.get('r')),d))
        out[s.get('name')]=rows
    return out
if __name__=='__main__':
    o=leer(sys.argv[1])
    for n,rows in o.items():
        print('====',n,len(rows),'filas')
        for r,d in rows[:int(sys.argv[2])]: print(r,d)
