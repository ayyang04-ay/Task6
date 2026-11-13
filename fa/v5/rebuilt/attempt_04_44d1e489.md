# AX-1177 (anti-IL-33 IgG1): portfolio audit recommendation and forward view

**Basis:** the four delivered files only: `AX-1177_rnaseq_huvec_il33.xlsx`, `AX-1177_rnaseq_contrasts.xlsx`, `AX-1177_serum_proteomics.xlsx`, `AX-1177_postmortem_lung.xlsx`, plus `AX-1177_methods_annex.pdf`. Every number below comes from these files. The few statements that rely on outside knowledge are marked *(external)*.
**Supporting material:** Figures 1–6 (`figures/`), `AX-1177_supporting_tables.xlsx` (8 sheets), analysis code (`code/`).

---

## 1. Bottom line

**Recommendation: KEEP the asset; DROP the indication as currently framed. This is a conditional, stage-gated keep with pre-agreed kill criteria.**

| | |
|---|---|
| **What our data defend** | AX-1177 is a potent, specific and clean neutraliser of IL-33 signalling in human endothelium. At 6 h it reverses a median **98%** of the 645 genes induced by IL-33, while the isotype control reverses a median **1%**. It shows no reproducible off-target activity in four cell types. |
| **What our data do not defend** | That IL-33 drives *severe lower respiratory viral infection*. We have no measurement of IL-33 itself in patients. Lung IL-33 is not increased in COVID-19. The in vitro IL-33 programme is no more linked to clinical severity than a random set of proteins. All patient data are from one virus (SARS-CoV-2), one pre-vaccination centre and one timepoint. |
| **What the data point at** | An endothelial mechanism, not a type-2 or airway one: IL-33 drives a thrombo-inflammatory activation programme in endothelium. The matching patient phenotype is endothelial injury with high soluble ST2 (sST2) at admission in hospitalised viral pneumonia. Our only evidence for it is in COVID-19. |
| **What we ask the committee to fund** | **Gate 1 only** (about 4 months), run mostly on samples and data we already own: retrieve the 100 withheld proteomic results (very likely including IL-33); measure free and total IL-33 in the same 100 biobanked sera; refit the RNA-seq; re-adjudicate the post-mortem set. **No IND-enabling spend** until Gate 1 passes. |
| **Kill criterion** | If IL-33 (free or complexed) is undetectable at enrolment, or is unrelated to outcome and to the endothelial IL-33 score, we drop or out-license. |

**If the committee chooses to drop now, here is what we would be dropping, and why.**
- *What:* a human IgG1 that (per the annex) binds reduced and oxidised IL-33 and neutralises a median 98% of the reduced-IL-33-induced programme in HUVEC at 6 h, reverses the same genes in a second vascular bed (HGMEC), and has a clean specificity profile.
- *What we would not be dropping:* a validated disease hypothesis. We don't have one, in the current indication or any other.
- *Why drop:* no evidence that IL-33, rather than broader IL-1-family, neutrophil and tissue-damage inflammation, drives severity. The "binds oxidised IL-33" differentiator has never been tested functionally.
- *Why I still recommend keep:* the decisive experiment is cheap and in-house. The withheld data very likely include the target ligand: IL-33 is on the panel that was run but is absent from the delivery. They also include at least three FDR-significant severity associations that we have not seen.

---

## 2. The case, in five findings

### Finding 1: The molecule works, specifically (strongest evidence; Figures 1 and 6)
- **Strong IL-33 response:** reduced IL-33 (30 ng/mL, about 1.7 nM) induces a large NF-κB programme in HUVEC.
  - 645 genes are induced (FDR < 0.05, log2FC > 1) at 6 h and 314 at 24 h.
  - The top Hallmark set is *TNFα signalling via NF-κB*: 90 of its 196 genes are in the 6 h core set.
- **Near-complete, specific neutralisation:** AX-1177 at 10 µg/mL, added together with IL-33 (no pre-incubation):
  - reverses a median **98%** of induced genes at 6 h (regression slope −0.96) and **84%** at 24 h (slope −0.84);
  - the isotype IC119 has no effect at 6 h (slope +0.01; median 1% reversal).
  - At 24 h the isotype shows a small non-specific effect (median 16%). Measured against the isotype arm, AX-1177 still inhibits a median 85%.
