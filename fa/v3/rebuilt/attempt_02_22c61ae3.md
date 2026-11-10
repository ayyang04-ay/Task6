# AX-1177 (anti-IL-33 IgG1, research code Compound_47): portfolio audit position

**Basis.** This memo uses only the AX-1177 data delivery: the methods annex, mmc2 (serum proteomics, 100 hospitalised COVID-19 patients), mmc3 (post-mortem lung IHC, 31 donors, 74 blocks) and mmc4/mmc5 (in vitro RNA-seq contrasts, 26 contrasts × 26,210 genes). I recomputed every number here from those files; the scripts are in `code/`. The few places where I rely on general knowledge rather than our data are marked **[external]**.

---

## 0. Bottom line

**Recommendation: KEEP AX-1177, but only as a re-scoped, gated asset. Stop carrying it as a "viral LRTD" development programme.**

**Evidence scorecard**

| Evidence dimension | Rating | Basis (our data) |
|---|---|---|
| In vitro pharmacology (neutralisation, specificity) | **Strong but narrow** | ~100% reversal of well-expressed IL-33-responsive genes in HUVEC; reproduced in HGMEC; no activity alone in 4 cell types. Single donors, single dose, exogenous IL-33red only. |
| Human IL-33-pathway association | **Moderate** | sST2 #2 of 1,063 proteins (q = 0.0075, NEWS2-adjusted). One centre, n = 100, no replication, prognostic only. |
| Target present in diseased tissue | **Moderate** | IL-33 high in lung endothelium and basal epithelium of all 31 donors. Not disease-specific. |
| Causality (IL-33 drives progression) | **Absent** | IL-33 never measured in patients; IL-33 programme not enriched in the severity proteome; no in vivo data. |
| Support for "viral LRTD" breadth | **Absent** | One virus (SARS-CoV-2), hospitalised, pre-vaccination. |
| Data integrity | **Needs remediation** | Invalid statistics for key endothelial genes; 9/31 post-mortem labels discordant with autopsy text; undocumented assay exclusions (§3). |

| | |
|---|---|
| **What we keep** | An antibody that is clean and reproducible in vitro. It reverses IL-33-driven endothelial activation and shows no activity of its own. We also keep one credible human pathway signal: **soluble ST2 (sST2; the IL-33 receptor/decoy) is the #2 prognostic protein out of 1,063** for ICU admission, invasive ventilation (IMV) or death in hospitalised COVID-19, independent of NEWS2. |
| **What the data point at** | The data do not point at viral LRTD as a whole. They point at a **host-response indication: IL-33-driven endothelial activation in hospitalised pneumonia, selected by high sST2 rather than by pathogen.** Nothing in our data is specific to any virus. |
| **What is missing** | **We have no evidence that IL-33 is released in patients or drives progression.** IL-33 was never measured in any patient: the assay is absent from the delivered data. Tissue IL-33 does not separate COVID+ from COVID− lungs. The IL-33 endothelial programme is not over-represented among outcome-linked serum proteins. |
| **The gate** | About 6 months, low cost, no new patients. (1) Measure IL-33 in the 100 banked sera. (2) Re-analyse the archived RNA-seq counts per cell line. (3) Re-read the post-mortem IHC blinded, with adjudicated labels. Kill criteria are pre-specified (§5.4). If they are met, drop the asset; §6 states what we would be dropping. |
| **Do not** | Do not present the current package externally or use it for IND-enabling work. It has integrity defects that diligence would find (§3). |

---

## 1. The case for keeping: the strongest version the data allow

### 1.1 The molecule does what it was designed to do (Fig 1, Tables T1–T3)

All points below use the isotype-matched comparison: AX-1177 + IL-33red vs NIP228 isotype + IL-33red.

- **Near-complete reversal of the IL-33 programme in HUVEC.**
  - IL-33red changes 4,031 genes at 6 h and 1,836 at 24 h (BH adjusted p < 0.05).
  - AX-1177 significantly reverses 2,884 of the 6 h genes. Only 12 genes move further in the IL-33 direction.
  - Among well-expressed IL-33-responsive genes, the reversal slope is −0.94 (r = −0.97) at 6 h and −0.79 (r = −0.94) at 24 h.
  - Relative to the isotype arm, median inhibition for those genes is **100% at 6 h (IQR 94–104%) and 101% at 24 h (IQR 91–108%)**.
  - Including low-count genes, median inhibition is 92.5% (6 h) and 76% (24 h). Blockade at 24 h is incomplete for complement and interferon-stimulated genes: residual log2FC vs vehicle C3 +1.4, CXCL10 +2.4, IFIT1 +1.7, MX1 +0.9 (T2, T3).
