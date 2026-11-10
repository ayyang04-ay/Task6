# AX-1177 (anti-IL-33 mAb; research code Compound_47): portfolio audit recommendation

**Basis.** This uses only the five files in the AX-1177 data dump: the methods annex, serum proteomics (mmc2), post-mortem lung IHC (mmc3) and endothelial/epithelial RNA-seq contrasts (mmc4, mmc5). All the numbers below were recomputed from those files (code in `analysis_code/`). No external literature or competitor data were used as evidence. General biology is used only to interpret the data, for example that ST2 is the IL-33 receptor.

---

## 1. Bottom line

**Recommendation: KEEP AX-1177, but re-scope it and put it behind gates. Stop carrying it as a broad "viral LRTD" asset.**

Our data support two claims strongly. They do not yet support the third, and that third claim is the one an indication requires.

| Claim | Status in our data | Key numbers |
|---|---|---|
| 1. AX-1177 completely and specifically neutralises IL-33-driven activation of human endothelium | **Strongly supported** | HUVEC 6 h: median reversal of IL-33-induced genes **100%** vs isotype (92% significantly reversed). Expressed genes changed ≥2-fold fall from 278 to **17** (noise floor 11). Same program suppressed in glomerular microvascular EC. Antibody alone: **0** expressed genes changed (FDR<0.05, ≥2-fold) in 15/16 contrasts across 4 cell types |
| 2. The IL-33 receptor axis tracks progression in hospitalised viral pneumonia | **Supported (association, one cohort)** | Serum **sST2 ranks #2 of 1,063 proteins** for ICU/IMV/death within 30 days. OR 3.02 (1.83–5.01) per log unit, FDR 0.009, adjusted for age, sex and NEWS2 (n=100, 44 events, pre-vaccination COVID-19) |
| 3. IL-33 is active in the diseased lung and drives the clinical phenotype | **Not shown** | IL-33 itself is **absent from the serum delivery**. Lung IL-33 IHC does not differ between COVID+ and COVID− pneumonia (epithelium p=0.92, endothelium p=0.16). The in vitro IL-33 program is **not enriched** among outcome-associated proteins (22% vs 19%, p=0.26) |

**Why keep rather than drop.** The missing link (claim 3) can mostly be tested with material we already own:

- the ~100 serum assays that were analysed but not delivered, which probably include IL-33 itself;
- the archived RNA-seq count matrix;
- RNA from 22 archived lung blocks;
- residual enrolment serum.

Dropping now would mean deciding on gaps that are cheap to close. Keeping is only defensible with explicit gates and kill criteria (Section 5.3).

**What the data point at.** They do **not** point at viral LRTD broadly. They point at a narrower indication:

- **hospitalised viral pneumonia at risk of progression to critical illness (ICU, invasive ventilation or death);**
- **with a systemic endothelial-activation phenotype;**
- **enriched by high sST2 at admission;**
- **evidenced so far only in pre-vaccination COVID-19.**

No data support a pivot to type-2 airway disease, kidney disease or heart failure (Section 6).

**Before the committee meets, fix four data defects** (Section 7):

- 82 key endothelial genes (including E-selectin, VCAM-1, IL-8 and ST2) have invalid RNA-seq statistics;
- ~100 analysed serum assays are missing from the delivery;
- 9/31 tissue donors have disease labels contradicted by their own pathology reports;
- the contrast proving IL-33 activity in HGMEC was never delivered.

**60-second version for the committee**

1. "AX-1177 works as a molecule. In human endothelium it switches off the entire IL-33-driven inflammatory and procoagulant program, even when added at the same moment as IL-33, and it does nothing on its own in four cell types."
2. "In 100 hospitalised COVID-19 patients, the IL-33 receptor (sST2) was the second-strongest of 1,063 serum proteins for predicting ICU, ventilation or death, independent of NEWS2."
3. "What we have not shown is that IL-33 itself is active in the disease. The tissue study cannot show it, and the IL-33 serum result is missing from our own delivery."
4. "So we keep the asset but narrow it to sST2-high hospitalised viral pneumonia at risk of progression, and we gate it. Gate 0 uses data already in our archive. If patient serum shows no AX-1177-sensitive endothelial activity and there is no independent sign of IL-33 activity in disease (lung RNA or serum IL-33), we release it."

---

