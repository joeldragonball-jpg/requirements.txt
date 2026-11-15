"""C42 (16-nov-2026): instantánea de rendimientos de DefiLlama (API pública abierta, sin clave, sin IA) para XRPL, Stellar
y referencias de préstamo/staking en Ethereum. Nivel S (agregador). APY = dato puntual, no promesa; incluye base y recompensas.
Uso: python scripts/leer_rendimientos.py  ->  explorador/rendimientos-defillama.json"""
import json
import urllib.request
from datetime import date
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "explorador" / "rendimientos-defillama.json"
URL = "https://yields.llama.fi/pools"


def fila(p):
    r = lambda x: None if x is None else round(x, 3)
    return {"cadena": p["chain"], "proyecto": p["project"], "simbolo": p["symbol"], "tvl_usd": round(p["tvlUsd"]),
            "apy_pct": r(p.get("apy")), "apy_base_pct": r(p.get("apyBase")), "apy_recompensa_pct": r(p.get("apyReward")),
            "pool": p.get("pool"), "estable": p.get("stablecoin")}


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "cartera-datos/1.0"})
    datos = json.load(urllib.request.urlopen(req, timeout=60))["data"]
    top = lambda ch, n: [fila(p) for p in sorted((p for p in datos if p["chain"] == ch), key=lambda p: -p["tvlUsd"])[:n]]
    ref = []
    for proy, simb in (("aave-v3", "USDC"), ("aave-v3", "USDT"), ("lido", "STETH"), ("morpho-v1", "USDC")):
        c = [p for p in datos if p["chain"] == "Ethereum" and p["project"] == proy and p["symbol"] == simb]
        if c:
            ref.append(fila(max(c, key=lambda p: p["tvlUsd"])))
    d = {"generado": date.today().isoformat(), "fuente": URL, "nivel": "S (DefiLlama, agregador; cifras de protocolos, parte interesada)",
         "metodo": "API pública de DefiLlama; por cadena se guardan los 10 pools de mayor TVL. APY es un dato puntual que cambia a diario; no es rentabilidad futura.",
         "xrpl": top("XRPL", 10), "stellar": top("Stellar", 8), "referencia_ethereum": ref,
         "avisos": ["XRP y XLM no tienen staking de protocolo (XRPL sin staking; XLM sin staking nativo): los APY de XRPL son pools AMM/DEX o fondos tokenizados de Tesoro, no staking.",
                    "APY alto en pools pequeños = TVL bajo y riesgo de impermanent loss/contrato [RAZONADO].",
                    "XLS-66 (préstamos nativos del XRPL): en votación, sin activar [VERIFICAR estado]."]}
    RUTA.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(RUTA, len(d["xrpl"]), len(d["stellar"]), len(ref))


main()
