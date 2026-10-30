# W11 · Política y elecciones: revisión semanal (30-oct-2026)

Sin predicción de resultados ni recomendaciones. Etiquetas: [P] primaria leída · [S] prensa · [VERIFICAR] · [ESPECULACIÓN].

## 1. Citas que ya pasaron
- **Brasil, 2.ª vuelta (25-oct):** Lula 51,77 % y Flávio Bolsonaro 48,23 % de los votos válidos, según O Povo citando al TSE [S]; otras webs dan 51,74-51,76 % con 99,8 % escrutado, diferencias de momento de recuento. Flávio dice que no reconoce el resultado [S]. **Cuidado:** hay webs que muestran «Flávio 47,03 %, Lula 45,16 %, Cury 2,89 %, 100 % escrutado»; son de la **1.ª vuelta** (4-oct), no de la 2.ª. El portal del TSE es una página dinámica que no devuelve texto: **cifra oficial sin leer** [VERIFICAR]. Nivel sigue en S.

## 2. Citas de los próximos 60 días
| Cita | Fecha | Fuente | Nivel |
|---|---|---|---|
| **EE. UU., mitad de mandato** | **3-nov-2026** | 2 U.S.C. § 7: «el martes siguiente al primer lunes de noviembre». El 1-nov es domingo, el primer lunes es el 2 y la elección el 3. Texto de la ley leído en LII/Cornell. | **P** (antes S) |
| **España, generales** | **29-nov-2026** | Real Decreto 806/2026, de 5-oct (art. 2): «se celebrarán el domingo 29 de noviembre de 2026»; BOE-A-2026-20742, publicado el 6-oct. | **P** (ya lo era) |

- La cita de España ya estaba en `eventos/calendario.toml` (impacto alto, fuente BOE, de C30): sin cambios.
- Los plazos de campaña (13-nov) y de constitución de las Cortes (23-dic) siguen siendo de prensa [S, VERIFICAR en el decreto].

## 3. Países con fecha vacía
- **Alemania:** fecha sin fijar, pero la ventana oficial es del **26-ene-2029 al 25-mar-2029** (art. 39 de la Ley Fundamental: 46-48 meses tras el inicio de la legislatura, que empezó el 25-mar-2025; domingo o festivo; si se disuelve antes, elecciones en 60 días) [P, Bundeswahlleiterin]. Corregido el estado, que decía «pasada». Un sitio de encuestas cita «septiembre-octubre de 2029»: contradice la ley y la fuente oficial, descartado.
- **Países Bajos:** no se tocó (próxima cita sin fecha; la fuente actual es el parlamento, nivel S). Pendiente de buscar en Kiesraad.
- **China:** sin elecciones nacionales competitivas; no aplica (ya constaba).

## 4. Encuestas (neutral, no son predicción)
- **EE. UU. [S]:** el CFR indica que ya se conoce el resultado de ≈ 90 % de las plazas de la Cámara y ≈ 75 % de las del Senado; unas 20 plazas de la Cámara y 5 del Senado, en el aire. Modelos y mercados de predicción de esta semana difieren mucho en el Senado (de ~35 % a ~62 % de probabilidad de Senado demócrata según los resultados de búsqueda, de fechas distintas) y los más citados no son encuestas ni fuentes oficiales: **no los uso**.
- **España [S, ya en el repo]:** CIS (organismo público; barómetro de octubre): PSOE 34 %, PP 22,2 %, Vox 17,1 %. Otras casas pueden diferir y la prensa critica la metodología del CIS. Una búsqueda de hoy no halló encuestas nuevas del periodo de campaña [VERIFICAR].

## 5. Efectos (solo escenarios [ESPECULACIÓN])
- Un Congreso dividido en EE. UU. podría frenar o retrasar la CLARITY Act en la sesión posterior (lame duck) y el gasto; sin efecto sobre este informe.
- España: incertidumbre fiscal y de regulación (CNMV, MiCA, vivienda) hasta formar gobierno.
## 6. Qué se tocó
`explorador/elecciones.json` (EE. UU. a P; Alemania con ventana oficial; Brasil con cifras y aviso de 1.ª vuelta), Seguimiento regenerado. `revisar_explorador.py`: 0 avisos.

## 7. A vigilar
1. Resultado oficial del 3-nov (y si Flávio impugna ante el TSE en Brasil).
2. Encuestas del CIS y de otras casas durante la campaña de España (desde el 13-nov, [S]).

## 8. Seguridad
Solo lecturas públicas; la web de la Bundeswahlleiterin dio fallo de certificado a Python y **no se desactivó la verificación**: se leyó con el navegador integrado. Sin claves; sin workflows ni API de Anthropic.
