# C255 · Primas de riesgo frente a Alemania (Francia, Italia, España) · 12-nov-2026

Nota corta, solo con datos que ya están en el repo (sin red, sin API de Anthropic). Para leer dentro de la próxima W02 (martes 17-nov). Sin recomendaciones.

## 1. Cálculo propio (HECHO: el dato; el diferencial es cálculo propio, no una cifra oficial)
Fuente de los rendimientos: `explorador/paneles.json › bonos › mensual10` (serie mensual del BCE a 10 años, nivel S: el panel no enlaza a la tabla oficial). Prima = rendimiento del país − rendimiento de Alemania.

| País | Sep-2026 | Oct-2026 | Cambio |
|---|---|---|---|
| Alemania (10 años) | 3,473 % | 3,416 % | −5,7 pb |
| Francia | 4,440 % → **97 pb** | 4,890 % → **147 pb** | +50 pb |
| Italia | 4,362 % → **89 pb** | 4,680 % → **126 pb** | +37 pb |
| España | 3,927 % → **45 pb** | 4,066 % → **65 pb** | +20 pb |

(pb = puntos básicos; 100 pb = 1 punto porcentual.) Los tres cuadran con las cifras de partida del encargo (97→147, 89→126, 45→65).

## 2. Contraste con la serie diaria
- Francia: `bonos-manual.json` (AFT, índice TEC 10, leído el 22-oct) sube de 4,90 % (1-oct) a 5,13 % (22-oct), por encima de la media mensual de octubre (4,89 %). Coherente con que la subida se concentrara en la segunda quincena.
- Alemania, Italia y España: no hay serie diaria en el repo, así que **no se puede contrastar** el diferencial día a día. [VERIFICAR] con los datos diarios de cada Tesoro/BCE.
- `bonos-manual.json` sigue en su lectura del 22-oct: refrescarlo exige leer la AFT con Chrome (la web bloquea scripts). Pendiente.
- Matiz de método: la media mensual no es el cierre; el diferencial de cierre puede ser distinto.

## 3. Lectura: caso alcista y caso bajista
- Caso «tensión»: Francia y Italia amplían más que España. El mercado exigiría más prima por deuda con déficit alto y política menos estable; si el diferencial de Francia sigue en el entorno de 150 pb, la prima ya es un 50 % mayor que en septiembre. [ESPECULACIÓN] sobre las causas: el repo no tiene una fuente primaria que las explique.
- Caso «sin alarma»: los niveles absolutos siguen lejos de episodios de estrés, y el Bund bajó mientras los demás subieron, de modo que parte de la ampliación es el Bund y no solo el país (refugio alemán). España mantiene la prima más baja del trío.
- Sesgos de la fuente: una serie mensual suaviza picos; un mes de diferencia no es tendencia.

## 4. Pendientes
- [VERIFICAR] diferenciales diarios y cierre de octubre con fuente oficial.
- Refrescar `bonos-manual.json` (Francia leído el 22-oct) con Chrome.
- Conectar con W02 (subastas y calificaciones del 17-nov).

## Lecciones (máx. 5)
1. Una prima «a ojo» depende de la serie: nombrar siempre si es media mensual o cierre.
2. El repo no tiene Bund diario; sin él no se contrasta nada con la serie diaria de Francia.

## Seguridad
Sin claves, sin red, sin cambios en cerebro/.
