# FASE 3 — Sesiones experimentales (normdrift)

**Antes de nada, todos:** `git pull` en vuestra carpeta `normdrift` y comprobar `grep VERSION normdrift.py` → **1.1.0**.

**Roster tras las Enmiendas 2 y 3 (5 modelos):** gemma2:9b, gemma3:latest, gemma3:12b, qwen2.5:7b, phi4.
**EXCLUIDOS — no ejecutéis nada con ellos:** deepseek-v2:16b y llama3:8b.

Cada modelo se corre en sus dos sitios, con las **4 condiciones** y en **orden fijo**: C0 → C1 → C2 → C2p. Primero un modelo entero (sus 4 condiciones), luego el siguiente.
Cada sesión son 36 rondas × 8 agentes con sondas privadas: **1–2 h por sesión**. Son 8 sesiones por sitio: repartidlas en varios días, una o dos al día.

El número de `--session` NO es decorativo: distingue vuestra celda de la del otro sitio. Copiadlo exacto.

- **macOS** (site2, site5): anteponer `caffeinate -i`.
- **Linux / servidor** (site1, site4): sin `caffeinate`; en servidor, dentro de `tmux`.
- **Windows** (site3): sin `caffeinate`; desactivar la suspensión.

---

## site1 — Óscar (Ubuntu) — gemma2:9b (s0) y qwen2.5:7b (s0)
```
python3 normdrift.py run --condition C0  --model gemma2:9b --session 0
python3 normdrift.py run --condition C1  --model gemma2:9b --session 0
python3 normdrift.py run --condition C2  --model gemma2:9b --session 0
python3 normdrift.py run --condition C2p --model gemma2:9b --session 0
python3 normdrift.py run --condition C0  --model qwen2.5:7b --session 0
python3 normdrift.py run --condition C1  --model qwen2.5:7b --session 0
python3 normdrift.py run --condition C2  --model qwen2.5:7b --session 0
python3 normdrift.py run --condition C2p --model qwen2.5:7b --session 0
```

## site2 — Isra (macOS) — phi4 (s0) y gemma2:9b (s1)
```
caffeinate -i python3 normdrift.py run --condition C0  --model phi4 --session 0
caffeinate -i python3 normdrift.py run --condition C1  --model phi4 --session 0
caffeinate -i python3 normdrift.py run --condition C2  --model phi4 --session 0
caffeinate -i python3 normdrift.py run --condition C2p --model phi4 --session 0
caffeinate -i python3 normdrift.py run --condition C0  --model gemma2:9b --session 1
caffeinate -i python3 normdrift.py run --condition C1  --model gemma2:9b --session 1
caffeinate -i python3 normdrift.py run --condition C2  --model gemma2:9b --session 1
caffeinate -i python3 normdrift.py run --condition C2p --model gemma2:9b --session 1
```

## site3 — Roberto (Windows) — gemma3:latest (s0) y phi4 (s1)
```
python3 normdrift.py run --condition C0  --model gemma3:latest --session 0
python3 normdrift.py run --condition C1  --model gemma3:latest --session 0
python3 normdrift.py run --condition C2  --model gemma3:latest --session 0
python3 normdrift.py run --condition C2p --model gemma3:latest --session 0
python3 normdrift.py run --condition C0  --model phi4 --session 1
python3 normdrift.py run --condition C1  --model phi4 --session 1
python3 normdrift.py run --condition C2  --model phi4 --session 1
python3 normdrift.py run --condition C2p --model phi4 --session 1
```

## site4 — Beatriz (Linux) — gemma3:12b (s0) y gemma3:latest (s1)
```
python3 normdrift.py run --condition C0  --model gemma3:12b --session 0
python3 normdrift.py run --condition C1  --model gemma3:12b --session 0
python3 normdrift.py run --condition C2  --model gemma3:12b --session 0
python3 normdrift.py run --condition C2p --model gemma3:12b --session 0
python3 normdrift.py run --condition C0  --model gemma3:latest --session 1
python3 normdrift.py run --condition C1  --model gemma3:latest --session 1
python3 normdrift.py run --condition C2  --model gemma3:latest --session 1
python3 normdrift.py run --condition C2p --model gemma3:latest --session 1
```

## site5 — Raúl (macOS) — qwen2.5:7b (s1) y gemma3:12b (s1)
```
caffeinate -i python3 normdrift.py run --condition C0  --model qwen2.5:7b --session 1
caffeinate -i python3 normdrift.py run --condition C1  --model qwen2.5:7b --session 1
caffeinate -i python3 normdrift.py run --condition C2  --model qwen2.5:7b --session 1
caffeinate -i python3 normdrift.py run --condition C2p --model qwen2.5:7b --session 1
caffeinate -i python3 normdrift.py run --condition C0  --model gemma3:12b --session 1
caffeinate -i python3 normdrift.py run --condition C1  --model gemma3:12b --session 1
caffeinate -i python3 normdrift.py run --condition C2  --model gemma3:12b --session 1
caffeinate -i python3 normdrift.py run --condition C2p --model gemma3:12b --session 1
```

---

## Qué hacer al terminar cada sesión
Pegad en el canal la última línea que imprime el programa (la que da el nombre del run y el CSV). Nada más: **no miréis ni comentéis resultados**. El análisis está congelado en el repo y se ejecuta una sola vez, al final, con todos los datos.

## Al terminar vuestras 8 sesiones
Subid resultados como en la Fase 2:
```
git checkout -b resultados2-siteN
git add results/
git commit -m "fase 3 siteN"
git push -u origin resultados2-siteN
```
y abrid el Pull Request con el enlace que os da el terminal.

## Incidencias
Si una sesión se corta a medias: borrad su CSV incompleto de `results/`, apuntadlo en el canal (fecha + causa) y relanzad esa sesión entera. Nunca reanudéis a medias.
