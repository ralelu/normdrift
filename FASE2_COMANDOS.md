# FASE 2 — Líneas base (normdrift). Comandos por sitio

**Antes de nada, todos:** `git pull` y comprobar que `grep VERSION normdrift.py` dice **1.1.0**.

Reglas: un comando cada vez, esperando a que termine. Máquina enchufada y sin suspensión. Nada pesado en paralelo.
- **macOS** (site2 Isra, site5 Raúl): anteponer `caffeinate -i`, como en los ejemplos.
- **Linux / servidor** (site1 Óscar, site4 Bea): SIN `caffeinate`. En servidor remoto, lanzar dentro de `tmux` (o con `nohup ... &`) para que sobreviva a la desconexión.
- **Windows** (site3 Roberto): SIN `caffeinate`. Desactivar antes la suspensión en Configuración → Sistema → Inicio/apagado.

**Primario vs réplica:** el sitio PRIMARIO de cada modelo mide su línea base completa (206 ítems × 16 muestras, 2–4 h). El sitio RÉPLICA mide solo 40 ítems (`--subset 40`, 30–45 min) para comprobar equivalencia entre máquinas. Copiar el comando equivocado invalida la celda: revisa que el tuyo lleve o no `--subset 40` según la tabla.

| Sitio | Persona | Sistema | Modelos (rol) |
|---|---|---|---|
| site1 | Óscar | Ubuntu (servidor) | gemma2:9b (primario), qwen2.5:7b (primario) |
| site2 | Isra | macOS | phi4 (primario), gemma2:9b (réplica) |
| site3 | Roberto | Windows | gemma3:latest (primario), llama3:8b (primario), phi4 (réplica) |
| site4 | Beatriz | Linux | gemma3:12b (primario), gemma3:latest (réplica), llama3:8b (réplica) |
| site5 | Raúl | macOS | qwen2.5:7b (réplica), gemma3:12b (réplica) |

Total: 6 líneas base completas + 6 sub-bases = 12 comandos en todo el equipo.

---

## site1 — Óscar (Ubuntu) — 2 completas
```
python3 normdrift.py baseline --model gemma2:9b
```
```
python3 normdrift.py baseline --model qwen2.5:7b
```

## site2 — Isra (macOS) — 1 completa + 1 sub-base
```
caffeinate -i python3 normdrift.py baseline --model phi4
```
```
caffeinate -i python3 normdrift.py baseline --model gemma2:9b --subset 40
```

## site3 — Roberto (Windows) — 2 completas + 1 sub-base
```
python3 normdrift.py baseline --model gemma3:latest
```
```
python3 normdrift.py baseline --model llama3:8b
```
```
python3 normdrift.py baseline --model phi4 --subset 40
```

## site4 — Beatriz (Linux) — 1 completa + 2 sub-bases
```
python3 normdrift.py baseline --model gemma3:12b
```
```
python3 normdrift.py baseline --model gemma3:latest --subset 40
```
```
python3 normdrift.py baseline --model llama3:8b --subset 40
```

## site5 — Raúl (macOS) — 2 sub-bases
```
caffeinate -i python3 normdrift.py baseline --model qwen2.5:7b --subset 40
```
```
caffeinate -i python3 normdrift.py baseline --model gemma3:12b --subset 40
```

---

**Al terminar cada comando:** pegad en el canal la línea `baseline written -> BASE_...csv` y la línea de tasas entre paréntesis (abstención / rechazos / fallos de parseo). No analicéis nada.

**NO ejecutéis todavía ningún `run --condition ...`:** la Fase 3 (sesiones experimentales) arranca solo cuando el coordinador lo anuncie, con las 12 líneas base completadas.

**Si algo se corta a medias:** borrad el CSV incompleto de `results/`, apuntad el incidente en el canal (fecha + causa) y relanzad ese comando entero.
