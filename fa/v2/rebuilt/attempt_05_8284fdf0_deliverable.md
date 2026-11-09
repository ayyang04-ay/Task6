---
title: "AX-1177 (anti-IL-33 mAb): portfolio audit recommendation"
subtitle: "Evidence, recommendation, forward plan, and what was considered and ruled out"
---

**Basis.** This memo uses only the programme data dump: the methods annex; `mmc4`/`mmc5` (endothelial and epithelial transcriptomics: 114 libraries, 26 contrasts); `mmc2` (enrolment serum proteomics from 100 patients hospitalised with COVID-19: 13 Olink panels, composite endpoint of ICU, invasive ventilation or death within 30 days); and `mmc3` (post-mortem lung immunohistochemistry: 31 donors, 74 blocks). Compound_47 = AX-1177 and NIP228 = isotype control. I treated the files as ground truth. Where the files' own numbers limit what they can support, I say so (§9). Places where I use general biology to interpret a result are marked *(interpretation)*.

# 1. Recommendation

**Keep AX-1177, but retire it as a viral-LRTD programme.** Re-scope it to one time-boxed question (about 6 months, mostly re-analysis and in vitro work on material we already hold) and agree the kill criteria in advance:

> *Does IL-33 released from injured lung drive the endothelial, neutrophil-recruiting, pro-coagulant host response that predicts ICU admission, ventilation or death in severe pneumonia? And can AX-1177 still block that response once the patient is in hospital?*

If the §6.4 gates are missed, terminate the asset. If the committee will not fund the gate, the alternative is to **drop** it (§7). Continuing in viral LRTD as currently framed is not supported by our data.

**The case in five points**

1. **The molecule works on its target.** In endothelial cells, AX-1177 removes a median **98%** of the IL-33-induced transcriptional response at 6 h and **100%** for the 37 most strongly induced genes. This holds in two vascular beds (HUVEC and HGMEC). No off-target transcriptional signal was seen in any of the four cell types tested.
2. **Our data do not yet link IL-33 to the disease.** IL-33 itself is missing from the serum delivery. Lung IL-33 staining is equally high in COVID+ pneumonia, COVID- pneumonia and non-pneumonia lungs. The serum proteins that predict outcome form a generic severity signature.
3. **Nothing in our data is specific to a virus.** The only patient cohort is SARS-CoV-2: single-centre, pre-vaccination, n = 100. In lung tissue, COVID+ and COVID- pneumonia cannot be told apart on any of 11 measures.
4. **The one thread that runs through all three datasets is endothelial.** That points to a population defined by host response (severe pneumonia with endothelial activation), not one defined by pathogen (§5).
5. **The questions that decide the programme are cheap to answer, mostly with assets we already own.** These are banked serum, archived lung RNA, archived RNA-seq counts, and 100 Olink results that were analysed but not delivered. "Drop now" therefore gives up that option for little saving. "Continue as is" keeps spending on a thesis that has not been validated.

**Decisions requested:**

1. Retire the viral-LRTD positioning.
2. Approve the Stage 0–1 package (§6.4).
3. Endorse the kill criteria.

# 2. Evidence scorecard