- **A 427-gene AX-1177-reversible core programme** (6 h), including:
  - myelopoietic/neutrophil-recruiting: GM-CSF/CSF2 +10.3 log2 (119% inhibition), G-CSF/CSF3 +8.3 (99%), CXCL6 +9.4 (86%), CXCL2, CXCL3, CXCL5, CCL20 +9.2 (106%), IL-6 +5.8 (102%), TNF, IL-1α/β;
  - adhesion: ICAM1 +6.0 (98%);
  - pro-coagulant: tissue factor/F3 +5.6 (q = 2e-26), PAI-1/SERPINE1 +1.7 (q = 8e-23), uPA/PLAU +1.5, thrombomodulin/THBD −1.0 (q = 2e-10);
  - complement: C3 +4.8, CFB +3.9;
  - OPG/TNFRSF11B +4.8 (100%).
  - At 24 h, the tight-junction gene occludin is repressed (−1.0, q = 9e-7) and restored by AX-1177.
- **Second vascular bed:** the same genes are reversed in glomerular microvascular endothelium (HGMEC). At 6 h, 59% of the core genes are reversed at FDR < 0.05, and reversal tracks the HUVEC values (ρ = 0.59).
- **No intrinsic activity:** AX-1177 alone vs isotype, PBS or DMSO gives 14–73 nominal FDR hits per contrast. None are reproducible: 0–1 genes overlap between independent timepoints or between cell lines, which is chance level. They are low-count lncRNAs or statistical artefacts.

### Finding 2: The IL-33 pathway is engaged in severe disease, but only through its decoy receptor (Figure 3)
- **sST2 is the #2 prognostic protein of 1,094** for ICU/ventilation/death within 30 days. Soluble ST2 is the IL-33 decoy receptor.
  - OR 3.02 (1.83–5.01) per log unit, q = 0.0075, adjusted for age, sex and NEWS2.
  - Cohort: 100 hospitalised COVID-19 patients, 44 events.
- **Four IL-33-inducible, AX-1177-reversible endothelial products are also prognostic:**
  - OPG: OR 6.8 (q = 0.014) and 4.4 (q = 0.020), replicated on two panels;
  - CCL20: OR 1.83 (q = 0.020);
  - IL-6: OR 2.1–2.3, replicated on four panels (q ≤ 0.019);
  - IL-18R1: OR 6.1 (q = 0.018).
- **Endothelial-injury markers track outcome:** vWF q = 0.050, ANGPT2 q = 0.052, E-selectin p = 0.022, PAI-1 p = 0.048.

### Finding 3: Nothing in our data shows that IL-33 itself drives severity (Figures 4 and 5)
- **IL-33 was not delivered.** The ligand is absent from the proteomics, although it is an analyte on the Olink Target 96 Inflammation panel *(external: vendor panel content)* (see Section 8).
- **The in vitro programme does not single out severe patients.**
  - Of 67 mapped core proteins, 19% are FDR-significant for severity, versus 17% of all other proteins (Fisher OR 1.16, p = 0.62; permutation p = 0.37).
  - The null holds under every definition I tried (OR 1.1–1.3, p 0.41–0.79).
  - The strongest in vitro products are not prognostic: G-CSF, CXCL6, CX3CL1, TNF, CXCL10, CXCL5, VCAM1 and ICAM1 are all non-significant (q 0.16–0.98).
  - Only a weak global concordance exists (ρ = 0.14 across 912 proteins), consistent with shared NF-κB biology.
  - *Caveat:* this compares in vitro transcripts in HUVEC with serum proteins that come from all tissues. The null weakens an IL-33 contribution but does not exclude one.
- **The severe phenotype is generic inflammation.**
  - 82% of all proteins have OR > 1.
  - The IL-1-family receptors IL-1R2 and IL-18R1 (q = 0.018 each) and the neutrophil-granule proteins PRTN3, CD177 and LCN2 (q = 0.02–0.03) are as prognostic as sST2.
  - Neither the top serum hit (HGF) nor the vWF/ANGPT2 markers respond to IL-33 in vitro.