- **The effect reproduces in a second endothelial type.** In glomerular microvascular cells (HGMEC), the AX-1177 reversal mirrors the HUVEC IL-33 programme at about half the amplitude (slope −0.54, r = −0.82, 6 h).
- **No activity on its own.**
  - AX-1177 alone vs isotype produced 21–73 "significant" genes per contrast across HUVEC, HGMEC, A549 and MCF7.
  - On inspection these are statistical artefacts (§3, item 2).
  - At most 3 of 260 robust IL-33 signature genes moved in any of the 16 antibody-alone contrasts.
  - There is no detectable off-target transcriptional footprint and no sign of agonism.

### 1.2 In patients, the IL-33 pathway is among the strongest prognostic signals (Fig 2)

- **sST2 ranks 2nd of 1,094 assays (1,063 proteins)** for the 30-day composite of ICU, IMV or death (100 patients; 44 events, inferred from mmc2).
  - OR 3.02 (95% CI 1.83–5.01) per log unit; p = 1.7×10⁻⁵; BH adjusted q = 0.0075.
  - The model adjusts for age, sex and NEWS2 at enrolment, so the association is independent of bedside severity. Incremental discrimination (AUC) cannot be computed from the summary data delivered.
  - It ranks above IL-6 (#11; OR 2.14; q = 0.012).
- **The proteomic data are technically sound.** Proteins measured on more than one panel give concordant associations: Spearman ρ = 0.99 over 36 duplicate-assay pairs. IL-6 on four panels gives ORs of 2.07–2.31.

### 1.3 The target is present where the disease is (Fig 3)

- IL-33 immunoreactivity is high in lung endothelium and in bronchial/bronchiolar basal epithelium in essentially every donor. Endothelial scores are ≥ 4.25 in 70 of 74 blocks.
- Endothelial IL-33 is **lower in lungs whose autopsy text records acute pneumonia**: −0.37 units (95% CI −0.64 to −0.10), p = 0.007, donor level, age-adjusted. It also falls as neutrophil elastase rises (age-adjusted partial ρ = −0.43, p = 0.015).
- This fits IL-33 being released from endothelial nuclei during acute lung inflammation, which is the mechanism AX-1177 would block. It is *consistent with* release, not proof of it, and it is fragile (§3, item 8).

### 1.4 The biology fits severe-pneumonia pathology (Table T3)

In HUVEC, IL-33red switches on a programme that AX-1177 reverses. For each group below, the first value is the 6 h IL-33 effect (log2FC) and the second is the 6 h AX-1177 reversal vs isotype (log2FC):

| Process | Genes: IL-33 effect → AX-1177 reversal |
|---|---|
| Neutrophil recruitment and granulopoiesis | CXCL2 +6.8 → −6.7; CXCL3 +8.3 → −8.4; CXCL5 +5.3 → −5.8; CXCL6 +9.4 → −8.1; CSF3/G-CSF +8.3 → −8.3; CSF2/GM-CSF +10.3 → −12.2 |
| Adhesion | CX3CL1 +8.4 → −8.7; E-selectin, VCAM-1 and ICAM-1 rise ~60- to ~2,300-fold by point estimate (see §3 on their p values) |
| Pro-coagulant, anti-fibrinolytic switch | Tissue factor F3 +5.6 (~50-fold) → −5.5; thrombomodulin THBD −1.0 → +0.9; PAI-1 SERPINE1 +1.7 → −1.8 |
| Complement | C3 +4.8 → −4.6; CFB, C1R and C1S follow the same pattern |
| Inflammatory cytokine | IL-6 +5.8 → −6.0 |

In our own autopsies:
- 4 of 16 COVID+ reports record pulmonary thrombo-emboli.
- Neutrophil elastase scores are higher in pneumonic lungs: donor-level Kruskal–Wallis across the three labelled groups p = 0.023; pneumonia vs non-pneumonia p = 0.007.

This is a coherent mechanistic story, not evidence of causality.

### 1.5 The decisive experiments are cheap because we already own the material

- Sera from all 100 patients are stored at −80 °C (annex §6).
- RNA has already been extracted from post-mortem blocks (the "Tissue RNA" IDs in mmc3).
- The RNA-seq count matrices and fitted model are archived (annex §5).
- The biologics file with affinity and potency exists (annex §1).

Gate A therefore needs no new patients and no animals. A partner or acquirer would ask for the same data.

---

## 2. The case against continuing as is

| What would have to be true for "viral LRTD" | What our data show |
|---|---|
| IL-33 is elevated or released in patients who progress | **Not measured.** The Olink Inflammation panel run includes an IL-33 assay [external: panel content], but IL-33 is missing from the delivery, together with 14 other low-abundance analytes (TSLP, IL-4, IL-5, IL-13, IL-1α, IL-2, …). The two undocumented per-group columns in mmc2 never exceed 9%, which fits an undocumented missingness / limit-of-detection filter. IL-33 was most likely undetectable. |
| IL-33 is higher in diseased lung | **No.** Donor-level, COVID+ vs COVID− pneumonia: basal epithelium 4.25 vs 4.50 (p = 0.92); endothelium 4.81 vs 5.50 (p = 0.16, trending *lower* in COVID+). |
| The IL-33 endothelial programme tracks with outcome in patients | **No.** 34% of all measured proteins are risk-associated (p < 0.05). Proteins encoded by IL-33-induced HUVEC genes are risk-associated at the background rate: 6 h, 26/75 = 34.7% vs 36.7%, OR 0.92, p = 0.80; 24 h, 22% vs 37%, OR 0.48, p = 0.048. Individual overlaps (IL-6, CCL20, OPG) are what chance alone would produce. |
| sST2 reflects IL-33 activity specifically | **Not shown.** sST2 is a decoy receptor and a generic severity marker. In HUVEC the IL1RL1 transcript rises +1.6 log2 with IL-33 and AX-1177 reverses it. HGMEC shows no reversal (+0.2), and IL1RL1's delivered standard errors are invalid in every contrast. |
| The effect is general to viral LRTD | **No data.** The only human outcome data come from one virus (SARS-CoV-2), one centre, hospitalised pre-vaccination patients. There are no RSV, influenza, outpatient or paediatric data. |
| Blockade helps in a disease-relevant system | **Not tested.** No virus appears in any experiment. IL-33red is added exogenously at 30 ng/mL to single-donor cells. There are no lung microvascular cells, no primary airway epithelium, no dose–response, no pre-incubation, no IL-33ox arm and no in vivo work. |

---

## 3. Integrity findings to resolve before anyone quotes these data

Each of these changes what can be claimed.

| # | Issue | Evidence | Consequence | Fix |
|---|---|---|---|---|
| 1 | **Invalid standard errors for the most important endothelial genes** | One voom/limma model fitted across 4 very different cell types (annex §5). 274 genes have SEs more than 5× what their expression level predicts. Examples: **E-selectin log2FC +11.2 but q = 0.50 (SE 8.9 log2 units); VCAM-1 +8.7, q = 0.51; IL-8 +8.2, q = 0.19; CXCL1 +8.2, SE 1,155; MCP-1 +4.2, q = 0.77; PTX3 q = 0.98; IL1RL1 (ST2) q = 0.98.** VWF, CDH5 and GAPDH are also affected (Fig 4A, T4). | Read as delivered, the tables would say IL-33 does *not* induce E-selectin, VCAM-1, IL-8 or MCP-1. That is almost certainly wrong: the effects are huge and AX-1177 reverses them. Until re-analysed, these genes have effect sizes only. | Re-fit per cell line from the archived counts; run sample-level QC (PCA, library swaps) |
| 2 | **Spurious significance** in antibody-alone contrasts | AKR1C2 in A549 at 24 h: log2FC +0.06 to +0.17 (4–12%) with t = 61–169 (q down to 10⁻⁹⁴). The other "hits" are near-zero-count lncRNAs and pseudogenes (Fig 4B). | The 21–73 antibody-alone "DEGs" must not be reported as off-target effects. | Same as #1 |
| 3 | Gaps in the in vitro design | No HGMEC vehicle arm, so there is no IL-33 effect estimate in HGMEC. A549 and MCF7 were never given IL-33, so the epithelial arms say nothing about IL-33 biology. MCF7 is breast carcinoma. A DMSO vehicle was used for an antibody. Endothelial cells come from one donor each, so "n = 3 biological replicates" are culture replicates. Single doses only; concurrent addition. | Pharmacology only: no potency, no generalisability, no epithelial data. | Redesign (§5.4) |
| 4 | Isotype partly dampens the IL-33 response at 24 h | IL-33 + isotype vs IL-33 alone: ~5–20% lower response for top genes (e.g., C3 6.1 vs 5.8; IL-6 2.8 vs 2.3; CXCL2 3.3 vs 2.7 log2). | "AX-1177 + IL-33 vs IL-33 alone" contrasts (also delivered) overstate the specific effect. | Quote isotype-matched contrasts only (as here) |
| 5 | Presentation hazard in the delivered file | Both mmc5 sheets ("6h", "24h") contain the same 24 contrasts (12 per timepoint), with identical values. An active filter shows only the HUVEC isotype contrast in each sheet. | A reader of mmc5 sees 1 of 24 contrasts and none of HGMEC. | Re-issue the file |
| 6 | Undocumented proteomics processing | IL-33 and 14 other assays dropped with no stated rule. 27 proteins sit on 2–4 panels (1,094 assays = 1,063 proteins). Two undocumented columns appear; their values are multiples of 1/56 and 1/44, consistent with per-group missingness and implying 44 events. ORs are per "log unit", so magnitudes are not comparable across assays (e.g., CSF-1 OR 90). No adjustment for renal function. | Rankings rest on p values, not ORs. IL-33 cannot be assessed. | Document QC; report per-SD ORs; add eGFR |
| 7 | **Post-mortem labels contradict the autopsy text** | 9 of 31 donors discordant. 4/10 "COVID-neg pneumonia" donors have no pneumonia in their report. 3/5 "non-pneumonia" controls have acute pneumonia/pneumonitis or pulmonary coccidioidomycosis. 2/16 COVID+ donors have no acute pneumonia, including donor 2067, who contributes 8 blocks. SARS-CoV-2 status is missing for donor 1905. | Any group comparison as labelled is unreliable. | Pathologist adjudication |
| 8 | Post-mortem scoring and replication | Scores were recoded "n+" → n + 0.5, so values reach 5.5 on a documented 0–5 scale. Endothelial IL-33 sits at the 5.5 ceiling in 53% of blocks. One unblinded reader. 74 blocks from 31 donors; 3 donors supply 24 of 49 COVID+ blocks. | Block-level statistics are pseudo-replicated. Ceiling effects hide differences. The pneumonia association weakens in a donor-random-effect model (p = 0.13). | Blinded 2-reader re-score on the raw scale; donor-level analysis |

---

## 4. Which indication do our data actually point at?

**Answer: hospitalised pneumonia with endothelial activation, defined by host response (high sST2) and not by pathogen. This is the pre-ICU window, where the composite endpoint (ICU, IMV or death within 30 days) is decided.**

The reasoning, all from our data:

1. **Mechanism.** The mechanism lives in the endothelium and is pathogen-agnostic. It shows as IL-33 → NF-κB → neutrophil chemokines, G-CSF/GM-CSF, adhesion molecules, pro-coagulant switch and complement. It appears in two endothelial beds. No virus is involved anywhere in the in vitro work.
2. **Population.** The clinical signal is in **hospitalised** patients, and sST2 predicts progression **beyond NEWS2**. That defines a population selected by severity and host response, not "viral LRTD" broadly (which would include mild and outpatient disease).
3. **Tissue.** The tissue signal, such as it is, follows **acute pneumonia of any cause**. Adjusted for pneumonia, COVID status adds nothing (p = 0.12). Endothelial IL-33 medians: COVID− lungs with acute pneumonia 4.88, COVID+ lungs with acute pneumonia 4.69, non-pneumonic lungs 5.50.
4. **Type-2 disease.** The data do **not** point at a type-2 airway indication. Serum IL-5Rα, eotaxin-1/CCL11, CCL24, CCL17 and IL-5 are unrelated to outcome (q = 0.17–1.0). Tissue IL-33 is unrelated to eosinophil granule markers (EPX, EDN, MBP: |ρ| ≤ 0.2) or to recorded COPD or asthma (p = 0.21–0.88).

**Honest limits.** The pathogen-agnostic reading is a hypothesis. Our only outcome data are in SARS-CoV-2, and the tissue evidence rests on 31 elderly donors. The re-scope widens the pathogen range and narrows the population. It is not a new therapeutic area. No non-respiratory indication has any support in our data (§7).

---

## 5. Forward view: what the next studies must establish, biomarkers, sampling, plan

### 5.1 What the next studies must establish (in order of decision value)

1. **IL-33 is released in the target population and carries information.** Measurable IL-33 (total and IL-33:sST2 complex; free and reduced IL-33 where pre-analytics allow) must be higher in progressors than non-progressors at admission. It must add to NEWS2 and sST2, or else sST2 must stay prognostic after adjusting for eGFR and IL-6.
2. **The in vitro neutralisation claims survive correct statistics.** After per-cell-line re-analysis, E-selectin, VCAM-1, ICAM-1, IL-8, MCP-1, tissue factor, IL-6 and CCL20 must be significantly induced by IL-33 and reversed by AX-1177.
3. **Endogenous IL-33 at realistic concentrations drives lung-relevant endothelium, and AX-1177 blocks it.** This means primary lung microvascular endothelium (≥ 3 donors) exposed to IL-33 released by virus-infected or damaged primary airway epithelium, not 30 ng/mL of recombinant protein. It also needs a potency curve (IC50/IC90), pre-incubation vs concurrent addition, and **both IL-33red and IL-33ox**, because the antibody's dual-form binding is untested in our data.
4. **The effect is pathogen-agnostic.** Show it with influenza, RSV and SARS-CoV-2, plus a bacterial stimulus. This supports the re-scoped label.
5. **No loss of antiviral control.** IL-33 induced interferon-stimulated genes in HUVEC (MX1, IFIT1, CXCL10), and AX-1177 only partly blocked them at 24 h. Viral replication must therefore be measured alongside efficacy.
6. **In vivo proof of mechanism.** In a viral-pneumonia model, blockade must reduce vascular leak, neutrophil influx or coagulopathy, with the PD markers below moving. Species cross-reactivity must be checked in the biologics file first.
7. **Corrected tissue evidence.** With adjudicated labels and blinded scoring, loss of nuclear endothelial IL-33 and endothelial ST2 expression must associate with acute lung injury.

### 5.2 Biomarkers: evidence and role in patients

| Marker (matrix) | Evidence in our data | Role in patients | Ready for patients? |
|---|---|---|---|
| **sST2** (serum/plasma) | #2 of 1,063 proteins; OR 3.02 (1.83–5.01); q = 0.0075; independent of NEWS2 | **Prognostic enrichment / stratification** at baseline, to enrich for progressors and raise event rates. Exploratory PD only. | **Yes**, as stratification or enrichment. The threshold must be set in an independent cohort. [external] Clinical-grade sST2 immunoassays exist. |
| **IL-33**: total, free, reduced/oxidised, IL-33:sST2 complex (EDTA plasma) | Not in our data | **Target engagement** (free IL-33 falls, total/complexed rises on drug) and candidate **predictive** marker for selection | **No.** Assay and pre-analytics are needed first; this is Gate A. |
| **IL-6** | Risk on 4 panels (OR 2.07–2.31, q ≤ 0.019). IL-33-induced +5.8 log2; AX-1177 reverses it fully in HUVEC (residual −0.1) and by −2.9 log2 in HGMEC. | Prognostic covariate; exploratory PD. Record concomitant IL-6 pathway blockade. | Yes (routine assay), but non-specific |
| **CCL20** | OR 1.83, q = 0.020. IL-33-induced +9.2 (6 h) and +5.6 (24 h) log2, reversed in both endothelial types. | **Exploratory PD** (endothelial IL-33 response panel) | After Gate A/B |
| **OPG (TNFRSF11B)** | OR 6.77 and 4.40 on two panels (q 0.014, 0.020). +4.8 log2, reversed. | Exploratory PD | After Gate A/B |
| **sIL-18R1** | OR 6.07, q = 0.018. +3.6 log2, reversed. | Exploratory PD | After Gate A/B |
| **CCL7/MCP-3** | OR 1.72, q = 0.020. 6 h only; low-count gene. | Exploratory PD (weaker) | After Gate B |
| **sE-selectin, ICAM-1, VCAM-1, IL-8, MCP-1** | Largest IL-33 effects, but delivered p values invalid. Serum E-selectin OR 2.08 (q = 0.09), IL-8 2.23 (q = 0.023); ICAM-1 and VCAM-1 n.s. | PD candidates *only if* the re-analysis confirms them | Not yet |
| **PTX3, HGF, vWF, ANGPT2** | Outcome-associated (q 0.004–0.052). vWF and ANGPT2 are **not** moved by IL-33 in vitro; PTX3's in vitro p value is invalid. | Disease-severity / prognostic covariates, **not PD** | Yes, as covariates |
| **Viral load** (qPCR) | Indirect: partial ISG escape at 24 h | **Safety** | Yes |
| Tissue IL-33 IHC; in vitro transcript signatures | No COVID discrimination; ceiling effects | None in patients: discovery and translational tools only | No |

**Specificity caveat.** No PD marker in our data has been shown to be IL-33-*selective*. TNF and IL-1 also induce CCL20, IL-6 and OPG. Gate B must include TNF, IL-1β and virus-conditioned stimuli, with and without AX-1177, to find which markers move only when IL-33 is blocked.

### 5.3 Sampling timepoint

**Primary: at enrolment (hospital admission), before the first dose, within 48 h of admission.** Record days since symptom onset and any prior corticosteroid, IL-6 pathway or JAK-inhibitor exposure.

Why this timepoint:
1. It is the only timepoint at which our data link a biomarker (sST2) to outcome.
2. The IL-33 endothelial response is early and transient in vitro: 4,031 genes at 6 h vs 1,836 at 24 h. IL-33 effects from 6 h to 24 h: TNF +7.9 → −0.1; tissue factor +5.6 → +1.2; IL-6 +5.8 → +2.8 log2. The biology and the treatment window are both early.
3. Later samples are confounded by escalation of care.

**Secondary (PD): 24 h after the first dose, then day 3–5 and day 7.**
- At 24 h, IL-33-driven products are still raised in vitro (CCL20 +5.6, CSF2 +8.1, IL-6 +2.8 log2), and AX-1177 still suppresses them (CCL20 −5.3, IL-6 −2.4). Suppression should therefore be visible if IL-33 is driving the patient's disease.
- Day 3–5 captures slower markers (OPG, sST2).

**Pre-analytics.** Collect EDTA plasma on ice, processed within 1 h, alongside serum. The existing sera were clotted (annex §6), so **[external]** labile reduced IL-33 will probably have oxidised. Banked sera can support total and complexed IL-33 measurement, not form-specific measurement.

**In vitro and ex vivo follow-up:** 6 h is the primary readout (peak response), with 24 h secondary to capture durability and the partial escape of complement and ISGs.

### 5.4 Plan and gates

| Phase | Work (material) | Decision criterion |
|---|---|---|
| **Gate A (0–6 months; existing material)** | (a) Per-cell-line re-analysis of archived counts with sample QC. (b) Retrieve affinity, potency and cross-reactivity from the biologics file. (c) Validated high-sensitivity IL-33 assay (total, IL-33:sST2) on the 100 banked sera; re-fit logistic models with IL-33, sST2, IL-6 and eGFR; report per-SD ORs and discrimination beyond NEWS2. (d) Blinded 2-reader IHC re-score on the raw 0–5 scale, pathologist-adjudicated labels, donor-level models, ST2 IHC; score IL-33-endothelial genes in the existing tissue RNA. | **Kill** if **any** of the following. (i) The human pathway signal fails: IL-33, where measurable, shows no association with progression **and** sST2 loses significance after eGFR/IL-6 adjustment. (ii) Re-analysis fails to confirm AX-1177 reversal of the core endothelial panel. (iii) Potency is incompatible with a feasible clinical dose. **Go** if IL-33 (or the IL-33:sST2 complex) associates with progression, or sST2 stays independently prognostic, *and* the pharmacology is confirmed. **Downgrade** (enrichment rationale only; no further spend until Gate B shows dependence on endogenous IL-33) if IL-33 is reliably measurable but clearly unrelated to progression while sST2 survives. |
| **Gate B (6–12 months)** | Primary lung microvascular endothelium (≥ 3 donors) × primary airway epithelium (ALI) infected with influenza, RSV or SARS-CoV-2, plus a bacterial stimulus. AX-1177 vs isotype; dose–response; pre-incubation; IL-33red and IL-33ox arms; readouts at 6 and 24 h (activation panel, TEER, neutrophil adhesion, tissue factor, viral replication). In parallel, a **prospective multi-pathogen hospitalised-pneumonia cohort** in the post-vaccination era with admission EDTA plasma. | Go if AX-1177 reduces activation driven by **endogenous** IL-33 by ≥ 50% on the core panel without raising viral replication, and the sST2 (± IL-33) association replicates outside COVID-19. |
| **Gate C (12–18 months)** | In vivo viral-pneumonia model (cross-reactive antibody or surrogate): vascular leak, neutrophil influx, coagulation, survival, PD panel. Then a Phase 1b/2a proof-of-mechanism in sST2-high hospitalised pneumonia with PD and safety endpoints (viral load, secondary infection). | Standard development gates |

---

## 6. If the committee drops it: what we are dropping and why

**What we would be dropping:**
- A well-behaved anti-IL-33 IgG1 that reverses the IL-33-induced endothelial programme essentially completely in vitro, with no transcriptional activity of its own.
- An **untested** hypothesis: that IL-33 released in acute lung inflammation drives the endothelial activation, neutrophil recruitment and coagulopathy that take hospitalised pneumonia patients to ICU, IMV or death.
- The one human signal in support: sST2 as a top prognostic marker.

**Why dropping would be defensible:**
- Our data establish pharmacology and prognostic association, **not causality**.
- IL-33 itself was never measured in patients.
- The IL-33 programme is not over-represented in the severity proteome.
- Tissue IL-33 is not disease-specific.
- The only outcome data are single-centre, pre-vaccination COVID-19, and the "viral LRTD" framing has no data behind it.
- The package has integrity defects that would need rework in any scenario.

**What we would *not* be dropping:** any evidence of safety liability. There is none in our data either way; no in vivo or toxicology data were delivered.

---

## 7. Considered and ruled out

### 7.1 Indications

| Indication | Verdict | Reason from our data |
|---|---|---|
| **Viral LRTD (broad, current framing)** | Ruled out as framed | Only SARS-CoV-2; only hospitalised, pre-vaccination; no RSV, influenza, outpatient or paediatric data. Nothing virus-specific in mechanism or tissue. |
| **COVID-19-specific** | Ruled out | Tissue IL-33 does not separate COVID+ from COVID− pneumonia. The pre-vaccination population no longer represents current disease. |
| **COPD / asthma (type-2 airway)** | Not supported by *our* data | No airway-disease cohort. Tissue IL-33 unrelated to COPD or asthma notes (p = 0.21–0.88) or eosinophil markers (\|ρ\| ≤ 0.2). Serum type-2 markers unrelated to outcome. Epithelial IL-33 biology was never tested: A549 and MCF7 got no IL-33. [external] The literature rationale is not ours to claim. |
| **Kidney (glomerular endothelium)** | Ruled out | HGMEC responds at about half the HUVEC amplitude and transiently (24 h slope −0.14). No HGMEC vehicle; no renal clinical data. |
| **Cardiovascular / heart failure** (sST2 is a cardiac marker) | Ruled out | No cardiac cohort; NT-proBNP only weakly associated (OR 1.2–1.24, q > 0.1). |
| **Sepsis / non-pneumonic ARDS** | Plausible extension, unsupported now | The mechanism is pathogen-agnostic, but we have no data outside pneumonia. |
| **Oncology** (A549/MCF7 in the package) | Ruled out | The antibody is inert in both lines, and no IL-33 biology was tested. |

### 7.2 Analyses and claims

- **Trusting the delivered p values for SELE, VCAM1, CXCL8, CCL2, CXCL1, PTX3 and IL1RL1.** Ruled out because the SEs are invalid (§3 #1). Effect sizes only.
- **Treating antibody-alone "DEGs" as off-target biology.** Ruled out as artefacts.
- **Using "AX-1177 + IL-33 vs IL-33 alone" as the efficacy contrast.** Ruled out because the isotype itself dampens the response at 24 h.
- **Using the DMSO contrasts.** Ruled out: DMSO is an irrelevant vehicle for an antibody.
- **Block-level post-mortem statistics.** Ruled out as pseudo-replication. Donor-level means, plus a donor-random-effect sensitivity model, are used instead.
- **Comparing groups on the delivered labels alone.** Replaced by a sensitivity analysis on autopsy-text classification; this reading is mine and needs pathologist adjudication.
- **Ranking serum markers by OR magnitude.** Ruled out: per-log-unit ORs are scale-dependent.
- **Reading individual overlaps (IL-6, CCL20, OPG) as a translational bridge.** Ruled out by the enrichment test (no over-representation).
- **Claiming AX-1177 blocks both IL-33 forms.** Not testable here: there is no IL-33ox arm.
- **Things I could not do with the delivery:**
  - re-fit the RNA-seq (counts not delivered);
  - patient-level models, AUC/NRI or sST2 cut-offs (only summary statistics delivered);
  - potency or dose reasoning (biologics file not delivered);
  - replication (no second cohort).

---

## 8. Anticipated challenges and answers

- **"sST2 goes up in everything. Why is that IL-33 evidence?"** It is not proof of IL-33 causality. It is the strongest IL-33-pathway signal in an unbiased 1,063-protein screen and is independent of NEWS2. We propose it for *prognostic enrichment*, which is valid whatever the mechanism, and Gate A tests whether IL-33 itself carries information.
- **"You never measured IL-33."** Correct, and that is Gate A. The sera exist. Pre-analytics limit us to total and complexed IL-33 in the banked sera; prospective EDTA plasma is specified for free and reduced IL-33.
- **"HUVEC with 30 ng/mL recombinant IL-33 is artificial."** Agreed. It shows pharmacology, not disease relevance. Gate B replaces it with endogenous IL-33 from infected primary epithelium acting on lung microvascular cells.
- **"The tissue data show nothing."** They show the target is abundant and not COVID-specific, which is why we re-scope away from COVID and viral LRTD. The suggestion of IL-33 release in pneumonia is weak and is re-tested blinded.
- **"Why not drop now?"** Gate A uses material we already own, answers the single most important unknown, and is what any partner would require. The kill criteria are explicit, so keeping is cheap and reversible.
- **"Can we show the current data externally?"** Not before the §3 fixes. The delivered RNA-seq statistics would mislead on the key endothelial genes, and the post-mortem labels contradict the autopsy reports.

---

## Appendix A. Re-analysis methods (summary)

- **Transcriptomics (mmc4, mmc5).**
  - Parsed all 26 contrasts (2 in mmc4; 24 in mmc5, duplicated across both sheets). Gene set and AveExpr are identical across contrasts, consistent with one fit.
  - Implied SE = |logFC/t|, compared with the rolling median at matched AveExpr. Flagged genes have SE > 5× expected.
  - Neutralisation metrics use isotype-matched contrasts. Derived arm differences (e.g., AX-1177 + IL-33 vs vehicle) come from additivity of group-mean contrasts in one linear model.
  - HGMEC has no vehicle, so its IL-33 amplitude is estimated from the reversal contrast against the HUVEC IL-33 effect.
- **Serum proteomics (mmc2).**
  - Olink assay names were mapped to HGNC symbols (manual dictionary in `code/`); duplicates were collapsed for protein-level counts.
  - Translational bridge: Fisher's exact test of risk association (OR > 1, p < 0.05) among proteins whose transcripts are IL-33-induced in HUVEC, vs all other proteins with a matched transcript (915). Sensitivity definitions are in T6.
- **Post-mortem (mmc3).**
  - "n+" coding decoded (numeric = n + 0.5).
  - Donor-level means; donor fields propagated from the first block and notes pooled across blocks.
  - Age-adjusted OLS with HC3 SEs; a block-level mixed model with donor random intercept as sensitivity.
  - Autopsy-text classification of acute pneumonia is tabulated per donor (T8) for adjudication.

## Appendix B. Files

- `figures/`
  - `Fig1_invitro_pharmacology.png`
  - `Fig2_serum_proteomics.png`
  - `Fig3_postmortem_IHC.png`
  - `Fig4_transcriptomics_integrity.png`
- `tables/`
  - `T1` contrast summary
  - `T2` neutralisation metrics
  - `T3` key endothelial genes (6/24 h, HUVEC/HGMEC, derived residuals, SE validity)
  - `T4` 274 genes with invalid SEs
  - `T5` serum proteins with IL-33-responsive transcripts (PD candidate screen)
  - `T6` enrichment tests
  - `T7` all Olink assays with gene mapping
  - `T8` post-mortem donor-level table with label/autopsy-text discordance
  - `T9` every post-mortem statistic quoted in this memo
- `code/`: `run_all.sh` regenerates everything from the raw delivery.
  - `xlsx2tsv.py`: streaming xlsx parser
  - `01_prepare_data.py`
  - `make_tables.py`
  - `fig1`–`fig4` scripts
  - `build_pdf.py`
  - helpers `olink_map.py` (Olink → HGNC mapping) and `load_mmc3.py` (IHC decoding plus the autopsy-text classification)
