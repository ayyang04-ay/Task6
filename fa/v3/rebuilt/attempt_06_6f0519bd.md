# AX-1177 (anti-IL-33 IgG1) — Portfolio audit position

**Evidence base:** the delivered AX-1177 package only. That covers the methods annex, the endothelial and epithelial RNA-seq contrasts (mmc4/mmc5; 114 libraries), Olink serum proteomics from 100 hospitalised COVID-19 patients (mmc2), and post-mortem lung IHC (mmc3; 31 donors, 74 blocks). Compound_47 = AX-1177; NIP228 = isotype control. All numbers below were recomputed from these files. Full tables are in *AX-1177_supporting_tables.xlsx*, and the code is in *code/*.

---

## 1. Recommendation

**KEEP AX-1177, re-scoped and gated. Do not keep it as the current viral-LRTD programme.**

- **Re-scope:** an endothelium-directed, host-response therapy for **hospitalised pneumonia at risk of progression to ICU, invasive ventilation or death. The indication is pathogen-agnostic and enriched by high serum sST2 at admission.** The premise that the asset is specific to *viral* LRTD is not supported by our data.
- **Fund now:** Gates 0–1 only (Section 6.4). These consist mostly of re-analysing data, and testing material, that we already hold. No in vivo or clinical spend until Gates 0–2 are passed.
- **Kill criteria, written in advance:**
  - lung microvascular endothelium does not respond to IL-33;
  - the AX-1177-reversible IL-33 response signature is absent from pneumonia lung tissue;
  - sST2 is not prognostic outside COVID-19.

**The case in four lines**

1. **The mechanism is real and AX-1177 shuts it off.** IL-33 switches human endothelium into an inflammatory, neutrophil-recruiting, pro-coagulant state:
   - up: GM-CSF, G-CSF, IL-6, TNF, CXCL1/2/3/5/6/8, CCL20, E-selectin, VCAM-1, ICAM-1 and tissue factor;
   - down: thrombomodulin.

   Against isotype control, AX-1177 blocks a median **98 %** of the induced response at 6 h (557 genes) and **85 %** at 24 h.
2. **It is clean.** Without IL-33, AX-1177 moves nothing coherent in four cell types. There is no agonism, no endotoxin-like signal and no off-target program.
3. **The pathway is engaged in patients who deteriorate.** Soluble ST2 (sST2), the IL-33 decoy receptor, ranks **#2 of 1,094** serum proteins for ICU, invasive ventilation or death within 30 days. The odds ratio is 3.0 (95 % CI 1.8–5.0) per log unit, q = 0.0075, adjusted for age, sex and NEWS2. Proteins from the AX-1177-reversible endothelial program also predict deterioration: IL-6, CCL20, OPG, IL-18R1, IL-1β, MCP-3 and IL-8 (all q < 0.05).
4. **Our data do not support the viral-LRTD premise.**
   - Lung IL-33 is not associated with COVID-19, pneumonia or diffuse alveolar damage under any classification.
   - Fatal COVID-19 lungs are mostly *mixed* pneumonias: 9/16 carry bacterial-pattern bronchopneumonia, and only 7/16 show diffuse alveolar damage.
   - 82 % of *all* 1,094 serum proteins have an odds ratio above 1 for deterioration, so the serum link is not IL-33-specific.
   - Serum IL-33 itself is missing from the delivery.

---

## 2. What our data show: evidence map

| Claim | Data | Key result | Strength | Main caveat |
|---|---|---|---|---|
| IL-33 activates human endothelium | mmc4 (HUVEC) | 645 genes induced more than 2-fold at 6 h (q<0.05). Top hits (log2FC): CSF2 +10.3, CXCL6 +9.4, CCL20 +9.2, CX3CL1 +8.4, CSF3 +8.3, TNF +7.9 | Strong | Single donor; umbilical vein; one IL-33 concentration |
| AX-1177 neutralises the response | mmc4 + mmc5 | Median inhibition 98 % at 6 h (IQR 78–104 %) and 85 % at 24 h (IQR 45–102 %), vs isotype+IL-33 | Strong (effect sizes in independent arms) | One antibody concentration; added at the same time as IL-33 |
| Microvascular endothelium responds too | mmc5 (HGMEC) | The same genes are reversed at 6 h at about half the HUVEC magnitude; little effect at 24 h | Moderate | No HGMEC vehicle arm; glomerular, not lung |
| AX-1177 is inert without IL-33 | mmc5 (4 cell types, 8 conditions) | Top-100 IL-33 genes unchanged (median ≤0.18 log2, vs 4.5 for IL-33). 92 % of the 632 nominal "hits" are low-count noise or SE artefacts | Strong | n = 3 per arm |
| IL-33 axis tracks deterioration | mmc2 | sST2 ranks #2/1,094 (OR 3.0, q = 0.0075). IL-18R1 (#25) and IL-1R2 (#27) are also near the top | Moderate | Single centre; pre-vaccination COVID only; sST2 is not IL-33-specific |
| AX-1177-reversible proteins track deterioration | mmc2 × mmc4/5 | IL-6 (4 concordant assays, OR 2.1–2.3), CCL20 1.8, OPG 6.8, IL-18R1 6.1, IL-1β 2.4, MCP-3 1.7, IL-8 2.2; all q < 0.05 | Moderate | Not enriched beyond the global severity shift (Fisher p = 0.74) |
| IL-33 is abundant in lung vasculature | mmc3 | Endothelial IL-33 sits at the top of the scale in 39/74 blocks, in every group | Moderate | Ceiling effect; single reader |
| Lung IL-33 is **not** disease-specific | mmc3 | No association with COVID status, pneumonia (delivered labels or autopsy diagnoses), DAD, or within accession batch (all p ≥ 0.08). For endothelium, COVID+ minus COVID− = −0.19 (95 % CI −1.00 to 0.00) | Moderate: robust to every classification (31 donors) | Expression is not release |
| Granulocyte differences between groups | mmc3 | By delivered labels, EDN, MBP and neutrophil elastase are higher in "pneumonia" (p 0.004–0.014). By **autopsy diagnosis**, eosinophil proteins are *lower* in acute pneumonia (EDN p = 0.043, MBP p = 0.023). Within accession batch, nothing is significant | **Not interpretable** | Labels disagree with autopsy in 9/31 donors; groups are nested in staining batches (MBP batch p = 0.0007) |

## 3. What our data do not show

These are the gaps the committee will find.

- **Disease relevance:** nothing shows that IL-33 is up, released or active in *viral* (vs bacterial) pneumonia. Tissue staining cannot measure release.
- **Circulating IL-33:** IL-33 is part of the Olink Inflammation panel that was run, but it is absent from the delivered table. It is one of 100 assays that were adjusted for but not delivered (Section 8). So we cannot say whether sST2-high patients carry free, active IL-33 or IL-33 that sST2 has already sequestered.
- **Lung-relevant cells:** there is no lung microvascular endothelium and no primary airway epithelium. The epithelial lines (A549, and MCF7, which is a breast line) were never given IL-33.
- **Potency and timing:** only one antibody concentration was tested (~41-fold molar excess over IL-33), added at the same time as IL-33. There is no IC50, no time-of-addition data and no oxidised IL-33 test. The annex's dual-form binding claim is untested in this dataset.
- **In vivo:** no efficacy and no PK/PD. The primary cells come from a single donor.
- **Serum cohort:** 100 patients, single centre, pre-vaccination COVID-19 only. Enrolment timing relative to admission is not recorded.

---

## 4. Anticipated challenges and answers

**"IL-33 isn't even up in COVID lungs. Why keep it?"**
Agreed, and that is why we are not asking to keep it as a COVID or viral asset. IL-33 is a pre-stored nuclear alarmin, so its activity depends on release rather than expression. The substrate is present wherever tissue is injured: lung endothelium and basal epithelium are IL-33-positive in every donor, with donor means of 2.75–5.5 and endothelium at the top of the scale in 39/74 blocks. Whether IL-33 is released and active in pneumonia is exactly what Gate 1 (IL-33 response signature in archived lung RNA) and Gate 2 (circulating IL-33 and IL-33:sST2 complexes) test. Endothelial IL-33 staining is lower where neutrophil elastase is higher (ρ = −0.43, p = 0.016), and this holds after age adjustment (partial ρ = −0.43, p = 0.015). It does not hold after adjusting for staining batch (p = 0.12). So it stays a hypothesis to test, not evidence.

**"sST2 rises in every sick patient. Isn't it just a severity marker?"**
Partly, yes. 82 % of all serum proteins have an odds ratio above 1 for deterioration, and the AX-1177-reversible program is not enriched beyond that. Even so, sST2 ranks #2 against that background and independently of NEWS2. That makes it useful for **enrichment**: it raises the event rate and trial power. It does not prove that IL-33 drives disease. We will use it as a prognostic enrichment marker, not a predictive one, until a randomised trial shows a treatment-by-sST2 interaction.

**"High sST2 means IL-33 is already sequestered, so the antibody is redundant."**
Our data cannot answer this, because IL-33 was not delivered. It is a genuine risk. Gate 2 addresses it directly with free IL-33 and IL-33:sST2 complex assays.

**"4,000 DEGs is overwhelming evidence."**
We do not rely on that number. The strongly "repressed" genes (423 with a >2-fold decrease) are mostly low-count lncRNAs and pseudogenes. The isotype "restores" them almost as much as AX-1177 does (only 30 % are reversed vs isotype+IL-33), so they are an artefact of the IL-33-alone arm. The robust signal is the ~650 strongly *induced* genes. Those are what AX-1177 blocks: 81 % of all 2,191 induced genes are significantly reversed vs isotype+IL-33.

**"The RNA-seq statistics are flawed."**
Yes. A single voom model across four unrelated cell types produced implausible standard errors for 130 genes, including SELE, VCAM1, CXCL8, CXCL1, CCL2 and IL1RL1. Our neutralisation conclusion does not use those p-values. It rests on effect sizes across independent arms (IL-33 vs vehicle; AX-1177+IL-33 vs isotype+IL-33), which agree closely: for example, SELE +11.2 vs −11.0 and VCAM1 +8.7 vs −8.8 log2. Gate 0 re-fits the data per cell line from the archived counts.

**"Why not pivot to COPD or asthma, where anti-IL-33 has external validation?"**
Our data say nothing about airway epithelium. No epithelial cell was stimulated with IL-33. In tissue, a history of COPD or asthma had no relationship with IL-33 (p ≥ 0.21), and type-2 serum markers are null or were not delivered. A COPD pivot would rest entirely on external evidence and need a new package from scratch.

**"The endothelial cells are umbilical vein and glomerulus, not lung."**
Correct. The glomerular (microvascular) response was about half that of HUVEC at 6 h and had faded by 24 h. Lung microvascular endothelium is therefore the first Gate 1 experiment, and no response means we kill the asset.

**"The antibody was added together with IL-33. In patients, IL-33 is already out."**
Correct. Block was 98 % at 6 h when added together, but some genes escape by 24 h: interferon-stimulated genes such as CXCL10 and MX2 are only 40–50 % inhibited. That looks like a secondary cascade. It argues for treating early, at admission, and makes time-of-addition a Gate 1 go/no-go experiment.

**"Is it safe to block IL-33 in a viral infection?"**
IL-33 induces about 20 interferon-stimulated genes in endothelium, and AX-1177 blocks them (median 92 % at 6 h). Viral load kinetics must therefore be a safety biomarker in any trial that enrols viral cases.

---

## 5. If we drop it: what we are dropping and why

**What we drop.** A selective IL-33 neutraliser with three things going for it:
- near-complete in vitro blockade of IL-33-driven endothelial activation (inflammatory, neutrophil-recruiting, pro-coagulant);
- no detectable activity on its own;
- a human biomarker (sST2) linked to progression in hospitalised viral pneumonia.

**Why we would drop it.**
- Its disease rationale (IL-33 up in viral LRTD) is not supported by our own tissue data.
- Its serum link is not specific, and circulating IL-33 is unmeasured.
- It has no lung-cell, potency, oxidised-IL-33 or in vivo data.
- The delivered package has analysis defects that must be fixed before any external use.

**What dropping forgoes.** The option on a pathogen-agnostic, host-directed therapy for severe pneumonia with a ready-made enrichment biomarker. The cheapest decisive tests (Gates 0–1) use data and material we already own.

---

## 6. Forward view

### 6.1 The indication our data point at

Our data do not point to a different disease area. They point to a **re-definition of the LRTD indication**:

- **from** pathogen-defined ("viral LRTD")
- **to** mechanism- and biomarker-defined: **hospitalised pneumonia of any cause at risk of progression to respiratory failure, with systemic endothelial activation (high sST2 at admission), treated early.**

Why this and not "viral":

1. The only functional data are in **endothelium**, where IL-33 drives the neutrophil-recruiting and pro-coagulant program that AX-1177 blocks.
2. In **tissue**, nothing about IL-33 is specific to COVID-19 or to viral injury. There is no association with COVID status, pneumonia or diffuse alveolar damage under any classification, and the IL-33 reservoir is present in every lung. The autopsy reports also show that fatal "viral LRTD" is in practice mixed. 9/16 COVID+ lungs carry bacterial-pattern bronchopneumonia, one with *Aspergillus*. Only 7/16 show diffuse alveolar damage, and 4 show both. A pathogen-defined indication would fit these patients poorly.
3. In **serum**, endothelial-injury proteins (HGF, PTX3, vWF, ANGPT2, E-selectin), neutrophil-activation proteins (PRTN3, CD177, S100A12, IL-8) and IL-1-family soluble receptors (sST2, IL-18R1, IL-1R2) dominate the prognostic signal. This is coherent with IL-33-driven endothelial chemokine and G-/GM-CSF output.
4. The **endpoint** that our serum data predict is progression within 30 days of admission. The population is therefore admitted patients before deterioration, not established ARDS.

### 6.2 Biomarkers: what could go into patients, and in what role

| Marker | Evidence in our data | Patient-ready? | Role | Specimen / timepoint |
|---|---|---|---|---|
| **sST2** | #2/1,094 for ICU/IMV/death (OR 3.0 [1.8–5.0], q = 0.0075), independent of NEWS2. IL-33 decoy receptor. IL1RL1 is modestly IL-33-inducible in endothelium (+1.6 log2; SE unreliable) | **Yes.** Clinical immunoassays exist; a cut-off is needed (Gate 2) | **Enrichment / stratification (prognostic).** Exploratory PD | Serum at enrolment, pre-dose; repeat at 24 h and day 3 |
| **IL-6** | 4 concordant assays, OR 2.1–2.3, q ≤ 0.02. IL-33-induced +5.8 log2; fully blocked (102 %) | **Yes** (routine) | Stratification covariate. PD (not IL-33-specific) | Enrolment; 24 h; day 3 |
| **CCL20** | OR 1.8, q = 0.02. IL-33-induced +9.2 log2; fully blocked; also reversed in HGMEC | **Yes** (immunoassay) | **Lead PD / proof-of-mechanism marker** | 24 h; day 3 |
| OPG, IL-18R1, IL-1β, MCP-3 | q < 0.05 in serum. IL-33-induced and ≥96 % blocked | Yes (research assays) | Exploratory PD panel | 24 h; day 3 |
| IL-8, MCP-1, sE-selectin | q 0.02–0.09 in serum. IL-33 induction of +4 to +11 log2, reversed 1:1 (in vitro SE unreliable) | Yes | Exploratory PD; sE-selectin is the most endothelium-specific | 24 h; day 3 |
| HGF, PTX3 (also vWF, ANGPT2) | Top prognostic proteins (OR 5.0 and 11.6), but **not** IL-33-inducible in endothelium | Yes | **Prognostic covariates only, not PD** | Enrolment |
| Free / total IL-33; IL-33:AX-1177 and IL-33:sST2 complexes | Not in the delivered data | **Not yet** (assay development) | Target engagement; test of the sequestration risk | Pre-dose and post-dose |
| Viral load (RT-PCR) | IL-33 induces endothelial ISGs, which AX-1177 blocks | Yes | **Safety** (viral cases) | Baseline, day 3, day 7 |
| Lung IL-33 IHC; eosinophil and neutrophil IHC; lung IL-33-response RNA signature | Tissue only; IL-33 not different between groups; ceiling effects; granulocyte scores batch-confounded | **No** | Translational mechanism only | Post-mortem or biopsy |
| Blood eosinophils; type-2 markers (IL-5, IL-13, TSLP, eotaxins) | Not supported: null or not delivered | No | Not for selection | — |

### 6.3 Sampling timepoint

**Primary: serum at enrolment (hospital admission), before the first dose, within a fixed and recorded window (proposed ≤24 h from admission).**

1. It is the **only timepoint** at which our prognostic associations exist, because all mmc2 serum was drawn at enrolment. The odds ratios do not transfer to later samples.
2. In vitro, the IL-33 endothelial program peaks early (6 h) and is partly self-sustaining by 24 h. AX-1177 is most complete when present from the start (98 % vs 85 %). Both treatment and biomarker assessment therefore have to be early.
3. The outcome (progression within 30 days) is anchored to hospitalisation.

**PD sampling** in Phase 1b/2a: 24 h and day 3 after the first dose (plus day 7), with dense early sampling in Phase 1b to establish in vivo kinetics, which our data cannot give.

### 6.4 Next studies: gated plan with go / no-go criteria

| Gate | What it must establish | How | Go | Stop / narrow |
|---|---|---|---|---|
| **0. Fix the evidence base** (weeks; existing data) | That the current conclusions survive correct analysis | (a) Re-fit RNA-seq per cell line from archived counts. (b) Obtain the full 1,194-assay serum table including IL-33 and LOD flags, plus patient-level NPX; compute per-SD ORs and AUC gain over NEWS2; test an "AX-1177-reversible endothelial protein score" against a global-severity axis. (c) Adjudicate the lung diagnoses, then re-stain and re-score all blocks in one randomised, blinded run (second reader or digital quantification). (d) Pull affinity, potency, IL-33ox and species cross-reactivity from the biologics file | Neutralisation holds. sST2 stays independent of NEWS2 per SD | sST2 association collapses with complete, per-SD data |
| **1. Is the pathway on in human lung, and can we block it there?** (≈3–6 months; archived tissue + in vitro) | Tissue activity; lung-cell pharmacology; treatment window | (a) Score the IL-33 response signature in **archived lung RNA from 22 donors**. Classify them by adjudicated autopsy diagnosis, not the delivered labels: 17 with acute pneumonia (8 COVID+, 9 COVID−) and 5 without. (b) Primary **lung microvascular endothelium** (≥3 donors): IL-33red and IL-33ox dose–response, AX-1177 IC50/IC90, **time-of-addition** (0–6 h after IL-33), secretome matched to the Olink panel. (c) Primary airway epithelium (ALI) with IL-33ox | Signature raised in pneumonia lungs. ≥80 % inhibition in lung MVEC at clinically achievable concentrations. Meaningful block when added hours after IL-33 | **Kill** if lung MVEC are unresponsive or no tissue signature is found |
| **2. Does the biomarker generalise beyond COVID?** (≈6–9 months; retrospective biobank) | sST2 prognostic across pathogens; whether IL-33 is free or sequestered | Independent multi-centre hospitalised LRTD cohort (influenza, RSV, bacterial CAP, current-era COVID): sST2 (clinical assay), hs-IL-33, IL-33:sST2 complexes and the PD panel at admission. Outcome ICU/IMV/death at 30 days, adjusted for NEWS2 and CRP/IL-6 | Independent across pathogens; cut-off fixed; free IL-33 detectable | **Narrow** to viral if prognostic only in viral cases; **drop** if only in COVID |
| **3. In vivo PoC, then Phase 2a** | Efficacy with therapeutic dosing; safety | Viral and bacterial pneumonia models (model depends on species cross-reactivity): vascular leak, neutrophil influx, survival, viral load. Then a randomised, placebo-controlled, **sST2-enriched**, pathogen-stratified Phase 2a. Primary endpoint: progression to ICU/IMV/death by day 28–30. PD: CCL20, IL-6, IL-8, sE-selectin. TE: total IL-33. Safety: viral load | Efficacy with treatment after infection; no viral-load penalty | Otherwise stop |

---

## 7. Considered and ruled out

| Option / inference | Decision | Reason (our data) |
|---|---|---|
| Continue viral LRTD unchanged | Ruled out | No virus-specific IL-33 or granulocyte signal in tissue; serum signal non-specific; one pre-vaccination COVID cohort |
| COVID-19-specific indication | Ruled out | No COVID-specific IL-33 signal under any classification; upper 95 % bound for endothelial IL-33 (COVID+ minus COVID−) is 0.00. 9/16 fatal COVID lungs had bacterial-pattern bronchopneumonia |
| COPD / asthma (airway epithelial, type-2) | Ruled out on our data | No epithelial IL-33 stimulation; COPD/asthma history unrelated to tissue IL-33 (p ≥ 0.21); type-2 serum markers null or not delivered |
| Kidney / glomerular disease (HGMEC responded) | Ruled out | HGMEC response about half of HUVEC and transient; no kidney patient data; kidney injury markers modest (KIM-1 q = 0.11) |
| Eosinophil-driven indication | Ruled out for AX-1177 | Tissue eosinophil scores are not interpretable: the direction reverses under autopsy-based classification, and MBP tracks staining batch (p = 0.0007). Eosinophils are unrelated to tissue IL-33 (ρ −0.20 to +0.08). The IL-5Rα duplex read tracks neutrophil elastase (ρ 0.89). Serum type-2 signals are weak or not delivered |
| "Pneumonia brings granulocytes, so IL-33 is pneumonia biology" (label-based tissue analysis) | Rejected | Delivered group labels disagree with the autopsy diagnoses in 9/31 donors, and groups are nested in accession batches |
| HGF / PTX3 as PD markers | Ruled out (keep as prognostic covariates) | Not IL-33-inducible in endothelium (HGF +0.5 log2, ns) |
| sST2 as proof of IL-33 activity | Ruled out | It is a decoy and a general stress marker; IL-33 itself is unmeasured |
| "Lower IL-33 staining in COVID lungs = release" | Hypothesis only | Not significant at donor level after age adjustment (p 0.21–0.23); age drives vascular IL-33 (p = 0.001) |
| Block-level tissue statistics | Rejected | Pseudoreplication: 3 donors supply 24/49 COVID+ blocks. Block-level p 0.016–0.028 becomes 0.11–0.16 at donor level |
| Delivered p-values for key endothelial genes and antibody-alone "hits" | Rejected | Implausible SEs; effect-size concordance used instead |
| "4,000 DEGs" headline | Rejected | The 423 strongly repressed genes are mostly an artefact of the IL-33-alone arm; the robust program is the ~650 strongly induced genes |
| Off-target, agonist or endotoxin concern | Considered; ruled out | AX-1177 alone does not move the IL-33 or NF-κB program in any cell type |
| Potency or IL-33ox claims | Cannot be made | Single concentration; IL-33ox not tested |

---

## 8. Data-integrity findings in the delivered package

The full log is in the workbook, sheet *Data_issues_log*.

1. **mmc5:** the sheets named "6h" and "24h" are identical duplicates, and each contains both timepoints (24 contrasts).
2. **One voom/limma model across four unrelated cell types** gave implausible standard errors for 130 genes (median SE >2 log2, up to ~16,000). These include SELE, VCAM1, CXCL8, CXCL1, CCL2, IL1RL1, PTX3, VWF and CDH5. Eight genes that IL-33 induces more than 8-fold are reported as non-significant. Conversely, 12 rows have collapsed SEs (t up to 169 for |log2FC| < 0.2). Gene-specific df (75–85) indicate robust eBayes, which is not an error.
3. **AveExpr is averaged over all 114 libraries**, so endothelial IL-33 targets look "low expressed" (CSF2 −3.2). Filtering on AveExpr would delete them.
4. **The strongly IL-33-repressed genes (>2-fold; 423) are mostly an artefact of the IL-33-alone arm**: 65 % are low-count, and only 30 % are reversed vs isotype+IL-33. There is no HGMEC vehicle arm, IL-33 was never applied to the epithelial lines, and a DMSO "vehicle" was used for an IgG.
5. **mmc2: BH was applied with m = 1,194, but 1,094 assays were delivered.** Evidence: adj.p/p = 1194.000 for the top row. So 100 assays were tested and withheld. By panel content these include IL-33, IL-4, IL-5, IL-13 and TSLP. About 16 of the withheld assays had p < 0.05 and 1–3 had p ≤ 0.001. The annex statement ("across all assays in the delivery") is inaccurate.
6. **mmc2: columns composite_endpoint_0/1 are undocumented.** From their values they are the fraction missing or below LOD in 56 non-events and 44 events. Odds ratios "per log unit" are not comparable across assays (CSF-1 OR 90, CI 4–1,933). 27 proteins were measured on more than one panel; the duplicates agree (good QC) but are not independent hits.
7. **mmc3 layout:** donor fields appear only on the first block, some on the second. There is one unevaluated Excel formula, "ND" entries, and "n+" coded as n+0.5 (scores of 5.5 on a 0–5 scale). 39/74 endothelial IL-33 scores sit at the ceiling. One "COVID-negative" donor has no test result. There was a single unblinded reader.
8. **mmc3 biases:** age confounds vascular IL-33 (ρ = 0.55).
9. **mmc3 group labels disagree with the autopsy diagnoses in 9/31 donors** (the delivered pathology text):
   - 4 of 10 "COVID− pneumonia" donors have no pneumonia recorded (1905, 1961, 1968, 1970);
   - 3 of 5 "no pneumonia" controls have acute lung disease (1976 acute and organizing pneumonia, 1956 acute pneumonitis, 1944 pulmonary coccidioidomycosis), and the other two have fibrotic lung disease;
   - 2 of 16 "COVID+ pneumonia" donors have no acute pneumonia (2067, which contributes 8 blocks, and 2101).
10. **mmc3 groups are nested in accession batches:** each block-ID batch contains a single group, and scores differ by batch (MBP p = 0.0007; neutrophil elastase p = 0.005). Group comparisons of granulocyte scores therefore cannot be separated from staining or scoring batch. IL-33 scores show no batch effect (p 0.10–0.65).

## 9. Methods summary

**RNA-seq**
- Delivered limma contrasts were reshaped to one row per gene.
- SE plausibility was assessed as |logFC/t|. Gene-specific df were checked against t→p, and BH was verified per contrast (exact).
- The IL-33 response used IL-33 vs vehicle (HUVEC).
- Neutralisation was judged against the **independent** comparator, AX-1177+IL-33 vs isotype+IL-33. This avoids the shared-reference bias of comparing against the IL-33-alone arm.
- % inhibition = 1 − [(AX-1177+IL-33) − vehicle] / [(isotype+IL-33) − vehicle], computed where the isotype-treated response exceeds 1 log2.

**Serum**
- 1,094 Olink assays were mapped to HGNC symbols and joined to the in vitro effects. Wald z was derived from the CIs.
- Enrichment was tested with Fisher and Mann–Whitney tests against all measured proteins, with duplicate assays collapsed per gene.
- The BH denominator was reconstructed from adj.p/p.

**Tissue**
- The formula cell was evaluated, ND was set to missing, and "n+" scored as n.
- Blocks were collapsed to donor means (n = 31).
- Analyses: Kruskal–Wallis; rank-ANCOVA with pneumonia, COVID status and age; Hodges–Lehmann differences with 4,000-sample bootstrap CIs.
- Sensitivity analyses:
  - each donor was re-classified from the delivered autopsy diagnoses (acute pneumonia, DAD, bronchopneumonia);
  - models were re-run within accession batch (block-ID ranges).

**Figures:** Fig 1 shows in vitro neutralisation, Fig 2 serum, Fig 3 tissue and Fig 4 data integrity.
