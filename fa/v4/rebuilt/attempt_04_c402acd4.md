# AX-1177 (anti-IL-33 mAb): portfolio audit brief

**Scope.** This brief covers the four delivered data files and the methods annex, which I treated as ground truth: in vitro RNA-seq (two workbooks), serum proteomics, post-mortem lung IHC and the annex. Every number here was recomputed from those files. Analysis code is in `analysis_code/`, full tables are in `tables/AX-1177_supporting_evidence.xlsx`, and figures are in `figures/`. Any interpretation that relies on general biology rather than our data is marked *(context)*.

---

## 1. Bottom line

**Recommendation: No. Do not keep AX-1177 as an active asset for severe lower respiratory viral infection.**

Decisions requested from the committee:
1. Discontinue the severe viral LRTI indication now, and stop indication-directed spend.
2. Put the molecule on a gated hold for one quarter. Fund only work that uses material we already own (archived data, banked sera, banked lung RNA; Gates A–B, run in parallel; section 6.4), and agree the kill criteria up front.
3. If Gate B fails, terminate or out-license. Do not re-enter any indication before Gate B has passed.

**Why, in four points:**

1. **The molecule works.** In primary endothelial cells AX-1177 removes **95%** of the reduced-IL-33 transcriptional response at 6 h and **82%** at 24 h, measured against an isotype-matched arm. This holds even though the antibody was added at the same time as IL-33, with no pre-incubation. On its own, the antibody has no transcriptional effect in four cell types.
2. **The target–disease link is missing.** Nothing in our human data shows that IL-33 *activity* drives severe disease:
   - IL-33 itself was never measured in patients; it is absent from the proteomics delivery.
   - The proteins that AX-1177 blocks in vitro are no more associated with ICU admission, ventilation or death than randomly chosen proteins (permutation p = 0.55).
   - The most IL-33- and endothelium-specific of those proteins (VCAM-1, CXCL6, CXCL5, G-CSF, CXCL1) show no association at all.
3. **The tissue shows no COVID-specific IL-33 signal.** Analysed per donor rather than per block, IL-33 in basal epithelium, endothelium and vascular smooth muscle does not differ between COVID+ and COVID− pneumonia (p = 0.92, 0.16, 0.15). Endothelial IL-33 is at or near the top of the scoring scale in every group, controls included.
4. **The human evidence is narrow.** It comes from one virus (SARS-CoV-2), one centre, the pre-vaccination period and 100 patients. That is not "severe lower respiratory viral infection" as a class.

**The one human result that looks supportive is prognostic, not mechanistic.** Soluble ST2 ranks #2 of 1,094 serum assays for severe outcome (OR 3.02, 95% CI 1.83–5.01 per log unit; adj. p = 0.0075; adjusted for NEWS2).
- *(context)* sST2 is IL-33's decoy receptor, and stressed tissue releases it under many stimuli.
- In our own in vitro data, its link to IL-33 is weak (section 4.2).

---

## 2. What we are dropping, and what we are not (for the minutes)

**Dropping.** The hypothesis that neutralising IL-33 reduces progression to ICU admission, invasive ventilation or death in patients hospitalised with viral LRTI.
- Our data validate the **pharmacology** but not the **target–disease link**.
- Each of the three data types (RNA-seq, serum proteomics, post-mortem) has analysis or annotation defects. Correcting them removes the signals that looked supportive: block-level tissue statistics, uncorrected serum hit counts, and comparisons against IL-33 alone instead of the isotype arm.

**Not discarding** (this is the residual value for any re-entry or out-licensing):
- A clean, effective neutraliser of reduced-IL-33 signalling in macro- and microvascular endothelium. Effective at about 41-fold molar excess; potency has not been measured.
- A 6-hour in vitro pharmacodynamic panel that responds strongly to IL-33 and is fully reversible by the antibody.
- A prognostic enrichment marker (sST2) for hospitalised viral pneumonia.

---

## 3. Evidence at a glance

