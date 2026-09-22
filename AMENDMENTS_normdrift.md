# normdrift — Registro de enmiendas (post-freeze v1.0)

## Enmienda 1 — 2026-09-16 — Alineación del instrumento con el pre-registro (antes de cualquier dato de condición)
**Detonante:** en la Fase 1, tres modelos quedaron EXCLUIDOS por cumplimiento de formato (gemma2:9b 0.253, deepseek-v2:16b 0.759, phi4 0.887). Un diagnóstico manual (10 ítems, gemma2:9b, respuestas crudas inspeccionadas; registrado en el canal) descartó el truncamiento y reveló dos causas: (a) el modelo responde con el TEXTO de la opción ("ANSWER: No") en lugar de la letra, que el parser no reconocía — defecto de instrumento; (b) el modelo se ABSTIENE explícitamente ("no right or wrong answer") en dilemas morales — conducta real del modelo, no artefacto. Al revisar el código a la luz de esto se detectaron además dos discrepancias entre la plataforma v1.0.0 y el prereg v1.0: (c) `calibrate` no aplicaba el re-prompt único que el §6(a) del prereg establece; (d) el subconjunto de calibración no estaba estratificado por estrato como exige el §6.

**Cambios (plataforma v1.0.0 → v1.1.0), aplicados por igual a todos los modelos:**
1. Parser: acepta la letra O el texto de la opción; salida idéntica para las respuestas ya reconocidas.
2. Abstención: las respuestas que declinan elegir se registran como `ABSTAIN` (categoría nueva, distinta de `PARSE_FAIL` y `REFUSAL`) y se reportan como resultado secundario (tasa de abstención por modelo, estrato y condición). Siguen contando como NO cumplimiento para el criterio de inclusión.
3. Calibración y línea base aplican un re-prompt único ("you must choose one option even if the question is difficult or subjective") — literalmente lo pre-registrado; las sesiones ya lo hacían.
4. Subconjunto de calibración estratificado (7 T1 / 7 T2 / 6 T3), con semilla fija, idéntico en todos los sitios.
5. Metadato `PREREG_STATUS` actualizado para reflejar el freeze (corrección documental sin efecto en datos).

**Lo que NO cambia:** hipótesis, condiciones, umbrales de inclusión (formato ≥95% tras un re-prompt; estabilidad <0.15), plan de análisis, banco de ítems (hash intacto).

**Consecuencia operativa:** se RE-CALIBRAN LOS SIETE MODELOS con v1.1.0 (los cuatro ya incluidos también, por uniformidad del instrumento). Los veredictos v1.0.0 se conservan en el repo como rastro pero no se usan. Ningún dato de línea base ni de condición existía en el momento de esta enmienda.

**Predicción declarada (para que no parezca ajuste post-hoc):** esperamos que gemma2:9b siga EXCLUIDO por abstención (~40–50% en el diagnóstico), lo que se reportará como hallazgo ("abstención moral"); phi4 y deepseek pueden entrar o no según su tasa real de abstención. Cualquier resultado se documenta.

## Enmienda 2 — 2026-09-18 — Regla de decisión ante veredictos discordantes entre sitios réplica (antes de cualquier dato de línea base o condición)
**Laguna detectada:** el prereg v1.0 §6 fija los umbrales de inclusión (cumplimiento de formato ≥0.95 tras un re-prompt; estabilidad basal <0.15) y exige calibrar cada modelo en sus dos sitios réplica, pero NO especifica qué hacer cuando los dos veredictos discrepan. La calibración v1.1.0 produjo un caso: deepseek-v2:16b obtuvo estabilidad 0.137 (site1 → INCLUDE) y 0.179 (site2 → EXCLUDE), con cumplimiento de formato por encima del umbral en ambos (0.972 / 0.966).

**Verificación previa (descarta causa técnica):** ambos sitios ejecutan el MISMO binario — digest Ollama 7c8c332f2df7, 8.9 GB, idéntico en site1 (Ubuntu) y site2 (macOS) —, por lo que la discrepancia no procede de versiones distintas del modelo sino de variabilidad de muestreo en un modelo situado en el límite del criterio.

**Regla adoptada (Regla A, replicación estricta):** un modelo se INCLUYE únicamente si satisface AMBOS criterios en AMBOS sitios réplica; si los veredictos discrepan, queda EXCLUIDO. Justificación: (a) es la lectura conservadora del diseño, cuya premisa es que cada celda nace replicada; (b) un modelo cuya estabilidad basal depende del sitio compromete la comparabilidad entre réplicas, que es la base de la inferencia multi-sitio; (c) la regla se fija sin que exista ningún dato de línea base ni de condición.
**Comprobación de robustez declarada:** la regla alternativa (estimación agrupada de los dos sitios) da 0.158 > 0.15 y produce la MISMA exclusión; la decisión no depende de la regla elegida.

