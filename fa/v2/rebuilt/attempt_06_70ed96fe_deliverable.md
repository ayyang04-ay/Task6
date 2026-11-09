# AX-1177 (anti-IL-33 IgG1; research code Compound_47): portfolio audit recommendation

**Scope.** This uses only the five files delivered: the methods annex, mmc2 (serum proteomics, n = 100), mmc3 (post-mortem lung IHC, 31 donors / 74 blocks), mmc4 (IL-33 vs vehicle in HUVEC) and mmc5 (all other in vitro contrasts). I re-analysed the data from those files. I did not bring in any outside efficacy data. Where I point to vendor panel content, I say so.

---

## 1. Decision

**Keep the molecule. Stop the viral-LRTD programme in its current form.**
I recommend putting AX-1177 on a gated hold for about 6 months. During that time only a low-cost validation package would be funded (Section 6), with kill criteria agreed in advance. If the gates are not met, drop the asset.

**Why not "keep as is".** Our data do not show that IL-33 is involved in viral LRTD:
- The target was never measured in patients. IL-33 is not among the delivered serum assays.
- Lung IL-33 does not differ between COVID-positive lungs, COVID-negative pneumonia and non-pneumonia lungs.
- The serum signal we do have is not specific to IL-33 (Section 3.2).

**Why not "drop now".** The molecule itself is clean and potent against the biology it targets (Section 3.1). There is one strong pathway-linked prognostic signal: sST2, ranked #2 of 1,094 proteins. Also, the three questions that would settle the case can mostly be answered with material we already own: archived counts, undelivered Olink assays, the existing 100 sera, and the RNA from the autopsy blocks. That makes one more information cycle cheap compared with what it could tell us.

**If the committee wants a binary answer for active development, the answer is drop.** Here is what we would be dropping, and why:

> *What:* a specific, potent IL-33 neutraliser. In vitro it blocks an IL-33-driven inflammatory and pro-coagulant programme in macro- and microvascular endothelium. It has no detectable IL-33-independent activity.
> *Why:* our data do not show IL-33 is elevated, released or causal in viral LRTD. The one clinical cohort is COVID-19 from the pre-vaccination period. Its prognostic markers rise with severity across the whole proteome, so they are not specific to IL-33. None of our data points convincingly to another indication.

---

## 2. Where the data point (the forward view)

**The biology:** IL-33 released from lung vasculature drives endothelial activation, both inflammatory and pro-coagulant. Nothing in our data makes this virus-specific.

**The population:** hospitalised patients with acute pneumonia or acute lung injury who are at risk of progressing to ICU, mechanical ventilation (IMV) or death, enriched by high sST2 at enrolment.

- **COVID-19 is the only population with patient-level serum evidence.** The narrowest statement the data support is therefore "hospitalised COVID-19 pneumonia, sST2-high at enrolment".
- **The autopsy data suggest the biology is pathogen-agnostic:**
  - IL-33, inflammatory infiltrates and eosinophil/neutrophil markers do not separate COVID-positive from COVID-negative pneumonia.
  - Endothelial IL-33 staining is lower wherever acute pneumonia or lung injury is present, whatever the cause (Section 3.3).
- **So the re-scoped hypothesis to test** is "severe pneumonia / acute lung injury with endothelial activation", not "viral LRTD".

**What our data do not point to:**

| Candidate indication | Verdict | Reason (from our data) |
|---|---|---|
| Viral LRTD broadly (RSV, influenza, hMPV) | Not supported | Zero non-COVID patients; the cohort is pre-vaccination COVID-19 only. |
| COPD / asthma / type-2 airway disease | Not supported | Serum type-2 markers do not predict outcome (IL-5 OR 1.00, eotaxin-1 1.08 / 0.98, eotaxin-2 0.92, TARC 0.85). Tissue eosinophil markers track pneumonia, not COVID or COPD. IL-33 IHC does not differ by COPD annotation (p = 0.21–0.59). No epithelial IL-33 experiment was done. |
| Renal (glomerular endothelium) | Not supported | HGMEC have no vehicle arm, so the IL-33 effect cannot be estimated there. The reversal seen in HGMEC is about half the HUVEC size. No renal clinical signal: cystatin C OR 1.39, p = 0.18; KIM-1 only nominal (p = 0.03 / 0.07, adj p ≥ 0.11). |
| Cardiac / vascular (sST2-driven) | Not supported | NT-proBNP and troponin I are not prognostic here (p = 0.05–0.17). |

