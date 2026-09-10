# normdrift — Guía de arranque multi-sitio (día 1)

## Coordinador (Raúl), hoy:
1. Crea un repo PRIVADO en GitHub: `normdrift`. Sube: normdrift.py, prereg_normdrift_DRAFT_v0.9.md, este README. Haz commit y tag: `git tag v0.1-mock && git push --tags`.
2. Invita a los 4-5 autores como colaboradores del repo.
3. Reparte los site-id (site1..site5) en un mensaje al grupo, uno por persona/máquina.

## Cada autor, en su ordenador, hoy (15 min):
1. Instalar Ollama si no lo tiene (ollama.com) y Python 3 (viene en Mac).
2. Clonar: `git clone https://github.com/<usuario>/normdrift.git && cd normdrift`
3. Identificarse: `export NORMDRIFT_SITE=siteN`  (el número asignado; añadirlo a ~/.zshrc)
4. Validar: `python3 normdrift.py mock`  → debe acabar en `MOCK ACCEPTANCE: PASS`.
   Pegar el PASS en el canal del equipo. Con los 4-5 PASS, los sitios están certificados.
5. Ir descargando modelos asignados: `ollama pull <modelo>` (lista de asignación la fija el coordinador al congelar el prereg).

## Bloqueado hasta el freeze (deliberadamente):
- `baseline`, `calibrate` y `run` se niegan a ejecutar sin items.json verificado y prereg v1.0.
- Nadie edita normdrift.py: solo se ejecuta desde commits etiquetados del repo (el manifiesto graba el commit; un árbol sucio bloquea el run).

## Flujo de datos:
Cada sitio corre sus celdas asignadas → `git checkout -b resultados-siteN` → añade su carpeta results/ → push → Pull Request → el coordinador ejecuta `python3 normdrift.py merge-validate --dir results` antes de aceptar.

## Pendiente del coordinador científico (Claude) antes del freeze:
items.json con normas humanas verificadas (MoCA + Scruples + Chaos-NLI, estratificado T1/T2/T3), lectura de delimitación de los 3 papers frontera, y asignación modelos×sitios.
