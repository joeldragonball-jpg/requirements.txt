# España: lo que solo puedes hacer tú, paso a paso (6-nov-2026)

Todo lo demás de España ya está hecho o lo hago yo. Esto es lo que queda y por qué. Están ordenados de **más rentable a menos**: con los dos primeros cierras casi todo lo que sigue abierto.

**Regla común para los archivos:** descárgalos a tu carpeta **Descargas** con el nombre que traigan. **No los subas al repositorio** (es público y pesan). Después me escribes solo «ya» y el nombre del paso; yo los leo desde Descargas (así leí los PDF de Interior), vuelco las cifras con su fuente y nivel [P], y los archivos se quedan fuera del repo.

---

## 1. Solicitud de acceso a la información pública (10 minutos, una sola vez)

**ESTADO: PRESENTADA el 6-nov-2026** (justificante de registro en poder de Joel; expediente y nº de registro REGAGE no se copian aquí porque el repositorio es público). Fecha de expediente y de registro: 6-nov-2026 (el justificante escribe una como 06/11 y la otra como 11/06: es el mismo día en dos formatos). **Plazo orientativo de resolución: hasta ≈6-dic-2026** (un mes desde que llegue al órgano competente; si el órgano la recibe después, corre desde entonces; ampliable a dos). Si no hay respuesta: silencio negativo y reclamación ante el Consejo de Transparencia dentro del mes siguiente [VERIFICAR plazos]. Lo que sigue queda como referencia.

**Qué desbloquea:** el desglose oficial de lo que cobran secretarios de Estado, subsecretarios y directores generales (sueldo, complemento de destino, específico, **productividad**, trienios, extras). Hoy sé que el Portal de Transparencia paga unos 48.000 € más de lo que suma la ley a un secretario de Estado, y que la única explicación posible es la productividad; pero solo tengo **un caso individual y de prensa [S]**. Sin esto, esa cifra no pasa de [VERIFICAR].

**Qué haces:**
1. Abre `research/MANUAL-PARA-JOEL.md`, sección «Solicitud de acceso a la información pública: retribuciones 2024 de altos cargos», y copia el texto.
2. Entra en el Portal de Transparencia (transparencia.gob.es), apartado de **solicitud de acceso a la información** (derecho de acceso). Te pedirá identificarte con **Cl@ve** (certificado, DNI electrónico o Cl@ve PIN). El sistema y el ministerio destinatario exactos los confirma la propia web: en mi texto van marcados [VERIFICAR] porque no los he podido abrir yo.
3. Pega el texto, envía y **guarda el justificante** (número de expediente y fecha).
4. Dime «hecho 1» y el número de expediente: lo anoto en el Seguimiento con la fecha límite. **El plazo legal es de un mes** (ampliable a dos si el asunto es complejo); la respuesta llega a tu correo o a la sede.

**Extra opcional (un párrafo más para el mismo escrito):** *«Solicito también el número de altos cargos y de personal eventual (artículos 10 y 11 de los Presupuestos Generales prorrogados) por ministerio, a 1 de enero de 2024 y de 2025.»* Con eso cierro la otra laguna que no tiene tabla oficial: cuántas personas hay por ministerio (hoy [VERIFICAR]).

**Cuando llegue la respuesta:** me la pasas (PDF o texto) y actualizo las cifras. Si responden «no obra en nuestro poder» o deniegan, también es un dato: lo anoto tal cual.

---

## 2. SEPE: paro registrado de 2024 (0 minutos tuyos si me das OK)

**Qué desbloquea:** poner 2024 junto a 2025 en paro y prestaciones, que es lo que falta para cerrar la comparación 2024/2025 de España.

**Por qué no lo he hecho:** el SEPE solo publica esas cifras dentro de **24 Excel mensuales** (enero a diciembre de 2024 y de 2025) y tu regla es que descargar un archivo necesita tu permiso.

**Opción A (recomendada):** me escribes **«OK descarga SEPE»**. Los bajo con `curl` a una carpeta temporal fuera del repo, los leo y los borro.
**Opción B (a mano):** abre https://www.sepe.es/HomeSepe/que-es-el-sepe/estadisticas/estadisticas-prestaciones/informe-prestaciones.html y baja los informes de 2024 (`Informe-202401` a `202412`). Me basta con el de **diciembre de 2024** y el de **diciembre de 2025** para tener el año cerrado; los intermedios son opcionales.

**Aviso del propio SEPE:** los datos de subsidios desde noviembre de 2024 son provisionales; lo marcaré así.

---

