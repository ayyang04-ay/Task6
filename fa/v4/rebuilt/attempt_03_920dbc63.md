---
title: "AX-1177 (anti-IL-33 mAb): portfolio audit recommendation"
subtitle: "Decision, evidence, forward view and what was ruled out"
---

**Scope.** This memo uses only the AX-1177 data package: the methods annex, in vitro RNA-seq contrasts (HUVEC, HGMEC, A549, MCF7), serum proteomics from hospitalised COVID-19 patients (n = 100) and post-mortem lung IHC (31 donors, 74 blocks). Every number below was recomputed from the delivered files. Where the files are wrong, incomplete or misleading, this is stated (§6, Table S1). Cost, competitive landscape and the programme biologics file (affinity, potency, epitope) are not in the package and were not used.

# 1. Bottom line

**Recommendation: KEEP AX-1177, but conditionally. The current indication rationale should go; the asset should stay as a re-scoped, gated programme.**

1. **Retire unselected severe lower respiratory viral infection as the stated indication.** Our data do not show that IL-33 drives severe viral lower respiratory tract infection (LRTI), and nothing in our data ties IL-33 specifically to viral infection.
2. **Re-scope to the one hypothesis our data support:** IL-33-driven endothelial activation (an "endotheliopathy") in severe pneumonia, with patients selected at enrolment by soluble ST2 (sST2).
3. **Fund only a time-boxed, gated plan with pre-specified kill criteria (§4.5).** Gate 0 uses data we already own. If Gate 0 or Gate 1 fails, drop the asset with the rationale in §3.4.

**Why keep.**

- The pharmacology is clean and complete. AX-1177 abolishes the IL-33-driven endothelial inflammatory and pro-thrombotic programme. The isotype control does not. AX-1177 has no effect of its own in any of the four cell types.
- Our patient data contain one pathway-specific prognostic signal. sST2, the IL-33 decoy receptor, is the #2 predictor of ICU admission, ventilation or death out of 1,063 serum proteins after adjusting for NEWS2, age and sex.
- The remaining uncertainty is cheap to resolve, largely from material already in our archive.

**Why not continue as is.**

- Lung IL-33 is not elevated in COVID-19 or in pneumonia.
- The IL-33-inducible programme, taken as a class, does not track outcome.
- There is no type-2 signal.
- IL-33 itself was not delivered in the serum data.
- There is no infection-model or in vivo efficacy.
- Several apparent results in the delivered files are artefacts of how the data were analysed or presented.

# 2. What our data show

## 2.1 Pharmacology (in vitro RNA-seq): strong, clean, narrow (Fig. 1)

- **IL-33 turns on a full endothelial inflammatory, pro-adhesive and pro-thrombotic programme.** In HUVEC at 6 h, IL-33red (30 ng/mL, 1.66 nM) induced 97 genes by more than 8-fold:
  - E-selectin (SELE) +11.2 log2, VCAM1 +8.7, ICAM1 +6.0;
  - IL-8 +8.2, GM-CSF +10.3, IL-6 +5.8, CCL20 +9.2;
  - tissue factor (F3) +5.6, PAI-1 +1.7, ST2 (IL1RL1) +1.6;
  - thrombomodulin −1.0 and eNOS −1.1.
- **AX-1177 returns this programme to baseline.** The dose was 10 µg/mL (68.5 nM), a 41-fold molar excess, added concurrently with IL-33.
  - For the 97 strongly induced genes, the median residual response was 2.3% at 6 h and 5% at 24 h.
  - For well-expressed genes, the residual was −0.4% (IQR −4% to +4%) for IL-33-induced genes and 7.6% for IL-33-repressed genes.
  - The IL-33 + isotype arm reproduced the full IL-33 response (median log2FC 4.12 vs 4.02), so the effect is specific to AX-1177.
