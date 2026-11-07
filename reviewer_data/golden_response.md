# AX-1177 — mechanistic package, committee proposal

**Recommendation: carry AX-1177 forward on the 6 h endothelial signature, which reproduces across two independent endothelial beds; exclude the 24 h window, which does not.**

---

## 1. The response signature we would carry forward

**Criterion, stated as a predicate.** A gene is in the signature if, in the
isotype-controlled HUVEC 6 h contrast, it has `adj.P.Val < 0.05` and
`|logFC| > 1`; **and**, in the corresponding HGMEC 6 h contrast, it has
`adj.P.Val < 0.05` and a `logFC` of the same sign.

**Resulting count: 315 genes.** The HUVEC 6 h attributable set is 1126 genes
(`mmc5.xlsx`, `Compound_47_IL33_vs_IL33_NIP228_HUVEC_6hrs`, count of rows with
`adj.P.Val < 0.05` and `|logFC| > 1`). Of those, 315 meet the HGMEC condition
(`..._HGMEC_6hrs`, same reduction plus sign agreement with the HUVEC `logFC`).

**Why the predicate uses direction and nominal significance rather than a
second fold-change cut.** Applying `|logFC| > 1` in HGMEC as well returns 219
genes, and that number is an artifact of the threshold rather than a measure
of reproducibility, for two independent reasons.

First, effect sizes are systematically smaller in HGMEC. Median `|logFC|`
across the 1126 HUVEC-significant genes is 2.0140 in HUVEC and 0.7367 for the
same genes in HGMEC, a factor of 2.7337 (`mmc5.xlsx`,
`Compound_47_IL33_vs_IL33_NIP228_HUVEC_6hrs` and `..._HGMEC_6hrs`, median of
absolute `logFC` over the HUVEC-significant subset). A cut fixed at 1.0
therefore falls near the centre of the HGMEC distribution and removes genes
for being small, not for being irreproducible.

Second, the two-sided threshold rule admits genes that contradict it. Of the
219 genes it returns, **11 have opposite signs in the two lines** — ABCC11,
AC007336.3, AC091133.2, AL353807.3, ATP2B1-AS1, CALR4P, CNFN, DNAH17-AS1,
GATM, MLXIPL and RF00003. RF00003 is +2.5564 in HUVEC and −2.7988 in HGMEC,
both significant (`mmc5.xlsx`, same two contrasts). A gene regulated in
opposite directions in the two beds is not reproducing in either direction,
so a rule that counts it is measuring something other than agreement.

**Module composition of the 315 genes.** Membership by gene symbol under the
patterns stated here; 272 of 315 are negative and 43 positive.

| Module | Predicate | n | All negative |
|---|---|---|---|
| interferon response | `IFI*`, `IFIT*`, `ISG*`, `MX1/2`, `OAS*`, `IRF*`, `STAT1/2`, `RSAD2`, `DDX58`, `EPSTI1`, `HELZ2`, `IFIH1`, `SAMD9*`, `XAF1` | 16 | yes |
| NF-κB | `NFKB1/2`, `NFKBIA/B/E/Z`, `RELA/B`, `TNFAIP3/6`, `TRAF1` | 10 | yes |
| CSF and cytokine | `CSF1/2/3`, `IL1A`, `IL1B`, `IL6`, `TNF` | 7 | yes |
| chemokine | `CCL*`, `CXCL*`, `CX3CL*` | 9 | yes |

Every member of every named module is negative, so the reproducible part of
the response is suppression of an inflammatory programme, not a mixed effect.
`NFKB2` at −2.8605 and `RELB` at −3.2667 place the suppression on the
non-canonical NF-κB arm as well as the canonical one. `F3` at −5.4739 and `C3`
at −4.6241 extend it to coagulation initiation and complement.

The 43 positive genes belong to no named module. They are SLC14A1, FSTL4,
NDP, GAP43, CNFN, ABCC11, GATM, MLXIPL, ZNF177, SYTL1, C2orf72 and a set of
antisense, lincRNA and pseudogene transcripts. They are not characterised here
and no part of the recommendation rests on them.

**The genes carrying the clinical argument**, with HUVEC 6 h `logFC`: CCL20
−9.8418, IL6 −5.9676, CCL7 −4.9922, TNFRSF11B −4.9854, IL1B −3.9716, IL18R1
−3.4542, CSF1 −3.0173, CTSS −2.3897, TRIM21 −1.1135, BIRC2 −1.1639, B4GALT1
−1.1047, FSTL3 −1.0836, TANK −1.0242. These are the thirteen with a
measured serum counterpart; section 5 takes them forward.

Full membership for all 315 genes is in `signature_membership.tsv`.

## 2. Timepoint

Both windows were assessed on the same predicate and the same contrasts.

