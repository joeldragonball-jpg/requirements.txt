"""C237 (9-nov-2026): cobertura de los hechos P de informes/hechos/lote-NN.jsonl frente a TODOS los JSON de explorador/
(no solo la Línea de tiempo). Local, sin IA ni red. Uso: python scripts/cobertura_hechos.py salida.json
Puntuación: cifras del hecho encontradas (70 %) + palabras largas (30 %). >=0,6 «está», 0,4-0,6 «dudoso», <0,4 «falta».
Es heurística: revisar a mano con Grep antes de volcar."""
import json,re,glob,collections,sys
import pathlib
R=str(pathlib.Path(__file__).resolve().parent.parent).replace("\\","/")+"/"
sys.path.insert(0,R+"scripts")
from cruzar_hechos import tokens,cifras
corp={}
for p in glob.glob(R+"explorador/*.json"):
    if any(x in p for x in ("precios_","noticias-archivo","prueba-datos")): continue
    corp[p.split("/")[-1].split("\\")[-1]]=open(p,encoding="utf-8").read().lower()
# also regulacion matriz in cerebro? only explorador
def norm(c): return c.replace(".",",")
H=[]
for p in sorted(glob.glob(R+"informes/hechos/lote-*.jsonl")):
    for l in open(p,encoding="utf-8"):
        if l.strip():
            h=json.loads(l); h["_lote"]=p[-13:-6]; H.append(h)
P=[h for h in H if h.get("nivel")=="P"]
out=[]
for h in P:
    t=h["hecho"]; cf=[c for c in re.findall(r"\d+(?:[.,]\d+)+|\d{3,}",t) if not re.fullmatch(r"20\d\d",c)]
    tk=[w for w in tokens(t) if not re.search(r"\d",w) and len(w)>4]
    best=(0,None)
    for f,txt in corp.items():
        nc=sum(1 for c in cf if c.lower() in txt or norm(c) in txt or c.replace(",",".") in txt)
        nt=sum(1 for w in tk if w in txt)
        s=(nc/len(cf) if cf else 0)*0.7+ (nt/max(1,len(tk)))*0.3 if cf else (nt/max(1,len(tk)))*0.6
        if s>best[0]: best=(s,f)
    h["_s"]=round(best[0],2); h["_f"]=best[1]; out.append(h)
json.dump(out,open(sys.argv[1],"w",encoding="utf-8"),ensure_ascii=False)
c=collections.Counter()
for h in out: c[(h.get("ambito"), "esta" if h["_s"]>=0.6 else ("dudoso" if h["_s"]>=0.4 else "falta"))]+=1
for a in sorted({k[0] for k in c},key=lambda a:-sum(v for k,v in c.items() if k[0]==a)):
    print(a, {k[1]:v for k,v in c.items() if k[0]==a})
