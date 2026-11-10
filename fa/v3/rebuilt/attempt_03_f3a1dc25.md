# AX-1177 (anti-IL-33 mAb): portfolio audit position

**Basis.** This position uses only the AX-1177 data dump: the methods annex, serum proteomics (mmc2), post-mortem lung IHC (mmc3), and endothelial/epithelial transcriptomics (mmc4, mmc5). Every number below can be reproduced from `AX-1177_supporting_tables.xlsx`. Where we depart from the delivered tables, for example by reconciling duplicate assays or re-labelling donors from their pathology reports, we say so.

> **Verdict: keep AX-1177, but re-scoped and gated.**
>
> - AX-1177 is a clean IL-33 antibody that neutralises IL-33 near-completely in our endothelial assays.
> - Its pathway marker, serum sST2, independently predicts severe COVID-19 outcome.
> - Our data do **not** support the all-comers viral LRTD programme.
> - Re-scope to sST2-high hospitalised patients with severe viral pneumonia, with an endothelial, non-type-2 mechanism.
> - Fund only Gates 0–2. Drop the asset if AX-1177 fails to work after IL-33 has been released (Gate 1), or if the sST2 signal does not replicate outside SARS-CoV-2 (Gate 2).

---

## 1. Recommendation

**Keep AX-1177, but do not keep the current programme.**

- **Stop** the all-comers "viral LRTD" thesis. Our data do not support it:
  - The only clinical evidence is *prognostic*. It comes from a single virus (SARS-CoV-2), in the pre-vaccination era, at one centre, in 100 patients.
  - Our pharmacology models only *prophylactic* neutralisation: antibody and IL-33 were added to endothelial cells at the same time.
- **Re-scope** AX-1177 as a type-2-independent, endothelial IL-33 blocker. The population is hospitalised patients with severe viral pneumonia and a high serum sST2. The intent is to prevent progression to ICU admission, invasive ventilation or death.
- **Fund only a gated package** (Gates 0–2, §5.2). It is mostly re-analysis of archived data, standard in vitro pharmacology and testing of banked sera, with pre-specified kill criteria.
  - Hold IND-enabling spend until Gates 1 and 2 are passed.
  - If either gate fails, drop the asset.

### Why keep: three pillars

1. **The drug does exactly what it should, and nothing else we can detect.**
   - IL-33red drives a large NF-κB inflammatory programme in primary human endothelium: 4,031 genes at 6 h and 1,836 at 24 h (HUVEC).
   - Measured against the isotype control, AX-1177 neutralises a median **97%** of the response of genes induced more than 2-fold at 6 h (n = 644; residual versus vehicle 2%). The figure is **99%** for genes induced more than 8-fold.
   - It also blocks the IL-33-dependent response in a second vascular bed, glomerular microvascular cells (HGMEC).
   - On its own, AX-1177 has no reproducible transcriptional effect across four cell types and two time points.
2. **The IL-33 pathway is linked to outcome in patients.**
   - Serum **sST2**, the IL-33 decoy receptor and the only IL-33-pathway-specific analyte in our data, ranks **2nd of 1,094 assays** for ICU, ventilation or death within 30 days.
   - OR 3.02 per log unit (95% CI 1.83–5.01), FDR 0.007, adjusted for age, sex and NEWS2 at enrolment. It therefore adds information beyond clinical severity.
3. **A drug-reversible signature is visible in patient serum, and a biomarker strategy is ready to use.**
   - 23 outcome-associated serum proteins are transcripts that IL-33 induces and AX-1177 reverses.
   - The most robust are **OPG** (replicated on 2 panels), **IL-6** (4 panels) and **CCL20**. Each is strongly induced, still induced at 24 h, about 100% neutralised, and reversed in both endothelial beds at 6 h.
   - This gives sST2 for patient enrichment and OPG/IL-6/CCL20 for pharmacodynamics (§5.3).

### Why not as-is: the gaps the committee will probe

