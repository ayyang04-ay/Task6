# AX-1177 — committee audit

**Keep it. The data establishes that the antibody engages IL-33 and shows what
programme it blocks, but not that the pathway causes the disease, and the
programme it blocks is not the type 2 biology anti-IL-33 is usually developed
against. That is a reason to redirect it, not to drop it.**

---

## 1. What our data establishes

**The antibody engages the ligand, and the effect needs the ligand present.**
In HUVEC at 6 h, 1126 genes change with the antibody against the isotype
control in the presence of IL-33 (`AX-1177_rnaseq_contrasts.xlsx`,
`Compound_47_IL33_vs_IL33_IC119_HUVEC_6hrs`, `adj.P.Val < 0.05` and
`|logFC| > 1`). That is not an antibody artefact. The antibody-alone arms
(`Compound_47_vs_IC119_<line>_<tp>`, no IL-33) return 31 and 36 genes in
HUVEC and 62 and 67 in HGMEC, and those sets barely intersect the attributable
sets — 6 genes of 1126 in HUVEC 6 h, 1 of 487 in HGMEC 6 h. Dropping every
gene significant in either antibody-alone arm leaves 1114 of the 1126 and moves
the between-line attenuation from 2.7337x to 2.7341x. The two epithelial lines,
which never received IL-33, bound the null at 13 to 40 genes across six arms.

**It reproduces in a second endothelial bed, at 6 h only.** Over the same 1126
genes, median `|logFC|` is 2.0140 in HUVEC and 0.7367 in HGMEC at 6 h, a factor
of 2.7337; at 24 h it is 2.2349 against 0.5136, a factor of 4.3512. Pearson r
across the two lines is 0.6216 at 6 h and 0.3032 at 24 h; sign agreement
76.82% and 64.27%. Requiring the same direction and adjusted significance (`adj.P.Val < 0.05`) in
HGMEC leaves 315 genes at 6 h and 23 at 24 h. Nominal p would give 458 and 83.

Note what that is not. A second fixed `|logFC| > 1` cut in HGMEC returns 219
and reads as a reproducibility failure, but the cut is invalid on a line whose
effects are 2.7-fold smaller — it removes genes for being small — and it admits
11 genes with opposite signs in the two lines, including RF00003 at +2.5564 in
HUVEC and −2.7988 in HGMEC.

## 2. What our data does not establish

**That IL-33 causes the disease.** No file involves a virus, an animal or a
dose. `AX-1177_serum_proteomics.xlsx` is cross-sectional at enrolment in 100 hospitalised patients
with no treatment arm, so it shows that soluble ST2 tracks outcome — rank 2 of
1094 assays, OR 3.0243 (1.83 to 5.01) — and cannot show that anything moves on
treatment. `AX-1177_postmortem_lung.xlsx` is post-mortem tissue from a different cohort with no
identifiers shared with `AX-1177_serum_proteomics`, so the two cannot be linked either way. The
package is silent on causality, not negative.

**And the tissue data argues against elevation in the target disease.**
`AX-1177_postmortem_lung.xlsx` scores IL-33 immunohistochemistry in three compartments. Median
scores by group, COVID-negative non-pneumonia / COVID-negative pneumonia /
COVID-positive pneumonia: bronchial and bronchiolar basal epithelium 5.50 /
4.25 / 4.25; endothelium 5.50 / 5.50 / 4.75; vascular smooth muscle 3.25 /
3.25 / 2.75. COVID-positive pneumonia carries the **lowest** median in every
compartment, and staining sits near the top of the scale in the controls. So
the one tissue dataset in the package does not show IL-33 raised in the
disease the programme is aimed at. It is a different cohort from the serum
patients and was read by a single reader, so it cannot close the question —
but it does not support the premise either.

Three further gaps bear on the audit. The annex places affinity, potency and
exposure outside the delivery (§1), so there is no potency or exposure data at
all. Only reduced IL-33 was tested, although §1 names an oxidised form.
Each endothelial line is one donor and three wells, not three donors (§3), and
HGMEC has no vehicle arm, so the IL-33 response in the second line is never
measured — only the part the antibody reverses. The Benjamini-Hochberg
correction in `AX-1177_serum_proteomics` reproduces only at 1,194 tests against 1,094 delivered,
so roughly 100 analysed assays are absent and at least four were significant.
IL-33 itself is not among the 1,094.

## 3. The indication our data points at, and whether viral LRTD is right

**Viral LRTD is the right disease area and the wrong mechanism to be
developing against.** Anti-IL-33 is conventionally pursued through type 2
inflammation. Our data shows IL-33 driving nothing of the kind in endothelium.

