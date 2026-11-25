# Panel de tráfico en Ormuz (IMF PortWatch) · 25-nov-2026

- Fuente [P]: IMF PortWatch, API ArcGIS `Daily_Chokepoints_Data` (acceso libre, sin clave). Retraso 2-3 días.
- `scripts/leer_portwatch.py` -> `explorador/ormuz-portwatch.json` (363 días, último 22-nov; campos fecha, total, petroleros).
- Cargado en `explorador.py` como `datos["ormuz"]`; bloque en `pCumbres` solo si la cumbre trae `"osint": "ormuz"` (puesto en `iran-ormuz-2026-11-24`).
- Lectura (hecho medido por AIS): último día 1 buque y 0 petroleros; media 7 días 2,7 buques/día frente a 67,8 en ene-feb 2026 (-96 %); petroleros 0,3 frente a 37/día. Tabla semanal: ver Órbita > Cumbres > Irán-Ormuz.
- [VERIFICAR] la causa (cierre, guerra, AIS apagado en flota en la sombra): PortWatch no la explica; cotejar con UKMTO y agencias.
- Se añade el paso al flujo `paneles.yml` (sin IA, sin claves; no lanzado).