1. **We have no evidence that neutralising IL-33 *after* its release changes anything.** That is the situation in hospitalised patients. No delayed-addition, dose–response or potency data exist in this dump.
2. **We have no clinical data outside SARS-CoV-2, and none from the current, vaccinated era.**
3. **Serum reflects the IL-33 endothelial programme only partly.**
   - 34 serum proteins are strongly (more than 4-fold) IL-33-induced and AX-1177-reversed in vitro. Only 8 of them are outcome-associated.
   - CXCL5, CXCL6, G-CSF, TNF, CXCL10 and CX3CL1 are not.
   - So the data support IL-33 as *a* component of severity, not *the* driver.
4. **Several key pieces of biology are untested:**
   - the oxidised form of IL-33, which AX-1177 is stated to bind and which is its differentiating feature;
   - the lung microvasculature and airway epithelium;
   - efficacy in any in vivo model.

### If the committee drops it, this is what we are dropping

We would drop a clean, fully neutralising IL-33 antibody with a defined biomarker path in severe viral pneumonia. The reasons would be:

- We cannot show that blocking IL-33 after release helps.
- We cannot show the sST2 signal exists beyond a pre-vaccination COVID-19 cohort.
- Most of the severe-disease proteome, including the top hit HGF, is not IL-33-driven.

That is a defensible drop. However, the uncertainties behind it are cheap to resolve, which is why we recommend keeping the asset with gates.

---

## 2. What our data can and cannot answer

| Dataset | What it is | Can answer | Cannot answer |
|---|---|---|---|
| In vitro RNA-seq (mmc4, mmc5) | Cells: HUVEC and HGMEC (one donor each). Treatment: ± IL-33red 30 ng/mL, ± AX-1177 or isotype 10 µg/mL, antibody added at the same time as IL-33. Time points: 6 h and 24 h. Epithelial lines A549 and MCF7 received antibody only. n = 3 per arm; 114 libraries; one pooled limma model | Does AX-1177 neutralise IL-33red-driven endothelial transcription? Is AX-1177 inert on its own? | Potency; therapeutic window; oxidised IL-33; epithelial or immune-cell IL-33 biology; lung microvasculature; in vivo efficacy |
| Serum proteomics (mmc2) | 100 hospitalised COVID-19 patients (56 non-events, 44 events, inferred); enrolment serum; Olink, 13 panels; logistic regression per assay for ICU, ventilation or death within 30 days, adjusted for age, sex and NEWS2 | Which circulating proteins carry prognostic information beyond clinical severity? | Causality; other viruses; kinetics; response to drug |
| Post-mortem IHC (mmc3) | 31 donors, 74 blocks: COVID+ pneumonia 16, COVID− pneumonia 10, COVID− non-pneumonia 5. IL-33 scored in basal epithelium, endothelium and vascular smooth muscle; eosinophil, neutrophil and mast-cell markers. Single reader | Where IL-33 is stored in elderly lungs | Differences between groups: labels are unreliable, numbers are small, and this is end-stage tissue |

---

## 3. The evidence

### 3.1 AX-1177 neutralises IL-33red-driven endothelial activation near-completely and cleanly (Figures 1 and 3)

**IL-33red drives a broad endothelial activation programme in HUVEC:**
- NF-κB machinery: NFKBIA, TNFAIP3, TRAF1, RELB, BIRC3.
- Cytokines and chemokines: TNF, GM-CSF (CSF2, +10.3 log2), IL6, IL1B, CXCL1/2/3/5/6/8, CCL20.
- A procoagulant switch: tissue factor (F3) +5.6 log2, PAI-1 (SERPINE1) up, thrombomodulin (THBD) −1.0 log2.
- OPG (TNFRSF11B) +4.8 log2.

**AX-1177 reverses it, measured against the isotype-matched arm:**
- 2,884 of 4,031 IL-33-responsive genes (72%) are significantly reversed at 6 h; 694 of 1,836 (38%) at 24 h.
- Only 12 and 6 genes, respectively, move further in the IL-33 direction.

**Neutralisation is essentially complete for induced genes:**

| Time point | Genes induced >2-fold | Median neutralisation | Residual vs vehicle | Genes induced >8-fold |
|---|---|---|---|---|
| 6 h | n = 644 | 97% | 2% | 99% |
| 24 h | n = 314 | 85% | 16% | 92% |

IL-33-repressed genes recover less completely: 73% at 6 h and 48% at 24 h.