| Dataset | What it establishes | What it does **not** establish |
|---|---|---|
| In vitro RNA-seq: HUVEC, HGMEC, A549, MCF7; 114 libraries | AX-1177 specifically neutralises reduced IL-33 in endothelium (95% / 82% at 6 / 24 h in HUVEC). The same programme is reversed in glomerular endothelium at 6 h. The antibody is inert alone. **Strong** | Potency: one dose, about 41-fold molar excess. Oxidised or full-length IL-33. Any epithelial IL-33 biology: the epithelial lines never received IL-33. Lung microvascular endothelium. Donor-to-donor variability: single-donor cells |
| Serum proteomics: 100 hospitalised SARS-CoV-2 patients, 44 events | sST2 is strongly prognostic independent of NEWS2. The severity axis is dominated by neutrophils, endothelial injury and IL-6. No type-2 signal. **Moderate** | Any measurement of IL-33. That IL-33 activity drives outcome. Generalisation beyond pre-vaccination COVID |
| Post-mortem lung IHC: 31 donors, 74 blocks | IL-33 protein is abundant in lung endothelium, vascular smooth muscle and basal epithelium of elderly donors. **Moderate** | Any COVID-specific change. Released vs stored IL-33. Reliable group comparisons: 9/31 group labels conflict with the donor's own pathology |
| Methods annex | Design and analysis parameters | Affinity and potency, which are held in the biologics file and were not provided |

---

## 4. The case in detail

### 4.1 The molecule neutralises IL-33 in endothelium: our strongest evidence (Fig 1)

**The IL-33 response.** Reduced IL-33 (30 ng/mL) drives a large, canonical NF-κB programme in HUVEC:
- **4,031 genes at 6 h and 1,836 at 24 h** (adj. p < 0.05).
- Largest inductions: E-selectin (+11.2 log2), GM-CSF (+10.3), CXCL6 (+9.4), CCL20 (+9.2), VCAM-1 (+8.7), fractalkine (+8.4), G-CSF (+8.3).
- A coherent **procoagulant switch**: tissue factor +5.6, PAI-1 +1.7, uPA +1.5, thrombomodulin −1.0.

**How neutralisation was measured.** All contrasts come from one fitted model, so log fold-changes add up. That lets me compute the residual IL-33 response in each antibody arm relative to vehicle.

**Neutralisation versus the isotype-matched arm:**
- 6 h: AX-1177 removes **95%** of the response (538 reliably estimated IL-33-responsive genes; median per-gene inhibition 98%).
- 24 h: it removes **82%** (215 genes; median 93%).
- The procoagulant switch is fully reversed (residual ≤ 0.3 log2).
- The only coherent partial escape is a small interferon-stimulated set at 24 h (IFIT1/2/3).

**Glomerular endothelium (HGMEC).** AX-1177 reverses the same programme at 6 h:
- 1,460 differentially expressed genes; 47% of the HUVEC IL-33 programme is significantly reversed, and only 1 gene moves the wrong way.
- VCAM-1 −11.7, BIRC3 −8.8, E-selectin −8.7, GM-CSF −7.1 log2.
- At 24 h the reversal is much weaker (269 genes; 8% of the programme).

**No activity on its own (Fig 2B).** AX-1177 alone is transcriptionally inert in all four cell types. The 632 nominal "hits" across the 16 antibody-alone contrasts break down into:
- 490 that are count noise at near-zero expression;
- 94 that are changes smaller than 1.25-fold with artefactually tiny standard errors;
- 48 scattered genes (47 distinct). None recurs across cell types, and they form no coherent pathway.

**Caveats the committee should hear from us first:**

- **The delivered p-values are unusable for many key genes (Fig 2).**
  - One voom/limma model was fitted across the endothelial cells and two cancer lines, so residual variance was pooled across unrelated cell types.
  - As a result, 1,024 genes have an SE above 1 (the median is 0.34). They include the best IL-33 targets: E-selectin (SE 8.9, delivered adj. p = 0.50), VCAM-1 (adj. p = 0.51) and CXCL1 (SE 1,155, adj. p = 1.00).
  - The fold-changes themselves are real. For the 10 most affected genes, IL-33 induction and AX-1177 reversal were estimated from completely separate sample groups and agree at **r = −0.998**, slope ≈ −1.
  - The counts must be re-fitted per cell line from the archive before any external use.
- **The isotype control is not neutral at 24 h.** The IL-33 + isotype arm keeps 95% of the IL-33-alone response at 6 h but only 86% at 24 h. Any claim of AX-1177 efficacy "vs IL-33 alone" therefore overstates it. All numbers in this brief use the isotype-matched arm.
- **HGMEC has no vehicle arm.** The IL-33 response in glomerular endothelium cannot be estimated from the delivery. The AX-1177 reversal gives only a lower bound.
- **The design is narrow:**
  - one IL-33 form (reduced, mature residues 112–270);
  - one antibody concentration (10 µg/mL ≈ 68 nM, about 41-fold molar excess over IL-33 at ≈ 1.7 nM), so there is **no potency estimate**;
  - cells from a single donor.
