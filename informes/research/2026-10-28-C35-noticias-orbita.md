# C35 · Noticias en la Órbita con caducidad (28-oct-2026)

Hecho sin IA de pago ni web: `scripts/noticias_a_orbita.py` lee git local y archivos del repo. Informativo; no es recomendación de compra ni venta. Los titulares son [S] salvo que la ficha diga [P].

## Qué hace
- **Entrada:** noticias del bot (rama `datos`, que ya incluye las manuales C18) y `noticias/manuales/*.json`, con nota ≥ 7, no marcadas como bulo, de las últimas 72 h y con enlace. Se omiten las que mencionan cartera o tesis (repo público).
- **Capa por tema:** Petróleo y Ormuz → `energia`; Economía y mercados → `liquidez`; Regulación y Cripto y regulación → `reg`; XRP / Ripple y Stellar / XLM → `puente`. **Geopolítica y política no tiene capa**: se cuenta como «sin capa» y se lleva a C30 (hoy 0 en la ventana de 72 h).
- **Ficha en el movimiento** (`origen: "noticia"`): `url`, `nivel` P/S, `tema`, `frecuencia` (24h/7d/30d/fija), `revisado` y `caduca` (fecha), `nota_bot`. `revisar` se queda como en el esquema común (verdadero/falso); la frecuencia va en `frecuencia`.
- **Caducidad:** 24h → caduca a los 2 días; 7d → 14; 30d → 60; fija → nunca. Si la noticia vuelve a salir, se renueva `revisado`.
- **Tope:** 5 vigentes por capa; el resto pasa al archivo con motivo «tope».
- **Retirada sin borrar:** las vencidas van a `explorador/noticias-archivo.json` (`estado_vida: "archivada"`, fecha y motivo). Lo escrito a mano en `datos.json` no se toca.

## Resultado de la primera pasada
20 noticias vigentes (5 en cada una de Liquidez, Energía, Puente y Regulación) y 1 archivada por tope. Es idempotente: una segunda pasada da lo mismo. `revisar_explorador.py`: 0 avisos en 12 capas y 83 movimientos.

## Límites y pendiente
- No enganchado aún a `paneles.yml` (se hace cuando Joel lo decida; el workflow tendría que correr antes de `construir_movil.py`).
- No probado a 1920×1080: falta que Joel mire en la app (F11) cómo se ven los 20 movimientos nuevos y que no saturen la capa.
- Hacer visible en la Órbita el enlace «Ver archivo» y la marca de caducidad: no hecho; hoy los campos nuevos están en los datos pero las pestañas no los muestran.
- Las noticias de Google News traen la URL de redirección de Google, no la del medio.
