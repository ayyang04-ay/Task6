---
title: "AX-1177 (anti-IL-33 mAb): portfolio audit position"
subtitle: "Recommendation, evidence, forward view and biomarker plan, based only on the AX-1177 data files"
---

**Scope.** This memo uses only the five AX-1177 files: the methods annex, the HUVEC IL-33 RNA-seq file, the 24-contrast RNA-seq file, the serum Olink proteomics file (n = 100) and the post-mortem lung IHC file (31 donors, 74 blocks). I re-derived every number below from those files. Code and tables are in `code/` and `tables/`. Compound_47 = AX-1177 and IC119 = isotype control, as stated in the annex.

# 1. Bottom line

**Recommendation: KEEP AX-1177, but re-scope it and put it behind a gate. Don't carry it forward on its current indication.**

Our data support two claims:

* **The drug works on its target, and cleanly.** AX-1177 blocks reduced-IL-33 signalling in human endothelium with no off-target transcriptional signal.
* **There is a credible human reason to care.** sST2, the IL-33 decoy receptor, ranks 2nd of 1,094 serum proteins for predicting ICU admission, ventilation or death in hospitalised COVID-19.

Our data do **not** support two others:

* **That IL-33 itself is elevated or active in patients.** We have no direct measurement showing this.
* **The breadth of the current label, "severe lower respiratory viral infection".** Every patient datapoint we have is either COVID-19 (pre-vaccination, one centre) or pneumonia that isn't specific to a virus.

The defensible position has four parts:

1. **Re-scope the indication.** Move from "severe lower respiratory viral infection" to *IL-33-driven endothelial activation in hospitalised severe pneumonia, enriched for high serum sST2*. This is the one compartment (vascular endothelium) and the one population (hospitalised COVID-19) where we actually have evidence.
2. **Gate the asset on one decisive question.** *Does patient material contain IL-33 activity that AX-1177 neutralises?* We can answer it in about 6 months, mostly with samples and data we already own. The kill criteria should be agreed in advance (Section 7).
3. **No IND-enabling or clinical spend** until Gate 1 is passed.
4. **If the committee won't fund the gate, drop the asset.** Section 4 states what we would be dropping and why.

## Evidence scorecard

| Claim | What our data show | Strength |
|---|---|---|
| AX-1177 neutralises IL-33 (reduced form) in human endothelium | 4,031-gene IL-33 programme in HUVEC. The top 100 genes are 100% inhibited at 6 h and 98% at 24 h versus isotype. Reversed in a second endothelial type (HGMEC) | **Strong** (but only one IL-33 form, single donors, one dose) |
| AX-1177 is specific | With no IL-33 present, 14–73 scattered genes change per contrast, and none reproduce across 4 cell lines × 2 timepoints | **Strong** (transcriptome level) |
| The IL-33 axis tracks severe outcome | sST2 ranks 2/1,094: OR 3.0 (95% CI 1.8–5.0), FDR 0.7%, adjusted for NEWS2. Cardiac strain markers don't explain it | **Moderate** (indirect marker, one centre, COVID-19 only) |
| IL-33 is present where the drug acts | Abundant in lung endothelium and basal epithelium in all 31 donors | **Moderate** |
| IL-33 is released or active in patients | Not shown. IL-33 wasn't in the delivered serum data, and IHC isn't increased in COVID-19 | **Absent (this is the gap)** |
| The IL-33 endothelial programme drives the serum severity signal | As a set it is **not** enriched beyond a proteome-wide shift. Response size in vitro doesn't predict prognostic value (ρ = −0.08) | **Not supported** |
| Virus- or COVID-specific biology | COVID-19 and non-COVID pneumonia lungs look the same for IL-33 and inflammatory cells | **Not supported** |
| Type-2 / airway (asthma, COPD) relevance | No type-2 serum signal, and IL-33 IHC shows no association with COPD, asthma or emphysema | **Not supported** |

# 2. The case for keeping it

## 2.1 The drug works, specifically (Figures 1 and 2)

**IL-33 turns on a large inflammatory programme in endothelium.**