- **The differentiating claim is untested.** The annex says the antibody binds oxidised IL-33, but this was never tested functionally, and the epithelial lines never received IL-33.

### 4.2 The human serum data do not support the target–disease link (Fig 3)

**IL-33 itself is missing.**
- The Inflammation panel was delivered with 77 of its 92 assays.
- *(context)* IL-33 is part of that panel's content; its absence is consistent with a below-LOD filter. This needs confirming from the vendor NPX data.
- So we have **no measurement of the drug's target in patients.**

**Severity is associated with almost everything.** 82% of the 1,094 assays have OR > 1, 35% reach nominal p < 0.05, and 98% of those point upward. Any single association therefore needs a comparator.

**The comparator that matters, the proteins AX-1177 actually blocks, is null.**
- 913 measured proteins have genes quantified in vitro.
- The 100 that are ≥ 2-fold induced by IL-33 and ≥ 2-fold reversed by AX-1177 have median z 1.44, versus 1.42 for the rest (Mann–Whitney p = 0.98).
- For the core programme (≥ 8-fold induced, ≥ 75% reversed; 31 proteins), p = 0.67, and a random-set permutation gives p = 0.55.

**The most IL-33- and endothelium-specific products are not associated with outcome:**

| Protein | OR | p |
|---|---|---|
| VCAM-1 | 1.28 | 0.44 |
| CXCL6 | 1.02 | 0.95 |
| CXCL5 | 1.17 | 0.52 |
| G-CSF | 1.25 | 0.23 |
| CXCL1 | 1.28–1.40 | ≥ 0.28 |
| ICAM-1 | 1.67 | 0.11 |
| E-selectin | 2.08 | 0.022 (adj. p = 0.09; nominal only) |

The IL-33-inducible proteins that *are* associated (IL-6, PTX3, OPG, CCL20, IL-8) are broadly inducible inflammatory proteins.

**What does track severity:**
- Myeloid and neutrophil activation: CLEC5A, FCAR, IL1R2, IL18R1, CD177, PRTN3, resistin (z 3.3–3.9).
- Endothelial injury markers that IL-33 does **not** induce in vitro: vWF (OR 3.87), ANGPT2 (2.21), sFLT1 (4.70).
- HGF (the top hit, not IL-33-inducible in vitro), IL-6, and many intracellular proteins.
- Classic type-2 and mast-cell markers are null: eotaxin-1/-2, TARC, IL-5, CD23, tryptase, KIT, HPGDS, MCP-4. Two granulocyte proteins are nominal (ECP p = 0.011; IL-5Rα p = 0.059), but neither survives FDR.

**sST2 ranks high but does not show mechanism.** It is the #2 hit (OR 3.02, z = 4.30, adj. p = 0.0075), but:
- *(context)* it is a decoy receptor for IL-33;
- in our HUVEC data, IL-33's induction of *IL1RL1* (+1.6 log2) carries an unusable SE (8.3), and it is not reversed in HGMEC (+0.2).

It is a good prognostic marker, not evidence that IL-33 is active.

**Technical notes:**
- 27 proteins are measured on 2–4 panels (IL-6 four times), so the 178 "significant" assays are 169 unique proteins.
- Cross-panel agreement is excellent (r = 0.97 for log-OR), so the assay layer is sound.
- "OR per log unit", applied to NPX values that are already on a log2 scale, is not comparable across assays: OR size tracks CI width (ρ = 0.42), while z does not (ρ = 0.03). SPON2's OR of 93 (CI 1.4–6,326) is a scale artefact. All ranking here uses z.

### 4.3 The tissue shows no COVID-specific IL-33 signal (Fig 4)

**Unit of analysis.**
- The 74 blocks come from 31 donors; three COVID+ donors contribute 24 of the 49 COVID+ blocks.
- Block-level tests are therefore pseudo-replicated. At block level, endothelial and VSM IL-33 look significantly lower in COVID than in controls (p = 0.011 and 0.009). At donor level they are not (p = 0.08 and 0.13).

