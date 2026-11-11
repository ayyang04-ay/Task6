# v2 — verdict and pillars

Reshape. The v1 golden recommended carrying the asset forward on the 6 h
signature. The source authors' own conclusion is narrower: "Although this does
not show a causal relationship with disease, these results provide a rationale
to evaluate pathological roles for IL-33 in viral LRTD." All eight v1 runs
reached that position independently from the data alone. The v1 verdict was
the outlier.

**The paper is not mounted and the golden cites nothing from it.** Every value
below is derivable from the four workbooks and the annex.

## Verdict

Do not advance to IND-enabling work. The package establishes that the antibody
engages IL-33 and characterises the programme it blocks, but not that the
pathway drives disease. Fund target validation, in the models and at the
timepoint the data identifies, with the readouts it supports. The programme the
antibody blocks is not the one anti-IL-33 is conventionally developed against,
and that changes which indications to consider.

Deliverables shift from a go/no-go to **what to measure, in which model, when,
what goes into the clinic** — the prompt's four asks — plus **which indications
the data points at**.

## P1 — Target engagement is established and is ligand-dependent

**For.** 1126 genes are attributable in HUVEC at 6 h (`AX-1177_rnaseq_contrasts`,
`Compound_47_IL33_vs_IL33_IC119_HUVEC_6hrs`, `adj.P.Val < 0.05` and
`|logFC| > 1`). The effect requires ligand: the antibody-alone sets are
disjoint from the attributable sets, overlap 6 of 1126 in HUVEC 6 h and 1 of
487 in HGMEC 6 h, and dropping every standalone-significant gene leaves 1114
of 1126 with the attenuation moving 2.7337x to 2.7341x. The receptor-null
lines bound the null at 13 to 40 genes across six arms.

**Against.** One donor per endothelial line, three wells not three donors
(annex §3). One concentration, 10 ug/mL. Reduced IL-33 only; the oxidised form
the annex names in §1 is never tested. No affinity, potency or exposure data —
annex §1 places them outside the delivery. The annex states that `Compound_47` is the research designation for
AX-1177, so the test article's identity is not in question.

**Caveat.** HGMEC has no vehicle arm, so the IL-33 response there is never
measured, only the part the antibody reverses.

## P2 — The programme blocked is interferon-driven and neutrophilic with a procoagulant endothelial switch

**This is the pillar that sets the indication, and it is the one no v1 run
made.**

**For.** In `AX-1177_rnaseq_huvec_il33.xlsx`, `IL33_vs_Nontreated_HUVEC_6_hrs`:

| Arm | Genes | Result |
|---|---|---|
| type 2 effectors | IL5, IL13, CCL11, CCL24, IL25 | **not in the table at all** |
| type 2, measured | IL4 −1.229 at `AveExpr` −4.164 (4th pctile), TSLP +0.176 at −3.999 (5th), CCL26 −0.839 at −2.016 (29th), GATA3 −0.978 (SE 22.891), IL1RL1 +1.602 (SE 8.324) | **uninformative.** IL4 and TSLP are in the bottom tenth of expression, so their nulls cannot separate *not induced* from *not detectable*; GATA3 and IL1RL1 are unreadable. CCL26 alone is readable and null |
| interferon | IFIT1 +1.939, IFIT3 +1.727, MX1 +1.913, OAS3 +1.095, CXCL10 +6.887, IRF1 +2.608, ISG20 +2.937 | **all significant** |
| neutrophil chemoattraction | CXCL2 +6.768, CXCL3 +8.279, CXCL5 +5.301, CXCL6 +9.406, CSF2 +10.296, CSF3 +8.319, IL1B +3.649, IL6 +5.817 | **all significant** |
| coagulation and complement | F3 +5.636, SERPINE1 +1.744, C3 +4.791 up; **THBD −1.001 down** | **all significant, and directionally coherent** |

Tissue factor and PAI-1 up with thrombomodulin down is a procoagulant switch,
not a list of inflammatory genes. The same four modules carry through the
reproducible signature: every member of the interferon, NF-kB, CSF/cytokine
and chemokine sets in it is negative under antibody.

**Against.** One cell type. In vitro. No infection anywhere in the package, so
this characterises what IL-33 does to endothelium, not what happens in disease.

**The type 2 half of this pillar does not hold and is withdrawn.** The only
IL-33 arms are endothelial monocultures; A549 and MCF7 never received IL-33.
Those cultures contain none of the cells through which IL-33 drives type 2
biology — ILC2s, Th2 cells, mast cells, basophils — and IL4 is a lymphocyte,
mast cell and basophil product while TSLP is epithelial. The stimulation data
therefore cannot test type 2 in either direction, and an answer that says type 2
was not tested in vitro is correct. Note the asymmetry: low expression does not
void a positive, since CSF2 sits at the 14th percentile and is +10.296 at
`adj.P` 5.3e-23 — it is only a *null* at low expression that carries no
information.

