# Pre-Registration DRAFT v0.9.2 — Collective drift from human norms in locally deployed LLM agent teams under supervisor influence

**Date of draft:** 2026-08-14 (v0.9.2 same day: team fixed at 5 sites; 7 candidate models, each at exactly 2 sites). **Status:** NO data collected. FROZEN as v1.0 upon written ratification by all participating authors (target: before any site runs baselines). Amendments after freeze: dated log, as in Study 1.
**Relation to Study 1:** independent study; inherits the frozen supervisor framings (prestige+retention / peer) and platform architecture; new instrument, new inclusion rule, new outcome (drift from human norms).
**Sites:** 5 independent computers/operators (site1–site5; 7 candidate models, each run at exactly 2 sites; provisional assignment in ASSIGNMENTS.md, confirmed at freeze). Canonical code lives in a private GitHub repository; every run manifest records site-id and git commit hash; each model×condition cell is run at ≥2 sites (built-in replication). Data enter analysis only via the repository after automated merge validation.

## 1. Research question
As agent teams built on small local models are deployed with one agent in a supervisory role, does supervisor influence pull team judgments on subjective questions away from documented human norms — and does this depend on how strong the human consensus is?

## 2. Item bank and human norms (constructed before any model sees any item)
Binary-choice subjective items with per-item human response distributions from public datasets: MoCA moral-permissibility (25 human annotations/item; Nie et al. 2023), Scruples Anecdotes (≥10 annotations/item; Lourie et al. 2021), and Chaos-NLI (100 annotations/item; non-moral subjective tier). Consensus tiers by human majority share m: **T1 near-unanimous** (m ≥ .90), **T2 high-majority** (.70 ≤ m < .90), **T3 divided** (.50 ≤ m < .70). Target: 30 items/tier balanced across sources (bank of 90; expandable by amendment before freeze). Every item carries source, ids, n_annotators, and the human distribution; the platform refuses to run items lacking verified norms. The human-norm populations (US-centric crowdworkers/Reddit) are a declared limitation, stated in the manuscript, not discovered by reviewers.

## 3. Conditions (teams of 8 subject agents; supervisor scripted, first responder; framings frozen verbatim from Study 1)
- **C0 — no supervisor:** team answers sequentially (rotated order); measures spontaneous team drift (interaction-only).
- **C1 — aligned supervisor:** prestige+retention framing; supervisor advocates the human-majority option on every T1/T2 round (T3: the more-frequent option).
- **C2 — counter-normative supervisor:** identical framing; supervisor advocates the human-MINORITY option on a seed-scheduled 75% of T1/T2 rounds (25% majority option, providing within-condition floor); on T3 rounds advocates a seed-fixed side (T3 measures pure susceptibility — "counter-normative" is undefined without consensus, and is analyzed as such).
- **C2p — peer control:** identical answer stream to C2 (yoked seeds), supervisor introduced with the frozen peer framing. Isolates authority framing, as in Study 1.
Sessions: 36 rounds, items sampled without replacement stratified by tier; item streams and supervisor schedules seed-yoked across C1/C2/C2p.

## 4. Baselines and probes
- **Solo baseline (pre-condition):** per model×item, K = 16 isolated samples at the run temperature → the agent's own propensity p̂(option) per item. Run before any social condition at each site holding that model.
- **Immediate private probe** after each public answer (identical wording to Study 1; comparability).
- **Deferred private probe:** at session end, each agent is re-asked every critical item in-context, prefaced that the task and all evaluation are over ("for the record, visible to no one"). New relative to Study 1; responds to the response-persistence critique.

## 5. Hypotheses (directional, confirmatory)
- **H1 (induced drift):** P(public answer = human-majority option) on T1/T2 counter-normative rounds is lower in C2 than in C0 and than in C1.
- **H2 (consensus gradient):** the C2–C0 drift is larger in T2 than in T1 (condition × tier interaction): weaker human consensus → weaker anchor.
- **H3 (authority vs peer):** drift in C2 exceeds C2p. (Study 1 predicts a small effect concentrated where the supervisor conflicts with an emergent team consensus; exploratory decomposition planned.)
- **H4 (sphere dissociation):** immediate and deferred private probes on critical rounds show whether public drift is accompanied by private drift; directional prediction (from Study 1): no immediate public–private divergence; the deferred probe is the stronger test and is confirmatory for the presence/absence of persistence, with equivalence bounds ±5 pp.
- **H5 (baseline-relative influence):** on critical rounds, P(agent adopts the supervisor-advocated option) in C2 exceeds the agent's own solo-baseline propensity for that option on that item (within-item, within-model contrast).
All falsifiable; nulls published with TOST (±5 pp). Contingency: "teams keep human anchors under counter-normative authority" is a publishable outcome, as is the reverse.

## 6. Models and inclusion (mechanical; replaces Study 1's accuracy band)
Candidates (fixed): gemma2:9b, gemma3:latest, qwen2.5:7b, phi4, gemma3:12b, deepseek-v2:16b, llama3:8b — the Study-1 pair, three capability-excluded models readmitted under the new criterion, one DeepSeek architecture and one Llama (:cloud models vetoed by design; substitutions only by pre-freeze amendment). Inclusion requires, on a 20-item stratified calibration subset: (a) format compliance ≥ 95% after one re-prompt; (b) baseline stability: mean split-half absolute difference of item propensities < 0.15 with K = 16. No capability ceiling exists for subjective items; exclusions logged with traces.

## 7. Sample sizes
Per model×condition: ≥ 2 sites × 1 session × 36 rounds × 8 agents = 576 agent-trials (~430 critical in C2/C2p). Power for H1 at baseline-follow rates ~0.15–0.25 and smallest effect of interest 10 pp: >0.90 at α=.05 one-sided with clustering inflation. Caps and no optional stopping as in Study 1.

## 8. Analysis (frozen before unblinding)
Trial-level GEE/GLMM (logit): outcome = answer-is-human-majority (H1–H3) or adopts-supervisor-option (H5); fixed: condition, tier, their interaction, model; clusters/random: site, session, item. Item-level alignment distance (Jensen–Shannon divergence between team answer distribution and human distribution) by condition as descriptive complement. Exact tests alongside asymptotic where events are sparse; Holm within families; TOST for nulls. Site treated as random factor; site×condition heterogeneity reported.

## 9. Integrity protocol (multi-site)
Single canonical repo; runs only from tagged commits; manifests record site-id, commit sha, seeds, framing hashes, model digests; results enter via pull request and `merge-validate` (schema, hash, seed-collision and duplicate checks); mock-mode acceptance required per site before real runs; incidents logged, never hidden; all sites' data reported regardless of outcome. Lessons of Study 1 (single-source-of-truth, no untracked code edits, no out-of-roster runs) are hard rules from day one.

## 10. Pre-freeze task list (blocking)
(1) Item bank built and verified from source datasets with licenses checked; (2) full-text delimitation reading of arXiv:2606.14037, 2607.21558, 2508.14918 logged in the related-work memo; (3) author ratification of this document → v1.0 freeze; (4) per-site mock acceptance.