**Second vascular bed (HGMEC).** AX-1177 changes 1,460 genes against isotype at 6 h and 269 at 24 h. The IL-33-dependent (AX-1177-reversible) response is about **40%** of the HUVEC magnitude at 6 h and about **5%** at 24 h. Microvascular responses are therefore smaller and shorter-lived, which matters for the lung (§4).

**AX-1177 alone is transcriptionally inert.**
- Antibody-only contrasts give 14–73 genes at FDR < 0.05 each, out of 26,210.
- None reproduces across cell types or time points, and none is an IL-33-pathway gene.
- The extreme p-values in the epithelial contrasts are variance artefacts on changes smaller than 0.2 log2 (e.g. AKR1C2 log2FC 0.11, t = 169).

**Caveats:**
- One antibody concentration, about a 41-fold molar excess over IL-33.
- Antibody added at the same time as IL-33, so this is a model of prophylaxis, not treatment.
- One donor per cell type.
- Only the reduced form of IL-33 was tested.
- The correct comparator is the isotype-matched arm. The isotype arm responds less to IL-33 than IL-33 alone (84% of the IL-33-alone response for up-regulated genes at 24 h), so contrasts against IL-33 alone overstate the drug effect.

![Figure 1. IL-33red response in HUVEC versus the AX-1177 effect against isotype, at 6 h and 24 h. Right panel: size of the AX-1177-reversible response in HGMEC relative to HUVEC.](figures/fig1_invitro_neutralisation.png)

### 3.2 sST2, the IL-33 pathway marker, is among the strongest independent predictors of severe COVID-19 (Figure 2)

- 178 of 1,094 assays are associated with ICU, ventilation or death at FDR < 0.05. After reconciling duplicate assays, that is **169 unique proteins**. There were 44 events in 100 patients.
- **sST2 ranks 2nd:** OR 3.02 (1.83–5.01) per log unit, p = 1.7 × 10⁻⁵, FDR 0.007, adjusted for age, sex and NEWS2.
- **HGF ranks 1st** (FDR 0.004). In our data HGF is not IL-33-responsive in endothelium (log2FC 0.5, FDR 0.70).
- **The type-2 axis is silent:**
  - IL-5: OR 1.00, p = 0.997.
  - Eotaxin-1: p = 0.84 and 0.96 on two panels; eotaxin-2: p = 0.58; CCL17: p = 0.39.
  - IL-4, IL-13, TSLP and IL-33 itself are absent from the delivery, most likely removed as below the limit of detection.
  - The IL-33 biology relevant to this disease is not type-2.
- **Classic endothelial adhesion and injury markers are not outcome-associated** after NEWS2 adjustment: VCAM1, ICAM1, E-selectin, thrombomodulin, ESM-1, TIE2 and PECAM1 all have FDR 0.09–0.95. vWF and ANGPT2 are borderline (FDR 0.050–0.052). The serum signal is carried by *secreted inflammatory mediators*, not by endothelial injury markers.
- **Caveats:**
  - This is a prognostic association from a single cohort.
  - sST2 also comes from sources other than IL-33 signalling (myeloid cells, epithelium, mechanical stress).
  - The per-log-unit ORs cannot be compared across assays (§7).

![Figure 2. Serum proteome at enrolment versus 30-day ICU, ventilation or death, reconciled to unique proteins. Colours give the in vitro IL-33/AX-1177 status of each protein.](figures/fig2_serum_bridge.png)

### 3.3 Part of the AX-1177-reversible endothelial programme is visible in patient serum (Figures 2 and 3)

**The overlap.** 23 outcome-associated proteins are IL-33-induced in HUVEC and reversed by AX-1177 against isotype. Three more (sST2, PTX3, IL-8) point the same way but cannot be tested in the delivered statistics (§7).

**Tier 1 markers: OPG, IL-6, CCL20.**

| Marker | Serum association | IL-33 induction (log2, 6 h / 24 h) | AX-1177 neutralisation | HGMEC reversal at 6 h |
|---|---|---|---|---|
| OPG | OR 6.8, FDR 0.014; replicated OR 4.4, FDR 0.020 on a second panel | +4.8 / +2.4 | about 100% at both time points | Yes |
| IL-6 | OR 2.07–2.31, FDR 0.012–0.019 on all 4 panels | +5.8 / +2.8 | about 100% | Yes |
| CCL20 | OR 1.83, FDR 0.020 | +9.2 / +5.6 | about 100% | Yes |

