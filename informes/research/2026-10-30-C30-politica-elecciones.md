# C30 · Política y elecciones por país

Fecha: 2026-10-30 · Sin recomendaciones ni predicciones de resultado · Etiquetas: [P] primaria leída · [S] prensa · [VERIFICAR] · [ESPECULACIÓN]

## 1. Resumen
1. **Solo España está confirmada en fuente oficial [P]**: el BOE (Real Decreto 806/2026, art. 2) fija el 29-nov-2026. El resto viene de prensa y agregadores **[S]** y queda **[VERIFICAR]**; la 2.ª pasada del 30-oct añadió Reino Unido (límite legal 15-ago-2029), Países Bajos (gobierno en minoría Jetten desde el 23-feb, sin fecha), Corea del Sur (locales del 3-jun, generales abril de 2028) y Canadá (oct-2029 por cálculo), todos [S].
2. **Novedad que cambia el calendario: España vota el 29-nov-2026** (generales anticipadas; disolución el 5-oct, Real Decreto 806/2026 según ESdiario, publicado el 6-oct). Estaba previsto para 2027. No estaba en el calendario del repo: añadido.
3. **Brasil ya votó** (2.ª vuelta, 25-oct): Lula ~51,7 % frente a ~48,2 % de Flávio Bolsonaro; el TSE confirmó la reelección y Bolsonaro no la reconoce **[S]**.
4. **EE. UU. el 3-nov**: Senado 53-47 republicano; los demócratas necesitan +3 en la Cámara y +4 en el Senado (CFR). Mercados de predicción daban la Cámara demócrata ~84 % y el Senado abierto (cifras antiguas) **[S]**. La CLARITY Act queda para la sesión posterior (lame duck).
5. **Francia**: presidencial el 18-abr y 2-may-2027 (Gobierno, 1-jul-2026) **[S]**. **Italia**: antes de dic-2027; Meloni estudiaría abril de 2027 (Bloomberg, fuentes sin nombre) **[S]**. **Alemania**: la AfD gana Sajonia-Anhalt (43,8 %) el 6-sep **[S]**.

## 2. Calendario (resumen; detalle en `explorador/elecciones.json`)
| País | Cita | Fecha | Nivel |
|---|---|---|---|
| EE. UU. | Mitad de mandato | 3-nov-2026 | S |
| España | Generales anticipadas | 29-nov-2026 | **P** (BOE) |
| Francia | Presidencial, 1.ª / 2.ª vuelta | 18-abr y 2-may-2027 | S |
| Italia | Generales | antes de dic-2027 | S |
| Argentina | Presidencial y legislativas | 24-oct-2027 | S |
| México | Legislativas intermedias | ~jun-2027 | S [VERIFICAR] |
| India | Presidencial indirecta | ~jul-2027 | S [VERIFICAR] |
| Brasil, Japón (8-feb), Alemania (autonómicas) | ya celebradas | — | S |
| Reino Unido | Generales (límite legal) | 15-ago-2029 | S |
| Canadá | Generales | ~15-oct-2029 (cálculo) | S [VERIFICAR] |
| Países Bajos | sin fecha (gobierno en minoría) | — | S |
| Corea del Sur | locales 3-jun-2026 (hechas); generales abr-2028 | — | S |
| China | no aplica | — | — |

## 3. Qué cambiaría según el bloque
Solo como escenario **[ESPECULACIÓN]**: en EE. UU., un Congreso dividido podría frenar leyes cripto (CLARITY) y limitar gasto; el aviso de Trump de no atacar Irán antes del 3-nov (8-oct, CNBC) liga esta fecha con el petróleo (C29). En España y Francia, la lectura es de deuda y calificaciones. No hay material suficiente para comparar programas cripto por bloque: queda como hueco.

## 4. Sesgos y límites
Mercados de predicción y encuestas son opiniones agregadas, no hechos. Varias fuentes son secundarias (agregadores de prensa); un titular daba el 27-abr para Francia y su texto el 18-abr. Encuestas: solo el CIS de España (octubre: PSOE 34 %, PP 22,2 %, Vox 17,1 %, [S] vía prensa); es un organismo público y la prensa señala que otras casas dan al PP por delante, sin que yo haya leído esas encuestas **[VERIFICAR]**. EE. UU.: sin encuesta neutral leída.

## 5. Qué se tocó
`explorador/elecciones.json`; `eventos/calendario.toml` (España 29-nov y Francia 18-abr); `eventos/vinculos.json` (regla nueva «elecciones/presidencial» → W11); capa «Política y elecciones» con 7 movimientos en `explorador/datos.json`; Agenda del móvil, desplegable «Elecciones próximas». Propuesta de rutina **W11** (revisión semanal corta, ~1 %).