---

## 3. The evidence

### 3.1 In vitro: AX-1177 blocks an IL-33 endothelial programme cleanly (Fig 1, 2, 5)

**The response is large.** IL-33red (30 ng/mL) vs vehicle in HUVEC at 6 h changed 4,031 genes (BH < 0.05), of which 1,068 moved by |log2FC| > 1. The programme is classic ST2/MyD88/NF-κB. The most robust effects (log2FC at 6 h):

| Group | Genes (log2FC) |
|---|---|
| Cytokines / growth factors | GM-CSF (CSF2, 10.3), G-CSF (CSF3, 8.3), TNF (7.9), IL-6 (5.8), IL-1α (4.6), IL-1β (3.6) |
| Chemokines | CXCL6 (9.4), CCL20 (9.2), CX3CL1 (8.4), CXCL3 (8.3), CXCL10 (6.9), CXCL2 (6.8) |
| Other | ICAM1 (6.0), OPG / TNFRSF11B (4.8) |
| Pro-coagulant switch | tissue factor F3 up (5.6, about 50-fold); thrombomodulin THBD down (−1.0) |

**AX-1177 removes it.** AX-1177 (10 µg/mL) was co-added with IL-33, and the comparison below is against the isotype control (NIP228) plus IL-33:
- 566 of the 1,068 IL-33-responsive genes were significantly reversed. Only 12 moved further in the IL-33 direction.
- For robustly induced, expressed genes (n = 74), median reversal was **99%**, and 89% were at least 75% reversed.
- The residual difference between "AX-1177 + IL-33" and vehicle was a median of 0.03 log2.
- Because an anti-IL-33 antibody cannot neutralise endotoxin or other contaminants, near-complete reversal also shows the 6 h response is IL-33-specific.

**The same programme is blocked in glomerular microvascular endothelium (HGMEC).**
- Reversal at 6 h: CSF2 −7.1, CSF3 −6.5, CXCL3 −6.7, CCL20 −5.6, IL-6 −2.9, F3 −3.3, THBD +0.95.
- Across HUVEC-responsive genes the HGMEC reversal is about 0.5× the HUVEC size (slope 0.50).

**The controls behave.**
- The isotype is inert in the presence of IL-33 (median |log2FC| 0.05; 1 of about 10,300 expressed genes above 1).
- AX-1177 alone produced 21–73 "hits" per contrast across four cell types, but **none replicate**: 0 genes reach BH < 0.05 with |log2FC| > 1 in the same direction in two or more of the eight isotype-controlled contrasts. The hits are low-count genes or micro-changes (log2FC 0.02–0.2) with artefactually small standard errors (e.g. AKR1C2 t = 169 at log2FC 0.11). There is no evidence of IL-33-independent activity.

**Timing.** 6 h is where the signal and its neutralisation are strongest (Fig 2):

| Measure | 6 h | 24 h |
|---|---|---|
| IL-33 vs vehicle, DE genes (HUVEC) | 4,031 | 1,836 |
| AX-1177 reversal, DE genes (HUVEC) | 4,239 | 1,160 |
| AX-1177 reversal, DE genes (HGMEC) | 1,460 | 269 |
| Median log2FC, same 265 robustly induced genes | 2.9 | 1.1 (only 40% still significant) |
| Median neutralisation of expressed induced genes | 99% | 73% |

- At 24 h a few late interferon-type genes are not reversed (e.g. CXCL10 residual +2.4 log2).
- Several transcripts are transient: TNF, F3 and CCL7 are largely gone by 24 h.

**Limits of this evidence:**
- One concentration only, at about a 41-fold molar excess of IgG over IL-33. No potency/IC50 is available (affinity data are held in the biologics file).
- Antibody was co-added with IL-33 with no pre-incubation, which is a prophylactic paradigm. Reversal of already-established activation was not tested.
- Only the reduced form of IL-33 was tested, although the annex claims the antibody binds both forms.
- One donor per primary cell type, at different passages (HUVEC P2, HGMEC P5).
- No lung microvascular endothelium, no functional read-outs, no in vivo data.
- The epithelial lines were never given IL-33. MCF7 is a breast line, and DMSO is not an antibody vehicle. So our data contain no epithelial IL-33 biology.

