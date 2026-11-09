# AX-1177 (anti-IL-33 mAb; research code Compound_47): portfolio audit

**Scope.** This review uses only the delivered programme files: `AX-1177_methods_annex.md`, `mmc2.xlsx` (serum Olink vs outcome), `mmc3.xlsx` (post-mortem lung IHC), `mmc4.xlsx` and `mmc5.xlsx` (endothelial/epithelial RNA-seq contrasts).

I re-analysed the summary statistics myself. Raw counts, patient-level data and potency data were not delivered, so some questions cannot be settled here; those points are flagged.

The small amount of outside context I use is labelled **[external context]**.

---

## 0. Bottom line for the committee

**Recommendation: KEEP AX-1177, but as a gated, re-scoped asset. Do not fund further viral-LRTD development on the current evidence package.**

The position in one sentence: *the molecule is de-risked; the indication is not.*

| | What our data show | Strength |
|---|---|---|
| **Molecule** | AX-1177 abolishes the IL-33(reduced)-driven endothelial inflammatory programme. For genes induced >4-fold in HUVEC at 6 h, reversal is median 98% (slope −0.98). The response replicates 1:1 in the isotype arm. Reversal also occurs in glomerular microvascular cells. Without IL-33 the antibody is transcriptionally inert in four cell types (no more change than swapping one vehicle for another). | **Strong** (in vitro) |
| **Target presence** | IL-33 protein is abundant in human lung endothelium and basal airway epithelium. | **Strong**, but not disease-specific |
| **Disease link (viral LRTD)** | IL-33 is *not* higher in COVID-19 lungs (donor-level, age-adjusted; the trend is lower). IL-33 itself is absent from the delivered serum data. The IL-33 endothelial programme is *not* over-represented among serum proteins that predict ICU/ventilation/death (Fisher p = 0.75). sST2 (the IL-33 decoy receptor) predicts outcome, but about half the serum proteome does too. | **Weak / unproven** |
| **Breadth** | All patient data come from one centre, are SARS-CoV-2 only, and pre-date vaccination. Nothing covers RSV, influenza or hMPV. | **Absent** |
| **Data integrity** | Material defects in all three datasets (section 6). Some change headline claims, e.g. E-selectin/VCAM-1 "2,000-fold induction" is statistically invalid as delivered, and about 100 serum assays were analysed but not delivered. | **Must fix before audit** |

**Why keep rather than drop.** The evidence that decides the indication question largely **already exists in our archive** and was not in the delivery:

- About 100 serum assays were analysed but not delivered. At least 2 were FDR-significant, and the gap very probably includes IL-33 itself.
- The per-cell-line RNA-seq re-analysis and the HGMEC IL-33 contrast can be produced from archived counts.
- Patient-level proteomics are also archived.

Dropping now would mean deciding on incomplete and partly corrupted data. Advancing now would be indefensible, because nothing in our data shows IL-33 drives severe viral LRTD.

**Indication our data point at.** Not "viral LRTD" as a whole, and not a different therapy area. At most, our data support **hospitalised viral pneumonia with endothelial activation, at risk of progression to ICU/invasive ventilation/death, selectable by high admission serum sST2**. SARS-CoV-2 is the only virus with evidence.

**Kill criteria** are in section 1.4. **If dropped**, the statement of what we are dropping and why is in section 1.5.

---

## 1. The recommendation and how to defend it

### 1.1 Recommendation
1. **Retain AX-1177** in the portfolio, downgraded from "viral-LRTD development" to **"conditional / de-risking"** status.
2. **Re-scope the hypothesis** from "viral LRTD" to a **biomarker-defined, hospitalised, endothelial-activation phenotype** (section 2).
3. **Release spend only against three gates** (section 4). Gate 0 uses archived data only and can be closed within weeks.
4. **Correct the data package** before it goes to the committee (section 6).

### 1.2 The strongest supporting evidence (with numbers)

**A. AX-1177 is a functional, clean IL-33 neutralizer (mmc4, mmc5; Fig. 1, Fig. 5)**

