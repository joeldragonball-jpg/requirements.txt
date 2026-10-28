# Índice de datos del Explorador (autogenerado)

Generado el 2026-10-28 por `python scripts/indice_datos.py` (sin IA, solo lectura de los JSON). No editar a mano.

## Cómo se usa
Buscar un dato aquí → abrir el archivo → ir al campo. `por-pais.json`, `por-tema.json`, `cambios.json` e `informes.json` enumeran cada elemento con su huella común.

## Dato → archivo → campo
| Dato | Archivo | Campo |
|---|---|---|
| Etapa regulatoria (0-5) por país y tema | `regulacion.json` | `celdas[].etapa` (`jur`, `tema`) |
| Estado, próxima fecha, hitos y lo que falta | `regulacion.json` | `celdas[].estado`, `proxima`, `hitos`, `falta` |
| Política monetaria (dirección y valor) | `regulacion.json` | `celdas[tema=politica].dir`, `valor` |
| Países y jurisdicciones | `regulacion.json` | `jurisdicciones[]` (`id`, `nombre`, `pais_id`) |
| Hechos por capa (producción, piloto, plan, XRP/XLM) | `datos.json` | `capas[].produccion/piloto/plan/xrp[]` |
| Cifras clave de cada capa | `datos.json` | `capas[].cifras[]` |
| Línea de tiempo de eventos | `datos.json` | `movimientos[]` |
| Informes de origen | `datos.json` / `regulacion.json` | `informe` / `celdas[].informes` / `base_informes` |
| Voces y predicciones | `voces.json` | `voces[]`, `canales[]` |
| Paneles de mercado (stablecoins, RWA, tipos, defensa…) | `paneles.json` | claves de primer nivel |
| Calificaciones soberanas | `calificaciones.json` | `paises` |
| Deuda (FMI) | `deuda-fmi.json` | `paises`, `anios` |
| Reservas y oro | `reservas.json` | `reservas`, `oro`, `bancos_centrales` |
| Valoración sectorial | `valoracion.json` | `filas[]` |
| Bancos europeos (EBA) | `bancos-eba.json` | `bancos[]` |
| Módulos del Centro | `centro.json` | `modulos[]` |
| Todos los informes por tema y país | `indice/informes.json` | `informes[]` (`tema`, `pais_id`) |
| Qué cambió en 7 y 30 días | `indice/cambios.json` | `ultimos_7_dias`, `ultimos_30_dias` |

## Esquema común (campos opcionales y aditivos: no sustituyen a los antiguos)
| Campo | Tipo | Significado |
|---|---|---|
| `pais_id` | texto o lista | Código de país en mayúsculas (ISO 3166-1 alfa-2). Pseudocódigos: `EU` Unión Europea, `EA` zona euro, `INT` internacional o supranacional |
| `nivel` | `P` / `S` / `V` | Certeza de la fuente: P = primaria leída, S = secundaria, V = por verificar. Mismo criterio que `fuente` y `k` |
| `fecha` | AAAA[-MM[-DD]] | Fecha del hecho o del último cambio (ya existía en celdas y movimientos) |
| `url` | http(s):// | Fuente enlazable (ya existía en 76 celdas) |
| `revisar` | verdadero/falso | Hay que volver a comprobarlo (nivel S/V o celda sin dato) |
| `caduca` | AAAA-MM-DD | Desde cuándo el dato debe darse por viejo. En celdas: `revisado` + 90 días (convención de C43, ajustable) |
| `sesgo` | texto o lista | Sesgo de la fuente (promoción, conflicto de interés…). Reservado; sin rellenar aún |
| `perspectivas` | texto o lista | Caso alcista, bajista u otras lecturas. Reservado; sin rellenar aún |

Rellenado hoy: `regulacion.json` (jurisdicciones: `pais_id`; celdas: `pais_id`, `nivel`, `revisar` y `caduca` si hay `revisado`) y `datos.json` (movimientos y hechos o cifras de las capas con país: `pais_id`, `nivel`, `revisar` cuando procede). El resto de JSON, sin tocar. `python scripts/revisar_explorador.py` comprueba la forma de estos campos.

## Recuento
- Elementos con huella común: 323 (28 países, 18 temas).
- Informes indexados: 206.
- Cambios en 7 días: 90 datos y 78 informes; en 30 días: 152 y 199.

## Informes por tema
| Tema | Informes |
|---|---|
| Auditorías y verificaciones | 25 |
| Cripto y ETF | 35 |
| Deuda y bonos | 6 |
| Energía y Ormuz | 4 |
| Fiscal | 8 |
| Macro y tipos | 9 |
| Otros | 41 |
| Regulación por país | 30 |
| Sesiones diarias (apertura y cierre) | 41 |
| Voces y predicciones | 7 |