**Group labels.** 9 of 31 donors carry labels contradicted by their own pathology text:
- four "COVID− pneumonia" donors with no documented pneumonia;
- three "non-pneumonia" controls with acute or organising pneumonia, acute pneumonitis, or pulmonary coccidioidomycosis;
- two "COVID+ pneumonia" donors with no acute pneumonia.

There is no normal-lung control, and one donor lacks a SARS-CoV-2 status.

**Donor-level results, using pathology-verified groups:**
- IL-33 does not differ between COVID+ (n = 14) and COVID− (n = 9) acute pneumonia in any compartment. Cliff's δ: basal epithelium +0.25 [−0.33, 0.78]; endothelium −0.24 [−0.66, 0.22]; VSM −0.36 [−0.75, 0.11].
- It also does not differ between COVID+ donors with and without diffuse alveolar damage or acute lung injury.
- Endothelial IL-33 sits at or near the top of the scale in every group (median 4.8 in COVID+; 5.5 in both COVID− groups), so an increase could hardly have been detected.
- The only nominal finding is **lower** endothelial IL-33 in acute pneumonia of any cause (δ −0.50; permutation p = 0.038). IHC cannot tell release from down-regulation, and this would not survive multiplicity correction.

**Inflammatory cells.**
- Neutrophil elastase, IL-5Rα and H&E eosinophils are higher in pneumonia than in non-pneumonia (donor-level p 0.005–0.05). Eosinophil granule-protein scores are inconsistent: MBP even reverses direction once labels are corrected. No inflammatory-cell score differs between COVID+ and COVID− pneumonia (all p > 0.1).
- IL-5Rα tracks neutrophil elastase (ρ ≈ 0.87), not eosinophil granule proteins (ρ ≤ 0.32), so it cannot be read as a type-2 marker here. The infiltrate is neutrophil-dominant.

**Score handling.**
- The numeric columns are the text scores plus 0.5, which produces values up to 5.5 on a documented 0–5 scale. IL-33 exists only in this transformed form.
- Endothelial and VSM IL-33 correlate with donor age (ρ ≈ 0.55).

---

## 5. Anticipated challenges

**"sST2 is the second-strongest predictor out of 1,094. Doesn't that validate the pathway?"**
It validates sST2 as a prognostic marker.
- The ligand was not measured.
- The proteins downstream of IL-33 that AX-1177 blocks are not enriched among severity markers (p = 0.55).
- In our own cells, sST2 is not a reliable IL-33 read-out.

**"IL-6, PTX3, OPG, CCL20 and IL-8 are all blocked by AX-1177 and all predict outcome."**
- They predict outcome at the same rate as random proteins in this cohort.
- The IL-33/endothelium-specific products do not predict it.
- The top severity markers (HGF, CLEC5A, SEMA4C, sFLT1, GDF15) are not IL-33-inducible in vitro.

**"It is potent. Isn't that enough?"**
Potency is necessary, not sufficient. Ours is also a single high-dose observation: there is no IC50, and affinity is not in this dataset.

**"IL-33 is abundant in the lung."**
It is abundant in every group, controls included, at or near the scale ceiling. Its distribution is neither disease- nor COVID-specific, and IHC measures stored IL-33, not released IL-33.

**"Isn't dropping premature, since IL-33 was never measured?"**
Yes, that is the decisive gap. That is why Gate B exists: it is cheap and uses banked sera. Continuing the full programme without it is not defensible.

**"The RNA-seq tables call E-selectin and VCAM-1 non-significant. Is the pharmacology real?"**
Yes. Independent-sample replication gives r = −0.998. The p-values are an artefact of the modelling, not of the biology.

**"Off-target liabilities?"**
None at the transcriptional level in four cell types at 10 µg/mL. Our package contains no toxicology, tissue cross-reactivity, PK or immunogenicity data.

**"Could it work in influenza or RSV?"**
Our data cannot address other viruses. The tissue data suggest that any IL-33 role would be pathogen-agnostic, which is why the re-entry hypothesis is framed that way.

---

## 6. Forward view

### 6.1 Which indication do our data point at?

Not a new disease area, and not a specific virus. Three features converge:

1. **A demonstrated mechanism.** IL-33 activates endothelium: adhesion molecules; neutrophil-recruiting chemokines and growth factors (CXCL1/2/3/5/6/8, GM-CSF, G-CSF); and a procoagulant switch. AX-1177 blocks all of it in HUVEC and reverses it in glomerular endothelium.
2. **Matching human severity biology.** In our cohort, severity is driven by myeloid/neutrophil activation and endothelial injury, with high sST2. The lung infiltrates are neutrophil-dominant, and IL-33 is abundant in endothelium.
3. **No pathogen specificity** in the tissue.

