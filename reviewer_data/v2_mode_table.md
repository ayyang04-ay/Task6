# v2 — pre-registered failure modes

For the FA session. Four modes, each stated so a second annotator can decide
yes/no per trajectory without exercising judgment.

Every figure is asserted against the shipped room by
`scratch/analysis/verify_golden_v2.py`, 64 claims. Occupancy is measured
against the eight v1 trajectories — c3051d03, 5ee4d9d8, d96741c2, 026318d8,
3fa01b44, 85c06969, 356f2f79, d684fc0a — whose deliverables were rebuilt from
transcript file operations and are in `fa/fpfj2b81/rebuilt/`. v1 ran a
different prompt, so occupancy is a prior on what will be easy, not a
prediction.

All four are the same shape: apply domain knowledge or a statistical check to
delivered values and draw a consequence. That is where the v1 panel was thin.
Where it was strong — enumerating the package's gaps — every candidate is
occupied, so none of those became a mode.

---

## 1. `type-2-by-default` — the indication pillar

**Fails to check:** what the blocked programme actually consists of, before
naming an indication.

**If a solver falls in.** Keeps viral LRTD, or proposes an asthma, COPD or
atopic indication, on the reasoning that anti-IL-33 is a type 2 drug. Never
asks what IL-33 induces in the delivered data.

**What refutes it.** `mmc4.xlsx`, `IL33_vs_Nontreated_HUVEC_6_hrs`. Stated
carefully, because the strongest-looking version of this does not hold:
IL5, IL13, CCL11, CCL24 and IL25 are absent from the 26,210-gene universe, so
they were filtered as unexpressed and never measured — nothing follows from
that. What does follow is that where the type 2 axis is well measured it does
not move: **GATA3 at the 90.6th percentile of expression changes −0.978 at
adj.P 0.9869**, and IL1RL1 at the 52.8th changes +1.602 at 0.9803. IL4 and
TSLP sit at the 4th and 5.2nd percentiles, where only a large effect would
show — and a large one would: CXCL10 at the 5.8th percentile is induced
+6.887 and CSF2 at the 13.8th by +10.296. Against that, the interferon arm is significant
throughout (CXCL10 +6.887, IFIT1 +1.939, IFIT3 +1.727, MX1 +1.913, OAS3
+1.095, IRF1 +2.608, ISG20 +2.937), the neutrophil arm is significant
throughout (CSF2 +10.296, CXCL6 +9.406, CSF3 +8.319, CXCL3 +8.279, CXCL5
+5.301, CXCL2 +6.768, IL6 +5.817, IL1B +3.649), and haemostasis moves
coherently: F3 +5.636 and SERPINE1 +1.744 up with **THBD −1.001 down**, C3
+4.791 up.

**Counterfactual.** The indication is the severe endothelial-injury and
coagulopathy phenotype of viral LRTD, selected on that basis. Type 2
indications are excluded not because type 2 biology is shown absent but
because the package cannot speak to it: the effectors were never measured and
the two type 2 genes it does measure well are unmoved.

**Occupancy: 0 of 8.** No run named THBD or SERPINE1, so none characterised
the haemostatic shift directionally; four named F3 alone. Every type 2 mention
in all eight concerns `mmc3` eosinophil IHC or the Olink panel, not the
transcriptomic response.

**Why it is not defensible to skip.** The prompt asks what indication the data
points at. Answering without reading what the data shows the antibody blocks
does not address the question.

---

## 2. `unenriched-intersection`

**Fails to check:** whether the overlap between the signature and the
prognostic analytes exceeds the base rate.

**If a solver falls in.** Reports that N analytes are both prognostic in serum
and in the signature, and treats the intersection as evidence of translational
relevance, with no denominator.

**What refutes it.** In `mmc2.xlsx`, **893 of 1094 odds ratios exceed 1**
(binomial p 1.6e-104) and **176 of the 178 significant rows point the same
way**. Being prognostic in this panel is close to universal, so an
intersection is uninformative until tested. The test: 38 of the 315 signature
genes have any analyte on the panel, 13 of those are significant in serum, and
the base rate is 169 significant analytes of 1063, or 15.9%. Expected 6.0
against 13 observed — **2.15-fold enrichment, hypergeometric p 0.0037**.

**Counterfactual.** The overlap is real and is the only result in the package
linking the in vitro programme to human outcome as a statistical claim. Run
the test and the shortlist is established; skip it and the same 13 analytes
are an unsupported list.

**Occupancy: 0 of 8.** Several runs intersected the signature with prognostic
markers. None computed a base rate or an enrichment. d684fc0a alone noted the
global directional shift, and did not connect it to its own shortlist.