## 2. What the data are, and what each dataset can and cannot tell us

| Dataset | Design (from annex and files) | Can tell us | Cannot tell us |
|---|---|---|---|
| **In vitro RNA-seq** (mmc4/5) | HUVEC (6 arms), HGMEC (5 arms, **no vehicle**), A549/MCF7 (4 arms, **no IL-33**). n=3 per arm, 6 h and 24 h. IL-33red 30 ng/mL (≈1.7 nM) + AX-1177 10 µg/mL (≈68 nM, 41-fold molar excess), added **concurrently**. One limma-voom fit across all 114 libraries; 26 contrasts delivered | Whether AX-1177 blocks IL-33red signalling in endothelium, and whether it has IL-33-independent effects | Potency (single dose); oxidised IL-33 / epithelial biology (never tested); donor variability (single donors); lung microvasculature (not used) |
| **Serum proteomics** (mmc2) | 100 hospitalised PCR+ SARS-CoV-2 patients, single centre, pre-vaccination. Enrolment serum. 13 Olink panels, 1,094 assays delivered (1,063 unique proteins). Logistic models per assay, adjusted for age, sex, NEWS2. 44 events / 56 non-events | Which circulating proteins at admission predict 30-day ICU/IMV/death | Causality; response to treatment; other viruses; vaccinated patients; IL-33 itself (not delivered) |
| **Post-mortem lung IHC** (mmc3) | 31 donors / 74 blocks, semi-quantitative, single reader. Labels: 16 COVID+ pneumonia, 10 COVID− pneumonia, 5 "non-pneumonia" | Where IL-33 sits in human lung; whether IL-33 or eosinophils differ by group | Dynamics; release of IL-33; anything about living patients. It has no normal-lung control |

---

## 3. The case for keeping: evidence ranked by strength

### 3.1 Pharmacology is clean, complete and specific (strongest evidence)

**IL-33red drives a large inflammatory program in endothelium.**
- HUVEC 6 h: 4,031 genes at FDR<0.05 and 1,068 changed ≥2-fold (645 up). At 24 h: 1,836 and 512.
- Induced genes include neutrophil-mobilising factors (CSF2/GM-CSF +10.3 log2, CSF3/G-CSF +8.3, CXCL2/3/5/6) and chemokines (CCL20 +9.2, CX3CL1 +8.4, CXCL10 +6.9).
- Also induced: cytokines (TNF +7.9, IL6 +5.8, IL1B +3.6), adhesion (ICAM1 +6.0) and the procoagulant switch (tissue factor F3 +5.6, PAI-1 +1.7, thrombomodulin −1.0).
- NF-κB feedback genes are induced (TNFAIP3, NFKBIA, TRAF1, BIRC3).
- By logFC, SELE (+11.2), VCAM1 (+8.7), IL-8 (+8.2), CXCL1 (+8.2), MCP-1 (+4.2) and ST2/IL1RL1 (+1.6) are also strongly induced. Their statistics are invalid (Section 7).

**AX-1177 reverses essentially all of it, despite no pre-incubation.**
- For the 299 well-expressed IL-33-induced genes at 6 h, median reversal against the independent isotype+IL-33 control is **100% (IQR 93–106%)**, and **92%** are significantly reversed.
- At 24 h: 82% (IQR 69–96%), 68% significant. The late, partly escaping component is interferon- and complement-type (OASL, IFIT1, C3).
- Rescue is near complete. The derived AX-1177+IL-33 vs vehicle contrast leaves 17 expressed genes changed ≥2-fold at 6 h, against 278 with IL-33 alone and a noise floor of 11 (antibody vs isotype). The median residual is 0.3% of the IL-33 effect.
- I deliberately did **not** use the naive "AX-1177+IL-33 vs IL-33" slope (−0.82). It shares the IL-33 group with the IL-33 vs vehicle contrast, which builds in a negative correlation. The isotype-controlled estimate is the defensible one.

**The same program is blocked in glomerular microvascular endothelium.**
- HGMEC 6 h: AX-1177 suppresses 236 genes against both IL-33 controls.
- 73% of these are HUVEC IL-33 genes (r = −0.71; e.g., BIRC3 −9.0, CSF2 −7.2, CXCL3 −6.7, CSF3 −6.6, CCL20 −5.7 log2).
- The response is smaller by 24 h (33 genes).
- **Caveat:** HGMEC has no vehicle arm and the IL-33-alone contrast was not delivered, so the HGMEC IL-33 response is inferred.