* Reduced IL-33 (30 ng/mL) changes 4,031 genes in HUVEC at 6 h (FDR < 5%), falling to 1,836 at 24 h.
* The top genes are canonical IL-1-family/NF-κB targets: NFKBIA, RIPK2, TNFAIP3, TRAF1, RELB, NFKB1/2 and IRAK2.
* Secreted products include GM-CSF, G-CSF, CXCL2/3/5/6, CCL20, CX3CL1, IL-6 and OPG.
* IL-33 also shifts endothelium towards clotting: tissue factor +5.6 log2, PAI-1 +1.7 log2, thrombomodulin −1.0 log2.

**AX-1177 abolishes that programme.** In the isotype-matched comparison (AX-1177 + IL-33 vs isotype + IL-33, which shares no arm with the IL-33 signature):

* The genome-wide correlation with the IL-33 response is r = −0.80 at 6 h.
* The 100 most responsive genes are inhibited by a median 100% (IQR 97–103) at 6 h and 98% (IQR 92–106) at 24 h.
* This held despite a conservative design: the antibody was added at the same time as IL-33, with no pre-incubation.

**The effect carries over to a second, microvascular cell type.** In HGMEC, the isotype-matched reversal moves 1,460 genes at 6 h, anti-correlated with the HUVEC IL-33 signature (r = −0.66). 39 genes form a robust core: induced at both timepoints, ≥90% inhibited at both, and also reversed in HGMEC (`tables/exvivo_PD_core_gene_panel.csv`).

**The response is not an endotoxin artefact.** An anti-IL-33 antibody cannot neutralise LPS, yet it removes about 100% of the response.

**The antibody is inert on its own.**

* Without IL-33, AX-1177 shifts only 14–73 genes per contrast across HUVEC, HGMEC, A549 and MCF7 at both timepoints.
* These are low-count lncRNAs or ±0.1-log2 changes in housekeeping genes, with no coherent pathway.
* Antibody-alone contrasts correlate at r ≈ 0.5 only when they share the same AX-1177 arm, which is what a shared n = 3 arm produces by chance. Across cell types and timepoints r ≈ 0.
* Conclusion: no detectable off-target transcriptional activity.

## 2.2 Patients with bad outcomes carry the IL-33-axis footprint (Figures 3 and 4)

**sST2 (IL1RL1), the IL-33 decoy receptor, is one of the strongest severity markers we measured.**

* It ranks 2nd of 1,094 serum assays for ICU admission, invasive ventilation or death within 30 days.
* OR 3.02 per unit (95% CI 1.83–5.01), p = 1.7 × 10⁻⁵, FDR 0.7%.
* This is adjusted for age, sex and NEWS2, so it adds to bedside severity scoring.
* It is not just cardiac strain: in the same samples NT-proBNP (p = 0.05 and 0.17 on two panels) and troponin I (p = 0.11) are unremarkable.

**Several IL-33-inducible, AX-1177-reversible endothelial products are also in the top few percent:**

* PTX3: rank 6.
* IL-6: rank 11, consistent across all four panels that measure it (OR 2.07–2.31).
* OPG: rank 16, consistent on two panels.
* IL-18R1, MCP-3 and CCL20: CCL20 is rank 46 (FDR 2%).
* IL-8: rank 89.

CCL20, OPG and IL-6 are also in the 39-gene robust in vitro core. That makes them the best bridges between the mechanism and patients.

## 2.3 The target sits where the mechanism acts (Figure 5)

**IL-33 protein is present in every donor.** It is abundant in lung vascular endothelium and bronchial basal epithelium in all 31 donors. Endothelial scores hit the top of the scale in 39 of 74 blocks.

**Vascular IL-33 is lower, not higher, in COVID-positive and injured lungs.** All comparisons use donor-level tests:

* Endothelium, COVID-positive vs rest: p = 0.05 (GEE p = 0.03).
* Endothelium, acute pneumonia vs none: p = 0.03.
* Vascular smooth muscle, COVID-positive vs rest: p = 0.07 (GEE p = 0.03).
* Endothelial IL-33 falls as inflammatory infiltrate rises: ρ = −0.41 to −0.51 against neutrophil elastase, IL-5Rα-positive cells and H&E eosinophils.