- **IL-33 response.** IL-33red (30 ng/mL) changed 4,031 genes in HUVEC at 6 h and 1,836 at 24 h (FDR < 0.05). 645 and 314 respectively were induced >2-fold.
- **What the programme is.** A neutrophil-recruiting, pro-adhesive, pro-coagulant endothelial activation programme. It includes GM-CSF (CSF2 +10.3 log2), CXCL6 (+9.4), CCL20 (+9.2), CX3CL1 (+8.4), G-CSF (CSF3 +8.3), TNF (+7.9), IL-6 (+5.8), tissue factor (F3 +5.6), OPG (+4.8), IL-1β (+3.7) and complement C3.
- **Neutralization.** AX-1177 (10 µg/mL; about 41-fold molar excess, added at the same time as IL-33 without pre-incubation) reversed the induced genes almost completely.
  - Compared with IL-33 + isotype (NIP228), the reversal slope was −0.98 at 6 h and −0.75 at 24 h.
  - Median inhibition was 98% at 6 h and 84% at 24 h.
  - For genes induced >8-fold, the residual effect was 0.06 log2 at 6 h.
- **Replication.** The induction replicates in the independent IL-33 + isotype arm (ratio 1.02 at 6 h). The effect therefore does not depend on one group of three wells.
- **Not an endotoxin or contaminant artefact.** A contaminant-driven NF-κB response would not be blocked by an anti-IL-33 antibody. It is blocked by AX-1177 and not by the isotype control.
- **Microvascular endothelium.** In glomerular microvascular endothelium (HGMEC), AX-1177 reversed the same programme at 6 h: 1,460 DEGs, with slope −0.64 against the HUVEC IL-33 effect. This shows HGMEC respond to IL-33 and that AX-1177 blocks it. How complete the block is in HGMEC cannot be quantified (section 6).
- **Core signature.** 117 genes have valid statistics, are induced >4-fold by IL-33, replicate with the isotype, are reversed >4-fold in HUVEC and are reversed >2-fold in HGMEC (Table T3).
- **Specificity.** Without IL-33, AX-1177 vs isotype/PBS/DMSO gave 14–73 nominally significant genes per contrast (16 contrasts, 4 cell types).
  - All were either about 0.1 log2 shifts in very highly expressed genes or ±3 log2 noise in barely expressed lncRNAs.
  - Only one gene (ZBTB20, MCF7 vs DMSO, 24 h) reached |log2FC| ≥ 1 with reasonable expression.
  - The spread is equal to DMSO-vs-PBS (vehicle-vs-vehicle) differences.
  - There is also no sign of endogenous IL-33 tone in unstimulated endothelium.

**B. The target is present where the mechanism operates (mmc3; Fig. 3)**
- IL-33 IHC is high in lung endothelium in every group: 53% of blocks score at the top of the recorded range. Basal epithelial staining is also high (donor medians 4.25–4.88 on the delivered scale).

**C. Patient data are consistent with the IL-33 axis being relevant to severity (mmc2; Fig. 2)**
- **sST2 (IL1RL1)** is the **2nd of 1,063 unique serum proteins** for the 30-day composite of ICU, invasive ventilation or death. OR 3.02 per log unit (95% CI 1.83–5.01), p = 1.7×10⁻⁵, delivered adj p = 0.0075. The model is adjusted for age, sex and NEWS2, so sST2 adds information beyond bedside severity.
- **Bridging proteins.** Eight IL-33-inducible, AX-1177-reversible endothelial genes have serum proteins that are also prognostic (delivered FDR < 0.05):
  - **IL-6**: OR 2.14, concordant on 4 separate panels
  - **OPG/TNFRSF11B**: OR 6.8 and 4.4 on 2 panels
  - **IL-18R1**: OR 6.07
  - **CCL20**: OR 1.83
  - **CCL7/MCP-3**: OR 1.72
  - **IL-1β**: OR 2.45
  - **CSF-1** and **CTSS**
- These are the only direct in-house link between the cell pharmacology and patients.

### 1.3 Challenges the committee will raise, and the answers