| Question | What our data show | What that supports |
|---|---|---|
| **Does AX-1177 neutralise IL-33?** | **HUVEC, IL-33red 30 ng/mL:** 1,068 genes change >2-fold at 6 h and 512 at 24 h.<br>**With AX-1177 (10 µg/mL, co-added):**<br>â¢ 6 h: median inhibition **98%** (IQR 77–103%) across 242 genes induced >4-fold<br>â¢ 24 h: median inhibition **76%** (IQR 40–97%) across 103 genes</li><li>37 genes induced >32-fold: **100%** inhibition<br>**HGMEC (glomerular microvascular EC):** the same programme is blocked. 73% of genes induced >8-fold in HUVEC fall >2-fold with AX-1177 at 6 h. | **Yes:** functional neutralisation of reduced IL-33 on endothelium.<br>**Not tested:** potency, oxidised IL-33, lung cells, dosing after exposure. |
| **Is it clean?** | Antibody alone vs isotype, all four cell types: only 4–9% of genes reach p < 0.05, close to the null. The few "hits" are low-count noise or statistical artefacts. They do not replicate between 6 h and 24 h or across cell lines. The antibody alone does not move the IL-33 programme (slope 0.01–0.02). | No off-target transcriptional activity detected. The epithelial arms had no positive control. |
| **What does IL-33 do to endothelium?** | An NF-κB programme with three parts:<ul><li>**Neutrophil mobilisation and recruitment:** GM-CSF ~1,260×, G-CSF ~320×, CXCL1/2/3/5/6/8, E-selectin ~2,400×, ICAM-1, VCAM-1</li><li>**Pro-coagulant switch:** tissue factor ~50× up, thrombomodulin 2× down, PAI-1 3× up</li><li>**Other mediators:** complement C3/CFB, IL-6, IL-1α/β, TNF</li></ul>A secondary interferon programme appears at 24 h. | A plausible mechanism for endothelial activation and immunothrombosis in severe pneumonia *(interpretation)*. |
| **Is IL-33 present or increased in patients?** | **Serum:** IL-33 is on the Inflammation panel that was run, but it is not in the delivery.<br>**Lung (donor level):**<ul><li>IL-33 is abundant in endothelium, basal epithelium and vascular smooth muscle in every group.</li><li>Endothelium reaches the top of the scale in at least one block for 24 of 31 donors.</li><li>COVID+ vs COVID- pneumonia: p = 0.15–0.92.</li><li>Pneumonia vs non-pneumonia: p = 0.14–0.37.</li></ul> | The target is stored in lung. No increase specific to disease is shown, and release cannot be measured with these data. |
| **Does the IL-33 axis track outcome?** | **The IL-33 axis:** sST2 ranks #2 of 1,063 proteins (OR 3.02 per log unit, 95% CI 1.83–5.01, q = 0.007; adjusted for age, sex and NEWS2). IL-18R1 and IL-1R2 are also associated.<br>**The background:** 82% of proteins have OR > 1 and 35% are nominally significant (5% expected). Intracellular proteins are over-represented.<br>**IL-33-induced endothelial products:** 24% at FDR < 5% vs 15% background (p = 0.06 for the wider set). The most strongly induced (CXCL6, G-CSF, VCAM-1, CXCL1, CXCL5, CCL5) show no association.<br>**What best tracks outcome:** neutrophil activation (79% nominally significant) and the IL-1-receptor family (78%). | Consistent with IL-33 being involved, but does not show that IL-33 drives severity. sST2 is usable for *prognostic* enrichment. |
| **Is anything virus-specific?** | Patients: SARS-CoV-2 only. Lung: COVID+ and COVID- pneumonia are indistinguishable on all 11 IHC measures (p = 0.15–1.0). | No. "Viral" is an assumption, not a finding. |
| **Is there a type-2 / eosinophil angle?** | **Serum:** IL-5 OR 1.00, p = 0.997. Eotaxin-1 and -2, CCL17, CCL13, tryptase and KIT are all null.<br>**Lung:** eosinophil markers rise with pneumonia of any cause (EDN p = 0.004, MBP p = 0.006) but do not differ by COVID status (p = 0.44–0.67). | No type-2 rationale in our data. |

![In vitro: AX-1177 removes the IL-33-induced endothelial programme. Top: HUVEC 6 h and 24 h; each point is a gene (x = response with isotype, y = response with AX-1177). Bottom left: the same genes are reversed in HGMEC. Bottom right: kinetics.](figures/Fig1_invitro_neutralisation.png)

# 3. Why the viral-LRTD thesis should be retired

