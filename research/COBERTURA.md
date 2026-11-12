# Cobertura, huecos y repeticiones (2026-11-12)

Generado por `scripts/auditar_cobertura.py` (local, sin IA). Los hallazgos son datos objetivos; interpretarlos es aparte.

## 1. Capas sin movimiento reciente en la Línea de tiempo (lo más viejo primero)

Ojo: solo cuenta la Línea de tiempo; la Matriz de regulación es otro almacén (ver sección 6).

| Capa | Hechos | Último | Días | Niveles |
|---|---|---|---|---|
| Depósitos tokenizados | 1 | 2026-01-07 | 309 | {'S': 1} |
| Bancos centrales y CBDC | 10 | 2026-10-06 | 37 | {'S': 2, 'P': 8} |
| Liquidación y custodia | 8 | 2026-10-26 | 17 | {'P': 4, 'sin nivel': 3, 'S': 1} |
| Tokenización (RWA) | 7 | 2026-10-28 | 15 | {'P': 6, 'S': 1} |
| Stablecoins | 14 | 2026-10-28 | 15 | {'P': 9, 'S': 2, 'sin nivel': 3} |
| Fondos, ETF y tesorerías | 8 | 2026-10-30 | 13 | {'sin nivel': 1, 'S': 2, 'P': 5} |
| Redes y activo puente | 14 | 2026-11-02 | 10 | {'sin nivel': 6, 'P': 4, 'S': 4} |
| Matriz de riesgos | 11 | 2026-11-07 | 5 | {'sin nivel': 7, 'P': 4} |
| Deuda soberana y bonos | 13 | 2026-11-09 | 3 | {'P': 10, 'S': 3} |
| Regulación y política monetaria | 29 | 2026-11-10 | 2 | {'P': 19, 'S': 9, 'sin nivel': 1} |
| Política y elecciones | 27 | 2026-11-10 | 2 | {'S': 15, 'P': 11, 'V': 1} |
| Liquidez y tipos oficiales | 24 | 2026-11-11 | 1 | {'P': 14, 'S': 10} |
| Energía y Ormuz | 21 | 2026-11-11 | 1 | {'P': 7, 'S': 13, 'V': 1} |

## 2. Concentración por país en los hechos

Menciones totales: 182. Las 3 primeras: EE. UU. 55 (30 %), España 23 (12 %), Internacional 16 (8 %).

- Países con ficha pero **0 hechos** en la Órbita (5): Indonesia, Egipto, Etiopía, Venezuela, Cuba.
- Países con hechos pero **sin ficha**: Canadá, Hong Kong, Unión Europea, Luxemburgo, Arabia Saudí, Corea del Sur, Zona euro, Taiwán, Catar, Singapur, Australia.

## 3. Calidad de los hechos

- Sin nivel de certeza: 21 de 190.
- Sin informe de respaldo: 26 de 190.
- Con fecha futura: 3.

## 4. Posibles repeticiones (mismo actor y fecha, o texto casi igual)

- 2026-11-04 · Legislativas de EE. UU.: Proyección de mayoría demócrata en la Cámara; el Senado sigue abierto; aprobació ⟷ Según AP vía medios, los demócratas ganan la Cámara y el Senado (54–44 con 2 esc
- 2026-11-09 · Google Noticias · Ormuz (ES): El Brent cae más de un 3 % y baja de 95 $. ⟷ El Brent cae casi un 5 % hasta 93,72 $.
- 2026-11-10 · Google News · Mercados (EN): Waller apoya subir tipos en diciembre y no descarta un movimiento mayor. ⟷ El bono a 10 años de EE. UU. supera el 5 %.
- 2026-11-11 · Google News · Mercados (EN): La Fed está dividida sobre el ritmo de las subidas de tipos. ⟷ El dólar sube a máximos de 19 meses por las apuestas de subida de la Fed.
- 2026-09-16 · capas distintas: Sube 25 pb los tipos, a 3,75-4,00 %. ⟷ Sube los tipos (ola de subidas de septiembre).
- 2026-09-24 · capas distintas: Propuestas de reglas de la GENIUS Act para comentario (hasta el 30-nov). ⟷ Sube el tipo hasta el 1,25 %.
- 2026-10-08 · capas distintas: Custodia de BTC, ETH, SOL y USDC en la UE; sin XRP ni XLM. ⟷ BNY añadiría custodia de XRP y Ripple se acerca a 1.000 M$ de ingresos.

## 5. Tensiones entre hechos del mismo tema (revisar a mano)

- Hechos que hablan de tipos: {'tipos: sube': 7}. Si hay de ambos signos en el mismo mes, comprobar que no se contradicen.

## 6. Sincronía entre almacenes (para corregir, no para interpretar)

- Celdas de la Matriz con fuente [P] de los últimos 75 días **sin ningún hecho de la Línea de tiempo cerca** (±10 d, mismo país): 9.
  - 2026-11-02 · Suiza · fiscal
  - 2026-10-31 · Suiza · cbdc
  - 2026-10-30 · brics · ley_marco
  - 2026-10-29 · Hong Kong · politica
  - 2026-10-21 · Reino Unido · ley_marco
  - 2026-10-12 · brics · stablecoins
  - 2026-09-16 · Emiratos Árabes Unidos · ley_marco
  - 2026-09-15 · Canadá · etf
  - 2026-09-12 · brics · cbdc
- Celdas de la Matriz **caducadas**: 0.
- Celdas con «próxima fecha» **ya pasada** (falta anotar qué ocurrió): 1.
  - Corea del Sur · tokenizacion (próxima 2026-11-11)
- Tipos oficiales: el panel y la Matriz **no coinciden** en: ninguno.
- Voces con plazo vencido y aún «pendiente»: 1.
  - v061 EIA (STEO de octubre de 2026) (prometido 2026-11-10)
- Proyectos de CBDC/blockchain sin dato o sin fuente: Pontes (BCE), Project Agorá (BIS + 7 bancos centrales + ~40 bancos), Singapur: wCBDC, BLOOM, letras MAS tokenizadas, Hong Kong: Ensemble / EnsembleTX, Brasil: Drex, EAU: Dirham digital, Palau (Ripple, XRPL), Bután, Montenegro, Georgia, Colombia (Ripple).
- Elecciones aún «en recuento» tras su fecha: EE. UU. (2026-11-03).