- **Lung tissue IL-33 is not increased in COVID-19** (donor level, 16 vs 15 donors).
  - Basal epithelium: p = 0.70.
  - Endothelium and vascular smooth muscle trend *lower* (p = 0.075 and 0.084). This is largely explained by age (ρ = 0.57 with age; age-adjusted p = 0.10 and 0.11).
  - IL-33 is constitutive and near ceiling in the endothelium of controls.
  - *Caveat:* IHC measures *stored* (nuclear) IL-33, and release lowers staining. So the tissue data cannot show IL-33 activity either way. The downward vascular trend fits release, but age explains it.

### Finding 4: No type-2 signal anywhere, so a type-2 or eosinophil thesis is off the table
- **Serum:** IL-5 OR 1.00 (p = 1.0). Eotaxin-1 and -2, TARC, tryptase and KIT are all null (p ≥ 0.39).
- **Lung, donor level:** eosinophil peroxidase, EDN and MBP do not differ by COVID status (p = 0.43, 0.13, 0.56). IL-33 does not correlate with eosinophils.

### Finding 5: The data have integrity problems that limit what can be claimed (Section 8 and Figure 2)
The claims in this memo survive these problems. Claims made by anyone reading the raw deliverables naïvely would not, for example:
- "SELE/VCAM1/ST2 are not IL-33 targets";
- "about 4,000 IL-33 genes";
- "eosinophils are increased in COVID lungs (p = 0.0006)".

---

## 3. What indication do our data actually point at?

**A mechanism and a phenotype, not a new disease area.**
- **Mechanism:** IL-33 acting on endothelium. The effect is a thrombo-inflammatory activation programme: neutrophil chemokines, GM-/G-CSF, adhesion, tissue factor/PAI-1 up, thrombomodulin down, complement, barrier loss. AX-1177 reverses it.
- **Patient phenotype:** endothelial injury (vWF, ANGPT2, OPG, E-selectin) with a high IL-33 decoy receptor (sST2) at admission, which predicts ICU/ventilation/death. The post-mortem COVID-19 lungs are consistent: 7 of 16 donors had diffuse alveolar damage or acute lung injury, and 4 had thrombo-emboli.
- **Most defensible indication statement:** *"hospitalised viral pneumonia at high risk of progression, enriched by sST2 at admission, with an endotheliopathy mechanism."* We have evidence for this **only in pre-vaccination COVID-19**. The broad class label "severe lower respiratory viral infection" is not supported, because influenza, RSV and other viruses are untested.
- **Why this is not a repurposing:**
  - Type-2/eosinophilic disease (asthma, eosinophilic indications): contradicted.
  - COPD: not supported. We have no epithelial IL-33 pharmacology, and tissue IL-33 is unrelated to COPD or asthma history (p = 0.22–0.94).
  - Renal vascular disease: HGMEC in vitro only, with no vehicle arm.
  - Cardiovascular: NT-proBNP and troponin are not FDR-significant.
  - A move to any of these would be a decision based on outside data, not ours.

---

## 4. Forward view: what the next studies have to establish

Timelines are indicative planning assumptions, not derived from data.

| Gate | Must establish | Key activities | Go / no-go |
|---|---|---|---|
| **1 (0–4 mo; mostly in-house)** | That **IL-33 itself** is present at admission and linked to outcome and to the endothelial IL-33 response | (a) Retrieve all 1,194 Olink results (expected to include IL-33) with NPX/LOD/missingness; re-analyse per protein with per-SD ORs, adding eGFR and days from onset. (b) Free IL-33, total IL-33 and IL-33:sST2 complexes in the **100 biobanked enrolment sera**. (c) Per-cell-type RNA-seq refit from archived counts (valid statistics for SELE, VCAM1, CXCL8, PTX3, ST2). (d) Re-adjudicate post-mortem labels; blinded second reader; donor-level, age-adjusted analysis; request the 22 tissue-RNA samples. | **Go:** IL-33 detectable in a meaningful fraction, and associated with outcome beyond NEWS2 and sST2, **and** correlated with an IL-33 endothelial score (OPG + CCL20 + IL-6, plus SELE/PTX3 if the refit confirms them). **No-go:** undetectable, or unrelated to outcome and score, then drop or out-license. |
| **2 (4–10 mo)** | Potency that supports a dose; the oxidised-IL-33 differentiator; a therapeutic window; IL-33 specificity; the epithelium-to-endothelium link in virus infection | Primary lung microvascular EC from ≥3 donors, reduced and oxidised IL-33, 8-point dose–response (IC50/IC90). AX-1177 pre-incubated vs concurrent vs added 1/3/6 h after IL-33. Comparator arms: IL-1β, TNF, poly(I:C)/IFN-β, virus-conditioned epithelial medium; anti-ST2. Primary bronchial ALI ± influenza/RSV/SARS-CoV-2 ± AX-1177: IL-33 release, then conditioned-medium transfer to EC. | **Go:** IC90 reachable at projected lung exposure; activity against oxidised IL-33; an IL-33-specific readout defined; meaningful inhibition with delayed addition. **No-go:** activity collapses when the antibody follows IL-33. |
| **3 (10–18 mo)** | In vivo benefit without impairing viral control | Surrogate anti-IL-33 in a viral pneumonia model. Readouts: vascular leak, lung injury, survival, viral load, antiviral T cells. Prophylactic vs delayed dosing. | **Go to IND-enabling** only with efficacy on lung injury and unimpaired viral control. |