- **AX-1177 alone is inert.** Compared with the isotype, it showed no agonism and no coherent off-target transcription in any of the four cell types. Its nominal FDR "hits" are very-low-expression lncRNAs and pseudogenes, or trivial fold-changes.
- **The second vascular bed (HGMEC, glomerular microvascular) shows the same programme suppressed** (E-selectin −8.7, VCAM1 −11.7, ICAM1 −5.4 log2 vs isotype; genome-wide r = −0.57 against the HUVEC IL-33 signature). HGMEC has no vehicle arm, so the size of its IL-33 response and the percentage blockade cannot be estimated.
- **What this package cannot tell us:**
  - It covers a single donor per endothelial cell type.
  - It tests one IL-33 and one antibody concentration, so there is no potency (IC50) information.
  - Only the reduced form of IL-33 was tested, although the annex states AX-1177 also binds the oxidised form.
  - There are no lung microvascular cells and no IL-33-responsive immune cells.
  - The epithelial lines were never exposed to IL-33, so there is no epithelial efficacy information.
  - There is no infection model.
- **The 6 h timepoint carries the signal.** The IL-33 response decays by 24 h (FDR < 5% genes in the delivered statistics fall from 4,031 to 1,836; E-selectin from +11.2 to +4.7 log2).
- **Caution for anyone reading the delivered tables.** E-selectin, VCAM-1, IL-8, CXCL1, MCP-1, PTX3 and ST2 carry invalid t and P values because of a variance artefact (§6). Filtering on adjusted P would conclude that IL-33 does not induce them. Their log2FCs replicate across independent arms and are reliable.

## 2.2 Patients (serum proteomics; COVID-19; 56 non-events and 44 events): one specific signal; the IL-33 programme as a class does not predict outcome (Fig. 3)

- **Scale of the signal.** The 1,094 delivered assays represent 1,063 unique proteins. 169 proteins (178 assays) pass FDR < 5%, and 176 of those 178 have OR > 1. The whole proteome is shifted upward in patients with events: 82% of assays have OR > 1 and 35% have p < 0.05. Individual markers therefore have to be judged against this background.
- **sST2 (IL1RL1) stands out.** OR 3.02 per log unit (95% CI 1.83–5.01), p = 1.7 × 10⁻⁵, BH-adjusted 0.0075. It ranks #2 of 1,063 (after HGF) and sits about 2 robust SD above the proteome background. It is adjusted for NEWS2, age and sex and has no missing values. Its gene is IL-33-inducible in HUVEC (+1.6 log2 at 6 h) and normalised by AX-1177; this was not seen in HGMEC.
- **Several IL-33-inducible endothelial and thrombo-inflammatory products that AX-1177 blocks in vitro also predict outcome:**
  - PTX3: rank #5, BH 0.012;
  - IL-6: rank #10, BH 0.012, consistent across 4 panels (OR 2.07–2.31);
  - OPG: BH 0.014; IL-18R1: BH 0.018; MCP-3/CCL7 and CCL20: BH 0.020; IL-8: BH 0.023;
  - MCP-1 and tissue factor: BH 0.051;
  - sE-selectin: p = 0.022, BH 0.09.
- **But the programme as a class is not enriched among outcome-associated proteins.** The 98 IL-33-induced, AX-1177-reversed proteins have median z 1.38 vs 1.49 for the rest (p = 0.71). The 50 most strongly induced proteins give p = 0.66. sVCAM-1, sICAM-1, G-CSF, CXCL1/5/6 and TNF are strongly IL-33-inducible but not prognostic (p = 0.11–0.95).
- **An endotheliopathy is present, but is not shown to be IL-33-driven.** Endothelial-injury markers that IL-33 did not induce in vitro are prognostic: vWF (OR 3.9, p = 0.008), ANGPT2 (OR 2.2, p = 0.009), sFlt-1 (p = 0.009), uPAR (BH 0.025) and VEGF-A (BH 0.024). Whether IL-33 contributes to this endotheliopathy is the open question.
- **There is no type-2 signal.** IL-5 (OR 1.00), eotaxin-1 (0.98–1.08), CCL24, CCL17, CCL13, CCL18 and tryptase all have p > 0.38. The only nominal signals are ECP (p = 0.011, BH 0.06) and soluble IL-4Rα (BH 0.02). Both are also produced by myeloid cells.
- **The dominant prognostic signal is myeloid and neutrophil activation plus tissue damage:** HGF, CLEC5A, FCAR, IL-1R2, OSM, PRTN3, CD177, S100A12, LCN2 and GDF-15.
- **Limits of this cohort:**
  - single centre, pre-vaccination, COVID-19 only;
  - one timepoint (enrolment), n = 100;
  - IL-33 not delivered, and 100 tested assays withheld (§6);
  - no adjustment for renal function, CRP, time from symptom onset or treatments.