- **The link between target and disease is unproven.** We have no IL-33 measurement in patients. Tissue shows no increase, and the serum signal is generic. sST2 is the best IL-33-axis signal we have. But it is a decoy receptor that rises in many acute illnesses *(interpretation)*, and it sits inside a proteome-wide upward shift (Fig. 2).
- **The indication is defined by something our data cannot see.** We have one virus and nothing that separates it from other causes of pneumonia.
- **The in vitro design is prophylactic, but the clinical setting is therapeutic.** The antibody was added at the same moment as IL-33. Hospitalised patients arrive after alarmin release. Our own kinetics show why this matters:
  - The primary-response genes are already fading by 24 h (E-selectin 2,400× → 27×; tissue factor 50× → 2×; TNF back to baseline).
  - Even with antibody present from time zero, inhibition falls from 98% at 6 h to 76% at 24 h.
  - The late interferon programme partly escapes: CXCL10 is only 47% inhibited, MX2 42% and RSAD2 33%.
  - Whether AX-1177 can reverse a response that is already established is the most important untested question for a hospital indication.
- **The stated differentiator is untested.** AX-1177 binds oxidised IL-33, but only reduced IL-33 was used, and only endothelium was challenged. Today our data cannot distinguish AX-1177 from any blocker of the ST2 pathway.
- **The cohort has limits.** It is single-centre, pre-vaccination and n = 100, with one timepoint. We have summary statistics only, with no patient-level data, no time from symptom onset, and no adjustment for renal function or treatment.

# 4. Why keep the molecule (the defence)

- **Neutralisation is clean, strong and reproducible.** It holds across two endothelial beds and two timepoints, with no off-target signal.
- **What it blocks matches the biology that predicts outcome.** IL-33 makes endothelium recruit neutrophils (G-CSF, GM-CSF, CXCL chemokines, E-selectin) and switch to a pro-coagulant state. The serum biology that best predicts ICU, ventilation or death is exactly this neighbourhood: neutrophil activation (19/24 proteins nominally significant), IL-1-receptor-family decoys including sST2 (7/9), and endothelial injury (HGF, PTX3, vWF, ANGPT2, uPAR, tissue factor).
- **IL-33 is stored where it would matter.** Lung endothelium stains at the ceiling in 24 of 31 donors, including non-COVID pneumonia. The hypothesis is therefore pathogen-agnostic.
- **A pharmacodynamic (PD) panel already exists.** Ten IL-33-induced, AX-1177-blocked endothelial products are measurable in patient serum and associated with outcome at FDR < 5%: PTX3, IL-6, OPG, sIL-18R1, MCP-3, CCL20, IL-8, CSF-1, cathepsin S and IL-1β. Tissue factor and MCP-1 are borderline (q = 0.051).
- **The decisive experiments are cheap and use assets we hold:**
  - banked enrolment serum (n = 100);
  - 22 archived lung RNA samples (Zr4940 series: 9 COVID+ pneumonia, 9 COVID- pneumonia, 4 controls);
  - archived RNA-seq counts;
  - the 100 analysed-but-withheld Olink results.

![Serum proteomics (one point per protein). Neutrophil-activation and IL-1-receptor-family proteins track outcome far more often than background. IL-33-induced endothelial genes track outcome at close to the background rate, and type-2 proteins below it. 82% of proteins have OR > 1.](figures/Fig2_serum_proteomics.png)

# 5. What indication our data actually point at

**A population defined by host response, not by pathogen: hospitalised severe pneumonia / acute lung injury with endothelial activation. It would be pathogen-agnostic and biomarker-selected, for example by high sST2 plus endothelial-activation markers at admission.**

COVID-19 is the only setting in which we have patient data. Treat it as the validation context, not the indication.

**Why endothelial.** It is the only thread present in all three datasets:

| Dataset | Endothelial evidence |
|---|---|
| Tissue | IL-33 is stored at the highest levels in lung endothelium. |
| Mechanism | IL-33 turns endothelium inflammatory, neutrophil-recruiting and pro-coagulant, and AX-1177 blocks this in macro- and microvascular cells. |
| Patients | The outcome signature is dominated by neutrophil activation, endothelial injury and IL-1-family decoys. |

**Why pathogen-agnostic.** In lung tissue, COVID- pneumonia is indistinguishable from COVID+ pneumonia on both IL-33 and inflammatory cells.

**What the data do not point at:**

