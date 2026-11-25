# Auditoría independiente del lote 3 de Cumbres (25-nov-2026)

Entradas: `g7-evian-2026-06-15`, `jackson-hole-warsh-2026-08-28`, `brics-nueva-delhi-2026-09-12` de `explorador/cumbres.json`. Método: lectura en Chrome (pestaña propia, cerrada) y cotejo con `explorador/precios_historico.json`. No se editó `cumbres.json`; las correcciones propuestas están en el archivo `fix-lote3.json` del scratchpad.

## G7 Évian

| Elemento | Resultado | Fuente |
|---|---|---|
| Cita «the right of transit passage without restrictions or tolls is the bedrock of international trade» | Literal | Élysée, declaración geopolítica, 17-jun-2026 |
| «strengthen our sanctions, including those on the oil and gas sectors» y «the right moment to proceed with additional measures» | Literales | Ídem |
| «historic opportunity to prevent Iran from acquiring any nuclear weapon» | Literal | Ídem |
| Declaración de crecimiento: «have been persistent and have widened in recent years», «more emphasis on forward-looking scenarios», «arbitrary export restrictions», «excessive dependencies» | Literales; no hay «tariff» ni «China» | Élysée, declaración de crecimiento |
| Reserva de 90 días de la AIE | Está en la declaración de crecimiento (no en la geopolítica) | Élysée |
| Taiwán (declaraciones[2]) | Era traducción entre comillas; el original es «in particular by force or coercion». Corregir | Élysée, geopolítica |
| «Más de mil millones de dólares» para el ébola; nueve declaraciones; invitados India, Kenia, Corea del Sur, Brasil, Egipto | Correctos | Élysée, resultados |
| «No hay: activos rusos congelados, precios tope, flota en la sombra, aranceles» | Confirmado: las palabras no aparecen | Élysée |
| «China solo aparece como participante de la cumbre del 11-jun» | Inexacto: también aparece en «East and South China Seas». Corregir | Élysée, geopolítica |
| Cita del funcionario francés | Literal, pero dicha antes de la cumbre, no el 17-jun. Matizar | TimesLive/Reuters |
| Trump–Zelenski del 16-jun («very good»), Altman y Amodei «expected» | Correctos | TimesLive/Reuters |
| Niveles P/S | Correctos: P en textos Élysée, S en prensa y anónimo | |
| Mercado (Brent 87,33 a 79,55 entre el 12 y el 17-jun) | Coincide | precios_historico.json |
| G7 Research Group (182 compromisos) | No se pudo abrir (la navegación no se completó); sigue [VERIFICAR] | |
| Chatham House | No reabierta (403 ya conocido); sigue [VERIFICAR] | |

## Jackson Hole (Warsh)

| Elemento | Resultado | Fuente |
|---|---|---|
| «The responsibility for 65 months of sustained, elevated inflation sits squarely with the central bank.» | Literal | federalreserve.gov, discurso 28-ago-2026 |
| «I stand here today committed to a discipline, not to a decision.» | Literal (apartado Conclusion) | Ídem |
| «But progress over the past two years has been modest.» | Literal; pero firmado[0] decía «desde 2022». Corregir | Ídem |
| PCE 3,7 % (12 meses), 4,1 % (seis meses), paro 4,1 % | Correctos | Ídem |
| «overstayed its welcome», «hall-of-mirrors», «meaningfully improved» | Literales | Ídem |
| Actas de julio: «good majority… await new information» | Correcto | Ídem |
| No menciona stablecoins ni balance de la Fed; «payments» solo en el título | Confirmado leyendo el texto oficial; se pueden cerrar los [VERIFICAR] | Ídem |
| Task force de productividad y empleo; base monetaria y velocidad | Correcto | Ídem |
| Posen | PBS lo da como cita literal («You are basically setting yourself up…»); la entrada decía paráfrasis. El artículo es de AP y del 29-ago | PBS/AP |
| Cook asistió, Rogoff almuerzo, foto con Macklem y Bailey, 10 años «barely rose» | Correctos | PBS/AP |
| «Ovación a Powell 2025 (Fortune)» | Está en PBS/AP, no en Fortune. Corregir fuente | PBS/AP; Fortune |
| Fortune | Existe (Bloomberg, 29-ago); no se leyó entera | Fortune |
| Kansas City Fed | La página existe (título coincide); contenido no leído | kansascityfed.org |
| Hora del discurso (10:00 ET) | No figura en el texto oficial; sigue sin confirmar | |
| Mercado: 10 años 4,672 a 4,72 a 4,758 %; oro 4.664 a 4.530; BTC y XRP a la baja el 28-ago | Coinciden | precios_historico.json |
| Niveles P/S | Correctos | |