## 2.3 Lung tissue (post-mortem IHC): the target is present everywhere but is not elevated by disease (Fig. 4)

- **IL-33 is constitutive and abundant in lung endothelium and basal epithelium in every group, including non-pneumonia controls.** Endothelial IL-33 sits at the scoring ceiling in 52% of donors. The target reservoir exists; it is not a disease marker.
- **At the correct unit of analysis (the donor), groups do not differ.** COVID+ pneumonia (n = 16), COVID− pneumonia (n = 10) and non-pneumonia (n = 5) show no difference in epithelial (p = 0.65), endothelial (p = 0.11) or vascular smooth muscle (VSM; p = 0.16) IL-33.
  - The direction is lower in COVID+: endothelial median 4.8 vs 5.5; VSM 2.4 vs 3.3–3.5.
  - Treating blocks as independent, as the file layout invites, manufactures significance (p = 0.028 and 0.016).
- **Age, not disease, is the dominant correlate.** Endothelial IL-33 correlates with donor age (ρ = 0.55, p = 0.001); after age adjustment the COVID effect is β = −0.35 (p = 0.06).
- **Endothelial IL-33 is lower where granulocytes infiltrate.** It correlates inversely with neutrophil elastase and IL-5Rα+ infiltrate (ρ ≈ −0.4, p ≈ 0.02, uncorrected). Lower nuclear IL-33 in injured lung is consistent with alarmin release, but IHC cannot distinguish release from cell loss.
- **Granulocyte infiltrates track pneumonia, not COVID.** EDN, MBP, IL-5Rα and neutrophil elastase separate pneumonia from non-pneumonia (p = 0.004–0.009) but not COVID+ from COVID− pneumonia (p = 0.44–1.0). IL-33 is unrelated to eosinophil granule proteins.
- **Vascular injury is COVID-specific in this set.** Diffuse alveolar damage (DAD) appears in 7 of 16 COVID+ donors and none of 15 COVID− donors (Fisher p = 0.007). Thromboemboli appear in 4 of 16 vs 0 of 15 (p = 0.10). This is consistent with an endotheliopathy, which is where AX-1177's pharmacology sits.
- **Limits of the tissue data:**
  - 9 of 31 category labels conflict with the donor's own pathology report;
  - single reader, semi-quantitative scoring, with a ceiling;
  - no AT2-cell or ST2 scoring;
  - elderly (64–98 y), all-white donors, with end-stage tissue.

# 3. The case for the committee

## 3.1 Position and supporting pillars

**Position: keep, re-scoped and gated.** Four pillars support it.

- **P1. The target pharmacology is proven and clean.** AX-1177 gives complete, isotype-controlled neutralisation of IL-33-driven endothelial activation in HUVEC and strong suppression of the same programme in microvascular HGMEC, with no agonism or off-target activity (§2.1).
- **P2. Our patient data contain a pathway-specific prognostic signal that survives NEWS2 adjustment against a globally shifted proteome.** sST2 ranks #2 of 1,063. IL-33-inducible endothelial products (PTX3, IL-6, CCL20, IL-8, tissue factor) are among the outcome predictors.
- **P3. One biological mechanism connects all three datasets.**
  - The endothelium is the most strongly IL-33-positive lung compartment scored.
  - COVID-19 lungs show vascular injury (DAD, thromboemboli), and endothelial IL-33 trends lower where injury and infiltrate are greatest.
  - IL-33 switches endothelium to a pro-adhesive, pro-thrombotic state (E-selectin, VCAM-1, tissue factor and PAI-1 up; thrombomodulin and eNOS down), and AX-1177 prevents that switch.
- **P4. The decisive open questions are cheap and fast to answer.** Gate 0 is re-analysis of material we already hold: archived count matrices, the full Olink output (which very likely includes IL-33) and lung RNA from 22 donors.

## 3.2 The strongest case against, and why it does not change the recommendation