**Why "impairing viral control" is a gate:**
- At 24 h, IL-33 induces interferon-stimulated genes in endothelium: CXCL10, MX2, IFIT1, OASL.
- These partly escape AX-1177: CXCL10 51% and MX2 36% inhibition, versus about 100% for the primary NF-κB genes.
- What blocking them means for antiviral defence is untested.

---

## 5. Biomarkers, sampling timepoint, and which markers can go into patients

**Sampling timepoint**
- **In patients: admission/enrolment, before dosing.** This is the only timepoint at which our associations exist.
  - It is also when an early-release alarmin is most likely to be present.
  - In vitro, with antibody added at the same time as IL-33, neutralisation is 98% at 6 h but 84% at 24 h, and interferon-stimulated genes partly escape. This fits early signalling before the antibody captures IL-33.
  - Whether adding the antibody *after* IL-33 still works is untested (Gate 2). Until then, design for early dosing, with sampling before it.
- **First on-treatment PD sample at 24 h.** In vitro, OPG, CCL20 and IL-6 remain IL-33-dependent and fully AX-1177-reversible at 24 h (102–115% inhibition), while many primary transcripts have decayed. Follow with day 3 and day 7.
- **In vitro/ex vivo assays:** transcripts at **6 h** (the primary, maximally reversible response); secreted proteins at **24 h**.

| Marker | Role in patients | Basis in our data |
|---|---|---|
| **sST2** (serum) | **Yes: prognostic enrichment/stratification at enrolment.** Not a PD marker; not proof of IL-33 activity. | #2/1,094; OR 3.02, q = 0.0075, NEWS2-adjusted |
| **OPG, CCL20, IL-6** (± IL-18R1) (serum) | **Yes: exploratory PD/response panel** (baseline, 24 h, D3, D7), plus prognostic covariates | Induced by IL-33, about 100% reversed by AX-1177 at 6 h and 24 h, and prognostic (q ≤ 0.02); IL-6 and OPG replicate across panels. IL-6 is the least specific. |
| **Total IL-33** (drug-bound); **free IL-33; IL-33:sST2 complex** | **Yes, once assays exist: target engagement** (total IL-33 should rise), and mechanism confirmation or selection if detectable pre-dose | Absent from our data. This is the critical gap (Gate 1b). |
| **E-selectin, PTX3, IL-8** | **Later:** PD candidates once the refit validates them | Very large in vitro IL-33 effects reversed by AX-1177, but the delivered P values are invalid; serum SELE p = 0.022, PTX3 q = 0.012, IL-8 q = 0.023 |
| **vWF, ANGPT2** | **Stratification only** (endotheliopathy covariate); **not PD** | Prognostic, but not IL-33 transcriptional targets |
| **GM-CSF, G-CSF, CXCL6, CX3CL1, TNF, CXCL10** | **No.** In vitro potency/bioassay and ex vivo PD only | Best in vitro markers, but not prognostic in serum (or, for GM-CSF, not measured) |
| **Type-2 markers; lung IL-33 IHC** | **No** | Null; IHC needs tissue and sits at ceiling |

---

## 6. What I considered and ruled out

