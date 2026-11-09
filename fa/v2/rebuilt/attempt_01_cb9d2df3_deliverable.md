---
title: "AX-1177 (anti-IL-33) — portfolio audit brief"
subtitle: "Recommendation, evidence, defence, forward plan"
---

# AX-1177 (anti-IL-33; research code Compound_47) — portfolio audit brief

**Scope.** This brief uses only the programme's delivered data: the methods annex; HUVEC, HGMEC, A549 and MCF7 transcriptomics (mmc4, mmc5); serum proteomics from the hospitalised COVID-19 cohort (mmc2); and post-mortem lung immunohistochemistry (IHC) (mmc3). Where I use general biology to interpret a result, I say so. All numbers can be reproduced with the scripts in `code/`. Supporting tables are in `tables/` and figures in `figures/`.

---

## 1. Bottom line

> **Recommendation: KEEP AX-1177, but stop treating it as a viral-LRTD (lower respiratory tract disease) development asset.**
> Re-classify it as *mechanism-validated, indication-unvalidated*. Put it on a time-boxed, evidence-gated hold whose first gate uses only material we already own, with kill criteria agreed now. Fund no viral-LRTD efficacy, IND-enabling or clinical-planning work on the current package.
> **If the committee will not fund Gate 1 (section 6.5), drop it.** Section 6.6 states what we would be dropping.

The case in three sentences:

1. **The molecule works.** AX-1177 neutralises the IL-33 (reduced-form) endothelial programme almost completely: median inhibition is **101 %** for robustly induced genes at 6 h and **84 %** at 24 h. This holds in both macro- and microvascular endothelium. The antibody has **no detectable activity of its own** in four cell types.
2. **The indication is unproven.**
   - No delivered dataset shows IL-33 is raised, released or specifically active in patients.
   - Lung IL-33 staining is constitutive and *not* higher in COVID-19.
   - IL-33 itself is missing from the delivered serum data.
   - Serum proteins that IL-33 induces in endothelium are **no more likely to predict outcome than any other protein** (21 % vs 19 %, p = 0.70).
3. **The gap is cheap to close.** We already hold the material to answer the deciding question before any new spend: 100 stored enrolment sera, 22 archived lung RNAs, the raw count matrices, and 100 analysed-but-undelivered serum assays (IL-33 is among the missing Inflammation-panel assays). The deciding question is: *is there IL-33 activity that AX-1177 can neutralise in the patients who do badly?*

---

## 2. Evidence ledger — what our data do and do not establish

