# Cobertura, huecos y repeticiones (2026-11-09)

Generado por `scripts/auditar_cobertura.py` (local, sin IA). Los hallazgos son datos objetivos; interpretarlos es aparte.

## 1. Capas sin movimiento reciente en la Línea de tiempo (lo más viejo primero)

Ojo: solo cuenta la Línea de tiempo; la Matriz de regulación es otro almacén (ver sección 6).

| Capa | Hechos | Último | Días | Niveles |
|---|---|---|---|---|
| Depósitos tokenizados | 1 | 2026-01-07 | 306 | {'S': 1} |
| Bancos centrales y CBDC | 9 | 2026-10-01 | 39 | {'S': 2, 'P': 7} |
| Liquidación y custodia | 7 | 2026-10-12 | 28 | {'P': 4, 'sin nivel': 2, 'S': 1} |
| Fondos, ETF y tesorerías | 5 | 2026-10-12 | 28 | {'sin nivel': 1, 'S': 2, 'P': 2} |
| Deuda soberana y bonos | 6 | 2026-10-22 | 18 | {'P': 6} |
| Stablecoins | 8 | 2026-10-24 | 16 | {'P': 7, 'S': 1} |
| Tokenización (RWA) | 7 | 2026-10-28 | 12 | {'P': 6, 'S': 1} |
| Matriz de riesgos | 8 | 2026-10-31 | 9 | {'sin nivel': 7, 'P': 1} |
| Redes y activo puente | 11 | 2026-11-02 | 7 | {'sin nivel': 4, 'P': 2, 'S': 5} |
| Política y elecciones | 14 | 2026-11-04 | 5 | {'S': 10, 'P': 3, 'V': 1} |
| Regulación y política monetaria | 14 | 2026-11-05 | 4 | {'P': 6, 'S': 7, 'sin nivel': 1} |
| Liquidez y tipos oficiales | 17 | 2026-11-06 | 3 | {'P': 11, 'S': 6} |
| Energía y Ormuz | 16 | 2026-11-06 | 3 | {'P': 5, 'S': 10, 'V': 1} |

## 2. Concentración por país en los hechos

Menciones totales: 114. Las 3 primeras: EE. UU. 37 (32 %), Japón 11 (9 %), Irán 8 (7 %).

- Países con ficha pero **0 hechos** en la Órbita (8): Sudáfrica, Indonesia, Egipto, Etiopía, El Salvador, Argentina, Venezuela, Cuba.
- Países con hechos pero **sin ficha**: Canadá, Hong Kong, Unión Europea, Luxemburgo, Arabia Saudí, Corea del Sur, Zona euro, Taiwán, Catar, Singapur, Australia.

## 3. Calidad de los hechos

- Sin nivel de certeza: 15 de 125.
- Sin informe de respaldo: 27 de 125.
- Con fecha futura: 2.

## 4. Posibles repeticiones (mismo actor y fecha, o texto casi igual)

- 2026-11-04 · Google News · SEC/MiCA/CFTC (EN): Las probabilidades de la CLARITY Act caen al 31 %. ⟷ Demócratas de la Cámara preparan una ley cripto con más poder para la SEC y norm
- 2026-11-06 · Google News · Mercados (EN): Se espera que la Fed mantenga su subida de tipos de diciembre tras el dato de em ⟷ Daly (Fed): más subidas de tipos probables.
- 2026-09-16 · capas distintas: Sube 25 pb los tipos, a 3,75-4,00 %. ⟷ Sube los tipos (ola de subidas de septiembre).
- 2026-09-24 · capas distintas: Propuestas de reglas de la GENIUS Act para comentario (hasta el 30-nov). ⟷ Sube el tipo hasta el 1,25 %.
- 2026-10-08 · capas distintas: Custodia de BTC, ETH, SOL y USDC en la UE; sin XRP ni XLM. ⟷ BNY añadiría custodia de XRP y Ripple se acerca a 1.000 M$ de ingresos.

## 5. Tensiones entre hechos del mismo tema (revisar a mano)

- Hechos que hablan de tipos: {'tipos: sube': 6}. Si hay de ambos signos en el mismo mes, comprobar que no se contradicen.

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
- Celdas con «próxima fecha» **ya pasada** (falta anotar qué ocurrió): 6.
  - Brasil · ley_marco (próxima 2026-11-06)
  - Brasil · custodia (próxima 2026-11-06)
  - Brasil · politica (próxima 2026-11-04)
  - Rusia · stablecoins (próxima 2026-11-04)
  - Emiratos Árabes Unidos · politica (próxima 2026-10-28)
  - brics · ley_marco (próxima 2026-10-30)
- Tipos oficiales: el panel y la Matriz **no coinciden** en: ninguno.
- Voces con plazo vencido y aún «pendiente»: 1.
  - v062 Yi He (co-CEO de Binance) (prometido 2026-11-01)
- Proyectos de CBDC/blockchain sin dato o sin fuente: Pontes (BCE), Project Agorá (BIS + 7 bancos centrales + ~40 bancos), Singapur: wCBDC, BLOOM, letras MAS tokenizadas, Hong Kong: Ensemble / EnsembleTX, Brasil: Drex, EAU: Dirham digital, Palau (Ripple, XRPL), Bután, Montenegro, Georgia, Colombia (Ripple).
- Elecciones aún «en recuento» tras su fecha: EE. UU. (2026-11-03).