IL-33 is a nuclear alarmin, so losing it at injured sites is the pattern you would expect if it is being released. This fits the hypothesis but doesn't prove it. The p-values are uncorrected and the IHC data have quality problems (Section 10).

## 2.4 Why keep rather than drop now

* **Nothing in our data contradicts the hypothesis.** "IL-33 not detected in serum" is a delivery gap, not a negative result. The BH arithmetic in the serum file shows 1,194 assays were tested but only 1,094 were delivered. 102 panel assays are absent, so at most 2 were never tested, and IL-33 is one of the 15 Inflammation-panel assays missing. It was therefore very likely run but withheld (Section 10). Lower tissue staining at injured sites is compatible with release.
* **The decisive unknown is cheap to resolve.** It needs stored enrolment sera, the archived RNA-seq counts and the existing tissue blocks.
* **Dropping now forfeits the option without learning anything.**

# 3. What the data don't show: likely challenges and answers

| Likely challenge | What our data say | Answer / action |
|---|---|---|
| "Is IL-33 actually raised in these patients?" | Not shown. It isn't in the delivered serum data, and IHC shows no increase (if anything, lower vascular staining) | Retrieve the withheld IL-33 result. Measure free, total, reduced and oxidised IL-33 in stored sera (Gate 1) |
| "sST2 is non-specific" | True. It also rises with other inflammatory stimuli. As a decoy, high sST2 could even mean *less* free IL-33 | Use sST2 for **prognostic enrichment**, not as proof of mechanism. Test whether it predicts AX-1177 benefit |
| "Everything is raised in sick patients" | True: 82% of proteins have OR > 1 and 35% have nominal p < 0.05 (5% expected). The IL-33 endothelial programme as a set is not enriched beyond this shift (Fisher p = 0.69; ρ = −0.08) | Claim only the outliers: sST2 (99.9th percentile), PTX3 (99.5th), IL-6 (99th), OPG (98.6th), CCL20 (96th) |
| "HUVEC is not lung" | Correct. HUVEC is umbilical vein from one donor (P2). HGMEC is one donor (P5) with no vehicle arm | Use primary lung microvascular endothelium from ≥ 3 donors (Stage 1) |
| "The differentiating feature, oxidised-IL-33 binding, was never tested" | Correct. Only reduced IL-33 was used. A549 and MCF7 never received IL-33. sRAGE (p = 0.055) and EGFR (p = 0.78) show no serum signal | Oxidised IL-33 on primary airway epithelium ± AX-1177 (Stage 1) |
| "Is this virus or COVID biology?" | No evidence it is. COVID-19 and non-COVID pneumonia lungs don't differ in IL-33 or inflammatory cells (all p ≥ 0.15) | Re-scope to pneumonia with endothelial activation. Test non-COVID pneumonia (Stage 2) |
| "These are 2020 data" | One centre, pre-vaccination, COVID-19 only. Standard of care now includes dexamethasone and IL-6R/JAK blockade | Contemporary, multi-pathogen replication cohort (Stage 2) |
| "What dose?" | Unknown. One antibody concentration (10 µg/mL ≈ 68 nM, about 41-fold molar excess over 1.7 nM IL-33), no titration. Affinity data are held outside this dataset | 8-point titration: IC50/IC90, with pre-incubated, concurrent and delayed addition (Stage 1) |
| "Could blocking IL-33 hurt antiviral defence?" | IL-33 induces an interferon-stimulated gene (ISG) programme in endothelium by 24 h (GBP5, MX1/2, IFIT1, RSAD2, IFI6, CXCL10), and AX-1177 blocks it | Viral load and ISG score as safety markers. Infection-model check (Stage 2) |

# 4. If we drop it: what we're dropping and why

**What we'd be dropping:**

* A specific anti-IL-33 antibody, annotated as binding both reduced and oxidised IL-33, that works cleanly in our hands.
* It completely blocks IL-33-driven inflammatory and pro-coagulant activation in HUVEC, and reverses it in glomerular microvascular endothelium (HGMEC).
* It comes with an enrichment biomarker, sST2, that is highly prognostic in hospitalised COVID-19.
* In short: an option on a host-directed, endothelium-protective therapy for severe pneumonia.