| Option / hypothesis | Verdict | Why (our data) |
|---|---|---|
| Continue in "severe lower respiratory viral infection" as framed | Ruled out as framed | COVID-19-only, pre-vaccination, single centre; IL-33 unmeasured; tissue IL-33 not increased; programme not enriched among severity proteins |
| Type-2/eosinophilic mechanism in viral LRTI | Ruled out | IL-5, eotaxins, TARC, tryptase, KIT null; tissue EPX/EDN/MBP unchanged (donor level) |
| Reposition to COPD/asthma | Not supported by our data | No epithelial IL-33 arm (A549/MCF7 never got IL-33); tissue IL-33 unrelated to COPD/asthma history |
| Reposition to glomerular/renal vascular disease | Not supported | HGMEC in vitro only (one donor, no vehicle arm); no patient data |
| Reposition to cardiovascular disease (sST2 is an HF marker) | Not supported | NT-proBNP and troponin not FDR-significant |
| sST2 as proof of IL-33 activity, or as a PD marker | Ruled out | A decoy induced by many stimuli; rises alongside IL-1R2 and IL-18R1 |
| AX-1177 off-target/agonist activity | Ruled out (favourable) | 0–1 antibody-alone genes replicate across timepoints or cell lines |
| Isotype/Fc effects explaining the neutralisation | Ruled out | Isotype slope +0.01 on IL-33-induced genes |
| "About 4,000 IL-33-regulated genes" | Ruled out | Repressed genes are restored by the isotype too (artefact); the attributable programme is 427 induced genes |
| Block-level post-mortem statistics | Ruled out | Pseudo-replication; effects vanish at donor level or after age adjustment |
| Ranking serum markers by OR magnitude | Ruled out | Per-log-unit ORs are scale-dependent (CSF-1 OR 90, CI 4–1,933) |
| HGF (top serum hit), vWF or ANGPT2 as IL-33 PD markers | Ruled out | Not IL-33-responsive in HUVEC |
| Drop the asset now | Not recommended | Asset quality is high; the decisive evidence is cheap and in-house |

---

## 7. Challenges the committee will raise, and the answers

- **"The in vitro data are overwhelming. Isn't that enough?"**
  They prove AX-1177 neutralises reduced IL-33 in endothelium at a single, high concentration (about 41-fold molar excess). They say nothing about potency (single dose) or about whether IL-33 is present in patients, and that is the open question.
- **"sST2 is a top hit. Doesn't that validate the target?"**
  No. sST2 is the IL-33 *decoy* receptor, produced in response to many stimuli, and it rises alongside other IL-1-family decoys and receptors. High sST2 may equally mean IL-33 is already being buffered. Only measuring IL-33 (Gate 1b) resolves this.
- **"Why are E-selectin and VCAM1 not significant, when IL-33 should induce them?"**
  It's an artefact of the model. In the single pooled limma fit, their gene-wise SEs are 7–9 log2 units (CXCL1: about 1,100), which is impossible for real replicate variance. Their fold changes are huge (+11.2 and +8.7 log2) and fully reversed. A refit is required before anyone cites their P values (Figure 2).
- **"The block-level data show eosinophils and IL-33 loss in COVID lungs."**
  That result comes from pseudo-replication: three donors contribute 24 of the 49 COVID+ blocks. At donor level, and after adjusting for age, the effects are not significant.
- **"Why not go to COPD, where the field is moving?"** *(external context: other anti-IL-33/ST2 agents are in late-stage COPD development)*
  A crowded field is a reason for caution, not a rationale. More importantly, none of our data test IL-33 in epithelium or associate IL-33 with COPD.
- **"Pre-vaccination COVID-19 isn't today's patient."**
  Agreed. That is why the indication claim is bounded, and why Gate 3 and the clinical design are multi-virus and contemporary.
- **"Is blocking an alarmin during infection safe?"**
  Untested. IL-33 induces interferon-stimulated genes in endothelium that AX-1177 only partly blocks at 24 h. Viral control is therefore an explicit Gate 3 criterion.

---

## 8. Data-integrity findings the committee should know (details: supporting tables, sheet 1)