**Why it is not defensible to skip.** The 81.6% figure is one line of
arithmetic over a column the solver has already read, and once seen it makes
the untested intersection indefensible.

---

## 3. `attenuation-as-nuisance-only`

**Fails to check:** what the between-bed effect-size difference says about
which model to use, as opposed to how to threshold.

**If a solver falls in.** Uses the 2.7-fold attenuation only to argue that a
fixed fold-change cut misjudges reproducibility — correctly — and then
recommends a model, or a next study, without reference to it. Or treats HUVEC
as the model because that is where the data is.

**What refutes it.** HUVEC is umbilical vein, macrovascular and venous;
HGMEC is glomerular, microvascular and renal. Neither is pulmonary and the
indication is a lung disease. Between those two beds the same antibody effect
differs **2.7337-fold at 6 h** (median |logFC| 2.0140 against 0.7367) and
**4.3512-fold at 24 h** (2.2349 against 0.5136). That is a measurement of how
much bed identity changes the result.

**Counterfactual.** Direction and membership transfer — 315 genes move the
same way in both beds at 6 h, sign agreement 76.82%, all four modules negative
in both — so the hypothesis that lung microvascular endothelium behaves in the
same direction is reasonable and is the best inference available. Magnitude
does not transfer, so the confirmatory study runs in lung endothelium and is
powered on direction and gene set rather than on these effect sizes.

**Occupancy: 2 of 8 partial.** All eight named the two beds. 5ee4d9d8 proposed
"lung microvascular endothelium or airway/alveolar epithelium" as the model and
85c06969 noted "umbilical-vein (not lung) endothelium". Neither derived the
recommendation from the attenuation figure, and the other six did not raise
the bed question in their model choice.

---

## 4. `point-estimate-without-interval`

**Fails to check:** whether an odds ratio is estimated precisely enough to act
on.

**If a solver falls in.** Nominates CSF-1, CTSS or BIRC2 as markers, or ranks
the shortlist by odds ratio, on point estimates of 90.095, 23.199 and 12.437.

**What refutes it.** Their 95% intervals are **4.200 to 1932.572**, 2.691 to
200.019 and 2.409 to 64.215 (`mmc2.xlsx`, `l95` and `u95`). All three are
significant and the direction is informative, but the magnitude is not
estimated at n = 100 and no study could be sized on them. By contrast the
eight usable analytes have upper bounds under 11, and ST2's interval ratio of
2.74 against a median of 3.92 across the 178 significant rows is what a
well-estimated marker looks like here.

**Counterfactual.** Separate the eight analytes whose magnitude is estimated
from the three whose direction only is, and say which is which.

**Occupancy: 0 of 8.** No run raised the precision problem. The `l95` and
`u95` columns are hidden in the delivered workbook, which is an authentic
property of the source file rather than anything added.

---

## Considered and not pre-registered

| Candidate | Why not |
|---|---|
| **The verdict.** All eight v1 runs recommended against advancing where the v1 golden recommended advancing. | The v2 golden now agrees with them, and the v2 grader places the verdict under NEUTRAL. Standing rule 4 grades the pillars and the justification, not the verdict. |
| **mmc3's IL-33 scores.** COVID-positive pneumonia carries the lowest median in all three compartments: epithelium 4.25 against 5.50, endothelium 4.75 against 5.50, smooth muscle 2.75 against 3.25. | Kept in the golden as evidence, since the case is built from everything the room offers. Weak as a mode: a single reader's semi-quantitative scores on a cohort unrelated to the serum patients, with controls near the ceiling, is something a careful expert could decline to weight. |
| Molar excess — 41.3-fold, all four inputs in the annex | Occupied 8 of 8. 5ee4d9d8: "only one 41:1 antibody-to-IL-33 molar ratio was tested". |
| IL-33ox never tested though the annex claims dual-form binding | Occupied 8 of 8. |
| Epithelial lines never receive IL-33 | Occupied 7 of 8 explicitly. |
| mmc3 compartment analysis | Occupied 4 of 8, and they reached a finding the golden had missed. |
| mmc5 sheet duplication and row padding | Occupied 8 of 8. Three ran explicit row-matched identity tests; 85c06969 compared all 629,040 rows. |
| sST2 as a pharmacodynamic readout | Marginal in v1 and the basis has changed: IL1RL1's implied SE of 8.32 sits outside the attributable set's 1.7439 ceiling, so its non-significance resolves nothing. The golden now excludes sST2 because `mmc2` has no drug arm and no file measures sST2 protein under antibody. Two v1 runs handled it correctly as a stratification marker. |
| Threshold intersection giving 219 | The v1 basin. Occupied 0 of 8 in the sense that nobody fell in — every run used correlation, slope or sign agreement. Retained in the grader's B section because the error remains possible, but not expected to fire. |
