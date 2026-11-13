# AX-1177 (anti-IL-33 mAb): portfolio audit position

**For:** Respiratory portfolio audit committee

**Basis:** The five AX-1177 files delivered: the methods annex, the HUVEC IL-33 RNA-seq, all other RNA-seq contrasts, the serum proteomics and the post-mortem lung data. Every number below was re-derived from those files.

**Supporting material:** `AX-1177_audit_supporting_tables.xlsx` (11 sheets), `figures/` (Figs 1–6) and `scripts/` (full re-analysis; `run_all.sh` reproduces all outputs from the raw files).

---

## 1. Recommendation

### KEEP, but re-scoped and stage-gated. Do not continue on the current path.

**Stop** spending against *"severe lower respiratory viral infection"* as an all-comers indication. Our data do not show that IL-33 drives severity:
- The target itself was never reported in patient serum.
- Lung IL-33 is not increased in COVID-19.
- The classical downstream IL-33 (type-2) axis is flat in patients.

**Keep** the asset, because three things are true, and each is in our data:
1. **The molecule works and is clean.** It completely neutralises the endothelial IL-33 programme against an isotype-matched control, and it shows no transcriptional activity of its own in four cell types.
2. **Our own patients carry an IL-33-axis prognostic signal.** Soluble ST2 (sST2), the IL-33 decoy receptor, ranks #2 of 1,063 serum proteins for association with ICU, ventilation or death, after adjustment for NEWS2.
3. **The decisive missing evidence is mostly already in our archive.** Three items can be obtained in weeks, not years:
   - The undelivered Olink assays, very probably including IL-33 itself.
   - The RNA-seq count matrix.
   - 22 banked post-mortem lung RNAs.

**Decision gate at about 6 months, with kill criteria agreed now** (§5.3). Only a biomarker-enriched Phase 1b/2a would follow a pass. If the gates fail we drop the asset, and the drop statement is already written (§6).

*Confidence:* high that the current thesis is under-supported. Whether the re-scoped thesis survives the gates is genuinely uncertain, which is why the gates are cheap and the kill criteria are agreed in advance. This is an option-value decision, not an efficacy claim.

### Evidence scorecard

