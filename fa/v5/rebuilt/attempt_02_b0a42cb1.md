---
title: "AX-1177 (anti-IL-33 mAb): portfolio audit recommendation and forward view"
subtitle: "Prepared for the respiratory portfolio committee"
---

**Basis.** This memo uses only the five AX-1177 files delivered, treated as ground truth: the methods annex, the HUVEC IL-33 RNA-seq, the RNA-seq contrast workbook, the serum proteomics and the post-mortem lung IHC. Every number below was re-derived from those files. The few points where outside context matters are labelled *outside our data*, and none of them is used to reach the recommendation. Supporting tables are in `AX-1177_supporting_tables.xlsx`, figures in `figures/`, and code in `code/`.

# 1. Recommendation

**Keep AX-1177, but as a gated, re-scoped asset. It should not continue as a development programme for "severe lower respiratory viral infection" in its current form.** Do not commit IND-enabling spend on the current thesis. Fund two gated stages:

- **Stage 0 (about 3 months, low cost):** re-analysis and assays on data and samples we already own.
- **Stage 1 (about 6 months):** decisive pharmacology, funded only if Gate A is passed.

Both stages have explicit kill criteria (Section 8).

**The case in four points**

1. **The molecule works.** AX-1177 almost completely reverses the IL-33 response in endothelial cells:
   - median reversal **98% at 6 h** across 376 robust IL-33-regulated genes, and **81% at 24 h**;
   - seen in two vascular beds;
   - achieved even though the antibody was added at the same time as IL-33, with no pre-incubation.

   It showed no activity of its own in four cell types. Molecule-level problems (potency or off-target activity), a common reason to kill a preclinical antibody, are not what limits this asset.
2. **The disease link is not established by our data.**
   - Our post-mortem lungs show **no increase in IL-33 in COVID-19**. Staining is, if anything, lower in endothelium and vascular smooth muscle (donor-level p = 0.05–0.07).
   - IL-33 itself is **missing from the serum proteomics delivery**.
   - The supportive human signal is indirect. Soluble ST2 (sST2), IL-33's decoy receptor, is the **2nd strongest of 1,063 serum proteins** predicting ICU admission, ventilation or death (OR 3.0 per log unit, adjusted for NEWS2). However, it sits inside a proteome-wide severity signal.
3. **The gap is cheap to close.** Most of the decisive questions can be answered with material we already hold:
   - about 100 withheld Olink assays, including IL-33;
   - patient-level serum data;
   - 22 archived lung RNA samples;
   - archived RNA-seq counts.
4. **Neither alternative is consistent with all three datasets.**
   - Dropping now would discard a clean molecule on the strength of our weakest dataset: 31 donors, mislabelled groups, a single reader, and a readout that cannot tell IL-33 release from IL-33 loss.
   - Keeping the programme unchanged would spend money on a thesis our data do not support.

**If the committee drops AX-1177 anyway**, the accurate statement is:

> *"We are dropping a potent, clean anti-IL-33 antibody. Its disease hypothesis, that IL-33 drives severe viral lower respiratory infection, is not supported by our own human tissue data. It rests on a single, non-specific circulating marker (sST2) in one pre-vaccination COVID-19 cohort. We are not dropping it for a molecule-level problem. We are dropping an unproven option on IL-33-driven endotheliopathy in hospitalised viral pneumonia."*

# 2. Evidence scorecard