**Possible liability in viral disease.** IL-33 also induced antiviral / interferon-stimulated genes in endothelium, and AX-1177 blocked them:

| Gene | IL-33 effect at 6 h (log2FC) | AX-1177 reversal |
|---|---|---|
| IFIH1 | +2.4 | −2.3 |
| DDX58 | +1.6 | −1.6 |
| IFIT1 / IFIT2 / IFIT3 | about +1.7 to +1.9 | reversed |
| MX1 | +1.9 | reversed |
| RSAD2 | +2.0 | reversed |
| OASL | +3.4 | reversed |
| CXCL10 | +6.9 | reversed |

Any viral-LRTD development would need antiviral-safety monitoring, such as viral load.

### 3.2 Clinical serum proteomics: sST2 is a strong prognostic marker, but the signal is not specific to IL-33 (Fig 3)

**Cohort.** 100 hospitalised COVID-19 patients, pre-vaccination, single centre, serum at enrolment. Endpoint: ICU, IMV or death within 30 days. The undocumented endpoint columns imply 56 non-events and 44 events.

**What supports the pathway:**
- **sST2**, the IL-33 decoy receptor and the only IL-33-axis analyte delivered, ranks **#2 of 1,094**: OR 3.02 per log unit (95% CI 1.83–5.01), BH-adjusted p = 0.0075, adjusted for age, sex and NEWS2.
- This is a genuine outlier even after allowing for the global shift described below: z = 4.30 against a median z of 1.38 across all assays (SD 1.33).
- Proteins that IL-33 induces in endothelium and AX-1177 reverses are also prognostic:

| Protein | OR per log unit (95% CI) | BH-adjusted p | Note |
|---|---|---|---|
| IL-6 | 2.07–2.31 | 0.012–0.019 | Replicated on four panels |
| OPG | 6.77 and 4.40 | 0.014, 0.020 | Two panels |
| CCL20 | 1.83 (1.28–2.61) | 0.020 | |
| CCL7 / MCP-3 | 1.72 | 0.020 | |
| IL-1β | 2.45 | 0.046 | |
| IL-18R1 | 6.07 | 0.018 | |
| Tissue factor | 3.02 | 0.051 | Nominal p = 0.009 |

**What undercuts the pathway:**
- **The whole proteome shifts with severity.** 82% of all assays have OR > 1, the median z is +1.38, and 176 of the 178 BH-significant assays are positive. An association with outcome is the default in this cohort, not a sign of IL-33 biology. The cause could be biological (necrosis, myeloid activation) or pre-analytical / plate-related. It has not been excluded, because plate layout and handling times are not in the annex.
- **No enrichment for the IL-33 programme.** The 65 serum proteins that IL-33 induces and AX-1177 reverses in vitro are no more likely to be prognostic than other proteins: 20% vs 17% significant (Fisher OR 1.22, p = 0.32); median z 1.53 vs 1.41 (Mann–Whitney p = 0.17).
- **Several of the most strongly induced proteins are not prognostic at all:**

| Protein | OR per log unit |
|---|---|
| CXCL6 | 1.02 |
| CXCL5 | 1.17 |
| G-CSF | 1.25 |
| CXCL10 | 1.30 |
| CCL5 | 0.89 |
| TNFRSF9 | 1.09 |
| CX3CL1 | 1.99 (p = 0.054) |