**Why dropping would be defensible:**

1. Nothing shows that IL-33 is released or active in patients.
2. The human link is indirect (a decoy receptor), and the pathway-level serum signal can't be told apart from generic severity.
3. All clinical data are COVID-19, pre-vaccination and from one centre, so the broad viral-LRTI label is an extrapolation.
4. The pharmacology covers one IL-33 form in non-lung endothelium, at one dose, with no potency data.

**What dropping now would cost:** we could no longer settle the key question with material we already own, and the differentiating (oxidised-IL-33) hypothesis would stay untested.

# 5. Forward view: where our data actually point

**The data point to the vascular endothelium in severe pneumonia, not to the airway, and not to viruses specifically.**

* **Mechanism.** Endothelium is the only compartment where we have shown IL-33 biology and AX-1177 pharmacology (HUVEC and HGMEC).
* **Tissue.** IL-33 is most abundant in endothelium, and only the vascular compartments change with injury. Basal epithelial IL-33 is flat (p = 0.76).
* **Patients.** The prognostic signal is sST2 plus endothelial and inflammatory outputs: PTX3, IL-6, OPG, CCL20 and IL-8. Tissue factor, vWF and ANGPT2 sit around the 82nd–84th percentile.
* **Not virus-specific.** At tissue level, COVID-19 and non-COVID pneumonia are indistinguishable.

**Proposed indication hypothesis:** *hospitalised severe pneumonia with high sST2 / endothelial activation*. This would be a host-directed, endothelium-protective therapy, developed first in hospitalised COVID-19 (the only population with outcome data). Whether it extends to other viral and non-viral pneumonia and ARDS is a Stage 2 question.

Compared with the current label, this is narrower on mechanism, broader on cause, and defined by a biomarker.

**Not supported by our data:**

* Asthma or COPD (Section 9).
* Kidney disease.
* Cardiac disease.
* Fibrosis: only a 5-donor hint.

# 6. What the next studies must establish

* **E1 – Target present in the right form.** Bioactive IL-33 (free and total, reduced and oxidised) is measurably released in the target patients, and relates to outcome and/or sST2.
* **E2 – Target relevant in human disease.** Patient material contains endothelial-activating activity that **AX-1177 neutralises** (and isotype does not). This is the single most decisive experiment.
* **E3 – Pharmacology in relevant cells.** Potency (IC50/IC90) in primary lung microvascular endothelium and primary airway epithelium, from ≥ 3 donors, for both IL-33 forms, with pre-incubated, concurrent and delayed addition.
* **E4 – A biomarker that holds up.** sST2's prognostic value, and a PD panel, replicate in an independent, contemporary, multi-pathogen cohort with serial sampling that defines the time window.
* **E5 – Safety of the mechanism.** Blocking IL-33 does not blunt antiviral ISG responses or viral clearance.

# 7. Plan, gates and kill criteria

**Stage 0 (weeks 0–6, desk work and data requests):**

* Retrieve the roughly 100 tested-but-undelivered serum results (including IL-33, TSLP, IL-4, IL-13 and the Inflammation-panel IL-5), plus per-sample NPX, LOD flags and the plate map. The plate map lets us rule out plate or processing confounding behind the proteome-wide shift.
* Re-fit the archived RNA-seq counts separately per cell type. This should recover the canonical endothelial markers that the pooled model made "non-significant": E-selectin, VCAM-1, IL-8, CXCL1, MCP-1, PTX3 and IL1RL1.
* Re-adjudicate the post-mortem group labels against the autopsy reports. Add a blinded second reader and digital quantification of nuclear IL-33.
* **Gate 0 (data hygiene):** sST2 stays a top-decile marker after the plate check, and the endothelial markers are confirmed.

**Stage 1 (months 2–6, decisive experiments):**

* **E2 patient-serum bioassay.** Run about 40 enrolment sera, stratified by event/no event and by high/low sST2, on primary lung microvascular endothelium from 3 donors, with AX-1177 vs isotype (pre-incubated).
  * Readouts: the 39-gene core at **6 h**; CCL20 and sE-selectin protein at **24 h**.
  * Positive controls: reduced and oxidised IL-33.
