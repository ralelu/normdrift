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
