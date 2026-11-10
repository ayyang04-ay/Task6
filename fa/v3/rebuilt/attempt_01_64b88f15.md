---
title: "AX-1177 (anti-IL-33 mAb): portfolio audit recommendation"
subtitle: "Evidence review of the delivered AX-1177 data package (methods annex, mmc2–mmc5)"
---

# 1. Bottom line

**Recommendation: KEEP AX-1177, but only as a re-scoped, gated asset. Stop the viral-LRTD programme as currently framed.**

**The molecule is validated in our data; the indication is not.**

- **The molecule works.**
  - AX-1177 (Compound_47) neutralises a large IL-33-driven inflammatory programme in endothelial cells (4,031 genes change at 6 h in HUVEC).
  - It removes about 100% of the strongest responses at 6 h and 94–97% at 24 h.
  - It reverses the same programme in glomerular microvascular endothelium.
  - It has no reproducible activity of its own in four cell types.
- **The IL-33 pathway is engaged in the patients who do badly.** Soluble ST2 (sST2), the IL-33 decoy receptor, is the #2 predictor of ICU admission, invasive ventilation or death among 1,063 serum proteins in hospitalised COVID-19. This holds after adjusting for age, sex and NEWS2.
- **Nothing in the package shows that IL-33 drives disease, in any population.**
  - There are no efficacy data.
  - The IL-33 programme we characterised in vitro is no more frequent among outcome-associated serum proteins than chance would predict.
  - Tissue IL-33 does not distinguish COVID from other pneumonia, or pneumonia from controls.
  - The only clinical cohort is single-centre, pre-vaccination SARS-CoV-2.

**Where the data point.** Not "viral LRTD" as a pathogen-defined class. They point to **severe, hospitalised acute lower respiratory infection at risk of progression to ICU, invasive ventilation or death, defined by host response (sST2-high, endothelial activation) rather than by pathogen.** No other indication is supported by our data. COPD/asthma, type-2 disease, kidney, sepsis and cardiovascular were each examined and ruled out as *data-driven* options (Section 7).

**What the next studies must establish** before any development spend:

1. IL-33 activity is actually present in the target patients. Patient serum/BAL should activate lung endothelium, AX-1177 should block that activation, and free IL-33 should be measurable.
2. sST2 keeps its independent prognostic value in a contemporary (post-vaccination), multi-pathogen cohort with serial sampling.
3. AX-1177 has potency in lung-relevant cells, and does not impair viral clearance.

Each has a pre-specified kill criterion (Section 5).

**If the committee prefers to drop**, this is what we would be dropping: a clean, functionally validated IL-33 neutraliser with a human prognostic pathway marker, but with no evidence that IL-33 is causal in any disease we have data on. No alternative indication is supported by our own data.

---

# 2. What is in the package

| Dataset | What it is | What it can and cannot tell us |
|---|---|---|
| In vitro RNA-seq (mmc4, mmc5) | HUVEC and HGMEC (single-donor primary endothelium) treated with reduced IL-33 (30 ng/mL) ± AX-1177 or isotype (NIP228, 10 µg/mL) for 6 h and 24 h. A549 and MCF7 epithelial lines given antibody only. n = 3 per arm; 114 libraries in one pooled limma model. | Can show neutralisation and specificity in endothelium. **Cannot** address epithelial IL-33 biology (epithelial lines were never given IL-33; MCF7 is breast), oxidised IL-33, lung endothelium, donor variability or potency (one dose, ~41-fold molar excess of antibody). |
| Serum proteomics (mmc2) | 100 hospitalised SARS-CoV-2 patients, single centre, pre-vaccination; serum at enrolment; 13 Olink panels (1,094 assays = 1,063 unique proteins). Logistic models for ICU/IMV/death within 30 days (44 events), adjusted for age, sex, NEWS2. | Association with outcome at one timepoint, in one virus. No validation cohort, no treatment data, no cut-offs. IL-33 itself not delivered. |
| Post-mortem lung (mmc3) | 31 donors, 74 blocks: 16 COVID+ pneumonia, 10 COVID− "pneumonia", 5 COVID− "non-pneumonia". Semi-quantitative IHC (single reader) for IL-33 in basal epithelium, endothelium and VSMC, plus eosinophil, neutrophil and mast-cell markers. | Where IL-33 protein is located in end-stage lung. Weak for group comparisons (labels, ceiling effects, n). No timing, treatment or outcome data. |