The only forward hypothesis our data support is a host-response endotype: **early, sST2-high severe pneumonia or early lung injury, regardless of pathogen**, in which an IL-33 → endothelium → neutrophil axis would have to be active. This narrows and re-frames the population (biomarker-defined, pathogen-agnostic); it is not a new therapeutic area. It remains **hypothesis-grade until Gate B passes.**

| Option | Support in our data | Verdict |
|---|---|---|
| Severe viral LRTI, unselected (current) | Pharmacology only; no human mechanism | **Drop** |
| sST2-high severe pneumonia, pathogen-agnostic | sST2 prognostic independent of NEWS2; no COVID specificity in tissue; mechanism fits the neutrophil/endothelial severity biology | **Only re-entry route; gated** |
| Type-2 airway disease (e.g. asthma) | No type-2 serum signal; eosinophil IHC not linked to asthma notes (EPX δ −0.39 [−0.85, 0.14]); IL-5Rα stain behaves like a neutrophil marker; no epithelial IL-33 data | Not supported |
| COPD | Basal-epithelial IL-33 trend in COPD/emphysema (δ +0.32 [−0.09, 0.69], p = 0.14); no epithelial or oxidised-IL-33 data | Not supported (a data gap, not evidence against) |
| Kidney / glomerular endothelial disease | HGMEC reversal, but the IL-33 response is unquantified; KIM-1 weak (p = 0.03); cystatin C null; no kidney tissue | Not supported |
| Thrombo-inflammation | Procoagulant switch reversed in vitro; serum TF z 2.6, PAI-1 z 2.0; thromboemboli in 4/16 COVID+ vs 0/15 COVID− donors | Hypothesis only |

### 6.2 What the next studies must establish, in order

1. **IL-33 is present and released in the target patients.** Measure it directly (total, reduced, oxidised, and the IL-33:sST2 complex) and show it is associated with outcome independent of NEWS2 and IL-6.
2. **It acts on endothelium in those patients.** Patient serum should induce an endothelial programme that AX-1177 (vs isotype) reduces.
3. **Pathway-high patients can be identified at enrolment.** sST2 and/or IL-33 should identify them, and the proximal PD markers should move with IL-33 levels.
4. **Potency covers the relevant forms in the relevant cells.** Test reduced, oxidised, full-length and protease-matured IL-33 in lung microvascular endothelium and primary airway epithelium, using multiple donors, with vehicle and isotype arms in every cell type.
5. **The statistical defects are fixed:**
   - RNA-seq re-fitted per cell line;
   - proteomics reported one assay per protein, with per-SD odds ratios and multivariable adjustment;
   - tissue analysed per donor, with adjudicated labels and a second reader.

### 6.3 Biomarkers, roles in patients, and sampling timepoint (Fig 5)

| Marker | Evidence in our data | Can go into patients? Role |
|---|---|---|
| **sST2** | OR 3.02 (1.83–5.01), z 4.3, NEWS2-adjusted | **Yes, first in line: prognostic enrichment / stratification at enrolment.** Set the threshold on the NPX re-fit and validate it externally. Not a PD or target-engagement marker |
| **IL-33** (total / free; reduced / oxidised; IL-33:sST2 complex) | Not in our data (absent from delivery) | **Yes, once an assay is validated: target engagement** (drug–IL-33 complex, free IL-33 suppression), and pathway-high selection if Gate B passes |
| **E-selectin (soluble)** | +11.2 log2 at 6 h in HUVEC; 97–100% reversed; −8.7 in HGMEC; endothelium-specific; serum OR 2.08 (p = 0.022) | **Yes: exploratory proximal PD** |
| **OPG, PTX3, CCL20** | Fully reversed in vitro; associated with outcome (z 3.3–3.9; OPG replicated on 2 panels) | **Yes: exploratory PD with prognostic value** |
| IL-6, IL-8, MCP-1, tissue factor, PAI-1, fractalkine | Induced and reversed in vitro; associated with outcome but broadly inducible | Secondary / distal PD only. IL-6 is confounded by standard-of-care IL-6R blockade |
| sVCAM-1, sICAM-1, G-CSF, GM-CSF, CXCL1/5/6 | Strongly induced and reversed in vitro; **not** associated with outcome (GM-CSF not measured) | No, not for patient efficacy or enrichment. Use as in vitro / ex vivo read-outs (serum bioassay) |
| vWF, ANGPT2, sFLT1 | Associated with outcome; **not** IL-33-driven in vitro | Severity covariates. Specificity controls: PD markers should move, these should not |
| NFKBIA, TNFAIP3, TRAF1, SELE and CSF2 transcripts | Canonical early IL-33 read-outs | In vitro / ex vivo PD tools only |

