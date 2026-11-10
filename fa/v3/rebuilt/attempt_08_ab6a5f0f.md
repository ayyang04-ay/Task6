# AX-1177 (anti-IL-33): portfolio audit recommendation, evidence review and forward plan

**Scope.** This review uses only the AX-1177 data package: the methods annex, mmc2 (serum proteomics), mmc3 (post-mortem lung), and mmc4/mmc5 (endothelial and epithelial transcriptomics). Every number below was recomputed from those files. Nothing from outside the package is used as evidence. Competitive landscape, IP, CMC, affinity/potency and toxicology are not in the package, so they are out of scope. Supporting tables T1–T8 are in `tables/` and Figures 1–5 are in `figures/`.

---

## 1. Recommendation

**Keep AX-1177, but do not present it as a "viral LRTD" asset and do not fund it open-ended.**

- **Re-scope it.** The new positioning is a host-directed blocker of IL-33-driven endothelial activation (both inflammatory and pro-coagulant) in hospitalised severe pneumonia.
- **Enrich the population.** Select patients by serum sST2.
- **Start with hospitalised viral pneumonia.** It is the only patient population our data cover.
- **Fund a gated package of about 12 months with kill criteria written in advance** (Section 8).
- **Run the decision-critical experiment first.** Do the enrolment sera from our own 100-patient cohort contain endothelial-activating activity that AX-1177 reverses? We already hold this material. If the human-relevance gate (patient serum plus endogenous-alarmin assays) or the in vivo gate fails, drop the asset.

**Why keep it: three things our data do show**

1. **The drug works on its target in human endothelium, completely and cleanly.**
   - **What IL-33 does.** Reduced IL-33 (30 ng/mL) turns on a large NF-κB programme in HUVEC: 4,031 genes change at 6 h (q<0.05) and 1,836 at 24 h. The top genes are:
     - GM-CSF (CSF2) +10.3 log2
     - CXCL6 +9.4
     - CCL20 +9.2
     - G-CSF (CSF3) +8.3
     - TNF +7.9
     - IL-6 +5.8
     - tissue factor (F3) +5.6
   - **What AX-1177 does.** It was added at the same time as IL-33 (no pre-incubation).
     - At 6 h it removes a median 100% of the response across the 329 robustly induced genes (IQR 93–104%).
     - At 24 h it removes 94%.
   - **Controls.** The isotype control has no effect (+0.5% of the IL-33 response). The same programme is reversed in glomerular microvascular endothelium (HGMEC).
   - **Antibody alone.** AX-1177 without IL-33 produces no reproducible transcriptional change in any of the four cell types.
2. **The pathway it blocks is linked to outcome in patients.**
   - **The cohort.** Serum was taken at enrolment from 100 hospitalised COVID-19 patients. The outcome was ICU, invasive ventilation or death within 30 days (44 events). Models were adjusted for age, sex and NEWS2.
   - **sST2.** Soluble ST2, the IL-33 decoy receptor, has OR 3.02 per log unit (1.83–5.01), p=1.7×10⁻⁵, q=0.0075. It ranks 2nd of 1,094 assays.
   - **IL-33-inducible endothelial products.** Several proteins that IL-33 induces in endothelium and AX-1177 reverses are also associated with outcome, each after adjustment for age, sex and NEWS2: IL-6, OPG, sIL-18R1, CCL20, CCL7, CSF-1, IL-1β and tissue factor.
3. **The target is present in diseased lung, and its pattern fits release during acute injury regardless of pathogen.**
   - Endothelial IL-33 is lower in donors whose pathology shows acute pneumonia or lung injury (median 4.88 vs 5.50, p=0.028).
   - It falls as neutrophil infiltration rises (ρ=−0.43, p=0.016).
   - Nothing differs between COVID-positive and COVID-negative pneumonia (all p≥0.15).

**Why not "viral LRTD" as currently framed: what our data do not show**

- **No causal evidence.** There are no in vivo data and no infection model.
- **No potency or differentiation data.** The package tests one supra-saturating dose (about 41-fold molar excess) and never tests oxidised IL-33.
- **No virus-specific signal.** Nothing in the data separates viral from other pneumonia.
- **The IL-33 programme is not over-represented among severity proteins.** 22% of IL-33-signature proteins are severity-associated versus 19% of all other proteins (p=0.52). sST2 itself is not IL-33-specific.
- **A possible liability in infection.** AX-1177 also removes an IL-33-induced interferon-like, antiviral-sensing programme in endothelium (IRF1, IFIH1/MDA5, DDX58/RIG-I, CXCL10, MX1).

**Evidence scorecard**