## BRICS Nueva Delhi

| Elemento | Resultado | Fuente |
|---|---|---|
| Texto oficial | Leído en Chrome. La URL cargó con sufijo `-september-12-2026`. Sin 403 | pmindia.gov.in |
| Fechas | 12 y 13-sep-2026 (párr. 1 oficial; Al Jazeera «two-day summit», adopción el sábado 12). «13-14» era un error | pmindia.gov.in; Al Jazeera; Wikipedia |
| 140 párrafos | Correcto; último párrafo apoya a China como presidencia 2027 | pmindia.gov.in |
| «serious concern over the rising use of unilateral tariffs» | No literal. El texto dice «We voice serious concerns about the rise of unilateral tariff and non-tariff measures…» (párr. 21). Corregir | pmindia.gov.in |
| «unilateral coercive measures that are contrary to international law» | Literal (párr. 22) | Ídem |
| «practical solutions for cross-border payments among member countries» | No literal: «among BRICS countries». El texto oficial sí cita monedas locales y la BRICS Cross-Border Payments Initiative; la entrada decía lo contrario | pmindia.gov.in (párr. 90) |
| «growing risks of nuclear danger and conflict» | Literal (párr. 25) | Ídem |
| Oriente Medio | Sí hay párrafo (28: «maximum restraint»); Business Today no lo recogía | Ídem |
| Ucrania; desdolarización | No aparecen | Ídem |
| Carbon border adjustment mechanisms | Confirmado: rechazados como medidas unilaterales | Ídem |
| India y Brasil en el Consejo de Seguridad | Párr. 13 | Ídem |
| Risk Lab en GIFT City | «members expressed interest»; confirmado | Ídem |
| Troika, Red de Marinos, 10 propuestas | No están en la Declaración; son de Modi según AIR (S) | AIR |
| Citas de Modi (declaraciones[1]) | AIR usa estilo indirecto; no son palabras literales. Corregir | AIR, 12-sep-2026 |
| Business Today | No contiene las citas atribuidas | Business Today |
| Al Jazeera | Cotejado: 11 miembros, Putin y Xi asistentes, Iran–UAE, Donthi (ICG), sanciones sin ONU, Rio 2025 «blatant breach» | Al Jazeera, 13-sep |
| Asistentes | Wikipedia (S): Xi, Putin, Modi, Pezeshkian, Ramaphosa, Sisi, Prabowo, Abiy; Brasil con el ministro Mauro Vieira (no Lula); EAU con Khaled bin Mohamed Al Nahyan; Arabia Saudí no participó. Sin fuente primaria | Wikipedia |
| Mercado: DXY 99,12 / 99,46 / 99,65; Brent 104,61 a 108,75; WTI 100,05 a 105,83; S&P 7.657 a 7.586 | Coinciden | precios_historico.json |
| Niveles P/S | declaraciones[0] pasa de S a P con el texto oficial; el resto de S/R es correcto | |

## Pendiente tras la auditoría
- Aplicar `fix-lote3.json` en `cumbres.json` (no hecho aquí).
- G7: abrir la evaluación del G7 Research Group y Chatham House; leer los textos de minerales críticos e IA.
- BRICS: lecturas de China y Rusia y lista oficial de asistentes.
- Jackson Hole: hora del discurso y lectura completa de Fortune y de la nota del Kansas City Fed.