**Sampling timepoint.**
- **Patients.** Use one anchoring sample **at enrolment (hospital admission, before any study drug).**
  - This is the timepoint at which our cohort shows sST2's prognostic value independent of NEWS2, and the point at which a treatment decision would be made.
  - On-treatment PD samples must be taken early (within about 24 h of dosing). In vitro, the IL-33-driven programme is much larger at 6 h than at 24 h (4,031 vs 1,836 genes; E-selectin +11.2 vs +4.7 log2), so it is transient.
  - The exact schedule needs a kinetic sub-study; our data contain only the enrolment timepoint.
- **In vitro and ex vivo assays: 6 h.** At 6 h versus 24 h:
  - the IL-33 response is maximal (4,031 vs 1,836 genes; E-selectin +11.2 vs +4.7 log2);
  - the isotype arm is cleanest (retains 95% vs 86% of the response);
  - neutralisation is most complete (95% vs 82%);
  - cross-bed reversal is broadest (HGMEC 47% vs 8% of the programme).

  At 24 h, secondary programmes (complement C3/C1R/C1S, IFIT1/2/3) and isotype dampening confound the read-out.

### 6.4 Plan and gates

The thresholds below are proposals for the committee to agree before any data are unblinded.

| Gate | Work | Material | Time | Go criterion (proposed) | If no-go |
|---|---|---|---|---|---|
| **A** | Archive re-analysis: re-fit RNA-seq per cell line and extract the missing HGMEC IL-33 and isotype contrasts; proteomics from NPX level (retrieve IL-33 values and LOD, per-SD ORs, one assay per protein, multivariable with IL-6, renal function, time from symptom onset and treatments); re-adjudicate post-mortem labels and add a second reader | Archived counts and model object, Olink NPX, pathology | ~6 weeks | Neutralisation confirmed with per-line statistics; HGMEC IL-33 response quantified; sST2 still prognostic in the per-SD multivariable re-fit; any IL-33 NPX data retrieved and assessed | Terminate |
| **B** | Measure IL-33 (total, reduced, oxidised, IL-33:sST2) in banked enrolment sera (n = 100). **Ex vivo serum bioassay:** HUVEC + 10% patient serum ± AX-1177 vs isotype, read out at 6 h (SELE, VCAM1, CSF2, CCL20, TNFRSF11B, F3). qPCR on the 22 banked lung RNAs | Banked sera, banked tissue RNA, existing assay | ~3 months | IL-33 detectable in ≥ 50% of patients **and** associated with outcome independent of NEWS2 and IL-6; **and** AX-1177 reduces serum-induced endothelial activation by ≥ 30% in sST2-high or event sera | **Terminate or out-license** |
| **C** | Pharmacology package: IC50/IC90 against reduced, oxidised, full-length and protease-matured IL-33; lung microvascular endothelium and airway epithelium at air–liquid interface; ≥ 3 donors; vehicle and isotype in every cell type; pre-incubated and concurrent formats; oxidised-IL-33 RAGE/EGFR read-outs; anti-ST2 comparator | New wet lab | ~3–4 months | Complete neutralisation at achievable exposures; differentiation shown if we claim it | Re-scope claims or stop |
| Then | Biomarker-rich Phase 1b/2a in sST2-high early severe pneumonia (pathogen-agnostic), using the sampling scheme above | — | — | — | — |

---

## 7. Considered and ruled out