| Claim | Strength in our data | Basis |
|---|---|---|
| AX-1177 neutralises reduced-IL-33 signalling in human endothelium | **Strong (in vitro)** | 2 endothelial beds, 2 timepoints, isotype-controlled; ~100% inhibition of 329 genes |
| AX-1177 has no intrinsic transcriptional activity | **Moderate–strong** | 4 cell types × 2 timepoints; no reproducible hits |
| The IL-33/ST2 axis is linked to severity in hospitalised viral pneumonia | **Moderate (associative, one cohort)** | sST2 OR 3.0, q=0.0075, NEWS2-adjusted |
| Specific IL-33-inducible endothelial proteins track severity | **Moderate for IL-6, CCL20, OPG, sIL-18R1, TF**; not enriched overall | 8–12 markers; enrichment p=0.52 |
| IL-33 is released or depleted in acute lung injury | **Weak** | Single reader, ceiling effect, p=0.028 uncorrected |
| Virus-specific role | **Absent** | No COVID vs non-COVID difference |
| In vivo efficacy / causality | **Absent** | Not in package |
| Potency and differentiation (incl. oxidised IL-33) | **Absent** | Single dose; IL-33ox not tested |
| Safety in active infection | **Unknown**; theoretical liability | IL-33-induced endothelial ISG module is removed |

**What must be fixed or disclosed before numbers go to the committee (Section 5)**

- **Undelivered serum assays.** The serum q-values were computed over 1,194 tests, but only 1,094 assays were delivered.
  - The 100 missing assays include, according to the vendor's panel content, **IL-33 itself**.
  - At least two of the missing assays were among the strongest associations in the analysis (p≈0.0002–0.0011).
- **Unusable statistics for key canonical genes.** The transcriptomic statistics for E-selectin, VCAM-1, IL-8, MCP-1, PTX3 and IL1RL1 cannot be used. Their standard errors are inflated 10- to more than 3,000-fold in the single pooled model.
- **Undocumented library exclusion.** The model's degrees of freedom imply that one library was excluded, which the annex does not record.
- **Post-mortem scoring and labels.** Post-mortem IL-33 scores exceed the documented 0–5 scale, and 9 of 31 donors have category labels that contradict their pathology reports.

---

## 2. What is in the package

| Data | Content (verified) | Main limitation |
|---|---|---|
| **In vitro RNA-seq** (mmc4, mmc5) | 26 limma contrasts × 26,210 genes, documented as one voom model over 114 libraries (38 arm × time groups, n=3). HUVEC: vehicle, isotype, AX-1177, IL-33red, IL-33red+isotype, IL-33red+AX-1177. HGMEC: same arms but **no vehicle**. A549 and MCF7: PBS, DMSO, isotype, AX-1177, **no IL-33**. | Single-donor endothelial cells. One concentration each of IL-33 and antibody. Reduced IL-33 only. Counts and model object are not delivered. mmc5's two sheets ("6h", "24h") are identical copies, each holding all 24 contrasts. |
| **Serum proteomics** (mmc2) | 1,094 Olink assays = 1,063 unique proteins across 13 panels. Per-assay logistic regression on ICU/IMV/death ≤30 d, adjusted for age, sex and NEWS2. | Summary statistics only. Single centre, single timepoint, pre-vaccination, COVID-19 only. 100 tested assays are undelivered. |
| **Post-mortem lung IHC** (mmc3) | 74 blocks from 31 donors (16 COVID+ pneumonia, 10 COVID− pneumonia, 5 COVID− non-pneumonia). IL-33 in basal epithelium, endothelium and VSMC; eosinophil, neutrophil and mast-cell markers. | Single reader. Scale anomalies. Label/pathology conflicts. Elderly donors with heavy comorbidity; no healthy controls. |

---

## 3. The case for keeping: evidence with numbers

### 3.1 Pharmacology: complete, specific neutralisation in two human endothelial beds (Fig 1, Fig 2, T2)

**The IL-33 response in HUVEC**

| | 6 h | 24 h |
|---|---|---|
| Genes changed (q<0.05) | 4,031 | 1,836 |
| Changed >2-fold (up / down) | 1,068 (645 / 423) | 512 (314 / 198) |
| Hallmark TNFα-via-NF-κB NES | 3.12 | 3.10 |
| Hallmark IFN-γ response NES | 2.79 | 3.06 |
| Hallmark IL6-JAK-STAT3 NES | 2.58 | 2.66 |
| Hallmark coagulation NES | 1.57 | 1.44 |

The response falls into three functional modules:

- **(i) Leukocyte recruitment and myelopoiesis:** CSF2 +10.3, CXCL6 +9.4, CCL20 +9.2, CX3CL1 +8.4, CSF3 +8.3, CXCL3 +8.3, CXCL2 +6.8, IL6 +5.8 log2.
- **(ii) A pro-coagulant / anti-fibrinolytic switch:**
  - F3 (tissue factor) +5.6 (q=2×10⁻²⁶)
  - SERPINB2 +2.9
  - SERPINE1 (PAI-1) +1.7
  - THBD (thrombomodulin) −1.0 (q=2×10⁻¹⁰)