All analyses below were re-run from the delivered files at the correct unit of analysis: donors, not blocks; unique proteins, not assays. Genes with corrupted statistics were excluded (Section 8).

---

# 3. The case for keeping: the strongest defensible points

## 3.1 AX-1177 is a functionally validated IL-33 neutraliser (Fig. 1, Fig. 4)

**IL-33 response in HUVEC**
- IL-33 changes 4,031 genes at 6 h and 1,836 at 24 h (FDR < 0.05).
- The dominant programme is TNFα/NF-κB: Hallmark NES +3.15, padj 3×10⁻⁵⁹.
- Its content:
  - neutrophil-recruiting chemokines and growth factors: CXCL1/2/3/5/6/8, G-CSF (CSF3) +8.3 log2, GM-CSF (CSF2) +10.3;
  - cytokines: IL-6 +5.8, TNF +7.9, IL-1β +3.6;
  - adhesion molecules: ICAM1 +6.0 (E-selectin and VCAM-1 effect sizes +11.2 and +8.7);
  - pro-coagulant genes: tissue factor (F3) +5.6, PAI-1, uPA;
  - an interferon-stimulated gene component.

**AX-1177 reverses it**
- **Strongest targets (|log2FC| ≥ 5):** 37 genes at 6 h, median blockade 101% vs isotype + IL-33 (99.6% vs IL-33 alone). 9 genes at 24 h, median 94% (97%).
- **All IL-33-responsive genes:** median blockade vs IL-33 alone is 92% at 6 h and 78% at 24h.
  - The isotype-matched median is lower (78% at 6 h, 48% at 24 h). This is because the isotype arm itself dampened the IL-33 response (slope −0.2 to −0.3) and weak targets are noisy.
  - The two comparisons therefore bracket the truth. The lower 24 h figure is **not** loss of neutralisation.
- **Stringent set-up:** the antibody was added at the same time as IL-33, with no pre-incubation.

**The same programme is reversed in glomerular microvascular endothelium (HGMEC)**
- 1,460 genes at 6 h, FDR < 0.05.
- Hallmark TNFα/NF-κB NES −3.61, padj 6×10⁻⁶².
- Core targets: G-CSF −6.5, CCL20 −5.6, CX3CL1 −5.0, TNFRSF9 −5.0, CXCL5 −4.4.
- So the effect is not specific to one vascular bed.

**No intrinsic activity**
- AX-1177 alone vs isotype gives 21–73 "significant" genes per contrast.
- These are mostly low-count noise: at most one gene is shared between timepoints within a cell line, and one across cell lines.
- At pathway level, AX-1177 alone produces only small shifts in inflammatory/interferon sets. They run in opposite directions by cell type: NES +1.4 to +1.7 in HGMEC, −1.4 to −1.6 in HUVEC at 24 h. For comparison, the IL-33 signal is about ±3.
- So there is no agonist or off-target signature. The small HGMEC shift should be re-checked in the repeat experiment.

![**Fig. 1.** AX-1177 neutralises the IL-33-driven endothelial programme. A–C: each point is a gene; x = IL-33 response in HUVEC; y = effect of AX-1177 vs isotype in the presence of IL-33; dashed line = complete blockade. D: DE-gene counts per contrast.](figures/Fig1_AX1177_neutralises_IL33_endothelial_programme.png)

## 3.2 The IL-33 pathway marker is among the strongest prognostic signals in hospitalised patients (Fig. 2)

**sST2**
- OR 3.02 per log unit (95% CI 1.83–5.01), p = 1.7×10⁻⁵, FDR q = 0.0075.
- Wald z = 4.3: rank 2 of 1,063 unique proteins, behind only HGF.
- Adjusted for NEWS2 at enrolment, so the association is not explained by the bedside severity score. Incremental discrimination (AUC, reclassification) is not reported and needs patient-level data.
- NT-proBNP is only weakly associated (q = 0.15 and 0.33 on two panels), so the sST2 signal is not simply a cardiac-strain proxy.

**IL-33-inducible endothelial outputs that are also prognostic in serum**
- IL-6: OR 2.1–2.3 on four panels, q ≤ 0.02.
- OPG (TNFRSF11B):
  - in vitro: IL-33 +4.8 log2, reversed in both endothelial lines;
  - in serum: OR 6.8 and 4.4 on two independent panels, q = 0.014 and 0.02.