| Question the committee will ask | What our data show | Verdict |
|---|---|---|
| Does AX-1177 neutralise IL-33? | **Effect in HUVEC:** IL-33 changes 4,031 genes at 6 h. With AX-1177 present, 96% of them move back in the opposite direction (72% significantly).<br>**Size of reversal:** median 98% (IQR 85–105%) at 6 h across 376 robust genes; 81% (IQR 59–93%) at 24 h across 118 genes.<br>**Replication:** the same core programme is reversed in glomerular endothelium (HGMEC).<br>**Control:** the isotype is inert. | **Yes, strong.** Limits: in vitro, reduced IL-33 only, endothelium only, one concentration. |
| Does it do anything on its own? | **Hits:** 328 hits across eight isotype-controlled antibody-alone contrasts (4 cell types × 2 times).<br>**Quality:** 95% are near-zero-count genes or changes of less than 1.4-fold. The remaining 15 are singletons; none recurs or forms a pathway. | **No intrinsic activity detected.** |
| Is the IL-33 axis linked to severe outcome in patients? | **sST2:** ranks 2nd of 1,063 (OR 3.02, 95% CI 1.83–5.01, p = 1.7×10⁻⁵, FDR 0.009).<br>**Endothelial proteins:** the IL-33-inducible, AX-1177-reversible ones (IL-6, OPG, sIL-18R1, CCL20, CSF-1, tissue factor) are outcome-associated. But the set is only marginally enriched versus other proteins (27% vs 18% at FDR < 5%; p = 0.05), within a generic severity signal (82% of ORs > 1).<br>**IL-33 itself:** not delivered. | **Suggestive, indirect, non-specific.** |
| Is IL-33 increased or active in diseased lung? | **Donor-level IHC:** no difference in epithelium (p = 0.76); lower in COVID+ endothelium (p = 0.052) and vascular smooth muscle (VSM; p = 0.068).<br>**Relation to inflammation:** endothelial IL-33 staining falls as neutrophil and eosinophil infiltration rises (vs neutrophil elastase, IL-5Rα and H&E eosinophils: ρ = −0.41 to −0.51). | **Not supported** (and the readout is weak). |
| Do the data support "severe lower respiratory viral infection" as currently framed? | One virus (SARS-CoV-2), one pre-vaccination cohort, one timepoint. No other viruses and no in vivo infection data. | **No: the indication is broader than the evidence.** |

# 3. The defence: strongest arguments for keeping

**3.1 The pharmacology passes a stringent test** (Fig. 1).

- **Conservative design.** AX-1177 was added at the same time as IL-33, with no pre-incubation (annex §3). This is the harder test for a neutralising antibody.
- **Core NF-κB programme.** At 6 h, the key genes are reversed by about 100%. In log2 units, IL-33 effect vs AX-1177 effect: NFKBIA +3.13 vs −3.24; TNFAIP3 +4.75 vs −4.81; TRAF1 +5.89 vs −5.95.
- **Secreted effectors.** CSF2, CSF3, IL6 and CCL20 are fully reversed at 6 h (100–119%).
- **Replication in a second vascular bed.** The same programme is reversed in glomerular microvascular endothelium (HGMEC): 1,460 genes at 6 h, correlating with the HUVEC blockade profile at r = 0.64.
- **Controls are clean.** The isotype does not alter the IL-33 response. The antibody alone produces no coherent transcriptional change in endothelial, lung-epithelial or breast-epithelial lines.
- **Dose margin.** The antibody was present at a 41-fold molar excess over IL-33 (68.5 nM vs 1.66 nM). This is enough to show efficacy, but not enough to estimate potency.

**3.2 The biology AX-1177 blocks is the biology of severe viral pneumonia.**

- **What IL-33 does to endothelium, and AX-1177 reverses** (Fig. 1D):
  - **Coagulation:** induces tissue factor about 50-fold (log2FC 5.6, 97% reversed) and PAI-1 3.3-fold; also uPA and PAR-2.
  - **Thromboprotection and barrier:** suppresses thrombomodulin and occludin.
  - **Complement:** induces C3 28–70-fold, plus factor B, C1R and C1S.
  - **Recruitment:** induces leukocyte-recruiting chemokines and myeloid growth factors.
- **In our autopsies:** COVID+ lungs show diffuse alveolar damage (DAD) in 7/16 donors vs 0/15 COVID− (p = 0.007), and pulmonary thromboemboli in 4/16 vs 0/15 (p = 0.10).
- **In patient serum, the same thrombo-inflammatory axis moves in the "worse outcome" direction,** independent of NEWS2. Tissue factor, PAI-1 and uPA are IL-33-inducible and AX-1177-reversible in vitro. uPAR, vWF and ANGPT2 are not, or cannot be assessed, so they mark the axis rather than IL-33 itself:

  | Serum protein | OR | p |
  |---|---|---|
  | Tissue factor | 3.0 | 0.009 |
  | uPAR | 3.5 | 0.002 |
  | uPA | 3.0 | 0.014 |
  | vWF | 3.9 | 0.008 |
  | ANGPT2 | 2.2 | 0.009 |
  | PAI-1 | 2.1 | 0.048 |

