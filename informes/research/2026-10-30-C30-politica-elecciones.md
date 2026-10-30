# C30 · Política y elecciones por país

Fecha: 2026-10-30 · Sin recomendaciones ni predicciones de resultado · Etiquetas: [P] primaria leída · [S] prensa · [VERIFICAR] · [ESPECULACIÓN]

## 1. Resumen
1. **Ninguna fecha está confirmada en fuente oficial**: no abrí el BOE, el Congreso, Légifrance ni comisiones electorales. Todo viene de prensa y agregadores **[S]**; por eso cada fila queda **[VERIFICAR]**.
2. **Novedad que cambia el calendario: España vota el 29-nov-2026** (generales anticipadas; disolución el 5-oct, Real Decreto 806/2026 según ESdiario, publicado el 6-oct). Estaba previsto para 2027. No estaba en el calendario del repo: añadido.
3. **Brasil ya votó** (2.ª vuelta, 25-oct): Lula ~51,7 % frente a ~48,2 % de Flávio Bolsonaro; el TSE confirmó la reelección y Bolsonaro no la reconoce **[S]**.
4. **EE. UU. el 3-nov**: Senado 53-47 republicano; los demócratas necesitan +3 en la Cámara y +4 en el Senado (CFR). Mercados de predicción daban la Cámara demócrata ~84 % y el Senado abierto (cifras antiguas) **[S]**. La CLARITY Act queda para la sesión posterior (lame duck).
5. **Francia**: presidencial el 18-abr y 2-may-2027 (Gobierno, 1-jul-2026) **[S]**. **Italia**: antes de dic-2027; Meloni estudiaría abril de 2027 (Bloomberg, fuentes sin nombre) **[S]**. **Alemania**: la AfD gana Sajonia-Anhalt (43,8 %) el 6-sep **[S]**.

## 2. Calendario (resumen; detalle en `explorador/elecciones.json`)
| País | Cita | Fecha | Nivel |
|---|---|---|---|
| EE. UU. | Mitad de mandato | 3-nov-2026 | S |
| España | Generales anticipadas | 29-nov-2026 | S |
| Francia | Presidencial, 1.ª / 2.ª vuelta | 18-abr y 2-may-2027 | S |
| Italia | Generales | antes de dic-2027 | S |
| Argentina | Presidencial y legislativas | 24-oct-2027 | S |
| México | Legislativas intermedias | ~jun-2027 | S [VERIFICAR] |
| India | Presidencial indirecta | ~jul-2027 | S [VERIFICAR] |
| Brasil, Japón (8-feb), Alemania (autonómicas) | ya celebradas | — | S |
| Reino Unido, Países Bajos, Corea del Sur, Canadá, China | **sin consultar** | — | V |

## 3. Qué cambiaría según el bloque
Solo como escenario **[ESPECULACIÓN]**: en EE. UU., un Congreso dividido podría frenar leyes cripto (CLARITY) y limitar gasto; el aviso de Trump de no atacar Irán antes del 3-nov (8-oct, CNBC) liga esta fecha con el petróleo (C29). En España y Francia, la lectura es de deuda y calificaciones. No hay material suficiente para comparar programas cripto por bloque: queda como hueco.

## 4. Sesgos y límites
Mercados de predicción y encuestas son opiniones agregadas, no hechos. Varias fuentes son secundarias (agregadores de prensa); un titular daba el 27-abr para Francia y su texto el 18-abr. Muestra: 10 países con dato, 5 sin consultar.

## 5. Qué se tocó
`explorador/elecciones.json`; `eventos/calendario.toml` (España 29-nov y Francia 18-abr); `eventos/vinculos.json` (regla nueva «elecciones/presidencial» → W11); capa «Política y elecciones» con 7 movimientos en `explorador/datos.json`; Agenda del móvil, desplegable «Elecciones próximas». Propuesta de rutina **W11** (revisión semanal corta, ~1 %).