- CCL20: q = 0.02.
- MCP-3: q = 0.02.
- IL-18R1: q = 0.018.
- IL-1β: q = 0.046.
- Tissue factor: q = 0.051.

**The type-2 axis is flat**
- IL-5 OR 1.00; eotaxin-1 and eotaxin-2 OR 0.92–1.08; TARC 0.85; tryptase 1.07.
- So the severity-linked biology is not eosinophilic. That matches what we showed AX-1177 blocks in vitro: endothelial and neutrophilic inflammation.

![**Fig. 2.** Serum proteome vs ICU/IMV/death in 100 hospitalised COVID-19 patients. A: volcano of 1,063 unique proteins. B: IL-33-programme proteins are not over-represented among outcome-associated proteins. C: selected proteins.](figures/Fig2_serum_proteomics_sST2_and_IL33_programme.png)

## 3.3 IL-33 is located where the mechanism acts (Fig. 3)

- IL-33 protein is abundant in lung endothelium in every donor, near the top of the scale, and in basal airway epithelium.
- At donor level, endothelial IL-33 staining is **lower** in lungs with acute inflammation of any cause (p = 0.028).
- It also falls as neutrophil infiltration rises (Spearman ρ = −0.43, p = 0.016).
- This fits, but does not prove, release of the alarmin from endothelial stores during acute lung injury. It is coherent with the neutrophil-recruiting programme in 3.1.

![**Fig. 3.** Post-mortem lung at donor level. IL-33 IHC does not separate groups; endothelial IL-33 is lower where neutrophils and acute inflammation are higher; open circles = label not supported by autopsy text; F: pseudo-replication risk.](figures/Fig3_postmortem_lung_donor_level.png)

## 3.4 The key uncertainty is cheap to resolve

- The decisive questions in Section 5 can largely be answered with materials we already hold:
  - archived count matrices and the fitted model;
  - banked sera from the 100-patient cohort (stored at −80 °C per the annex; residual volume to be confirmed);
  - tissue RNA already extracted from 22 blocks (22 donors).
- These answers should come before any in vivo or clinical commitment.

---

# 4. The case against, and how the recommendation handles it

| Challenge | What our data show | How the recommendation handles it |
|---|---|---|
| "There is no efficacy evidence." | Correct. No in vivo, infection-model or clinical-intervention data. | No development spend until Gate 1 passes (Section 5). |
| "The in vitro IL-33 programme doesn't explain patient severity." | Correct. IL-33-induced, AX-1177-reversed genes are as often outcome-associated as any other protein: 19% vs 17%, Fisher p = 0.62. This holds under every definition tested (p = 0.14–0.99). The most robust sustained IL-33 outputs (G-CSF, CXCL5, CXCL6, KYNU, TNFRSF9) are **not** prognostic. | This is the central gap. Gate 1 tests it directly: does patient material drive AX-1177-sensitive endothelial activation? We do not claim IL-6, CCL20 etc. as a "mechanistic bridge": those overlaps are what chance predicts. |
| "sST2 is a generic marker." | Partly true. 82% of proteins have OR > 1 (a broad severity shift). Other IL-1-family receptors are also prognostic (IL-1R2 OR 4.5, IL-18R1 OR 6.1). | sST2 is used only for prognostic enrichment, which our data support, not as proof of mechanism or as a target-engagement marker. |
| "It's one virus, pre-vaccination." | Correct. The only clinical data are SARS-CoV-2, pre-vaccination, one centre, 44 events. | Indication re-scoped to a host-response-defined population. Gate 2 requires validation in a contemporary, multi-pathogen cohort. |
| "Tissue IL-33 isn't disease-specific." | Correct. At donor level, IL-33 scores do not differ across the three groups (Kruskal–Wallis p = 0.11 endothelium, 0.16 VSMC, 0.65 epithelium). Granulocyte infiltrates mark pneumonia of any cause, not COVID (COVID+ vs COVID− pneumonia: all eosinophil, basophil, IL-5Rα, neutrophil and mast-cell scores p ≥ 0.35). | Tissue is used only as a consistency check, which also argues against a virus-specific thesis. |
| "Blocking IL-33 could harm antiviral defence." | IL-33 induces an interferon-stimulated gene component in endothelium (MX1/MX2, IFIT1-3, RSAD2, GBP5, CXCL10, IDO1; +2 to +7 log2; Hallmark IFN-α NES +2.7), and AX-1177 removes it. | Viral load and viral clearance become mandatory safety endpoints (Gate 3 and any trial). |
| "The data package has quality problems." | Yes (Section 8). In vitro statistics are corrupted for ~130 genes, including the hallmark endothelial genes and ST2. ~100 serum assays were tested but not delivered. 9/31 tissue donors have labels contradicted by their own autopsy. | Gate 0 fixes these first. None of the conclusions above rests on the affected genes, assays or block-level statistics. |

