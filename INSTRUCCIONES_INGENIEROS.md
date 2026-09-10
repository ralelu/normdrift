# Instrucciones generales para los ingenieros — estudio normdrift
### (complemento común a tu GUIA_siteN.md personal; léelas juntas)

## Qué estamos haciendo y por qué importa tu parte
Medimos si equipos de agentes de IA locales se desvían de las respuestas humanas ante dilemas y juicios cuando un "supervisor" de IA les presiona. Es un estudio PRE-REGISTRADO: el protocolo quedó congelado antes de recoger un solo dato, y su credibilidad depende de que los cinco sitios ejecuten EXACTAMENTE lo mismo. Tu ordenador es un instrumento de laboratorio; estas reglas son la calibración del instrumento.

## Las 6 reglas de oro
1. **Solo código del repo, solo desde commit limpio.** Nunca edites normdrift.py ni items.json — el programa detecta cambios y se niega a correr. Si crees que hay un bug: canal del equipo, lo arregla el coordinador con versión nueva para todos.
2. **Un comando cada vez.** Lanza, espera a que termine, lanza el siguiente. Nada en paralelo en la misma máquina (los modelos compiten por memoria y se degradan).
3. **Orden fijo.** El orden de comandos de tu guía no es una sugerencia: C0→C1→C2→C2p por modelo, primer modelo entero antes del segundo. El orden es parte del protocolo.
4. **Los incidentes se apuntan, jamás se esconden.** ¿Se cortó una sesión, se durmió el portátil, saltó un error raro? No pasa nada: borra el CSV incompleto de esa sesión, apunta en el canal fecha+qué pasó, y relánzala. Lo que rompería el estudio no es el incidente — es ocultarlo.
5. **No mires resultados.** Los CSV que generas son datos crudos; nadie (tampoco el coordinador) analiza nada hasta que TODO esté recogido y fusionado. Curiosear agregados a mitad contamina las decisiones. El script de análisis está congelado en el repo y se ejecuta una vez, al final.
6. **Máquina en condiciones de laboratorio:** enchufada a corriente, tapa abierta (o suspensión desactivada en Linux), sin otras cargas pesadas (juegos, renders, VMs) mientras corre una sesión.

## Tu flujo completo (los comandos exactos están en tu GUIA_siteN.md)
- **FASE 0 (hoy):** clonar repo → `export NORMDRIFT_SITE=siteN` → `python3 normdrift.py mock` → pegar el PASS en el canal → `ollama pull` de tus modelos → pegar tu `ollama list` → leer el prereg y ratificar (o comentar).
- **FASE 1 (a la señal de FREEZE):** `calibrate` de cada uno de tus modelos → pegar veredicto INCLUDE/EXCLUDE.
- **FASE 2:** `baseline` completo de tus modelos primarios; `baseline --subset 40` de tus modelos réplica (tu guía te dice cuál es cuál).
- **FASE 3 (a la señal del coordinador):** las sesiones `run` en el orden de tu guía. Cada una tarda 1–3 h; ideal una por mañana y otra por noche.
- **FASE 4:** rama `resultados-siteN`, push, Pull Request. El validador automático comprobará tu entrega; si falla, el mensaje de error te dice qué corregir.

## Detalles técnicos que te ahorrarán problemas
- El `session_idx` de cada comando de tu guía NO es decorativo: distingue tu réplica de la del otro sitio. Cópialo exacto.
- `caffeinate -i` (Mac) va delante de cada comando largo. Linux: `systemd-inhibit` o desactiva la suspensión.
- Las sesiones escriben en `results/` con un manifiesto por run (semillas, versión, huella del banco de ítems, huella de tu binario del modelo). No renombres ni muevas nada de esa carpeta.
- Si `run` te dice BLOCKED: es el sistema protegiendo el protocolo (falta freeze, árbol sucio, o site-id sin definir). El mensaje te dice cuál de los tres.
- Espacio en disco: ten ≥25 GB libres antes de los pulls.

## Qué ganas tú
Coautoría del paper (revista Q1 objetivo), un protocolo multi-sitio en el CV, y la satisfacción de que si esto sale — en cualquier dirección — nadie podrá tumbarlo por ejecución descuidada. Gracias por ser parte.