* **E1 assays.** Ultrasensitive, drug-tolerant, form-specific IL-33 assays on all 100 stored sera.
* **E3 potency and form coverage.**
  * Reduced and oxidised IL-33; 8-point AX-1177 titration; pre-incubated, concurrent and delayed addition.
  * Lung microvascular endothelium plus primary bronchial epithelium (air–liquid interface).
  * Comparator stimuli (IL-1β, TNF, poly(I:C)) to separate IL-33-specific genes from generic NF-κB targets.
* **Gate 1 (proposed; to be agreed before starting):**
  * **Go** requires all of the following:
    * AX-1177 (not isotype) cuts serum-induced core-signature activity by ≥ 50% in at least one third of event-patient sera.
    * The neutralisable fraction is higher in events, or in sST2-high sera.
    * IL-33 (any form) is quantifiable in most event patients and relates to outcome or sST2.
    * The IC90 is compatible with achievable exposure (needs the biologics/PK file).
  * **Kill:** no AX-1177-neutralisable activity in patient sera, whatever the immunoassay shows. IL-33 may act locally, so if airway samples exist (e.g. tracheal aspirates from ventilated patients), test those before killing.

**Stage 2 (months 6–12):**

* **E4 replication cohort.** Hospitalised pneumonia: post-vaccination COVID-19, influenza, RSV, and non-viral pneumonia/ARDS.
  * Sampling at enrolment, 24 h, day 3 and day 7.
  * Same composite endpoint; pre-specified sST2 cut-off.
* **E5 infection models.** Measure viral load and ISGs with IL-33 blockade.
* **Gate 2:** sST2 (or IL-33) replicates and adds to NEWS2 outside COVID-19. Then design a Phase 1b/2a in sST2-high severe pneumonia, with sST2-stratified randomisation so its *predictive* value can be tested.

# 8. Biomarkers, sampling timepoint and role in patients

| Marker | Evidence in our data | Proposed role | Ready for patients? |
|---|---|---|---|
| **sST2 (IL1RL1)** | Rank 2/1,094; OR 3.0 (1.8–5.0); independent of NEWS2; not cardiac-driven. Induced by IL-33 in HUVEC (+1.6 log2) and reversed, but variance-inflated | **Prognostic enrichment / stratification at enrolment.** Test as predictive in Phase 2 | **Yes**, as a prognostic enrichment and stratification factor. Cut-off still to be set and replicated |
| **IL-33 (free/total, reduced/oxidised)** | Not in the delivered data (tested but withheld); present in tissue | **Target engagement:** drug-bound complex accumulates (total rises) and free IL-33 falls. Possible selection marker if detectable | After assay development (Stage 1) |
| **CCL20** | Induced +9.2 / +5.6 log2 (6 h / 24 h, FDR < 10⁻⁸), fully reversed in HUVEC and HGMEC, in the robust core. Serum rank 46 (FDR 2%, 96th percentile) | **Lead downstream PD marker.** Also a prognostic covariate | After Stage 1 confirms it ex vivo |
| **sE-selectin (SELE)** | Largest in vitro effect (+11.2 log2), reversed, endothelium-restricted (but variance-inflated; needs re-fit). Serum p = 0.02 (75th percentile) | **Endothelium-specific PD** | After re-fit and Stage 1 |
| **OPG (TNFRSF11B)** | In the robust core; serum 98.6th percentile on 2 panels | Exploratory PD and prognostic | After Stage 1 |
| **PTX3** | IL-33-inducible (transient, variance-inflated); serum rank 6 | Prognostic covariate | Yes (as covariate) |
| **IL-6, IL-8** | Induced and reversed; strongly prognostic; non-specific | **Prognostic covariates only, not PD.** Confounded by standard of care (IL-6R blockade raises IL-6; dexamethasone suppresses NF-κB targets) | Covariate only |
| **Tissue factor / PAI-1 / thrombomodulin** | IL-33 causes a pro-coagulant shift that is reversed; serum tissue factor p = 0.009, PAI-1 p = 0.048 | Exploratory mechanism (thrombo-inflammation) | Exploratory |
| **Viral load + ISG score** (GBP5, MX1, IFIT1, RSAD2, IFI6) | IL-33 induces endothelial ISGs and AX-1177 blocks them | **Safety** (viral clearance) | Yes |
| *Not recommended* | CXCL6, CXCL5, G-CSF, CXCL1, VCAM-1: strong in vitro but not prognostic (20th–45th percentile). HGF: prognostic rank 1 but not IL-33-regulated. Type-2 markers: null | n/a | n/a |