**What not to claim in committee:**
- that AX-1177 has shown efficacy;
- that IL-33 drives COVID or viral LRTD severity;
- that IL-33 induces E-selectin, VCAM-1, IL-8 or ST2 "significantly" (the delivered statistics for these genes are unusable);
- any potency or dose figure;
- any sST2 cut-off;
- that AX-1177 acts on airway epithelium (never tested).

---

# 5. Forward view: indication, gates and kill criteria

## 5.1 The indication the data point at

**Severe, hospitalised acute lower respiratory tract infection at risk of progression to ICU, invasive ventilation or death, enriched for high sST2 (host-response-defined, pathogen-agnostic).**

- **Narrower than "viral LRTD":**
  - hospitalised, high-risk patients only;
  - our outcome signal is in patients already sick enough to be admitted (44% event rate);
  - we have nothing on outpatient or early disease.
- **Broader in aetiology:**
  - the mechanism we demonstrated is endothelial and has no pathogen component;
  - tissue shows the same IL-33 and neutrophil picture in COVID-negative pneumonia.
- **Only SARS-CoV-2 has direct human evidence.** Extension to influenza, RSV or bacterial pneumonia is a hypothesis that Gate 2 must test.

## 5.2 Gated plan

| Gate | What must be established | How (using existing material first) | Kill or redirect criterion |
|---|---|---|---|
| **0. Data remediation** | That the evidence base is sound. | (a) Re-derive the RNA-seq statistics from the archived counts: sample-identity QC, inspect raw counts of affected genes, fit per cell line. Extract the missing contrasts (HGMEC IL-33 response, isotype vs vehicle). (b) Obtain the full serum output, including the ~100 undelivered assays and IL-33 itself. (c) Re-adjudicate tissue labels against autopsy text; blinded two-reader re-scoring. | Kill if the HUVEC IL-33 programme and its AX-1177 reversal do not reproduce on re-analysis. |
| **1. Is there active IL-33 in the target patients?** (decisive) | That patient material contains IL-33 activity that AX-1177 blocks. | (a) Stimulate primary human **lung microvascular** endothelium (≥3 donors) with sera/BAL from sST2-high vs sST2-low patients ± AX-1177 vs isotype. Read out the endothelial IL-33 panel at **6 h**. (b) Measure free and total IL-33 (reduced and oxidised) in banked enrolment sera and relate them to sST2 and outcome. (c) Profile the existing tissue RNA for the endothelial IL-33 signature vs endothelial IL-33 IHC. | Kill the respiratory indication if sST2-high patient material does not produce AX-1177-sensitive endothelial activation **and** IL-33 is not elevated in poor-outcome patients. |
| **2. Is the population real today?** | That sST2 keeps independent prognostic value in current patients and across pathogens. | Prospective or banked contemporary cohort: post-vaccination SARS-CoV-2, influenza, RSV, bacterial CAP. Serial sampling (admission, ~24 h, day 3, day 7). Pre-register an sST2 cut-off derived from the patient-level data of the original cohort. | Drop the enrichment strategy (and likely the indication) if sST2 adds no information over NEWS2 in the contemporary cohort. |
| **3. Lung-relevant pharmacology and safety** | Potency, breadth and antiviral safety. | Dose–response (IC50) with and without pre-incubation. Reduced **and** oxidised IL-33. Primary airway epithelium (ALI) as well as lung endothelium. In vivo infection model with a cross-reactive reagent (species cross-reactivity is in the biologics file, not this package), with viral load as an endpoint. | Drop viral indications if IL-33 blockade impairs viral clearance. |
| **Then** | — | Biomarker-enriched (sST2-high) phase 1b/2a in hospitalised severe LRTI, with PD and viral-load safety. | — |

---

# 6. Biomarkers, roles in patients and sampling timepoint

## 6.1 Proposed markers

Full evidence for each marker is in `tables/AX-1177_supporting_tables.xlsx`, sheet *Biomarker_candidates*.