**Tier 2 markers:** IL-1β, CTSS, CSF-1, IL-18R1, MCP-3 and VEGF-A (serum FDR 0.018–0.046).

**Enrichment.**
- IL-33-induced, AX-1177-reversed genes that replicate in both endothelial beds are over-represented among outcome-associated proteins: 31% (17/54) versus 16% (132/814); OR 2.4, p = 0.008.
- The enrichment is weaker for HUVEC-only sets (OR 1.6, p = 0.08).
- It is absent for the most strongly induced set: 8/34 versus 141/834, p = 0.35.

**Interpretation.** IL-33-driven endothelial activation explains a *slice* of the severe-COVID proteome, not the bulk. The bridge markers are generic NF-κB outputs. They are valid as pharmacodynamic markers (change on drug versus placebo), but they are not proof of IL-33 activity in a given patient.

![Figure 3. Candidate bridge markers: IL-33 induction in HUVEC at 6 h and 24 h (left), and AX-1177 effect against isotype in both endothelial beds (right).](figures/fig3_marker_kinetics.png)

### 3.4 In tissue, IL-33 is abundantly stored but not specific to COVID (Figure 5)

- **Donor-level comparison** (31 donors; blocks aggregated to avoid pseudo-replication): no difference between COVID+ and COVID− pneumonia in IL-33 in endothelium (p = 0.20), basal epithelium (p = 0.96) or vascular smooth muscle (p = 0.19). Endothelial staining sits near the top of the scale in every group.
- **Disease labels are unreliable.** They contradict the autopsy pathology for 7 of 31 donors, and 2 more are queryable (§7).
- **After re-labelling from the pathology text,** endothelial IL-33 is lower in acute pneumonia of any cause than in lungs without pneumonia (p = 0.028 for COVID+, p = 0.039 for COVID−). This is compatible with release of IL-33 during acute injury, but it is not COVID-specific.
- This result is exploratory: about 20 tests were run, and endothelial and vascular-smooth-muscle IL-33 scores correlate with donor age (ρ = 0.57).
- **Bottom line:** the tissue data neither support nor refute the thesis. They do rule out tissue IL-33 as a patient-selection marker.

![Figure 5. Donor-level IHC. Top row: labels as delivered. Bottom row: groups re-assigned from the autopsy pathology text.](figures/fig5_ihc_donor_level.png)

---

## 4. Anticipated challenges, and the answer our data support

| Challenge | Answer |
|---|---|
| "sST2 is just a generic severity marker." | It remains prognostic after adjustment for NEWS2 and ranks 2nd of 1,063 unique proteins. We use it for *prognostic enrichment*, not as proof of causality. Whether it predicts benefit from AX-1177 must be tested in the trial as a treatment × sST2 interaction. |
| "IL-6 and OPG are generic NF-κB outputs." | Agreed. That is why they are pharmacodynamic markers, where specificity comes from the randomised drug-versus-placebo comparison. Gate 1c tests attribution: AX-1177 must not block TNF- or IL-1β-driven induction. |
| "Many IL-33-induced chemokines do not track with outcome." | True: 8 of 34 do. Our claim is therefore *a component*, not *the driver*. Gate 2 is designed to test whether the sST2/OPG component generalises. |
| "Antibody and IL-33 were added together, which is irrelevant to patients who already have disease." | Agreed. This is the biggest gap, and Gate 1a (delayed addition plus dose–response) is a kill gate. |
| "Only COVID-19." | Agreed. Gate 2 (RSV, influenza, hMPV, current-era COVID) is a kill gate. The tissue hint that IL-33 depletion is pathogen-agnostic (§3.4) is exploratory only. |
| "The RNA-seq statistics are broken." | For about 0.5% of genes (121), mostly cell-type-identity genes. The Tier-1 and Tier-2 markers are unaffected (SE 0.1–0.7 log2, against 3 to more than 16,000 for affected genes). The count matrices are archived, so a re-fit is cheap (Gate 0). |
| "The microvascular response is weaker." | True: HGMEC show about 40% of the HUVEC response at 6 h and about 5% at 24 h. Primary lung microvascular cells are mandatory in Gate 1. |
| "Why not pivot to COPD or asthma?" | Our data are silent or negative there. There is no epithelial IL-33 stimulation, no COPD or asthma patients, and IL-33 IHC is unrelated to COPD notes (p = 0.22–0.65), emphysema (p = 0.11–0.68) or asthma (p = 0.42–0.94). Such a pivot would be a decision on external evidence, not ours. |
| "Is it safe or specific?" | We found no reproducible transcriptional effect of AX-1177 alone and no agonism. This is a specificity result, not a toxicology assessment. |