| Challenge | Answer grounded in our data |
|---|---|
| "sST2 is the #2 hit, so IL-33 drives severe disease." | **No.** The whole serum proteome shifts toward worse outcome: 82% of 1,094 ORs are >1, the median protein has z = +1.37, and an estimated ~50% of proteins are associated. Centred on that shift, sST2 is only nominally separable (empirical p = 0.037, q = 0.97) and no protein survives FDR. sST2 is a **prognostic** marker. It is not proof of IL-33 causality. [external context: sST2 also rises with heart failure, renal dysfunction and glucocorticoids, none of which were adjusted for.] |
| "IL-33 induces E-selectin 2,000-fold and VCAM-1 430-fold; that is overwhelming." | The fold-changes are plausible: they lie exactly on the complete-reversal line in Fig. 1. **But their delivered statistics are invalid**: E-selectin t = 1.26 (p = 0.50), VCAM-1 t = 1.24, CXCL1 t = 0.007 for an 8.2 log2 change. Implied standard errors reach thousands of log2 units. Do not cite them. Cite the valid genes instead (GM-CSF, CXCL6, CCL20, CX3CL1, G-CSF, IL-6). |
| "IL-33 is everywhere in diseased lung; that validates the target." | It validates **presence**, not **involvement**. Non-pneumonia controls have as much or more IL-33 as COVID lungs. After age adjustment, the COVID effect is p = 0.88 (epithelium), 0.063 (endothelium, lower) and 0.087 (smooth muscle, lower). |
| "Why not drop it now?" | The decisive data already exist and were not delivered (about 100 Olink assays, very probably including IL-33; per-cell-line RNA-seq; patient-level proteomics). Deciding without them means deciding on the wrong data. Retrieving them costs weeks, not a new study. |
| "Why not pivot to COPD/asthma, where IL-33 is clinically validated?" | **Nothing in our data supports it.** Serum type-2 markers are null: IL-5 OR 1.00; eotaxins, CCL17, FCER2 and tryptase all null. Tissue IL-33 is unrelated to COPD, emphysema or asthma annotations (p ≥ 0.07) and to eosinophil scores. We have no epithelial or type-2 pharmacology. A COPD move would be a strategy decision needing a new evidence package, not a data-driven repurposing. |
| "Is it specific, and is it safe?" | It is transcriptionally inert without IL-33 in 4 cell types. This is **not** a safety package: there are no FcγR-bearing immune cells, no tissue cross-reactivity and no in vivo data. |
| "Does it block oxidised IL-33?" | Binding to both forms is asserted in the biologics file (not delivered). Function was tested **only against IL-33red**. Open gap. |
| "Is the potency adequate?" | Unknown. There was one concentration (about 41:1 molar excess) and one IL-33 dose, which is supraphysiological. There is no IC50 and no PK. |

### 1.4 What would change the recommendation
- **Drop the viral-LRTD hypothesis** if Gate 0 shows all of the following:
  1. Serum IL-33 is undetectable or not associated with outcome.
  2. After valid re-analysis, the IL-33-specific endothelial products (E-selectin, VCAM-1, CXCL6, CX3CL1, G-CSF, GM-CSF) do not associate with outcome.
  3. sST2 loses independent prognostic value once batch/plate and the proteome-wide shift are handled with patient-level data.
- **Drop the asset entirely** if Gate 1 shows AX-1177 does not block virus-conditioned endothelial activation at achievable concentrations, or does not neutralise IL-33ox.
- **Advance** to a biomarker-enriched Phase 1b/2a only if Gates 0–2 all pass.

### 1.5 If the committee chooses to drop: what we are dropping and why
- **What we drop:** a specific, functionally validated IL-33(red) neutralizer with in vitro proof of mechanism in macro- and microvascular endothelium, a 117-gene endothelial PD signature, and a candidate prognostic enrichment marker (sST2).
- **Why:**
  - Our own data do not show IL-33 is elevated or causal in viral LRTD.
  - The only patient data are a single-centre, pre-vaccination, SARS-CoV-2-only cohort of 100 patients.
  - The serum association is not pathway-specific.
  - Potency, oxidised-IL-33 activity and in vivo efficacy are untested.
  - The data package has integrity defects that would need remediation before anyone could build on it.