| Marker | Role in patients | Use now? | Evidence (our data) | Key caveat |
|---|---|---|---|---|
| **sST2** | **Prognostic enrichment / stratification** at enrolment. Predictive value to be tested by stratified randomisation. | **Yes**, as a stratifier or enrichment criterion. | #2 of 1,063 proteins; OR 3.02 (1.83–5.01), adjusted for age, sex and NEWS2. | Not target engagement (AX-1177 binds IL-33, not ST2). No cut-off derivable from summary data. Single cohort. |
| **HGF** | Prognostic covariate (risk adjustment). | Yes, as a covariate. | #1 protein; replicated on two panels (OR 4.99 and 4.84). | Not IL-33-induced in vitro (log2FC +0.5, n.s.). Says nothing about AX-1177 pharmacology. |
| **Free / total IL-33** | **Target engagement** (free IL-33 falls and total rises with drug binding). | Needs assay build. | Absent from delivery; the vendor Inflammation panel normally carries it. | Drug-tolerant assay required. Low circulating levels expected. |
| **Endothelial IL-33 output panel:** OPG, CCL20, G-CSF, CXCL5, CXCL6, KYNU, tissue factor (IL-6 secondary) | **Pharmacodynamic / proof of mechanism**: change from baseline vs placebo. | After Gates 0–1 (lock the panel on the lung-endothelium data first). | All IL-33-induced and AX-1177-reversed in HUVEC and HGMEC. OPG, CCL20 and tissue factor are also prognostic. G-CSF, CXCL5, CXCL6 and KYNU are sustained to 24 h. | All have non-endothelial sources in vivo. IL-6 is confounded by standard of care (IL-6R blockade raises it; steroids suppress it). Plasma preferred for platelet-rich CXCL5. |
| **Viral load + ISG panel** (MX1, IFIT1–3, RSAD2, CXCL10) | **Safety**. | Yes, in any viral-infection study. | IL-33 drives an endothelial ISG component that AX-1177 removes. | Endothelial ISGs are a small part of antiviral defence; in vivo relevance unknown. |
| E-selectin, VCAM-1, IL-8, MCP-1, PTX3 | Hold. | No, until re-analysed. | Large effect sizes with full reversal, but delivered statistics are unusable. | Re-derive first (Gate 0). |
| Type-2 markers; tissue IL-33 IHC | None. | No. | Null vs outcome; non-discriminating in tissue. | — |

![**Fig. 4.** Candidate PD markers: IL-33 induction (6 h, 24 h), AX-1177 reversal in HUVEC and HGMEC, and serum outcome association (Wald z). Below the line: delivered statistics unusable; effect sizes only.](figures/Fig4_PD_marker_candidates_kinetics.png)

## 6.2 Sampling timepoint

**Patients.** The recommended timepoint is **enrolment, before study drug, within the admission window in which NEWS2 is scored.**
- It is the only timepoint at which our serum data have outcome information (serum at enrolment; models adjusted for NEWS2 at enrolment).
- It is the right timepoint for the enrichment marker (sST2) and the prognostic covariate (HGF).
- It also serves as the PD baseline.

**Experiments.** The primary PD readout for the next in vitro and ex vivo work is **6 h** after IL-33 or patient-material exposure, with 24 h as secondary.
- At 6 h the IL-33 programme is broadest: 4,031 vs 1,836 genes at 24 h.
- AX-1177 reversal is maximal in both endothelial beds at 6 h. In HGMEC it is largely gone by 24 h: median reversal of HUVEC's strong targets −2.2 log2 at 6 h vs −0.3 at 24 h.
- 886 IL-33 targets are 6 h-only (including TNF and tissue factor); 181 are sustained.

**On-treatment PD in patients.** IL-33 release cannot be timed, so use the **sustained** outputs (G-CSF, CXCL5, CXCL6, KYNU, CCL20, OPG) rather than transient ones (TNF, tissue factor). Sample pre-dose, then at about 24 h, day 3 and day 7.
- Those in vivo times are a design proposal for the first study to refine. They are extrapolated from in vitro kinetics and not validated.

---

# 7. What I considered and ruled out

## 7.1 Indications

