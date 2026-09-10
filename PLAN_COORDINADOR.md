# PLAN DEL COORDINADOR — normdrift, del freeze al paper
### (paso a paso + checklist; versión 2026-09-10, acompaña al prereg v0.9.4)

## PASO 1 — Actualizar el repositorio (hoy, 20 min)
Sube/reemplaza en GitHub estos archivos del paquete `normdrift-v1.0-freeze.zip`:
`normdrift.py` (v1.0.0), `items.json`, `items_bank_hash.json`, `ACTA_VALIDACION_ITEMS.md` (completa antes el nombre/afiliación de la experta), `prereg_normdrift_DRAFT_v0.9.md` (v0.9.4), `analysis_normdrift.py`, `ASSIGNMENTS.md`, `INSTRUCCIONES_INGENIEROS.md`, y las 5 `GUIA_siteN.md`.
Cómo: página del repo → Add file → Upload files → arrastrar → Commit changes.
Después crea la release: Releases → Create a new release → tag `v1.0-freeze-candidate` → Publish.

## PASO 2 — Ratificación del equipo (esta semana)
Envía al canal: enlace al repo + mensaje pidiendo a cada autor (a) leer prereg v0.9.4 y ACTA, (b) responder literalmente "RATIFICO prereg v0.9.4" o sus objeciones. Las psicólogas no ratifican (no son autoras salvo que decidáis lo contrario); los 5 autores sí, tú incluido.
⚠️ Si alguien propone cambios: se discuten AHORA — tras el freeze todo cambio es enmienda fechada.

## PASO 3 — Certificación de sitios (en paralelo al paso 2)
Cada ingeniero completa la FASE 0 de su guía (clonar, site-id, mock, pulls). Tú recolectas.

## PASO 4 — Declarar el FREEZE
Cuando el checklist A esté completo: crea la release `v1.0-freeze` (definitiva) y anuncia en el canal: "FREEZE declarado — arranca FASE 1 según vuestras guías". Desde este momento: código y banco intocables; incidentes al canal, nunca silenciados.

## PASO 5 — Supervisar Fases 1–2 (2–3 semanas)
Tu papel: recolectar veredictos INCLUDE/EXCLUDE de calibración, resolver dudas, verificar que los sitios respetan el orden fijo, registrar incidentes con fecha. NO mirar resultados de contenido: nadie ejecuta `analysis_normdrift.py` hasta el paso 7 — el script está congelado en el repo precisamente para eso.

## PASO 6 — Fusión de datos
A cada Pull Request de resultados: en tu máquina, `git pull` de la rama y `python3 normdrift.py merge-validate --dir results`. PASS → merge; FAIL → devolver al sitio con el error (los fallos típicos: manifiesto ausente, digest de modelo distinto entre sitios, celda duplicada).

## PASO 7 — Análisis y manuscrito
Con TODAS las celdas fusionadas y merge-validate global en PASS: se ejecuta `analysis_normdrift.py` tal cual está congelado (cualquier cambio = enmienda), me subes el `results/` completo y entrego informe estadístico, figuras y borrador de manuscrito con la regla de contingencia del §5: deriva o resistencia, ambas se publican.

---

# CHECKLIST

## A — Pre-freeze (todo ✔ antes de declarar freeze)
- [ ] Repo actualizado con los 9+ archivos del paquete y release `v1.0-freeze-candidate`
- [ ] ACTA con nombre y afiliación de la psicóloga experta completados
- [ ] Ratificación escrita de los 5 autores ("RATIFICO prereg v0.9.4") archivada (pantallazo o hilo)
- [ ] 5/5 sitios con `MOCK ACCEPTANCE: PASS` pegado en el canal
- [ ] 5/5 sitios con sus modelos descargados (`ollama list` pegado en el canal)
- [ ] Asignación modelos×sitios confirmada contra el hardware real (pesados en máquinas ≥16 GB)
- [ ] Release `v1.0-freeze` publicada y anuncio de arranque enviado

## B — Fase 1 (calibración)
- [ ] 7/7 modelos con veredicto INCLUDE/EXCLUDE publicado en el canal (con su rastro en el repo)
- [ ] Filtro de rechazos aplicado: lista de ítems >20% de no-respuesta (si los hay) registrada
- [ ] Incidentes de la fase (si los hubo) anotados con fecha y causa

## C — Fases 2 (líneas base) y 3 (sesiones)
- [ ] Línea base completa (206×16) de cada modelo incluido en su sitio primario
- [ ] Sub-base de equivalencia (40 ítems) de cada modelo en su sitio réplica
- [ ] Sesiones C0→C1→C2→C2p completadas por cada sitio para sus modelos, en orden fijo
- [ ] Cero ejecuciones del script de análisis antes del paso 7 (compromiso de todos)

## D — Cierre
- [ ] Todos los PR fusionados con merge-validate en PASS (incluido chequeo de digests idénticos)
- [ ] results/ completo entregado al coordinador científico para análisis congelado
- [ ] Registro de incidentes consolidado para la sección de métodos