---

## 2. What indication do our data actually point at?

The data triangulate on a **mechanism**: IL-33-driven endothelial activation (neutrophil chemokines, myelopoietic factors, adhesion molecules, tissue factor). They point at only **one population with any patient-level support**: hospitalised, unvaccinated adults with SARS-CoV-2 pneumonia, where sST2 and several IL-33-inducible endothelial products at admission predict ICU/IMV/death independent of NEWS2.

So the defensible indication is a **narrowing, not a pivot**:

> **"Prevention of progression to critical illness (ICU / invasive ventilation / death by day 30) in adults hospitalised with viral pneumonia and endothelial activation (high admission sST2)."** Evidence exists for SARS-CoV-2 only. Other viruses must be shown (Gate 2).

Why this and not the alternatives:
- **Too broad: "viral LRTD".** We have no data on RSV, influenza or hMPV, on non-hospitalised disease, or on vaccinated / current-standard-of-care populations.
- **Possibly pathogen-agnostic.** Tissue IL-33, eosinophil and neutrophil scores do not distinguish COVID from non-COVID pneumonia. The severity proteome is generic, and the mechanism is endothelial. If IL-33 matters, it may matter in severe pneumonia or early ARDS regardless of pathogen. That is a **hypothesis to test**, not a current indication.
- **Other therapy areas** (COPD/asthma, kidney, oncology, sepsis) are not supported (section 5).

---

## 3. Biomarkers, sampling timepoint, and which can go into patients

### 3.1 Proposed biomarkers and roles

| Marker | Matrix | Evidence in our data | Role | Into patients now? |
|---|---|---|---|---|
| **sST2** (Olink "ST2", CVD III) | serum | OR 3.02 (1.83–5.01), adj p 0.0075; rank 2/1,063; NEWS2-adjusted. Caveat: within a proteome-wide shift. | **Prognostic enrichment / stratification** at enrolment | **Yes, as an exploratory stratification factor** in the next clinical study. **Not yet as an eligibility cut-off**: it needs an absolute (non-NPX) assay, a pre-specified cut-off and replication. **Not a PD marker**: no valid in vitro evidence that AX-1177 changes it (IL1RL1 statistics are invalid; Table T2). |
| **CCL20** | serum | IL-33 +9.2 log2, AX-1177 −9.8 (HUVEC 6 h), −5.6 (HGMEC); serum OR 1.83, adj p 0.02 | Downstream **PD** + prognostic | **Yes, exploratory PD** |
| **OPG (TNFRSF11B)** | serum | +4.8 / −5.0 / −1.9; OR 6.8 and 4.4 (2 panels), adj p 0.014 | PD + prognostic | **Yes, exploratory PD** |
| **IL-18R1** | serum | +3.6 / −3.5 / −2.4; OR 6.07, adj p 0.018 | PD + prognostic | **Yes, exploratory PD** |
| **IL-6** | serum | +5.8 / −6.0 / −2.9; OR 2.1 (4 concordant panels) | **Prognostic covariate**. A poor PD marker: non-specific, and confounded by standard of care (dexamethasone, tocilizumab) [external context] | Yes, as a covariate only |
| **GM-CSF, CXCL6, G-CSF, CX3CL1** | cell supernatant / ex vivo | Largest IL-33 dynamic range (+8.3 to +10.3 log2), fully reversed, valid statistics. **Not** prognostic in serum. | **Potency / ex vivo PD assay readouts** | Not yet. Use in the ex vivo potency assay; add to the clinical panel only as exploratory. |
| **Total and free IL-33** (drug–target complex) | serum | **Absent from the delivery** (very probably analysed; section 6) | **Target engagement** | Required before any clinical study; assay and detectability to be established |
| E-selectin, VCAM-1, IL-8, MCP-1, PTX3 | serum | Large in vitro fold-changes, but **statistics invalid**. Serum: PTX3 adj p 0.012, IL-8 0.023, E-selectin 0.09, VCAM-1 ns | On hold | Not until re-analysed |
| Tissue factor (F3) | cells | +5.6 / −5.5. Thromboemboli in 4/16 COVID+ vs 0/15 COVID− autopsies (p = 0.10) | Mechanistic hypothesis (thrombo-inflammation) | No |
| Lung IL-33 IHC; eosinophil IHC or type-2 serum markers | tissue / serum | Near ceiling, does not discriminate; eosinophils track pneumonia, not COVID or IL-33; type-2 serum null | None for this asset and indication | No |

