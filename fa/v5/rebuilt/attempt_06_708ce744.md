# AX-1177 (anti-IL-33 mAb): portfolio audit memo

**Scope.** This memo is based only on the five delivered files: the methods annex, the HUVEC IL-33 RNA-seq, the RNA-seq contrasts, the clinical serum proteomics and the post-mortem lung IHC. I used outside knowledge only to interpret what an assay measures (for example, that soluble ST2 is a decoy receptor), and I say so where I do. Competitive landscape, CMC, PK/tox and the biologics file (affinity/potency, which the annex says exists but was not delivered) are outside this assessment.

Figures: `figures/Fig1–Fig4`. Tables: `AX-1177_supporting_tables.xlsx` (S1–S10). Code: `code/`.

---

## 1. Recommendation

**Keep AX-1177, but conditionally: re-scope it and put it on a time-boxed decision package. Do not continue it as a "severe lower respiratory viral infection" programme in its current form.**

- **The molecule has earned a place.**
  - It neutralises reduced IL-33 almost completely in primary human endothelial cells: 95% median inhibition of IL-33-induced genes at 6 h, against an isotype control.
  - On its own it has no transcriptional effect above inert-arm background in four cell types.
- **The indication has not earned a place.** None of our human data show that IL-33 biology is specific to the disease we target, or that IL-33 output tracks severity:
  - Lung IL-33 does not differ between COVID pneumonia, non-COVID pneumonia and controls (if anything it is lower in COVID).
  - The apparent eosinophil signal depends on the delivered labels and disappears when donors are classified by their own autopsy reports.
  - IL-33's endothelial secretome is not over-represented among the serum proteins that predict a bad outcome.
  - The one supportive signal, serum sST2, is non-specific, and it could mean either more or less IL-33 signalling.