---

## 5. Forward view

### 5.1 The indication our data point at

**What the data point towards:**
- **A mechanism:** endothelial and vascular, not airway type-2.
- **A severity level:** hospitalised patients, where the signal is prognostic beyond NEWS2.
- **A biomarker-defined subset:** sST2-high, possibly OPG-high.

**Proposed indication:** prevention of progression to critical illness (ICU, invasive ventilation, death) in hospitalised patients with severe viral pneumonia and an sST2-high, IL-33 endothelial-inflammatory phenotype.
- This is a narrower, enrichment-defined version of the current indication, not a departure from it.
- Strictly, SARS-CoV-2 is the only setting where our data show a clinical link.
- If Gate 2 shows the sST2/OPG signal is pathogen-agnostic, the adjacent indication is **severe community-acquired pneumonia or ARDS regardless of pathogen**. The mechanism is pathogen-agnostic, and the tissue data hint the same.

A positioning argument, partly external: in endothelium, AX-1177 shuts off IL-33-driven induction of IL-6, GM-CSF, IL-1β and TNF together. These are mediators that have been targeted individually in severe COVID-19.

**What the data do not point at:**
- all-comers or outpatient viral LRTD;
- asthma, COPD or any type-2 indication;
- kidney or cardiovascular indications (no clinical data; KIM-1 FDR 0.11, NT-proBNP FDR 0.15–0.33);
- selection of patients by tissue IL-33.

### 5.2 What the next studies must establish: a gated plan

**The next studies must establish six things, in order of importance:**

1. AX-1177 still works when given *after* IL-33 has been released (a therapeutic window), and it neutralises oxidised IL-33 as well as the reduced form.
2. The IL-33-dependent endothelial programme exists in **lung microvascular** cells, and virus-infected airway epithelium can trigger it.
3. The PD markers (OPG, IL-6, CCL20) move because of IL-33 specifically, not because of inflammation in general.
4. The sST2 (± OPG) prognostic signal replicates outside SARS-CoV-2 and in the current treatment era.
5. In vivo biomarker kinetics, to set the PD sampling schedule.
6. A free/total IL-33 target-engagement assay that works in patient samples.

Durations are indicative planning estimates, not derived from our data.

**Gate 0: data remediation (weeks; no new wet work)**
- **(a)** Re-fit the archived RNA-seq counts per cell type (or with group-specific variances). Obtain valid statistics for IL1RL1/ST2, PTX3, CXCL8, SELE, VCAM1, ICAM1, CCL2 and VWF.
- **(b)** Obtain patient-level Olink NPX data and compute:
  - per-SD ORs;
  - incremental AUC over NEWS2;
  - correlations among sST2, OPG, IL-6 and HGF;
  - bootstrap validation;
  - why IL-33 was excluded;
  - corticosteroid and IL-6R-blocker exposure.
- **(c)** IHC: correct the labels from pathology, add a second blinded reader, and report raw grades.
- Gate 0 does not kill the asset. It fixes the marker list.