## Sampling timepoint

**Patients: enrolment (pre-dose).** It is the only timepoint where our data show prognostic value, and the natural point for sST2-based selection.

**Ex vivo / in vitro PD: 6 h for transcripts and 24 h for secreted protein.** The IL-33 response is about twice as large at 6 h:

* HUVEC: 4,031 vs 1,836 genes (6 h vs 24 h).
* HGMEC reversal: 1,460 vs 269 genes.
* Transient genes (TNF, tissue factor) are largely back to baseline by 24 h, and NF-κB feedback genes such as NFKBIA have fallen by about 60%.

Sustained genes (CCL20, CSF2, CSF3, CXCL5/6, C3) still give a window at 24 h, when protein has had time to accumulate.

**On-treatment PD in patients:** first sample within 24 h of dosing, then day 3. Prefer sustained markers (CCL20, sE-selectin, OPG) over transient ones. How in vitro kinetics translate to patients is what Stage 2's serial sampling establishes.

## Which markers can go into patients, and in what role

* **Now:** sST2 as a *prognostic enrichment/stratification* marker at enrolment, with NEWS2 as covariate and viral load for safety.
* **After Stage 1:** CCL20 (± sE-selectin, OPG) as *pharmacodynamic* markers, and total/free IL-33 as a *target-engagement* marker.
* **Not as decision markers:** IL-6/IL-8, HGF and type-2 markers.
* **Caveat:** nothing yet supports sST2 as a *predictive* marker of AX-1177 benefit. That has to be tested.

# 9. What I considered and ruled out

| Considered | Verdict | Basis in our data |
|---|---|---|
| HUVEC response is an endotoxin/contaminant artefact | Ruled out | An anti-IL-33 antibody removes about 100% of the top-100 responses; it can't neutralise LPS |
| AX-1177 has off-target activity | Ruled out at the transcriptome level | Fig. 2: no reproducible genes across 4 cell types × 2 timepoints |
| The reversal is overstated | Checked | "vs IL-33 alone" (r = −0.93) shares an arm with the signature, which inflates it. The isotype-matched contrast gives r = −0.80 and confirms the effect |
| Top-of-sheet genes (SELE, VCAM-1, IL-8) are significant hits | Ruled out as stated | The sheet is sorted by log2FC and these are "n.s." because of variance inflation. Their effects are still real and consistent across independent arms |
| IL-33 is up-regulated in COVID-19 lungs | Not supported | Epithelium flat; vascular scores lower |
| COVID-specific tissue biology | Not supported | COVID-19 vs non-COVID pneumonia: IL-33 in all three compartments p ≥ 0.15; eight inflammatory-cell scores p ≥ 0.35 |
| Repurpose to asthma/COPD (type-2 airway) | Not supported | CCL17 OR 0.85; eotaxin, CCL24 and tryptase null; IL-5 (Immune Response panel) OR 1.00; IL-4, IL-13 and TSLP not delivered; IL-33 IHC vs COPD/asthma/emphysema all p ≥ 0.07. The only trend (lower endothelial IL-33 with emphysema) tracks COVID status: emphysema is in 9/16 COVID-positive vs 3/15 COVID-negative donors |
| sST2 is just cardiac strain | Not supported | NT-proBNP and troponin I unremarkable |
| The IL-33 endothelial programme explains the severity proteome | Not supported | Set not enriched (p = 0.69); in vitro response size vs prognostic value ρ = −0.08 |
| Rank biomarkers by OR size | Rejected | ORs are per delivered unit and the scale differs by assay (e.g. CSF-1 OR 90, 95% CI 4–1,933). Rank by z/p instead |
| Block-level IHC statistics | Rejected | Pseudo-replication: 3 donors supply 24 of 49 COVID-positive blocks. Naive p-values are 3–10× too small |
| Kidney indication (HGMEC) | Not supported | No vehicle arm, so the IL-33 response can't be estimated; KIM-1 at the 72nd percentile |
| Lung fibrosis | Hypothesis only | 5 curated donors, endothelial IL-33 p = 0.03, one nominal hit among about 45 tests |
| Thrombo-inflammation as a standalone indication | Supportive, not sufficient | Pro-coagulant shift reversed in vitro; pulmonary thromboemboli in 4/16 COVID-19 donors vs 0/15 COVID-negative (p = 0.10) |
| HGF as a biomarker | Not for PD | Top prognostic marker but not IL-33-regulated |
| IL-6/IL-8 as PD markers | Rejected | Non-specific; confounded by standard of care |
| `composite_endpoint_0/1` columns are outcomes | No | These are per-group fractions below LOD (exact multiples of 1/56 and 1/44, implying 56 non-events and 44 events) |