**RNA-seq**
1. **Inflated SEs from the single pooled model.** The model pools four very different cell types. 121 genes have median SE > 3 log2 units (typical 0.34), including SELE, VCAM1, CXCL8, CXCL1, ST2/IL1RL1, CDH5 and VWF, so their P values are meaningless. Other genes have implausibly small SEs (AKR1C2 t = 169 for log2FC 0.11), which creates spurious hits.
2. **Mislabelled sheets.** Sheets "6h" and "24h" each contain all 24 contrasts at both timepoints (identical values). No rows are lost, despite the 1,048,576-row sheet dimension.
3. **Reference-arm label conflict:** "Nontreated" vs "Vehicle".
4. **No HGMEC vehicle arm.**
5. **Epithelial lines never received IL-33;** MCF7 is a breast line; DMSO is not a vehicle for an IgG.
6. **Thin design:** single donors; a single antibody concentration; no pre-incubation; reduced IL-33 only.
7. **IL-33-repressed genes are an artefact of the IL-33-alone arm** (restored by the isotype too).

**Serum proteomics**
8. **100 analysed assays were withheld.** The reported adjusted p-values imply BH over **1,194** tests, against 1,094 delivered (exact from the top-ranked assay). Reconstruction places at least 3 undelivered assays at FDR < 0.05 (p ≈ 0.0003, 0.0011, 0.0055) and about 15 at p < 0.05.
   - IL-33 is absent. So are IL-4, IL-13, TSLP and IL-1α. All are Inflammation-panel analytes *(external: vendor panel content)*.
   - The annex's statement that BH was applied "across all assays in the delivery" is therefore incorrect.
9. **Duplicate counting.** 27 proteins are measured on more than one panel (58 rows; IL-6 ×4) and are counted separately: 178 significant rows are 169 proteins. The duplicates are concordant.
10. **ORs are not comparable across proteins.** They are "per log unit" with the base unspecified, on data (NPX) that are already log2.
11. **Undocumented columns:** `composite_endpoint_0/1` (k/56 and k/44; probably the fraction below LOD).
12. **Analysis limits:** no adjustment for renal function or symptom duration; a single timepoint; 82% of ORs > 1.

**Post-mortem lung**
13. **Pseudo-replication:** 74 blocks from 31 donors.
14. **Labels disagree with the pathology text for 8 of 31 donors.**
    - 4 of 10 "COVID-neg pneumonia" donors have no pneumonia recorded.
    - 2 of 5 "non-pneumonia" controls do have pneumonia or pneumonitis, and one control has pulmonary coccidioidomycosis.
    - 2 of 16 COVID+ donors have no acute pneumonia.
    - One donor has no SARS-CoV-2 result.
15. **Score problems.** Scores reach 5.5 on a documented 0–5 scale. Numeric columns use an undocumented transform. IL-33 scores are identical across every block in about half of multi-block donors. There is a ceiling effect and a single reader.
16. **Age confounds vascular IL-33** (ρ = 0.57). The cohort is end-stage, elderly and entirely white.

---

### Appendix: how the key numbers were derived
- **Gene-wise SE** = |logFC / t| per row.
  - The implied residual df is 85.1 (76 residual + about 9 prior), consistent with 114 libraries and 38 groups.
  - AveExpr and annotation are constant per gene across all 26 contrasts. The two RNA-seq workbooks come from one fit.
- **Group means relative to vehicle** use additivity of contrasts within one fitted model, for example (IL-33 + AX-1177) vs vehicle = (IL-33 vs vehicle) + (IL-33 + AX-1177 vs IL-33). The isotype effect is the difference between the two AX-1177 contrasts.
- **Core programme** (6 h: 427 induced genes; 24 h: 140) requires all of:
  - IL-33 vs vehicle FDR < 0.05 and |log2FC| > 1;
  - AX-1177 reversal at FDR < 0.05 vs both IL-33 alone and IL-33 + isotype;
  - an isotype effect below 50% of the IL-33 effect.
- **Olink mapping:** names were mapped to HGNC symbols (912 of 1,063 proteins map to genes present in the RNA-seq). Duplicates were collapsed to the most significant assay. Enrichment used Fisher's test and 5,000 size-matched permutations.
- **Withheld assays:** BH back-calculation m = adj.p × rank / p. "Anchor" rows, where the adjusted value is not a running minimum, give each delivered assay's rank among the 1,194.
- **Post-mortem:** donor medians across blocks; Mann–Whitney tests; rank-regression and proportional-odds models for age adjustment. Groups were re-derived from the pathology text.
- **Pathway sets:** MSigDB Hallmark/Reactome (msigdbr 7.5.1, offline).