### 3.2 Sampling timepoint
- **Patients, primary sample: at enrolment (hospital admission), before first dose.** This is the only timepoint at which we have patient evidence (enrolment serum, NEWS2-adjusted). It is the enrichment and stratification sample.
- **Ex vivo / in vitro PD and potency assays: 6 h after IL-33 exposure.**
  - 6 h is the peak of the IL-33 programme: 4,031 DEGs at 6 h vs 1,836 at 24 h.
  - It is also the point of largest neutralization window: 4,239 reversed DEGs in HUVEC at 6 h vs 1,160 at 24 h, and 1,460 vs 269 in HGMEC.
  - Several key transcripts are transient. TNF is back to baseline by 24 h; CCL20 falls from +9.2 to +5.6; CX3CL1 falls from +8.4 to +3.2.
  - Sustained readouts (GM-CSF, CXCL6, G-CSF, C3) tolerate timing error better and are the preferred potency readouts. Secreted-protein readouts will probably need 24 h; to be confirmed.
- **On-treatment PD in patients:** first sample **≤24 h post-dose**, then day 3 and day 7. The primary IL-33 response is transient, so late-only sampling would miss it. The exact in vivo timing cannot be derived from our data and must be set in the first clinical study.

---

## 4. Next studies and gated plan

**Gate 0: archive retrieval and re-analysis (weeks; no new experiments)**
1. **Serum.**
   - Retrieve the full 1,194-assay Olink result set, with LOD and missingness by outcome group. Confirm whether IL-33, TSLP, IL-4, IL-5 and IL-13 were measured, and report detectability and association.
   - Recompute FDR on the correct family after collapsing proteins measured on more than one panel.
   - Obtain patient-level NPX plus plate IDs to test plate or batch effects behind the global shift.
   - Estimate sST2's incremental discrimination over NEWS2 (ΔAUC, calibration).
   - Adjust additionally for renal function, steroid exposure, days from symptom onset and cardiac comorbidity.
2. **RNA-seq.**
   - Re-fit per cell line (separate voom/limma models) from the archived counts. This should recover valid statistics for E-selectin, VCAM-1, IL-8, CXCL1, MCP-1, PTX3 and ST2 (IL1RL1).
   - Deliver the missing contrasts: HGMEC IL-33 + isotype vs isotype; HUVEC IL-33 + isotype vs vehicle; isotype vs vehicle.
   - Deliver per-cell-line expression levels.
3. **Tissue.**
   - Second blinded reader with inter-rater agreement.
   - Document the score transformation.
   - Adjudicate the 8 donors whose label conflicts with their pathology report.
   - Release the archived lung-tissue RNA (`Zr4940_*`) for in-situ IL-33 signature scoring.
- **Go** if IL-33 itself, or the IL-33-specific endothelial products, associate with outcome after correct analysis, **or** sST2 retains meaningful independent prognostic value after batch and global-shift handling. Otherwise stop viral-LRTD work (section 1.4).

**Gate 1: pharmacology (about 3–6 months)**
- AX-1177 concentration–response (IC50/IC90) against IL-33red and IL-33ox:
  - at near-physiological IL-33 concentrations
  - in primary human **lung microvascular** endothelial cells and HUVEC, from at least 3 donors each
  - with pre-incubation and with concurrent addition
  - reading transcripts at 6 h and secreted proteins at 24 h