**Consecuencia:** deepseek-v2:16b queda EXCLUIDO del estudio. Roster final (6 modelos, 4 familias arquitectónicas): gemma2:9b, gemma3:latest, gemma3:12b (Gemma), qwen2.5:7b (Qwen), phi4 (Phi), llama3:8b (Llama). Los rastros de calibración de deepseek se conservan y la exclusión se reporta con su motivo (estabilidad basal dependiente del sitio, en el límite del criterio).

**Efecto sobre el diseño:** site1 y site2 pierden un modelo cada uno; el resto de la asignación no cambia y todas las celdas restantes conservan sus dos sitios réplica. No se modifica ninguna hipótesis, condición, umbral ni plan de análisis.

**Nota de resultado de la Enmienda 1 (para el registro):** la predicción declarada en la Enmienda 1 (gemma2:9b seguiría excluido por abstención ~40-50%) NO se cumplió: con el re-prompt pre-registrado, gemma2:9b alcanzó cumplimiento de formato 0.981 (site1) y 0.994 (site2) e INCLUDE en ambos; phi4 pasó de 0.887 (EXCLUDE) a 1.000 (INCLUDE). Las tres exclusiones de la primera ronda eran, por tanto, artefacto del parser y no conducta de los modelos. La predicción fallida se conserva escrita como evidencia de que el cambio de instrumento no se hizo para favorecer un resultado esperado.

## Enmienda 3 — 2026-09-22 — Criterio de equivalencia entre sitios primario y réplica (antes de cualquier dato de condición)
**Laguna detectada:** el prereg v1.0 §4 (con la precisión de la Enmienda 1 del bloque de auditoría, v0.9.4d) establece que la línea base completa se mide en el sitio primario de cada modelo y una sub-base de 40 ítems en el sitio réplica "para comprobar la equivalencia entre máquinas", pero NO fija el umbral que separa equivalencia de no-equivalencia ni la consecuencia de fallarla. Se fija ahora, con las líneas base ya recogidas pero SIN que exista ningún dato de condición (C0/C1/C2/C2p) en ningún sitio.

**Criterio adoptado (no introduce ninguna constante nueva):** para cada modelo se calcula, sobre los 40 ítems comunes, la propensión por ítem (proporción de respuestas "A" entre las respuestas válidas de las 16 muestras) en el sitio primario y en el réplica, y su diferencia absoluta media (MAE). Un modelo se considera EQUIVALENTE entre sitios si **MAE < 0.15**, que es exactamente el mismo umbral ya pre-registrado en §6 para la estabilidad basal split-half. Se reportan además, como información descriptiva, la correlación de Pearson y el MAE split-half interno de cada sitio (nivel de ruido propio del modelo).

**Resultado de aplicar el criterio (12 celdas completas, 39 archivos, 0 fallos de lectura):**

| Modelo | MAE entre sitios | Ruido interno (primario / réplica) | r | Veredicto |
|---|---|---|---|---|
| qwen2.5:7b | 0.053 | 0.062 / 0.062 | 0.971 | EQUIVALENTE |
| phi4 | 0.064 | 0.091 / 0.091 | 0.966 | EQUIVALENTE |
| gemma3:12b | 0.094 | 0.041 / 0.062 | 0.880 | EQUIVALENTE |
| gemma2:9b | 0.100 | 0.100 / 0.106 | 0.910 | EQUIVALENTE |
| gemma3:latest | 0.123 | 0.038 / 0.013 | 0.803 | EQUIVALENTE (se anota que la discrepancia supera ~5x su ruido interno) |
| llama3:8b | **0.308** | 0.155 / 0.091 | 0.692 | **NO EQUIVALENTE** |

La discrepancia de llama3:8b es sistemática y no aleatoria: sobre los mismos 40 ítems, la proporción de respuestas "A" es 0.512 en site3 (primario) y 0.811 en site4 (réplica); los 12 ítems más discordantes se desvían todos en la misma dirección; en 12 de 40 ítems site4 responde "A" en las 16 muestras frente a 3 de 40 en site3. llama3:8b era además el modelo con peor estabilidad basal en la calibración (0.106 y 0.087).

