# ASIGNACION DEFINITIVA modelos x sitios — tras Fase 1 (calibración) y Enmienda 2

**Roster final: 6 modelos, 4 familias arquitectónicas.** deepseek-v2:16b EXCLUIDO (Enmienda 2: veredictos discordantes entre sitios réplica; mismo digest verificado, 7c8c332f2df7).

| Modelo | Sitio PRIMARIO (línea base completa, 206 ítems) | Sitio RÉPLICA (sub-base, `--subset 40`) | session_idx |
|---|---|---|---|
| gemma2:9b | site1 (Óscar) | site2 (Isra) | s0 / s1 |
| qwen2.5:7b | site1 (Óscar) | site5 (Raúl) | s0 / s1 |
| phi4 | site2 (Isra) | site3 (Roberto) | s0 / s1 |
| gemma3:latest | site3 (Roberto) | site4 (Bea) | s0 / s1 |
| llama3:8b | site3 (Roberto) | site4 (Bea) | s0 / s1 |
| gemma3:12b | site4 (Bea) | site5 (Raúl) | s0 / s1 |

Carga de Fase 2 por sitio: site1 = 2 líneas base completas · site2 = 1 completa + 1 sub-base · site3 = 2 completas + 1 sub-base · site4 = 1 completa + 2 sub-bases · site5 = 2 sub-bases.

## Veredictos de calibración (plataforma v1.1.0, tras Enmienda 1)

| Modelo | Sitio A (formato / estabilidad) | Sitio B (formato / estabilidad) | Veredicto |
|---|---|---|---|
| gemma2:9b | site1: 0.981 / 0.110 | site2: 0.994 / 0.135 | INCLUDE |
| qwen2.5:7b | site1: 1.000 / 0.013 | site5: 1.000 / 0.050 | INCLUDE |
| phi4 | site2: 1.000 / 0.100 | site3: 1.000 / 0.081 | INCLUDE |
| gemma3:latest | site3: 1.000 / 0.044 | site4: 1.000 / 0.006 | INCLUDE |
| llama3:8b | site3: 1.000 / 0.106 | site4: 1.000 / 0.087 | INCLUDE |
| gemma3:12b | site4: 1.000 / 0.062 | site5: 1.000 / 0.062 | INCLUDE |
| ~~deepseek-v2:16b~~ | site1: 0.972 / 0.137 INCLUDE | site2: 0.966 / 0.179 EXCLUDE | **EXCLUIDO (Enmienda 2)** |

Las 12 celdas (6 modelos x 2 sitios) están completas y todas las réplicas coinciden en veredicto. Rango de estabilidad observado: 0.006 (gemma3:latest) a 0.135 (gemma2:9b), todas bajo el umbral. Umbral: formato >=0.95 tras un re-prompt; estabilidad <0.15. Heterogeneidad de plataformas registrada: site1 Ubuntu (servidor), site2 macOS, site3 Windows, site4 Linux, site5 macOS.
