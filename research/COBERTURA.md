# Cobertura, huecos y repeticiones (2026-11-16)

Generado por `scripts/auditar_cobertura.py` (local, sin IA). Los hallazgos son datos objetivos; interpretarlos es aparte.

## 1. Capas sin movimiento reciente en la Línea de tiempo (lo más viejo primero)

Ojo: solo cuenta la Línea de tiempo; la Matriz de regulación es otro almacén (ver sección 6).

| Capa | Hechos | Último | Días | Niveles |
|---|---|---|---|---|
| Depósitos tokenizados | 2 | 2026-09-24 | 53 | {'S': 1, 'P': 1} |
| Bancos centrales y CBDC | 12 | 2026-10-06 | 41 | {'S': 2, 'P': 10} |
| Liquidación y custodia | 13 | 2026-10-28 | 19 | {'P': 9, 'sin nivel': 3, 'S': 1} |
| Matriz de riesgos | 15 | 2026-11-09 | 7 | {'sin nivel': 7, 'P': 8} |
| Fondos, ETF y tesorerías | 15 | 2026-11-09 | 7 | {'sin nivel': 1, 'S': 5, 'P': 9} |
| Deuda soberana y bonos | 14 | 2026-11-09 | 7 | {'P': 11, 'S': 3} |
| Tokenización (RWA) | 21 | 2026-11-12 | 4 | {'P': 16, 'S': 5} |
| Stablecoins | 23 | 2026-11-13 | 3 | {'P': 17, 'S': 3, 'sin nivel': 3} |
| Regulación y política monetaria | 41 | 2026-11-13 | 3 | {'P': 29, 'S': 11, 'sin nivel': 1} |
| Liquidez y tipos oficiales | 32 | 2026-11-13 | 3 | {'P': 22, 'S': 10} |
| Energía y Ormuz | 28 | 2026-11-14 | 2 | {'P': 14, 'S': 13, 'V': 1} |
| Redes y activo puente | 20 | 2026-11-15 | 1 | {'sin nivel': 6, 'P': 11, 'S': 3} |
| Política y elecciones | 32 | 2026-11-15 | 1 | {'S': 15, 'P': 16, 'V': 1} |

## 2. Concentración por país en los hechos

Menciones totales: 249. Las 3 primeras: EE. UU. 75 (30 %), Internacional 33 (13 %), España 30 (12 %).

- Países con ficha pero **0 hechos** en la Órbita (5): Indonesia, Egipto, Etiopía, Venezuela, Cuba.
- Países con hechos pero **sin ficha**: Canadá, Hong Kong, Unión Europea, Luxemburgo, Arabia Saudí, Corea del Sur, Zona euro, Taiwán, Catar, Singapur, Australia, UE.

## 3. Calidad de los hechos

- Sin nivel de certeza: 21 de 270.
- Sin informe de respaldo: 24 de 270.
- Con fecha futura: 2.

## 4. Posibles repeticiones (mismo actor y fecha, o texto casi igual)

- 2026-10-28 · DTCC: Lanza su servicio de tokenización («Goes Live») en Canton y Besu, con 20 partici ⟷ Arranca el DTCC Tokenization Service (DTC): crea representaciones tokenizadas de
- 2026-11-12 · Google News · Mercados (EN): Hammack (Fed): hacen falta tipos más restrictivos. ⟷ La Fed cambia el calendario: en octubre de 2027 no habrá votación de tipos.
- 2026-09-16 · capas distintas: Sube 25 pb los tipos, a 3,75-4,00 %. ⟷ Sube los tipos (ola de subidas de septiembre).
- 2026-09-24 · capas distintas: Propuestas de reglas de la GENIUS Act para comentario (hasta el 30-nov). ⟷ Sube el tipo hasta el 1,25 %.

## 5. Tensiones entre hechos del mismo tema (revisar a mano)

- Hechos que hablan de tipos: {'tipos: sube': 5}. Si hay de ambos signos en el mismo mes, comprobar que no se contradicen.

## 6. Sincronía entre almacenes (para corregir, no para interpretar)

- Celdas de la Matriz con fuente [P] de los últimos 75 días **sin ningún hecho de la Línea de tiempo cerca** (±10 d, mismo país): 13.
  - 2026-11-14 · es · stablecoins
  - 2026-11-14 · es · custodia
  - 2026-11-14 · Suiza · tokenizacion
  - 2026-11-13 · Canadá · ley_marco
  - 2026-11-02 · Suiza · fiscal
  - 2026-10-31 · Suiza · cbdc
  - 2026-10-30 · brics · ley_marco
  - 2026-10-28 · es · tokenizacion
  - 2026-10-21 · Reino Unido · ley_marco
  - 2026-10-12 · brics · stablecoins
  - 2026-09-15 · Canadá · etf
  - 2026-09-14 · brics · fiscal
  - 2026-09-12 · brics · cbdc
- Celdas de la Matriz **caducadas**: 0.
- Celdas con «próxima fecha» **ya pasada** (falta anotar qué ocurrió): 0.
- Tipos oficiales: el panel y la Matriz **no coinciden** en: ninguno.
- Voces con plazo vencido y aún «pendiente»: 0.
- Proyectos de CBDC/blockchain sin dato o sin fuente: Pontes (BCE), Project Agorá (BIS + 7 bancos centrales + ~40 bancos), Singapur: wCBDC, BLOOM, letras MAS tokenizadas, Hong Kong: Ensemble / EnsembleTX, Brasil: Drex, EAU: Dirham digital, Palau (Ripple, XRPL), Bután, Montenegro, Georgia, Colombia (Ripple).
- Elecciones aún «en recuento» tras su fecha: EE. UU. (2026-11-03).
