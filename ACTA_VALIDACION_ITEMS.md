# Acta del proceso de validación del banco de ítems — normdrift
**Fecha de cierre: 2026-09-10. Se adjunta al material suplementario y al pre-registro (bloqueante para el freeze v1.0).**

## Origen del material
206 ítems (62 dilemas morales, 144 juicios causales) del dataset MoCA (Nie et al., NeurIPS 2023; repositorio público cicl-stanford/moca, clonado y verificado), cada uno con 25 respuestas humanas reales (IRB del estudio original). Estratos de consenso por votos enteros (T1 ≥22/25; T2 18–21/25; T3 ≤17/25), ratificados antes de que ningún modelo viera ningún ítem.

## Ronda 1 — cribado preliminar (2 juezas - psicólogas)
Partición completa 206/206 sin solapamiento (68/70/68), independiente. Resultado bruto: 85 aptos directos, 23 no-aptos, 1 claridad ≤2, 84 marcas de carga emocional, 13 dudas. Incidencia detectada y documentada: una revisora aplicó a su bloque íntegro (los 62 morales + 6 causales) un criterio de exclusión distinto del escrito ("contenido de daño/ética como confundido" en lugar de "contenido gratuito"), divergencia atribuible a la ausencia de sesión de calibración previa — déficit del diseño del proceso, no de las revisoras. DECISIÓN (equipo, fechada pre-freeze): la ronda se recalifica como cribado preliminar; sus señalizaciones pasan a instancia experta; las 84 marcas de carga se conservan como covariable pre-registrada de análisis de sensibilidad (no como exclusión); reconocimiento ajustado a su papel real.

## Ronda 2 — validación experta decisoria (1 Doctor en Psicología [Dr. Raúl Alelú-Paz])
Paquete ciego y aleatorizado de 67 ítems: los 24 señalizados + 13 dudas + muestra aleatoria de 30 para acuerdo. Con guía de calibración previa (5 principios; criterio "sensible gratuito" operativizado con regla de desempate duro/gratuito). Resultado: 67/67 aptos, 0 gratuitos, claridad 5 en 60 y 4 en 7 (ninguno bajo el umbral de exclusión ≤2). Las 23 señalizaciones de no-apto de la ronda 1 quedan revocadas por la instancia experta — vuelco íntegro que se reporta como cuantificación del efecto de la calibración.

## Acuerdo entre rondas
Muestra solapada n=30: acuerdo bruto experta–psicólogas en aptitud 30/30 (100%). Kappa no estimable (marginales sin varianza en la muestra); se reporta el acuerdo bruto con esta limitación. El desacuerdo del proceso se concentró íntegramente en los ítems señalizados, no en la muestra aleatoria.

## Banco final congelado
206 ítems (T1=16, T2=69, T3=121; 84 con marca de sensibilidad como covariable). Exclusiones finales: 0 (la experta revocó todas las candidaturas). Salvaguardas mecánicas adicionales pre-registradas: filtro automático de tasa de rechazo por ítem en calibración (los ítems que disparen negativas de los modelos por encima del umbral caen por regla), y análisis de sensibilidad con/sin ítems marcados por carga.
**SHA-256 del items.json congelado: a7cd9ee9a3b32ca5… (completo en items_bank_hash.json; se graba en el manifiesto de cada run).**

## Declaración de integridad
Todas las decisiones de este proceso son anteriores a cualquier exposición de modelo alguno al material. Los instrumentos rellenos de las cuatro revisoras se archivan como material suplementario.
