# T22 — XRPL y Stellar: enmiendas, seguridad post-cuántica, DEX/AMM y TVL

Hecho el 22-oct-2026 (≈ 20:00 UTC). Sin recomendaciones ni predicciones de precio. [P] = fuente primaria leída hoy; [S] = prensa/terceros; [VERIFICAR] = sin comprobar.

## 1. Enmiendas del XRPL
**Hechos**
- **fixCleanup3_4_0 sigue sin activarse** y ya tiene mayoría: la consulta JSON-RPC `feature` a dos nodos públicos (s1.ripple.com y xrplcluster.com) devuelve `enabled: false` y `majority: 845909182` (segundos desde la época de Ripple) = **21-oct-2026 14:46:22 UTC** [P, ledger]. Con 14 días de espera, la activación más temprana es el **4-nov-2026 14:46 UTC**, que coincide con XRPLWin/CoinDesk [S] y confirma el aplazamiento desde el 23-oct (09:34 UTC).
- Causa del aplazamiento: en el control de las 12:54 UTC del 21-oct los apoyos bajaron a 26 de 35 (hacen falta 29, más del 80 %) y reinició la cuenta atrás; volvió a 29 a las 14:46 y hoy hay 31 de 35 [S: CoinDesk con XRPL Dashboard y XRPLWin; el recuento por validador no se pudo leer en fuente primaria → [VERIFICAR]]. Si baja de 29 en cualquier control, se reinicia otra vez. Quien no responde cuenta como «no».
- Contenido (xrpl.org, Known Amendments [P]): paquete de arreglos de Single Asset Vaults, Lending Protocol, AMM (p. ej. `AMMClawback` retira del todo al último titular de LP), DEX con permisos, trust lines, NFT, MPT, Escrow, Sponsorship, delegación de permisos y prefijos de firma nuevos. CoinDesk añade que cierra un resquicio por el que una cuenta con permiso solo de quemar podía crear tokens [S].
- **LendingProtocol** y **SingleAssetVault** siguen `enabled: false` [P, ledger]. Votos: 19 y 21 de los 29 necesarios (CoinDesk, 19-oct) [S]; ninguna ha iniciado su cuenta atrás. Hay además `LendingProtocolV1_1`, `Sponsor`, `DynamicMPT`, `ConfidentialTransfer` y `XChainBridge` sin activar [P, ledger].
- **Versión 3.4.1:** publicada el 25-sep; corrige un desbordamiento entero del motor de pagos (podría haber creado XRP por encima del suministro; sin explotación observada) y un fallo de validación de lotes (`fixBatchV1_2`, activada en Mainnet el 9-oct) [P: informe de divulgación de xrpl.org]. Sin pérdida de fondos según el propio informe.

**Lectura (opinión)**: el aplazamiento no es un fallo de red; es el mecanismo de umbral funcionando. Lo relevante para el seguimiento es que el margen es estrecho (29 justos el 19-oct) y que préstamos y vaults dependen de nuevos votos. [ESPECULACIÓN] sobre cuándo se logrará.

## 2. Seguridad post-cuántica
| | XRPL (Ripple) | Stellar (SDF) |
|---|---|---|
| Documento | ripple.com/insights/post-quantum-readiness-on-the-xrp-ledger (20-abr-2026) [P, empresa] | stellar.org, «Quantum Preparedness Plan» (9-jun-2026) [P, fundación] |
| Fase en curso | 2.ª (1S-2026): evaluación del riesgo y pruebas de algoritmos NIST; 3.ª (2S-2026): firmas candidatas en Devnet junto a las actuales | Etapa 1 (2026): verificación de firmas ML-DSA-44/65 en Soroban (funciones nativas) y cuentas de contrato |
| Transición completa | Enmienda de firmas post-cuánticas, objetivo «2028 como máximo» | Etapa 2 (2027): firmante seguro en cuentas clásicas; Etapa 3: retirada de Ed25519, fecha sin fijar |
| Contingencia | Plan «Q-Day»: dejar de aceptar firmas clásicas y recuperar fondos con pruebas de conocimiento cero | Recuperación con semilla en estudio; firmas del consenso (SCP) en una mejora aparte, sin algoritmo ni fecha |
| Ya existe | Rotación nativa de claves; prueba de concepto ML-DSA en AlphaNet; trabajo con Project Eleven | Separación entre dirección y clave; rotación con `set_options` |
- Ninguna de las dos webs confirma que los hitos del 1S-2026 estén cumplidos (Ripple: «no se confirma») → [VERIFICAR] en el repositorio o la hoja de ruta.
- Auditoría de un validador (Vet, abr-2026): ~300.000 cuentas con 2.400 M XRP nunca han enviado fondos, así que su clave pública no está expuesta [S: CoinDesk]. Es cifra de un tercero, [VERIFICAR].
- Sesgo: ambos planes son documentos de la propia organización, con interés en mostrar preparación; CoinDesk (21-abr) tituló la hoja de ruta como «viento a favor» para el precio, lectura que no es un hecho.

## 3. DEX, AMM y TVL (hoy, DefiLlama [S] salvo indicación)
| | XRPL | Stellar |
|---|---|---|
| TVL | **$39,2 M** (R43: máx. $119,9 M el 18-jul-2025) | **$236,9 M** (R43: máx. $272,8 M el 1-oct-2026) |
| Volumen DEX 24 h | **$5,4 M** | **$1,4 M** |
- Ambas cifras son de DefiLlama [S]; no incluyen todo lo que hay en cadena. El estado del ledger se lee directo del nodo y el detalle (AMM XRP/RLUSD ≈ $4,8 M; 79 % de operaciones de Stellar contra pools) está en `informes/research/2026-10-17-R43-dex-amm-xrpl-stellar-profundo.md` [P/S según allí].
- Cambio en cinco días: XRPL TVL $39,1 M → $39,2 M; Stellar $230,3 M → $236,9 M; XRPL DEX $6,2 M → $5,4 M; Stellar $1,7 M → $1,4 M (R43 vs hoy). No es tendencia.

## 4. Alcista vs. bajista (análisis, no recomendación)
- **A favor del uso:** Stellar con TVL +76 % interanual (R43) y USDC en Soroban; el XRPL sigue añadiendo funciones (vaults, préstamos, AMM) y corrige errores críticos con rapidez (3.4.1 en tres días).
- **En contra:** el TVL de XRPL está −51 % en un año y el volumen DEX es de unos millones de dólares; préstamos sin colateral dependen del juicio externo del bróker; el desbordamiento de XRP, aunque no explotado, existía en 3.4.0 y anteriores; las apuestas de «preparación cuántica» son planes, no despliegues.
- **Sesgos:** DefiLlama es un agregador; CoinDesk informa con titulares de precio; Ripple y SDF hablan de sí mismas.

## 5. Qué vigilar
1. **4-nov 14:46 UTC:** activación de fixCleanup3_4_0 si no baja de 29 votos (comprobar con la consulta `feature` y con XRPL Dashboard).
2. Votos de LendingProtocol y SingleAssetVault (19 y 21 de 29 el 19-oct).
3. Swell (27-29 oct) y Meridian (28-29 oct): anuncios de producto, siempre desde fuente de la empresa.
4. Hitos de Devnet de firmas post-cuánticas (2S-2026) y la etapa 1 de Soroban.

## Fuentes
xrpl.org (Known Amendments, divulgación de vulnerabilidades 3.4.1); nodos públicos s1.ripple.com y xrplcluster.com (método `feature`); ripple.com/insights; stellar.org; DefiLlama (chains y DEX); CoinDesk (19-oct, 22-oct, 21-abr, 28-ago); R43 del repo.