- **(iii) An interferon-like, antiviral-sensing module:** IRF1 +2.6, IFIH1 +2.4, DDX58 +1.6, CXCL10 +6.9, MX1 +1.9.

**Neutralisation by AX-1177**

The conditions were 10 µg/mL AX-1177 (about 68 nM, a 41-fold molar excess over 1.66 nM IL-33), added at the same time as IL-33 without pre-incubation. Inhibition is measured against the isotype + IL-33 arm.

| | 6 h | 24 h |
|---|---|---|
| Robust IL-33-induced genes (q<0.05, >2-fold, t>5) | 329 | 102 |
| Median inhibition | 100% (IQR 93–104%) | 94% (IQR 77–104%) |
| Genes inhibited ≥80% | 90% | 72% |
| Genes significantly reversed | 96% | 87% |
| Hallmark NF-κB NES for the reversal | −3.10 | −3.02 |
| Isotype effect in presence of IL-33 | +0.5% of the IL-33 effect (IQR −2 to +3%) | −10% (consistent with noise/regression to the mean) |

**Second vascular bed (HGMEC)**

- At 6 h, AX-1177 significantly reduces 69% of the 329 HUVEC-defined IL-33 genes in IL-33-treated HGMEC. The median magnitude is about half that in HUVEC, and the NF-κB NES is −3.70.
- Examples: CSF2 −7.1, CSF3 −6.5, CCL20 −5.6, F3 −3.3, IL6 −2.9.
- By 24 h the HGMEC reversal has largely disappeared (median −0.1 log2). Because HGMEC has no vehicle arm, the size of the HGMEC IL-33 response itself cannot be measured.

**No intrinsic activity of the antibody** (T7)

- AX-1177 vs isotype gives 21–73 "hits" per contrast in HUVEC, HGMEC, A549 and MCF7. These are not real effects:
  - 56–91% are genes with negative pooled AveExpr (low-count noise).
  - Up to 42% are variance artefacts with |log2FC|<0.3.
  - After requiring |log2FC|>1, sane SE and AveExpr>0, only 0–9 remain per contrast.
  - Only 3 of 325 hit genes recur in more than one of the 8 contrasts, and those with trivial or opposite changes.
  - Between 6 h and 24 h within a cell line, the log2FCs correlate at −0.06 to 0.18.
- Hallmark shifts in proliferation and metabolism gene sets do appear, but their direction flips between cell lines and timepoints. For example, MYC targets have NES −2.96 in HUVEC 24 h, +2.41 in HGMEC 6 h, −3.14 in A549 6 h and +2.67 in MCF7 24 h. That pattern is well-to-well variation, not pharmacology.

**Specificity and reagent quality checks contained in the design**

- **The response is IL-33-mediated.** Near-complete reversal by an anti-IL-33 antibody, with an inert isotype control, excludes a contaminant such as endotoxin in the IL-33 preparation. That contaminant would not be neutralised by AX-1177.
- **The AX-1177 lot shows no agonist or endotoxin-like activity.** The LPS-sensitive NF-κB genes in HUVEC do not move with antibody alone: CSF2 −0.4, CXCL6 −0.8, CCL20 0.0, TNFAIP3 0.0 log2.

### 3.2 Human relevance: the IL-33-axis marker is among the strongest predictors of severe outcome (Fig 3, T3)

- **sST2.** OR 3.02 per log unit (1.83–5.01), p=1.7×10⁻⁵, q=0.0075. It ranks 2nd of 1,094 assays, and 1st or 2nd of 1,063 unique proteins. The association holds independently of NEWS2, the clinical severity score at enrolment. Whether sST2 also improves discrimination needs the individual-level data.
- **IL-33-inducible, AX-1177-reversible endothelial products that are also associated with outcome:**

  | Protein | Serum OR per log unit | Serum p / q | HUVEC 6 h induction (log2) |
  |---|---|---|---|
  | IL-6 (4 assays on 4 panels) | 2.07–2.31 | all p<0.0005 | +5.8 (q=2×10⁻¹³) |
  | OPG (2 assays) | 6.8 and 4.4 | p=0.0002 and 0.0008 | +4.8 |
  | sIL-18R1 | 6.1 | p=0.0004 | +3.6 |
  | CCL20 | 1.83 | p=0.0008 | +9.2 |
  | CCL7 | 1.72 | p=0.0008 | +2.2 |
  | CSF-1 | 90 (CI 4–1,933; scale not comparable) | p=0.004, q=0.037 | +2.9 |
  | IL-1β | 2.45 | p=0.0065, q=0.046 | +3.6 |
  | CTSS | 23 (scale not comparable) | p=0.004, q=0.037 | +2.1 |
  | Tissue factor | 3.0 | p=0.0085, q=0.051 | +5.6 |