**No IL-33-independent activity.**
- AX-1177 alone gives 14–73 FDR "hits" per contrast across 16 contrasts in 4 cell types. Of all hits, 490/632 are low-count transcripts and 99/632 are changes smaller than 0.5 log2. The rest are scattered one-off genes.
- Among expressed genes, **0 reach FDR<0.05 with ≥2-fold change in 15 of 16 contrasts** (1 gene in the 16th).
- There is no evidence of endogenous IL-33 tone in the cultures: IL-33-responsive genes are not shifted by AX-1177 alone (p=0.11–0.63).
- The isotype itself is inert on IL-33-induced genes at 6 h (median 0.01 log2).

### 3.2 The IL-33 receptor axis is among the strongest predictors of progression in patients

- **sST2 is the #2 protein of 1,063** (after HGF): OR 3.02 (1.83–5.01) per log unit, p = 1.7×10⁻⁵, FDR 0.0075 as delivered and 0.009 when recomputed on unique proteins. The models were adjusted for age, sex and NEWS2.
- It is not simply a cardiac-strain proxy in this cohort. NT-proBNP (p = 0.05–0.17 across two panels) and troponin I (p = 0.11) are weak, and cystatin C is null (p = 0.18).
- The cross-panel duplicates are reproducible. All 15 duplicated proteins with p<0.05 agree in direction across panels, with ORs within 1.6-fold (IL-6 on four panels: OR 2.07–2.31). The assay data look technically sound.

### 3.3 The patient phenotype resembles what IL-33 does to endothelium, though not specifically (see Section 4, point 3)

