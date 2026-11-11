# AX-1177 (anti-IL-33 mAb): portfolio audit position

**Basis:** Only the five delivered files were used: the methods annex, the HUVEC IL-33 RNA-seq, the RNA-seq contrasts, the serum proteomics and the post-mortem lung IHC. Every number below can be regenerated from `code/` (scripts 01–03; 04–05 render this memo). Outside knowledge appears only where it is labelled as such.

---

## 1. Bottom line

**Recommendation: KEEP AX-1177, but re-scoped and gated. Do not keep it in its current framing.** Fund only the next decisive, low-cost step (Gates 0–1, §6). Hold in-vivo, CMC and clinical spend until Gate 1 reads out. Each gate has a kill criterion agreed in advance.

1. **The molecule works as designed, and cleanly.**
   - In HUVEC, reduced IL-33 (30 ng/mL) changes **4,031 genes at 6 h**. The program is NF-κB endothelial activation: leukocyte recruitment plus a pro-coagulant shift.
     - Induced: E-selectin +11.2 log2, GM-CSF +10.3, CCL20 +9.2, IL-6 +5.8, tissue factor (F3) +5.6.
     - Reduced: thrombomodulin −1.0.
   - Against the isotype control, AX-1177 neutralises a **median 92 % of every gene IL-33 induces >4-fold** (n = 346) at 6 h, and 72 % at 24 h.
   - In a second endothelium from a different vascular bed (glomerular microvascular, HGMEC), it lowers **60 of the 61 most-induced genes**.
   - On its own it has **no reproducible effect** in four cell types.
2. **The pathway it blocks is active in the patients we would treat, and it marks who deteriorates.**
   - The cohort: 100 hospitalised COVID-19 patients, 44 with ICU admission, invasive ventilation or death (ICU/IMV/death) within 30 days. The 44 is inferred from the delivered table.
   - Of 1,094 serum proteins, **soluble ST2 (sST2, the IL-33 decoy receptor) is the #2 predictor of that outcome**: OR 3.02 per log unit (95 % CI 1.83–5.01), BH-adjusted p = 0.0075.
     - This holds independently of age, sex and NEWS2 at enrolment.
   - The IL-33-inducible endothelial proteins that AX-1177 switches off in vitro also track outcome:
     - IL-6, significant on 4 separate panels
     - OPG and IL-18R1, both BH < 0.02
     - CCL20 and CCL7
     - CSF-1 and IL-8
     - tissue factor, uPA and E-selectin, nominal p < 0.05
3. **The causal link from IL-33 to outcome in patients is *not* shown, and we should say so.**
   - **IL-33 itself is absent from the serum delivery.** It is dropped together with 14 other Inflammation-panel assays that are usually undetectable in serum (e.g. IL-4, IL-5, IL-13, TSLP, IL-2). This is inferred from vendor panel content.
   - **Lung IL-33 protein is constitutive**, and it is not increased in COVID-19 at donor level.
   - **The IL-33-responsive gene set as a whole** is no more linked to outcome than other inflammation proteins (p = 0.56).
   - That matters because **82 % of all 1,094 proteins trend higher in the severe group.**
4. **Our data support a narrower, different indication than "severe lower respiratory viral infection".**
   - The supported indication is **hospitalised viral pneumonia with an endothelial / thrombo-inflammatory phenotype, identifiable at admission by high sST2**.
   - So far this is evidenced for SARS-CoV-2 only, and only in the pre-vaccination era.
   - Three independent data types converge on the vasculature. None supports an airway/type-2 or a pan-viral framing.
5. **The next studies must establish five things:**
   - neutralisable IL-33 activity in patient material (sST2-high sera on primary lung microvascular endothelium, AX-1177 vs isotype);
   - a sensitive direct measurement of IL-33;
   - potency against oxidised and native IL-33;
   - replication of sST2's prognostic value in vaccinated COVID-19, influenza and RSV;
   - whether the in-vitro IL-33 endothelial signature is present in diseased lung. Lung RNA already exists for 22 of the post-mortem donors.
6. **Biomarkers for patients:**
   - **sST2 at enrolment (pre-dose): prognostic enrichment / stratification.** Usable now, once a cut-off is set and the assay is transferred to a clinical platform.
   - **CCL20, OPG, IL-18R1, tissue factor and E-selectin at 24 h post-dose: exploratory pharmacodynamic (PD) markers.**
   - **Total (drug-bound) IL-33: target engagement**, once an assay exists.
   - Not for patient use: IL-33 measured by Olink, tissue IHC, and eosinophil/type-2 markers.

---

## 2. Evidence scorecard

