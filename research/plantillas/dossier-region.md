# Plantilla: dossier por región o tema

Salida: `informes/research/AAAA-MM-DD-<ID>-<tema-en-minusculas>.md` (NO dentro de `cerebro/`).

Método (aplicar siempre):
1. Buscar primero la fuente primaria en su idioma original: banco central, regulador, ley, comunicado de la empresa, BIS/FMI. Traducirla yo sin perder matices y citar enlace + fecha.
2. Segunda fuente independiente para cada cifra o fecha clave. Si no existe, marcar [VERIFICAR].
3. Separar HECHOS (con fuente) de OPINIONES y [ESPECULACIÓN].
4. Señalar sesgos: promoción, conflicto de interés, hype, cuentas anónimas, titulares sin dato.
5. Contrastar caso alcista vs. bajista. Contexto macro solo si cambia la conclusión.
6. Sin recomendaciones de compra/venta.

Estructura del informe:
```
# <Tema> (fecha, ID)
## Resumen (5 líneas)
## Qué es hecho verificado (tabla: dato | fuente primaria | fecha | idioma original)
## Qué está sin verificar o es opinión
## Caso alcista / caso bajista
## Qué cambia para los digital assets (XRP, XLM, stablecoins, CBDC, tokenización)
## Fechas próximas (catalizadores) con fuente
## Qué falta por buscar
```
Cierre: anotar el coste real en `research/COLA.md`, y como máximo 5 líneas nuevas (sin repetir) en `cerebro/documentos/` solo en los tres archivos de lecciones: patrones-de-bulos, fuentes-fiables-y-dudosas, catalizadores-xrp-xlm.

## Modo PROFUNDO (IDs terminados en P, p. ej. R02P)
Objetivo: gastar cuota en calidad. Partir del informe rápido existente del mismo tema (en `informes/research/`) y su sección "Qué falta por buscar".
1. Para cada hueco, ir a la fuente PRIMARIA con WebFetch y leer el documento entero (comunicado, informe anual, ley, circular), no solo el extracto del buscador. Si una página da 403 o no carga, buscar la copia oficial alternativa (PDF, archivo) y anotar el intento.
2. Tres pasadas: (a) hechos con fuente primaria leída; (b) contraste con una segunda fuente independiente; (c) huecos que siguen abiertos.
3. Ampliar el informe rápido en un archivo nuevo `AAAA-MM-DD-<ID>-<tema>-profundo.md`; no borrar el rápido. Marcar cada dato: LEÍDO ENTERO / extracto / secundaria.
4. Las traducciones de originales no ingleses se citan con la frase original corta y mi traducción.
5. Cierre: coste real medido por diferencia de get_usage; anotarlo en `research/COLA.md`.