- Severe outcome is marked by neutrophil activation (CLEC5A #7, OSM #14, PRTN3, CD177, IL-8) and endothelial/vascular injury (HGF, PTX3, vWF, angiopoietin-2, tissue factor, VEGF-A, sFlt-1).
- It is not marked by type-2 inflammation. IL-5 (OR 1.00), eotaxin-1/-2, TARC, FcεRII and tryptase are all null; ECP is borderline (FDR 0.058).
- Several IL-33-inducible, AX-1177-reversible gene products are themselves prognostic: IL-6, CCL20, MCP-3, OPG, IL-18R1, CSF-1, IL-1β (FDR 0.017–0.044), with tissue factor and MCP-1 borderline (FDR 0.050).
- In lung tissue, **diffuse alveolar damage is the one COVID-specific feature**: 7/16 COVID+ vs 0/15 COVID− donors, p = 0.007. It is an endothelial–epithelial barrier injury.
- Endothelium is the compartment with the most IL-33 in every group (median at the 5.5 ceiling in both COVID-negative groups, 4.81 in COVID+). Endothelial IL-33 tends to be **lower** where inflammation is present:
  - ρ = −0.43 with neutrophil elastase;
  - 4.88 vs 5.50 in lungs with vs without documented pneumonia (p = 0.054);
  - this would fit release of the alarmin, but it is exploratory.

---

## 4. What the data do NOT show: weaknesses the committee will find anyway

1. **No direct evidence IL-33 is elevated or released in disease.**
   - IL-33 protein is not in the delivered serum file.
   - Lung IL-33 is not higher in COVID+ than COVID− pneumonia by donor-level tests or age-adjusted mixed models (endothelium p = 0.24, VSMC p = 0.23, epithelium p = 0.56).
   - Endothelial IL-33 is at the assay ceiling in 39/74 blocks, so an increase could not have been detected anyway.
2. **sST2 is an association, not proof of mechanism.**
   - It is a soluble decoy receptor. High sST2 may even mean released IL-33 is already being neutralised, which would argue against adding an antibody.
   - Only measuring free versus total IL-33 resolves this.
3. **The in vitro program is not specifically linked to outcome.**
   - 82% of all proteins trend upward with severity (sign test p ≈ 10⁻¹⁰¹), so "prognostic" is the default for a circulating protein in this cohort.
   - Against that background, IL-33-inducible proteins are no more prognostic than others (22% vs 19%, Fisher p = 0.26; robust to every threshold tried, p = 0.15–0.48).
   - Two of the leading prognostic markers (HGF #1, OSM #14) and the endothelial-injury markers angiopoietin-2 and vWF (both borderline, FDR ≈ 0.05) are not IL-33-inducible in vitro.
4. **Narrow clinical evidence.**
   - One single-centre cohort, n = 100, COVID-19 only, pre-vaccination, hospitalised, 44% event rate.
   - Nothing on RSV, influenza, outpatients or vaccinated patients.
5. **Pharmacology gaps.**
   - Single antibody concentration, so there is no IC50 and no potency ranking.
   - Reduced IL-33 only. The oxidised form the annex says AX-1177 also binds (its stated differentiator) was never tested.
   - The epithelial lines were never given IL-33, and MCF7 (breast) is irrelevant to lung.
   - Single-donor HUVEC and HGMEC; no lung microvascular endothelium; no in vivo, PK or safety data in the dump.
6. **Tissue study design.**
   - Five "non-pneumonia" controls, all with lung disease (IPF, coccidioidomycosis, organising pneumonia).
   - Elderly donors (median 82–84 years).
   - Endothelial and VSMC IL-33 correlate with age (ρ ≈ 0.55).
   - Single reader; pseudoreplication (3 donors supply 24/49 COVID+ blocks).

### 4b. Anticipated committee challenges and data-based answers

| Challenge | Answer from our data |
|---|---|
| "You haven't even measured IL-33 in patients." | Correct: it is not in the delivery. The FDR values show ~100 more assays were analysed than delivered, and the Inflammation panel delivered 77/92 slots. Retrieving them is Gate 0a and needs no new experiments. Until then our patient evidence for the axis is sST2 |
| "sST2 is just a generic severity or heart-strain marker." | It is adjusted for NEWS2, age and sex. It sits at the 99.8th percentile of association strength against a proteome in which 82% of proteins drift upward. Cardiac markers are weak in this cohort (NT-proBNP p = 0.05–0.17, troponin I p = 0.11). It is still not proof of mechanism, which is why Gates 0c and 1a exist |
| "Top serum marker is HGF, not anything IL-33-related." | Agreed. HGF is not IL-33-inducible in vitro (+0.5 log2, ns). We use it as a severity covariate, not a drug marker |
| "The in vitro data set is broken: E-selectin and VCAM-1 are non-significant." | The defect is confined to 82 of 26,210 genes and is identifiable by impossible standard errors. Everywhere else the statistics are internally consistent (single df ≈ 85, BH reproduces to 10⁻¹⁴). All headline numbers exclude the 82 genes. By logFC they are among the most induced (E-selectin +11.2) and most completely reversed (−11.0) genes |
| "A 41-fold molar excess is bound to work." | The design is conservative in one respect: no pre-incubation, so antibody and receptor competed for IL-33 from t = 0. It is uninformative on potency (single concentration), which is why dose–response is in Gate 1d |
| "The tissue study is negative. Doesn't that kill the hypothesis?" | It is uninformative rather than negative. There are 5 controls, all with lung disease; 9/31 labels conflict with pathology; 39/74 endothelial scores sit at the ceiling; there is one reader. DAD is the COVID-specific lesion (p = 0.007). The 22 archived RNA samples give a better test (Gate 1b) |
| "Pre-vaccination COVID is yesterday's disease." | That is a real limitation. Gate 1e replicates in post-vaccination COVID and influenza/RSV. If that fails, the asset is COVID-only and should be parked |
| "Why not move it to asthma/COPD, where IL-33 biology is established?" | Nothing in our data supports that move. Type-2 markers are null, there is no epithelial IL-33 experiment, IL-33ox was never tested, and there is no airway cohort. It would be a literature bet needing its own package |

---

## 5. Forward view

### 5.1 Which indication our data actually point at

| Candidate indication | Verdict | Why (our data) |
|---|---|---|
| **Hospitalised viral pneumonia at risk of progression to ICU/IMV/death, endothelial-activation phenotype, sST2-high** | **Recommended focus** | Our only human data are hospitalised patients and that exact composite endpoint. sST2 at admission predicts it independently of NEWS2. The severe phenotype is neutrophilic and endothelial, which is what IL-33 induces in endothelium. DAD is the COVID-specific lesion. AX-1177 blocks the endothelial program completely |
| Viral LRTD as currently framed (broad, incl. earlier or outpatient disease, any virus) | **Drop this framing** | No data outside hospitalised, pre-vaccination COVID-19; nothing on early disease |
| Type-2 / eosinophilic airway disease (asthma, COPD) | Not supported | Type-2 serum markers are null for severity. Tissue eosinophils track pneumonia, not COVID (EDN p = 0.52 COVID+ vs COVID−). IL-33 is not different in COPD/emphysema donors (p = 0.14–0.91). No epithelial IL-33 or IL-33ox experiments were done |
| Kidney / glomerular endothelial disease | Hypothesis only | The HGMEC response is inferred and fades by 24 h (236 → 33 genes). No renal patient data (KIM-1 FDR 0.14) |
| Heart failure (the sST2 context) | Not supported | No cardiac cohort, and cardiac markers are weak here |
| Thrombo-inflammation as a stand-alone indication | Fold into the focus indication | IL-33 raises tissue factor (+5.6 log2) and PAI-1 and lowers thrombomodulin, all reversed by AX-1177. Serum tissue factor is borderline (FDR 0.050). Thromboemboli 4/16 vs 0/15 (p = 0.10). Use as a PD and mechanism read-out |
| All-cause ARDS / sepsis | Possible later extension | The mechanism is not virus-specific, but we have no non-viral data |

### 5.2 If the committee drops AX-1177, what exactly it is dropping

**What we would give up:**
- a clean, specific IL-33 neutraliser with transcriptome-wide proof of complete functional blockade in two human endothelial beds;
- a candidate enrichment biomarker (sST2) with a strong adjusted association in patients;
- a ready-made pharmacodynamic panel (Section 5.4).

**What we would not be giving up,** because we never had it:
- evidence that IL-33 drives viral LRTD;
- tissue evidence of IL-33 involvement;
- any data outside pre-vaccination COVID-19;
- any in vivo efficacy, PK or safety package.

The honest one-liner for a drop decision: *"We are dropping a well-characterised antibody whose target has not been shown to be active in the disease we were developing it for."*

### 5.3 What the next studies must establish: gated plan with kill criteria

**Gate 0: data remediation (weeks; archived data only; no new wet lab)**

Actions:
- **0a.** Retrieve the ~100 serum assays that were analysed but not delivered. The BH values imply 1,194 tests and only 1,094 were delivered (Section 7). Priority: **IL-33**, plus TSLP, IL-4, IL-13 and IL-1α, and all LOD/QC flags.
- **0b.** Re-fit the RNA-seq data from the archived count matrix, **per cell type**. Restore valid statistics for the 82 affected genes. Deliver the missing contrasts: HGMEC IL-33 vs isotype, HUVEC isotype vs vehicle, and AX-1177+IL-33 vs vehicle.
- **0c.** Using patient-level serum data:
  - express ORs per SD, since per-log-unit ORs are not comparable (e.g., CSF-1 OR 90, CI 4–1,933);
  - adjust sST2 for NT-proBNP, troponin, eGFR and time from symptom onset;
  - bootstrap-validate an sST2 cut-off;
  - clarify "log-transformed", since NPX is already log2 and negative NPX cannot be logged.
- **0d.** Re-adjudicate tissue labels against the pathology reports and add a blinded second reader.

**GO if:** sST2 stays in the top decile after these adjustments, and IL-33 has been retrieved and is either detectable and associated with outcome, or undetectable for documented LOD reasons.

**Gate 1: bridging biology (months; mostly archived material)**

Actions:
- **1a. Decisive experiment.** Expose primary **lung microvascular** endothelial cells (≥3 donors) to enrolment serum from high- vs low-sST2 patients and from progressors vs non-progressors, ± AX-1177 vs isotype.
  - Read out the **179-gene cross-endothelial AX-1177-reversible IL-33 signature** (supplied) at **6 h**, plus secreted proteins.
  - **GO if** AX-1177 removes at least a pre-specified fraction (suggest ≥30%) of serum-induced signature activity in sST2-high or progressor sera, and not in low-sST2 sera.
- **1b.** Score the same signature in the **22 archived lung RNA samples** (9 COVID+, 9 COVID− pneumonia, 4 other). Relate it to DAD and to loss of endothelial IL-33.
- **1c.** Measure free and total IL-33 (reduced and oxidised forms) in residual enrolment serum.
- **1d.** Fill the pharmacology gaps:
  - dose–response ± pre-incubation (IC50);
  - an IL-33ox arm in primary bronchial epithelium, to test the dual-form claim;
  - IL-1β and TNF comparator arms, to identify which PD markers are IL-33-specific;
  - a 48–72 h time course.
- **1e.** Replicate the sST2 association in a **non-COVID viral pneumonia** cohort (influenza/RSV) and a **post-vaccination COVID** cohort.

**Decision rules at Gate 1**
- **KILL** (release from the portfolio) if the decisive experiment 1a is negative **and** there is no independent evidence of IL-33 activity in disease. That means neither 1b (signature in COVID lung RNA) nor 0a/1c (IL-33 associated with outcome, or free IL-33 detectable) is positive.
- **ADVANCE** to Gate 2 if 1a is positive **and** at least one of 1b or 0a/1c is positive.
- **PARK** on mixed results, e.g. 1a negative but lung RNA positive, which would point to local rather than systemic IL-33 biology. Then decide on a BAL or tracheal-aspirate study.
- **RE-SCOPE** to "COVID-only", or park, if 1e fails but the rest pass.

**Gate 2: clinical translation (only after Gate 1)**

- PK and target engagement first.
- Then a biomarker-rich phase 1b/2a in hospitalised viral pneumonia, enriched for high sST2 at admission.
- Primary: safety, PK and target engagement. Key secondary: change in the IL-33 PD panel at 24 h. Exploratory: 30-day ICU/IMV/death (the composite our cohort used).

### 5.4 Biomarkers: which could go into patients, in what role, and when

| Role in patients | Markers | Evidence from our data | Readiness |
|---|---|---|---|
| **Enrichment / prognostic stratification** | **sST2** | #2/1,063; OR 3.02, FDR 0.009, adjusted for NEWS2. IL-33 raises IL1RL1 mRNA +1.6 log2 and AX-1177 reverses it (statistics invalid) | **Closest to patients.** Needs a clinical-grade assay (Olink is research-use), an independently validated cut-off, and an AX-1177 interference test. **Not** a PD marker until we show it is IL-33-driven and unaffected by drug–IL-33 complexes |
| **Pharmacodynamic panel, IL-33-dependent and prognostic** | IL-6, CCL20, MCP-3*, OPG, IL-18R1, CSF-1, IL-1β, tissue factor (borderline) | Each is induced 2.2–9.2 log2 by IL-33 in HUVEC, ~96–109% reversed by AX-1177, suppressed in HGMEC, and prognostic (FDR ≤0.05) | Use as a composite score measured pre- vs post-dose, on the same Olink panels. Individually non-specific (other stimuli induce them), so never use for selection. *MCP-3 is low-count in vitro and noisy |
| **Pharmacodynamic, IL-33-dependent, not prognostic** | CXCL6, CXCL5, CXCL10, G-CSF, CX3CL1, TNFRSF9, ICAM-1 | Induced 5.3–9.4 log2 and ~87–109% reversed; not outcome-associated | Pure pathway-activity read-outs; useful for dose-finding |
| **PD candidates on hold** | E-selectin, VCAM-1, IL-8, MCP-1, PTX3 | Strongly induced and reversed by logFC, but in vitro statistics are invalid. Serum: IL-8 FDR 0.022, PTX3 0.013, MCP-1 0.050, E-selectin 0.087, VCAM-1 null | Only after the Gate 0b re-analysis |
| **Severity covariates / specificity controls** | HGF, angiopoietin-2, vWF, OSM, CLEC5A, PRTN3, CD177 (+ NEWS2) | Prognostic but **not** IL-33-inducible in vitro | Stratify and adjust. If these fall on drug but the IL-33 panel does not, the effect is not via the proposed mechanism |
| **Target engagement** | Free and total (drug-bound) IL-33, serum ± BAL | **No data**: IL-33 is not in the delivery | Develop the assay (Gate 1c) |
| **Not for patient use** | Lung IL-33 IHC; type-2 markers (IL-5, eotaxins, TARC, tryptase); RAGE/EGFR | IHC: post-mortem, ceiling, no group difference. Type-2: null. RAGE p = 0.055, EGFR null, IL-33ox never tested | Research only |

**Sampling timepoints**

- **Enrolment, hospital admission, pre-dose.** This is the only timepoint our outcome data validate: serum drawn at enrolment predicted 30-day ICU/IMV/death. Use it for sST2 enrichment and baseline PD. Record time from symptom onset and from admission, which our cohort lacks.
- **24 h post-dose: primary PD timepoint.** In vitro, the AX-1177-sensitive primary IL-33 response (TNF, F3, CX3CL1, IL-6, TRAF1) is maximal at 6 h and largely gone by 24 h, while reversal is still 82% at 24 h. Short-half-life primary-response proteins should therefore move early.
  - Add **day 3 and day 7** for the later complement and interferon-type component (C3, CFB, MX1/2, GBP5 rise at 24 h in vitro).
  - Optionally add a 6 h sample in the first cohort to define kinetics.
  - Follow outcome to day 30.
- **Ex vivo and in vitro work:** 6 h primary read-out, 24 h secondary.

---

## 6. What I considered and ruled out

**Indications.** See the table in 5.1. In short:
- broad viral LRTD: framing dropped;
- type-2 airway disease: no supporting data;
- kidney: hypothesis only;
- heart failure: unsupported;
- thrombo-inflammation: folded in as a mechanism read-out;
- all-cause ARDS/sepsis: deferred.

**Interpretations I tested and rejected**

| Tempting conclusion | Why rejected |
|---|---|
| "IL-33 does not induce E-selectin, VCAM-1, IL-8, MCP-1 or ST2" (P ≈ 0.2–1.0 in the tables) | Their implied SEs (logFC/t) are 2–36,723 log2 units versus a median of 0.33. A voom/limma fit cannot produce these, so the statistics are artefacts. By logFC these genes are among the most induced and most fully reversed |
| "AX-1177 has off-target effects" (up to 73 FDR hits alone) | Hits are low-count noise (490/632) or tiny shifts <0.5 log2 (99/632), with no recurrence or pathway coherence. 0 expressed genes ≥2-fold in 15/16 contrasts |
| "Reversal slope −0.82 quantifies efficacy" | That slope is biased by the shared IL-33 group. Isotype-controlled reversal and a derived full-rescue contrast were used instead |
| "COVID lungs show more IL-33 / more eosinophils" | No difference at donor level or in age-adjusted mixed models. Naive block-level tests inflate n (ICC 0.35–0.63) |
| "The IL-33 in vitro signature predicts outcome" | No enrichment over the general upward shift of the proteome (p = 0.26, robust to thresholds) |
| "Rank biomarkers by OR" | ORs are per log unit, which varies in spread across proteins (CSF-1 OR 90, CI 4–1,933). Rank by z and FDR |
| "mmc2 FDR values are over the 1,094 delivered assays" (as the annex states) | Recomputation shows BH over **1,194** tests (HGF adj.p = p × 1194 exactly) |
| "mmc5 sheets '6h' and '24h' hold 6 h and 24 h contrasts" | Both sheets hold the same 24 contrasts covering both timepoints; they are duplicates |
| "Epithelial lines show AX-1177 is inert in epithelium against IL-33" | They never received IL-33; they only test antibody-alone effects |
| "HGMEC IL-33 response is demonstrated" | No vehicle arm and the IL-33 contrast was not delivered; the response is inferred from AX-1177 suppression only |

**Not assessed, because it is absent from the dump:** competitive landscape, IP, CMC, PK/toxicology, binding affinity (held in the biologics file), and cost or timelines. The committee should get these from the relevant functions. They are not evidence either way here.

---

## 7. Data-integrity findings to fix before the audit

| # | Issue | Evidence | Impact | Fix |
|---|---|---|---|---|
| 1 | **82 genes have invalid limma statistics in all 26 contrasts** | Implied SE (logFC/t) 2.0–36,723 log2 units vs median 0.33 (99th centile 1.18). Includes SELE, VCAM1, CXCL8, CXCL1, CCL2, PTGS2, PTX3, IL1RL1, ESM1, VWF, CDH5, PECAM1, KDR | The most translatable endothelial genes look "non-significant". Headline numbers here exclude them | Re-fit from the archived counts (Gate 0b) |
| 2 | **~100 analysed serum assays not delivered; IL-33 absent** | BH adjusted p-values imply 1,194 tests (annex: "across all assays in the delivery"). Reconstruction: one undelivered assay had p ≈ 2–3×10⁻⁴ (≈ rank 20/1,194, FDR ≈ 0.017), a second had p ≈ 0.7–1.1×10⁻³, and ~16 had p<0.05. Inflammation panel delivered 77/92 slots | The key analyte for an anti-IL-33 program is missing. FDR values are not reproducible from the delivery | Retrieve the full results and QC (Gate 0a) |
| 3 | **Tissue labels contradicted by pathology in 9/31 donors** | 4/10 "COVID− pneumonia" donors have no pneumonia in their reports. 3/5 "non-pneumonia" donors have acute pneumonitis, organising pneumonia or coccidioidomycosis. 2/16 COVID+ (including an 8-block donor) have no acute pneumonia/DAD. One donor has missing SARS-CoV-2 status | Group comparisons are diluted. There is no true control group | Re-adjudicate; add normal-lung controls |
| 4 | **HGMEC IL-33 activity never shown** | No vehicle arm; IL-33 vs isotype contrast not delivered | The microvascular claim rests on inference | Deliver the contrast (Gate 0b) |
| 5 | Tissue scale and format | Scores up to 5.5 on a stated 0–5 scale ("n+" recoded as n+0.5; 61 values >5). 39/74 endothelial blocks at ceiling. One cell holds a formula (=(2+4.5)/2). Donor fields stored in merged cells | Ceiling removes sensitivity | Use digital quantitative IHC |
| 6 | Model design choices | One voom/eBayes fit pools variance and low-expression filtering across four unrelated cell types. AveExpr is averaged over all 114 libraries | Affects which genes pass and their precision | Per-cell-type fits |
| 7 | Labelling | mmc4 sheet says "Vehicle" but the contrast column says "Nontreated". mmc5 sheet names don't match content. A DMSO vehicle arm appears in an antibody experiment | Confusing, not outcome-changing | Document |
| 8 | Serum model details | "Log-transformed" NPX, which is already log2. Per-log-unit ORs. 27 proteins duplicated across panels inside the BH (concordant) | Effect sizes are not comparable across proteins | Per-SD ORs; report on unique proteins |

Checks that passed, which support trusting the rest of the data:
- limma P-values are consistent with a single df (≈85) and BH reproduces to 10⁻¹⁴ within each contrast;
- AveExpr is constant per gene;
- serum p-values match the Wald p from the CIs (max deviation 0.0002 log10);
- cross-panel duplicates are concordant;
- no evidence of a culture batch effect (single library batch and flow cell).

---

## 8. Methods (brief) and file index

**In vitro.**
- Delivered limma contrasts; 82 invalid-statistics genes excluded from inference.
- IL-33 signature: FDR<0.05 and |log2FC| ≥1, IL-33red vs vehicle in HUVEC.
- "Expressed" means AveExpr >0 (note this is an average over all 114 libraries).
- Reversal = −(AX-1177+IL-33 vs isotype+IL-33) / (IL-33 vs vehicle).
- Full rescue = (IL-33 vs vehicle) + (AX-1177+IL-33 vs IL-33), which equals AX-1177+IL-33 vs vehicle in logFC with no shared-group noise.
- HGMEC: genes significant in the same direction against both IL-33 controls.

**Serum.**
- Duplicates across panels collapsed to mean z and mean ln(OR); BH across 1,063 unique proteins.
- Olink assays mapped to genes by hand-curated alias table.
- Enrichment by one-sided Fisher test and Mann–Whitney test, sensitivity-tested across definitions.

**Tissue.**
- Donor-level means; merged donor fields forward-filled.
- Kruskal–Wallis and Mann–Whitney tests; block-level linear mixed models (random donor intercept) ± age.
- Pathology free text parsed for pneumonia, DAD, emboli, emphysema and fibrosis.

**Files**

| File | Content |
|---|---|
| `AX-1177_portfolio_audit_recommendation.md` / `.pdf` | This report |
| `AX-1177_supporting_tables.xlsx` | All supporting tables (README sheet inside) |
| `figures/Fig1–Fig5` | In vitro pharmacology; serum proteome and bridge; tissue; data integrity; biomarker role map |
| `tables/*.csv` | Same tables as CSV, plus the 179-gene core signature for Gate 1a/1b |
| `analysis_code/01–07_*.py` + `README.md` | Reproducible pipeline from the raw files (≈4 min; re-run from a clean cache reproduces all tables exactly) |
| `tables/key_numbers.json` | Every number quoted in this report, as computed |