- **Four more markers with large in vitro effects whose in vitro statistics are unusable:**

  | Protein | Serum association | HUVEC induction (log2) |
  |---|---|---|
  | PTX3 | OR 11.6, p=9×10⁻⁵ | +2.2 |
  | IL-8 | p=0.0017 | +8.2 |
  | MCP-1 | p=0.008 | +4.2 |
  | E-selectin | p=0.02 | +11.2 |

- **Endothelial injury and coagulation markers also track outcome:** vWF (p=0.008), ANGPT2 (p=0.009), uPAR (p=0.002), VEGF-A (p=0.002) and PAI-1 (p=0.048).
- **Technical replication.** Proteins measured on several panels give concordant ORs (e.g., IL-6 2.07–2.31; HGF 4.99 and 4.84; OPG 6.8 and 4.4; TNFRSF10A 5.4 and 4.6).

### 3.3 Tissue: the target is present in diseased lung, with a release-consistent pattern that is not pathogen-specific (Fig 4, T5)

This analysis is done at donor level; the block level would be pseudo-replicated.

- **IL-33 is abundant.**
  - Endothelium: median score ≥4.8 in every group.
  - Basal epithelium: median 4.25–4.88.
  - VSMC: median 2.4–3.5.
- **Lower endothelial IL-33 in acute injury.** When donors are grouped by whether their own pathology report documents acute pneumonia or lung injury:
  - endothelial IL-33 is lower (4.88 vs 5.50, p=0.028);
  - it correlates inversely with neutrophil elastase (ρ=−0.43, p=0.016).

  This is consistent with alarmin release or depletion during acute injury. These are uncorrected, exploratory statistics on a ceiling-limited, single-reader scale.
- **No difference by pathogen.** COVID+ and COVID− pneumonia do not differ in IL-33 in any compartment or in granulocytes (all p≥0.15).
  - Granulocytes (EDN, MBP, IL-5Rα, neutrophil elastase) are higher in pneumonia than non-pneumonia (p=0.004–0.009) whatever the virus status.
- **Thromboemboli** appear in the pathology text of 4/16 COVID+ donors vs 0/15 COVID− donors (p=0.10). This fits, but does not prove, a thrombo-inflammatory component.

---

## 4. Limits: what our data do not show

| # | Gap | Evidence |
|---|---|---|
| 1 | **No causal evidence** | No in vivo experiment, no infection model, and no patient-derived material has been tested with AX-1177. |
| 2 | **The IL-33 programme is a minority of the severity signal** | 15/68 IL-33-signature proteins (22%) are severity-associated vs 156/843 (19%) of all others (Fisher p=0.52). The rank correlation is weak (ρ=0.14). Strongly IL-33-induced, fully reversed products do not predict outcome: G-CSF p=0.23, CXCL5 0.52, CXCL6 0.95, CXCL10 0.25, TNFRSF9 0.68, VCAM-1 0.43, ICAM-1 0.11. Most top severity proteins are not IL-33-inducible in endothelium (HGF, HDGF, SEMA4C, CLEC5A, OSM, IL-1R2). 176/178 significant assays have OR>1, a global injury-burden signal. |
| 3 | **sST2 is not IL-33-specific** | It is a soluble decoy receptor, not a readout of IL-33 activity. In our data it sits inside a broad injury-burden signal (176/178 significant assays have OR>1), and its induction by IL-33 in endothelium is unverified (IL1RL1 +1.6 log2 with an inflated SE). It can select patients; it cannot prove IL-33 activity. |
| 4 | **Nothing virus-specific** | Tissue shows no COVID vs non-COVID difference. The in vitro work contains no virus. The serum cohort is COVID-only, so generality across pathogens is untested either way. |
| 5 | **Possible liability in active viral infection** | AX-1177 removes the IL-33-induced endothelial ISG-like module (Fig 2). Whether that helps or harms antiviral control is unknown. |
| 6 | **No potency, no differentiation** | A single supra-saturating dose cannot give an IC50. The annex claims binding to oxidised IL-33, but the package contains no oxidised-IL-33 binding or function data, so that differentiation claim is currently unsupported. |
| 7 | **Model relevance** | Umbilical-vein and glomerular endothelium from single donors; no lung microvascular endothelium. The epithelial lines (A549 tumour, MCF7 breast) never received IL-33, so the package says nothing about epithelial IL-33 biology. |
| 8 | **Clinical cohort** | Single centre, pre-vaccination, COVID-19 only, one timepoint with no time-from-onset. ICU admission is capacity-dependent. Only summary statistics are available, so discrimination gain over NEWS2 (AUC, NRI) cannot be computed. |

---

## 5. Data integrity and provenance findings (T1, Fig 5)

These are internal-consistency findings within the delivered files. They do not overturn the main conclusions, but several change what can be claimed.

**Transcriptomics**