- **C1. The indication-critical link is missing.**
  - IL-33 was never measured in patients, and tissue IL-33 is not elevated.
  - The IL-33 programme does not predict outcome as a class.
  - sST2 also rises with IL-1, TNF and mechanical strain, so it is not IL-33-specific.
  - High sST2 may itself neutralise IL-33 (it is a decoy), which could make an antibody redundant.

  *Response:* this is exactly what Gates 0–1 test, mostly with existing material. If C1 is confirmed we drop, with a documented rationale.

- **C2. Nothing in this package differentiates AX-1177 from other anti-IL-33 antibodies.** There are no potency, affinity or epitope data. *Response:* append the biologics file (it exists) before the committee decides on Gate 1 spend.

- **C3. The package has integrity problems that would not survive external due diligence (§6).** *Response:* these must be fixed whatever the decision, because the files are our record.

- **C4. Safety of blocking IL-33 during active infection is untested in our data.** *Response:* this is a Gate 1 experiment. IL-33's host-defence and repair roles are background knowledge, not in our data, and are flagged here as a risk.

## 3.3 Anticipated challenges

- ***"sST2 is just a severity marker."***
  - It survives NEWS2 adjustment and stands out from a proteome in which 82% of proteins lean positive.
  - It is the pathway's own receptor, and its gene is IL-33-inducible and AX-1177-reversible in HUVEC.
  - It is proposed as an **enrichment** marker to be validated, not as proof of mechanism. Measuring IL-33 itself is the missing link.
- ***"If sST2 is high, isn't IL-33 already neutralised?"*** Possibly. The Gate 1 patient-serum bioassay tests directly whether sST2-high sera still contain AX-1177-sensitive endothelial-activating activity. It is a kill criterion.
- ***"Why not COPD or asthma, like the rest of the field?"*** Nothing in our data supports either (§5). That would be a new programme needing a new data package, not a repurposing grounded in our evidence.
- ***"The tissue study shows IL-33 going down in COVID."*** Not at the donor level, after age adjustment. Where a trend exists, lower nuclear staining in injured tissue is what alarmin release would look like. Either way, tissue IL-33 cannot be a patient-selection marker.

## 3.4 If the committee drops AX-1177: what we are dropping, and why

**What we would be dropping:**

- a specific, clean IL-33 neutraliser with demonstrated blockade of IL-33-driven endothelial activation (complete in HUVEC; strong in HGMEC);
- an untested but data-derived hypothesis: sST2-selected, IL-33-driven endotheliopathy in severe pneumonia.

**Why we would be dropping it.** Our data do not show that IL-33 drives severe viral LRTI:

- tissue IL-33 is not elevated;
- IL-33 was not measured in patients;
- the IL-33-driven programme does not predict outcome as a class;
- there is no type-2 involvement and no disease-model efficacy;
- the one supportive patient signal (sST2) is correlative and non-specific.

**Before closing,** the IL-33 endothelial signature, the sST2 finding and the data-integrity log should be archived as reusable assets.

# 4. Forward view

## 4.1 The indication our data point at

Our data point at a **mechanism**, IL-33-driven endothelial activation, rather than at a pathogen or at type-2 airway disease. The most data-consistent indication is:

> **Severe pneumonia / acute lung injury with an endotheliopathy phenotype, selected by high sST2 at enrolment.**

- Start where we have patient data: hospitalised COVID-19.
- Test whether the finding generalises to influenza, RSV and bacterial pneumonia. The post-mortem data show that the IL-33 and granulocyte patterns are pneumonia-generic; the serum data are COVID-only.
- This is a re-scoping within acute severe lung disease, not a move into chronic airway disease.

## 4.2 What the next studies must establish

1. **Release.** Is IL-33 (total and free; reduced and oxidised) measurable and elevated in the patients we would select, and how does it relate to sST2?
2. **Disease-relevant activity (the decisive experiment).** Does patient serum or BAL activate primary human lung microvascular endothelium in a way AX-1177 reverses? Read out at 6 h with the transcript panel in §4.3, comparing sST2-high with sST2-low patients.
3. **Selection.** Is sST2 an independent, reproducible enrichment marker in a contemporary, multi-centre, post-vaccination cohort, with a usable cut-off and enough prevalence?
4. **Potency.** What is AX-1177's IC50 against reduced and oxidised IL-33?
   - Test in lung microvascular endothelial cells from at least 3 donors and in IL-33-responsive immune cells.
   - Compare pre-incubation with concurrent addition.