| Question | What our data say | Confidence |
|---|---|---|
| Does AX-1177 neutralise IL-33? | **Yes, completely.** 0–1% of the IL-33 response remains vs 86–101% with isotype. Shown for reduced IL-33 in endothelium, at one concentration. | High |
| Is it clean (no agonism or off-target activity)? | **Yes.** No coherent transcriptional effect of the antibody alone in HUVEC, HGMEC, A549 or MCF7. | High |
| Is the IL-33 axis linked to severe outcome? | **The receptor/decoy is (sST2, #2 of 1,063); IL-33 itself is absent from the delivery.** | Moderate |
| Is lung IL-33 increased in COVID-19? | **No.** It is constitutive, at the scale ceiling in controls, and numerically lower in COVID+ lungs. | Moderate |
| Does the type-2/eosinophil axis track severity? | **No.** IL-5 OR 1.00; eotaxins 0.92–1.08; tryptase 1.07. | High |
| Does IL-33 drive severity? | **Not shown.** | — |
| Is oxidised-IL-33 activity (the presumed differentiator) supported? | **Untested.** Only reduced IL-33 was used. | — |

---

## 2. What our data show

### 2.1 Pharmacology: in vitro RNA-seq (HUVEC, HGMEC, A549, MCF7; 6 h and 24 h; n=3/arm) — Figs 1, 2

- **IL-33 triggers a large, canonical NF-κB inflammatory programme in HUVEC.**
  - 4,031 DE genes at 6 h and 1,836 at 24 h (q<0.05).
  - Top genes: NFKBIA, RIPK2, TNFAIP3, TRAF1, RELB and IRAK2.
  - Secreted outputs include GM-CSF (CSF2), G-CSF (CSF3), CXCL6, CCL20, IL-6, tissue factor (F3) and OPG (TNFRSF11B).
  - The response is larger at 6 h than at 24 h and partly transient (46% as many DE genes at 24 h).
- **AX-1177 fully neutralises it**, using the isotype-matched comparator (IL-33 + IC119).
  - On robust IL-33-induced genes (n=195 at 6 h, n=41 at 24 h), a median 0% of the IL-33 response remains with AX-1177 (IQR −4 to +4%). With isotype, 101% remains (98–103%).
  - At 24 h the figures are 1% vs 86%.
  - Across all IL-33-responsive genes, the reversal mirrors the response (r = −0.80 at 6 h; −0.65 at 24 h).
  - This holds even though the antibody was added concurrently, without pre-incubation.
- **The microvascular line (HGMEC) also responds and is reversed**: 1,460 DE genes in the AX-1177 reversal contrast at 6 h and 269 at 24 h. On robust genes the reversal is about 61% (6 h) and 31% (24 h) of the HUVEC magnitude. Because HGMEC has no vehicle arm, its % neutralisation cannot be computed.
- **No agonism and no off-target activity.**
  - AX-1177 alone vs isotype gave 21–73 nominal hits per contrast. Nearly all are low-count lncRNA/pseudogene noise or trivially small fold-changes.
  - After filtering, 0–12 remain per contrast, none pathway-coherent.
  - The p-value distributions are near-null (estimated null fraction 0.90–1.00).
  - The antibody-alone profile is uncorrelated with the IL-33 programme (r = 0.005).
- **Not tested:**
  - Oxidised IL-33.
  - Potency: only one concentration was used (10 µg/mL ≈ 41-fold molar excess over 30 ng/mL IL-33), with no dose–response.
  - Epithelial IL-33 responses: A549 and MCF7 never received IL-33.
  - Lung-derived endothelium.
  - Immune cells.

### 2.2 Patients: serum Olink (100 hospitalised COVID-19, single centre, pre-vaccination) — Fig 3

The endpoint was ICU, invasive ventilation or death within 30 days: 44 events (inferred from the 56/44 group denominators). Models were adjusted for age, sex and NEWS2.

- **sST2 (IL1RL1) ranks #2 of 1,063 proteins:** OR 3.02 (95% CI 1.83–5.01) per log unit, p = 1.7×10⁻⁵, q = 0.0075.
  - NT-proBNP is only weakly associated (OR 1.20–1.24, q ≥ 0.15). So sST2 is unlikely to be merely a cardiac-stretch signal.
- **Other IL-1-family receptors also track severity:** IL-18R1 OR 6.07 (q=0.018), IL-1R2 4.52 (q=0.018), IL-1β 2.45 (q=0.046).
- **Severity is a broad signature: 169 proteins at q<0.05** (178 assays, because some proteins are measured on more than one panel). It is led by:
  - HGF (#1), IL-6 (four panels, concordant OR 2.07–2.31), PTX3, OSM and OPG.
  - Neutrophil activation: CLEC5A, PRTN3, CD177 and IL-8.
  - Endothelial/coagulation markers at or near the threshold: uPAR (q=0.025), vWF (q=0.050), tissue factor (q=0.051) and ANGPT2 (q=0.052).
- **The classical downstream type-2 IL-33 axis is flat:** IL-5 OR 1.00; eotaxin-1 0.98–1.08; eotaxin-2 0.92; CCL17 0.85; CCL13 0.86; tryptase 1.07; KIT 1.05. ECP is borderline (1.50, q=0.06).
- **IL-33 itself is not in the delivery.**
  - BH adjustment was computed over 1,194 assays, but only 1,094 were delivered.
  - 102 of the 1,196 panel assays are absent from the delivery, including IL-33, IL-4, IL-13, TSLP and IL-5 (Inflammation panel). The BH denominator shows that 100 of the absent assays were analysed, so IL-33 was very probably run.
  - Reconstruction from the delivered q-values shows two of the missing assays had p ≈ 0.0002–0.001, which would pass FDR. About 15 had p < 0.05, where about 5 would be expected by chance (Fig 6).

### 2.3 Tissue: post-mortem lung (31 donors, 74 blocks; analysed per donor) — Fig 5

- **IL-33 is constitutively high in every group.**
  - Endothelial IL-33 sits at the top of the scale (5.5, which is *above* the stated 0–5 range) in 4/5 non-pneumonia and 6/10 COVID-negative pneumonia donors. Overall, 39/74 endothelial blocks are at ceiling.
- **IL-33 is not increased in COVID-19.** Differences, COVID+ minus COVID− pneumonia (95% bootstrap CI):
  - Endothelium −0.38 (−0.81 to +0.06).
  - Vascular smooth muscle −0.60 (−1.31 to +0.17).
  - Basal epithelium +0.06 (−0.58 to +0.72).
  - An increase in endothelium is effectively excluded, but the ceiling in controls limits what the scoring can show.
- **Inflammatory-cell markers track pneumonia, not SARS-CoV-2.**
  - Neutrophil elastase, EDN, MBP, IL-5Rα and H&E eosinophils separate pneumonia from non-pneumonia (p = 0.004–0.010).
  - They do **not** separate COVID+ from COVID− pneumonia (p ≥ 0.44).
  - In a sensitivity analysis restricted to the 22 donors whose category agrees with their pathology report, no COVID+ vs COVID− pneumonia difference reaches significance (all p ≥ 0.18).
- **Endothelial IL-33 is lower where neutrophils are abundant** (ρ = −0.43, p = 0.016, nominal among ~30 tests). This is consistent with IL-33 release from inflamed vessels, but nuclear IHC cannot see released IL-33, so it is only a hypothesis.

### 2.4 The bridge: does the AX-1177-reversible programme explain severity in patients? — Fig 4

- **Only partly, and weakly.**
  - Among 869 serum proteins mappable to the transcriptome, genes that are IL-33-induced *and* reversed by AX-1177 are modestly over-represented among severity markers: 23% vs 16%, OR 1.56, p = 0.094.
  - The most strongly IL-33-induced secreted products (CXCL6, G-CSF, CXCL5, CXCL10, TNF) show no association with outcome.
- **The overlap is a usable PD panel.** OPG, IL-6, CCL20, IL-18R1, IL-1β and CSF-1 each:
  - are IL-33-induced at 6 h **and** 24 h;
  - are neutralised ≥90% by AX-1177 at both timepoints;
  - are severity-associated (q < 0.05).
- **Early-only markers:** tissue factor, VEGF-A and MCP-3 are induced and reversed at 6 h only, not at 24 h.
- **The key link is currently unreadable.** Six serum severity markers are most relevant to an endothelial IL-33 mechanism: **sST2, PTX3, IL-8, vWF, MCP-1 and E-selectin.** The delivered RNA-seq statistics for these genes are degenerate (§8), so our in vitro data can neither confirm nor exclude that IL-33 drives them. Their point estimates sit on the full-neutralisation line (e.g., E-selectin +11.2 / −11.0 log2; IL1RL1 +1.6 / −1.7). That makes a per-cell-line refit the single highest-value, lowest-cost next step.

---

## 3. The case for keeping: the strongest arguments our data support

1. **Competent, specific pharmacology.**
   - AX-1177 reverses a ~4,000-gene IL-33 programme against an isotype control, at both timepoints, even when added concurrently with IL-33. Reversal is complete on robustly measured genes.
   - It has no detectable transcriptional activity of its own in four cell types.
2. **An IL-33-axis prognostic biomarker in our own patients.**
   - sST2 is #2 of 1,063 proteins, adjusted for NEWS2, and is not mirrored by the cardiac-stretch marker NT-proBNP.
   - That gives the first patient study a ready enrichment strategy, which is unusual at this stage.
3. **The drug's pharmacology intersects the patient severity signature.**
   - Six proteins that AX-1177 fully suppresses in endothelium are higher in patients who deteriorate.
   - That is a pre-specified PD readout with a supported sampling window (§5.4).
4. **A plausible tissue substrate.** Every donor lung shows substantial endothelial IL-33 staining (donor means 3.0–5.5), the highest of the three compartments scored. Its nominal depletion where neutrophils are abundant fits, but does not prove, an alarmin-release model.
5. **Cheap resolution of the key uncertainties.** The undelivered Olink results (very probably including IL-33), the count matrix and the banked tissue RNA already exist. Killing the asset before reading data we own would be hard to defend.

## 4. The case against: how the committee will challenge it, and our answers

| Challenge | Answer |
|---|---|
| "sST2 marks severity; it doesn't prove IL-33 matters." | Agreed. We use sST2 **only** for prognostic enrichment. Proof of IL-33 involvement is Gate G1, and failing it kills the asset. |
| "You never measured IL-33 in patients." | Correct: it is not in the delivery. But the BH denominator shows 100 assays were analysed but not delivered, very probably including IL-33, and 2 of those are FDR-significant. Retrieving them is step 0a. |
| "Lung IL-33 isn't higher in COVID-19." | Correct, and this scoring could not show an increase because controls are at ceiling. Nuclear IHC measures stored, not released, IL-33. Step 1b tests pathway *activity* in banked lung RNA. |
| "Most IL-33-induced genes don't track outcome." | Correct (enrichment p = 0.094). We carry forward only the overlapping subset, and only as PD markers, not as proof of causality. |
| "One pre-vaccination COVID cohort, single centre, n=100." | Correct. Replication in influenza, RSV and vaccinated-era COVID is Gate G3, and failing it kills the asset. |
| "What differentiates AX-1177?" | On our data, nothing yet. Binding to oxidised IL-33 is asserted in the annex but never tested functionally. That is Gate G2. Competitive positioning is outside the data provided. |
| "Is the in vitro evidence sound?" | The neutralisation conclusion is robust: it holds on well-measured, non-degenerate genes at both timepoints against isotype. But 178 genes, including the canonical activation markers, need a refit before anyone quotes them (§8). |

---

## 5. Forward view

### 5.1 What indication do our data actually point at?

**Not a different disease. They point at a narrower, mechanism-defined subset of the current one:**

> **Hospitalised adults with viral pneumonia, not yet ventilated, with a high-sST2 / endothelial-activation profile at admission. Goal: prevent progression to ICU, invasive ventilation or death.**

Why, from our data:
- The IL-33 activity we have shown, and neutralised, is **endothelial**.
- In patients, severity tracks the **sST2 and endothelial/coagulation/IL-6 axis**, not the type-2 axis.
- Lung **endothelium shows the highest IL-33 staining** of the three compartments scored, in every group.
- The IL-33 response is **early and partly transient** (4,031 → 1,836 genes from 6 h to 24 h). That favours intervening **before** respiratory failure rather than in established ARDS.
- The tissue picture is **indistinguishable in COVID+ and COVID− pneumonia**, so a pathogen-agnostic "viral pneumonia" framing is plausible. But our serum evidence is COVID-only, and that is exactly what Gate G3 tests.

*Honest caveat:* the endothelial emphasis partly reflects design, since only endothelial cells received IL-33. The patient and tissue data **corroborate** it; they did not independently discover it.

**What the data do not point at:**
- **Asthma, COPD or eosinophilic disease.** There is no type-2 signal, and no epithelial or oxidised-IL-33 data. The only COPD-relevant information is post-mortem annotations (12 donors; IL-33 differences not significant). A COPD pivot would be an externally motivated bet, not a data-driven one.
- **Kidney disease.** The only support is HGMEC responsiveness; serum KIM-1 is nominal and cystatin C is null.
- **Sepsis broadly.** We have no data.

### 5.2 What the next studies must establish

**Stage 0 — use what we already own (0–8 weeks; negligible external cost)**

| # | Action | Must establish |
|---|---|---|
| 0a | Retrieve the 100 analysed-but-undelivered Olink assays, with %<LOD. | Is serum IL-33 detectable, and is it associated with severity after NEWS2 adjustment? |
| 0b | Obtain patient-level NPX and covariates (100 patients). | sST2's incremental value over NEWS2 (ΔAUC/NRI) and a provisional cut-off. Whether sST2 is independent of IL-6/HGF. How the PD panel correlates with sST2. Also confirm the log base and the meaning of `composite_endpoint_0/1`. |
| 0c | Refit the RNA-seq **per cell line** from the archived counts, with sample-identity QC. | Resolve the 178 degenerate genes (sST2/IL1RL1, E-selectin, VCAM-1, ICAM-1, IL-8, MCP-1, PTX3, vWF). Extract the HGMEC IL-33 response (IL-33+isotype vs isotype) and isotype vs vehicle. |
| 0d | Blinded two-reader digital re-quantification of the post-mortem IHC (nuclear vs extracellular IL-33). Re-adjudicate the 9 discordant categories and add normal-lung controls. | Whether IL-33 is released or depleted in inflamed lungs, measured on an unsaturated scale. |

**Stage 1 — decisive experiments (2–6 months; modest cost)**

| # | Action | Must establish |
|---|---|---|
| 1a | Functional pharmacology: AX-1177 dose–response vs **reduced and oxidised** IL-33, in **lung microvascular endothelium** (ST2 readouts) and **primary airway epithelium** (ST2-independent / oxidised readouts). Compare pre-incubation vs concurrent addition; time course to 72 h. | IC50/IC90 for each form, and whether the oxidised-form claim is functional (G2). |
| 1b | RNA-seq of the **22 banked post-mortem lung RNAs** (Zr4940 series: 9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia). | Is the AX-1177-reversible IL-33 endothelial signature *active* in viral-pneumonia lung vs controls (G1, tissue arm)? |
| 1c | Independent biomarker cohort (biobank or prospective): hospitalised influenza, RSV and vaccinated-era SARS-CoV-2 pneumonia. Sample at admission (pre-treatment), then 24 h, day 3 and day 7. Measure sST2, sensitive total/reduced/oxidised IL-33 and the PD panel. Outcome: ICU/IMV/death ≤ 30 d. | Does sST2's prognostic value generalise beyond pre-vaccination COVID (G3)? Is IL-33 present and prognostic (G1, serum arm)? |

### 5.3 Gates at ~6 months (agree these now)

| Gate | Pass criterion | If it fails |
|---|---|---|
| **G1: target present** | IL-33 (any form) is detectable in a meaningful share of admitted patients and associated with severity after NEWS2 adjustment (0a or 1c). **Or** the AX-1177-reversible signature is elevated in viral-pneumonia lung vs controls (1b). | **Kill** |
| **G2: differentiation** | AX-1177 neutralises oxidised-IL-33 activity with potency comparable to reduced IL-33 (e.g., within 10-fold; biologics team to ratify). | Re-position as a conventional anti-IL-33; the committee decides whether to compete undifferentiated. |
| **G3: enrichment holds** | sST2 keeps independent prognostic value beyond NEWS2 (CI excludes 1; positive ΔAUC) in the non-COVID / vaccinated-era cohort. | **Kill** (or a COVID-only niche, if commercially justified) |
| **G4: bridge** (supportive) | After refit, IL-33 induces and AX-1177 reverses endothelial sST2 / E-selectin / VCAM-1 / IL-8 / PTX3. | PD panel stays limited to OPG/IL-6/CCL20/IL-18R1/IL-1β/CSF-1. |

If G1 and G3 pass: run a **Phase 1b/2a in sST2-high hospitalised viral pneumonia**.
- Primary endpoints: safety, target engagement (total IL-33) and change in the PD panel at 24 h.
- Exploratory endpoint: progression to ICU/IMV/death.

### 5.4 Biomarkers, sampling timepoint and their roles in patients

**Sampling timepoint: at enrolment / hospital admission, pre-dose.**
- It is the only timepoint at which our clinical associations exist (serum was drawn at enrolment).
- It is where an enrichment decision must be made.
- In vitro, the IL-33 endothelial response is larger at 6 h than at 24 h (4,031 vs 1,836 genes), so the earliest sample is the one most likely to capture it.
- Draw it before systemic corticosteroids or IL-6-pathway drugs where possible, or record their timing.

**On-treatment PD timepoint: 24 h post-dose.**
- It is the latest time at which our data show the IL-33 programme still active and fully blocked.
- The PD markers below are all still induced and reversed at 24 h.
- Tissue factor, MCP-3 and VEGF-A are reversed at 6 h only, so they are uninformative at 24 h.
- We have no data beyond 24 h. Day 3 and day 7 samples are for natural history and outcome, not PD.

| Marker (serum) | Role | Into patients? | Basis in our data | Prerequisite |
|---|---|---|---|---|
| **sST2** | **Prognostic enrichment / stratification** at enrolment | **Yes**: first patient study, as enrichment and stratification factor. **Not** a companion diagnostic (no predictive data). | OR 3.02/log unit, q = 0.0075, #2/1,063; NEWS2-adjusted; not tracked by NT-proBNP | Clinical-grade quantitative assay; cut-off from patient-level data (0b); replication (G3) |
| **Total IL-33** (free + drug-bound; reduced / oxidised) | **Target engagement**; dose selection | **Yes**, once an assay exists (Phase 1b) | None yet; IL-33 not delivered | Form-specific sensitive assay; read the hidden Olink result first |
| **OPG** (lead), **IL-6**, **CCL20**, **IL-18R1**, **IL-1β**, **CSF-1** | **Pharmacodynamic** pathway panel; exploratory endpoints, pre-dose vs 24 h | **Yes**, exploratory only | Induced at 6 h and 24 h; ≥90% reversed; serum q < 0.05. OPG replicated on 2 panels (OR 6.8, 4.4); IL-6 on 4 | Confirm in lung microvascular cells (1a); note IL-6 is confounded by steroids / IL-6R blockade |
| vWF, PTX3, E-selectin, IL-8, MCP-1, ANGPT2 | Prognostic covariates; PD role pending refit | Exploratory | Severity-associated; in vitro status unresolved | Refit (0c) |
| Tissue IL-33 IHC; eosinophil / type-2 markers | None | **No** | Constitutive / at ceiling; type-2 flat | — |

*PD caveat:* none of these markers is IL-33-specific; they are shared NF-κB outputs. Their job is to show that the pathway moves on drug, not to select patients. CSF-1's OR of 90 (CI 4–1,933) is a per-log-unit scaling artefact and should not be quoted as an effect size.

---

## 6. If we drop it: what we are dropping and why

> We would be dropping a clean, fully neutralising anti-IL-33 antibody. Its demonstrated activity is blockade of the endothelial IL-33/NF-κB programme, and it comes with a prognostic enrichment biomarker (sST2) and a pre-specified PD panel for hospitalised COVID-19.
>
> We would drop it because, on our data:
> 1. There is no evidence that IL-33 itself is elevated, released or causal in severe viral pneumonia. The serum assay result was never delivered, and lung IL-33 is constitutive and not increased in COVID-19.
> 2. Severity in patients tracks a broad inflammatory, endothelial and neutrophil signature. It is only weakly enriched for the IL-33 programme, and not at all for the type-2 axis.
> 3. The presumed differentiator, oxidised-IL-33 binding, has never been shown to be functional.
> 4. The clinical evidence is one pre-vaccination COVID-19 cohort.
>
> No other indication is supported by our data.

---

## 7. What we considered and ruled out

| Considered | Outcome | Why |
|---|---|---|
| Continue in severe viral LRTI, all-comers | **Ruled out** | No evidence IL-33 drives severity (§2.2–2.4) |
| Type-2 / eosinophil framing; eosinophil-based selection | **Ruled out** | IL-5, eotaxins, CCL17 and tryptase are flat in serum; tissue eosinophils are not COVID-specific |
| Pivot to asthma/COPD on our data | **Ruled out as data-driven** | Only post-mortem annotations (n=12, n.s.); no epithelial/oxidised-IL-33 or patient data |
| Kidney/glomerular indication (from HGMEC) | **Ruled out** | In vitro responsiveness only; KIM-1 nominal, cystatin C null |
| Tissue IL-33 IHC as a patient biomarker | **Ruled out** | Invasive, constitutive, at ceiling, no disease contrast |
| Serum IL-33 (Olink) for selection or PD | **Not usable yet** | Not delivered (presumably below LOD); needs a sensitive assay |
| sST2 as a PD marker | **Not supported yet** | IL1RL1 in vitro statistics are degenerate (+1.6 log2, q = 0.98); refit first |
| Headline "IL-33 induces E-selectin >2,000-fold" (top of the HUVEC file by logFC) | **Ruled out** | t = 1.26, q = 0.50; degenerate SE |
| Ranking serum markers by OR | **Ruled out** | Per-log-unit ORs are scale-dependent (CSF-1 OR 90; CTSS 23; GSTP1 25) |
| Counting 178 significant assays as 178 proteins | **Corrected to 169** | 27 proteins are measured on 2–4 panels under different IDs |
| Block-level post-mortem statistics | **Ruled out** | Pseudoreplication: 3 donors contribute 24 of 49 COVID+ blocks |
| Neutralisation measured against the IL-33-alone arm | **Replaced by isotype comparator** | The isotype arm retains only 86% of the IL-33 response at 24 h, so the IL-33-alone comparison overstates neutralisation |
| AX-1177 vs PBS/DMSO as specificity evidence | **Ruled out** | DMSO and PBS are not antibody vehicles; the isotype is the valid control |
| "AX-1177 alone has off-target effects" (21–73 hits) | **Ruled out** | Low-count noise and numerical artefacts; no pathway coherence; π0 ≈ 1 |
| Using the sheet names "6h"/"24h" | **Ruled out** | Both sheets hold identical data for both timepoints |
| Filtering genes on AveExpr | **Ruled out** | AveExpr is pooled over 4 cell types; it would discard CSF2 (AveExpr −3.2), the strongest IL-33 gene |
| IL-33–neutrophil inverse correlation as proof of release | **Hypothesis only** | Nominal p = 0.016 among ~30 tests; IHC cannot see released IL-33 |
| Competitive or commercial positioning | **Not assessed** | Outside the data provided; the committee should overlay it |

---

## 8. Data-integrity findings that constrain what can be claimed

Full log with remedies: supporting tables, sheet 10; see also Fig 6.

1. **RNA-seq: 178 genes have degenerate statistics.**
   - The implied SE is more than 10× the expected value for their expression (e.g., CD93 SE ≈ 16,500 log2 units; t ≈ 10⁻⁵ at log2FC up to 8).
   - They are enriched for cell-identity genes and for the canonical endothelial-activation genes (SELE, VCAM1, CXCL8, CCL2, PTX3, IL1RL1, VWF, ESM1).
   - The most likely cause is the single pooled model across four very different cell types, possibly with a mis-assigned library.
   - Whatever the cause, these genes cannot be interpreted until the data are refit per cell line.
2. **RNA-seq: workbook and design issues.**
   - The "6h" and "24h" sheets are identical in content; nothing is truncated, despite a 1,048,576-row header.
   - AveExpr is pooled over all 114 libraries.
   - HGMEC has no vehicle arm.
   - The isotype is not fully inert at 24 h.
   - Only reduced IL-33 was used, at a single antibody concentration.
3. **Serum: undelivered assays and documentation gaps.**
   - BH was applied over 1,194 assays, but 1,094 were delivered. The annex says "across all assays in the delivery".
   - The absent assays include IL-33 (very probably among the 100 analysed). Two of the 100 are FDR-significant.
   - `composite_endpoint_0/1` is undocumented. Its values are k/56 and k/44, consistent with per-outcome-group fractions that are missing or below LOD.
4. **Serum: scaling and scope.**
   - ORs are "per log unit" with no base stated, applied to NPX, which is already log2.
   - The cohort is single-centre, single-timepoint and pre-vaccination, with no treatment covariates and no patient-level data delivered.
5. **Post-mortem: structure, scoring and labels.**
   - Donor fields are recorded on the first block only.
   - The numeric columns convert "n+" to n+0.5 (verified for EPX, elastase and tryptase), so 5+ becomes 5.5. The IL-33 columns likewise top out at 5.5, above the stated 0–5 scale, and 53% of endothelial blocks sit at that ceiling.
   - There was a single reader.
   - The category conflicts with the pathology text in 9/31 donors (e.g., a "non-pneumonia" donor with acute and organizing pneumonia).
   - All "non-pneumonia" controls have significant lung disease (IPF, coccidioidomycosis, pneumonitis).
   - Tissue RNA exists for 22 blocks but was not delivered. The Zr4940 numbering has gaps (6, 13, 16–20, 23, 24); ask about them.

**None of these findings changes the neutralisation conclusion or the sST2 association.** Items 1 and 3 do materially limit what we can claim about the mechanism in patients, which is why they are fixed first (Stage 0).

---

### Data requests to the programme team (all referenced in the annex as archived)

1. The 100 undelivered Olink assays, with %<LOD, plus patient-level NPX and clinical covariates (including steroid/IL-6 treatment and days from symptom onset).
2. The RNA-seq count matrix and fitted-model object, for a per-cell-line refit and to extract the missing contrasts.
3. The 22 banked post-mortem lung RNAs (and any others in the Zr4940 series) and the IHC slides for re-scoring.
4. The programme biologics file: affinity, potency, oxidised-form binding and species cross-reactivity.

### Appendix: how the re-analysis was done

- **RNA-seq.**
  - Used the delivered limma-voom statistics.
  - Because every contrast comes from one fitted model, derived contrasts were obtained as linear combinations of log2FCs. Example: IL-33+isotype vs vehicle = (IL-33 vs vehicle) + (AX-1177+IL-33 vs IL-33) − (AX-1177+IL-33 vs IL-33+isotype). No SEs were derived for these.
  - "Robust" genes: q<0.01, |log2FC|>1, AveExpr>1, |t|>6, not degenerate.
  - Degenerate genes: median |logFC/t| across 26 contrasts more than 10× the median of 30 expression-matched bins.
- **Serum.**
  - Olink IDs were mapped to HGNC symbols (alias table in `scripts/olink_map.py`) and collapsed to the protein level.
  - The CI-derived Wald p-values reproduce the delivered p-values exactly.
  - BH denominator reconstruction: q·rank/p gives integer implied ranks at m = 1,194.
  - Enrichment was tested with Fisher's exact test.
- **Post-mortem.**
  - Donor fields forward-filled; "n+" strings parsed; block scores averaged per donor.
  - Tests: Kruskal–Wallis and Mann–Whitney, with bootstrap CIs of mean differences.
  - Sensitivity analysis restricted to pathology-concordant donors.
- **Software:** Python 3.11 (pandas, SciPy, statsmodels, matplotlib). `scripts/run_all.sh` reproduces every table and figure from the raw files.

---

## Figures

![Figure 1. AX-1177 fully neutralises reduced IL-33 signalling in HUVEC at 6 h and 24 h (isotype-matched comparator). Left/centre: each point is a gene; the dashed line is complete neutralisation. Red circles are genes with degenerate statistics (their point estimates lie on the neutralisation line, but they cannot be tested). Right: % of the IL-33 response remaining on robust induced genes.](figures/fig1_invitro_neutralisation.png)

![Figure 2. AX-1177 alone has no coherent transcriptional activity. DE-gene counts per contrast; hatched segments show antibody-alone hits that survive removal of low-count noise and trivial fold-changes.](figures/fig2_specificity_DEcounts.png)

![Figure 3. Serum proteomics (100 hospitalised COVID-19 patients). Left: all 1,094 delivered assays; sST2 ranks #2. Right: IL-1-family receptors and the endothelial/IL-6 axis track severity; the type-2/eosinophil/mast-cell axis is flat; NT-proBNP is weak.](figures/fig3_serum.png)

![Figure 4. Bridge between in vitro pharmacology and patient severity. Only a subset of the AX-1177-reversible endothelial IL-33 programme tracks severity (enrichment p = 0.094). The six most mechanism-relevant serum markers cannot be placed because their RNA-seq statistics are degenerate.](figures/fig4_bridge_invitro_serum.png)

![Figure 5. Post-mortem lung, donor level. IL-33 is constitutively high (endothelium at ceiling in controls) and not increased in COVID-19. Inflammatory-cell markers separate pneumonia from non-pneumonia, not COVID+ from COVID− pneumonia.](figures/fig5_postmortem.png)

![Figure 6. Data-integrity findings. Left: 178 genes with implausible implied standard errors, including canonical endothelial-activation genes. Right: reconstruction of the 100 analysed-but-undelivered serum assays from the BH denominator (m = 1,194).](figures/fig6_data_integrity.png)