**Gate 1: in vitro pharmacology that mirrors the clinic (about 3 months). Kill gate.**
- **(a)** Dose–response (IC50 and IC90) against IL-33red and IL-33ox. Compare AX-1177 pre-incubated, added at the same time, and added **1, 3 and 6 h after** IL-33.
- **(b)** Primary human **lung microvascular** endothelial cells (at least 3 donors) alongside HUVEC. Measure secreted OPG, IL-6, CCL20, sST2, PTX3 and IL-8 at 6 h and 24 h.
- **(c)** Specificity: stimulate with TNF-α or IL-1β ± AX-1177. AX-1177 should not block, which confirms the PD markers are attributable to IL-33.
- **(d)** Primary bronchial epithelial air–liquid-interface cultures ± RSV, influenza or SARS-CoV-2. Test whether their conditioned medium drives an AX-1177-sensitive endothelial response.
- **Kill criterion:** if AX-1177 added at 3 h or later does not reduce secreted OPG, IL-6 or CCL20 by at least 50% at plausible exposures, *and* virus-conditioned epithelial medium does not produce an AX-1177-sensitive endothelial response, there is no rationale for treating hospitalised patients. Drop.

**Gate 2: clinical biomarker replication on banked samples (about 6 months, in parallel with Gate 1). Kill gate.**
- **(a)** At least two independent cohorts of hospitalised viral LRTD (RSV, influenza, hMPV and current-era COVID-19). Use admission serum and the same composite endpoint. Pre-specify sST2 and OPG, adjusted for NEWS2, age and sex, and report incremental AUC and a cut-point.
- **(b)** Optionally, a non-viral severe CAP or ARDS cohort to test whether the signal is pathogen-agnostic.
- **(c)** Serial sampling (admission, 24 h, 72 h, day 7) to learn in vivo kinetics; this sets the PD schedule.
- **Kill criterion:** if sST2 is not independently prognostic in non-COVID viral LRTD (CI including OR = 1 after adjustment), the viral-LRTD thesis fails. Pursue the pathogen-agnostic option only if 2(b) is positive.

**Gate 3: clinical (only after Gates 1 and 2 pass)**
- Phase 1b/2a in sST2-high hospitalised viral pneumonia.
- Endpoints: safety, PK and PD (OPG, IL-6 and CCL20 change from baseline versus placebo), plus exploratory clinical outcomes.
- Test the treatment × sST2 interaction.

### 5.3 Biomarkers: which can go into patients, and in what role

| Marker | Evidence in our data | Role | Into patients? |
|---|---|---|---|
| **sST2** | Rank 2; OR 3.02 (1.83–5.01), FDR 0.007, NEWS2-adjusted. Transcript +1.6 log2 with IL-33 and fully reversed, but untestable in the delivery | **Prognostic enrichment / patient selection.** Exploratory PD after Gate 0 | **Yes, now.** Serum; clinical-grade assays exist (external). Predictive value unproven |
| **OPG** | Two panels (FDR 0.014 and 0.020). +4.8 / +2.4 log2 at 6 h / 24 h; about 100% neutralised; HGMEC-replicated | **Primary pharmacodynamic (pathway-modulation) marker.** Secondary enrichment candidate | **Yes** (exploratory PD) |
| **IL-6** | Four panels (FDR 0.012–0.019). +5.8 / +2.8 log2; about 100% neutralised | **Supportive PD only.** Not for selection: non-specific, and confounded by standard of care (steroids lower it; IL-6R blockade raises serum IL-6) | Yes, with caveats |
| **CCL20** | FDR 0.020. +9.2 / +5.6 log2; about 100% neutralised; HGMEC-replicated | **Exploratory PD** (largest dynamic range) | Yes (exploratory) |
| IL-1β, CTSS (persist at 24 h); CSF-1, IL-18R1, MCP-3, VEGF-A (mostly 6 h only) | Serum FDR 0.018–0.046; IL-33-induced and reversed | Exploratory PD panel | Exploratory. Transient markers will be missed at a 24 h draw |
| PTX3, IL-8 | Strong serum associations; in vitro untestable | Hold | After Gate 0 |
| GM-CSF (CSF2) | Strongest secreted in vitro marker (+10.3 / +8.1 log2; reversed in both beds at both time points); **not on our serum panels** | Candidate PD | After a sensitive assay is confirmed |
| HGF | Rank 1 prognostic; **not IL-33-linked** | Prognostic covariate only | Yes, as covariate |
| Free and total IL-33 (reduced and oxidised) | Absent from the delivery (below-LOD filter inferred) | Target engagement | Needs assay development |
| NF-κB transcripts (NFKBIA, TNFAIP3, TRAF1) | Cleanest in vitro readout (t up to 44) | In vitro potency / ex vivo PD assay | No (intracellular) |
| Tissue IL-33 IHC; type-2 markers (IL-5, eotaxins, eosinophils) | Near ceiling or label-dependent (tissue); null (serum) | None | No |