5. **Safety in infection.** In infected airway-epithelium/endothelium co-cultures, or in vivo if species cross-reactivity allows, does AX-1177 leave viral replication, interferon responses and epithelial repair intact?

## 4.3 Biomarkers: roles, and which can go into patients (full table: Table S2)

| Marker | Evidence in our data | Into patients? Role |
|---|---|---|
| **sST2** | Serum #2/1,063; OR 3.02 per log unit (1.83–5.01), NEWS2-adjusted. IL1RL1 is IL-33-inducible and AX-1177-reversible in HUVEC | **Yes: baseline prognostic enrichment marker**; exploratory PD. Clinical immunoassays exist; needs an external cut-off |
| **Total/free IL-33, AX-1177:IL-33 complex** (reduced and oxidised) | Not measured; absent from the delivery | **Yes, once the assay exists: target engagement**; also test as a predictive marker. This is the critical missing link |
| **sE-selectin** | Largest in vitro effect (+11.2 log2, fully normalised; HGMEC −8.7). Serum OR 2.1, p = 0.022 | **Yes: primary pathway PD marker.** Most endothelium-specific; weak as a prognostic marker |
| **PTX3** | IL-33 +2.2 log2, reversed. Serum #5/1,063 | **Yes: prognostic and PD** |
| IL-6, CCL20, IL-8, MCP-1/3, tissue factor, OPG, IL-18R1 | IL-33-inducible and reversed. Serum BH 0.012–0.051 | Yes: secondary exploratory PD panel. Multi-source, so interpret only against placebo |
| ANGPT2, vWF (uPAR, sFlt-1, VEGF-A) | Prognostic; **not** IL-33-responsive in vitro | Yes: stratification covariates for the endotheliopathy phenotype. **Not** PD markers |
| sVCAM-1, sICAM-1, G-CSF, CXCL1/5/6, TNF | IL-33-inducible but not prognostic | Not as prognostic markers (sVCAM-1 possible as PD only) |
| Type-2 markers (IL-5, eotaxins, CCL17, tryptase) | Null | **No**, for this indication |
| Lung IL-33 IHC | At ceiling; no disease discrimination; age-confounded | **No.** Tissue research readout only |
| 6 h endothelial transcript panel: SELE, VCAM1, ICAM1, CXCL8, IL6, CSF2, CCL20, F3, SERPINE1, IL1RL1 (up); THBD, NOS3 (down) | Full dynamic range and reversal | **Lab/ex vivo only:** potency assays and patient-serum bioassays |

## 4.4 Sampling timepoint

- **Patients: serum at enrolment (hospital admission), before dosing.** This is the only patient timepoint in our data and the one at which sST2 predicted outcome independently of NEWS2.
  - Record days since symptom onset.
  - In the validation cohort, add draws at day 3 and day 7 to define kinetics and the on-treatment PD window. Our data cannot yet set that window.
- **Lab and ex vivo: 6 h after exposure, with 24 h as a secondary readout.** At 6 h the IL-33 response is maximal (4,031 vs 1,836 FDR genes) and the blockade readout is cleanest (HGMEC genome-wide r = −0.57 at 6 h vs −0.12 at 24 h).

## 4.5 Gated plan with kill criteria

The thresholds below are proposals for the committee to ratify.

**Gate 0 (about 2–3 months): re-analysis of data we already own.**

- RNA-seq:
  - Refit per cell line from the archived counts.
  - Deliver HGMEC IL-33 vs isotype.
  - Report per-cell-line expression of IL1RL1 and IL1RAP.
- Serum:
  - Retrieve all 1,194 assay results, per-patient NPX values and LOD flags, including IL-33 if it was measured.
  - Refit per SD, adjusting additionally for eGFR, CRP, days from onset and immunomodulator use.
  - Estimate the bootstrap-validated incremental AUC of sST2 over NEWS2.
  - Correlate sST2 with the endothelial panel.
- Tissue:
  - Have a pathologist re-adjudicate the category labels.
  - Obtain a blinded second IHC read with digital H-scores, and add ST2 IHC.
  - Retrieve RNA from the 22 donors and score the 6 h IL-33/AX-1177 endothelial signature against DAD, thrombosis and COVID status.