In `AX-1177_rnaseq_huvec_il33.xlsx`, `IL33_vs_Nontreated_HUVEC_6_hrs`. The delivered statistics in
this file are not uniformly usable, so each gene is taken with its implied
standard error, `|logFC / t|`, against the file's median of 0.339. Genes beyond
about five times that are not interpretable in either direction, and the
`AveExpr` column cannot stand in for expression here because it carries one
value per gene across all 114 libraries, including the two epithelial lines.

**The type 2 axis, taken honestly.**

| Gene | logFC | implied SE | adj.P | usable? |
|---|---|---|---|---|
| IL4 | −1.229 | 0.759 (2.2×) | 0.3371 | **yes — a real null** |
| TSLP | +0.176 | 0.606 (1.8×) | 0.9705 | **yes — a real null** |
| CCL26 | −0.839 | 0.724 (2.1×) | 0.5467 | **yes — a real null** |
| GATA3 | −0.978 | **22.891 (67.6×)** | 0.9869 | no |
| IL1RL1 | +1.602 | **8.324 (24.6×)** | 0.9803 | no |
| IL5, IL13, CCL11, CCL24, IL25 | — | — | — | absent from the gene universe |

Three measured type 2 genes have sound statistics and none of them moves.
GATA3 and IL1RL1 cannot be used in either direction: their standard errors put
them in the same unreadable class as SELE at 8.866 and VCAM1 at 7.064, and a
proposal leaning on GATA3's `adj.P` of 0.9869 makes the same mistake as one
leaning on SELE's 0.4979. The five absent effectors were filtered as
unexpressed and support no claim; endothelium is not a type 2 effector cell, so
an expert would expect that.

**What is blocked, on readable statistics throughout.** Every gene below has an
implied SE under three times the median.

- **Interferon (10):** IFIT1 +1.939, IFIT2 +1.948, IFIT3 +1.727, MX1 +1.913,
  OAS3 +1.095, OASL +3.400, IRF1 +2.608, ISG20 +2.937, RSAD2 +2.028,
  CXCL10 +6.887.
- **Neutrophil chemokines (4):** CXCL2 +6.768, CXCL3 +8.279, CXCL5 +5.301,
  CXCL6 +9.406. **CXCL1 and CXCL8 are excluded** — SE 1154.884 and 4.061 —
  even though both are neutrophil chemokines carrying large fold changes.
- **CSF and cytokine (5):** CSF2 +10.296, CSF3 +8.319, TNF +7.885, IL6 +5.817,
  IL1B +3.649.
- **Haemostasis and complement (4):** F3 +5.636 and SERPINE1 +1.744 up with
  **THBD −1.001 down**, C3 +4.791 up. A procoagulant switch on four genes whose
  standard errors are 1.0×, 0.3×, 0.4× and 1.8× the median — the best-measured
  part of the whole response.

**So the claim is about what the package can support, and about which of its
numbers can be read.** It cannot support a type 2 indication: the three type 2
genes measured cleanly do not move, the two measured badly cannot be read, and
the effectors were never measured. What it can support, on twenty-three genes
with sound statistics, is a programme that is interferon-driven, neutrophilic
and procoagulant.



The same four modules carry into the reproducible 315-gene set, and every
member of each is negative under antibody: 16 interferon genes, 10 NF-κB
including NFKB2 −2.8605 and RELB −3.2667, 7 CSF and cytokine, 9 chemokine,
plus F3 −5.4739 and C3 −4.6241.

That phenotype is what the rest of the package selects for. `AX-1177_serum_proteomics`'s endpoint
is ICU admission, mechanical ventilation or death. `AX-1177_postmortem_lung` samples 20
COVID-positive and 10 COVID-negative pneumonia blocks against 5
non-pneumonia. So: stay in viral LRTD, but develop against the severe
endothelial-injury and coagulopathy phenotype rather than a type 2 one, and
select patients on that basis. Nothing in the package supports an asthma,
COPD or atopic indication, and the absence of the type 2 arm is a positive
reason not to try.

## 4. What the next studies have to establish

| Study | What it has to settle | Why our data cannot |
|---|---|---|
| Infection model in vivo, with dosing after inoculation | whether blocking IL-33 changes outcome once disease is established | nothing in the package involves a virus, an animal or a dose |
| IL-33 measured in patients, longitudinally, against outcome | whether the ligand itself rises and tracks severity | IL-33 is absent from the 1,094 delivered assays; only the receptor was measured |
| Potency and exposure characterisation | whether 10 µg/mL relates to an achievable concentration | annex §1 places affinity, potency and exposure outside the delivery |
| The oxidised form against the same readouts | whether engagement covers both species | only IL-33red was tested |
| Repeat in pulmonary endothelium, multiple donors | whether the programme is general or vascular-bed and donor specific | one donor per line, three wells; HGMEC is glomerular, not pulmonary |
| Deliver the HGMEC vehicle arm and the archived counts | the size of the IL-33 response in the second line, and the variance estimates | no HGMEC vehicle arm; counts and the fitted model are not delivered (§5) |