### 5.4 Sampling time points

**Patient selection: at enrolment (hospital admission), before the first dose.** This is the only time point at which our cohort links biomarkers to outcome (30-day composite, adjusted for NEWS2 at enrolment).

**Pharmacodynamics: first on-treatment draw at about 24 h.**
- Our in vitro kinetics show the IL-33-dependent signal is front-loaded: 4,031 genes at 6 h versus 1,836 at 24 h, and the microvascular signal is largely gone by 24 h.
- At a practical clinical draw, only markers that stay IL-33-dependent at 24 h are usable: **OPG, IL-6, CCL20, IL-1β, CTSS** (and GM-CSF if assayable).
- Later draws (e.g. 72 h, day 7) should be set from PK and Gate 2 kinetics. Our data cannot determine them.

**In vitro (Gate 1):** read transcripts at **6 h** (peak signal, most complete reversal) and secreted proteins at **24 h** (accumulated protein).

---

## 6. What we considered and ruled out

| Considered | Verdict | Reason from our data |
|---|---|---|
| Keep the all-comers viral LRTD thesis | Not supported | One virus, pre-vaccination, one centre; the association is prognostic only; the in vitro work models prophylaxis only |
| Drop now | Not recommended | Clean, complete pharmacology; sST2 ranks 2nd independent of NEWS2; a coherent biomarker path; decisive next steps are cheap |
| Type-2 (eosinophil/ILC2) mechanism | Ruled out | IL-5, eotaxin-1/2 and CCL17 null in serum; IL-4/IL-13/TSLP absent from the delivery (likely below detection); tissue eosinophil results flip with label correction (EDN p = 0.005 → 0.175, direction reversed) |
| Pivot to asthma or COPD | Not supported by our data | No relevant cells or patients; IHC shows no association with COPD, emphysema or asthma |
| Kidney or cardiovascular repositioning | Not supported | HGMEC respond, but there are no renal or CV clinical signals (KIM-1 FDR 0.11; NT-proBNP FDR 0.15–0.33) |
| Tissue IL-33 IHC for patient selection | Ruled out | Near ceiling; no COVID difference; label-dependent; invasive |
| HGF as a PD marker | Ruled out | Not IL-33-inducible (log2FC 0.5, FDR 0.70) |
| Endothelial injury/adhesion markers (VCAM1, ICAM1, E-selectin, TM, ESM-1, TIE2, PECAM1) as the clinical bridge | Not supported | Not outcome-associated after NEWS2 adjustment (FDR 0.09–0.95) |
| "AX-1177 has off-target effects" | Ruled out | Antibody-only hits are not reproducible; extreme p-values are variance artefacts |
| "IL-33 does not induce SELE, VCAM1, ST2 or PTX3" (as the delivered p-values imply) | Ruled out as a conclusion | Artefact of the pooled model (SE 7–11 log2 units). Point estimates are large and fully reversed by AX-1177 |
| AX-1177+IL-33 versus IL-33 alone as the measure of drug effect | Rejected | Overstates the effect because the isotype arm responds less; the isotype-matched contrast is used throughout |
| A549/MCF7 as evidence of epithelial IL-33 biology | Rejected | They received no IL-33; MCF7 is a breast line; DMSO is an irrelevant vehicle for an antibody. Useful only as specificity controls |
| Comparing Olink OR magnitudes across assays | Rejected | ORs are per log unit of differently scaled NPX variables (e.g. CSF-1 OR 90, CI 4–1,933). We rank by z and p instead |

---

## 7. Data-integrity issues the committee should know about

We treated the files as ground truth. The following are places where the files are internally inconsistent, or where the analysis design limits inference. All are fixable. Full log: workbook sheet 11.

