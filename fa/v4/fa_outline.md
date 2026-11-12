# v4 FA — writer handoff

Reformat of `error_modes.md`. **No new analysis.** Every cell traces to a verified
row there. Cells are clipped deliberately: they are facts to work from, not
sentences to lift.

Shape follows the accepted FA from the influenza/HAI task — numbered
prescriptions in Part 2, each naming the run that did it correctly with a
location, then a closing "everything else was already right" line with its
exceptions verified.

---

# PART 1 — what the model did wrong

## M1 (primary) — sST2's decoy direction raised in reasoning, dropped from the deliverable

**Runs:** `c402acd4`, `bd4f9a92`.

| Run | What it produced | Where |
|---|---|---|
| `c402acd4` | thinking: *"since it's a decoy that sequesters IL-33, sST2-high patients may actually have low free IL-33"* | thinking block 36 |
| `c402acd4` | deliverable: sST2 → "Yes, first in line: prognostic enrichment / stratification at enrolment" | §6.3 biomarker table |
| `c402acd4` | deliverable, the only decoy mention: "sST2 is IL-33's decoy receptor, and stressed tissue releases it under many stimuli" | §1, marked *(context)* |
| `bd4f9a92` | thinking: *"not just that its decoy receptor is up"* | thinking block 58 |
| `bd4f9a92` | thinking: *"free serum IL-33 is rapidly oxidized and sequestered by sST2"* | thinking block 21 |
| `bd4f9a92` | deliverable: section asserting the axis "is engaged in our target patients" | §3.2 heading |
| `bd4f9a92` | deliverable: alternatives tested = cardiac (NT-proBNP 1.20–1.24, troponin I 1.18) and renal (cystatin C 1.39); decoy direction absent | §3.2, "Alternative explanations for sST2 are weak in our own data" |
| `bd4f9a92` | deliverable: sST2 rejected as PD on a different ground — "the in-vitro response is small and absent in HGMEC" | §7 |

**Zero matches** in either deliverable for: sequester / buffered / mopped / already
neutralised / redundant / equally consistent.

**Why it is wrong, in the room's own terms.** sST2 is the soluble decoy. Elevation
is compatible with pathway activity **or** with ligand already bound. Under the
second reading an sST2-high patient carries least free IL-33 — the inverse of what
sST2-based enrichment for an IL-33 antibody selects for. Neither run states this
where it assigns the role.

**Why it is not a defensible call** — runs that put it in the deliverable:

| Run | What it states | Where |
|---|---|---|
| `920dbc63` | "High sST2 may itself neutralise IL-33 (it is a decoy), which could make an antibody redundant" | §3.2 |
| `920dbc63` | makes the bioassay testing it a kill criterion | §3.3, §4.5 Gate 1 |
| `970c71dd` | "serum sST2 itself sequesters IL-33, so the bioassay must be read together with total IL-33… not a kill by itself" | §5.2 design note |
| `92f09677` | "A high value is equally consistent with IL-33 being mopped up" | §2.2 |
| `dbd6f47e` | "equally consistent with IL-33 being sequestered, so direction must be tested first" | §7 ruled-out table |
| `cc5a3c81` | "high sST2 could even mean IL-33 is already buffered… why the gate measures free IL-33 and the IL-33:sST2 complex" | §3.2 |
| `af1a3322` | "sST2 in the sample will buffer it" | Gate 1a feasibility caveat |

**Exemplar for the failure item:** `920dbc63` — one clause, in the case-against
column, and carried through to a kill criterion.

**One honest limit to carry.** Nothing in the room shows IL-33 *is* sequestered.
The six runs state it as a possibility that must be tested, not as a finding. The
item is that the objection went unstated where the role was assigned — **not** that
sST2 enrichment is wrong.

---

## M4 (mention) — isotype comparator's timepoint-dependence not named

**Runs:** `af1a3322`, `920dbc63`.

| Run | What it produced | Where |
|---|---|---|
| `af1a3322` | "Reversal is complete for robust genes at both timepoints, and the isotype is inert" | §4.1 |
| `920dbc63` | "The IL-33 + isotype arm reproduced the full IL-33 response (median log2FC 4.12 vs 4.02)" — no timepoint named | §2.1 |

**[computed]** Isotype retains **0.991** of the IL-33 response at 6 h, **0.874** at
24 h among induced genes under independent selection (select at 6 h, measure at
24 h; n = 205). Dependent selection gives 0.844 — about a quarter of the apparent
effect is winner's curse. Genome-wide the difference is centred at zero at both
timepoints, so a genome-wide null is a valid calibration target.