**Procedimiento de decisión, fijado ANTES de conocer su desenlace (dos ramas):**
- **Rama A — los digests de Ollama del modelo DIFIEREN entre los dos sitios:** la causa es un binario distinto (descargas en fechas o cuantizaciones distintas), no conducta del modelo. Se unifica el binario (`ollama pull` en ambos sitios hasta digest idéntico), se repiten calibración y líneas base de ese modelo en ambos sitios, y se vuelve a aplicar el criterio. El modelo permanece en el roster si entonces pasa.
- **Rama B — los digests son IDÉNTICOS:** la divergencia es conducta dependiente del sitio con el mismo binario. El modelo queda EXCLUIDO del estudio, por la misma lógica que la Enmienda 2: la inferencia multi-sitio descansa en que las celdas réplica sean comparables. Los datos recogidos se conservan como rastro y la exclusión se reporta con sus cifras.

**Laguna instrumental asociada, corregida a futuro:** los archivos de línea base y calibración (`BASE_*.csv`) NO llevan manifiesto, por lo que el digest del modelo no queda registrado en esta fase y ha debido solicitarse a los sitios a posteriori. Las sesiones de condición sí lo registran. Se deja constancia; no se modifica la plataforma a mitad de fase.

**Incidencias operativas registradas en la Fase 2 (sin efecto sobre los datos analizables):**
1. site2 ejecutó una línea base completa de deepseek-v2:16b (3.296 filas) después de que la Enmienda 2 lo excluyera; los datos se conservan como rastro y no entran en ningún análisis.
2. site2 ejecutó además una línea base completa de gemma2:9b siendo sitio réplica (además de su sub-base de 40 ítems). Ambos archivos se conservan; la comprobación de equivalencia de gemma2:9b usa los 40 ítems comunes, como en el resto de modelos, y la comparación sobre los 206 ítems (MAE 0.098, r 0.914) se reporta como información adicional.
3. `BASE_llama3-8b_site4_79c1.csv` está vacío (0 filas): ejecución interrumpida en site4, anterior a la Fase 2. Se conserva el archivo y se documenta.
4. No se conservan en el repositorio los rastros de calibración de deepseek-v2:16b de site1 ni la segunda tanda de calibraciones de ese sitio; pendiente de confirmación con site1.

### Enmienda 3 — RESOLUCIÓN (2026-09-22)
Comprobación solicitada a site3 y site4: ambos sitios ejecutan **el mismo binario** de llama3:8b (digest Ollama `365c0bd3c000`, 4.7 GB). Se aplica por tanto la **rama B**, pre-especificada antes de conocer este dato: **llama3:8b queda EXCLUIDO del estudio**.

**Observación de control (refuerza la atribución):** la divergencia no es atribuible al sitio ni al sistema operativo. La misma máquina Windows (site3) produjo resultados equivalentes en sus otros dos modelos (phi4: MAE 0.064 frente a macOS; gemma3:latest: MAE 0.123 frente a Linux), y el resto de pares —que cruzan macOS, Linux, Windows y servidor— cumplen el criterio. La no-equivalencia es específica de llama3:8b, el modelo con mayor ruido interno del roster (split-half 0.155 / 0.091 y estabilidad de calibración 0.106 / 0.087, los peores valores medidos).

**Interpretación reportable (no demostrada, se declara como tal):** un mismo modelo cuantizado y con digest idéntico puede producir distribuciones de respuesta distintas según el hardware y el backend de inferencia. Con las mediciones disponibles no podemos identificar el mecanismo; lo que sí establecen es que la equivalencia entre máquinas no puede darse por supuesta ni siquiera fijando el binario, y que conviene comprobarla empíricamente en cualquier estudio multi-sitio con modelos locales. Esto se reportará en el manuscrito como hallazgo metodológico, junto con las cifras.

**Roster final tras la Enmienda 3: 5 modelos, 3 familias arquitectónicas.**

| Modelo | Familia | Sitio primario | Sitio réplica |
|---|---|---|---|
| gemma2:9b | Gemma | site1 | site2 |
| gemma3:latest | Gemma | site3 | site4 |
| gemma3:12b | Gemma | site4 | site5 |
| qwen2.5:7b | Qwen | site1 | site5 |
| phi4 | Phi | site2 | site3 |

Modelos excluidos y motivo: deepseek-v2:16b (Enmienda 2, estabilidad basal discordante entre sitios), llama3:8b (Enmienda 3 rama B, no-equivalencia de propensiones entre sitios con binario idéntico). Todos los rastros se conservan y ambas exclusiones se reportan con sus cifras.

**Efecto sobre la Fase 3:** 5 modelos × 2 sitios × 4 condiciones = 40 sesiones (8 por sitio). site3 pierde un modelo primario y site4 un modelo réplica; el resto de la asignación no cambia y todas las celdas conservan sus dos sitios.
