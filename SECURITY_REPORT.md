# 🟡 REVISAR — Informe de seguridad

**Fecha:** 2026-10-22 · **Última comprobación:** 2026-10-28, 🔴→🟡 el script marcó que CISA KEV añadió el 27-oct el CVE-2026-111497 (Brotli) como explotado activamente; comprobado a mano: sin exposición en el código; solo queda por saber el Brotli del Chromium de `despertador.yml` (no comprobado; solo visita nuestra propia app de Streamlit) (no repetir búsquedas ya hechas hoy) · Repositorio público: este informe no incluye datos del equipo local.

## Resumen
1. El aviso del vídeo se **confirma en lo esencial** en fuentes oficiales: hay parches de seguridad en Node.js (21-oct), Python (1-oct y 21-oct), Go (8 y 19-oct) y Java (Oracle CPU, 20-oct); en Rust no hay aviso oficial del lenguaje en octubre.
2. El fallo de ejecución remota sin autenticación existe: **CVE-2026-111497**, desbordamiento en el decodificador de **Brotli** (NVD, CVSS 4.0 = 9,2 crítica). **No afecta al proyecto**: no usa Node ni Java ni Go ni Rust, y la librería `brotli` no está instalada en Python.
3. Lo de los «≈7 certificados» es real pero con matices: son **8 certificados intermedios de eMudhra** con claves comprometidas (Mozilla, 17-oct). El proyecto ya está cubierto: `certifi 2026.10.19` retira una raíz de eMudhra.
4. Auditoría del proyecto: **0 vulnerabilidades** en 79 paquetes de Python y en las GitHub Actions; **0 secretos** en el código y en los 728 commits; **0** verificaciones TLS desactivadas.
5. Quedan decisiones pendientes (observaciones de endurecimiento y elementos fuera del repositorio); ver «Pendiente de decisión».

## Qué usa el proyecto
Python (única dependencia real): app con `uv` (Python 3.14.8, OpenSSL 3.5.9), workflows en Python 3.12 (`ubuntu-24.04`), devcontainer en Python 3.11. Paquetes: streamlit 1.66.1, pandas 3.1.0, numpy 2.5.4, plotly 7.1.0, requests 2.34.2, jinja2 3.1.6, anthropic 2.1.0, urllib3 2.8.0, certifi 2026.10.19, y otros (79 en total). Extras: feedparser, playwright, markdown, openpyxl, pypdf, tzdata. JavaScript: solo `docs/sw.js` (sin dependencias). Sin Go, Rust ni Java.