1. **mmc5 sheet names are wrong.**
   - The "6h" and "24h" sheets each contain *the same* 24 contrasts, covering both time points; they are value-for-value identical (629,040 rows each).
   - The "6h" sheet is padded with 419,535 blank rows up to Excel's 1,048,576-row limit, which looks like truncation but is not. No data were lost.
2. **The RNA-seq statistics come from a single voom/limma model pooled across four unrelated cell types (Figure 4).**
   - 121 genes have median standard errors of 3 to more than 16,000 log2 units across the endothelial contrasts; for 110 of them the SE exceeds 3 in every endothelial contrast. These are the cell-type-restricted genes, including IL1RL1 (ST2), PTX3, SELE, VCAM1, CXCL8, CXCL1, CCL2, VWF, ESM1, PECAM1 and KDR. Their p-values are meaningless (e.g. SELE log2FC 11.2, p = 0.21).
   - Some of the same genes show the opposite problem in the epithelial contrasts, with collapsed variance (e.g. AKR1C2 log2FC 0.11, t = 169).
   - AveExpr is averaged over all four cell types.
3. **Design gaps:**
   - HGMEC has no vehicle arm, so the IL-33 effect there cannot be estimated directly.
   - The epithelial lines never received IL-33.
   - There is no dose–response, no delayed addition, no oxidised-IL-33 arm, and only one donor per primary cell type.
4. **Olink (mmc2):**
   - 27 proteins are measured on 2–4 panels (58 rows) and were not reconciled. BH correction was applied across the duplicates. In fairness, the duplicates agree closely, which is a useful internal replication.
   - IL-33 itself is absent.
   - Two columns are undocumented. Their values step in 1/56 and 1/44 and never exceed about 9%, consistent with an undocumented below-LOD filter.
   - ORs are "per log unit" of NPX, which is already log2, and the log base is unspecified.
   - There is no AUC, multivariable or validation analysis.
5. **IHC (mmc3):**
   - A formula is stored as text (`=(2+4.5)/2`).
   - Numeric scores are the ordinal grade plus 0.5, so "5+" becomes 5.5, outside the stated 0–5 scale.
   - The IL-33 columns appear to average raw and converted grades.
   - Some cells contain "ND" or trailing spaces, and there are blank spacer rows.
   - **Disease labels contradict the pathology text for 7 of 31 donors (2 more queryable).** Conclusions change with correction.
   - There are 1–8 blocks per donor, so block-level tests overstate evidence (IL-5Rα p = 0.025 at block level versus 0.49 at donor level).

![Figure 4. The pooled single-model fit gives cell-type-restricted genes uninformative standard errors in the endothelial contrasts.](figures/fig4_variance_artefact.png)

---

## 8. Method notes

**Transcriptomics:**
- All 26 delivered contrasts were merged by Ensembl ID. The two mmc5 sheets were verified identical.
- Internal consistency was checked: BH adjustment reproduces exactly, and p-values are consistent with t at about 85 degrees of freedom.
- The drug effect is the isotype-controlled contrast (AX-1177+IL-33 versus NIP228+IL-33).
- Neutralisation = −(drug effect) ÷ (isotype-arm IL-33 response), where the isotype-arm response is reconstructed from the linear contrasts of the single fitted model.
- "Testable" means an implied SE below 1.5 log2.

**Serum proteomics:**
- Assays were mapped to HGNC genes, with panel suffixes stripped and Olink names mapped manually.
- The best panel per protein is reported.
- Enrichment used Fisher's exact test over the 868 Olink proteins with a testable endothelial transcript.

**IHC:**
- Ordinal grades were parsed; the formula was evaluated; "ND" was treated as missing.
- Blocks were aggregated to the donor median, and groups compared by Mann–Whitney.
- Groups were re-assigned from the pathology text as a sensitivity analysis.

**Scripts** that regenerate every number, table and figure from the raw files are in `code/` (run `code/run_all.sh`).

**Files:**
- `AX-1177_portfolio_position.md` / `.pdf` / `.html`: this memo.
- `AX-1177_supporting_tables.xlsx`: 12 sheets, including the biomarker plan, bridge markers, all 1,063 unique proteins with in vitro annotations, neutralisation summary, untestable genes, IHC donor-level data and label audit, the issue log, and what was considered and ruled out.
- `figures/`: Figures 1–5.