## 3. Tesoro Público: vida media y coste medio de la deuda — HECHO el 6-nov-2026

**Estado:** Joel bajó el boletín de octubre de 2026 y ya está volcado (nominal, vida media, tipo medio, financiación 2026). Pendiente solo el perfil de vencimientos (pág. 30), que mi lector no extrae [VERIFICAR]. Lo que sigue queda como referencia.

**Qué desbloquea:** cuánto cuesta la deuda de España y cuánto tarda en vencer. Hoy tengo el **saldo por ISIN** (página oficial legible), pero **no** la vida media, el tipo medio ni las financiación de 2026, porque van en PDF/Excel que mis herramientas no leen desde la web.

**Lo comprobé el 6-nov-2026 en la web del Tesoro (Chrome):** la página de «Estadísticas Mensuales» tiene un **boletín completo de octubre de 2026** y, además, cada tabla suelta. Lo más cómodo es bajar solo el boletín:
- **Un solo archivo (recomendado):** https://www.tesoro.es/documents/d/tesoro/estadisticas_es-pdf («Boletín estadísticas octubre 2026»). Contiene todas las tablas de abajo.
- Si prefieres tablas sueltas (cada una también existe en Excel, cambiando `-pdf` por `-xlsx`): `02` Vida media de la Deuda del Estado · `03` Tipo de interés medio de la Deuda del Estado · `09` Evolución de la financiación del Estado en 2026 · `11` Subastas (nominal emitido y rendimientos 2026-2025). Otras útiles: `01` nominal en circulación, `13` financiación neta 2026 y 2025, `14` perfil de vencimientos anual.
  Enlace de cada una: `https://www.tesoro.es/documents/d/tesoro/NN-pdf` (con NN = 02, 03, 09, 11…).
- Página de origen (ojo: lleva «í» con tilde): https://www.tesoro.es/deuda-publica/estad%C3%ADsticas-mensuales. Mi enlace anterior iba sin esa tilde y daba «Página no encontrada».

**Qué haces:** abre el enlace del boletín y guarda el PDF en **Descargas** (si el navegador lo abre en pantalla, usa «Guardar como»). Me escribes «hecho 3». Yo lo leo desde Descargas, saco vida media, tipo medio, financiación y vencimientos, y los vuelco con fecha y nivel [P]. El archivo no entra en el repo.

---

## 4. Inversión de Adif y capítulo 6 de Transportes (solo si quieres el nivel de detalle)

**Qué desbloquea:** cuánto se invierte realmente en infraestructura ferroviaria, para contrastar con la recaudación (pedido de C78).

**Paso previo mío (no lo hagas tú todavía):** busco con Chrome la URL exacta del tomo de Presupuestos / ejecución de la Sección 17 y de Adif en `sepg.pap.hacienda.gob.es`, y te la paso lista. Hoy no la tengo (Adif dio 404). **Tú solo descargarás el PDF** cuando te dé el enlace.

---

## 5. Subvenciones a CEAR (BDNS) (10 minutos, opcional)

**Qué desbloquea:** cuánto dinero público recibe la Comisión Española de Ayuda al Refugiado, para el bloque de inmigración.

**Por qué es manual:** la API de la Base de Datos Nacional de Subvenciones no deja filtrar por beneficiario y no he podido leer su respuesta.

**Qué haces:** entra en el portal público de la BDNS (infosubvenciones.es), busca en **concesiones** por el nombre del beneficiario «Comisión Española de Ayuda al Refugiado» y el año, y guarda el resultado en Excel/CSV (botón de exportar). Ruta exacta de menús: [VERIFICAR], porque no la he podido recorrer yo. Dime «hecho 5».

---

## Lo que NO necesita nada tuyo (para que no te quedes con la duda)

- **IGAE, planes de control:** son PDF de poco valor para el tablero; los dejo [VERIFICAR] y no te pido nada.
- **IPC por programa y centro** del presupuesto: es un cálculo mío posterior; no necesita datos nuevos.
- **Cierre definitivo del presupuesto de 2024 (IGAE):** cuando se publique, lo leo yo con Chrome.
- **Resultado de la solicitud del paso 1:** llega solo por correo.

## Cómo lo vamos cerrando

Cuando me digas «hecho N» o «OK descarga SEPE», hago lo siguiente sin más preguntas: leer, volcar a `espana-manual.json` con fuente y nivel, regenerar móvil y Órbita, actualizar `research/tareas.csv` y enseñarte el `git status` antes de subir. Nada de esto cuesta cuota de Claude fuera de la lectura (sin API de Anthropic).