- Append the biologics file (affinity, potency, epitope, species cross-reactivity).
- **Kill if:** sST2's adjusted association loses significance (CI includes 1) after the added covariates, **or** both of the following hold: IL-33 is undetectable or unrelated to outcome, and the IL-33 signature is not elevated in COVID/DAD lung RNA.

**Gate 1 (about 3–6 months): decisive biology.**

- Patient-serum/BAL bioassay on lung microvascular endothelium from at least 3 donors.
- IC50 against reduced and oxidised IL-33.
- Infection co-culture measuring IL-33 release, endothelial activation, viral load and interferon response, with and without AX-1177.
- **Go if:** AX-1177 reverses a pre-specified fraction (proposed ≥ 30%) of patient-material-induced endothelial activation in sST2-high samples, and viral control is unchanged. **Otherwise kill.**

**Gate 2 (about 6–9 months, can overlap Gate 1): clinical biomarker validation.**

- Use an independent multi-centre biobank of hospitalised viral and bacterial pneumonia, with enrolment, day 3 and day 7 serum.
- Measure sST2, IL-33 (with a TE-capable assay), sE-selectin, PTX3, IL-6, ANGPT2 and vWF.
- **Go if:**
  - sST2 is independently prognostic at a pre-specified cut-off (proposed: adjusted OR per SD with lower CI bound > 1.5, and incremental AUC over NEWS2 ≥ 0.05);
  - sST2-high prevalence is at least about 25% of admissions.

**Then:** a placebo-controlled Phase 1b/2a in sST2-enriched patients.

- Endpoints: target engagement (IL-33 complex); PD, with sE-selectin primary and PTX3 and IL-6 secondary; safety including viral clearance.
- Clinical outcomes are exploratory.

# 5. Considered and ruled out

**Indications**

| Indication | Verdict | Basis in our data |
|---|---|---|
| Unselected severe viral LRTI (status quo) | **Retire as framed** | No virus-specific signal; tissue IL-33 not elevated; IL-33 programme not enriched among prognostic proteins; no efficacy model |
| Asthma / eosinophilic type-2 disease | **Ruled out** | IL-5, eotaxins, CCL17/13/18 and tryptase null in serum (IL-4/IL-13 not delivered); lung IL-33 unrelated to eosinophil granule proteins; no epithelial IL-33 experiments |
| COPD | **Not supported by our data** | No COPD cohort; basal-epithelial IL-33 does not differ by COPD history (p = 0.21); epithelial and oxidised-IL-33 biology untested; would need a new programme and new data |
| Kidney microvascular disease | **Not supported** | HGMEC in vitro only; no kidney tissue or patient data; serum KIM-1 only nominal (p = 0.03, BH 0.11) |
| Cardiac (sST2 is a heart-failure marker) | **Ruled out** | NT-proBNP weakly or not associated (p = 0.05 / 0.17), so the sST2 signal is not cardiac strain; no cardiac data |
| Oncology | **Ruled out** | A549 and MCF7 served only as antibody-alone controls |
| Sepsis / systemic endotheliopathy | **Parked** | Plausible extension of the endothelial mechanism; no non-pulmonary patient data. Revisit after Gate 2 |

**Interpretations and analyses rejected, with reasons**

- ***"IL-33 does not significantly induce E-selectin, VCAM-1, IL-8 or ST2"*** (delivered adjusted P). Rejected: this is the variance artefact. The log2FCs replicate across independent arms.
- ***"AX-1177 only partly restores IL-33-repressed genes," or "the isotype is active."*** Rejected: both come from the shared-reference design and low-expression noise. Well-expressed genes are fully normalised, and the isotype effect is at the noise floor: 15–28 expressed genes with |log2FC| > 1, against 11–37 in the antibody-alone null contrasts.
- ***"AX-1177 has off-target effects in epithelial cells."*** Rejected: the hits are noise (lncRNAs, pseudogenes) or trivial fold-changes with miscalibrated precision (AKR1C2: log2FC 0.11, t = 169).
- ***"Lung IL-33 differs by COVID status"*** (either direction). Rejected: this depends on block-level pseudo-replication; the donor-level comparison is null and age is a confounder.
- ***"HGMEC blockade is 40%."*** Rejected: this cannot be estimated without a vehicle arm.
- ***"The largest ORs are the strongest effects"*** (CSF-1 90, SEMA4C 21). Rejected: the ORs are per log unit and scale-dependent. I ranked proteins by Wald z instead.
- ***"178 significant proteins."*** Corrected: this is 169 unique proteins, and 100 tested assays are missing from the delivery.
- ***"The 6h sheet is truncated at Excel's row limit."*** Rejected: the extra rows are empty formatted rows.
- ***"RNA P-values are inconsistent with t."*** Rejected: the discrepancies are explained by gene-specific degrees of freedom from robust empirical Bayes, which is consistent across files.