| | 6 h | 24 h |
|---|---|---|
| HUVEC attributable set | 1126 | 417 |
| median \|logFC\| HUVEC vs HGMEC | 2.0140 / 0.7367 | 2.2349 / 0.5136 |
| attenuation factor | 2.7337× | 4.3512× |
| Pearson r over the HUVEC set | 0.6216 | 0.3032 |
| sign agreement | 76.82% | 64.27% |
| signature under the stated predicate | **315** | **23** |
| Jaccard of the two thresholded sets | 0.1571 | 0.0356 |

(`mmc5.xlsx`, the four contrasts `Compound_47_IL33_vs_IL33_NIP228_{HUVEC,HGMEC}_{6hrs,24hrs}`;
r and sign agreement computed over the HUVEC-significant subset at each
timepoint, Jaccard over the two independently thresholded sets.)

**Conclusion: the 6 h window carries and the 24 h window does not.** At 6 h,
three quarters of the HUVEC-attributable response moves the same way in a
second endothelial bed and the two effect vectors correlate at 0.62. At 24 h
sign agreement falls to 64.27%, close to what direction alone would give, the
correlation halves, and the signature collapses from 315 genes to 23.

This is not a tissue-identity argument. The same two cell lines, from the same
single fitted model, agree at 6 h and disagree at 24 h. A difference
attributable to vascular bed would apply at both timepoints.

## 3. What the model data supports

**The effect is ligand-dependent.** Each endothelial line has an
antibody-alone arm: `Compound_47_vs_NIP228_{line}_{tp}`, antibody against
isotype with no IL-33. These return 31 and 36 genes in HUVEC and 62 and 67 in
HGMEC at 6 h and 24 h. More importantly they are **disjoint from the
attributable sets**: 6 of 1126 in HUVEC 6 h and 1 of 487 in HGMEC 6 h.
Dropping every gene significant in either standalone arm leaves 1114 of the
1126 and moves the attenuation from 2.7337× to 2.7341× (median `|logFC|`
2.0154 in HUVEC against 0.7371 in HGMEC, `mmc5.xlsx`, the two 6 h
isotype-controlled contrasts restricted to that subset). The attributable
response is therefore not a ligand-independent antibody effect.

The epithelial lines give the scale of a null result. A549 and MCF7 carry
antibody-against-control contrasts against three comparators and return 13 to
40 genes across all six arms (`mmc5.xlsx`, the `A549` and `MCF7` contrasts).
HUVEC's standalone counts sit inside that range. HGMEC's sit above it, so the
floor comparison alone does not establish ligand-dependence for that line;
disjointness does.

**What the second endothelial line establishes.** That the 6 h response is not
specific to umbilical vein endothelium. 487 genes are antibody-reversed in
HGMEC at 6 h under the package criterion, so the microvascular bed is
IL-33-responsive and the antibody acts on it.

**What it does not establish.** HGMEC has no unstimulated vehicle arm —
`mmc5.xlsx` carries no `IL33_vs_Vehicle` or equivalent for that line, and
`mmc4.xlsx` provides the stimulation contrast for HUVEC only. The magnitude of
the IL-33-driven response in HGMEC is therefore never measured directly, only
the part of it the antibody reverses. The 2.734× attenuation is measured on
antibody effect, and whether it reflects a smaller underlying IL-33 response
or a smaller antibody effect on an equal response cannot be separated in this
package.

**Cross-model behaviour does not extend beyond endothelium.** The epithelial
lines were run without IL-33 in any arm, so they bound the null and say
nothing about epithelial pharmacology.

**One structural caveat on all of it.** A single linear model was fitted
across the whole dataset, with `df.total` of 85.128 identical in all 24
contrasts and `AveExpr` per-gene identical across all 24 for all 26,210 genes
(`mmc5.xlsx`, `df.total` recovered by inverting `t` against `P.Value`).
Variance is therefore moderated across cell lines that differ in expression
range, which tends to compress between-line differences rather than inflate
them. This is conservative with respect to our conclusion.

## 4. Circulating markers worth taking into the clinic

The serum dataset reports **1094 assays over 1063 distinct analytes**. 27
analytes appear on more than one panel, IL6 on four and SCF and FGF-21 on
three. Of 178 assay rows with `adj.p.value < 0.05`, **169 are distinct
analytes**. Counting assays rather than analytes overstates both figures.

**Reconciliation rule** (`mmc2.xlsx`, `panel` and `assay` columns): merge two
assay names that differ only by a trailing panel suffix. Applying it to every
trailing all-capital token rather than to a fixed list gives 28 groups over 60
assays; one of those, `TR-AP` with `TR`, is spurious because TR-AP is
tartrate-resistant acid phosphatase rather than `TR` on a panel named AP.
Excluding it leaves **27 groups over 58 assays, 31 duplicate rows, 1063
analytes**. A fixed suffix list omits at least `NEUI` and so misses
`GDNF-INFI` with `GDNF-NEUI`, which is how a count of 1064 arises.