| Question the committee will ask | What our data show | Status |
|---|---|---|
| Does AX-1177 neutralise IL-33 in human cells? | **Reduced IL-33 on two endothelial types: yes.** HUVEC: 92 % (6 h) / 72 % (24 h) median neutralisation of genes induced >4-fold. HGMEC: 60/61 core genes lowered (48 at FDR < 0.05). | **Strong** (reduced IL-33, endothelium) |
| Is it specific? | AX-1177 alone vs isotype, 4 cell lines × 2 times: 21–73 FDR hits per contrast, almost all low-expressed or trivially small (<1.2-fold). No gene recurs in ≥3 of 8 contrasts; profiles uncorrelated (\|r\| ≤ 0.23). No IL-33-like signal in unstimulated cells. | **Strong** |
| Does it block oxidised IL-33 or the epithelial arm (the stated reason it binds both forms)? | **Not tested.** The epithelial lines (A549, MCF7) never received IL-33, and there is no oxidised-IL-33 arm. | **Gap** |
| Potency, dose, timing? | One concentration (10 µg/mL ≈ 68 nM vs IL-33 1.7 nM, ≈41-fold molar excess), added concurrently with IL-33. Potency and affinity are "held in the biologics file", outside this dataset. | **Gap** |
| Is the IL-33 axis engaged in target patients? | sST2 is #2 of 1,094 serum proteins for ICU/IMV/death, independent of NEWS2. IL-33 itself is not measured. | **Moderate, indirect** |
| Does the biology AX-1177 blocks track outcome? | The endothelial, neutrophil and IL-6 compartments are shifted, and type-2 is null. 33 of the 87 IL-33-inducible, AX-1177-reversible proteins are outcome-linked (p < 0.05; 18 at BH < 0.05). That is the same rate as other proteins (38 % vs 37 %), so the set-level test is null. | **Moderate** |
| Is IL-33 present or altered in diseased lung? | Constitutive in all 31 donors. Not increased in COVID-19. Endothelial/VSMC IL-33 is borderline lower with COVID and with acute injury. | **Weak / neutral** |
| Does it generalise beyond SARS-CoV-2? | No data. Single centre, pre-vaccination COVID-19 only. | **Gap** |
| In-vivo efficacy, PK? | None in the dataset. | **Gap** |

---

## 3. The case for keeping, as strong as the data allow

### 3.1 AX-1177 does what it is designed to do, and nothing else (Fig. 1)

**IL-33 produces a large, coherent endothelial program.**
- HUVEC 6 h: 4,031 genes at FDR < 0.05; 1,068 also change more than 2-fold (645 up, 423 down). HUVEC 24 h: 1,836 genes (512 with |log2FC| > 1).
- The induced genes are the canonical endothelial-activation set:
  - adhesion molecules: *SELE*, *VCAM1*, *ICAM1*;
  - neutrophil and monocyte chemokines: *CXCL1/2/3/5/6/8*, *CCL2*, *CCL20*, *CX3CL1*;
  - myeloid growth factors: *CSF2*, *CSF3*, *CSF1*;
  - cytokines: *IL6*, *TNF*, *IL1A/B*.
- There is also a **pro-thrombotic switch**:
  - tissue factor (*F3*) +5.6 log2, PAI-1 (*SERPINE1*) +1.7 and uPA (*PLAU*) +1.5;
  - thrombomodulin (*THBD*) −1.0, plus a non-significant trend for eNOS (*NOS3*, −1.1).

**The antibody removes that program.**
- **HUVEC, compared against the isotype-matched arm (IL-33 + IC119):**
  - 6 h: the 346 genes induced >4-fold are neutralised by a median **92 %**.
  - 24 h: the 176 such genes are neutralised by a median **72 %**.
  - The headline mediators are **86–106 % neutralised at 6 h**: CSF2, CCL20, CXCL2/3/5/6, CXCL8, TNF, IL-6, ICAM1, CSF3, E-selectin, VCAM-1, tissue factor.
  - Most stay ≥83 % neutralised at 24 h. The lower 24 h median comes from other genes, mainly interferon-type ones.
- **HGMEC, a different vascular bed:**
  - 60 of the 61 genes that IL-33 induced >16-fold in HUVEC are lowered by AX-1177 (48 at FDR < 0.05), by a median of about 10-fold.
  - HGMEC has no vehicle arm, so its own IL-33 response cannot be measured directly. But AX-1177 alone does nothing, so these reductions are a lower bound on that response.

**The antibody is specific.**
- Alone, AX-1177 vs isotype gives 21–73 FDR hits per contrast across HUVEC, HGMEC, A549 and MCF7 at both times. Almost all are in low-expressed genes or are trivially small (<1.2-fold).
- No gene is hit in 3 or more of the 8 contrasts, and the fold-change profiles are uncorrelated.
- There is no agonism and no IL-33-like (or anti-IL-33-like) signature in unstimulated endothelium (slope −0.01 to 0.02).