# 6. Data integrity: must be fixed before the package is used externally (full log: Table S1)

1. **Presentation hides content.**
   - The contrasts workbook opens with AutoFilters that hide 23 of 24 contrasts, including every HGMEC and epithelial result. Its "6h" and "24h" sheets each contain both timepoints and are duplicates of each other.
   - The serum sheet hides the 95% CI columns.
   - The post-mortem sheet hides every IHC column.
2. **RNA-seq statistics are invalid for 101 genes.** These include the key endothelial targets (SELE, VCAM1, CXCL8, CXCL1, CCL2, PTX3, ST2) and the endothelial identity genes. The implied SE ranges up to 16,536 log2 units and is identical at both timepoints. The most likely cause is the single pooled fit across four unrelated cell types; the fix is to refit per cell line from the archived counts.
3. **Design gaps.** HGMEC has no vehicle arm. The epithelial lines never received IL-33. There is a single donor per endothelial type, a single dose of each agent, and the reduced form of IL-33 only.
4. **The serum delivery is incomplete.** The BH correction used m = 1,194 tests, but 1,094 assays were delivered. At least one withheld assay had p ≈ 2–3 × 10⁻⁴. Going by the panel's standard content, the 15 missing Inflammation-panel assays would include IL-33 itself (to be confirmed against the vendor manifest).
5. **Serum reporting issues.**
   - ORs are per log unit, and the NPX transformation is ambiguous.
   - Cross-panel duplicates are counted separately.
   - Two columns are undocumented (they reveal the 56/44 outcome split).
6. **Post-mortem data issues.**
   - Blocks are pseudo-replicates; 3 donors supply 49% of COVID+ blocks.
   - 9 of 31 labels conflict with the pathology reports.
   - Scores exceed the documented 0–5 scale.
   - Lung RNA exists for 22 donors but was not delivered.

# Appendix: what was done

- **RNA-seq.** All 26 contrasts were parsed, and I confirmed that both RNA files come from one fitted model (identical AveExpr and gene-specific df). I tested internal consistency: P vs t, BH adjustment, and implied SE.
- **Exact derived contrasts.** Shared groups cancel, so these are exact: IL-33 + AX-1177 vs vehicle = (C47+IL33 − IL33) + (IL33 − vehicle); IL-33 + isotype vs vehicle is derived the same way.
- **Serum.**
  - Verified Wald consistency of OR, CI and p.
  - Reverse-engineered the BH denominator and the ranks of the withheld tests.
  - Deduplicated cross-panel assays.
  - Mapped assays to genes to bridge to the in vitro data; tested enrichment by Mann–Whitney and Spearman.
- **Post-mortem.**
  - Cleaned the data, converted ordinal scores and aggregated to donor level.
  - Used non-parametric tests and age-adjusted OLS.
  - Coded the pathology free text myself (DAD, thromboemboli, pneumonia on report). This coding is not a pathologist re-read.
- **Code and tables** are in `code/` and `tables/`. Figures: Fig 1 (pharmacology), Fig 2 (RNA-seq artefact), Fig 3 (serum and bridge), Fig 4 (post-mortem).

![Fig. 1. AX-1177 neutralises IL-33-driven endothelial activation](figures/Fig1_invitro_pharmacology.png)

![Fig. 2. Variance inflation makes delivered t/P values invalid for key endothelial genes](figures/Fig2_rnaseq_statistics_artefact.png)

![Fig. 3. Serum: proteome-wide shift; sST2 stands out; in vitro to patient bridge](figures/Fig3_serum_proteomics_bridge.png)

![Fig. 4. Post-mortem lung IL-33 at donor level](figures/Fig4_postmortem_lung_IL33.png)