**Shortlist: 13 analytes** that are both prognostic in serum and inside the
6 h signature. Odds ratios are per log unit, adjusted for age, sex and NEWS2
(`mmc2.xlsx`, `OR`, `l95`, `u95`, `adj.p.value`); `logFC` is the HUVEC 6 h
isotype-controlled contrast in `mmc5.xlsx`.

| Analyte | Gene | Serum OR (95% CI) | Panel | HUVEC 6 h logFC |
|---|---|---|---|---|
| CCL20 | CCL20 | 1.830 (1.284–2.608) | Inflammation | −9.8418 |
| MCP-3 | CCL7 | 1.719 (1.253–2.356) | Inflammation | −4.9922 |
| IL6 | IL6 | 2.066–2.308 across four panels | Infl., Onc II, CVD II, Imm Resp | −5.9676 |
| B4GALT1 | B4GALT1 | 2.315 (1.399–3.832) | Development | −1.1047 |
| IL1B | IL1B | 2.447 (1.284–4.662) | Oncology III | −3.9716 |
| FSTL3 | FSTL3 | 2.527 (1.294–4.934) | Development | −1.0836 |
| TRIM21 | TRIM21 | 2.950 (1.494–5.825) | Immune Response | −1.1135 |
| TANK | TANK | 3.324 (1.631–6.775) | Immune Response | −1.0242 |
| OPG | TNFRSF11B | 4.399 (1.844–10.499) / 6.767 (2.467–18.561) | CVD III / Inflammation | −4.9854 |
| IL-18R1 | IL18R1 | 6.071 (2.229–16.531) | Inflammation | −3.4542 |
| BIRC2 | BIRC2 | 12.437 (2.409–64.215) | Immune Response | −1.1639 |
| CTSS | CTSS | 23.199 (2.691–200.019) | Neurology | −2.3897 |
| CSF-1 | CSF1 | 90.095 (4.200–1932.572) | Inflammation | −3.0173 |

**Take the first eight forward. The last three are not usable as effect-size
estimates**, on a stated rule: an upper 95% bound above 20 means the magnitude
is not estimated at this sample size. CSF-1's interval spans 4.200 to
1932.572, CTSS's 2.691 to 200.019 and BIRC2's 2.409 to 64.215. All three are
significant and the direction is informative, but no trial could be sized on
them and quoting the point estimate would misrepresent the precision. They
stay on the list as qualitative confirmation, not as quantitative readouts.
The eight with upper bounds below 11 are the ones to measure.

**Multi-panel analytes need a declared choice.** IL6 is assayed on four
panels and returns four odds ratios between 2.066 and 2.308; OPG on two, 4.399
and 6.767. Reconciling assays to analytes therefore does not produce one value
per analyte. Here the range is reported and the panel named; a single figure
would require a rule for choosing between panels that the delivered data does
not supply.

**Join rule.** Olink reports protein assay names, not gene symbols. Four of
the thirteen require reconciliation: `OPG` to TNFRSF11B, `CSF-1` to CSF1,
`MCP-3` to CCL7, `IL-18R1` to IL18R1. Matching on the raw assay string returns
9 of the 13 and silently drops those four. The reconciliation is closed over
this dataset: every one of the 169 significant analyte names maps to a symbol.

**Excluded, with reasons.**

- **Soluble ST2.** `ST2` is the second-ranked analyte of 1094 at an odds ratio
  of 3.0243 (`mmc2.xlsx`, row 2 by `adj.p.value`), and it is the receptor for
  the pathway's own ligand. It has **no pharmacodynamic response**: `IL1RL1`
  is not significant in any of the 24 contrasts in `mmc5.xlsx`, minimum
  `adj.P.Val` 0.9614, and it is absent from the signature. It is a prognostic
  marker for selecting patients, not a readout for confirming target
  engagement, and using it as the latter would report drug effect where none
  is measurable.
- **The adhesion molecules.** SELE, VCAM1 and CXCL8 carry three of the ten
  largest fold changes in the HUVEC 6 h contrast at −10.9852, −8.7623 and
  −8.4467, and they are the textbook endothelial activation readouts. None is
  attributable: `adj.P.Val` 0.4950, 0.4965 and 0.1772 respectively. ICAM1 at
  −5.9116 and `adj.P.Val` 0.0101 is attributable and is the adhesion readout
  the data supports.

## 5. What this package does not contain

No affinity, potency or exposure data for AX-1177 appears in the delivered
files. The recommendation rests on direction and reproducibility of
transcriptional response at a single concentration in each arm, not on
pharmacological parameters, and a committee decision on dose or schedule
cannot be supported from this package.