# 10. Data-integrity findings and requests to data owners

| # | Finding | Consequence / request |
|---|---|---|
| 1 | **Serum: BH adjusted over m = 1,194 tests but only 1,094 delivered.** Reconstructing the ranks shows about 100 tested assays were withheld. About 2 had p < 0.0011 (which would pass FDR 5%), about 5 had p < 0.01 and about 15 had p < 0.05. IL-33 is one of the 15 Inflammation-panel assays absent from the delivery (102 of 1,196 panel assays are absent, so ≥ 100 of them were tested) | **Request the full result set**, per-sample NPX, LOD flags and plate map. The annex says BH was "across all assays in the delivery", which the numbers contradict |
| 2 | Serum: 82% of proteins have OR > 1 | Read every association against this shift. Rule out plate or processing confounding: 100 samples need at least 2 plates per panel |
| 3 | Serum: 27 proteins are measured on 2–4 panels (58 rows), not reconciled | Don't double-count. The duplicates agree (IL-6 OR 2.07–2.31) |
| 4 | Serum: ORs are "per log unit" of NPX, which is already log2 | Magnitudes aren't comparable across assays |
| 5 | Serum, not plasma | Platelet-derived proteins (e.g. VEGF-A) are inflated by clotting |
| 6 | RNA-seq: the contrasts workbook sheets "6h" and "24h" each hold all 24 contrasts, with identical values | A labelling error only; no data are lost |
| 7 | RNA-seq: one voom/limma model pooled endothelial and cancer epithelial lines, with robust eBayes | Canonical endothelial genes were variance-inflated (df ≈ 75): 8 of the 103 strongest, arm-consistent responders read as "n.s.". **Re-fit per cell type** |
| 8 | RNA-seq: implied residual df is 75, but the annex design implies 76 | One library dropped, or an undocumented term. Request the count matrix and design |
| 9 | RNA-seq: `AveExpr` is averaged over all 114 libraries; the IL-33 file is sorted by log2FC; the comparison label says "Nontreated" but the annex says "Vehicle" | Don't filter on `AveExpr`. Don't quote top rows as hits. Confirm which control arm was used |
| 10 | RNA-seq design | HGMEC has no vehicle arm. Epithelial lines were never given IL-33. DMSO is an irrelevant vehicle for an antibody. Single donors, one dose, no pre-incubation |
| 11 | Post-mortem: 1–8 blocks per donor; donor fields on the first block only (and notes sometimes on the second) | Analyse at donor level |
| 12 | Post-mortem: **9 of 31 donors' group labels contradict their own autopsy reports** (details below); donor 1905 has no SARS-CoV-2 status | Re-adjudicate |
| 13 | Post-mortem: numeric IHC columns code "N+" as N + 0.5, so "5+" becomes 5.5 on a 0–5 scale; 39/74 endothelial scores sit at the ceiling; single reader | Use ordinal/rank methods; add a blinded second reader and digital quantification |
| 14 | Post-mortem: all donors are 64–98 years old, and the "controls" have lung disease | There is no normal-lung reference |

