# ASIGNACION PROVISIONAL modelos x sitios — 5 sitios, 7 modelos (confirmar al congelar; cambios por hardware se registran)

| Sitio | Modelos (session_idx) |
|---|---|
| site1 | gemma2:9b (s0), qwen2.5:7b (s0), deepseek-v2:16b (s0) |
| site2 | gemma2:9b (s1), phi4 (s0), deepseek-v2:16b (s1) |
| site3 | gemma3:latest (s0), phi4 (s1), llama3:8b (s0) |
| site4 | gemma3:latest (s1), gemma3:12b (s0), llama3:8b (s1) |
| site5 | qwen2.5:7b (s1), gemma3:12b (s1) |

Cada modelo corre en exactamente 2 sitios (replicacion incorporada). Carga por sitio: site1=3 modelos, site2=3 modelos, site3=3 modelos, site4=3 modelos, site5=2 modelos. Modelos pesados (gemma3:12b ~8GB, deepseek-v2:16b ~9GB) requieren >=16GB RAM: avisa ANTES del freeze para reasignar.