| # | Claim | Our evidence | Strength |
|---|---|---|---|
| E1 | IL-33 (reduced) strongly activates endothelium | HUVEC: 4,031 DE genes at 6 h, 1,836 at 24 h. The response is an NF-κB inflammatory, adhesion, myelopoietic and pro-coagulant programme (Hallmark TNFα/NF-κB: 92/197 genes, 19-fold enrichment). Examples: SELE +11.2 log2 (~2,400×), CSF2 +10.3, CCL20 +9.2, VCAM1 +8.7, CXCL8 +8.2, TNF +7.9, IL6 +5.8, **tissue factor F3 +5.6 (~50×)**, PAI-1 +1.7, **thrombomodulin −1.0** | **Strong** (one donor per cell type) |
| E2 | AX-1177 neutralises that programme | Vs isotype + IL-33 at 6 h: 4,239 DE genes. Robustly induced genes (n = 52): median inhibition 101 % (IQR 96–103 %), 100 % reversed. All induced genes (n = 645): 95 %, 87 % reversed. At 24 h: 84 % (robust) and 73 % (all). IL-33-repressed genes are restored less fully (median 41 % at 6 h) | **Strong** |
| E3 | Microvascular endothelium (glomerular, HGMEC) responds and is protected | 1,460 AX-1177-reversed genes at 6 h, dominated by the NF-κB core (NFKBIA, TNFAIP3, TRAF1, RELB, NFKB1/2, IRAK2, BIRC3). 977 genes are significant in both HUVEC and HGMEC, 97 % in the same direction. Signal is weak by 24 h (269 genes) | **Moderate** (no HGMEC IL-33-vs-control contrast was delivered) |
| E4 | AX-1177 alone is pharmacologically silent | 16 antibody-alone contrasts (vs isotype, PBS, DMSO; 4 cell types × 2 times). "Hits" are either sub-0.25 log2 shifts in abundant genes or noise in barely detected genes. 0–9 genes per contrast exceed 2-fold among expressed genes. None reproduces across timepoints (6 h vs 24 h r = −0.06 to 0.18). Only 3 genes reach significance in ≥2 of the 8 isotype-controlled contrasts | **Strong** |
| E5 | The IL-33/ST2 axis carries prognostic information in severe COVID-19 | sST2 (soluble ST2, the IL-33 decoy receptor) ranks **2nd of 1,063 unique proteins**: OR 3.02 per log unit (95 % CI 1.83–5.01), q = 0.009, adjusted for age, sex and NEWS2 (National Early Warning Score 2). IL-33-inducible, AX-1177-reversible outputs also predict ICU admission, invasive ventilation or death: IL-6 (OR 2.14, same on 4 panels), IL-8, CCL20, MCP-1, OPG, tissue factor | **Moderate** (prognostic, not causal; one cohort) |
| E6 | The prognostic signal is *specifically* IL-33-driven | **Not supported.** IL-33-inducible and reversible proteins are prognostic at the background rate (21 % vs 19 %; Fisher OR 1.11, p = 0.70; strict definition 21 % vs 20 %, p = 0.88). Only a weak overall rank correlation (ρ = 0.15). Top predictors are not IL-33 targets: HGF (#1), HDGF, SEMA4C, ANXA1, CLEC5A, intracellular proteins. Many strongly induced IL-33 products do not predict outcome: G-CSF, CXCL1, CXCL5, CXCL6, CXCL10, VCAM-1, TNF, CD137 | **Negative** |
| E7 | IL-33 is up-regulated or active in diseased lung | **Not supported.** IL-33 is constitutive in basal epithelium, endothelium and vascular smooth muscle (VSM) in every group. It is numerically *lower* in COVID-19 donors: endothelium 4.81 vs 5.50, p = 0.075; VSM 2.38 vs 3.25, p = 0.084 (donor level). Endothelial staining is at ceiling in 39/74 blocks | **Negative / uninformative** |
| E8 | AX-1177 blocks oxidised IL-33 or epithelial IL-33 biology | **Not tested.** Only reduced IL-33 was used, and the epithelial lines were never exposed to IL-33 | **Absent** |
| E9 | Anything outside SARS-CoV-2 (other viruses, vaccinated era, non-respiratory disease) | **No data** | **Absent** |

![Figure 1](figures/fig1_AX1177_neutralises_IL33_endothelial_programme.png)

---

## 3. The case for "keep, re-scoped, gated"

**What we keep is a validated pharmacological tool, not a validated indication.**

1. **Target engagement in a disease-relevant cell is demonstrated.** AX-1177 blocks an IL-33-driven endothelial programme that covers several pathways relevant to severe viral pneumonia:
   - leukocyte recruitment: CXCL1/2/3/5/6/8, CCL20, CX3CL1;
   - adhesion: E-selectin, VCAM-1, ICAM-1;
   - myelopoiesis: GM-CSF, G-CSF;
   - a **pro-coagulant switch**: tissue factor up about 50-fold, PAI-1 up, thrombomodulin halved.

   The blockade is complete at 6 h even though the antibody was added *at the same time* as IL-33 with no pre-incubation, which is a stringent format.
2. **The same axis tracks outcome in patients.**
   - sST2 is the second-strongest of 1,063 proteins and adds information beyond NEWS2.
   - Endothelial activation and coagulation proteins are prominent among the predictors: vWF, angiopoietin-2, sFLT1, tissue factor, uPAR, t-PA, PAI-1.
   - Thromboembolic findings appear only in COVID+ autopsies (4/16 vs 0/15; p = 0.10).
3. **Clean profile.** No agonism and no off-target transcriptional signature in four cell types.
4. **The deciding experiment is cheap and uses owned material** (Gate 1). The current package is *not decision-grade in either direction*:
   - the pooled transcriptomic model hides the strongest IL-33 effects (false negatives for SELE, VCAM1, CXCL8);
   - the serum delivery omits 100 analysed assays, including at least 4 that were significant at FDR < 5 % and, apparently, IL-33 itself;
   - the lung IHC labels disagree with the autopsy diagnoses for 9 of 31 donors.

   Dropping on this package would be as hard to defend as advancing on it.

### Challenges the committee will raise, and the answers

| Challenge | Answer from our data |
|---|---|
| "sST2 is the #2 prognostic protein. Doesn't that validate the target?" | It validates **risk stratification**, not causation. sST2 is a decoy receptor that many stimuli induce. IL-33 raised IL1RL1 (ST2) mRNA only modestly in HUVEC (+1.6 log2; unreliable statistics) and not at all in HGMEC. The proteins IL-33 actually induces are not enriched among predictors (E6). |
| "Neutralisation is ~100 %. Why not advance?" | The IL-33 programme in endothelium is a generic NF-κB programme (general biology: TNF and IL-1β drive much of the same programme; not tested here). Without evidence of IL-33 activity in patients, complete blockade in a dish says nothing about benefit. |
| "Lung tissue is full of IL-33. Isn't the target there?" | It is there in *all* donors, at ceiling in endothelium, and not higher in COVID-19. The apparent "significant" group differences come from counting blocks instead of donors (block-level p = 0.017 and 0.007 become 0.075 and 0.084 at donor level), and they point in the *opposite* direction. |
| "Why not drop now and save the money?" | Gate 0–1 costs little, uses stored sera, RNA and data, and answers the one question the portfolio decision depends on. Dropping now means deciding on a package with known analytical defects. |
| "Why not pivot to COPD or asthma, where IL-33 biology is well known?" | That would be an external-evidence decision; none of our data support it (section 7). |
| "Is it safe in a viral indication?" | Our data raise a specific flag. IL-33 induces an endothelial **antiviral interferon-stimulated gene (ISG) programme** (IFIH1/MDA5, DDX58/RIG-I, MX1/2, OAS1/3, OASL, IFIT1–3, RSAD2/viperin, GBP1/4/5, HLA class I), and AX-1177 suppresses it (e.g. HGMEC 24 h: MX2 −3.8, RSAD2 −3.2, OASL −3.2 log2). This must be tested before any viral-indication study (Gate 2). |

---

## 4. Why not keep it as a viral-LRTD asset

1. **No human evidence that IL-33 drives disease.**
   - Tissue: no up-regulation (E7).
   - Serum: no IL-33 measurement delivered, and no IL-33-specific signature (E6).
   - Clinical association: prognostic only (E5).
2. **"Viral LRTD" is far broader than our evidence.** Every human data point is hospitalised, pre-vaccination SARS-CoV-2 infection. We have nothing on RSV, influenza or hMPV, outpatients, children, or the vaccinated era.
3. **The differentiating claim is untested.** The annex says AX-1177 binds reduced *and* oxidised IL-33, but only the reduced form was tested, and only on endothelium. Nothing in our package shows an advantage over blocking the receptor (ST2).
4. **A possible antiviral liability** (ISG suppression, section 3) weighs specifically against infection indications.

## 5. Why not drop outright

- The pharmacology is the strongest part of the package and it is clean (E1–E4).
- The decisive tests (section 6.5, Gates 0–1) reuse data and samples we already hold.
- The current package understates the asset in places: the pooled model hides the SELE, VCAM1, CXCL8 and CXCL1 effects, and the proteomics delivery omits IL-33.
- The holding cost for a preclinical asset on a time-boxed hold is small compared with the value of the information.

---

## 6. Forward view

### 6.1 What indication do our data actually point at?

**Not "viral LRTD" as a class, and not a new disease area.**

Three things line up in our data:
- the mechanism our data validate: IL-33-driven endothelial activation with a pro-coagulant switch (E1–E3);
- the only human setting with clinical data: hospitalised SARS-CoV-2 pneumonia;
- the signal that links them: a baseline profile of high sST2 plus endothelial activation and coagulation markers that predicts ICU admission, invasive ventilation or death independently of NEWS2.

Together they point to a **biomarker-defined subset of severe viral pneumonia: hospitalised, sST2-high patients with an endothelial-activation / thrombo-inflammatory phenotype.** This is a *narrowing* of the current indication, and so far it is shown only for SARS-CoV-2.

Our data do **not** support repurposing to COPD or asthma, type-2 airway disease, kidney disease or sepsis (section 7). The ISG finding means a non-infectious endothelial indication would avoid the antiviral liability, but we have no data in any such indication. That is a reason to keep the *mechanism* open, not a data-backed indication.

### 6.2 What the next studies must establish (decision-critical questions, in order)

1. **Is IL-33 present in the target patients, and in which form?** Measure free reduced IL-33, oxidised IL-33 and IL-33:sST2 complexes in the 100 enrolment sera, relate them to outcome and to sST2, and retrieve the withheld Olink IL-33 result.
2. **Do patients' sera contain endothelial-activating activity that AX-1177 neutralises?** This is the single most important experiment.
3. **Is the IL-33 endothelial programme active in diseased lung?** Test with the 22 archived lung RNAs, using pathology-verified groups and donor-level analysis.
4. **Which markers are specific to IL-33 rather than generic NF-κB?** Use TNF and IL-1β comparators, plus oxidised IL-33, to define IL-33-specific pharmacodynamic (PD) read-outs.
5. **Does AX-1177 weaken antiviral defence?** Measure ISG induction and viral replication with and without AX-1177.
6. **Does the prognostic signal generalise?** Test sST2 and the IL-33 marker set in non-COVID viral pneumonia and vaccinated-era cohorts.
7. **How potent is it?** Measure concentration–response (IC50) against both IL-33 forms, with and without pre-incubation. The biologics file, not delivered, holds affinity and potency data.

### 6.3 Biomarkers — proposed role, and which can go into patients

| Tier | Marker(s) | Why (our data) | Role | Into patients? |
|---|---|---|---|---|
| A | **sST2** | #2 of 1,063 proteins; OR 3.02/log unit; q = 0.009; adds to NEWS2; pathway-proximal | **Prognostic enrichment / stratification** at enrolment | **Yes, now**, as a stratification factor. Use as an *inclusion criterion* only after a cut-off is derived on a quantitative, validated assay. Not a PD or predictive marker. |
| A | **IL-6** | OR 2.14 (concordant on 4 panels); IL-33-induced +5.8 log2 and fully reversed | Prognostic covariate; exploratory PD | **Yes, now**, as a covariate or exploratory read-out. It is non-specific and cannot show IL-33 target engagement on its own. |
| B | **CCL20, IL-8 (CXCL8), tissue factor, MCP-1 (CCL2), OPG, sE-selectin**; PTX3 as covariate | IL-33-induced (+4 to +11 log2), ~100 % AX-1177-reversible at 6 h, reversed in HGMEC, *and* prognostic (q 0.012–0.049; sE-selectin p = 0.02, q = 0.09). sE-selectin is the most endothelium-restricted | **Exploratory PD** of IL-33-driven endothelial activity, read as a panel score | **Exploratory only, and only after Gate 1 shows IL-33 dependence in patient material.** Not for decisions. |
| C | **sVCAM-1, G-CSF, fractalkine (CX3CL1)** | Among the largest IL-33 effects (+8.3 to +8.7 log2), fully reversed, but *not* prognostic here | Sensitive PD read-outs | Exploratory only |
| D | **IL-33 itself**: free/total, reduced/oxidised, sST2-complexed | Not in the delivered data (absent from the delivered Inflammation panel; see section 8) | **Target engagement**, and potentially a mechanistic selection marker | **Not yet.** Needs assay development and Gate 0/1 data. |
| E | HGF, vWF, angiopoietin-2, GDF-15, uPAR | Strongly prognostic but **not** IL-33-responsive in vitro | Risk covariates only | Covariates; **not** AX-1177 PD markers |
| F | **ISG panel** (MX1, MX2, IFIT1, OASL, RSAD2) **plus viral load** | IL-33-induced ISGs are suppressed by AX-1177 | **Safety monitoring** | **Yes**, in any viral-indication study |
| ✗ | Tissue IL-33 IHC; eosinophil, basophil and mast-cell stains | Constitutive, at ceiling, post-mortem only; no link to IL-33 or COVID status | — | **No** |

Full numbers are in `tables/T1_biomarker_candidates.csv` and Figure 5.

![Figure 5](figures/fig5_biomarker_candidates.png)

### 6.4 Sampling timepoints

- **In patients — at enrolment (admission), before the first dose.** This is the *only* timepoint at which our data show prognostic value: serum was drawn at enrolment and predicted 30-day outcome independently of NEWS2. Enrolment is also when enrichment decisions are made. The in vitro kinetics argue for early sampling too: the IL-33 response is front-loaded.
- **In vitro and ex vivo assays — read out at 6 h.**
  - The IL-33 response peaks at 6 h: 4,031 vs 1,836 DE genes at 24 h; TNF and tissue factor are largely back to baseline by 24 h.
  - AX-1177's effect is cleanest at 6 h (101 % vs 84 %).
  - The HGMEC signal is largely gone by 24 h (1,460 → 269 genes).
  - Keep a **24 h** read-out only for the antiviral/ISG safety arm, because ISGs rise late (MX2 +2.1 → +3.7; GBP5 +2.3 → +4.7; IFI6 +0.2 → +1.7 log2).
- **On-treatment PD (proposal, to be validated):** pair the pre-dose sample with an early on-treatment sample (≈24 h) for the fast NF-κB outputs (CCL20, IL-8, IL-6, sE-selectin, tissue factor) and a later one (day 3–7) for sST2 and slower markers. In vivo kinetics are unknown; our data support only "early".

### 6.5 Plan, gates and pre-agreed kill criteria

| Gate | What | Uses | Go / kill |
|---|---|---|---|
| **0 — make the package decision-grade** (weeks, analysis only) | (a) Retrieve the 100 undelivered Olink assays (incl. IL-33), LOD/QC flags and patient-level data, then re-analyse per protein. (b) Re-fit transcriptomics per cell line from archived counts; extract IL-33 + isotype vs isotype for HUVEC and HGMEC. (c) Re-adjudicate IHC groups against autopsy reports, add a second blinded reader, analyse at donor level. (d) Pull the biologics file. | Archive | No kill decision; updates the priors for Gate 1 |
| **1 — is there neutralisable IL-33 activity in patients?** (≈3 months) | (a) Validated high-sensitivity IL-33 assays (free reduced, oxidised, sST2-complexed) on all 100 enrolment sera. (b) **Ex vivo bioassay:** enrolment sera (sST2-high events vs sST2-low non-events) on primary endothelium (HUVEC plus lung microvascular endothelial cells, ≥3 donors) with AX-1177 or isotype (pre-incubated); 6 h read-out of SELE, VCAM1, CCL20, CXCL8, CSF3, F3. (c) Targeted expression of the IL-33 endothelial score on the 22 archived lung RNAs, using verified groups. | Stored sera, archived RNA | **GO** (thresholds proposed; to be agreed *before* unblinding): AX-1177 cuts serum-induced endothelial activation by ≥50 % in a meaningful fraction (e.g. ≥25 %) of sST2-high sera, **and** at least one of: detectable IL-33 that tracks sST2 or outcome, or an enriched IL-33 programme in COVID+ lung injury. **KILL:** no AX-1177-reversible serum activity **and** no detectable IL-33. |
| **2 — specificity, differentiation, antiviral safety** (≈3–6 months, partly parallel to Gate 1) | TNF, IL-1β, oxidised IL-33 and viral-stimulus comparators ± AX-1177 (define IL-33-specific PD markers); oxidised-IL-33 / RAGE–EGFR assays in primary airway epithelium (not A549/MCF7); IC50 for both forms; ISG and viral-replication assays ± AX-1177 | New in vitro work | **KILL** or re-scope if AX-1177 impairs viral control at relevant concentrations. If no IL-33-specific PD marker exists, clinical PD must rely on IL-33 target engagement (Tier D). |
| **3 — development path** | Replicate sST2 enrichment in independent cohorts (non-COVID viral pneumonia, vaccinated era); then design an sST2-enriched patient study with Tier B/C PD and Tier F safety markers | External cohorts | Portfolio decision on indication and investment |

### 6.6 If the committee drops the asset: what we are dropping, and why

**What we are dropping:**
- a potent, clean IL-33 neutraliser, with in vitro proof that it fully blocks IL-33-driven endothelial inflammation, adhesion, myelopoiesis and the pro-coagulant switch in macro- and microvascular endothelium;
- the only indication our data point to: sST2-high, hospitalised viral pneumonia with endothelial activation, still a hypothesis and shown only for SARS-CoV-2.

**Why:**
1. No human evidence that IL-33 drives disease.
2. The prognostic signal is not IL-33-specific.
3. Tissue IL-33 is constitutive and not raised.
4. Every human data point is pre-vaccination COVID-19.
5. The dual-form differentiation is untested.
6. There is a plausible antiviral liability.

Record the archived resources (sera, lung RNA, counts, withheld assays) so the asset can be re-activated cheaply.

---

## 7. What I considered and ruled out

**Decision options**
- *Continue viral-LRTD development as planned.* Ruled out (section 4).
- *Drop now.* Considered; not recommended while Gate 0–1 is cheap and unrun. It becomes the right call if Gate 1 is unfunded or fails.
- *Repurpose to COPD or asthma (epithelial / type-2 IL-33 biology).* Ruled out **on our data**:
  - the epithelial lines were never stimulated with IL-33;
  - lung IL-33 does not differ by COPD (n = 11) or asthma (n = 6) status (p = 0.19–0.94);
  - eosinophil, basophil and mast-cell markers are unrelated to IL-33;
  - serum IL-4, IL-5, IL-13 and TSLP are not in the delivery.
- *Repurpose to kidney / glomerular disease.* Considered because HGMEC respond strongly (VCAM1 −11.7, SELE −8.7 log2 with AX-1177) and serum NGAL (LCN2, q = 0.03) and KIM-1 (p = 0.03, q = 0.10) track outcome. Ruled out as a data-supported indication: one donor's cells, no kidney-disease data. Hypothesis only.
- *Stand-alone thrombo-inflammation / coagulopathy indication.* Considered. It is consistent across all three datasets (tissue factor, PAI-1 and thrombomodulin in vitro; tissue factor, PAI-1, vWF and uPAR prognostic; thromboemboli 4/16 vs 0/15). It is folded into the sST2-high severe-pneumonia hypothesis, not stand-alone, because the evidence is COVID-only and the autopsy difference is not significant (p = 0.10).
- *Eosinophilic / type-2 disease.* Ruled out: no relationship between IL-33 and eosinophil markers; eosinophil markers do not differ by COVID status.
- *Non-viral ARDS or sepsis.* No data either way; cannot be claimed.

**Biomarkers ruled out, or limited to a lesser role**
- Tissue IL-33 IHC as a selection marker: constitutive, ceiling-limited, post-mortem only.
- HGF (top prognostic protein) as a PD marker: not IL-33-responsive.
- vWF and angiopoietin-2 as PD markers: not transcriptionally IL-33-driven. Note: both are released from stored granules (Weibel–Palade bodies), which a transcriptome cannot capture; Gate 2 can test release directly.
- sST2 as a PD marker: induction is unreliable (inflated SE; none in HGMEC). Kept for enrichment only.

**Interpretations I tested and rejected**
- *"AX-1177 has off-target activity"* — the antibody-alone hits are variance artefacts or low-count noise and are not reproducible (E4).
- *"The isotype control blunts the IL-33 response by 20–30 %"* — a whole-signature regression suggested this. For robust genes it is ~0 % at 6 h and 8 % at 24 h; the apparent effect was noise plus a shared-group artefact.
- *Measuring neutralisation against "IL-33 alone"* — biased, because that group also sits on the x-axis and shared noise produces a spurious negative correlation. I used the isotype-controlled contrast throughout.
- *"The 6 h sheet of mmc5 was truncated at Excel's 1,048,576-row limit"* — no. That is only the declared sheet dimension. Both sheets hold 629,040 rows (24 contrasts × 26,210 genes) and are identical.
- *Epithelial contamination of endothelial libraries* — checked; the median shift of epithelial marker sets is about 0.
- *Block-level IHC statistics, the delivered IHC group labels, counting duplicated Olink assays, and ranking by "OR per log unit"* — all replaced (section 8).

---

## 8. Data-integrity findings the committee should know about

Full log: `tables/T5_data_integrity_log.csv` (17 entries).

1. **Transcriptomics: a single pooled limma model across four cell types** gives every gene one variance.
   - For genes that differ between endothelium and epithelium, the implied standard errors are absurd: median 0.34, but >2 for 130 genes and up to 16,536.
   - Those genes include **SELE, VCAM1, CXCL8, CXCL1, CCL2, PTGS2, PTX3 and IL1RL1**, which are called "non-significant" despite 3- to 11-log2 induction. The reverse artefact produces spurious antibody-alone hits (Figure 2).
   - I relied on effect sizes and concordance, not the delivered adjusted p-values. **Action:** re-fit per cell line.

   ![Figure 2](figures/fig2_pooled_model_artefact.png)

2. **Serum: the delivered table is a filtered subset.**
   - The Benjamini–Hochberg adjustment used **1,194 tests**; only **1,094** were delivered. Back-calculation places at least **4 undelivered assays below the FDR-5 % threshold**.
   - The Inflammation panel is delivered with **77 of its 92 assays**. IL-33 (the drug target), IL-4, IL-5, IL-13 and TSLP are absent.
   - The annex says the adjustment was "across all assays in the delivery", which is contradicted.
   - 27 proteins sit on 2–4 panels and are counted separately: 178 "significant assays" are really 186–194 unique proteins once de-duplicated and re-adjusted.
   - **Action:** obtain the full output.

   ![Figure 3](figures/fig3_serum_prognostic_vs_IL33_programme.png)

3. **Lung IHC.**
   - Rows are blocks, not donors: three COVID+ donors supply 24 of the 49 COVID+ blocks.
   - 9 of 31 donor labels contradict the autopsy text (four "pneumonia" controls without pneumonia; three "non-pneumonia" controls with coccidioidomycosis, acute pneumonitis or organising pneumonia; two COVID+ donors without acute lung injury).
   - Numeric scores reach 5.5 on a 0–5 scale.
   - Donor-level fields are not reliably on the first block.
   - I analysed at donor level with rank statistics, with and without pathology-verified groups.

   ![Figure 4](figures/fig4_lung_IHC_donor_vs_block.png)

4. **Design limits** (not errors, but they bound every inference):
   - one donor per endothelial line;
   - reduced IL-33 only, at one antibody concentration (~41-fold molar excess) with no pre-incubation;
   - no IL-33 stimulation of the epithelial lines; MCF7 is a breast line, and DMSO is not an antibody vehicle;
   - the clinical cohort is one centre, pre-vaccination, SARS-CoV-2 only, with one timepoint.

---

## 9. Methods summary

- **Transcriptomics.** All 26 delivered contrasts were used, with 26,210 genes each. Implied SE was computed as |logFC/t|. Neutralisation was measured as −logFC(AX-1177 + IL-33 vs isotype + IL-33) / logFC(IL-33 vs vehicle) on IL-33-responsive genes (adj.P < 0.05, |logFC| > 1). The "robust" subset additionally required logFC > 2, AveExpr > 2 and median SE < 1. Hallmark enrichment used msigdbr 7.5.1 (hypergeometric test, BH correction). Ensembl IDs were re-annotated with org.Hs.eg.db 3.18.
- **Serum.** Olink assay names were mapped to HGNC symbols with a curated table (`code/olink_name_map.py`). Cross-panel duplicates were collapsed (keeping either the most or least significant assay as a sensitivity check) and BH was re-applied over 1,063 unique proteins. The BH denominator was recovered as adj.p × rank / p; undelivered assays were located from the gaps between implied and observed ranks. Proteins were called IL-33-inducible and AX-1177-reversible when their endothelial transcript rose >2-fold with IL-33 and AX-1177 reversed at least half of that rise at the same timepoint (HUVEC). Enrichment used Fisher's exact and one-sided Mann–Whitney tests on signed z.
- **IHC.** Donor-level medians across blocks; Mann–Whitney, Kruskal–Wallis and Spearman tests. Groups were re-verified from the delivered autopsy diagnoses (`code/ax1177_data.py`, `ACUTE_LUNG_PATHOLOGY`).
- **Software.** Python 3 (pandas, SciPy, statsmodels, matplotlib) and R (org.Hs.eg.db, msigdbr). Run order: `ax1177_analysis.py` → `ax1177_figures.py` → `ax1177_biomarkers.py` → `ax1177_integrity_log.py`.

### File index

| File | Content |
|---|---|
| `tables/T1_biomarker_candidates.csv` | Biomarker tiers, roles, in vitro and serum numbers |
| `tables/T2_serum_proteins_deduplicated_with_IL33_annotation.csv` | 1,063 unique proteins with de-duplicated q, panels and IL-33/AX-1177 transcript data |
| `tables/T2b_...enrichment...csv` | Test of IL-33 programme enrichment among prognostic proteins |
| `tables/T3a–T3f` | DE counts, neutralisation summary, antibody-alone contrasts, SE-inflated genes, canonical gene panel, Hallmark enrichment |
| `tables/T4, T4b, T4c` | Donor-level IHC with verified groups; group tests; IL-33 vs cell-marker correlations |
| `tables/T5_data_integrity_log.csv` | Data-integrity findings and requested actions |
| `tables/T6, T6b` | Undelivered-assay forensics; assays per panel |
| `tables/key_numbers.json` | Every number quoted in this brief |
| `figures/fig1–fig5` | Figures 1–5 |