**Label discrepancies (finding 12):**

* 4 of 10 "COVID-negative pneumonia" donors have no pneumonia in their autopsy report.
* 2 of 16 "COVID-positive pneumonia" donors have no acute pneumonia in their report, including donor 2067, who contributes 8 blocks.
* 3 of 5 "non-pneumonia" donors have acute lung infection or inflammation (coccidioidomycosis, acute pneumonitis, organising pneumonia).

# Appendix A: how the key numbers were derived

**RNA-seq internal consistency:**

* I checked that t-statistics match p-values for all 681,460 rows. The result is consistent with limma `eBayes(robust=TRUE)`: df.total is 85.15 for typical genes and the implied df is identical per gene across contrasts.
* BH adjustment reproduces within each contrast.

**Inhibition:**

* IL-33 + isotype vs vehicle = (IL-33 vs vehicle) + (AX + IL-33 vs IL-33) − (AX + IL-33 vs isotype + IL-33).
* AX + IL-33 vs vehicle = (IL-33 vs vehicle) + (AX + IL-33 vs IL-33).
* % inhibition = 1 − [AX + IL-33 vs vehicle] / [IL-33 + isotype vs vehicle].
* Both are exact linear combinations of the delivered group-mean contrasts.

**Serum:**

* Wald z = ln(OR) / SE, with SE taken from the 95% CI.
* p-values and CIs are internally consistent.
* Percentiles are computed against all 1,094 delivered assays.
* Assay-to-gene mapping for the bridge analysis: 940 of 1,094 assays map to an RNA-seq gene.

**Withheld-assay reconstruction:**

* The delivered q-values anchor exactly to q = p × 1,194 / rank.
* Comparing the implied full-set rank with the delivered rank counts the undelivered tests below each p-value (`tables/serum_BH_reconstruction_withheld_assays.csv`).

**Post-mortem:**

* I curated pathology flags per donor by reading each autopsy report.
* Statistics use donor-level Mann–Whitney tests, with GEE (exchangeable, donor clusters) as a sensitivity check. Naive block-level tests are shown only to illustrate the inflation.

**Limits of this review:**

* There is no patient-level serum data, no count matrix and no PK/affinity data.
* Competitive and clinical precedent for other IL-33/ST2 agents is outside this dataset and wasn't used. It should be overlaid before Gate 2.

# Appendix B: files

* **Figures** (`figures/`):
  * `fig1_pharmacology_huvec.png`
  * `fig2_antibody_alone_specificity.png`
  * `fig3_serum_global_shift.png`
  * `fig4_bridge_invitro_to_serum.png`
  * `fig5_postmortem_il33_ihc.png`
* **Tables** (`tables/`):
  * `biomarker_triage_invitro_vs_serum.csv`
  * `exvivo_PD_core_gene_panel.csv`
  * `huvec_il33_top100_signature_with_inhibition.csv`
  * `rnaseq_contrast_summary.csv`
  * `serum_proteomics_annotated.csv`
  * `serum_BH_reconstruction_withheld_assays.csv`
  * `postmortem_donor_level_curated.csv`
* **Code** (`code/`): all analysis scripts.

![Figure 1. IL-33 response in HUVEC and its reversal by AX-1177 (isotype-matched). Red circles: canonical endothelial genes with large, arm-consistent effects that the pooled model made "non-significant".](figures/fig1_pharmacology_huvec.png)

![Figure 2. AX-1177 alone: no reproducible transcriptional effect across cell types or timepoints.](figures/fig2_antibody_alone_specificity.png)

![Figure 3. Serum proteomics: proteome-wide shift in patients with the endpoint (left) and the position of IL-33-axis, endothelial, type-2 and cardiac markers (right).](figures/fig3_serum_global_shift.png)

![Figure 4. Bridging the in vitro mechanism to patient serum.](figures/fig4_bridge_invitro_to_serum.png)

![Figure 5. Post-mortem IL-33 IHC at donor level by group, with the autopsy-report audit overlaid.](figures/fig5_postmortem_il33_ihc.png)
