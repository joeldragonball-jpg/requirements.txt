# Cobertura, huecos y repeticiones (2026-11-10)

Generado por `scripts/auditar_cobertura.py` (local, sin IA). Los hallazgos son datos objetivos; interpretarlos es aparte.

## 1. Capas sin movimiento reciente en la Línea de tiempo (lo más viejo primero)

Ojo: solo cuenta la Línea de tiempo; la Matriz de regulación es otro almacén (ver sección 6).

| Capa | Hechos | Último | Días | Niveles |
|---|---|---|---|---|
| Depósitos tokenizados | 1 | 2026-01-07 | 307 | {'S': 1} |
| Bancos centrales y CBDC | 10 | 2026-10-06 | 35 | {'S': 2, 'P': 8} |
| Stablecoins | 12 | 2026-10-24 | 17 | {'P': 7, 'S': 2, 'sin nivel': 3} |
| Liquidación y custodia | 8 | 2026-10-26 | 15 | {'P': 4, 'sin nivel': 3, 'S': 1} |
| Tokenización (RWA) | 7 | 2026-10-28 | 13 | {'P': 6, 'S': 1} |
| Fondos, ETF y tesorerías | 8 | 2026-10-30 | 11 | {'sin nivel': 1, 'S': 2, 'P': 5} |
| Redes y activo puente | 15 | 2026-11-02 | 8 | {'sin nivel': 6, 'P': 4, 'S': 5} |
| Matriz de riesgos | 11 | 2026-11-07 | 3 | {'sin nivel': 7, 'P': 4} |
| Regulación y política monetaria | 21 | 2026-11-08 | 2 | {'P': 11, 'S': 9, 'sin nivel': 1} |
| Energía y Ormuz | 18 | 2026-11-09 | 1 | {'P': 5, 'S': 12, 'V': 1} |
| Deuda soberana y bonos | 11 | 2026-11-09 | 1 | {'P': 8, 'S': 3} |
| Política y elecciones | 23 | 2026-11-10 | 0 | {'S': 15, 'P': 7, 'V': 1} |
| Liquidez y tipos oficiales | 22 | 2026-11-10 | 0 | {'P': 13, 'S': 9} |

## 2. Concentración por país en los hechos

Menciones totales: 164. Las 3 primeras: EE. UU. 52 (31 %), España 18 (10 %), Internacional 13 (7 %).

- Países con ficha pero **0 hechos** en la Órbita (6): Sudáfrica, Indonesia, Egipto, Etiopía, Venezuela, Cuba.
- Países con hechos pero **sin ficha**: Canadá, Hong Kong, Unión Europea, Luxemburgo, Arabia Saudí, Corea del Sur, Zona euro, Taiwán, Catar, Singapur, Australia.

## 3. Calidad de los hechos

- Sin nivel de certeza: 21 de 170.
- Sin informe de respaldo: 24 de 170.
- Con fecha futura: 3.

## 4. Posibles repeticiones (mismo actor y fecha, o texto casi igual)

- 2026-11-04 · Legislativas de EE. UU.: Proyección de mayoría demócrata en la Cámara; el Senado sigue abierto; aprobació ⟷ Según AP vía medios, los demócratas ganan la Cámara y el Senado (54–44 con 2 esc
- 2026-11-08 · Google News · Mercados (EN): IPC caliente: se da por hecha una subida de tipos de la Fed, pero las bolsas sub ⟷ La Fed mantiene tipos en la primera reunión de Warsh como presidente.
- 2026-11-09 · Google Noticias · Ormuz (ES): El Brent cae más de un 3 % y baja de 95 $. ⟷ El Brent cae casi un 5 % hasta 93,72 $.
- 2026-09-16 · capas distintas: Sube 25 pb los tipos, a 3,75-4,00 %. ⟷ Sube los tipos (ola de subidas de septiembre).
- 2026-09-24 · capas distintas: Propuestas de reglas de la GENIUS Act para comentario (hasta el 30-nov). ⟷ Sube el tipo hasta el 1,25 %.
- 2026-10-08 · capas distintas: Custodia de BTC, ETH, SOL y USDC en la UE; sin XRP ni XLM. ⟷ BNY añadiría custodia de XRP y Ripple se acerca a 1.000 M$ de ingresos.
- 2026-10-26 · capas distintas: Ripple recibe la aprobación final de la OCC para su banco fiduciario nacional (R ⟷ Ripple recibe la aprobación final para lanzar su propio banco fiduciario naciona

## 5. Tensiones entre hechos del mismo tema (revisar a mano)

- Hechos que hablan de tipos: {'tipos: sube': 4}. Si hay de ambos signos en el mismo mes, comprobar que no se contradicen.

## 6. Sincronía entre almacenes (para corregir, no para interpretar)

- Celdas de la Matriz con fuente [P] de los últimos 75 días **sin ningún hecho de la Línea de tiempo cerca** (±10 d, mismo país): 8.
  - 2026-11-02 · Suiza · fiscal
  - 2026-10-31 · Suiza · cbdc
  - 2026-10-29 · Hong Kong · politica
  - 2026-10-21 · Reino Unido · ley_marco
  - 2026-10-12 · brics · stablecoins
  - 2026-09-16 · Emiratos Árabes Unidos · ley_marco
  - 2026-09-15 · Canadá · etf
  - 2026-09-12 · brics · cbdc
- Celdas de la Matriz **caducadas**: 0.
- Celdas con «próxima fecha» **ya pasada** (falta anotar qué ocurrió): 3.
  - Brasil · politica (próxima 2026-11-04)
  - Emiratos Árabes Unidos · politica (próxima 2026-10-28)
  - brics · ley_marco (próxima 2026-10-30)
- Tipos oficiales: el panel y la Matriz **no coinciden** en: ninguno.
- Voces con plazo vencido y aún «pendiente»: 1.
  - v062 Yi He (co-CEO de Binance) (prometido 2026-11-01)
- Proyectos de CBDC/blockchain sin dato o sin fuente: Pontes (BCE), Project Agorá (BIS + 7 bancos centrales + ~40 bancos), Singapur: wCBDC, BLOOM, letras MAS tokenizadas, Hong Kong: Ensemble / EnsembleTX, Brasil: Drex, EAU: Dirham digital, Palau (Ripple, XRPL), Bután, Montenegro, Georgia, Colombia (Ripple).
- Elecciones aún «en recuento» tras su fecha: EE. UU. (2026-11-03).