- **The decisive data are cheap, and most of them we already own.**
  - The serum IL-33 assay (the drug's own target) is on a panel that was run, but it is not in the delivered file. It is one of ~100 assays that were tested (they sit in the multiple-testing denominator) but left out of the file, and that left-out set is enriched for outcome-associated results.
  - We also hold the RNA-seq count matrix (per the methods annex), 22 lung blocks with tissue-RNA IDs already assigned, and the enrolment sera (stored at −80 °C; residual volume to be confirmed).
  - Dropping now would mean dropping an anti-IL-33 antibody without having looked at IL-33 in our own patients.
- **The drop is pre-committed.** If Gates 0–1 (about 4–5 months, §6.5) miss their criteria, we drop. **If the committee will not fund the gates, the data support dropping now, not continuing as is.**

**Where our data point.** Not to a new disease area, and not to COVID as such. They point to IL-33-driven endothelial activation (inflammatory and procoagulant) in severe viral pneumonia with diffuse alveolar damage, in patients with high sST2 at admission, treated early. Our data make this plausible but have not shown it (§5).

**What has to be shown next.**
- IL-33 is released and active in the diseased lung.
- It tracks severity beyond generic inflammation.
- AX-1177 neutralises oxidised IL-33 with adequate potency.
- Endogenous IL-33 from infected epithelium drives endothelial activation, and AX-1177 blocks it without impairing antiviral defence (§6).

**Biomarkers for patients.**
- sST2 at admission, before dosing: prognostic enrichment.
- IL-33 species: target engagement (assays needed).
- IL-6, CCL20, OPG, IL-18R1 and MCP-3: exploratory PD panel.
- Viral load and ISGs: safety.
- Tissue IL-33 IHC and eosinophil markers are not usable (§6.2–6.3).

---

## 2. Evidence for keeping the molecule

### 2.1 Pharmacology in primary human endothelium (Fig. 1)

The design: reduced IL-33 at 30 ng/mL, AX-1177 at 10 µg/mL (about a 41-fold molar excess), added at the same time (no pre-incubation), n = 3 per arm.

| Finding | Number |
|---|---|
| IL-33 response in HUVEC | 4,027 DE genes at 6 h (q<0.05, valid-statistics genes); 1,831 at 24 h |
| What IL-33 induces | NF-κB endothelial activation: GM-CSF +10.3 log2, CXCL6 +9.4, CCL20 +9.2, fractalkine +8.4, G-CSF +8.3, TNF +7.9, 4-1BB +7.1, CXCL10 +6.9, ICAM-1 +6.0 (its statistics fall in the anomalous tail, so descriptive only), IL-6 +5.8 |
| | A procoagulant switch: tissue factor +5.6, thrombomodulin −1.0 (q=2×10⁻¹⁰) |
| | An interferon tier: IFIT1–3, MX1/2, RSAD2, GBP4/5, HLA-A/B |
| Blockade at 6 h (isotype-controlled) | 644 induced genes (log2FC>1): median inhibition 95%; slope of blockade vs IL-33 effect −0.98 |
| | 72% of all IL-33 DE genes individually reversed; 84–90% of well-expressed induced genes |
| Blockade at 24 h | Median inhibition 73%; 38% of IL-33 DE genes reversed |
| | The residual sits mainly in interferon-type genes (CXCL10 43%, MX2 47%, OASL 16%); the NF-κB core is still blocked (GM-CSF 100%, CCL20 94%, 4-1BB 90%) |
| Glomerular microvascular EC (HGMEC) | The HUVEC program is reproduced: 976 genes significant in both cell types, r = 0.87, at about 0.67× the magnitude |
| Specificity | AX-1177 alone vs isotype: 18–73 DE genes per contrast (4 cell types × 2 times). Inert-vs-inert comparisons give 0–88 (e.g. vehicle vs vehicle, isotype vs vehicle) |
| | The hits are low-expression lncRNAs and pseudogenes that do not replicate across times or cells. No agonism and no off-target signature |

### 2.2 Pathway link to outcome in patients (Fig. 3)

The cohort: 100 hospitalised COVID-19 patients (pre-vaccination, single centre), with 44 events of ICU, invasive ventilation or death within 30 days.

- **sST2 ranks #2 of 1,094 serum assays.** OR 3.02 per log unit (95% CI 1.83–5.01), q = 0.0075, adjusted for age, sex and NEWS2 at enrolment.
- **The severity proteome has an endothelial-activation profile.**
  - Associated: HGF (#1), PTX3, VEGF-A, uPAR and vWF (q ≤ 0.05).
  - Borderline (q ≈ 0.05–0.09): tissue factor, ANGPT2, sFLT1 and E-selectin.
  - Structural endothelial markers are flat: PECAM-1, VE-cadherin, VEGFR2 and endoglin.
- **Several IL-33-inducible, AX-1177-reversible endothelial proteins are also prognostic:** IL-6 (OR 2.14, replicated on 4 panels), CCL20 (1.83), OPG (6.77), IL-18R1 (6.07) and MCP-3 (1.72), all q ≤ 0.02.

### 2.3 Target presence

IL-33 protein is present in every lung examined: endothelium, bronchial basal epithelium and vascular smooth muscle. Endothelial IL-33 is at the top of the scale in 53% of blocks (Fig. 2A, 2E).

---

## 3. Why the current indication does not pass audit

1. **There is no disease-specific target signal in tissue** (31 donors, analysed per donor; Fig. 2).
   - IL-33 does not differ between COVID pneumonia, non-COVID pneumonia and controls (Kruskal–Wallis p = 0.65 epithelium, 0.11 endothelium, 0.16 VSMC).
   - If anything it is lower in COVID (endothelium median 4.81 vs 5.50; VSMC 2.38 vs 3.25), and lower in lungs with diffuse alveolar damage (VSMC 1.78 vs 3.25, p = 0.055).
   - Stored nuclear IL-33 is constitutive and hits the scale ceiling. IHC cannot measure *released* (active) IL-33.
2. **There is no robust type-2 or eosinophil signal.**
   - EDN/MBP appear elevated in "pneumonia" (p = 0.004/0.006) only because of the delivered labels. 8 of 31 donors are labelled against their own autopsy report.
   - With autopsy-based classification the difference disappears (EDN p = 0.54; MBP p = 0.14, now in the opposite direction).
   - Serum type-2 markers are flat: CCL11 (two panels), CCL17, CCL24, MCP-4 and IL-5 all have OR ≈ 1.
3. **IL-33's endothelial output does not track severity.**
   - 13 of 67 IL-33-program proteins are outcome-associated, against 145 of 842 other proteins (Fisher p = 0.62).
   - The most IL-33-specific outputs are flat: CXCL6 OR 1.02, G-CSF 1.25, 4-1BB 1.09, CXCL10 1.30, CCL5 0.89.
   - Serum levels integrate many cell sources, so this is a partial test, but it is the test we have, and it is negative.
   - The program proteins that do predict outcome (IL-6, CCL20, OPG) are induced by many stimuli, not only IL-33.
4. **sST2 is not evidence of IL-33 activity.**
   - sST2 is a decoy that sequesters IL-33, so a high level is consistent with *less* IL-33 signalling as well as more.
   - It is one of 169 associated proteins.
   - The finding comes from one centre, COVID only, pre-vaccination, n = 100, with no replication.
5. **The target itself is missing from the serum delivery.**
   - IL-33 is absent, as are IL-4, IL-13, TSLP and the Inflammation-panel IL-5 (IL-5 is still measured on the Immune Response panel).
   - The delivered adjusted p-values can only be reproduced with a BH family of 1,194 tests, but 1,094 were delivered.
   - The ~100 tested-but-undelivered assays include about 16 with p < 0.05 (5 expected by chance; binomial p = 4×10⁻⁵) and one at p ≈ 0.0002–0.0003 (Fig. 3C).
6. **The differentiating claim is untested.**
   - AX-1177 is described as binding reduced and oxidised IL-33, but only reduced IL-33 was tested.
   - There is one concentration (no potency), single-donor cells, no epithelial IL-33 stimulation, no infection model and no in vivo data.
7. **Generalisation to "viral LRTI" is untested.**
   - All clinical data are COVID.
   - The non-COVID pneumonias in tissue are bacterial-type bronchopneumonias in elderly donors, not RSV or influenza.

---

## 4. Anticipated committee challenges

**"sST2 is #2 of 1,094. Isn't that validation?"**
It validates sST2 as a *prognostic* marker, and I would use it for enrichment. It does not validate IL-33 as a *driver*. sST2 neutralises IL-33, 169 proteins associate with outcome, and the IL-33-specific outputs do not. Resolving this needs IL-33 itself (among the undelivered Olink assays) and, later, dedicated IL-33:sST2 complex assays.

**"The antibody blocks IL-33 completely. Isn't that the de-risking?"**
It shows on-target function against reduced IL-33 at about a 41-fold molar excess, with clean specificity. It does not show potency or oxidised-form activity (the claimed differentiator), and it says nothing about disease relevance.

**"IL-33 is everywhere in the lung. Isn't that target validation?"**
It shows the target is present, not that it is activated. Stored IL-33 does not differ between groups and tends to be lower where there is injury, which is what release would look like, but IHC cannot show release. That is why Gate 1a uses RNA from the same lungs.

**"Why not pivot to asthma/COPD, where the class is moving?"**
Nothing in our data supports it. Donors with recorded COPD, asthma or emphysema show no IL-33 or eosinophil difference, and we have no epithelial IL-33 pharmacology. That would be a decision on external evidence with its own data package, not a conclusion from this audit.

**"Can we trust the RNA-seq?"**
Mostly, yes.
- The checks pass: AveExpr is identical across all 26 contrasts, every contrast has ~85 df, BH adjustments reproduce exactly, and logFC and t never disagree in sign.
- 205 genes have impossible statistics (SE > 3; 281 at a stricter SE > 1.6), including IL1RL1 (ST2), E-selectin, VCAM-1 and IL-8.
- The conclusions rest on the ~26,000 valid genes, and every headline number is unchanged at either threshold. The affected genes are cited only descriptively.

**"sST2 gives us an enrichment strategy. Why not just run the trial?"**
Enriching on a prognostic marker raises the event rate. It does not show that the drug's mechanism drives those events. Without evidence that IL-33 is active in these patients, a trial would be an expensive test of a hypothesis our own data have not supported. The gates produce that evidence first, at a fraction of the cost.

**"Why spend anything more?"**
Because the IL-33 serum results and the count matrix already exist, and the lung blocks already have RNA IDs. Gate 0 costs almost nothing and could end the programme within weeks.

---

## 5. Forward view: what indication our data point at

**Not a new disease area.** The data point to a narrower, mechanism-defined version of the current indication:

> IL-33-driven endothelial activation (a thrombo-inflammatory endotheliopathy) in severe viral pneumonia with diffuse alveolar damage / acute lung injury, in patients selected by high sST2 at admission and treated early.

**Why this framing.**
- The IL-33 effector compartment we can demonstrate is the endothelium: the program is reproduced in two vascular beds, including a procoagulant switch (tissue factor up, thrombomodulin down). It is also the only compartment we ever stimulated with IL-33, so this is partly a consequence of the study design.
- IL-33 protein is most abundant in lung endothelium.
- The severity proteome is endothelial-activation-rich.
- DAD (7/16 COVID vs 0/15 non-COVID donors, p = 0.007) and thromboemboli (4/16 vs 0/15) distinguish the COVID lungs.
- Vascular IL-33 trends lower in DAD lungs.
- The 24 h escape of the interferon tier argues for dosing early, before the cascade becomes IL-33-independent.

**The caveat.** IL-33 is not yet shown to be the driver. §3 point 3 is a partial negative test of exactly this hypothesis.

| Option | Verdict on our data |
|---|---|
| Severe viral pneumonia with endotheliopathy, sST2-enriched, early treatment | **Best supported**, but still a hypothesis (Gates 0–2) |
| Severe viral LRTI as currently framed (all-comers, COVID-anchored) | Not supported (§3) |
| All-cause ARDS / sepsis endotheliopathy | Untested: in our data DAD is seen only in COVID lungs |
| Type-2 airway disease (asthma, COPD) | Not supported by our data (§4) |
| Kidney (glomerular endothelium) | Not supported: HGMEC is a scaled copy of HUVEC, with no distinct glomerular program and no renal patient data |
| Oncology | Not supported: A549/MCF7 were negative-control lines without IL-33 arms |

**If we drop, this is what we are dropping.** A clean, specific neutraliser of reduced IL-33 that completely reverses IL-33-driven inflammatory, procoagulant and interferon programs in human endothelium. It has untested oxidised-form activity, no potency, PK or in vivo data, and no validated indication.

**And why.** Our own human data show that:
- IL-33 biology is not specific to the disease we targeted;
- its endothelial outputs do not track severity;
- the only positive clinical signal (sST2) is non-specific and directionally ambiguous;
- the differentiating claim was never tested.

---

## 6. What the next studies must establish

### 6.1 Five questions

1. **Is IL-33 released and active in the diseased lung, not just stored?** Test with serum IL-33 species and the IL-33 program score in the 22 archived lung RNAs.
2. **Does IL-33 activity track severity beyond general inflammation?** Test IL-33, the IL-33/sST2 ratio and sST2 from the undelivered Olink data, adjusted for NEWS2 and for generic markers such as IL-6 and HGF. Add IL-33:sST2 complexes once assays exist.
3. **Is AX-1177 potent against oxidised as well as reduced IL-33?** This is the differentiation question.
4. **Does endogenous IL-33 from virus-infected epithelium drive endothelial activation that AX-1177 reverses, without impairing antiviral defence?** Our data show AX-1177 suppresses IL-33-induced ISGs (median 75% at 24 h).
5. **Does a biomarker-defined population replicate** in a vaccinated-era cohort and in influenza/RSV?

### 6.2 Biomarkers: roles and whether they can go into patients

| Marker (matrix) | Evidence in our data | Role | Into patients? |
|---|---|---|---|
| **sST2** (serum) | #2 of 1,094; OR 3.02, q = 0.0075, independent of NEWS2 | **Prognostic enrichment** at admission | **Yes, in the first patient study.** Stratification/enrichment factor, once measured with an absolute immunoassay, with a cut-off pre-specified in our 100-patient cohort and externally replicated. Not predictive of benefit. PD use only if Gate 0 shows IL-33 drives sST2 (IL1RL1 statistics are currently invalid) and drug–IL-33–sST2 complexes do not interfere with the assay. |
| **IL-33 total/free, IL-33:sST2 complex** (serum) | IL-33 not in the delivered file; complex assays not yet run | **Target engagement / PD** | **Yes, in Phase 1 as PD**, once drug-tolerant assays exist. Selection use only if Gate 0 is positive. |
| **IL-6, CCL20, OPG, IL-18R1, MCP-3** (serum) | IL-33-induced and AX-1177-reversed in both endothelial cell types; each prognostic (q ≤ 0.02) | **PD/response panel** | **Yes, exploratory.** Not IL-33-specific in vivo, so read against placebo. |
| Tissue factor (serum) | IL-33 +5.6 log2, reversed; serum q = 0.051 | Mechanistic procoagulant PD | Yes, exploratory |
| GM-CSF, CXCL6, G-CSF, fractalkine, 4-1BB | Most IL-33-specific in vitro (≥85% reversed at 6 h); flat vs outcome in serum (GM-CSF not on the delivered panels) | Ex vivo/challenge PD (potency, occupancy) | **No** for selection; ex vivo assays only |
| HGF, PTX3, vWF, ANGPT2 (serum) | Prognostic. In vitro: HGF and ANGPT2 not IL-33-regulated; vWF fold-change ~0; PTX3 +2.2 log2 but statistics invalid | Disease-activity covariates | Yes, as covariates |
| Viral load kinetics, ISG response | AX-1177 suppresses IL-33-induced ISGs/MHC-I in endothelium | **Safety** | **Yes, mandatory** in any infected population |
| Tissue IL-33 IHC; EDN/MBP; IL-5Rα duplex | Constitutive and ceiling-limited; eosinophil signal not robust; IL-5Rα duplex does not track EPX | — | **No** |

Full matrix with numbers: Table S6.

### 6.3 Sampling timepoint

- **Patients, primary: at admission/enrolment, before dosing.**
  - This is the only timepoint at which our data show prognostic value: sST2 at enrolment predicted 30-day outcome.
  - It is also where the enrichment decision is made.
- **Patients, on treatment (proposed; to be confirmed by PK/PD).**
  - A first PD sample within 24 h of dosing, because the IL-33 program is an early, fast-decaying response.
  - A second sample at day 3–5 to capture the secondary interferon tier and the clinical trajectory.
- **In vitro / ex vivo PD, primary: 6 h after IL-33 exposure.**
  - The response is largest then (4,027 vs 1,831 DE genes; TNF +7.9 log2 at 6 h vs ~0 at 24 h).
  - AX-1177 separation is largest (95% vs 73% median inhibition).
  - 24 h is a secondary timepoint to capture escape.

### 6.4 What the in vitro kinetics imply for dosing

Even with antibody present from time zero, a share of the 24 h response escapes (mainly the interferon tier). Treatment should therefore start early after admission, in sST2-high patients who are not yet critically ill, not as rescue therapy.

### 6.5 Gated plan and kill criteria (Table S10)

| Gate | Timing | Work | Go / no-go |
|---|---|---|---|
| **0. Data recovery** | Weeks 0–6 | Retrieve all 1,194 Olink results and per-patient NPX. Re-model as OR per SD with incremental AUC over NEWS2. Re-fit the RNA-seq from counts (IL1RL1 isoforms, E-selectin, VCAM-1, IL-8). Blinded pathology re-classification with a second IL-33 reader. | **Go** if serum IL-33 (level, detectability or IL-33/sST2 ratio) tracks outcome independently of NEWS2. **No-go** if IL-33 is measurable and null, and sST2 loses significance once generic inflammation markers are added. (If IL-33 is undetectable, treat it as uninformative and let Gate 1 decide.) |
| **1a. In situ test** | Months 1–3 | RNA-seq of the 22 archived lung RNAs. Score the 454-gene AX-1177-reversible program (Table S4) by DAD and acute pneumonia. | **Go** if the score is higher in DAD/COVID lungs than in non-COVID pneumonia and controls, by a pre-specified effect (≥0.5 SD). |
| **1b. Pharmacology** | Months 1–4 | IC50 against reduced and oxidised IL-33 in ≥3-donor lung microvascular EC and bronchial epithelial ALI. Pre-incubation, concurrent and delayed addition. Readouts at 6 h and 24 h. | **No-go** if oxidised IL-33 is not neutralised (the differentiation claim fails). |
| **1c. Infection model** | Months 2–5 | Virus-infected epithelium → endothelium, ± AX-1177. Measure released IL-33, the program score, tissue factor/thrombomodulin, viral titre and ISGs. | **Go** if a pre-specified share (≥30%) of infection-induced endothelial activation is AX-1177-reversible **and** viral control is intact. |
| **2. Validation + in vivo** | Months 4–12 | External multi-virus cohort. Drug-tolerant IL-33 assays. Cross-reactivity → PK/PD → viral pneumonia efficacy model. | IND-enabling work only if an sST2/IL-33-axis marker replicates across viruses **and** in vivo efficacy is shown. |

The timings are planning estimates. The thresholds are proposals for the committee to fix before any data are unblinded.

---

## 7. What I considered and ruled out

| Considered | Outcome and reason |
|---|---|
| COVID-specific IL-33 up-regulation in lung | **Ruled out.** Not different at donor level under either labelling, and age-adjusted (ages balanced across groups). |
| Type-2 / eosinophilic mechanism | **Ruled out.** Tissue signal does not survive autopsy-based re-classification and is never COVID-specific; serum type-2 markers are flat; IL-5Rα duplex does not track EPX (rho 0.00) but tracks neutrophil elastase (0.76). |
| Pre-existing COPD/asthma as an IL-33-high repurposing signal | **Ruled out on our data.** No IL-33 or eosinophil difference by COPD, asthma or emphysema (small n). |
| Kidney indication from HGMEC | **Ruled out.** HGMEC reproduces the HUVEC program at ~0.67×; its unique hits are noise; no renal data. |
| Oncology from A549/MCF7 | **Ruled out.** These are antibody-only control lines; antibody-alone hits are at noise level. DMSO/PBS comparators are not valid controls for an antibody. |
| Agonism or off-target activity of AX-1177 | **Ruled out.** At background level in 4 cell types × 2 times; not reproducible. |
| Serum severity signature = IL-33 endothelial signature | **Ruled out.** Not enriched (Fisher p = 0.62); the most IL-33-specific outputs are flat. |
| sST2 as proof of IL-33 pathology | **Downgraded** to a prognostic/enrichment marker (decoy biology; non-specific). |
| Block-level post-mortem statistics | **Rejected.** Pseudo-replication: 3 donors supply 24 of 49 COVID blocks. Analysed per donor. |
| Taking E-selectin/VCAM-1/IL-8/IL1RL1 statistics at face value | **Rejected.** Impossible standard errors; fold-changes used descriptively only. |
| Ranking serum effects by OR per log unit | **Rejected.** Scale-dependent (CSF-1 OR 90); ranked by p instead. |
| Reading the 24 h partial blockade as weak antibody | **Not supported.** Most 24 h non-reversal is low power; true escape is concentrated in the interferon tier. Read as a timing issue. Potency is unknown (single saturating dose). |
| Reading the IL-33 "down" program as real biology | **Rejected.** It is mostly low-expression noise and not reversed in isotype-controlled comparisons (slope +0.2). Its apparent reversal against IL-33 alone is regression to the mean from the shared IL-33 group. |
| "6h"/"24h" sheets as separate timepoints, or truncated | **Checked.** Both hold all 24 contrasts, are identical and are not truncated. |
| IL-33 IHC as a patient-selection marker | **Rejected.** Constitutive, at the scale ceiling, requires tissue. |

---

## 8. Data integrity (details in Table S1; Fig. 4)

None of these issues overturns the conclusions above. Several block specific claims and must be fixed before any external use.

- **RNA-seq.**
  - 205 genes have invalid statistics (76 in all contrasts; 281 at a stricter threshold, with no change to conclusions), including IL1RL1 (ST2), E-selectin, VCAM-1, IL-8 and GAPDH.
  - The "6h"/"24h" sheets are mislabelled duplicates.
  - There is no HGMEC IL-33 contrast and no HGMEC vehicle arm.
  - The comparator is labelled both "Vehicle" and "Nontreated".
- **Serum.**
  - ~100 tested assays are missing from the file after multiplicity correction. IL-33 is among the panel assays not delivered.
  - "Log-transformed NPX" is ambiguous.
  - 26 duplicated proteins are unreconciled, though they agree well (r = 0.96).
- **Tissue.**
  - 8 of 31 labels conflict with the autopsy reports.
  - The IL-33 and eosinophil columns are hidden in the workbook.
  - IL-33 scores are two-sub-score averages that exceed the stated 0–5 scale; there is a single reader.
  - Blocks are pseudo-replicated.
  - The IL-5Rα duplex readout is not a valid eosinophil measure.
- **Design.**
  - Only reduced IL-33 was tested, at one antibody concentration, without pre-incubation, in single-donor cells.
  - There was no epithelial IL-33 stimulation.

---

## 9. How the analysis was done

- **RNA-seq.**
  - Integrity checks across all 26 contrasts:
    - AveExpr identity;
    - implied df from t→p (85.1 in every contrast);
    - BH reproduction;
    - logFC/t sign consistency;
    - implied SE = |logFC/t|.
  - Genes with implied SE > 3 in any contrast (205) were excluded from inference. Repeating everything with SE > 1.6 (281 genes) changes no headline number: inhibition stays 95%/73%, HGMEC concordance r = 0.87, serum enrichment p = 0.61.
  - Blockade was quantified against an isotype control (AX-1177+IL-33 vs isotype+IL-33) relative to IL-33 vs vehicle. These are independent groups, which avoids the regression-to-the-mean artefact that the shared IL-33 group creates.
  - Derived contrasts use exact linear combinations of logFC from the single fitted model. The background DE counts (e.g. DMSO vs PBS) use approximate SEs.
- **Serum.**
  - The delivered statistics were re-derived: Wald p reproduced exactly, and the BH denominator was inferred.
  - The 100 withheld tests were reconstructed from the step-down structure.
  - Olink names were mapped to genes to test enrichment of the IL-33 program (Fisher exact, unique proteins).
- **Tissue.**
  - Hidden columns and formula cells were parsed.
  - Text scores were converted (e.g. "2+" → 2).
  - Donor-level fields were forward-filled, and blocks averaged per donor.
  - Non-parametric donor-level tests were used (Kruskal–Wallis, Mann–Whitney, rank ANCOVA for age).
  - Sensitivity analysis used manual autopsy-based re-classification.

---

## 10. Output files

| File | Contents |
|---|---|
| `AX-1177_portfolio_audit_memo.md` / `.pdf` | This memo |
| `figures/Fig1_invitro_pharmacology.png` | Blockade, HGMEC concordance, specificity, kinetics, key genes |
| `figures/Fig2_postmortem_lung.png` | Donor-level IL-33, DAD, eosinophil re-classification, pseudo-replication, ceiling, label conflicts |
| `figures/Fig3_serum_proteomics.png` | Volcano, IL-33 program forest plot, withheld-assay reconstruction, cross-panel agreement |
| `figures/Fig4_data_integrity.png` | Implied-SE anomaly and integrity log |
| `AX-1177_supporting_tables.xlsx` | S1 integrity log · S2 donor table · S3 post-mortem stats · S4 454-gene IL-33 program · S5 all serum assays · S6 biomarker matrix · S7 invalid-statistics genes · S8 null calibration · S9 contrast QC · S10 gated plan |
| `code/` | Analysis and figure scripts |
