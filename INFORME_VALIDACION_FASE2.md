# Informe de validación — Fase 2 (líneas base), normdrift

Fecha: 2026-09-22. Archivos recibidos: 39 (12 celdas de línea base + calibraciones). Lecturas fallidas: 0.

## 1. Completitud de las 12 celdas

| Modelo | Completa (primario) | Sub-base (réplica) |
|---|---|---|
| gemma2-9b | site1 ✓ | site2 ✓ |
| qwen2.5-7b | site1 ✓ | site5 ✓ |
| phi4 | site2 ✓ | site3 ✓ |
| gemma3-latest | site3 ✓ | site4 ✓ |
| llama3-8b | site3 ✓ | site4 ✓ |
| gemma3-12b | site4 ✓ | site5 ✓ |

## 2. Calidad de respuesta por archivo

| Modelo | Sitio | Tipo | Respuestas | Abstención | No-respuesta |
|---|---|---|---|---|---|
| deepseek-v2-16b | site2 | completa | 3296 | 0.003 | 0.034 |
| gemma2-9b | site1 | completa | 3296 | 0.000 | 0.010 |
| gemma2-9b | site2 | completa | 3296 | 0.000 | 0.007 |
| gemma2-9b | site2 | sub-base | 640 | 0.000 | 0.005 |
| gemma3-12b | site4 | completa | 3296 | 0.000 | 0.000 |
| gemma3-12b | site5 | sub-base | 640 | 0.000 | 0.000 |
| gemma3-latest | site3 | completa | 3296 | 0.000 | 0.000 |
| gemma3-latest | site4 | sub-base | 640 | 0.000 | 0.000 |
| llama3-8b | site3 | completa | 3296 | 0.000 | 0.000 |
| llama3-8b | site4 | sub-base | 640 | 0.000 | 0.000 |
| phi4 | site2 | completa | 3296 | 0.000 | 0.000 |
| phi4 | site3 | sub-base | 640 | 0.000 | 0.000 |
| qwen2.5-7b | site1 | completa | 3296 | 0.000 | 0.000 |
| qwen2.5-7b | site5 | sub-base | 640 | 0.000 | 0.000 |

Ninguna tasa de no-respuesta supera el 3.4% (deepseek, excluido). Ningún ítem alcanza el umbral del 20% de no-respuesta del filtro mecánico pre-registrado: **no se excluye ningún ítem del banco**.

## 3. Equivalencia primario–réplica (Enmienda 3: criterio MAE < 0.15 sobre 40 ítems comunes)

| Modelo | %A primario | %A réplica | r | MAE entre sitios | Ruido interno prim/repl | Veredicto |
|---|---|---|---|---|---|---|
| gemma2-9b | 0.360 | 0.378 | 0.910 | **0.100** | 0.100 / 0.106 | EQUIVALENTE |
| qwen2.5-7b | 0.353 | 0.366 | 0.971 | **0.053** | 0.062 / 0.062 | EQUIVALENTE |
| phi4 | 0.522 | 0.517 | 0.966 | **0.064** | 0.091 / 0.091 | EQUIVALENTE |
| gemma3-latest | 0.652 | 0.691 | 0.803 | **0.123** | 0.038 / 0.013 | EQUIVALENTE |
| llama3-8b | 0.512 | 0.811 | 0.692 | **0.308** | 0.155 / 0.091 | **NO EQUIVALENTE** |
| gemma3-12b | 0.666 | 0.678 | 0.880 | **0.094** | 0.041 / 0.062 | EQUIVALENTE |

## 4. Conclusión

Cinco de los seis modelos superan el criterio de equivalencia. llama3:8b lo falla con una divergencia sistemática (0.512 vs 0.811 de respuestas 'A' sobre los mismos ítems). Pendiente de comprobar los digests de Ollama en site3 y site4 para aplicar la rama A o la rama B de la Enmienda 3. La Fase 3 no arranca hasta resolverlo.