**Exemplar:** `c402acd4` — "The isotype control is not neutral at 24 h… keeps 95%
at 6 h but only 86% at 24 h. Any claim of AX-1177 efficacy 'vs IL-33 alone'
therefore overstates it." Names convention, both timepoints, direction of error.
Also `cc5a3c81` (tabulates both conventions), `dbd6f47e` (slope −0.82 vs −0.62),
`bd4f9a92` (restricts the claim to 6 h).

**Honest limit.** Use 0.874, not 0.844. The larger figure comes from a selection
sharing a group with the quantity measured.

---

## M2 (mention) — procoagulant switch not stated directionally

**Runs:** `cc5a3c81`, `970c71dd`.

| Run | What it produced | Where |
|---|---|---|
| `cc5a3c81` | "procoagulant genes: tissue factor (F3, +5.6) and PAI-1 (SERPINE1, +1.7)" — no anticoagulant arm | §2.1 |
| `970c71dd` | F3 +5.6 listed among neutrophil-mobilising genes; haemostatic module not characterised | §3.1 |

**[computed]** THBD −1.0005, `adj.P.Val` 1.72e-10, implied SE 0.123.

**Exemplar:** `c402acd4` ("tissue factor +5.6, PAI-1 +1.7, uPA +1.5, thrombomodulin
−1.0"); also `920dbc63` (adds eNOS −1.1), `92f09677`, `dbd6f47e`, `bd4f9a92`.

**Honest limit.** `cc5a3c81`'s statement is true as far as it goes; `970c71dd`'s is
an omission, not an error. Expect this one to be pinged.

---

## M3 (mention) — serum assays reported as proteins

**Runs:** `af1a3322`, `bd4f9a92`.

| Run | What it produced | Where |
|---|---|---|
| `af1a3322` | "#2 of 1,094 proteins"; "176 of 178 significant proteins"; no reconciliation anywhere | §2 claim 5, §3 |
| `bd4f9a92` | "Of 1,094 serum proteins"; "82% of all 1,094 proteins" | §1, §1 |
| `bd4f9a92` | computes the distinction elsewhere: "27 proteins appear on >1 panel (58 assays)" | §9 |

**[computed]** 1,094 assays = 1,063 analytes. The load-bearing suffix is `-NEUI`:
`GDNF-INFI` and `GDNF-NEUI` are one analyte. `-CAM` is not a panel suffix —
stripping it mangles `Ep-CAM` and `Nr-CAM`.

**Exemplar:** `920dbc63` — corrects it explicitly as a ruled-out item: *"'178
significant proteins.' Corrected: this is 169 unique proteins."*

**Honest limit.** 2.9% denominator error, changes no conclusion.

---

# PART 2 — what the model should have done

Prescriptions, each with the run that did it correctly. **Verdict block elements
are listed, not drafted** — the accepted format wants that paragraph in the
writer's prose.

## Verdict block — elements to assemble

| Element | The call |
|---|---|
| Asset | keep; freeze indication-directed spend |
| Indication, out | severe lower respiratory viral infection as framed |
| Indication, in | host-response-defined severe pneumonia; endothelial/thrombo-inflammatory phenotype; pathogen-agnostic as hypothesis |
| Population | hospitalised, pre-critical, sST2-high at admission |
| Enrichment marker | sST2; not PD, not target engagement |
| Target engagement | free/total IL-33 and IL-33:sST2 complex; assay does not exist |
| PD panel | IL-6, CCL20, CCL7, OPG, IL-18R1, CSF-1, IL-1β, tissue factor — readable SEs, drug-reversed, outcome-linked |
| Patient sampling | enrolment, pre-dose |
| In-vitro readout | 6 h primary, 24 h secondary |
| Decision structure | gated hold, kill criteria pre-committed, decisive gate on material already held |
| Named limits | no virus, no animal, no dose-response anywhere in the package; one concentration; single donors; reduced IL-33 only |

## Components, each with what derives it

| # | Component | The call | What derives or supports it |
|---|---|---|---|
| 1 | Target engagement established | yes, ligand-dependent | 1126 attributable genes, HUVEC 6 h, `Compound_47_IL33_vs_IL33_IC119_HUVEC_6hrs`; antibody-alone sets disjoint (6 of 1126, 1 of 487); receptor-null lines bound the null at 13–40 |
| 2 | Comparator convention | isotype-matched, and name its 24 h behaviour | isotype retains 0.991 at 6 h, 0.874 at 24 h (independent selection); "vs IL-33 alone" overstates |
| 3 | Programme blocked | interferon + neutrophilic + procoagulant | 23 readable genes; F3 +5.636 and SERPINE1 +1.744 up **with THBD −1.001 down** |
| 4 | Type 2, in vitro | not testable — do not read it either way | endothelial monocultures only; A549/MCF7 never received IL-33; no ILC2/Th2/mast/basophil; IL4 `AveExpr` −4.164 (4th pctile), TSLP −3.999 (5th) |
| 5 | Type 2, excluded on | serum and tissue | IL5 OR 1.001 (`adj.p` 0.9999), eotaxin-1 ×2, eotaxin-2, CCL17, tryptase, IL-5Rα, KIT, CD63 all null; IL13RA1 4.803 fails adjustment; tissue eosinophil/basophil/mast scores do not separate COVID+ from COVID− pneumonia |
| 6 | Reproducibility | 6 h across two beds, not 24 h | median \|logFC\| 2.0140 vs 0.7367, factor 2.7337 at 6 h; 2.2349 vs 0.5136, factor 4.3512 at 24 h; 315 genes at 6 h and 23 at 24 h on direction **plus adjusted** significance (nominal gives 458 and 83) |
| 7 | Human evidence | associative; no drug arm anywhere | `AX-1177_serum_proteomics` cross-sectional at enrolment, no treatment arm; sST2 rank 2 of 1094, OR 3.0243 (1.83–5.01) |
| 8 | sST2 role, not-higher | enrichment only | decoy; elevation equally consistent with ligand already bound, so not target engagement and not proof of activity |
| 9 | sST2 role, not-lower | keep it, do not discard | rank 2 of 1094; survives NEWS2 adjustment; CI ratio 2.74 against a median of 3.92; cardiac (NT-proBNP) and renal (cystatin C 1.39, p 0.18) alternatives both weak |
| 10 | Readouts for validation | 13 prognostic ∩ 6 h signature; 8 with usable precision | CCL20 1.830 (1.284–2.608), MCP-3 1.719, IL6 2.066–2.308 ×4 panels, B4GALT1 2.315, IL1B 2.447, FSTL3 2.527, TRIM21 2.950, TANK 3.324; ICAM1 `adj.P` 0.0101, implied SE 1.744 |
| 11 | Readouts excluded | SELE, VCAM1, CXCL8, CXCL1, IL1RL1 | implied SE 8.866 / 7.064 / 4.061 / 1154.884 / 8.324 against a file median of 0.339 — indeterminate, not negative |
| 12 | Magnitudes not usable | CSF-1, CTSS, BIRC2 | OR 90.095 (4.200–1932.572), 23.199, 12.437 — per-log-unit scale, not effect size |
| 13 | Alternative closed — type 2 airway | no | component 5, plus no epithelial IL-33 arm exists |
| 14 | Alternative closed — kidney | no | HGMEC has no vehicle arm so its IL-33 response is unmeasured; serum KIM-1 and cystatin C null |
| 15 | Alternative closed — cardiac | no | NT-proBNP weak, so the sST2 signal is not cardiac strain |
| 16 | Alternative closed — oncology | no | A549/MCF7 are antibody-only specificity controls |
| 17 | Package-level limit | state it | BH reproduces at 1,194 tests against 1,094 delivered (ratio constant 1094/1194; binding ranks imply 1194.00); ~100 analysed assays absent; IL-33 itself not among the 1,094 |
| 18 | Unit of analysis, tissue | donor, not block | 74 blocks carry a Block ID from 31 donors (78 rows include 4 blank spacers); 3 donors supply 24 of 49 COVID+ blocks |

## Closing line — exceptions verified run by run

Candidates for "everything else was already right in all eight", each checked
individually rather than screened:

| Thing | All eight? | Exception |
|---|---|---|
| Gated hold with pre-committed kill criteria | yes | — |
| sST2 assigned enrichment/stratification, not target engagement | yes | — |
| Per-log-unit OR not read as effect size | yes | `970c71dd` addresses the OR scale without naming CSF-1 |
| No potency, affinity or IC50 invented | yes | — |
| Post-mortem analysed at donor level, pseudo-replication named | yes | — |
| Causality not claimed from the serum data | yes | — |
| Set-level enrichment test run and null reported | yes | — |
| **6 h as the primary in-vitro / ex-vivo readout** | **no** | **`bd4f9a92`** justifies patient sampling on the 6 h-vs-24 h kinetics but sets no ex-vivo readout timepoint; its Gate 1 bioassay names none |
| Type 2 excluded on serum and tissue rather than in vitro | **no** | **`cc5a3c81`** asserts "There is no type-2 output" from filter-removed genes (§2.1, repeated in its ruled-out table) |

**Do not write "all eight" against the last two.** Both exceptions are the kind a
reviewer greps for.