- **T-1. Implied standard errors.** Because one model was fitted, each gene's SE (|logFC/t|) should be stable across contrasts. For most genes it is (median 0.34 log2 units).
  - 130 genes exceed 2 log2 units. They include SELE (9.0), VCAM1 (7.1), CCL2 (6.3), CXCL8 (4.1), PTX3 (10.9), IL1RL1 (8.3) and CXCL1 (1,166). They also include cell-identity and housekeeping genes (CD93 16,536; CDH5 926; VWF 144; GAPDH 9.5).
  - SEs this large are implausible for log-CPM data from a correctly specified voom/limma fit; the largest are impossible.
  - The consequence: E-selectin rises +11.2 log2 with IL-33 and falls −11.0 with AX-1177, yet has q=0.50. These genes are **unverified, not negative**.
  - The opposite artefact also occurs (AKR1C2 log2FC 0.11 with t=169). It creates spurious "antibody-alone" hits.
- **T-2. Degrees of freedom.** Most genes have df.total=85.13, but about 330 sit on a floor of 75.05. That implies a residual df ≤75, not the 76 expected for 114 libraries and 38 groups. A library was dropped, or a covariate added, without documentation.
- **T-3. Cross-cell-type signal.** Genes not expressed by a cell type still move between its arms:
  - Endothelial genes in epithelial contrasts: CDH5 +2.15 (A549), TIE1 +2.13 (MCF7).
  - Epithelial/MCF7 genes in endothelial contrasts: GREB1 +2.1, GATA3 +1.0, KRT19 +1.0.

  This is consistent with cross-library contamination, index hopping (all 114 libraries ran on one flow cell) or a mislabelled library. Together with the single pooled variance prior across four unrelated cell types, it explains T-1.
- **T-4. AveExpr and design coverage.**
  - AveExpr is pooled over all 114 libraries, so it cannot indicate expression in a single cell line (CSF2 has AveExpr −3.2 despite +10.3 log2 induction).
  - The HGMEC IL-33 response is not measurable (no vehicle arm, no contrast delivered).

**Serum proteomics**

- **S-1. Undelivered assays.** The delivered adj.p values equal Benjamini–Hochberg over **1,194** tests: adj × rank / p equals 1,194.000 exactly at several ranks. Only **1,094** assays were delivered, which contradicts the annex ("across all assays in the delivery").
  - Reconstruction from the delivered q-values:
    - One undelivered assay sat at p≈0.0002–0.0003 (overall rank about 19–21, q≈0.015).
    - A second sat at p≈0.0007–0.0011 (q≈0.02).
    - About 5 had p<0.01 and about 16 had p<0.05.
  - Fifteen Inflammation-panel assays are absent. According to the vendor's published panel content (to be confirmed against the run manifest), these include **IL-33**, IL-1α, IL-4, IL-5, IL-13 and TSLP.
  - **The most relevant analyte may have been tested and not delivered.**
- **S-2. Duplicates across panels.** The 1,094 assays are 1,063 unique proteins (27 proteins appear on 2–4 panels). The 178 significant assays are 169 unique proteins.
- **S-3. OR scale.** ORs are "per log unit" of each assay, and NPX is already log2, so the transform is ambiguous. ORs are therefore not comparable across assays (CSF-1 has OR 90, CI 4–1,933).
- **S-4. Undocumented columns.** The two `composite_endpoint_0/1` columns are not described. Their values are multiples of 1/56 and 1/44, which implies 44 events out of 100 patients.

**Post-mortem IHC**

- **P-1. Scale.** IL-33 scores use undocumented quarter-points.
  - 55 of 219 values are 5.5, above the documented 0–5 maximum.
  - Endothelial IL-33 sits at that ceiling in 39 of 74 blocks.
  - The numeric granulocyte columns equal the ordinal grade +0.5.
- **P-2. Pseudo-replication.** There are 1–8 blocks per donor, and three COVID+ donors contribute 24 of the 49 COVID+ blocks.
- **P-3. Labels contradict pathology.**
  - 6 donors labelled "pneumonia" have no acute pneumonia in their pathology report.
  - 3 donors labelled "non-pneumonia" have acute or organising pneumonia, pneumonitis, or pulmonary coccidioidomycosis.
  - One donor lacks SARS-CoV-2 status.
  - The reader was single and blinding is not stated.

---

## 6. Indication: what our data point at, and what I considered and ruled out

**The data point at a host-response indication, not a pathogen.** That indication is IL-33-driven endothelial activation (leukocyte recruitment plus a pro-coagulant switch) in **hospitalised severe pneumonia**, with the aim of preventing progression to ICU, invasive ventilation or death (the endpoint already used in our cohort), and with **sST2-high** patients as the enriched population.

- Start in viral pneumonia, because that is where our patient data are.
- Keep the mechanism and biomarker case pathogen-agnostic, because the tissue data show the same IL-33 and granulocyte picture in non-COVID pneumonia.
- This is a re-scoping, not a move to a new organ. Nothing in the package points convincingly to a different disease.