- Virus-infected primary airway epithelium (air-liquid interface; SARS-CoV-2, influenza, RSV). Apply its conditioned medium to endothelium ± AX-1177 to test whether IL-33 neutralization reduces *virus-driven* endothelial activation.
- **Go:** at least 50% inhibition of virus-conditioned endothelial activation at concentrations compatible with achievable exposure.

**Gate 2: clinical biomarker cohort (about 6–12 months; biobank or prospective)**
- Design: multi-centre, current-era (vaccinated) hospitalised viral LRTD (SARS-CoV-2, influenza, RSV, hMPV); n of about 300–500.
- Sampling: admission (primary), day 3 and day 7.
- Assays: sST2 (absolute assay), free and total IL-33, and the PD panel (CCL20, OPG, IL-18R1, IL-6 ± CX3CL1/G-CSF).
- Endpoint: same as our cohort (ICU/IMV/death by day 30).
- **Go:** sST2 (or IL-33) prognostic independent of NEWS2 in at least 2 viruses, with a pre-specified cut-off that identifies a subgroup with a clinically meaningful excess event rate.

**Then: Phase 1b/2a** in sST2-high hospitalised viral pneumonia.
- Sampling: enrolment (pre-dose), ≤24 h, day 3 and day 7.
- PD: total IL-33 (target engagement) plus the CCL20/OPG/IL-18R1 panel.
- Endpoint: ICU/IMV/death by day 30.

---

## 5. What I considered and ruled out

**Indications**

| Considered | Verdict | Basis in our data |
|---|---|---|
| Viral LRTD, broad (current scope) | **Ruled out as framed** | SARS-CoV-2-only, pre-vaccination, single-centre patient data; no IL-33 measurement delivered; tissue IL-33 not raised in COVID |
| Hospitalised SARS-CoV-2 / viral pneumonia with endothelial activation (sST2-high) | **Retained as the working hypothesis** (conditional) | sST2 and bridging proteins prognostic, NEWS2-adjusted; endothelial mechanism fully blocked in vitro |
| Pathogen-agnostic severe pneumonia / early ARDS | Plausible extension, **not yet supported** | Tissue biology not virus-specific; no non-COVID serum data |
| Asthma / eosinophilic (type-2) airway disease | **Ruled out on our data** | Serum IL-5, eotaxins, CCL17, FCER2 and tryptase null. Tissue IL-33 unrelated to eosinophils or asthma annotations. No type-2 pharmacology. Type-2 cytokines (IL-4/5/13, TSLP) absent from delivery. |
| COPD | **Not supported by our data** (strategic option only) | Tissue IL-33 not associated with COPD or emphysema annotations (p ≥ 0.07); no COPD patient data [external context: IL-33 is clinically pursued in COPD by others] |
| Kidney microvascular disease (glomerular endothelium) | **Ruled out** | HGMEC is one donor at P5 with no IL-33-vs-control contrast delivered; no kidney patient data; serum KIM-1 weak (adj p ≥ 0.11) |
| Thrombo-inflammation / COVID coagulopathy | Hypothesis only | Tissue factor induced and fully reversed in vitro; thromboemboli 4/16 vs 0/15 autopsies (p = 0.10); no coagulation biomarkers |
| Oxidised IL-33 / RAGE–EGFR epithelial arm | Untested | EGFR ligands AREG and TGF-α associate with outcome (each concordant on 2 panels), but no IL-33ox or epithelial-IL-33 experiments exist |
| Oncology | Not relevant | A549 and MCF7 were specificity controls only (no IL-33 arm) |

