# v4 FA — the two form questions, as tables

Reformat of `fa_outline.md`. No new analysis. Cells clipped: facts to type from,
not sentences to lift.

---

## Q1 — What did the model do wrong?

| Mode | Runs | The artefact | Where |
|---|---|---|---|
| **sST2 decoy direction raised then dropped** | `c402acd4` | derives it in reasoning, omits it from the deliverable, assigns sST2 "first in line" for enrichment | thinking block 36; §6.3 |
| | `bd4f9a92` | derives it in reasoning; omits it from a section that tests the cardiac and renal alternatives | thinking blocks 21, 58; §3.2 |
| Isotype comparator convention | `af1a3322` | "inert" asserted at both timepoints | §4.1 |
| | `920dbc63` | 6 h figure carried as a general claim | §2.1 |
| Procoagulant switch not directional | `cc5a3c81` | F3 and PAI-1 only, no anticoagulant arm | §2.1 |
| | `970c71dd` | F3 among inflammatory genes; module not characterised | §3.1 |
| Assays reported as proteins | `af1a3322` | "1,094 proteins", "178 significant proteins", no reconciliation | §2, §3 |
| | `bd4f9a92` | "1,094 serum proteins" in bottom line, reconciled in §9 | §1; §9 |

**Figures the items stand on** — all **[computed]** from the room:

| Claim | Value |
|---|---|
| sST2 | OR 3.0243 (1.8269–5.0067), `adj.p` 0.00746, rank 2 of 1094 |
| Isotype retention, 6 h | 0.991 |
| Isotype retention, 24 h, independent selection | 0.874 (n = 205) |
| Isotype retention, 24 h, dependent selection | 0.844 (n = 313) — inflated, do not use |
| THBD | −1.0005, `adj.P.Val` 1.72e-10, implied SE 0.123 |
| F3 / SERPINE1 | +5.6357 / +1.7442 |
| Assays vs analytes | 1,094 / 1,063 |

---

## Q2 — What should the model have done?

Prescription, then the run that did it, then where. **Each prescription needs the
writer's own wording** — these are the facts under it.

| # | Prescription | Run that did it | Where |
|---|---|---|---|
| 1 | State that sST2's elevation is equally consistent with IL-33 already being bound, where the role is assigned | `920dbc63` | §3.2, one clause; carried to a kill criterion at §4.5 |
| 2 | Or make it a gate-design constraint rather than a caveat | `970c71dd` | §5.2 design note |
| 3 | Name the comparator and its timepoint behaviour wherever a reversal figure is quoted | `c402acd4` | §4.1, one sentence, with the direction of the error |
| 4 | State the haemostatic shift directionally — up with down | `c402acd4` | §4.1 |
| 5 | Reconcile assays to analytes before quoting a denominator | `920dbc63` | §5, as a ruled-out item |
| 6 | Treat the in vitro type-2 data as untestable rather than negative | `970c71dd` | §6 ruled-out table, "no type-2 cells tested" |
| 7 | Exclude the inflated-SE genes, or retain them with the replication argument stated | `af1a3322` excludes; `c402acd4` retains with r = −0.998 | §3; §4.1 |

## The verdict — elements, for the writer's prose block

| Element | Call |
|---|---|
| Asset | keep, spend frozen |
| Out | severe lower respiratory viral infection as framed |
| In | host-response severe pneumonia, endothelial/thrombo-inflammatory, pathogen-agnostic as hypothesis |
| Population | hospitalised, pre-critical, sST2-high at admission |
| Enrichment | sST2 — not PD, not target engagement |
| Target engagement | free/total IL-33, IL-33:sST2 complex; assay absent |
| PD panel | IL-6, CCL20, CCL7, OPG, IL-18R1, CSF-1, IL-1β, tissue factor |
| Sampling | patients at enrolment pre-dose; in vitro 6 h primary, 24 h secondary |
| Structure | gated hold, kill criteria pre-committed, first gate on material already held |
| Limits to name | no virus, no animal, no dose-response in the package; one concentration; single donors; reduced IL-33 only |

## Closing line — verified exceptions

| Candidate for "all eight" | Verdict |
|---|---|
| gated hold with pre-committed kill criteria | all eight |
| sST2 to enrichment, not target engagement | all eight |
| per-log-unit OR not read as effect size | all eight |
| no potency, affinity or IC50 invented | all eight |
| donor-level tissue analysis, pseudo-replication named | all eight |
| causality not claimed from serum | all eight |
| set-level enrichment test run, null reported | all eight |
| 6 h as primary in vitro / ex vivo readout | **not all eight — `bd4f9a92`** |
| type 2 excluded on serum and tissue, not in vitro | **not all eight — `cc5a3c81`** |

---

## Citation audit

20 deliverable quotes and 3 thinking-block quotes checked verbatim against the
rebuilt files. One correction made: `c402acd4`'s decoy line is *"sST2 is IL-33's
decoy receptor, and stressed tissue releases it under many stimuli"* (§1, marked
*(context)*), not "a decoy receptor". All others verbatim, all locations resolve.

**A clean citation audit says nothing about whether the inference holds.** The
inference check is the plain-language restatement in `error_modes.md`.