| Option considered | What our data say | Verdict |
|---|---|---|
| **Viral LRTD, as currently framed** (pathogen-defined) | Serum association exists in COVID-19, but the tissue shows no virus specificity. There is no infection model. AX-1177 removes an endothelial antiviral-sensing module. | **Not as framed.** Redefine by host response. |
| **Severe pneumonia with endothelial activation, pathogen-agnostic, sST2-enriched** | In vitro endothelial programme blocked ~100%. sST2 plus IL-6, CCL20, OPG, sIL-18R1 and tissue factor track outcome. Endothelial IL-33 is lower in acute injury and falls with neutrophil influx in COVID+ and COVID− lungs. | **Recommended** (gated). |
| Pneumonia-associated thrombo-inflammation as a standalone indication | F3 +5.6, PAI-1 up and thrombomodulin down, all reversed. Serum TF, PAI-1, uPAR and vWF associated. Thromboemboli 4/16 vs 0/15 (p=0.10). | Keep as a **PD/biomarker axis inside** the recommended indication; too thin to stand alone. |
| Kidney (glomerular endothelium: AKI, DKD, glomerulonephritis) | HGMEC responds (about half the HUVEC magnitude at 6 h, largely gone by 24 h). No kidney patient data. Serum KIM-1 only nominal (p=0.03). | **Not supported.** Hypothesis only. |
| COPD / asthma / type-2 airway disease | No airway-epithelial IL-33 experiment (A549 and MCF7 unstimulated). Basal-cell IL-33 does not differ with COPD/emphysema (p=0.14). No type-2 serum signal (IL-5 OR 1.00, CCL11 n.s.). | **Not supported by our data.** This would be a new bet needing new data. |
| Eosinophil-driven disease | Eosinophil markers rise in pneumonia generally and do not correlate with IL-33 (ρ −0.2 to +0.1). | **Ruled out** on our data. |
| Oncology (A549, MCF7 in the package) | The lines were never exposed to IL-33, and the antibody alone does nothing. | **Ruled out.** No relevant data. |

**Analytical claims I checked and ruled out** (do not put these in front of the committee)

- *"AX-1177 has off-target transcriptional effects."* The hits are non-reproducible noise and variance artefacts.
- *"E-selectin, VCAM-1 and IL-8 are not induced by IL-33."* The q-values for these genes are uninformative, not negative.
- *"178 proteins predict severity."* It is 169 unique proteins, and 100 tested assays are missing.
- *"IL-33-induced proteins dominate the severity proteome."* Fisher p=0.52.
- *"IL-33 is increased in COVID-19 lungs."* No difference; if anything it is lower in acute injury.
- *"COVID-specific eosinophilia."* The same pattern is seen in COVID− pneumonia.
- *"AX-1177 is differentiated by binding oxidised IL-33."* Not tested in the package.
- *Using OR magnitudes to rank biomarkers.* The scales are not comparable.
- *Block-level post-mortem statistics.* They are pseudo-replicated.
- *Reading the 24 h proliferation gene-set "reversal" as IL-33-specific.* The same shifts appear with antibody alone.

---

## 7. Biomarkers, roles and sampling timepoint (T4)

| Marker | Matrix | Role | Into patients? | Basis in our data |
|---|---|---|---|---|
| **sST2** | serum | **Enrichment / stratification (prognostic)** | **Yes**, at enrolment | OR 3.02, q=0.0075, NEWS2-adjusted. Not IL-33-specific, so it selects patients rather than proving mechanism. |
| **IL-6, CCL20, sIL-18R1, OPG** | serum | **Downstream PD** (and prognostic covariates) | **Yes** | Each is IL-33-induced in endothelium (+3.6 to +9.2 log2), reversed by AX-1177 in HUVEC and HGMEC, and associated with outcome (p<0.001). |
| **Tissue factor (F3)** | **plasma** (serum TF is distorted by clotting) | PD for the thrombo-inflammatory arm | **Yes** | +5.6 log2 induced and fully reversed. Serum OR 3.0, p=0.0085. |
| CCL7, CSF-1, IL-1β, CTSS | serum | Exploratory PD | Exploratory | Induced and reversed; q<0.05 in serum. |
| PTX3, IL-8, MCP-1, E-selectin | serum | PD candidates **contingent on re-analysis** | Not yet | Strong serum associations and very large in vitro effects, but in vitro statistics unusable (T-1). |
| G-CSF, CXCL5, CXCL6, CXCL10, CX3CL1, TNFRSF9, VCAM-1, ICAM-1 | serum | Exploratory PD only | Not for selection | Strongly induced and reversed in vitro, but **not** associated with outcome. |
| **GM-CSF, CCL20, CXCL6, G-CSF in culture supernatant** | endothelial culture | **Potency (IC50) and ex vivo target-engagement bioassay** (patient serum ± AX-1177 on endothelial cells) | Indirectly (assay run on patient serum) | Largest and cleanest responses (CSF2 +10.3, reversal t=−31). Zero antibody-alone background. |
| Total / free IL-33 | serum | Target engagement | Pending | The assay was run (counted in BH) but **not delivered**. A drug-tolerant assay is needed. |
| NF-κB transcripts (TNFAIP3, NFKBIA, TRAF1, BIRC3) | cells | Mechanism / potency readouts only | **No** | Intracellular mRNA. |
| IL-33 IHC | tissue | Translational pathology only | **No** | Post-mortem; scale issues. |
| Viral load / clearance, ISG markers | respiratory samples / blood | **Safety** in viral indications | **Yes** | AX-1177 removes the IL-33-induced endothelial ISG module. |