**Interpretations and analyses I rejected**
- **Block-level tissue statistics.** 74 blocks from 31 donors, with 3 donors contributing 24 of 49 COVID+ blocks. Pseudo-replication turns non-significant donor-level results into false positives: EDN p = 0.0006 (block) vs 0.09 (donor); endothelial IL-33 p = 0.017 vs 0.052. All tissue conclusions are donor-level.
- **Ranking serum markers by OR size.** ORs are per unstandardised "log unit" on NPX values that are already log2, so they are not comparable across assays (e.g. CSF-1 OR 90, CI 4–1,933). I ranked by z/p instead.
- **Counting assays as proteins.** 27 proteins appear on 2–4 panels (58 rows). There are 1,063 unique proteins, not 1,094. Cross-panel agreement is good, e.g. IL-6 OR 2.07–2.31 on 4 panels.
- **Using the top of mmc4 (sorted by fold change).** 4 of the top 40 genes at 6 h (SELE, VCAM1, CXCL8, CXCL1) are non-significant with invalid statistics.
- **Interpreting IL-33-downregulated genes.** Only 40–60% of the apparent repression replicates in the isotype arm, and AX-1177 "reversal" of these genes is inconsistent (slope 0.23). The down-regulated set is not robust, so conclusions rest on induced genes.
- **Treating antibody-alone DEGs as off-target effects.** They are noise equivalent to vehicle-vs-vehicle.
- **Endotoxin contamination explaining the HUVEC response.** Excluded by the isotype-controlled, antibody-specific reversal.
- **Quantifying IL-33 response in HGMEC.** Not possible: no vehicle arm, and the IL-33 + isotype vs isotype contrast was never extracted.
- **sST2 as a PD marker.** No valid in vitro evidence, and it is the decoy receptor rather than a neutralization readout.

---

## 6. Data-integrity findings to fix before the audit
(Full log: `tables/T1_data_integrity_log.csv`.)

**RNA-seq (mmc4/mmc5)**
1. **205 genes have statistically impossible results.** Implied SE (|logFC/t|) is >3 log2 units and up to 36,723, against a median of 0.33. They include the canonical endothelial genes SELE, VCAM1, CXCL8, CXCL1, CCL2, PTX3, IL1RL1 (ST2), VWF, CDH5, PECAM1, KDR and ESM1.
   - Their fold-changes look internally consistent, which points to broken variance estimates.
   - Likely cause: the single pooled model across four very different cell types described in the annex.
   - Remedy: re-fit per cell line from the archived counts.
2. **mmc5 sheets "6h" and "24h" are identical** (24 contrasts each, both timepoints, different row order). The names are misleading; no data are lost.
3. **Mislabelled comparator.** The "IL33_vs_Vehicle" sheets carry "Nontreated" comparison labels.
4. **Key contrasts were never delivered.** These include HGMEC IL-33 vs control (no vehicle arm; IL-33 + isotype vs isotype not extracted), and isotype vs vehicle. The annex's "all remaining contrasts" is therefore inaccurate.
5. **AveExpr is pooled over 114 libraries from 4 cell types**, so it says nothing about expression in any one line.
6. **Design limits.** Each endothelial line comes from a single donor (HUVEC P2, HGMEC P5). There is one antibody concentration and one IL-33 dose, concurrent addition, no lung microvascular cells, and no IL-33ox.

**Serum proteomics (mmc2)**
7. **The BH family was 1,194 tests, but only 1,094 assays were delivered.** Back-calculated ranks are integers for 639 of 639 checkable rows. Of the roughly 100 undelivered assays, at least 2 had p < 0.005 (FDR-significant) and at least 16 had p < 0.05. The annex's statement that BH was applied "across all assays in the delivery" is therefore incorrect.
8. **The Inflammation panel is missing 15 of its 92 assays.** Against the vendor's standard v.3022 content [external context, to be confirmed against the panel sheet], these are IL-33, TSLP, IL-4, IL-5, IL-13, IL-2, IL-2RB, IL-1α, IL-20, IL-22RA1, IL-24, LIF, β-NGF, NRTN and FGF-23.
   - This means **the drug's target and the type-2 cytokines are probably missing**.
   - Every delivered assay has ≤9% missing values per outcome group, consistent with a post-analysis detectability filter.