| Option | Verdict | Why (our data) |
|---|---|---|
| Viral LRTD as currently framed (pathogen-defined, broad) | **Not supported as framed** | Only pre-vaccination SARS-CoV-2 in serum. Tissue IL-33 and granulocyte infiltrates do not differ between COVID+ and COVID− pneumonia. No data on other viruses, early or outpatient disease, or efficacy. |
| Severe COVID-19 as a standalone indication | Not recommended | It is the only population with human data, but the cohort is pre-vaccination. The severity proteome is a broad non-specific shift. Today's hospitalised COVID population and standard of care differ. Keep it as one stratum of the re-scoped indication. |
| COPD / asthma (epithelial, type-2 IL-33) | **Ruled out as data-driven** | No epithelial IL-33 challenge anywhere in the package (A549/MCF7 antibody-only; MCF7 is breast). Tissue IL-33 and eosinophil scores do not differ by COPD/asthma history (12 vs 19 donors, p = 0.12–0.97). Serum type-2 markers null. Would be a bet on external evidence, not ours. |
| Type-2 / eosinophilic mechanism in pneumonia | **Ruled out** | IL-5, eotaxins, TARC and tryptase null vs outcome. Tissue eosinophils, IL-5Rα+ cells and tryptase do not separate COVID+ from COVID− pneumonia. |
| Kidney (DKD/AKI), prompted by the HGMEC arm | **Ruled out as data-driven** | HGMEC shows AX-1177 works on glomerular endothelium, but there are no kidney-disease data. Serum kidney markers are not associated after adjustment (KIM-1 q = 0.11/0.18, renin q = 0.18, cystatin C q = 0.34). |
| Sepsis / systemic endotheliopathy | Hypothesis only; not recommended now | Two vascular beds respond to IL-33, and endothelial injury markers are prognostic (vWF q = 0.05, ANGPT2 q = 0.05, PTX3 q = 0.012, OPG q = 0.014). But there are no sepsis data, and it is a high-attrition indication. Revisit only if Gate 1 is strongly positive. |
| Cardiovascular (sST2 as a cardiac marker) | **Ruled out** | No cardiac data. NT-proBNP is only weakly associated, so the sST2 signal is not a cardiac-strain proxy. A prognostic marker does not imply benefit from blocking its ligand. |

## 7.2 Claims and analyses rejected

- **Using logFC rankings without statistics.** E-selectin (+11.2 log2), VCAM-1 (+8.7) and IL-8 (+8.2) top the IL-33 list by fold change, but their delivered statistics are corrupted (SE 4 to >1,000). They cannot be cited as significant.
- **"178 proteins predict outcome."** The count is inflated by cross-panel duplicates: 27 proteins are measured on 2–4 panels (IL-6 four times in the top 30). It also sits on a generic shift in which 82% of proteins have OR > 1. Proteins are ranked here by Wald z, not by ORs, which are numerically unstable per log unit (e.g. CSF-1 OR 90, CI 4–1,933).
- **Cherry-picking overlaps** (IL-6, CCL20) as mechanistic proof. The overall enrichment test is null.
- **sST2 as a PD or target-engagement marker.** Wrong target, and IL1RL1 is not evaluable in vitro.
- **IL-6 as primary PD.** Non-specific and confounded by standard of care.
- **HGF as an IL-33 marker.** Not IL-33-induced in vitro.
- **Block-level tissue statistics.** They create false positives (IL-5Rα COVID+ vs COVID− pneumonia p = 0.025 by block vs 0.49 by donor). Three donors supply 24 of 49 COVID+ blocks.
- **AveExpr as a per-cell-line expression filter.** It is averaged over all four cell lines.
- **Reading the 24 h drop in blockade as loss of efficacy.** The strongest targets are still about 94–97% blocked.
- **Reading the C47 vs DMSO contrasts as informative.** DMSO is not an antibody vehicle.
- **Any potency claim.** One concentration at ~41-fold molar excess (68.5 nM antibody vs 1.66 nM IL-33).

---

# 8. Data-integrity findings the committee should know

Full log in the workbook, sheet *Data_integrity_log*; summary in Fig. 5.

1. **In vitro statistics are corrupted for a subset of genes.**
   - About 115–190 genes per contrast have standard errors of 2 to 16,536 log2 units (typical is 0.1–1). 82 genes are affected in all 26 contrasts.
   - These are not possible for log-expression data. They include GAPDH, the endothelial identity genes (VWF, CDH5, CD93), **IL1RL1/ST2**, E-selectin, VCAM-1, IL-8, MCP-1 and PTX3.
   - The opposite artefact appears in a few very abundant genes (AKR1C2: t = 169 for a 0.11 log2 change).
   - The rate rises steeply with transcript abundance (0.1% of genes in the bottom half, 12.5% in the top 1%). This is consistent with an upstream count-processing or sample-identity problem, propagated by a single pooled model across four unrelated cell lines.
   - Conclusions here use only well-behaved genes.