**Sampling timepoint**

- **Experimental and ex vivo PD readouts: 6 h after IL-33 exposure.**
  - 6 h gives 329 robustly induced genes against 102 at 24 h.
  - The top 50 genes lose about half their log2FC by 24 h (median 5.6 → 2.7), and TNF is back to baseline.
  - The HGMEC reversal is largely gone by 24 h.
  - 24 h contrasts carry arm-level proliferation and metabolism shifts even without IL-33, which contaminate reversal estimates.
  - 24 h is useful only for sustained markers: OPG, CCL20, CSF3, CXCL6, C3.
- **Patients: enrolment, pre-dose.**
  - This is the only timepoint at which our data show prognostic value (sST2, IL-6 and the others, NEWS2-adjusted).
  - Add early on-treatment samples (about 24 h, then day 3 and day 7) so PD can be read. The 6 h in vitro kinetics suggest fast markers (IL-6, CCL20) should move within the first day if IL-33 drives them. In vivo timing is not in our data and must be set in Gates 2–3.

---

## 8. Forward plan with gates and kill criteria

| Gate | Timing | Study | What it must establish | Kill / stop criterion (pre-specify) |
|---|---|---|---|---|
| **0. Remediate** | 0–6 wk | **(a)** Retrieve the full 1,194-assay result, individual NPX/LOD data, clinical covariates and time-from-onset. **(b)** Re-fit the archived counts: library identity/contamination QC, document the excluded library, per-cell-line voom/limma, report HGMEC IL-33 vs isotype, restate SELE/VCAM1/ICAM1/CXCL8/CCL2/PTX3/IL1RL1. **(c)** Second blinded IHC reader (κ), documented scoring, reconciled labels. | The neutralisation conclusion survives per-cell-line models. The IL-33 assay result is known. sST2 adds discrimination over NEWS2 (AUC, NRI). | Neutralisation not reproducible in the re-fit. |
| **1. Pharmacology & human relevance** | 2–6 mo | **(a)** AX-1177 concentration–response against IL-33red **and IL-33ox** in primary human lung microvascular endothelium (≥3 donors), with and without pre-incubation. Readouts at 6 h: GM-CSF, CCL20, IL-6, IL-8; surface E-selectin/VCAM-1; tissue-factor procoagulant activity. **(b)** Conditioned media from damaged or virus-infected primary airway epithelium (ALI) ± AX-1177. **(c) Decision-critical:** enrolment sera from the existing 100-patient cohort on endothelial cells ± AX-1177, 6 h readout. **(d)** Score the IL-33 endothelial signature in the 22 archived post-mortem lung RNAs (Zr4940 series). | Potency in lung endothelium. The share of endogenous and patient-serum endothelial activation that is IL-33-dependent, and whether that share tracks sST2 and outcome. | Patient-serum and endogenous activity are negligibly AX-1177-reversible (threshold fixed in advance), or potency falls short of a pre-agreed benchmark (e.g., sST2-Fc or a reference anti-IL-33). |
| **2. In vivo & safety** | 6–12 mo | A viral and a bacterial pneumonia model (AX-1177 if cross-reactive, otherwise a surrogate or humanised IL-33 system). Endpoints: lung endothelial activation and permeability, neutrophil influx, microthrombosis, survival, and **pathogen load**. PK/PD with biomarker kinetics. | Benefit on vascular injury without impaired pathogen clearance. Biomarker kinetics to set clinical sampling. | No vascular benefit, or impaired clearance. |
| **3. Clinical biomarker validation** | 3–12 mo (parallel) | Contemporary, vaccinated-era, multi-pathogen hospitalised LRTI cohort (SARS-CoV-2, influenza, RSV, bacterial CAP). Serial samples at enrolment, 24 h, 72 h and day 7. | sST2 cut-off prognostic across pathogens; prevalence of sST2-high patients; PD-marker kinetics. | sST2 not prognostic outside the original pre-vaccination COVID-19 cohort, or sST2-high prevalence too low to be feasible. |

**If all gates are passed:** a Phase 1b/2a study in sST2-high hospitalised pneumonia.

- Primary: PD (IL-6, CCL20, sIL-18R1, OPG, plasma TF; ex vivo serum neutralisation).
- Safety: viral clearance and secondary infection.
- Exploratory efficacy: ICU, invasive ventilation or death at 30 days.

---