## 5. What to measure, when, and what could go into patients

**Readout.** The 315-gene reproducible set, and within it the four modules
above. The single most informative tissue readout is the procoagulant switch,
because it is the part with a plausible clinical correlate: F3, SERPINE1 and
THBD together.

**Model.** Primary human lung microvascular endothelium, not HUVEC and not
HGMEC. The 2.7337-fold attenuation between the two delivered lines is usually
read as a correction to apply when judging reproducibility, and it is that. It
is also a measurement of how much vascular bed identity changes the effect
size: 2.7337-fold at 6 h and 4.3512-fold at 24 h between umbilical vein and
kidney glomerulus, neither of which is pulmonary.

What that licenses and what it does not. **Direction and membership do
transfer**: 315 genes move the same way in both beds at 6 h, sign agreement is
76.82%, and the four modules are negative in both. So the hypothesis that lung
microvascular endothelium behaves in the same direction is reasonable, and it
is the best inference the package supports. **Magnitude does not transfer**:
if two off-target beds differ by 2.7 to 4.4-fold, no delivered figure can be
used to size an effect in a third. That is why the confirmatory experiment has
to be run in lung endothelium rather than inferred from these numbers, and why
it should be powered on the direction and the gene set rather than on the
effect sizes reported here.

**Timepoint: 6 h.** This is where the response reproduces across beds
(r 0.6216, 76.82% sign agreement, 315 genes). At 24 h it does not (0.3032,
64.27%, 23 genes). Sample at 6 h and treat 24 h as exploratory.

**ST2 is the strongest single piece of human evidence in the package, and it
survives the strictest available bar.** Only three of the 1094 assays clear
Bonferroni at 0.05/1094 = 4.57e-05: HGF at p 3.4e-06, **ST2 at p 1.7e-05**, and
HGF again on a second panel. At analyte level that is two analytes, and one of
them is the pathway's own receptor. ST2's odds ratio is 3.0243 (1.83 to 5.01)
per log unit after adjustment for age, sex and NEWS2, and its interval is
tighter than most: a u95/l95 ratio of 2.74 against a median of 3.92 across the
178 significant rows, 39th tightest of them. This is not a marginal hit read
off the top of a ranking.

**The ranking itself is weaker than the Bonferroni result, and the enrichment
is a property of this signature rather than of the response generally.** 893 of
1094 odds ratios exceed 1 (binomial p 1.6e-104) and 176 of the 178 significant
rows point the same way, so a high rank partly reflects assay precision and an
intersection with the signature establishes nothing on its own. The test must
compare like with like: among analytes whose gene was measured in the RNA data
at all, is the significance rate higher inside the signature? It is — 13 of 38
against 129 of 729, **34.2% against 17.7%, Fisher OR 2.419, p 0.0169**.
Comparing instead against the base rate over all 1063 analytes, including those
mapping to no measured gene, inflates this to 2.15-fold at p 0.0037 and should
not be used.

The result is sensitive to how the signature is drawn. On the tight 315-gene
direction-plus-nominal core it holds. On looser signatures of several hundred to
a thousand genes the same test returns null, because a larger set is less
specific. So a proposal that defines a broader signature and finds no
enrichment has not made an error.



**Markers that could go into patients.** Thirteen analytes are both
prognostic in `AX-1177_serum_proteomics` and inside the 6 h reproducible set. Eight have usable
precision, by which I mean an upper 95% bound under about 11:

| Analyte | Gene | Serum OR (95% CI) | HUVEC 6 h logFC |
|---|---|---|---|
| CCL20 | CCL20 | 1.830 (1.284–2.608) | −9.8418 |
| MCP-3 | CCL7 | 1.719 (1.253–2.356) | −4.9922 |
| IL6 | IL6 | 2.066–2.308 across four panels | −5.9676 |
| B4GALT1 | B4GALT1 | 2.315 (1.399–3.832) | −1.1047 |
| IL1B | IL1B | 2.447 (1.284–4.662) | −3.9716 |
| FSTL3 | FSTL3 | 2.527 (1.294–4.934) | −1.0836 |
| TRIM21 | TRIM21 | 2.950 (1.494–5.825) | −1.1135 |
| TANK | TANK | 3.324 (1.631–6.775) | −1.0242 |