2. **The in vitro delivery is incomplete.**
   - It omits the HGMEC IL-33 response (HGMEC has no vehicle arm), IL-33 vs isotype, and isotype vs vehicle.
   - The "6h" and "24h" sheets of mmc5 are saved filters; both contain all 24 contrasts.
3. **Serum results were selectively delivered.**
   - The adjusted p-values imply Benjamini–Hochberg over **1,194 tests**; 1,094 were delivered, and the annex says the adjustment was over the delivered assays.
   - About 100 tested assays are missing, about 5 of them with p < 0.01.
   - IL-33, which the vendor's Inflammation panel normally includes, is not in the delivery (77 of 92 Inflammation assays delivered).
   - Two columns (composite_endpoint_0/1) are undocumented. Their values are per-group fractions of 56 and 44 patients, probably missing or below-LOD rates.
4. **Tissue labels are unreliable.** 9 of 31 donors carry a group label their own autopsy diagnosis does not support:
   - 3/5 "non-pneumonia" controls have acute pneumonia, pneumonitis or pulmonary coccidioidomycosis;
   - 4/10 "COVID− pneumonia" and 2/16 "COVID+ pneumonia" have no acute pneumonia recorded;
   - one donor lacks a SARS-CoV-2 result.
   - Scoring issues: the numeric scores run to 5.5 on a stated 0–5 scale ("n+" coded as n + 0.5); one score is a spreadsheet formula; there is a single reader; and endothelial IL-33 sits at the ceiling.

---

![**Fig. 5.** Data integrity. A: implausible standard errors concentrate in the most abundant transcripts. B: sentinel genes. C: serum FDR computed over 1,194 tests vs 1,094 delivered.](figures/Fig5_data_integrity.png)

# 9. Methods (brief)

**Concordance checks**
- The delivered tables were checked for internal consistency: t vs P vs adjusted P vs SE for RNA-seq; Wald p vs CI and BH reconstruction for serum.
- The two mmc5 sheets were confirmed identical in content.

**In vitro**
- IL-33 response: HUVEC IL-33 vs vehicle.
- Neutralisation: AX-1177 + IL-33 vs isotype + IL-33, and vs IL-33 alone. Reported as regression slopes and as % blockade (−reversal / induction).
- IL-33-responsive genes: FDR < 0.05, |log2FC| > 1, SE < 2.
- Hallmark fgsea on moderated t, excluding genes with SE pathology.

**Serum**
- Assays mapped to gene symbols and collapsed to unique proteins (best assay per protein).
- Overlap of the in vitro programme with outcome-associated proteins tested by Fisher and Mann–Whitney tests.

**Tissue**
- Blocks aggregated to donor means.
- Ordinal scores analysed with rank-based tests (Kruskal–Wallis, Mann–Whitney, Spearman).
- Labels cross-checked against autopsy text.
- p-values are nominal and exploratory.

**Evidence base**
- Only the delivered files were used as evidence.
- Where the files contradict themselves (impossible standard errors, the BH test count, labels vs autopsy text), the problem is flagged rather than interpreted.
- General domain knowledge is used only for caveats, never as evidence for the recommendation. Examples: standard-of-care effects on serum IL-6; platelets as a CXCL5 source; the vendor's usual panel content.

All code is in `code/`.

## Files

- `AX-1177_portfolio_audit_memo.md` / `.docx` / `.html`: this memo.
- `figures/Fig1`: AX-1177 neutralisation of the IL-33 endothelial programme.
- `figures/Fig2`: serum proteome, sST2, enrichment test, forest plot.
- `figures/Fig3`: post-mortem lung at donor level.
- `figures/Fig4`: PD-marker candidates (kinetics, reversal, outcome association).
- `figures/Fig5`: data integrity.
- `tables/AX-1177_supporting_tables.xlsx`: biomarker candidates, unique serum proteins, the in vitro IL-33 programme, SE-pathology genes, donor-level tissue data and tests, Hallmark GSEA, data-integrity log.
- `tables/key_numbers.json`: every number quoted in this memo, regenerated from the data.