- **The top prognostic markers are not IL-33-driven in vitro.**
  - HGF (#1) and ANGPT2 are not induced by IL-33.
  - PTX3 and vWF cannot be assessed, because their in vitro standard errors are corrupted (Section 5).
  - The remaining top markers are mostly myeloid/neutrophil activation (CLEC5A, FCAR, OSM, IL-1R2, PRTN3, CD177) and cell-injury proteins.
- **sST2 is ambiguous as an IL-33 marker.** It is a generic stress/injury marker. As a decoy receptor, high levels could also mean less free IL-33.
- **IL-33 itself is missing.** The delivered adjusted p-values are exactly p × 1,194 / rank at several ranks (ranks 1, 3, 13, 14, 18, 22, 24). So BH was run over about 1,194 assays, but only 1,094 were delivered. The Inflammation panel arrived with 77 of 92 assays; per vendor content that panel includes IL-33.
- The undelivered assays do not include any of the top 24 associations.

### 3.3 Post-mortem lung IHC: the target is present everywhere, not specific to COVID (Fig 4)

**The analysis has to be done per donor.** There are 1–8 blocks per donor, and donor-level fields sit on the first block only. Analysing blocks as if they were independent creates false positives. For example, IL-5Rα in COVID-positive vs COVID-negative pneumonia gives p = 0.025 by block but p = 0.49 by donor.

**IL-33 is at or near the top of the scale in every group.** Donor-level medians:

| Compartment | Non-pneumonia | COVID-neg pneumonia | COVID-pos pneumonia | Kruskal–Wallis p |
|---|---|---|---|---|
| Endothelium | 5.5 | 5.5 | 4.8 | 0.11 |
| Basal epithelium | 4.9 | 4.5 | 4.25 | 0.65 |
| Vascular smooth muscle | 3.5 | 3.25 | 2.4 | 0.16 |

There is no COVID-specific increase; if anything the trend is lower in COVID-positive lungs.

**Eosinophil and neutrophil markers** (EDN, MBP, IL-5Rα, neutrophil elastase) are higher in pneumonia than non-pneumonia (p = 0.004–0.009). They are identical between COVID-positive and COVID-negative pneumonia (p = 0.44–1.0).

**The group labels conflict with the autopsy diagnoses for 9 of 31 donors:**
- Four "COVID-neg pneumonia" donors have no pneumonia in their autopsy diagnoses.
- Three "non-pneumonia" donors have acute pneumonia, pneumonitis or coccidioidomycosis.
- Two COVID-positive donors have only chronic changes.

**Sensitivity analysis using the autopsy diagnoses:**
- Endothelial IL-33 is lower with acute pneumonia/ALI (median 4.9 vs 5.5, p = 0.028; n = 23 vs 8).
- Endothelial IL-33 correlates inversely with neutrophil elastase (rho −0.43, p = 0.016; within-group rho −0.30, p = 0.10).
- This fits alarmin release during acute lung injury of any cause. It is hypothesis-generating only: a single reader, ordinal scores that exceed the stated 0–5 scale, and post-mortem tissue.

---

## 4. Biomarkers: what could go into patients, and in what role

| Marker | What our data show | Proposed role | Ready for patients? |
|---|---|---|---|
| **sST2** (serum) | #2 of 1,094 prognostic; NEWS2-adjusted OR 3.0 (1.8–5.0) | **Prognostic enrichment / stratification at enrolment.** Not a PD marker: IL-33 induction of IL1RL1 could not be assessed, and drug–IL-33 complexes may alter sST2 binding. Not predictive until a randomised test is done. | **Yes** (established immunoassays), as enrichment only. |
| **IL-6** (serum) | Prognostic on 4 panels (OR 2.1–2.3). About 57× induced at 6 h and 7× at 24 h in HUVEC; fully reversed; reversed in HGMEC | Stratification covariate plus a **secondary, non-specific PD** marker. It will also move with steroids or IL-6 blockade, so record concomitant medication. | **Yes** |
| **CCL20** (serum) | Prognostic (OR 1.83, adj p 0.02). Induced about 590× at 6 h and 48× at 24 h; reversed in HUVEC at both times and in HGMEC at 6 h | **Primary exploratory PD marker.** It is the best IL-33-linked serum protein available to us. | After analytical validation of a quantitative assay. |
| **OPG** (TNFRSF11B) | Prognostic on 2 panels; induced 28× (6 h) and 5× (24 h); reversed | Exploratory PD (panel with CCL20) | After validation |
| CCL7, IL-1β, CSF-1, IL-18R1 | Prognostic; induced and reversed at 6 h. CCL7 and CSF-1 are mostly gone by 24 h | Exploratory PD panel; requires early sampling | Research use |
| **Free and total IL-33** (serum / BAL) | **Not in the delivery** | **Target engagement** (free falls, total rises as drug–target complexes form). Also the candidate selection marker. | Only after assay development and validation (Gate B). It is the key missing marker. |
| GM-CSF (CSF2) | Largest and most completely reversed transcript (+10.3 / −12.2 log2). Not on the delivered panels | PD readout in in vitro / ex vivo assays | Patients only if a serum assay detects it |
| Tissue factor / thrombomodulin | F3 up about 50×, THBD down 2× by IL-33, both reversed. Serum TF borderline prognostic (adj p 0.051); soluble TM is not (p = 0.20) | Mechanistic exploratory (immunothrombosis) | Not yet |
| HGF, PTX3, vWF, ANGPT2 | Prognostic, but not IL-33-driven in vitro (HGF, ANGPT2) or not assessable (PTX3, vWF) | Prognostic covariates only; **not PD** | As covariates |
| E-selectin, VCAM-1, ICAM-1, IL-8, MCP-1 | Large in vitro point estimates, but uninterpretable statistics. Serum VCAM-1 (p = 0.43) and ICAM-1 (p = 0.11) are not prognostic | None until the counts are re-analysed | No |
| IL-33 IHC | At ceiling, no group difference, post-mortem, single reader | Tissue research only | No |
| Eosinophil / type-2 markers | Not prognostic; tissue eosinophils reflect pneumonia generally | None | No |
| **Viral load, ISGs** | IL-33 induces endothelial ISGs; AX-1177 blocks them | **Safety** monitoring in any viral-LRTD study | Yes (viral load) |

**Sampling timepoints.**
- **Selection / stratification:** at enrolment, before dosing. This is the timepoint at which the cohort showed prognostic value.
- **PD, in vitro and ex vivo:** 6 h after IL-33 exposure is the primary read, with 24 h secondary. 6 h holds about 2× more signal than 24 h and neutralisation is about 99% vs 73% complete. TNF, F3 and CCL7 are largely gone by 24 h.
- **PD, in patients:** sample before dosing, then within 24 h after dosing, then at 72 h. Late-only sampling (day 7 or later) would miss an early, transient IL-33 programme.
- The clinical cohort has one timepoint only. The actual in-patient window must first be defined by serial sampling in the observational study (Gate D).

---

## 5. Data-integrity findings the committee should know about

These do not change the direction of the conclusions. They do mean some tempting claims are not available. The full log is in `tables/data_issues_log.csv`.

**In vitro statistics**
1. **mmc5 "6h" and "24h" sheets are identical.** Each contains all 24 contrasts at both timepoints. Concatenating them double-counts everything; I de-duplicated.
2. **The single pooled model gives implausible standard errors.**
   - About 370 genes have standard errors at least 3× (174 at least 10×) the median for genes of similar expression, and these are concentrated in genes that differ between cell types. Examples: E-selectin, VCAM-1, IL-8, MCP-1, CXCL1, PTX3, IL1RL1 (ST2), vWF, CD93, and even GAPDH (SE about 9 log2).
   - A few genes have implausibly small standard errors (DYNC1H1 log2FC −0.18 with t = −16).
   - Cell-type marker genes do not shift between arms, so this is not a sample swap; it is a problem with how the variance was pooled.
   - Consequence: "E-selectin/VCAM-1 not significant" is uninformative, not negative. The count matrices in the archive should be re-fit per cell line.
3. **HGMEC has no vehicle arm.** The IL-33 effect there cannot be estimated; only the AX-1177 reversal can.
4. **AveExpr is averaged over all 114 libraries**, including the epithelial lines. It understates endothelial genes (for example, GM-CSF's AveExpr is −3.2).

**Serum proteomics**

5. ORs are "per log unit" with no base stated; NPX is already log2, so this may be a double transform. Per-unit ORs are not comparable across assays (CSF-1 OR 90, SPON2 OR 93 reflect narrow-range assays). I ranked on z instead.
6. 27 proteins appear on more than one panel (57 assays), e.g. IL-6 ×4, HGF ×2, OPG ×2. They are counted as independent tests, although their cross-panel agreement is good.
7. The endpoint columns `composite_endpoint_0/1` are undefined in the annex; they look like per-group missing fractions. BH was run over about 1,194 assays, not the 1,094 delivered.
8. Adjustment covers age, sex and NEWS2 only. Renal function, steroid or tocilizumab use, and time from symptom onset are not included, and no discrimination statistics (AUC) are reported.

**Post-mortem IHC**

9. Pseudo-replication across blocks. Some donor fields are not on the first block (notes for donors 2040 and 2045; donor 1159 is listed 1B before 1A).
10. Scores go up to 5.5 on a stated 0–5 scale, and the IL-33 encoding is undocumented.
11. SARS-CoV-2 status is missing for donor 1905.
12. The "non-pneumonia" controls have chronic lung disease.
13. Group labels conflict with the pathology for 9 of 31 donors.
14. Tissue RNA exists for a subset of blocks but was not delivered.

---

## 6. Plan: what the next studies must establish, with gates

| Gate | Question that must be answered | Study (material) | Go / kill |
|---|---|---|---|
| **A: Data remediation** (0–8 wk, no new wet lab) | Do the core findings survive correct analysis? | (1) Re-fit archived counts per cell line; confirm E-selectin, VCAM-1, IL-8, MCP-1, ICAM-1, IL1RL1 and the 6 h reversal. (2) Obtain the ~100 undelivered Olink assays, including IL-33 with LOD flags, plus patient-level data. Re-express ORs per SD; adjust for eGFR, steroids and plate; report AUC / NRI beyond NEWS2. (3) Pathologist adjudication of IHC categories; blinded second reader. | **Kill** if sST2's association disappears after renal / plate adjustment **and** the core IL-33 programme fails to replicate. |
| **B: Is the target in the disease?** (2–4 mo, existing samples) | Is IL-33 released in hospitalised pneumonia, and does it track progression? | (1) Validated high-sensitivity **free and total IL-33** in the 100 enrolment sera; relate to outcome, sST2, IL-6 and CCL20. (2) RNA from the autopsy blocks: IL-33 endothelial signature (CSF2, CCL20, IL6, F3, CXCL2/3, NFKBIA; THBD) in acute pneumonia vs none, and versus loss of endothelial IL-33 IHC. | **Go** if IL-33 is detectable in a meaningful fraction of patients and associated with progression independent of NEWS2, **or** the endothelial signature is raised in acute-injury lungs. **Kill** if neither. |
| **C: Is the pharmacology therapeutic?** (3–6 mo, in parallel) | Does AX-1177 reverse *established* activation at achievable concentrations without harming antiviral defence? | Primary lung microvascular endothelium (≥3 donors) plus HUVEC. IL-33red and IL-33ox. AX-1177 dose–response, added at 0, +1, +3 and +6 h. Primary read-out at **6 h**, secondary at 24 h: CSF2, CCL20, IL6, F3, THBD, SELE / VCAM1 mRNA; secreted GM-CSF, IL-6, CCL20; TF activity; permeability. Controls: ST2 blockade, heat-inactivated IL-33, endotoxin. Airway-epithelium ALI cultures infected with RSV, influenza or SARS-CoV-2 ± AX-1177: IL-33 release, viral titre, ISGs. | **Go** if ≥50% inhibition when added ≥3 h after IL-33 at clinically plausible concentrations, with no increase in viral replication. |
| **D: Who and when?** (only if A–C pass) | Is IL-33-axis activation virus-specific or pathogen-agnostic, and when does it peak? | Prospective observational cohort of hospitalised LRTD: RSV, influenza, vaccinated-era COVID-19, with bacterial CAP as comparator. Serial samples at enrolment, 24 h, 72 h and day 7: free / total IL-33, sST2, IL-6, CCL20, OPG. Outcome: ICU, IMV or death at 30 days. | Defines the indication label (viral vs all-cause severe pneumonia / ALI), the enrichment cut-off, and the PD window for first-in-patient work. |

**Decision point at about 6 months.** Gates A–C decide whether the asset re-enters active development under the re-scoped hypothesis or is dropped.

---

## 7. What I considered and ruled out

| Considered | Outcome | Why |
|---|---|---|
| Treating mmc5 sheets as 6 h and 24 h sets | Ruled out | The sheets are identical in content. |
| Claiming E-selectin, VCAM-1, IL-8 or MCP-1 induction or reversal as evidence | Ruled out for now | Point estimates are large and mirror-consistent, but the delivered standard errors are invalid. Needs re-fit. |
| Claiming AX-1177 off-target activity from the antibody-only contrasts | Ruled out | Zero replicated genes; the hits are low-count noise or artefactual-SE micro-changes. |
| Sample swap as the cause of the standard-error anomalies | Ruled out | No shift in cell-type marker genes between arms. |
| IL-33 effect in glomerular endothelium vs baseline | Not estimable | There is no HGMEC vehicle arm. |
| Epithelial IL-33 biology (A549 / MCF7; RAGE / EGFR; oxidised IL-33) | Not testable | The epithelial lines were never stimulated, and IL-33ox was never tested. |
| Ranking serum markers by OR | Ruled out | Per-log-unit ORs are on assay-specific scales; I used z / p. |
| Treating the 1,094 assays as 1,094 proteins | Ruled out | There are 27 cross-panel duplicates. |
| sST2 as a PD or predictive marker | Ruled out (now) | IL-33 induction could not be assessed; it is a decoy; no treatment data. Kept as **prognostic enrichment**. |
| HGF (#1 prognostic) as an IL-33 PD marker | Ruled out | Not induced by IL-33 in endothelium. |
| "The IL-33 programme explains severity" | Not supported | No enrichment (p = 0.32) against a proteome-wide shift. |
| Block-level IHC statistics | Ruled out | Pseudo-replication; for example, IL-5Rα p = 0.025 by block becomes 0.49 by donor. |
| "IL-33 is up-regulated in COVID-19 lungs" | Not supported | No group difference; the trend is lower. |
| Eosinophilic / type-2 repurposing (asthma, COPD) | Not supported by our data | Not prognostic in serum; tissue eosinophils are pneumonia-related, not COVID- or COPD-related. |
| Renal repurposing from HGMEC | Not supported | No baseline arm, no renal clinical signal. |
| Broad viral-LRTD label | Not supported | COVID-only, pre-vaccination cohort. |
| Endotoxin contamination as the source of the in vitro response | Largely excluded at 6 h | About 99% reversal by an anti-IL-33 antibody. The residual at 24 h (e.g. CXCL10) warrants controls in Gate C. |
| IL-33 IHC as a patient-selection marker | Ruled out | Ceiling effect, post-mortem only, single reader. |

---

## 8. Likely committee challenges, and answers

- **"sST2 is #2 of 1,094; isn't that enough?"**
  It shows the IL-33/ST2 axis tracks severity. It does not show that IL-33 drives severity:
  - 82% of all proteins rise with severity.
  - sST2 is produced by many stressed tissues.
  - As a decoy receptor, high sST2 may even lower free IL-33.
  - We have no IL-33 measurement.
- **"Go straight to a phase 2 in hospitalised COVID-19?"**
  Not on this evidence:
  - The cohort is pre-vaccination.
  - The efficacy paradigm is prophylactic co-addition only.
  - There is no target-engagement assay.
  - There is an open antiviral-safety question.
- **"Why not drop it outright?"**
  The molecule is clean, and Gates A–B mostly re-use material we already own. One inexpensive cycle either confirms the target is in the disease or ends the asset with a documented, data-based reason.
- **"Could it be repurposed to COPD or asthma?"**
  Not on our data. That would be a new bet based on external evidence and would need new data of its own.

---

### Files

| File | Contents |
|---|---|
| `AX-1177_portfolio_recommendation.md` / `.html` | This memo (HTML has the figures embedded) |
| `figures/Fig1–Fig5` | In vitro response and reversal; 6 h vs 24 h; serum proteomics; donor-level IHC; QC of delivered statistics |
| `tables/olink_vs_invitro_integrated.csv` | All 1,094 assays joined to in vitro IL-33 and AX-1177 effects |
| `tables/IL33_endothelial_programme_HUVEC_HGMEC.csv` | IL-33-responsive genes with reversal percentages and SE-anomaly flags |
| `tables/IHC_donor_level.csv` | Donor-level scores and label–pathology concordance |
| `tables/biomarker_candidates.csv` | The Section 4 table |
| `tables/data_issues_log.csv` | Every data-integrity issue, its impact and the remedy |
| `analysis_methods.md` | How each number was derived |