9. **Duplicate proteins** (27 proteins on 58 rows) are counted as separate assays.
10. **Undefined units.** "Log transformed" on top of NPX (already log2) is ambiguous.
11. **Undocumented columns.** `composite_endpoint_0/1` appear to be fractions missing or below LOD (denominators 56 and 44, i.e. 44 events).
12. **Proteome-wide shift toward worse outcome** (82% OR > 1). Plate layout, normalisation and randomisation are not documented.
13. **Adjustment set limited** to age, sex and NEWS2.

**Lung tissue (mmc3)**
14. **Rows are histology blocks, not donors** (74 blocks, 31 donors; 1–8 blocks per donor). Donor fields are on the first block only, except for some comorbidity notes that sit on later blocks.
15. **Scores are not on the documented 0–5 scale.**
    - The numeric EPX, neutrophil elastase and tryptase columns equal the ordinal score + 0.5 (6 values of 5.5).
    - The IL-33 columns are averaged composites (values such as 4.25 and 4.75; 16 epithelial and 39 endothelial values equal 5.5).
    - One IL-33 cell holds the formula text `=(2+4.5)/2`.
    - There are 'N/A'/'ND' entries and trailing spaces.
16. **Disease label conflicts with the pathology text in 8 of 31 donors.**
    - 4 "COVID-neg pneumonia" donors (1905, 1961, 1968, 1970) have no pneumonia in their reports.
    - 2 "non-pneumonia" donors have pneumonia or pneumonitis (1976, 1956).
    - 1 "control" has pulmonary coccidioidomycosis (1944).
    - 1 "COVID-pos pneumonia" donor has no acute pneumonia listed (2101).
    - Donor 1905 is also missing SARS-CoV-2 status.
    - Conclusions are unchanged after reclassification.
17. **Limited scoring and sample.** Single reader with no agreement statistics. Endothelial IL-33 sits at the top of the scale. Donors are elderly (64–98) and all white.

---

## 7. How I did the re-analysis (reproducibility notes)
- **Derived contrasts.** All RNA-seq contrasts come from one linear model, so log fold-changes add exactly. I used this to derive IL-33 + isotype vs vehicle, and IL-33 + AX-1177 vs vehicle (the residual effect).
  - Reversal = AX-1177 + IL-33 vs isotype + IL-33, regressed on IL-33 vs vehicle.
  - Statistic validity: implied SE = |logFC/t| (genes flagged if >3 in any contrast). The residual df of 85.13 was recovered from t/P (76 residual + about 9 prior).
- **Serum.**
  - Mapped Olink names to HGNC symbols and collapsed duplicates (keeping the best p).
  - Tested IL-33-signature enrichment with Fisher and Mann–Whitney tests on the universe of 851 proteins with valid in vitro statistics.
  - Empirical null = median and MAD of signed z (1.37, 1.41).
  - BH family reconstruction: implied rank = p × N / adj-p, with N = 1,194 (exact for the top hit).
- **Tissue.**
  - Donor mean over blocks, Kruskal–Wallis and Mann–Whitney tests, and a rank ANCOVA adjusted for age.
  - Sensitivity analysis reclassifying donors from the pathology text.
- **Limitations of this review.** Summary statistics only. I could not compute sST2 discrimination, check plate effects, or verify the Olink panel content against vendor documentation.

## Files
- `figures/fig1_invitro_reversal_and_invalid_stats.png`: IL-33 response vs AX-1177 reversal (HUVEC 6 h and 24 h); distribution of implied SEs
- `figures/fig2_serum_proteome.png`: volcano with the IL-33 signature overlaid; proteome-wide shift and empirical null
- `figures/fig3_tissue_donor_level.png`: donor-level IHC by group; block-level vs donor-level p
- `figures/fig4_serum_delivery_gaps.png`: reconstructed undelivered assays; missing assays by panel
- `figures/fig5_kinetics_6h_vs_24h.png`: 6 h vs 24 h kinetics and residual after AX-1177
- `tables/T1` data-integrity log; `T2` 205 genes with invalid statistics; `T3` 117-gene core IL-33 endothelial signature; `T4` serum proteins × in vitro bridge (1,063 proteins); `T5` tissue donor-level table with label flags; `T6` DEG counts per contrast; `T7` proteins measured on multiple panels