**Analytical readings I tested and rejected:**
- **Delivered RNA-seq p-values at face value.** Rejected because of the pooled-model artefact (section 4.1). I used fold-changes plus disjoint-sample replication instead.
- **Neutralisation quoted against IL-33 alone.** Rejected because the isotype dampens the response at 24 h; I used the isotype-matched arm.
- **Antibody-alone hits as off-target biology.** Rejected: they are noise or deflated SEs, with no recurrent or coherent pathway.
- **Serum hits counted per assay, ranked by OR.** Rejected because of cross-panel duplicates and the non-comparable OR scale. I used one assay per protein and ranked by z.
- **sST2 as proof of mechanism.** Rejected (sections 4.2 and 5).
- **The set of IL-33-inducible severity proteins as a translational bridge.** Rejected: there is no enrichment over random proteins.
- **Block-level tissue statistics, or GEE with 21 clusters.** Rejected: both are anti-conservative. The donor level is the unit.
- **Tissue group labels as delivered.** Rejected: 9 of 31 conflict with the pathology.
- **IL-5Rα IHC as eosinophil or type-2 evidence.** Rejected: it tracks neutrophil elastase.
- **A COVID-specific IL-33 hypothesis.** Rejected: there is no donor-level difference; if anything, IL-33 is non-significantly lower in COVID.
- **Renal clearance as the cause of the global serum shift.** Checked: cystatin C is not associated (OR 1.39, p = 0.18). I cannot fully exclude it without eGFR.
- **A sheet mix-up or truncation in the 123 MB contrasts workbook.** Checked: the "6h" and "24h" sheets are value-identical copies of all 24 contrasts, and nothing is truncated.

**Strategic options I considered and ruled out:**
- **Keep the current programme as is.** Ruled out: there is no human evidence of mechanism (sections 1–4).
- **Reposition now to type-2 airway disease, COPD, kidney disease or thrombo-inflammation.** Ruled out: our data do not support any of them (table 6.1).
- **Terminate immediately, without Gate B.** Ruled out. The decisive experiments are cheap and use material we own, and the pharmacology has residual value for re-entry or out-licensing.

---

## 8. Data-quality register (summary; the full 26-item register is in the workbook)

- **RNA-seq:**
  - The "6h" and "24h" sheets each hold both timepoints and are duplicates.
  - A single model was fitted across four cell types, giving 1,024 genes with inflated SE and deflated SEs for housekeeping genes.
  - HGMEC has no vehicle arm, and no isotype-vs-vehicle contrast was delivered.
  - The epithelial lines received no IL-33, and DMSO was used as the vehicle for an antibody.
  - Single IL-33 form, single dose, single-donor cells.
  - The "Nontreated" vs "Vehicle" naming is inconsistent.
- **Serum proteomics:**
  - IL-33 is absent from the delivery.
  - 27 proteins are duplicated across panels.
  - The OR scale is ambiguous (log of log2 NPX?).
  - Two columns are undocumented; their denominators imply 56 non-events and 44 events.
  - Single centre, pre-vaccination, SARS-CoV-2 only.
- **Post-mortem:**
  - Pseudo-replication.
  - Donor fields appear only on some rows.
  - 9/31 group labels conflict with pathology.
  - No normal controls; one donor's SARS-CoV-2 status is missing.
  - The numeric scores are transformed, reaching 5.5 on a 0–5 scale.
  - Ceiling effect in endothelium; single reader.
  - IL-5Rα behaves like a neutrophil stain.
  - Elderly, all-white donor pool.

---

## 9. Methods (brief) and files

**RNA-seq.**
- Used one copy of the value-identical duplicate sheets.
- Derived additive contrasts from the single fitted model.
- Approximated SEs as logFC/t.
- Measured neutralisation relative to the isotype-matched arm, using genes with SE < 0.5 as the reliable set.
- Replicated fold-changes for SE-inflated genes using contrasts on disjoint samples.

**Proteomics.**
- Reconciled panel suffixes and synonyms to 1,063 unique proteins and mapped them to HGNC symbols.
- Computed z = ln(OR) / [(ln u95 − ln l95) / 3.92].
- Tested enrichment of the in vitro IL-33 / AX-1177 gene set with Mann–Whitney and random-set permutation.

**Post-mortem.**
- Parsed the ordinal strings, forward-filled donor fields by Sample ID, and aggregated to donor means.
- Hand-curated pathology flags from the free text.
- Used donor-level Mann–Whitney, Monte Carlo permutation tests (200,000 permutations) and Cliff's δ with bootstrap CIs (4,000 resamples).

**Files:**
- `figures/Fig1`–`Fig5`.
- `tables/AX-1177_supporting_evidence.xlsx`: README, data-quality register, contrast summary, HUVEC neutralisation (6 h, 24 h), classified antibody-alone hits, annotated serum proteomics, biomarker matrix, donor-level post-mortem table and tests.
- `analysis_code/`: all scripts.