**The response is IL-33, not contamination.** A specific anti-IL-33 antibody abolishes the response and the isotype does not. So endotoxin contaminating the recombinant IL-33 could explain at most the small residual. This is a frequent challenge to recombinant-cytokine data, so it is worth making explicitly.

### 3.2 The IL-33/ST2 axis is engaged in our target patients and marks those who deteriorate (Fig. 2)

**The sST2 result.**
- sST2 ranks **#2 of 1,094 assays**: OR 3.02 per log unit (1.83–5.01), p = 1.7 × 10⁻⁵, BH = 0.0075 (0.009 when recomputed over unique proteins).
- The model adjusts for age, sex and **NEWS2 at enrolment**, so sST2 adds information beyond bedside severity.

**Alternative explanations for sST2 are weak in our own data.**
- sST2 is also a heart-failure marker, but the cardiac markers are weak: NT-proBNP OR 1.20–1.24 (p 0.05–0.17); troponin I 1.18 (p = 0.11).
- Renal clearance does not explain it either: cystatin C OR 1.39 (p = 0.18).

**The wider IL-33/IL-1-receptor family also tracks outcome:** IL-18R1 (OR 6.07, BH 0.018), IL-1R2 (4.52, BH 0.018), IL-1β and IL-1Ra. Category median OR 2.39, the highest of the 9 biological categories.

### 3.3 The biology AX-1177 blocks is the biology that tracks outcome: endothelium, not type-2 (Figs 2 and 4)

**Ranked by median OR, the outcome-linked serum compartments are:**

| Compartment | Median OR | Assays at p < 0.05 |
|---|---|---|
| IL-33/IL-1 receptor axis | 2.39 | 8/12 |
| IL-6 core inflammation | 2.10 | 14/16 |
| Neutrophil activation | 1.87 | 10/16 |
| Endothelial injury and coagulation | 1.82 | 19/45 |