## Hallazgos
| ID | Gravedad | Versiones afectadas | Corregida en | Fuente | ¿Me afecta? |
|---|---|---|---|---|---|
| **CVE-2026-111497** (desbordamiento en el decodificador Brotli; ejecución remota sin autenticación) | **Crítica** (CVSS 4.0: 9,2) | Brotli 1.0.3–1.2.0; Node 22.x, 24.x, 26.x | Node 22.23.4, 24.22.1, 26.12.1 (NVD no da versión de Brotli) | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [Node.js, 21-oct-2026](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) | **No** en el código (sin Node; `brotli`/`brotlicffi` no instalados en Python). **No se puede saber** para el Chromium que descarga Playwright en `despertador.yml`: no comprobada su versión de Brotli |
| CVE-2026-105483, CVE-2026-106069, CVE-2026-106072 (comprobación de nombre de host TLS evitable) | Alta, Alta, Media | Node 26.x y 24.x (105483); 26.x, 24.x y 22.x (las otras) | 22.23.4 / 24.22.1 / 26.12.1 | [Node.js, 21-oct-2026](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) | No (sin Node) |
| Otros seis de Node del 21-oct: CVE-2026-105482, -105481, -106074, -106070, -106071, -106073 | Alta a Baja | 22.x–26.x | ídem | ídem | No (sin Node) |
| **Certificados intermedios de eMudhra** (8, claves comprometidas; sin CVE) | n/d | Lista de CA anterior a la retirada (certifi ≤ 2026.7.22) | certifi 2026.10.19 | [Mozilla, 20-oct-2026](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/) · [Python 3.14.9](https://www.python.org/downloads/release/python-3149/) | **Corregido**: el proyecto resuelve `certifi 2026.10.19`, que ya no incluye «emSign ECC Root CA - G3» (comparado con 2026.7.22; Mozilla no nombra la raíz retirada, esa identificación es inferencia propia). `requirements.txt` no fija certifi: un entorno en caché anterior podría tener el antiguo |
| Python: CVE-2026-19553, -15310, -19672, -19445, -17084, -15806 (todas las ramas), -82049 y -87910 (3.10–3.13) | Variada (TLS, tarfile, zipfile, IDNA, credenciales) | Anteriores a 3.14.8 / 3.13.16 / 3.12.15 / 3.11.17 | 3.14.8, 3.13.16, 3.12.15, 3.11.17 (1-oct-2026) | [blog.python.org](https://blog.python.org/2026/10/python-31022-31117/) | App local (Python 3.14.8): corregido. Uso real de los módulos: `zipfile` solo para leer xlsx propios; no usa `tarfile`, `wrap_bio` ni `HTTPPasswordMgr` |
| CVE-2026-12345 (`tempfile.TemporaryDirectory`, carrera con enlaces simbólicos; local) | Media (CVSS 4.0: 5,9) | CPython anterior a 3.14.9 | 3.14.9 (21-oct-2026, «expedited security release») | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12345) · [python.org](https://www.python.org/downloads/release/python-3149/) | Riesgo bajo: `tempfile` solo en `scripts/maquetar_pdf.py` y `estudio_eventos.py`, que se ejecutan en local sobre archivos propios |
| Go: correcciones de seguridad en go1.27.2 y go1.26.9 (8-oct: `go`, `crypto/tls`, `html/template`, `net/http`, `net/textproto`, `os`) y go1.27.3 / go1.26.10 (19-oct: `crypto/x509`) | No indicada | Versiones anteriores | Las citadas | [go.dev/doc/devel/release](https://go.dev/doc/devel/release) | No (sin Go). La página no lista CVE |
| Java: Oracle CPU de octubre 2026 (20-oct): 55 parches de Java SE, 49 explotables por red sin autenticación según Oracle | Variada | JDK 8u, 11, 17, 21, 25, 27 anteriores | 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.33, 8u511 | [Oracle CPU oct-2026](https://www.oracle.com/security-alerts/cpuoct2026.html) | No (sin Java) |
| Rust: sin aviso oficial del lenguaje en octubre. El de Cargo (CVE-2026-33056) es de marzo (corregido en 1.94.1). Avisos de crates (rustls RUSTSEC-2026-0346 a 0349 y otros) | Baja a media | n/d | rustls 0.23.46 | [Blog de Rust](https://blog.rust-lang.org/2026/03/21/cve-2026-33056/); crates: **no verificado** en rustsec.org (solo vi referencias de terceros) | No (sin Rust) |
| CISA KEV (octubre 2026) | n/d | n/d | n/d | [Catálogo KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | **Actualizado 28-oct:** KEV añadió el 27-oct CVE-2026-111497 (Google Brotli, valor de retorno sin comprobar; vencimiento CISA 10-nov; corregido en Brotli 1.2.1) como explotado activamente. En el código: no afecta (`brotli`/`brotlicffi` no están y `requirements.txt` no los pide). Sin comprobar: el Chromium de Playwright en `despertador.yml` (solo abre nuestra app de Streamlit; el runner se destruye en cada ejecución). Resto de entradas de octubre (Adobe Commerce, PHP): no nos nombran |

## Veredicto sobre las afirmaciones del vídeo
| Afirmación | Resultado |
|---|---|
| Parches de seguridad en Node, Python, Java, Rust y Go | **Confirmado** para Node, Python, Java y Go; **no confirmado** para el propio lenguaje Rust (solo avisos de crates y uno de marzo) |
| Al menos un fallo de ejecución remota sin autenticación | **Confirmado**: CVE-2026-111497 (NVD: «remote unauthenticated attacker»); además Oracle indica 49 fallos de Java SE explotables sin autenticación |
| ≈7 certificados o claves comprometidos con riesgo de suplantación e interceptación | **Confirmado con matiz**: 8 intermedios de eMudhra, claves de generación débil, bloqueados por Mozilla (OneCRL, 17-oct) y retirada la raíz del almacén de confianza; eMudhra dice que no emitió certificados finales con ellos y abandona el negocio de TLS global |

## Auditoría del proyecto (22-oct-2026)
- `pip-audit` (79 paquetes, con los extras de scripts y workflows): **sin vulnerabilidades conocidas**. OSV para certifi, requests, urllib3, streamlit y anthropic: 0. OSV para `actions/checkout`, `actions/setup-python` y `actions/cache`: 0. No aplican `npm audit`, `govulncheck` ni `cargo audit` (no hay esos ecosistemas); `osv-scanner` no está instalado (su función queda cubierta con la API de OSV y `pip-audit`; si lo quieres, instálalo desde github.com/google/osv-scanner).
- **Secretos:** 0 coincidencias de patrones de claves (Anthropic, GitHub, AWS, Slack, Google, claves privadas y tokens de Telegram) en los archivos rastreados y en el historial de los 728 commits de todas las ramas. `privado/` está ignorado y no hay archivos suyos rastreados. Los workflows leen los secretos con `secrets.*`.
- **TLS:** 0 usos de `verify=False`, `rejectUnauthorized`, `CERT_NONE`, `NODE_TLS_REJECT_UNAUTHORIZED` ni contextos sin verificar.
- Rutina repetible: `python scripts/seguridad_rapida.py` (14 s, sin IA).

## Pendiente de decisión
1. **Observaciones de endurecimiento (no son vulnerabilidades):** 5 workflows sin bloque `permissions` (`alertas`, `despertador`, `escrow`, `eventos`, `onchain`); `pip install` sin versión fijada en 8 workflows (cadena de suministro); acciones fijadas por etiqueta y no por SHA; el devcontainer arranca Streamlit con CORS y XSRF desactivados (solo Codespaces). No se han tocado.
2. **`despertador.yml`:** descarga Chromium en cada ejecución; conviene confirmar que su versión incluya la corrección de Brotli.
3. Elementos del equipo local, fuera del repositorio: se comunican en el chat, no se publican aquí.

## Cambios aplicados
Ninguna actualización de dependencias: no había ninguna vulnerabilidad confirmada que afectara al proyecto. Solo se añade `scripts/seguridad_rapida.py` y este informe.