**Consequence.** Anti-IL-33 is conventionally developed against type 2 disease.
The programme this package shows the antibody blocking is interferon-driven,
neutrophilic and procoagulant. On the package's own evidence the indication to
consider is endothelial injury with thrombotic and neutrophilic features, which
is what `AX-1177_serum_proteomics`'s composite endpoint of ICU, ventilation or death selects for and
what `AX-1177_postmortem_lung`'s 20 COVID-positive and 10 COVID-negative pneumonia blocks sample.

Type 2 indications are unsupported, and the support for that comes from the
patients rather than the cultures: nine type 2 and effector-cell markers in
`AX-1177_serum_proteomics` are all null against the endpoint (IL5 OR 1.001 at
`adj.p` 0.9999, eotaxin-1 on two panels, eotaxin-2, CCL17, tryptase, IL-5Rα,
KIT, CD63; IL13RA1 at 4.803 is the only near miss and fails adjustment), and the
tissue eosinophil, basophil and mast cell scores do not separate COVID-positive
from COVID-negative pneumonia.

## P3 — Reproducibility: 6 h across two endothelial beds, not 24 h

**For.** Over the 1126-gene set: median `|logFC|` 2.0140 in HUVEC against
0.7367 in HGMEC, a factor of 2.7337 at 6 h; 2.2349 against 0.5136, a factor of
4.3512 at 24 h. Pearson r 0.6216 against 0.3032. Sign agreement 76.82% against
64.27%. Signature 315 genes against 23 under direction plus adjusted
significance (`adj.P.Val < 0.05`); nominal p would give 458 and 83.

**Against.** A fixed `|logFC| > 1` cut applied to the attenuated line gives 219
and reads as failure; the cut is invalid on that line and admits 11
sign-discordant genes. HGMEC is glomerular microvascular, not pulmonary.

**Caveat.** This is now a design input for validation — measure at 6 h — rather
than a verdict.

## P4 — The human evidence is associative, with no drug arm anywhere

**For.** `AX-1177_serum_proteomics` is cross-sectional at enrolment in 100 hospitalised patients
with no treatment arm. It establishes that sST2 tracks outcome, rank 2 of 1094
assays at OR 3.0243 (1.83 to 5.01). It cannot establish that any marker moves
on treatment. `AX-1177_postmortem_lung` is post-mortem tissue from an unrelated cohort with no
patient identifiers in `AX-1177_serum_proteomics`, so the two cannot be linked in either direction.
No file in the package involves a virus, an animal, or a dose.

**Against.** Nothing in the room contradicts a causal role; the package is
silent rather than negative.

**Caveat.** The Benjamini-Hochberg correction in `AX-1177_serum_proteomics` only reproduces at
1,194 tests against 1,094 delivered (the ratio of delivered adjusted p to the
BH value at the delivered count is a constant 1094/1194 across all rows, and
the binding step-up ranks imply m = 1194.00 exactly), so roughly 100 analysed
assays are absent
and at least four of them were significant. IL-33 itself is not among the 1,094.

## P5 — The readouts validation should carry

**For.** 13 analytes are both prognostic in `AX-1177_serum_proteomics` and inside the 6 h
signature. Eight have usable precision: CCL20 1.830 (1.284 to 2.608), MCP-3
1.719, IL6 2.066 to 2.308 across four panels, B4GALT1 2.315, IL1B 2.447,
FSTL3 2.527, TRIM21 2.950, TANK 3.324. ICAM1 is the attributable adhesion
readout at `adj.P.Val` 0.0101 and implied SE 1.744, inside the signature's
1.7439 ceiling.

**Against.** CSF-1 at OR 90.095 (4.200 to 1932.572), CTSS at 23.199 and BIRC2
at 12.437 are significant but their magnitudes are not estimated at n = 100.
SELE, VCAM1, CXCL8, CXCL1 and IL1RL1 carry implied SEs from 4.110 to 1137.323,
outside that ceiling, so attribution for them is indeterminate rather than
negative. sST2 is prognostic and has no measured drug response anywhere in the
package.

## What this does to the FA

Aligning the verdict to what the runs concluded removes the verdict divergence,
so discrimination has to live in the pillars. Checked against the eight v1
transcripts:

| Pillar | Occupied by v1 runs? |
|---|---|
| P1 | yes — several ran the standalone-arm check |
| **P2** | **partly, and the unoccupied half was wrong.** The type 2 half is withdrawn: the v1 runs put every type-2 mention on the post-mortem workbook (then mounted as `mmc3`) or the Olink panel, which is the correct place for it, so their reading was right and the pillar's was not. The procoagulant half stands and was genuinely unoccupied: no v1 run named THBD or SERPINE1, so none characterised the switch directionally, and four named F3 alone |
| P3 | yes — all eight reached the timepoint result |
| P4 | yes — all eight, and it is why they said no |
| P5 | partly. None raised the odds-ratio precision problem |

The procoagulant switch, stated directionally, is the surviving candidate basin.
The type 2 claim is not a basin; it was an error, corrected after v4 QA.