Roles differ and the distinction matters. These eight are candidate
**pharmacodynamic** readouts: each is IL-33-driven, antibody-reversed, and
measurable in serum. **sST2 is a stratification marker, not a pharmacodynamic
one** — see section 6. ICAM1 is the **target-engagement** readout among the
adhesion molecules, at `adj.P.Val` 0.0101 and an implied standard error of
1.744, which is the largest in the 1126-gene set but inside it.

Four of the thirteen need the analyte-to-gene mapping before they appear at
all: `OPG` is TNFRSF11B, `CSF-1` is CSF1, `MCP-3` is CCL7, `IL-18R1` is
IL18R1. Matching Olink assay names to gene symbols literally returns five of
the thirteen and drops those four. On the same point, the delivery is 1094
assays over **1063** distinct analytes: 27 analytes sit on more than one panel,
IL6 on four, SCF and FGF-21 on three. Of 178 significant assay rows, 169 are
distinct analytes.

## 6. Considered and ruled out

| Option | What closed it |
|---|---|
| **Drop the asset.** Nothing here shows the pathway causes disease, and there is no in vivo, potency or exposure data. | Target engagement is established and the blocked programme is characterised and reproducible at 6 h across two beds. That is a validation gap, not a dead target, and the gap is closable with the studies in section 4. |
| **Keep the type 2 framing.** It is where anti-IL-33 is developed and the standard indication set. | IL5, IL13, CCL11, CCL24 and IL25 are not in the table; IL4 is −1.229 and not significant; TSLP, CCL26, GATA3 and IL1RL1 are all non-significant. The package gives no type 2 response to block. |
| **Conclude the response does not reproduce across lines.** Intersecting the two threshold-filtered sets gives 219 of 1126, a Jaccard of 0.1571. | The threshold is invalid on a line whose effects are 2.7337-fold smaller, and it admits 11 sign-discordant genes. On direction plus nominal significance the same data gives 315 and r 0.6216. |
| **Carry both timepoints.** Both Jaccard values, 0.1571 and 0.0356, look low. | The statistics separate: r 0.6216 against 0.3032, sign agreement 76.82% against 64.27%, 315 genes against 23. |
| **Nominate sST2 as the pharmacodynamic readout.** Second of 1094 at OR 3.0243, and the pathway's own receptor. | Two reasons, and the first is specific to sST2 rather than general. Soluble ST2 is the decoy receptor for the drug's own target, so its serum concentration moves with pathway activity and with disease severity at once; a fall after dosing cannot be attributed to target engagement rather than to the patient improving. Every other marker proposed here sits downstream of the receptor and does not carry that confound. Second, nothing in the package resolves its behaviour under antibody: the only receptor measurement is the `IL1RL1` transcript, +1.6020 in `AX-1177_rnaseq_huvec_il33` and −1.6799 in the matching inhibition contrast, with an implied standard error near 8.32 against a median of 0.34, so it is unreadable either way. Prognostic and for patient selection: yes, on the Bonferroni result. Target engagement or pharmacodynamics: not shown, and not resolvable here. |
| **Report SELE and VCAM1 as blocked.** They carry the largest fold changes, −10.9852 and −8.7623, and are the textbook endothelial activation readouts. | Their implied standard errors are 8.779 and 7.019 against a ceiling of 1.7439 across the whole attributable set, so the delivered q-values of 0.4950 and 0.4965 establish nothing in either direction. CXCL1 at `t` −0.0071 and CXCL8, SLC7A2, CCL2 and PTGS2 are in the same condition. Indeterminate, not negative — and not citable as blocked. |
| **Use 1094 proteins and 178 hits.** One row per assay is the obvious count. | 27 analytes appear on more than one panel. The reconciled figures are 1063 and 169. |
| **Quote CSF-1, CTSS or BIRC2 as markers.** All three are significant and carry the largest odds ratios: 90.095, 23.199 and 12.437. | Their intervals are 4.200–1932.572, 2.691–200.019 and 2.409–64.215. Significant, but the magnitude is not estimated at n = 100 and no study could be sized on them. |
| **Use the lung tissue to support the mechanism.** `AX-1177_postmortem_lung` has IL-33 immunohistochemistry in endothelium across 74 blocks from 31 donors. | Different cohort, and `AX-1177_serum_proteomics` carries assay-level summaries with no patient identifiers, so no link can be established or excluded. Its `Tissue RNA` column names 22 samples whose RNA data is not in the delivery. |