## 9. If the committee drops AX-1177: what we would be dropping, and why

**What we would be dropping.** A human IgG1 anti-IL-33 that, in our hands:

- completely neutralises reduced-IL-33 signalling in two human endothelial beds;
- does so even without pre-incubation;
- shows no detectable activity on its own.

We would also drop a ready-made biomarker framework for severe pneumonia: sST2 for enrichment, and IL-33-inducible endothelial proteins for PD, already shown to track outcome in our own cohort.

**Why we would drop it.**

- There is no evidence yet that blocking IL-33 changes outcome.
- The human link is correlative, single-centre and pre-vaccination, and it rests on a non-specific marker.
- The biology is not virus-specific.
- The IL-33 endothelial programme is only part of the severity signal.
- Potency and differentiation, including the oxidised-IL-33 claim, are untested.
- Blocking an endothelial antiviral-sensing module is a theoretical liability in viral infection.
- The data package needs remediation before any of it can be externally defended.

---

## 10. Anticipated committee challenges

| Challenge | Answer grounded in our data |
|---|---|
| "Single-donor cells and cancer lines." | Agreed. The neutralisation conclusion holds across two independent endothelial beds and two timepoints, with near-complete effects. Multi-donor lung microvascular replication is Gate 1a. The cancer lines contribute only the "no intrinsic activity" finding. |
| "The stats are broken." | The main defect inflates variance for about 0.5% of genes. That makes those genes uninformative, not falsely positive. A smaller opposite artefact creates a few tiny-effect false hits, which a fold-change floor removes. The neutralisation case rests on 329 genes with t>5 and is unaffected. We do not use q-values for E-selectin, VCAM-1 or IL-8. |
| "sST2 is non-specific." | Agreed. It is proposed only for enrichment. Mechanism will be tested directly with the patient-serum bioassay (Gate 1c). |
| "Nothing is COVID-specific." | That is why we recommend a host-response, pathogen-agnostic positioning rather than "viral LRTD". |
| "Blocking IL-33 during infection is risky." | Our data show an IL-33-driven endothelial ISG module that AX-1177 removes. Pathogen load is a kill criterion in Gate 2 and a safety biomarker in the clinic. |
| "Why not COPD or asthma?" | Our package contains no airway-epithelial IL-33 data and no airway-disease signal. It cannot support that switch. That would be a new investment case. |

---

## Appendix A: How the numbers were produced

- **Transcriptomics**
  - All 26 contrasts were merged by Ensembl ID (mmc5's two sheets were verified identical).
  - Checks on the delivered statistics:
    - BH was recomputed within each contrast (reproduced to within 10⁻¹⁴).
    - t-to-p consistency was used to infer df per gene.
    - SEs were derived as |logFC/t|.
  - Derived contrasts were built from arm arithmetic:
    - isotype+IL-33 vs IL-33 = (AX+IL-33 vs IL-33) − (AX+IL-33 vs iso+IL-33);
    - residual IL-33 effect under AX-1177 = (AX+IL-33 vs IL-33) + (IL-33 vs vehicle).
  - Percent inhibition = 1 − (AX+IL-33 vs vehicle)/(iso+IL-33 vs vehicle). Genes were selected on the IL-33 effect only, to avoid circularity.
  - Pathway analysis used fgsea on moderated t with MSigDB Hallmark (msigdbr 7.5.1).
- **Serum**
  - Panel suffixes were collapsed to 1,063 unique proteins.
  - Olink names were mapped to HGNC symbols (e.g., TF→F3, ST2→IL1RL1).
  - The BH denominator was reconstructed from exact ranks.
  - The signature-enrichment comparison used a Fisher exact test and Spearman correlation on z = log(OR)/SE.
- **Post-mortem**
  - Donor-level fields were forward-filled, and block scores averaged per donor.
  - Groups were compared with Kruskal–Wallis and Mann–Whitney tests.
  - A sensitivity analysis reclassified donors by their pathology text. All p-values are exploratory and uncorrected.

## Appendix B: Output files

- `tables/T1_data_integrity_findings.csv`: all integrity and provenance checks.
- `tables/T2_IL33_endothelial_signature_AX1177_reversal.csv`: 455 IL-33-induced, AX-1177-reversed genes (HUVEC 6/24 h) with HGMEC, percent inhibition and SE flags.
- `tables/T3_serum_proteomics_with_invitro_mapping.csv`: all 1,094 assays, collapsed protein IDs, in vitro behaviour of the encoding gene.
- `tables/T4_biomarker_proposal.csv`: marker, matrix, evidence, role, patient use, timepoint, next step.
- `tables/T5_postmortem_donor_level.csv` and `T5b_postmortem_group_tests.csv`.
- `tables/T6_genes_with_inflated_SE.csv`, `T7_antibody_alone_hits_summary.csv`, `T8_hallmark_GSEA_all_contrasts.csv`.
- `figures/Fig1`–`Fig5`.