- The endothelial hits include **HGF (#1)**, **PTX3 (#6)**, VEGF-A, uPAR, vWF, tissue factor, ANGPT2, E-selectin and PAI-1.
- **Type-2 / eosinophil markers are flat** (category median OR 1.00): eotaxins CCL11 and CCL24, IL-5 and CCL17 are all null.

**Of the 87 IL-33-inducible, AX-1177-reversible genes whose proteins are on the panels, 33 are outcome-linked (p < 0.05; 18 at BH < 0.05).** That is the same rate as for all other proteins (38 % vs 37 %), so we cannot claim the IL-33 program as a whole is prognostic. From these we short-listed 12 endothelial effectors with large in-vitro effects, reversal in both vascular beds, and outcome links. This is our PD-marker shortlist (Fig. 4; `tables/biomarker_bridge_candidates.csv`):

| Protein | In vitro: IL-33 log2FC (HUVEC 6 h) | AX-1177 reversal: HUVEC / HGMEC | Serum OR (p) |
|---|---|---|---|
| CCL20 | +9.2 | −9.8 / −5.6 | 1.83 (8 × 10⁻⁴) |
| OPG | +4.8 | −5.0 / −1.9 | 6.8 (2 panels) |
| IL-18R1 | +3.6 | −3.5 / −2.4 | 6.07 |
| Tissue factor | +5.6 | −5.5 / −3.3 | 3.02 (p = 0.009) |
| E-selectin | +11.2 | −11.0 / −8.7 | 2.08 (p = 0.022) |
| IL-6 | +5.8 | −6.0 / −2.9 | 2.1–2.3 on 4 panels |

The other six are PTX3, CCL7, CSF-1, uPA, IL-8 and PAI-1.

### 3.4 The lung holds an IL-33 reservoir, and the pattern in injured lungs is consistent with release (Fig. 3)

*This section is hypothesis-generating only.*
- IL-33 is abundant in lung endothelium and basal epithelium in every group. For endothelium, 39 of 74 blocks score the maximum recorded value.
- At donor level, age-adjusted, COVID-19 lungs show **lower** endothelial IL-33 (−0.35, p = 0.064) and lower VSMC IL-33 (−0.58, p = 0.064). Basal-epithelial IL-33 does not differ (p = 0.93).
- Endothelial IL-33 falls as neutrophil elastase rises: ρ = −0.43, p = 0.016; age-adjusted p = 0.035.
- It is also lower in any acute lung injury, whether or not the lung is COVID-positive: 4.88 vs 5.50, p = 0.028.
- A fall in nuclear staining fits alarmin release from injured endothelium. IHC cannot prove release.

### 3.5 The asset comes with a biomarker strategy built from our own data

The three roles are already populated (§7):
- **Selection:** sST2, prognostic and independent of NEWS2.
- **PD:** the shortlist above, which AX-1177 reverses in two endothelial beds and which links to outcome in patients.
- **Target engagement:** total IL-33, once an assay is built.

Dropping the asset now discards this strategy. The experiments that would confirm or kill it are cheap, because they use material we already hold:
- sera stored at −80 °C (annex §6);
- lung RNA from 22 post-mortem donors (the "Tissue RNA" IDs in the post-mortem file);
- the existing cell systems.

---

## 4. What we concede, and how to answer

| Likely challenge | Fair? | Answer |
|---|---|---|
| "You never measured IL-33 in a patient." | **Yes.** | IL-33 is not in the serum delivery. It is absent with IL-4, IL-5, IL-13, TSLP, IL-2 and the other usually-undetectable Inflammation-panel assays (15 missing of 92, per vendor panel content), which points to QC exclusion. Gate 1 adds a sensitive IL-33 assay and an ex-vivo bioassay. |
| "sST2 is a generic severity marker." | **Partly.** | 82 % of proteins have OR > 1, and the IL-33 gene set is not enriched among outcome markers (p = 0.56). But sST2 ranks #2 of 1,094, beyond NEWS2, and the cardiac and renal explanations are weak. The decisive test is whether sST2-high sera carry AX-1177-neutralisable activity (Gate 1). |
| "IL-33 isn't up in COVID lungs." | **Yes.** | Correct: it is constitutive. An alarmin acts on release, not on up-regulation. Any apparent "significance" at block level is pseudo-replication (§9). |
| "Your in-vitro stats say E-selectin and VCAM-1 are not significant." | **No.** | This is an artefact of one voom model pooled over four cell types (§9). For 119 genes the reported SE is inflated to a median of 11.7 (overall median 0.34), yet two independent contrasts mirror each other (ρ = −0.85). Reading the effect sizes is valid; a per-cell-line refit is Gate 0. |
| "Why not an anti-ST2 instead?" | **Fair.** | Within our data, nothing yet distinguishes AX-1177 from ST2-pathway blockade. Only ST2-pathway (reduced IL-33) activity on endothelium was tested. Differentiation would have to come from the untested oxidised-IL-33/epithelial arm (Gate 1). The competitive landscape is outside these files. |
| "Does it work in flu or RSV?" | **Yes.** | We have no influenza or RSV data. That is why the indication is narrowed and Gate 2 requires non-COVID cohorts. |
| "Does the isotype control itself blunt IL-33?" | **Mostly no.** | For genes induced >4-fold at 6 h, the isotype has no effect (ratio ≈ 0). The apparent "isotype effect" sits in down-regulated, low-expressed genes, where the IL-33 arm is shared between contrasts and creates regression to the mean. At 24 h there is a 7–20 % attenuation among induced genes. Worth lot QC (endotoxin, aggregates), but not a confounder of the conclusion. |

---

## 5. What the data point at, and what we would be dropping

**The indication the data support.**
- The supported indication is **hospitalised viral pneumonia (COVID-19 first) with an endothelial / thrombo-inflammatory phenotype, enriched at admission by high serum sST2**. In practice, that is the patient heading to ICU, ventilation or death, on top of standard of care.
- Three independent lines point at the vasculature:
  1. **In vitro:** IL-33 → endothelial activation plus a pro-coagulant switch, largely reversible by AX-1177 (86–106 % for the headline mediators at 6 h).
  2. **Serum:** the endothelial, coagulation, neutrophil and IL-6 compartments carry the outcome signal; type-2 does not.
  3. **Tissue:** the only IL-33 compartments that trend with COVID-19 and injury are in the vascular wall: endothelium and VSMC (p ≈ 0.03–0.07), not basal epithelium. The pathology also records thromboemboli in 4 of 16 COVID-positive donors vs 0 of 15 COVID-negative (p = 0.10).
- **Caveat:** the in-vitro arm only challenged endothelium. The convergence rests on the serum and tissue data, which were not designed around the endothelium.

**Why not "severe lower respiratory viral infection" as framed.**
- All patient data are SARS-CoV-2, single-centre and pre-vaccination.
- There are no influenza or RSV data.
- The epithelial/oxidised-IL-33 biology behind an airway framing is untested.

**The adjacent indication to test, not to claim.** Acute lung injury / ARDS with endotheliopathy regardless of virus.
- Endothelial IL-33 is also lower in COVID-negative acute lung injury (4.88 vs 5.50 in no-injury lungs, p = 0.039).
- But there are no non-COVID serum or outcome data.

**What we would be dropping, if the committee drops it.** *An anti-IL-33 antibody with clean, specific neutralisation of reduced-IL-33-driven endothelial inflammation and pro-coagulant activation in two vascular beds. Its clinical rationale in severe COVID-19 rests on one strong prognostic pathway marker (sST2) and a set of outcome-linked IL-33-inducible effectors. Its activity against oxidised/native IL-33, its potency, its in-vivo efficacy and its relevance beyond SARS-CoV-2 are all untested.*

**Why one would drop it.**
- The IL-33 → outcome link in patients is indirect: no IL-33 measurement, no tissue up-regulation, and no set-level enrichment.
- The indication as currently framed is not supported by our data.

---

## 6. Forward plan: what the next studies must establish (Fig. 5)

| Gate | Question | Design (all from existing or banked material where possible) | Decision rule |
|---|---|---|---|
| **0. Remediation** (weeks) | Is our evidence base clean? | <ul><li>Re-fit RNA-seq per cell line from the archived counts (annex §5), so SELE, VCAM1, CXCL8, IL1RL1 and PTX3 get valid p-values.</li><li>Retrieve potency and affinity from the biologics file.</li><li>Post-mortem: donor-level analysis with corrected labels and staining batch as a covariate; add a second blinded reader.</li><li>Serum: BH over unique proteins; standardised ORs.</li></ul> | Proceed |
| **1. Mechanism in patient material** (~3–4 mo*) | Is there **AX-1177-neutralisable IL-33 activity** in the target patients? | <ol><li>Banked **enrolment** sera from the 100-patient cohort, stored at −80 °C per the annex (sST2-high vs -low; events vs non-events) on primary human lung microvascular endothelial cells, AX-1177 vs isotype. Readout: SELE, F3, CCL20, IL6, TNFRSF11B, IL18R1.</li><li>A sensitive immunoassay for reduced, oxidised and total IL-33 in the same sera.</li><li>Banked lung RNA from 22 post-mortem donors (Zr4940 series: 9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia). Score the 61-gene in-vitro IL-33/AX-1177 endothelial signature (`tables/il33_endothelial_signature_core_gt16fold_6h.csv`) against COVID status, acute injury and endothelial IL-33 IHC on the same block.</li><li>Pharmacology:<ul><li>concentration-response;</li><li>pre-incubation **and** delayed addition (1–2 h after IL-33, i.e. a therapeutic setting);</li><li>oxidised IL-33 and native IL-33 from necrotic or virus-infected epithelium;</li><li>primary bronchial epithelial cells;</li><li>at least 3 endothelial donors.</li></ul></li></ol> | **Kill** if sST2-high sera show no AX-1177-sensitive activity **and** IL-33 is undetectable. **Re-direct** to the epithelial arm if IL-33 is found but only in oxidised form. |
| **2. Generalisation** (~6–9 mo*) | Does the selection/PD strategy hold outside pre-vaccination COVID-19? | <ul><li>Independent cohorts: vaccinated COVID-19, influenza and RSV.</li><li>Sample at enrolment; same ICU/IMV/death endpoint; current standard of care.</li><li>Pre-specify the sST2 cut-off.</li><li>Multi-reader tissue IHC of IL-33 loss vs E-selectin, tissue factor and micro-thrombi.</li><li>In-vivo viral pneumonia model (needs a cross-reactive AX-1177 or a surrogate).</li></ul> | **Narrow** to COVID-19 or **kill** if sST2 is not independent of NEWS2 |
| **3. First-in-patient PD** | Does AX-1177 move the PD panel in patients? | <ul><li>Hospitalised viral pneumonia, sST2-stratified, placebo-controlled, on standard of care.</li><li>Samples at enrolment (pre-dose), 24 h, day 3 and day 7.</li><li>Target engagement by total IL-33.</li></ul> | **Go** to an efficacy trial if a pre-specified PD reduction vs placebo is achieved |

\*Durations are planning assumptions, not data.

---

## 7. Biomarkers, sampling timepoint, and what goes into patients

| Marker | Evidence in our data | Role in patients | Ready? |
|---|---|---|---|
| **sST2 (IL1RL1)** | <ul><li>#2 of 1,094 predictors; OR 3.02 (1.83–5.01) beyond NEWS2.</li><li>In vitro +1.6 / −1.7 log2 (HUVEC 6 h); no change in HGMEC.</li></ul> | **Baseline prognostic enrichment / stratification** at enrolment. **Not a PD marker**: the in-vitro response is small and absent in HGMEC. Not yet shown to predict benefit; Gate 1 tests sST2-high vs -low. | **Yes**, for enrichment/stratification after cut-off validation and transfer to a clinical immunoassay (sST2 is routinely measurable; outside our data) |
| **CCL20** | <ul><li>IL-33 +9.2 (6 h) and +5.6 (24 h).</li><li>AX-1177 −9.8 (HUVEC), −5.6 (HGMEC).</li><li>Serum OR 1.83, BH 0.02.</li></ul> | **Primary PD marker.** Expected fall at 24 h vs placebo. | Exploratory PD in first-in-patient study |
| **OPG (TNFRSF11B)** | <ul><li>+4.8 / −5.0 / −1.9.</li><li>Serum OR 6.8 and 4.4 on 2 panels.</li></ul> | PD | Exploratory |
| **IL-18R1** | <ul><li>+3.6 / −3.5 / −2.4.</li><li>Serum OR 6.07, BH 0.018.</li></ul> | PD | Exploratory |
| **Tissue factor (F3)** | <ul><li>+5.6 / −5.5 / −3.3.</li><li>Serum OR 3.02, p = 0.009.</li></ul> | PD and mechanism (thrombo-inflammation) | Exploratory |
| **E-selectin (SELE)** | <ul><li>+11.2 / −11.0 / −8.7.</li><li>Serum OR 2.08, p = 0.022.</li></ul> | PD with an endothelium-specific source | Exploratory |
| IL-6 | <ul><li>+5.8 / −6.0 / −2.9.</li><li>Serum OR 2.1–2.3 on 4 panels.</li></ul> | Secondary. Confounded by steroids and IL-6R blockade in standard of care. | Use with caution |
| PTX3, CSF-1, uPA | Outcome-linked and IL-33-reversible. CSF-1's OR of 90 per log unit (CI 4–1,933) reflects assay scale, not effect size. | Secondary PD / prognostic | Exploratory |
| **Total (drug-bound) IL-33** | Not measurable in our data | **Target engagement** | Needs assay development |
| *Not recommended* | <ul><li>VCAM-1, G-CSF, CXCL5/6/10 and TNFRSF9: strongly IL-33-inducible but **not** outcome-linked.</li><li>Eosinophil/type-2 markers: null.</li><li>IL-33 by Olink: undetectable.</li><li>Tissue IHC: post-mortem only.</li></ul> | — | — |

**Sampling timepoint: enrolment (admission), before the first dose, ideally within 24 h of hospitalisation. Add a paired PD sample 24 h after dosing.**

Why enrolment:
- **It is the only timepoint at which our serum associations exist**, measured at enrolment and adjusted for NEWS2 at enrolment.
- **IL-33's action is front-loaded and most antibody-sensitive early.**
  - In vitro, IL-33-regulated genes fall from 4,031 at 6 h to 1,836 at 24 h. E-selectin drops from +11.2 to +4.7, and TNF from +7.9 to ~0.
  - AX-1177 neutralisation drops from 92 % to 72 % over the same interval.
  - The residual at 24 h is concentrated in interferon-type genes that are less AX-1177-sensitive (CXCL10 47 %, MX2 42 %).
  - So the IL-33-dependent window is early, and later samples increasingly read secondary biology.
- **Practical:** an enrolment sample comes before steroids or IL-6/JAK blockade reshape these markers.

---

## 8. What I considered and ruled out

| Option / hypothesis | Evidence | Verdict |
|---|---|---|
| Continue as pan-viral "severe lower respiratory viral infection" | <ul><li>Only SARS-CoV-2 patient data (single centre, pre-vaccination).</li><li>No influenza or RSV.</li><li>Epithelial / oxidised-IL-33 biology untested.</li></ul> | **Ruled out as framed**; narrowed (§5) |
| Type-2 / eosinophilic mechanism, or a pivot to eosinophilic airway disease | <ul><li>Serum type-2 category median OR 1.00 (CCL11, CCL24, IL-5, CCL17 null).</li><li>Lung EDN, MBP and IL-5Rα are higher in *all* pneumonias vs non-pneumonia, with no COVID+ vs COVID− pneumonia difference (p ≥ 0.44).</li><li>MBP is dominated by staining batch: ~3 in the late block series vs ≤0.8 earlier, regardless of COVID status. 2D7 shows the same step (~1 vs ≤0.5).</li></ul> | **Ruled out** |
| COPD / asthma via airway-epithelial IL-33 | <ul><li>Not testable with our data: epithelial lines were never given IL-33.</li><li>Basal-epithelial IL-33 is unrelated to COPD or asthma history (p = 0.21 / 0.34) or COVID (p = 0.76).</li><li>A549 and MCF7 serve only as specificity controls.</li></ul> | **Not supportable from our data.** This is an evidence gap, not a biological refutation. |
| Kidney (HGMEC is glomerular endothelium) | <ul><li>HGMEC responds.</li><li>Serum renal markers are weak: cystatin C OR 1.39 (p = 0.18); KIM-1 1.55–1.66 (p 0.03–0.07).</li><li>No renal outcome data.</li></ul> | **Not supported** |
| Cardiac indication (sST2 is also a heart-failure marker) | NT-proBNP OR 1.20–1.24 and troponin I 1.18 are weak; GDF-15 is moderate. | **Ruled out.** The sST2 signal is not cardiac. |
| Serum IL-33 as the selection marker | Not in the delivery (undetectable-cytokine pattern) | **Not feasible** on this platform |
| "IL-33 is over-expressed in COVID-19 lung" as the rationale | No increase in any compartment at donor level. Block-level p-values (0.017 endothelium, 0.007 VSMC) are pseudo-replication: 3 donors contribute 24 blocks. | **Rejected** |
| Off-target or agonist activity of AX-1177 | None reproducible | **Ruled out** (within these assays) |
| Endotoxin in recombinant IL-33 driving the response | Abolished by AX-1177 (92 % of the >4-fold program at 6 h), not by the isotype | **Ruled out** as the driver. At most, it could explain the residual. |
| Stand-alone thrombosis / anticoagulant positioning | <ul><li>Supportive: tissue factor and PAI-1 up, thrombomodulin down; thromboemboli 4/16 vs 0/15 (p = 0.10); serum tissue factor OR 3.02.</li><li>But too thin: no coagulation outcome data.</li></ul> | **Folded into** the endothelial-phenotype hypothesis |
| ARDS / acute lung injury of any cause | Endothelial IL-33 is also lower in COVID-negative acute lung injury, but there are no non-COVID serum or outcome data. | **Adjacent hypothesis** (Gate 2), not a claim |
| Ranking serum markers by OR size | ORs are "per log unit" of each assay's own scale (e.g. CSF-1 OR 90, CI 4–1,933) | **Rejected.** Rank by z or p instead. |
| Reading the DMSO/PBS contrasts as controls for an antibody | DMSO is not the antibody's vehicle. AX-1177 vs IC119 is the valid control. | **Rejected** |

---

## 9. How the delivered files must be read (integrity findings that change conclusions)

| File | Finding | Consequence / handling |
|---|---|---|
| Post-mortem | **IL-33 score columns (X–Z) are hidden**, as are the eosinophil IHC columns (L–P, U–W) | All hidden columns were analysed |
| Post-mortem | 127 merged cells hold the donor fields. The SARS-CoV-2 merge **J12:J13 spans two donors** (1910 and 1905), so donor 1905's status is undocumented. Clinical notes for donors 2040 and 2045 sit on the *second* block, contrary to the annex. | Donor fields rebuilt from all blocks |
| Post-mortem | 74 blocks from 31 donors; 3 donors contribute 8 blocks each (24 of 49 COVID+ blocks) | **Analysed at donor level.** Block-level p-values are inflated (e.g. EDN 0.0006 at block level vs 0.09 at donor level). |
| Post-mortem | **Disease labels conflict with the pathology text:**<ul><li>4/10 "COVID neg pneumonia" donors have no pneumonia recorded (1905, 1961, 1968, 1970).</li><li>3/5 "non-pneumonia" controls have pneumonia, pneumonitis or fungal infection (1944, 1956, 1976).</li><li>2/16 COVID+ donors have no acute lung injury (2067, 2101).</li></ul> | Sensitivity analysis with pathology-verified groups; conclusions unchanged |
| Post-mortem | Staining batch by block series (MBP ~3 in the late series vs ≤0.8 earlier; 2D7 likewise). IL-33 scores reach 5.5 on a stated 0–5 scale, with an endothelial ceiling (53 % of blocks at the maximum). | Batch covariate. Treat IL-33 as ordinal and insensitive to increases. |
| Post-mortem | All donors are elderly (64–98) and white; single reader; no healthy young controls | Limits generalisability |
| Serum | Hidden rows (HGF-ONCII, IL6-ONCII) and a hidden lower-CI column. **27 proteins appear on >1 panel** (58 assays) and are counted separately in the BH correction. | BH recomputed over 1,063 unique proteins; conclusions unchanged. Cross-panel replicates agree (e.g. IL-6 OR 2.07–2.31). |
| Serum | Delivered adjusted p-values imply BH over ~1,194 tests, not the 1,094 delivered | Correction applied before assays were excluded; slightly conservative |
| Serum | **IL-33 absent.** It is one of 15 Inflammation-panel assays missing, all typically below the limit of detection. | No direct IL-33 evidence in patients |
| Serum | Columns `composite_endpoint_0/1` are undocumented. They are multiples of 1/56 and 1/44, i.e. the per-group fraction of samples flagged (likely below LOD). | Implies 44 events out of 100 (inferred) |
| Serum | **82 % of ORs > 1; 35 % of assays at p < 0.05** | The signal is broad; single-marker specificity is limited. Rank by z or p. |
| RNA-seq | The "6h" and "24h" sheets of the contrasts workbook are **identical copies**, each holding all 24 contrasts. Excel's declared dimension (1,048,576 rows) is metadata only, with no truncation. | Use one copy |
| RNA-seq | **One voom fit across 4 cell types** inflates SE for strongly regulated, cell-type-restricted genes. Eight of the 170 genes with \|log2FC\| > 3 are FDR ≥ 0.05: SELE, VCAM1, CXCL8, CXCL1, CCL2, PTGS2, TNFAIP2, SLC7A2. IL1RL1 and PTX3 are affected too. | Effect sizes read. Independent contrasts mirror each other (ρ = −0.85, median \|sum\| 0.05), which shows the reported SE is artefactual. **Refit per cell line (Gate 0).** |
| RNA-seq | `AveExpr` is averaged over all 114 libraries | Cannot judge endothelial expression (e.g. of ST2) from these tables |
| RNA-seq | HGMEC has no vehicle arm; epithelial lines got no IL-33; reduced IL-33 only; one concentration; no pre-incubation; single donor per endothelial line (passages 2 and 5) | Limits in §2 and §4. Addressed in Gate 1. |
| RNA-seq | The HUVEC file labels the control "Nontreated"; the annex calls it "Vehicle" | Cosmetic |

---

## 10. Methods, in brief

**RNA-seq.**
- Delivered limma-voom contrasts, reshaped to gene × contrast.
- Derived contrasts were computed as exact linear combinations of the cell-means contrasts, e.g. (IL-33 + IC119) − IL-33 = [AX+IL-33 − IL-33] − [AX+IL-33 − IL-33+IC119].
- Percent neutralisation = [(IL-33+isotype − vehicle) − (IL-33+AX-1177 − vehicle)] / (IL-33+isotype − vehicle).
- Reversal was judged against the isotype arm because it shares no group with IL-33-vs-vehicle (independent noise).
- SE = logFC / t.

**Serum.**
- Assay names were mapped to gene symbols (`code/olink_map.py`).
- Wald z was recomputed from the OR and CI (consistent with the delivered p for all 1,094 rows).
- BH was recomputed over unique proteins.
- The enrichment test compares the z-scores of IL-33-inducible, AX-1177-reversible proteins (n = 87) with the other 824 mapped proteins (Mann-Whitney).

**Post-mortem.**
- Donor fields were rebuilt across merged and hidden cells.
- Scores were parsed as "n+" → n; blocks were averaged per donor.
- Tests: Kruskal-Wallis and Mann-Whitney; OLS adjusted for age and staining series; Spearman correlation.
- Pathology features came from a regex over the free-text pathology, with manual checks of negations.

**Limits of this review.**
- No count matrices and no patient-level serum data.
- The OR scale is undefined.
- The IHC is semi-quantitative with a single reader.
- All p-values are exploratory.

**Deliverables**
- `figures/fig1…fig5`
- `tables/`:
  - curated serum table;
  - in-vitro/serum bridge;
  - IL-33 endothelial signatures (61-gene core, 346-gene broad);
  - gene-level derived contrasts;
  - donor-level post-mortem;
  - contrast summaries;
  - biomarker proposal;
  - hidden-content log
- `code/01_build_tables.py`, `02_figures.py`, `03_gate_figure.py`

---

## Figures

![Figure 1](figures/fig1_invitro_neutralisation.png)

**Figure 1. In-vitro neutralisation.**
- **(A, B)** Each gene's IL-33 response in HUVEC (x) against the AX-1177 effect in the presence of IL-33, relative to the isotype (y). The dashed line y = −x means complete neutralisation. Red rings mark genes whose delivered FDR is non-significant only because of the pooled-model variance artefact.
- **(C)** The HGMEC reversal plotted against the HUVEC IL-33 response. HGMEC has no vehicle arm.
- **(D)** Genes at FDR < 0.05 per contrast: IL-33 (blue), AX-1177 reversal (green), AX-1177 alone (grey).

![Figure 2](figures/fig2_serum_proteomics.png)

**Figure 2. Serum proteomics (n = 100 hospitalised COVID-19 patients; 44 with ICU/IMV/death).**
- **(A)** Wald z by biological compartment, against the distribution of all 1,094 assays. The IL-33/IL-1-receptor, IL-6, neutrophil and endothelial compartments are shifted; type-2 is null.
- **(B)** sST2 and the IL-33-inducible endothelial effectors. The bracket gives the in-vitro IL-33 induction and AX-1177 reversal in log2FC.

![Figure 3](figures/fig3_postmortem.png)

**Figure 3. Post-mortem lung (31 donors, 74 blocks).**
- **(A)** Donor-level IL-33 scores by group, with donor-level vs (pseudo-replicated) block-level p-values.
- **(B)** The staining-batch effect on MBP.
- **(C)** Endothelial IL-33 vs neutrophil elastase.

![Figure 4](figures/fig4_biomarker_bridge.png)

**Figure 4. The in-vitro to serum bridge used to choose the PD markers.** Heat map: in-vitro log2FC. Forest plot: serum OR for ICU/IMV/death.

![Figure 5](figures/fig5_gated_plan.png)

**Figure 5. Gated forward plan with kill criteria.** The durations are planning assumptions.
