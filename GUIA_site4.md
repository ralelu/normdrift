# Guia personal — site4

Bienvenido/a al estudio **normdrift** (deriva de equipos de agentes IA respecto a normas humanas).
Tu identificador: **site4**. Tus modelos: **gemma3:latest, gemma3:12b, llama3:8b**.
Regla de oro: nada se ejecuta que no venga del repo, un comando cada vez, y los incidentes se apuntan, no se esconden.

## FASE 0 — Hoy (15-20 min)
1. Instala Ollama: https://ollama.com (descargar, abrir, listo). Necesitas Python 3 (en Mac ya viene).
2. En Terminal, clona el repositorio (URL te la pasa el coordinador):
   `git clone [URL-DEL-REPO] && cd normdrift`
3. Identifica tu sitio de forma permanente:
   `echo 'export NORMDRIFT_SITE=site4' >> ~/.zshrc && export NORMDRIFT_SITE=site4`
   (Linux: ~/.bashrc. Windows: usa WSL o consulta al coordinador.)
4. Valida tu maquina sin gastar nada:
   `python3 normdrift.py mock`
   Debe acabar en `MOCK ACCEPTANCE: PASS` -> pega el PASS en el canal del equipo.
5. Descarga tus modelos (solo esto necesita internet):
   `ollama pull gemma3:latest`
   `ollama pull gemma3:12b`
   `ollama pull llama3:8b`
6. Lee `prereg_normdrift_DRAFT_v0.9.md` y manda al canal tu OK o comentarios de diseno.
   Tu ratificacion escrita es la que congela el protocolo (v1.0).

## FASE 1 — Tras el aviso de FREEZE (calibracion e inclusion; ~1-2h por modelo, uno cada vez)
`caffeinate -i python3 normdrift.py calibrate --model gemma3:latest`
`caffeinate -i python3 normdrift.py calibrate --model gemma3:12b`
`caffeinate -i python3 normdrift.py calibrate --model llama3:8b`
Pega los veredictos INCLUDE/EXCLUDE en el canal. Despues, lineas base completas:
`caffeinate -i python3 normdrift.py baseline --model gemma3:latest`
`caffeinate -i python3 normdrift.py baseline --model gemma3:12b`
`caffeinate -i python3 normdrift.py baseline --model llama3:8b`

## FASE 2 — Sesiones experimentales (cuando el coordinador de la salida; ~1-3h por tanda)
Orden fijo por modelo: C0 -> C1 -> C2 -> C2p. Primero un modelo entero, luego el siguiente. Uno cada vez.
Modelo gemma3:latest (tu session_idx: 1):
`caffeinate -i python3 normdrift.py run --condition C0  --model gemma3:latest --session 1`
`caffeinate -i python3 normdrift.py run --condition C1  --model gemma3:latest --session 1`
`caffeinate -i python3 normdrift.py run --condition C2  --model gemma3:latest --session 1`
`caffeinate -i python3 normdrift.py run --condition C2p --model gemma3:latest --session 1`
Modelo gemma3:12b (tu session_idx: 0):
`caffeinate -i python3 normdrift.py run --condition C0  --model gemma3:12b --session 0`
`caffeinate -i python3 normdrift.py run --condition C1  --model gemma3:12b --session 0`
`caffeinate -i python3 normdrift.py run --condition C2  --model gemma3:12b --session 0`
`caffeinate -i python3 normdrift.py run --condition C2p --model gemma3:12b --session 0`
Modelo llama3:8b (tu session_idx: 1):
`caffeinate -i python3 normdrift.py run --condition C0  --model llama3:8b --session 1`
`caffeinate -i python3 normdrift.py run --condition C1  --model llama3:8b --session 1`
`caffeinate -i python3 normdrift.py run --condition C2  --model llama3:8b --session 1`
`caffeinate -i python3 normdrift.py run --condition C2p --model llama3:8b --session 1`
(caffeinate evita que el Mac duerma; tapa abierta y enchufado. Linux: desactiva la suspension.)
Si una sesion se corta: borra su CSV incompleto de results/, apunta el incidente (fecha+causa) y relanzala.

## FASE 3 — Subir resultados
`git checkout -b resultados-site4`
`git add results/ && git commit -m "resultados site4" && git push -u origin resultados-site4`
Abre un Pull Request en GitHub (boton verde). El coordinador valida y fusiona.

No edites normdrift.py ni items.json: el sistema detecta cambios y se niega a correr — es lo que hace publicable el estudio.