**3.3 The pathway marker is strongly prognostic.** sST2 ranks 2nd of 1,063 unique proteins. Its association is independent of age, sex and NEWS2 at enrolment, and its confidence interval excludes an OR below 1.8 per log unit.

**3.4 The negative tissue data are not strong enough to kill on** (Fig. 4).

- **The readout cannot separate release from loss.** IHC measures IL-33 stored in nuclei. IL-33 is an alarmin that is released when cells are injured, so lower staining in inflamed lungs fits release just as well as absence. Our data cannot tell which.
- **Group labels are unreliable.** Eight of 31 donors carry disease labels that contradict their own autopsy diagnoses.
- **The scoring is weak.** There are no normal-lung controls and only one reader. 53% of endothelial blocks sit at the maximum score.
- **The effect is not COVID-specific.** The fall in staining tracks inflammation in general, not COVID in particular.

# 4. The attack: what the committee will challenge, and the honest answers

- **"sST2 is a generic severity marker."** Correct. It is prognostic and is not evidence that IL-33 drives disease. Our RNA-seq also cannot show that IL-33 regulates ST2, because IL1RL1 falls in the variance-inflated gene set (§10). We propose sST2 only as an enrichment marker.
- **"Where is IL-33 itself?"** It is not in the delivery.
  - The 15 Inflammation-panel analytes missing from the file are the low-detectability ones, including IL-33, TSLP, IL-4, IL-5 and IL-13. (Panel content is taken from Olink's published assay lists; that is the only external reference used here.)
  - The delivered FDRs reconstruct with about 1,194 tests against 1,094 assays delivered. So about 100 assays were run but withheld.
  - Retrieving them is the first action of Stage 0.
- **"The serum signal is everything at once."** Correct.
  - About half the proteome is associated with outcome (Storey π0 ≈ 0.5), and 82% of ORs are above 1.
  - Top hits include intracellular proteins (NPM1, CALR, GSTP1, PRDX1/6), consistent with release from damaged cells.
  - The AX-1177-reversible endothelial set is only marginally enriched (p = 0.05). sST2's rank alone does not prove pathway specificity.
- **"The tissue shows less IL-33 in COVID."** Yes, as a trend. IHC alone cannot tell us whether the IL-33 programme is active in tissue. That is why Stage 0 profiles the 22 archived lung RNAs for the AX-1177-reversible signature.
- **"The pharmacology is narrow."** Yes.
  - **Conditions tested:** one concentration; reduced IL-33 only, at 30 ng/mL (supraphysiological).
  - **Cell types:** endothelial cells only. No lung endothelium, airway epithelium or immune cells.
  - **Donors and models:** single donors; no in vivo data.
  - **Untested differentiator:** the stated advantage, binding oxidised IL-33, has never been tested functionally. The epithelial lines received no IL-33 at all.
  - **Weaker blockade at 24 h:** 81% vs 98%. The cause is unknown (potency or kinetics vs secondary mediators).
- **"Blocking an alarmin during active viral infection could impair host defence."** Our data do not address this; there is no infection model. Stage 1.4 includes viral clearance.
- ***Outside our data (flagged):*** other anti-IL-33 and anti-ST2 antibodies are in late-stage clinical development in COPD and viral lung infection. At least one is reported to share the same stated reduced/oxidised binding profile (public information; verify with competitive intelligence). This does not change what our data show, but it raises the bar for differentiation, and our current package does not clear it.

# 5. What indication our data actually point at

Our data point at a narrower version of the current indication, not a new disease:

- **Site of action:** the vascular endothelium is where AX-1177 has shown activity.
- **Clinical setting:** hospitalised viral pneumonia with a thrombo-inflammatory endotheliopathy (a pro-clotting, inflammatory state of the blood-vessel lining).
- **Population:** enriched by high circulating sST2.
- **Timing:** early in the hospital course.

| Line of evidence | What it shows |
|---|---|
| Mechanism (in vitro) | IL-33 drives endothelial NF-κB signalling, which induces tissue factor, PAI-1, complement and chemokines, and suppresses thrombomodulin and occludin. AX-1177 reverses this. |
| Patients (serum, at enrolment) | The same axis and sST2 predict ICU admission, ventilation or death independent of NEWS2. Tissue factor, PAI-1, uPA, IL-6, OPG, sIL-18R1 and CCL20 are IL-33-inducible and AX-1177-reversible in vitro. uPAR, vWF and ANGPT2 are not, or cannot be assessed. |
| Tissue | COVID+ lungs show DAD and thromboemboli. Stored IL-33 is not increased. |
| Timing | The endothelial IL-33 response is larger at 6 h than at 24 h (4,031 vs 1,836 genes), and blockade is more complete at 6 h. With only two timepoints the peak is not defined, but the evidence favours an early therapeutic and sampling window (enrolment). |

**What the data do not point at:** COPD, asthma or type-2 disease, kidney disease, oncology, fibrotic lung disease and cardiovascular disease. Each was tested against our data and is unsupported (§9). Moving to any of these would be a new thesis needing new data, not a repurposing that our data justify.

# 6. What the next studies must establish (in order)

1. **The target is present.** Is extracellular IL-33 (free or complexed; reduced or oxidised) detectable, and higher in patients who deteriorate, independent of NEWS2? *Source: the withheld Olink data, plus a high-sensitivity assay on the 100 stored sera.*
2. **The pathway is active in diseased lung.** Is the AX-1177-reversible endothelial signature elevated in viral-pneumonia lungs compared with non-pneumonia lungs? *Source: the 22 archived lung RNAs, plus IHC re-scored against normal-lung controls.*
3. **The drug blocks disease-relevant IL-33.**
   - Does AX-1177 block endothelial activation driven by IL-33 released from virus-infected human airway epithelium?
   - Does it do so at clinically achievable concentrations, against oxidised as well as reduced IL-33, and in lung microvascular endothelium?
   - What are IC50 and IC90?
4. **There is benefit without harm in vivo.** In a viral pneumonia model, does blockade reduce lung injury, vascular leak and coagulopathy without impairing viral clearance?
5. **The biomarkers replicate.** Does sST2 hold up as an independent prognostic marker in a contemporary, post-vaccination, multi-virus hospitalised cohort? Do the pharmacodynamic (PD) markers move in the expected window?

# 7. Biomarkers, sampling timepoint and role in patients

**Primary sampling timepoint:** **enrolment**. That means within 24 h of hospital admission, before the first dose and, where feasible, before systemic corticosteroids or other immunomodulators.

- **It is the only timepoint with clinical evidence.** sST2 and the endothelial proteins were measured at enrolment and adjusted for enrolment NEWS2.
- **The IL-33 response is larger early in vitro** (6 h vs 24 h), so the informative window is likely early.
- **Corticosteroids confound PD.** They suppress NF-κB-driven markers.

**Additional PD timepoints:**

- **24 h after dosing:** the early IL-33 programme.
- **Days 3 and 7:** later-wave markers such as complement C3 and C1S, which were still rising at 24 h in vitro.

| Tier | Marker(s) | Our evidence | Role in patients | Go into patients? |
|---|---|---|---|---|
| 1 | **sST2** | 2nd of 1,063; OR 3.02 (1.83–5.01) per log unit, independent of NEWS2 | **Prognostic enrichment and stratification.** Not predictive; not PD. | **Yes, in the first patient study.** Set the cut-off in an independent cohort. |
| 2 | **IL-33, free and total (drug-complexed)** | Not delivered; almost certainly below Olink LOD | **Target engagement** (PK/PD, dose selection); exploratory predictive | **Yes, once a sensitive, drug-tolerant assay is validated** |
| 3 | **OPG, sIL-18R1, CCL20, CSF-1, tissue factor, PAI-1** (IL-6 only within a composite) | Induced 3- to 590-fold by IL-33 in vitro and 81–107% reversed by AX-1177; outcome-associated at FDR 0.01–0.14 | **Exploratory PD panel** (composite score) and proof of mechanism | **Yes, as exploratory endpoints only.** Confirm at protein level in vitro first (Stage 1.1). |
| 4 | CXCL5, CXCL6, G-CSF | Strongly induced and reversed, but not outcome-associated (p = 0.23–0.95) | Mechanistic PD only | Optional |
| 5 | HGF, PTX3, ANGPT2, vWF | Outcome-associated, but either not IL-33-responsive or uninformative in vitro | Baseline risk covariates | Yes, as covariates only (not PD) |
| ✗ | E-selectin, VCAM-1, IL-8, MCP-1 as PD markers; IL-33 IHC; antibody-alone genes | Variance-inflated RNA-seq; non-discriminating tissue readout; noise | — | **No** |

Any study in infected patients also needs viral load/clearance and secondary-infection monitoring. This is standard for immunomodulators, and nothing in our data argues otherwise.

# 8. Plan and gates

| Stage | Step | What | Material |
|---|---|---|---|
| **0** (0–3 mo) | 0.1 | Retrieve the withheld Olink output: about 1,194 assays including IL-33, TSLP, IL-4/5/13, with LOD flags, plus patient-level NPX and clinical data. Re-analyse: per-SD ORs; what sST2 adds to NEWS2 (ΔAUC, bootstrap); an endothelial IL-33 score; adjustment for steroids and time from symptom onset. | Existing data |
| | 0.2 | Retrieve RNA-seq counts and the fitted model. Run sample-identity QC and per-cell-line refits. Deliver IL-33 vs isotype for HGMEC. Re-test SELE, VCAM1, IL8, MCP-1, IL1RL1 and PTX3. | Archive |
| | 0.3 | Re-score IHC: a blinded second reader on the raw 0–5 scale, plus digital nuclear H-score. Have a pathologist adjudicate the groups. Add normal-lung controls. | Existing slides |
| | 0.4 | Profile the 22 archived lung RNAs (9 COVID+, 9 COVID− "pneumonia", 4 other) for IL33, IL1RL1 and the AX-1177-reversible endothelial signature. | Existing RNA |
| **Gate A** | | **Continue only if both of the following hold.** (a) sST2 keeps independent prognostic value over NEWS2 in the patient-level re-analysis. (b) At least one of: serum IL-33 is detectable and higher in patients with events; or the AX-1177-reversible signature is elevated in viral-pneumonia lungs vs non-pneumonia lungs. **Otherwise stop.** | |
| **1** (3–9 mo) | 1.1 | IC50/IC90 against reduced and oxidised IL-33 in primary human lung microvascular endothelium (≥3 donors), concurrent vs pre-incubation, with protein readouts (TF activity, PAI-1, OPG, IL-6, CCL20, sIL-18R1, CSF-1). | New |
| | 1.2 | Endogenous IL-33: infect primary airway epithelium at air-liquid interface (ALI) with influenza, RSV or SARS-CoV-2, then expose lung endothelium to its conditioned medium ± AX-1177. | New |
| | 1.3 | Oxidised IL-33 / RAGE–EGFR signalling in primary airway epithelium ± AX-1177. This tests the stated differentiator. | New |
| | 1.4 | Viral pneumonia model (using cross-reactivity data or a surrogate antibody). Readouts: lung injury, vascular leak, coagulation markers, survival and viral clearance. | New |
| **Gate B** | | **Advance to clinical planning only if both hold.** (a) AX-1177 inhibits endothelial activation driven by endogenous, virus-induced IL-33 by at least 50% at clinically achievable exposure. (b) It does not impair viral clearance. **Otherwise stop.** | |
| **2** (9–18 mo) | 2.1 | Prospective observational biomarker cohort: hospitalised, post-vaccination, multi-virus. Sample at enrolment, 24 h, day 3 and day 7. Size it from the Stage 0 patient-level SDs. Then design a proof-of-mechanism study: sST2-enriched, dosed early, with the thrombo-inflammatory PD panel. | New |

# 9. Considered and ruled out

**Indications**

- **Keep "severe lower respiratory viral infection" unchanged.** Ruled out. The data cover one virus, one pre-vaccination cohort and one timepoint, and the tissue does not support the thesis.
- **COPD.** Ruled out; not supported by our data.
  - A raw comparison suggested higher endothelial IL-33 in COPD/emphysema donors (COVID-negative donors only, p = 0.0065).
  - But COPD donors were mostly those *without* acute pneumonia (6/8 vs 1/7), and acute pneumonia lowers staining.
  - After adjusting for acute pneumonia, COVID status and age, the effect disappears (p = 0.73).
  - We have no COPD cohort and no airway-epithelial or oxidised-IL-33 experiment.
- **Asthma or type-2 inflammation.** Ruled out; not supported.
  - There is no type-2 signature in tissue. IL-33 is unrelated to eosinophil granule proteins (ρ = −0.20 to +0.08) and inversely related to H&E eosinophils and IL-5Rα.
  - COVID+ and COVID− lungs do not differ in eosinophil, basophil or mast-cell scores.
  - IL-4, IL-5, IL-13 and TSLP were not delivered.
- **Kidney (AKI or diabetic kidney disease).** Ruled out; not supported. HGMEC shows that glomerular endothelium can be blocked, but we have no kidney disease data. Serum KIM-1 is weak (p = 0.03; FDR ≈ 0.10).
- **Oncology.** Ruled out. A549 and MCF7 were only tested with antibody alone.
- **Fibrotic lung disease.** Ruled out: three donors and no data.
- **Cardiovascular disease (sST2 is a heart-failure marker).** Ruled out: no data.

**Analytical shortcuts ruled out.** Each would have changed a conclusion.

- **Ranking IL-33 genes by fold change.** The HUVEC file is sorted by log2FC. Its top rows, SELE (11.2) and VCAM1 (8.7), are not significant (FDR 0.50–0.51). Neither are CXCL8 (FDR 0.19) or CCL2 (FDR 0.77).
- **Reading the "6h" and "24h" contrast sheets as timepoint-specific.** They are identical duplicates.
- **Using sST2, E-selectin, VCAM-1, IL-8, MCP-1 or PTX3 as AX-1177 PD markers.** The RNA-seq is uninformative for all of them (§10, issue R3).
- **Treating antibody-alone hits as off-target liabilities.** They are noise. Compound_47-vs-DMSO contrasts are uninterpretable, because DMSO is not the antibody's vehicle.
- **Claiming epithelial IL-33 blockade.** The epithelial lines had no IL-33 arm.
- **Quantifying the IL-33 effect in HGMEC.** There is no vehicle arm.
- **Counting the 178 delivered proteomic hits at face value.** Twenty-seven proteins appear on more than one panel (IL-6 four times), and BH was computed over about 1,194 tests. After de-duplication there are 186 hits among 1,063 unique proteins. The count is not the point either way, because the signal is pervasive.
- **Ranking proteins by OR.** ORs are per log unit and scale-dependent; for example, CSF-1 has OR 90 (95% CI 4–1,933).
- **Block-level post-mortem statistics.** These give p = 0.007 for VSM vs 0.068 at donor level, because three donors supply 24 of 49 COVID+ blocks.
- **Taking disease-category labels at face value.** Eight of 31 contradict the autopsy. The "non-pneumonia" group includes organising pneumonia, acute pneumonitis, pulmonary coccidioidomycosis and IPF.
- **Reading lower IL-33 staining as either "no IL-33 biology" or "IL-33 release".** IHC cannot separate the two.

# 10. Data integrity issues the committee should know about

The full log of 24 items, with evidence and fixes, is in the workbook (`Data_issue_log`). These are the ones that matter for the decision:

- **R3: RNA-seq variance inflation.**
  - About 275 genes (1%) have standard errors more than 5× the expected value in *every* contrast (Fig. 2). They include:
    - canonical endothelial activation markers: SELE, VCAM1, CXCL8, CCL2, CXCL1, PTGS2, PTX3, IL1RL1;
    - endothelial identity genes: CDH5, VWF, PECAM1, KDR;
    - epithelial-line identity genes: KRT8/18/19, GATA3, AKR1C1–3;
    - housekeeping genes: GAPDH has SE 9.6 vs a median of 0.34.
  - Y-linked genes are normal.
  - The pattern fits cross-library contamination (all 114 libraries shared one flow cell) or a mislabelled library, under a single model that pools variance across four very different cell types.
  - Consequence: for these genes, IL-33 regulation can be neither confirmed nor excluded.
  - The core IL-33 programme genes used for every conclusion above have normal variance.
- **P1: The drug target is missing from the serum data.** IL-33 is absent, and about 100 assays were withheld.
- **P6: Narrow serum cohort.** Single centre, pre-vaccination, one timepoint, n = 100. No data on treatments or time from symptom onset.
- **M1–M5: Post-mortem limitations.**
  - pseudo-replication: 74 blocks from 31 donors, handled here at donor level;
  - donor fields recorded only on the first block;
  - labels contradict pathology in 8/31 donors;
  - scores delivered as grade + 0.5, reaching 5.5 on a stated 0–5 scale, with ceiling effects;
  - a single reader;
  - SARS-CoV-2 status missing for donor 1905.
- **R5–R8: Gaps in the RNA-seq design.**
  - no HGMEC vehicle arm;
  - no IL-33 in the epithelial lines;
  - DMSO used as a comparator for an antibody;
  - a single concentration, single donors, and reduced IL-33 only.

# Appendix A. How the numbers were derived

- **Reversal.** % reversal = −(AX-1177 + IL-33 vs isotype + IL-33 log2FC) ÷ (IL-33 vs vehicle log2FC) × 100.
  - The robust gene set requires: FDR < 0.01, |log2FC| > 1, normal variance (SE ratio < 3) and AveExpr > 0.
  - The isotype-controlled contrast shares no group with IL-33 vs vehicle, so the ratio is not biased by shared noise.
- **Variance diagnostics.** SE = |log2FC / t|, compared with the median SE of genes at the same expression level (40 bins).
- **Proteomics.** Cross-panel duplicates were collapsed to one assay per protein, chosen without reference to outcome (lowest below-LOD fraction, then unsuffixed name). BH was then recomputed over 1,063 proteins.
  - **In vitro–patient bridge:** proteins were mapped to genes with a curated Olink-to-HGNC table; Olink "TF" maps to F3 (tissue factor).
  - **Enrichment test:** Fisher's exact test and Mann-Whitney on signed −log10 p.
  - **Undocumented columns:** `composite_endpoint_0/1` were interpreted as below-LOD fractions among 56 non-events and 44 events.
- **Post-mortem.** Donor fields were forward-filled, and scores averaged per donor. Tests are two-sided Mann-Whitney and Spearman at donor level. A donor random-intercept mixed model was run as a sensitivity analysis. Pathology features (acute pneumonia, DAD/ALI, thromboemboli, emphysema) were curated by hand from the delivered autopsy text and are listed in the code.
- **Multiplicity.** The post-mortem analyses are exploratory. The 36 group comparisons and 24 IL-33-versus-cell-marker correlations were run, and none survives correction for multiplicity (smallest p = 0.004). They are reported for direction and consistency, not as confirmatory tests.

# Appendix B. Figures

- **Fig. 1:** AX-1177 in vitro pharmacology: reversal of the IL-33 programme at 6 h and 24 h, DE counts by contrast, and the coagulation, complement, barrier and PD genes.
- **Fig. 2:** RNA-seq QC: variance inflation in cell-identity genes and canonical activation markers.
- **Fig. 3:** Serum proteomics: ranked associations, and the bridge between in vitro IL-33 response and patient outcome.
- **Fig. 4:** Post-mortem IL-33 IHC at donor level, and its inverse relation to inflammation.

![Fig. 1. AX-1177 in vitro pharmacology.](figures/Fig1_AX1177_in_vitro_pharmacology.png)

![Fig. 2. RNA-seq variance QC.](figures/Fig2_RNAseq_variance_QC.png)

![Fig. 3. Serum proteomics and in vitro–patient bridge.](figures/Fig3_serum_proteomics_bridge.png)

![Fig. 4. Post-mortem IL-33 IHC (donor level).](figures/Fig4_postmortem_IL33_IHC.png)