| Indication | Why not |
|---|---|
| **Asthma / COPD / type-2 airway disease** | No epithelial IL-33 experiment was done (the epithelial lines never received IL-33). There is no serum type-2 signal. Lung IL-33 staining is not higher in donors annotated with COPD or asthma (p ≥ 0.21). A case here would rest entirely on external evidence, so it is a different decision. |
| **Kidney** | HGMEC respond, but we have no renal patient data, and KIM-1 is only nominally associated (q = 0.11). |
| **Cardiovascular** | sST2 rises here in acute pneumonia, and we have no cardiac data. |

This is a hypothesis our data make plausible. They do not prove it.

# 6. Forward view

## 6.1 What the next studies must establish (in order of decision value)

1. **The target is present and active in patients.** Either IL-33 (free and total, reduced and oxidised) is measurable and tracks severity or endothelial markers, or patient serum carries endothelial-activating activity that AX-1177 can neutralise.
2. **There is a therapeutic window.** AX-1177 must reverse an IL-33 response that is already established (antibody added after IL-33), in lung microvascular endothelium from several donors.
3. **The tissue is relevant.** The IL-33 endothelial signature must be active in pneumonia lungs compared with controls.
4. **The pharmacology holds in the right system.** This needs:
   - concentration–response (IC50/IC90);
   - oxidised and full-length IL-33;
   - lung epithelium (the oxidised-IL-33 arm, which is AX-1177's differentiator);
   - functional endpoints (neutrophil adhesion and transmigration, permeability, tissue factor activity);
   - a TNF/IL-1β counter-screen to find which readouts are specific to IL-33.
5. **A biomarker strategy that works in patients.** This covers enrichment, PD, target engagement and safety (§6.2).

## 6.2 Biomarkers: which can go into patients, and in what role

| Marker | Role in patients | Ready now? | Evidence from our data |
|---|---|---|---|
| **sST2** | **Prognostic enrichment** at baseline, to select high-risk patients. A *candidate* predictive marker, to be tested in a stratified design rather than assumed. **Not a PD marker.** | Yes | #2 of 1,063 proteins; OR 3.02 (1.83–5.01) per log unit, q = 0.007; 0% below the limit of detection (LOD). IL-33 raised *IL1RL1* only about 3-fold in HUVEC (statistics unusable) and not at all in HGMEC. High sST2 may mean IL-33 is already sequestered *(interpretation)*. |
| **CCL20, OPG, IL-6, IL-8, sIL-18R1, MCP-3** (secondary: MCP-1, IL-1β) | **PD / mechanism:** the change from baseline at 24 h, drug vs placebo. Also secondary prognostic markers. | Yes | Each is induced by IL-33 in HUVEC (12–590× at 6 h) and ≥95% blocked by AX-1177. Each is associated with outcome (q = 0.012–0.046; MCP-1 q = 0.051). None is specific to IL-33, so they are interpretable only against placebo. |
| **Tissue factor, sE-selectin** | **Early** endothelial PD (exploratory). | Yes | Induced 50× and 2,400× at 6 h, mostly gone by 24 h, so they need early sampling. Serum tissue factor q = 0.051; sE-selectin p = 0.02 (q = 0.09). E-selectin is the most endothelium-restricted readout *(interpretation)*. |
| **HGF, PTX3, vWF, ANGPT2** | Prognostic covariates / stratification. **Not PD.** | Yes | HGF is the #1 predictor (q = 0.004) but does not respond to IL-33 in vitro. vWF and ANGPT2 (q ≈ 0.05) also do not move with IL-33. PTX3 (q = 0.012) rises about 4.5× with IL-33, but its transcript statistics are unusable. |
| **Neutrophil activation set** (CLEC5A, PRTN3, CD177, resistin, S100A12, LCN2, OSM) | Downstream disease activity; exploratory PD. | Yes | The most consistently outcome-linked biology: 19/24 proteins nominally significant, 11/24 at FDR < 5%. |
| **IL-33** (free, and drug-bound/total; reduced and oxidised) | **Target engagement.** Entry criterion if it proves detectable. | **No.** First retrieve the withheld result; then build drug-tolerant ultrasensitive assays. | The only direct proof that the target is present and engaged. Total IL-33 should *rise* on drug, because drug–IL-33 complexes accumulate; pre-specify this *(interpretation)*. |
| **Viral load / clearance** | **Safety** | Yes | IL-33 induced an interferon-stimulated gene programme in endothelium at 24 h (MX1/2, IFIT1, RSAD2, OAS2, GBP5). AX-1177 removes most of it. |
| GM-CSF, CXCL6, G-CSF, C3, CXCL5, EBI3; **26-gene core signature** | **Lab only:** in vitro potency, the serum bioassay, and scoring of tissue RNA. | No | These are the largest, most persistent and fully blocked responses, conserved in HGMEC. But serum CXCL6, G-CSF, CXCL5 and CCL5 are *not* outcome-associated, and GM-CSF is not on the panels. |
| **Ruled out for patients** | — | — | Serum VCAM-1, ICAM-1, CXCL1, TNF and CXCL10: strongly IL-33-induced in vitro but not outcome-associated (p = 0.11–0.46). Eosinophil and type-2 markers. IHC IL-33 score (post-mortem only, ceiling effect). |

## 6.3 Sampling timepoints

| Setting | When to sample | Rationale from our data |
|---|---|---|
| Lab | **6 h** after IL-33 exposure is the primary readout. 24 h is secondary only. | 6 h gives the peak response (1,068 vs 512 genes changing >2-fold) and the cleanest neutralisation (98% vs 76%). By 24 h, the primary-response genes (TNF, tissue factor, E-selectin, VCAM-1) have largely gone, and a secondary interferon programme confounds the readout. |
| Patients, baseline | **At enrolment, before the first dose.** | This is the only timepoint at which our data show prognostic value (sST2, HGF, PTX3, IL-6, CCL20, OPG). |
| Patients, PD | **24 h after the first dose.** | In vitro, the core PD markers are still strongly induced at 24 h and still fully blocked. Examples: CCL20 590× → 48×, IL-6 56× → 7×, IL-8 290× → 50×, OPG 28× → 5×; AX-1177 inhibition ~100% at both times. Tissue factor and E-selectin would need an additional earlier sample. |
| Patients, always | Record **time from symptom onset**. | The IL-33 response is front-loaded. |

## 6.4 Plan, gates and kill criteria

| Stage | Timing | Work | Material |
|---|---|---|---|
| **0: Re-analysis** | Weeks 0–6 | **(a) Serum data.** Retrieve the 100 withheld Olink results (IL-33 included), the LOD fractions and the patient-level NPX data. Re-analyse with: odds ratios per SD; adjustment for eGFR, treatment and time from onset; added value over NEWS2; sST2 cut-points; and a composite IL-33-endothelial PD score.<br>**(b) RNA-seq.** Refit the model per cell type from the archived counts.<br>**(c) Biologics file.** Pull AX-1177 affinity, potency and species cross-reactivity. | Existing data only |
| **1: Decisive experiments** | Months 1–5 | **(a) Endothelium.** Lung microvascular EC from ≥3 donors, plus HUVEC and HGMEC *with* vehicle arms:<ul><li>concentration–response for IL-33 in reduced, oxidised and full-length forms;</li><li>AX-1177 concentration–response vs isotype;</li><li>antibody pre-incubated, co-added, or added 1, 3 and 6 h *after* IL-33;</li><li>6 h readout (primary) and 24 h (secondary);</li><li>functional readouts: neutrophil adhesion and transmigration, permeability, tissue factor activity;</li><li>TNF and IL-1β arms as specificity controls.</li></ul>**(b) Epithelium.** Primary airway basal and alveolar epithelium ± oxidised IL-33 ± AX-1177.<br>**(c) Serum bioassay.** The 100 banked enrolment sera on lung microvascular EC, 6 h, ± AX-1177 or isotype.<br>**(d) Tissue.** Score the 26-gene core signature in the 22 archived lung RNAs at donor level, plus a blinded second IHC read with quantitative nuclear IL-33. | Banked serum, archived RNA, existing blocks |
| **Gate** | ~Month 6 | Decision below. | — |
| **2: Only if the gate is passed** | Months 6–15 | **(a) In vivo.** Dosing after disease onset in a pneumonia / lung-injury model (species set by cross-reactivity), with pathogen load as a safety readout.<br>**(b) Cohort.** An independent non-COVID pneumonia cohort (influenza, RSV, bacterial) run on the same serum panel.<br>**(c) Assays.** Drug-tolerant IL-33 (free and total) and a clinical sST2 assay.<br>**(d) Clinical plan.** Design of a biomarker-enriched proof-of-mechanism study. | New |

**Go requires both:**

- **G1 – target.** Either IL-33 is detectable and associated with severity or endothelial markers, or patient serum shows endothelial activity that AX-1177 neutralises (threshold to be pre-set).
- **G2 – window.** AX-1177 added ≥3 h after IL-33 reverses ≥50% of the established 6-h response in lung microvascular EC.

**Gate outcomes:**

| Result | Consequence |
|---|---|
| G1 or G2 fails | **Kill.** |
| G3 fails alone (core signature not higher in pneumonia lung RNA than in controls, at donor level) | Committee review. |
| No oxidised-IL-33 activity in epithelium, or AX-1177 does not block it | Not a kill, but it changes positioning: AX-1177 would be an ST2-pathway blocker in practice. |
| TNF/IL-1β reproduce the whole programme | Not a kill, but it changes positioning: PD would then have to rely on target engagement plus drug-vs-placebo comparison. |

# 7. If we drop AX-1177: what we are dropping, and why

**What we would drop.** A well-behaved anti-IL-33 antibody that binds reduced and oxidised IL-33. In vitro it blocks IL-33-driven endothelial activation almost completely in two vascular beds, with no detectable off-target activity. It comes with a biomarker framework that is ready to use: sST2 for enrichment, and an IL-33-inducible serum PD panel (CCL20, OPG, IL-6, IL-8, sIL-18R1, MCP-3).

**What we would *not* be dropping** is a validated link between IL-33 and the outcome of viral LRTD, because our data do not contain one.

**Why drop:**

1. No evidence that IL-33 is raised or active in patients; it is not in the delivery.
2. No IL-33 signal specific to disease in lung tissue.
3. The serum predictors of outcome are generic.
4. The therapeutic window for a hospitalised population is untested.
5. The differentiating feature (activity against oxidised IL-33) is untested.

**Residual value:** the molecule, the data package and the biomarker/assay framework can be parked, or offered to partners, and reactivated if IL-33 activity is later shown in a disease setting.

# 8. Considered and ruled out

**Indications**

| Option | Verdict | Reason (our data) |
|---|---|---|
| Viral LRTD (current framing) | Retire | IL-33 not measured in patients; no disease-specific tissue signal; serum signal generic; only one virus studied. |
| COVID-19-specific indication | Ruled out | COVID+ and COVID- pneumonia identical in tissue; pre-vaccination single-centre cohort. |
| Asthma / COPD / type-2 airway disease | Not supported by our data | No epithelial IL-33 stimulation was done. Serum IL-5 OR 1.00, and eotaxins and tryptase are null. Lung IL-33 staining does not differ by COPD or asthma annotation (n = 11 and 6 donors; p ≥ 0.21). |
| Renal / glomerular microvascular disease | Considered; not supported | HGMEC respond, but there is no HGMEC vehicle arm and no renal patient data. KIM-1 q = 0.11; NGAL is associated but non-specific. |
| Heart failure / cardiovascular (because of sST2) | Ruled out | The sST2 signal arises in acute pneumonia; no cardiac data. |
| Prophylaxis / early outpatient use | Deferred | Our in vitro efficacy comes only from co-addition. Revisit after the delayed-addition experiment. |

**Analytical shortcuts rejected**

| Shortcut | Why rejected | What I did instead |
|---|---|---|
| Use the delivered transcriptomic p-values and DEG counts at face value | About 130 genes have impossible SEs. Pooled degrees of freedom make 0.2-log2 changes "significant". | Effect sizes, replication and reversal by AX-1177. |
| Read the `mmc5` sheets as "6 h" and "24 h" | Both sheets contain all 24 contrasts. | Matched contrasts by name. |
| Count Olink hits by assay | 1,094 assays = 1,063 proteins (IL-6 ×4, HGF ×2, OPG ×2, …). | Deduplicated to proteins. |
| Rank proteins by OR magnitude | ORs per log unit are unstandardised (CSF-1 OR 90, CI 4–1,933). | Ranked by p and confidence interval. |
| Analyse IHC per block | Pseudo-replication: 3 donors contribute 24 of 74 blocks. Endothelial IL-33 gives p = 0.02 per block vs 0.14 per donor. | Analysed per donor. |
| Estimate the IL-33 effect in HGMEC, or use the epithelial lines for efficacy | No HGMEC vehicle arm. The epithelial lines received no IL-33, used DMSO as a vehicle, and MCF7 is a breast line. | Not attempted. |

**Biomarkers rejected:** serum IL-33 for selection now (not available); sST2 as a PD marker; HGF, vWF and ANGPT2 as PD markers; serum CXCL6, G-CSF, VCAM-1, CXCL1 and CXCL5; eosinophil and type-2 markers; the IHC IL-33 score.

# 9. Data-integrity findings the committee should know

Full log: `tables/AX-1177_supporting_tables.xlsx`, sheet 9.

![Left: canonical activation genes have huge fold-changes but inflated SEs, so their p-values are unusable. Middle: the same gene under the same 3-vs-3 design gets SEs differing up to ~10^4-fold by cell line. Right: the delivered q-values imply 1,194 tests, not 1,094.](figures/Fig4_data_integrity.png)

**Serum proteomics**

- **100 serum assays were analysed but withheld.** The delivered BH q-values can only be reproduced with 1,194 tests, not the 1,094 delivered (13 panels × 92 = 1,196). At least one withheld assay had p ≈ 2–3 × 10⁻⁴, and about 16 had p < 0.05. **IL-33 is on a panel that was run but is absent from the delivery.** Retrieving these results is the first action.
- **The proteomics ORs need care.** They are "per log unit" of unstated base (NPX is already log2) and are unstandardised. 82% of proteins have OR > 1. There is no adjustment for renal function or treatment, and serum rather than plasma may add release during clotting *(interpretation)*. The undocumented columns `composite_endpoint_0/1` look like fractions below LOD, with denominators 56 and 44 (i.e. 44 events).

**Transcriptomics**

- **The single limma-voom model across four unrelated cell types yields unusable statistics for a subset of genes.**
  - 130 genes have median SE > 2 log2 units, including CDH5, VWF, GAPDH and IL1RL1.
  - SEs for the same gene differ up to ~10⁵-fold between cell lines.
  - Result: false negatives for the best-known activation genes (E-selectin 2,400×, VCAM-1, CXCL1, IL-8, MCP-1, COX-2 and PTX3 all have p > 0.2), and a few false positives (e.g. AKR1C2 log2FC 0.11 with t = 169).
  - A per-cell-line refit is Stage 0.
- **Design gaps:**
  - no vehicle arm in HGMEC;
  - no IL-33 in the epithelial arms;
  - DMSO used as an antibody vehicle;
  - one antibody concentration (~41:1 molar excess);
  - co-addition only;
  - one donor per primary cell type;
  - no lung endothelium or basal epithelium.

**Lung IHC**

- Numeric scores are the grade + 0.5, so the maximum is 5.5, exceeding the stated 0–5 scale. Endothelial IL-33 is at that maximum in 39 of 74 blocks.
- Scoring was by a single reader.
- One donor (1905) lacks SARS-CoV-2 status.
- Lung-condition notes sit on non-first blocks for two donors.

# 10. Likely challenges

**"sST2 is the #2 predictor. Isn't that human validation of IL-33?"**
It is the best IL-33-axis signal we have, and it supports using sST2 to enrich for high-risk patients. But it is a decoy receptor measured inside a proteome-wide upward shift, and IL-33 itself was not delivered. High sST2 could even mean less free IL-33 *(interpretation)*. It validates prognosis, not mechanism.

**"98% inhibition is as good as it gets. Why not proceed?"**
That figure comes from co-addition, at ~41-fold molar excess, in non-lung endothelium from single donors, with reduced IL-33 only. It shows binding and neutralisation. It does not show potency, activity against oxidised IL-33, or reversal of an established response, and the last of these is the hospital scenario.

**"Why not pivot to COPD or asthma?"**
Nothing in our files supports it. Any such case would rest on external data, which is a separate decision with a different evidence base.

**"What if serum IL-33 is undetectable?"**
Release may be local to the lung. The serum bioassay and the lung-RNA signature are the back-up tests. If all three are negative, we kill the asset.

**"Can we trust the transcriptomics at all?"**
Yes, for the conclusions drawn here. The SE problem affects p-values for about 130 of 26,210 genes. The neutralisation result rests on effect sizes that replicate across timepoints, cell types and antibody reversal. The refit from archived counts is Stage 0.

**"What does the gate cost?"**
Stages 0–1 are re-analysis plus in vitro work on banked serum, archived RNA and existing blocks. No new patient sampling is needed before the gate.

# Appendix A. How the numbers were produced

**Transcriptomics**

- All contrasts come from one fitted model, so additional contrasts were derived as linear combinations of the delivered log2FCs:
  - IL-33 + isotype vs vehicle = (IL-33 vs vehicle) + (IL-33 + AX-1177 vs IL-33) − (IL-33 + AX-1177 vs IL-33 + isotype)
  - IL-33 + AX-1177 vs vehicle = (IL-33 vs vehicle) + (IL-33 + AX-1177 vs IL-33)
- **Inhibition** = 1 − (AX-1177 arm / isotype arm) on the log2 scale, for genes induced >4-fold with q < 0.05 in both the IL-33 and IL-33 + isotype arms.
- **SE** = logFC / t.
- **Off-target checks** used p-value distributions and cross-timepoint and cross-cell-line overlap.
- **26-gene core signature:** genes induced ≥4-fold at 6 h and at 24 h, ≥80% inhibited at both, reversed ≥2-fold in HGMEC at 6 h, and with median SE < 2.

**Serum proteomics**

- Olink assay names were mapped to HGNC symbols with a manual alias table (for example TF→F3, TM→THBD, ST2→IL1RL1, PAI→SERPINE1, OPG→TNFRSF11B).
- Assays were deduplicated to proteins, keeping the most significant assay; conclusions are unchanged using the least significant.
- GO localisation came from org.Hs.eg.db, excluding IEA annotations.
- Category tests used Fisher's exact test against the deduplicated background.
- The implied number of tests in the BH adjustment was computed as m = p × rank / q.

**Lung IHC**

- Block scores were averaged to donor level. Results were robust to using the median, the first block, the minimum or the maximum instead.
- Tests were Mann–Whitney, Kruskal–Wallis and Spearman.

**Tools:** Python (pandas, SciPy, statsmodels, matplotlib) and R (msigdbr, org.Hs.eg.db).

# Appendix B. Files

- `AX-1177_portfolio_audit_memo.md` / `.docx`: this memo.
- `figures/Fig1_invitro_neutralisation.png`, `Fig2_serum_proteomics.png`, `Fig3_lung_IHC_donor_level.png`, `Fig4_data_integrity.png`.
- `tables/AX-1177_supporting_tables.xlsx`, with these sheets: biomarker shortlist; the 152-gene IL-33 endothelial programme with serum links; the 26-gene core signature; all 1,094 Olink assays mapped and categorised; cross-panel duplicates; IHC donor-level data and tests; contrast summary; data-integrity log.
- `tables/biomarker_shortlist.csv`, `tables/data_integrity_log.csv`.
- `analysis_code/`: scripts that regenerate every figure and table from the four delivered files.

![Post-mortem lung IHC at donor level: IL-33 is abundant in every group and shows no COVID- or pneumonia-specific increase, while granulocyte markers track pneumonia of any cause.](figures/Fig3_lung_IHC_donor_level.png)
