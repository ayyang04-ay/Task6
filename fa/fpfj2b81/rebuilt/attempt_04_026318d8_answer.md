**Recommendation: NOT YET. Do not move AX-1177 into IND-enabling or clinical work on this package. Instead, fund a 12-month, three-gate de-risking plan (fix and complete the existing data → test the antibody in human lung cells under viral infection → run an in vivo proof of concept in two viruses with dosing after infection, and validate the biomarker in an independent cohort), with stop rules agreed in advance.**

# AX-1177 (anti-IL-33) for viral lower respiratory tract disease (LRTD): proposal to the Programme Committee

*Basis:* this proposal uses only the mounted package: `AX-1177_methods_annex.md`, `mmc2.xlsx` (serum proteomics), `mmc3.xlsx` (post-mortem lung), `mmc4.xlsx`/`mmc5.xlsx` (RNA-seq contrasts). I computed every number cited here from those files. Scripts and result tables are in `/tmp/outputs/analysis/` and figures in `/tmp/outputs/figures/`. Anything under "plan" or "design" is a proposal or assumption. None of it is a result.

---

## 1. Summary for the committee

**What the package supports**

1. **The antibody neutralises IL-33 in a dish.** The test was in human umbilical-vein endothelial cells (HUVEC) from a single donor.
   - Reduced IL-33 (IL-33red, 30 ng/mL) changes expression of 4,031 genes at 6 h (adj.P<0.05); 1,068 of them change ≥2-fold. The response is dominated by NF-κB, chemokine and interferon-stimulated genes.
   - The test article, Compound_47 (10 µg/mL, about a 41-fold molar excess), reverses **96%** of the 303 most robust IL-33 genes at 6 h when compared with the isotype control. The regression slope is −0.92 (95% CI −0.95 to −0.88). At 24 h the reversal falls to **78%**.
   - Compound_47 on its own produces no reproducible transcriptional signature in any of the four cell types tested.
2. **There is a prognostic serum signal on the IL-33 axis.**
   - Soluble ST2 (sST2), the decoy receptor for IL-33, ranks 2nd of 1,094 serum assays as a predictor of ICU admission, invasive ventilation or death by day 30.
   - The cohort is 100 patients hospitalised with SARS-CoV-2.
   - OR 3.02 per log unit (95% CI 1.83–5.01), adj.p 0.0075, adjusted for age, sex and NEWS2 (an early-warning severity score).

**What the package does not support: the links a clinical decision depends on**

3. **No evidence that IL-33 is increased in the diseased lung.**
   - Analysed correctly (per donor, not per block), IL-33 immunostaining is **not higher** in COVID-19 lungs.
   - Endothelial and vascular smooth-muscle IL-33 are, if anything, **lower**: donor-mean differences of −0.44 and −0.72 score units, p≈0.04–0.07.
   - None of five sensitivity analyses shows an increase.
4. **The IL-33 ligand itself is absent from the delivered serum data.**
   - The sST2 signal is not specific: 376 of 384 nominally significant assays (98%) point the same way.
   - Genes induced by IL-33 in vitro are **not enriched** among serum proteins that predict outcome (19% vs 17%, Fisher p=0.75).
5. **Large gaps:**
   - No viral infection anywhere in the package.
   - No lung endothelium and no primary airway epithelium.
   - No testing of oxidised IL-33 (IL-33ox), no concentration–response, no in vivo work, no pharmacokinetics (PK), no safety data and no target-engagement assay.
   - The package does not document that "Compound_47" is AX-1177.
6. **Data-integrity problems that must be fixed before any of this is relied on:**
   - **RNA-seq:** for about 130–180 genes the delivered statistics carry impossible standard errors. These include the core endothelial-activation genes SELE (E-selectin), VCAM1, CXCL8, CCL2 and CXCL1, and IL1RL1 (the ST2 receptor). For example, SELE shows a log2 fold change of +11.2 with p=0.21.
   - **Proteomics:** the FDR correction was run over 1,194 tests, but only 1,094 results were delivered. The 100 missing results include 4 that passed the study's own FDR<0.05 cut-off.
   - **Post-mortem:** the 74 tissue blocks come from only 31 donors, and 3 donors supply 24 of the 49 COVID+ blocks. IL-33 scores go above the documented 0–5 scale. For 9 of 31 donors, the group label contradicts the donor's own autopsy diagnosis.

**Decision logic.** The package shows that the molecule can neutralise IL-33. It does not show that neutralising IL-33 would change the course of viral LRTD: it neither confirms nor refutes that hypothesis. A "Go" therefore cannot be defended, and a "Stop" would be premature.

Gate 0 is the cheapest step that can change the decision. It needs no new wet-lab work: obtain the withheld data, confirm the identity of the test article and re-analyse what exists.

---

## 2. Evidence map: each link a clinical programme needs

| # | Link required | What the package shows (source) | Status |
|---|---|---|---|
| 1 | Drug neutralises human IL-33 | 96% (6 h) / 78% (24 h) reversal of the core IL-33red programme in HUVEC (mmc4+mmc5). Limits: one concentration, one donor, IL-33red only, no affinity/potency data (annex §1), Compound_47 not linked to AX-1177. | **Partly shown (in vitro, narrow)** |
| 2 | Drug is specific | No gene changed by Compound_47 vs isotype in ≥3 of 8 cell-line × time contrasts; 79–100% of the "hits" are noise (mmc5) | Partly shown (transcript level only) |
| 3 | IL-33 drives a pathogenic endothelial programme | 1,068-gene NF-κB/chemokine/ISG (interferon-stimulated gene) response in HUVEC. Limits: umbilical vein, not lung; one donor (mmc4) | Partly shown |
| 4 | IL-33 is present or released in the diseased human lung | Post-mortem staining not increased in COVID+; endothelium and smooth muscle lower. Release, extracellular IL-33 and ST2 were not measured (mmc3) | **Not shown** |
| 5 | IL-33 axis tracks clinical severity | sST2 prognostic (OR 3.02 per log unit), but the ligand was not delivered and the signal is non-specific (mmc2) | Weak / indirect |
| 6 | Blocking IL-33 improves viral LRTD | No infection model, no in vivo study | **Absent** |
| 7 | Blocking IL-33 is safe during active infection | No data. In HUVEC, IL-33 induces ISGs (CXCL10, MX1/2, IFIT1–3, RSAD2, OASL) and Compound_47 suppresses them (mmc4/5) | **Absent; risk flagged** |
| 8 | Dose rationale and target-engagement biomarker | No PK, no free/total IL-33 assay | **Absent** |
| 9 | Evidence extends beyond SARS-CoV-2 | All human data are SARS-CoV-2 (pre-vaccination, single centre; post-mortem) | **Absent** for "viral LRTD" |

---

## 3. Findings by dataset

### 3.1 In vitro pharmacology (mmc4, mmc5)

**Design (annex §2–3)**
- HUVEC (single donor, passage 2) and glomerular microvascular endothelial cells, HGMEC (single donor, passage 5); 6 h and 24 h; n=3 wells per arm.
- Compound_47 or the isotype control NIP228 (10 µg/mL = 68.5 nM) was added **at the same time** as IL-33red (30 ng/mL = 1.66 nM), with no pre-incubation.
- Molar ratio is 41:1 (83:1 counting both antibody binding sites).
- All 114 libraries were made in one batch on one flow cell, so there is no batch confounding.

**Consistency check.** All 26 contrasts share identical AveExpr values and a common residual df of 85.13 (76 residual + 9.1 prior). This is consistent with the annex's single-model statement, so logFCs can be combined arithmetically.

**IL-33red response and its neutralisation**

| | 6 h | 24 h |
|---|---|---|
| IL-33red vs vehicle, genes at adj.P<0.05 | 4,031 (2,191↑ / 1,840↓) | 1,836 (1,281↑ / 555↓) |
| … of which \|log2FC\| ≥ 1 | 1,068 | 512 |
| "Core" set (adj.P<1e-6, \|log2FC\| ≥ 1) | 303 (271↑ / 32↓) | 78 |
| Core: aggregate neutralisation vs IL-33+NIP228 | **96.0%** | **77.7%** |
| Core: slope of Compound_47 effect on IL-33 effect (95% CI) | −0.92 (−0.95 to −0.88) | −0.73 (−0.81 to −0.64) |
| Core: genes significantly reversed | 97.0% | 92.3% |
| Broad set (1,068 / 512 genes): aggregate / median per-gene neutralisation | 59.5% / 91% | 39.7% / 74% |

**Exemplar genes at 6 h** (IL-33 log2FC → Compound_47 vs isotype log2FC):

| Gene | IL-33 effect | Adj.P | Compound_47 vs isotype |
|---|---|---|---|
| CSF2 | +10.3 | 5×10⁻²³ | −12.2 |
| CXCL6 | +9.4 | | −8.1 |
| CCL20 | +9.2 | | −9.8 |
| CX3CL1 | +8.4 | | −8.7 |
| CSF3 | +8.3 | | −8.3 |
| TNF | +7.9 | | −7.7 |
| IL6 | +5.8 | | −6.0 |

The full table is in `03c_key_genes_table.csv`; the scatter plot is Fig. 1.

**How to read these numbers**
- **Reversal is measured against the isotype control, not against IL-33 alone.** The "Compound_47+IL-33 vs IL-33" contrast shares the IL-33 group with the contrast used to define the signature, so regression to the mean inflates it:
  - 6 h: 80% apparent reversal vs 60% against the isotype.
  - 24 h: 71% apparent reversal vs 40% against the isotype.
- **The broad-set estimate is biased low and the core-set estimate is less biased.** Selecting genes on significance biases the broad-set estimate downwards (winner's curse). The true value probably lies between 60% and 96% at 6 h.
- **Neutralisation is weaker at 24 h.** This fits incomplete capture when antibody and IL-33 are added together, or a secondary wave of signalling:
  - IL-33 induces ISGs at 24 h: GBP5 +4.7, MX2 +3.7, RSAD2 +2.6, IFIT1 +2.5.
  - Several are only partly reversed: OASL 16%, IFIT2 20%, RSAD2 34%, IFIT1 38%, CXCL10 43%, MX2 47%.
  - What happens to antiviral defence if this response is blocked during real infection has not been tested.
- **HGMEC responses cannot be quantified.** HGMEC have **no vehicle arm**, so the IL-33 response there cannot be measured. Compound_47 does suppress HUVEC core genes in HGMEC at 6 h (BIRC3 −8.8, CSF2 −7.1, CXCL3 −6.7, CSF3 −6.5 log2). But the HUVEC signature projects onto HGMEC with a slope of only −0.35 at 6 h and −0.13 at 24 h. That could mean a smaller IL-33 response or less complete neutralisation; the data cannot tell them apart.
- **No off-target transcriptional signal was detected.**
  - Compound_47 vs NIP228 gives 31/38 differentially expressed genes (DEGs) in HUVEC (6 h/24 h), 64/73 in HGMEC, 48/21 in A549 and 22/31 in MCF7.
  - 79–100% of these are near-zero-count noise (mean log-expression < 0 with \|log2FC\| ≥ 2) or <0.5 log2 shifts with implausibly small errors.
  - No gene recurs in ≥3 of the 8 contrasts, and the antibody-alone effect is uncorrelated with the IL-33 signature (r = 0.02 at 6 h, 0.06 at 24 h).
  - There is therefore no evidence of endogenous IL-33 tone or off-target transcription at 10 µg/mL (`06_antibody_alone_DEG_composition.csv`).
- **Design limits**
  - One donor per endothelial type: the n=3 are cultures from that one donor.
  - Neither endothelial type is lung.
  - One antibody concentration and one IL-33 concentration, so no IC50 and no dose rationale.
  - IL-33red only: the annex says Compound_47 binds IL-33ox, but that is not tested functionally, and affinity/potency data sit outside the package.
  - The epithelial lines were never exposed to IL-33. MCF7 is a breast line, and DMSO is not a relevant vehicle for an antibody.

### 3.2 The RNA-seq statistics are unreliable for a subset of key genes (Fig. 2)

- **Implied standard errors are impossible for some genes.**
  - SE = \|logFC/t\|. The median per-gene SE is 0.34 log2.
  - 130 genes have SE > 2, 97 have > 5 and 38 have > 20.
  - Examples: SELE 8.9, VCAM1 7.1, CXCL8 4.1, CCL2 5.7, IL1RL1 8.3, PTGS2 26, VWF 144, CDH5 926, CXCL1 1,155, CD93 16,536.
- **The same gene's SE varies enormously between contrasts.** In a single model it should not. 181 genes vary by >25-fold, and AKR1C2 varies by 2.3×10⁵-fold.
- **There is also the reverse problem.** AKR1C2 in A549 has a log2FC of 0.11 with t = 169 (adj.P 3×10⁻⁹⁴). That implies a replicate SD of ~0.0008 log2, below Poisson counting noise at any realistic sequencing depth.
- **An independent check on the B-statistics agrees.** The implied posterior residual SDs reach 10⁴–10⁵× those of the median gene: CD93 ~39,000×, XBP1 ~16,000×, GAPDH ~12,500× (`02b_Bstat_results.txt`).
- **Cell-identity genes of all four lines are the ones affected:**
  - Endothelial: VWF, CDH5, CD93, PECAM1, KDR.
  - A549: AKR1C2, ALDH3A1, NQO1.
  - MCF7: XBP1, GATA3, TFF1.
  - This matches the annex's single variance model forced across four unrelated cell types, or a sample-identity problem that the pooled fit spreads to every contrast.
  - The counts and the model object are withheld (annex §5), so the cause cannot be pinned down.
- **Consequences**
  - The delivered p-values cannot be used to assess E-selectin, VCAM-1, IL-8, MCP-1 or CXCL1, the genes most relevant to an "endothelial activation" thesis. Their point estimates show large induction (log2FC 4.2–11.2) and ~100% reversal, but without valid uncertainty.
  - AveExpr is averaged over all 114 libraries and says nothing about expression in any one cell line.
  - The robust core genes, whose SEs are normal (0.2–0.9), support the neutralisation conclusion. Even so, it needs confirmation from a per-cell-line re-fit.

### 3.3 Post-mortem lung IHC (mmc3; Fig. 3)

**Structure**
- 74 blocks from **31 donors**:
  - COVID+: 16 donors, 49 blocks; donors 2067, 2072 and 2073 contribute 8 blocks each (24 in total).
  - COVID− pneumonia: 10 donors, 15 blocks.
  - COVID− non-pneumonia: 5 donors, 10 blocks.
- All donors are white; median age 84 (range 64–98).
- Scored by a single reader.
- Within-donor correlation (ICC) is 0.40–0.64, so an 8-block donor carries only about 1.9 donors' worth of independent information. The donor is the correct unit of analysis.

| IL-33 compartment | Donor median, COVID+ (n=16) | Donor median, COVID− (n=15) | Donor-mean difference (bootstrap 95% CI) | p, donor-level Mann–Whitney | p, block-level (pseudo-replicated; not valid) |
|---|---|---|---|---|---|
| Basal airway epithelium | 4.25 | 4.75 | −0.09 (−0.60 to 0.46) | 0.76 | 0.33 |
| Endothelium | 4.81 | 5.50 | −0.44 (−0.84 to −0.06) | 0.052 (permutation 0.045) | 0.017 |
| Vascular smooth muscle | 2.38 | 3.25 | −0.72 (−1.38 to −0.09) | 0.068 (permutation 0.048) | 0.007 |

**Sensitivity analyses.** None shows higher IL-33 in COVID+ lungs (p = 0.08–0.92, `01_postmortem_sensitivity.csv`). They were:
- against labelled COVID− pneumonia only;
- pathology-confirmed pneumonia only;
- excluding the three 8-block donors;
- donor medians instead of means.

None of the borderline "lower" results survives correction for three compartments.

**Data problems**
- **Scale:** IL-33 values go above the documented 0–5 scale (annex §7). 39 of 74 endothelial blocks and 16 of 71 epithelial blocks score 5.5.
  - Endothelial IL-33 is therefore at ceiling in controls, which limits sensitivity to any increase.
  - The encoding is undocumented. For comparison, the eosinophil, neutrophil-elastase and tryptase "numeric" columns are exactly each "n+" score + 0.5.
  - Rank-based donor tests are used because they are robust to this.
- **Label conflicts with autopsy diagnoses (my reading of the delivered text, not a pathologist re-review):**
  - 4 of 10 "COVID− pneumonia" donors have no pneumonia listed (1905, 1961, 1968, 1970). Donor 1905 also has no SARS-CoV-2 result.
  - 3 of 5 "COVID− non-pneumonia" donors have pneumonia or pneumonitis: 1976, acute/organising pneumonia; 1956, acute pneumonitis; 1944, pulmonary coccidioidomycosis.
  - 2 of 16 COVID+ donors have no acute pneumonia, including 2067, which contributes 8 blocks.
- **Power:** with 16 vs 15 donors, the smallest detectable difference is about 1.04 SD.

**Reading.** IL-33 is constitutively abundant in lung endothelium and airway basal epithelium in every group. The data give no sign that disease raises it. Lower staining could reflect release, cell loss or nothing; IHC cannot measure release or bioactivity.

### 3.4 Serum proteomics (mmc2; Fig. 4)

**Cohort (annex §6).**
- 100 patients hospitalised with SARS-CoV-2; single centre; pre-vaccination.
- The per-group fraction columns have denominators of 56 and 44, which implies **44 events**. That gives about 11 events per parameter for the four-term models. The columns themselves are undefined in the annex.
- The reported p-values reproduce Wald p-values from the CIs exactly.

**IL-33 axis results**

| Assay | OR per log unit (95% CI) | Adj.p | Rank |
|---|---|---|---|
| ST2 | 3.02 (1.83–5.01) | 0.0075 | 2/1,094 |
| IL-1RT2 | 4.52 (1.95–10.47) | 0.018 | |
| IL-18R1 | 6.07 (2.23–16.53) | 0.018 | |
| RAGE (IL-33ox receptor) | 2.34 (0.98–5.56) | p=0.055 (unadjusted) | |
| EGFR | 1.16 (0.40–3.36) | p=0.78 (unadjusted) | |

**The IL-33 ligand is not among the delivered assays.** Only 77 of the Inflammation panel's 92 assays were delivered.

**Omitted results**
- For the top assay, adj.p/p equals exactly 1194.000, and 642 delivered rows map to exact integer ranks when M = 1,194. So the FDR adjustment covered **1,194 tests**, not "all assays in the delivery" (1,094) as the annex states.
- Among the 100 analysed-but-undelivered results:
  - 2 have p<0.002, 5 have p<0.01 and 15–16 have p<0.05;
  - **4 passed the study's own FDR<0.05**;
  - one would rank 19th–21st overall (adj.p ≈ 0.017).
- We cannot tell whether the IL-33 ligand is among them.

**Duplicates across panels**
- 27 proteins appear on more than one panel (58 assays). For example, IL-6 appears on 4 panels (OR 2.07–2.31) and HGF on 2 (4.99, 4.84). These are the same sera measured twice, which is technical concordance, not replication.
- The 178 FDR-significant assays correspond to 169 unique proteins.

**Specificity and scale**
- 98% of nominally significant assays have OR>1: the signal is broad "severity", not IL-33-specific.
- ORs are quoted "per log unit" on an unstated scale and are not standardised, so magnitudes cannot be compared across assays. For example, CALR 19.7 and CSF-1 90.1 reflect scale, not importance.
- sST2 is a decoy, so its rise does not say whether free IL-33 activity is higher or lower.
- sST2 is associated with outcome beyond NEWS2. That makes it a candidate stratifier, not evidence that IL-33 causes disease.

**Cross-walk between in vitro and clinic (`05_crosswalk_results.txt`)**
- 75 serum proteins correspond to genes induced by IL-33 in HUVEC at 6 h.
- 14 of them (19%) are prognostic, against 17% background (Fisher OR 1.10, p=0.75). The results at 24 h are similar.
- Proteins that are both IL-33-induced and Compound_47-reversed in vitro **and** prognostic: IL-6, OPG/TNFRSF11B, IL-18R1, CCL7/MCP-3, CCL20, IL-1β, CSF-1 and CTSS. These are candidate pharmacodynamic (PD) markers, but they are non-specific NF-κB products.
- Some of the strongest in vitro genes show no clinical association: CXCL6 OR 1.02, TNFRSF9 1.09, G-CSF 1.25, CXCL10 1.30.

---

## 4. Integrity and methods register (must be closed at Gate 0)

| # | Issue | Evidence | Impact | Fix |
|---|---|---|---|---|
| R1 | Impossible RNA-seq SEs for ~130–180 genes | §3.2; SELE SE 8.9, CD93 16,536; 181 genes with >25-fold within-gene SE range | Key endothelial genes cannot be tested; spurious antibody-alone "hits" | Re-fit per cell line from the archived counts; check library identity (markers, sex genes, SNPs, PCA) |
| R2 | Test article identity | Annex §1 names "Compound_47"; the programme is AX-1177 | Evidence may not apply to the candidate | Confirm sequence/lot bridging; retrieve the biologics file |
| R3 | One donor per endothelial type; not lung | Annex §2 | No donor-to-donor variation captured; relevance to lung disease unknown | ≥4 donors of primary lung microvascular endothelial cells |
| R4 | HGMEC has no vehicle arm; key contrasts missing | Annex §3; mmc5 | IL-33 response in microvascular EC cannot be quantified | Deliver IL-33+NIP228 vs NIP228 and NIP228 vs vehicle; add a vehicle arm |
| R5 | Only IL-33red; one concentration; antibody added at the same time | Annex §1, §3 | No potency, no IL-33ox data, no therapeutic window | Concentration–response across IL-33 forms and addition schedules (Stage 1) |
| R6 | Serum FDR over 1,194 tests; 100 results withheld | §3.4 | Selective reporting; the ligand may be missing | Deliver all results with LOD/missingness |
| R7 | Cross-panel duplicates; OR scale unstated; columns undefined | §3.4 | Hit counts inflated; ORs cannot be compared | Reconcile by UniProt; report per-SD ORs; define the columns |
| R8 | Post-mortem pseudoreplication | 74 blocks from 31 donors; block-level p 0.017/0.007 vs donor-level 0.052/0.068 | False precision | Donor-level, pre-specified analysis |
| R9 | IL-33 scores above 5; ceiling; single reader | 39/74 endothelial blocks at 5.5 | Unknown reliability; cannot detect increases | Second blinded reader (weighted κ); documented scale; digital quantification |
| R10 | Group labels conflict with autopsy diagnoses | 9/31 donors | Misclassified comparison groups | Pathologist adjudication |
| R11 | File hygiene | mmc5 sheets "6h" and "24h" are identical and each holds both timepoints; "6h" is padded with blank rows to Excel's 1,048,576-row limit; mmc4 labels "Nontreated" vs annex "Vehicle"; annex "applies to" omits the post-mortem dataset | Risk of double counting and mislabelling | Fix and re-issue |

---

## 5. Proposed plan: what we measure, in which model, and when

Every stage below answers a specific gap from §2–4.

### Stage 0 — Fix and complete the existing package (months 0–2; no new wet lab) → **Gate 0**

**Activities**
- Confirm that Compound_47 is AX-1177. Retrieve KD for IL-33red, IL-33ox and full-length IL-33, plus cross-reactivity to cynomolgus and mouse IL-33. This determines both the in vivo strategy and the toxicology species.
- Re-fit the RNA-seq per cell line from the archived counts, with library-identity QC. Deliver the missing contrasts.
- Deliver all 1,194 analysed serum results, including IL-33 if it was run, with LOD information. Report per-SD ORs and how much sST2 adds beyond NEWS2 (change in AUC, calibration).
- Post-mortem: second blinded reader, documented scoring scale, pathologist adjudication of group labels. Run a targeted IL-33 / IL1RL1 / endothelial-activation panel on the **22 tissue RNAs already listed** in mmc3 (9 COVID+ and 13 COVID− donors).

**Go criteria**
- Identity confirmed.
- Core HUVEC signature and ≥80% neutralisation at 6 h reproduce in the per-line re-fit.
- Valid SEs obtained for SELE, VCAM1, ICAM1, CXCL8 and CCL2.

**Stop / reassess**
- Sample mislabelling confirmed: treat the transcriptomics as void.

### Stage 1 — Human lung-relevant pharmacology and infection biology (months 2–6) → **Gate 1**

| Question | Model | Measurements | Timepoints |
|---|---|---|---|
| Potency against each IL-33 form | Primary human lung microvascular EC, ≥4 donors (≥2 aged >60 y); primary bronchial or small-airway epithelium at air–liquid interface (ALI), ≥4 donors | IL-33red, IL-33ox and full-length IL-33 (0.1–30 ng/mL) × AX-1177 (0.001–30 µg/mL), with NIP228 as control. IC50/IC90 per form per donor. Core-signature panel (CSF2, CXCL6, CCL20, CSF3, CXCL2/3, TNF, IL6, CX3CL1, plus SELE, VCAM1, ICAM1, CXCL8). Secreted IL-6, GM-CSF, CCL20, IL-8, sICAM-1, sVCAM-1, E-selectin | Signalling at 15–60 min; transcripts at 6 h and 24 h (as in the package); barrier/impedance to 48 h |
| Therapeutic window | Same cells | Antibody added 30 min before, with, or 1, 4, 8 or 24 h after IL-33 | 6 h, 24 h |
| Is IL-33 released in viral infection, and does it matter? | ALI epithelium infected with SARS-CoV-2, influenza A and RSV; epithelium–endothelium transwell co-culture | IL-33 release (total, reduced/oxidised, full-length/processed) in apical and basolateral media. Endothelial activation and barrier ± AX-1177. **Safety:** viral titre, IFN-λ/β and ISGs | 0–96 h after infection |

**Go criteria**
- IC90 for the least-sensitive IL-33 form allows a ≥10-fold margin under projected free-drug exposure in lung epithelial lining fluid (ELF) at day 28.
- ≥80% inhibition of the core panel in **every** donor.
- In ≥2 of 3 viruses, infected epithelium releases IL-33 that activates lung EC in a way AX-1177 reverses.
- No increase in viral titre >0.5 log10 and no ≥50% loss of IFN-λ/β.

**Stop criterion**
- No AX-1177-reversible endothelial activation in infected co-culture for any virus.

**Design note.** With ≥4 donors, a donor-level paired analysis detects an effect of about 2.1 SD of donor-to-donor variation. Three donors would detect only about 3.3 SD, which is why 4–6 are specified.

### Stage 2 — In vivo proof of concept with clinically realistic timing (months 4–12) → **Gate 2**

**Prerequisite.** If AX-1177 does not bind mouse IL-33 (Stage 0), use a potency-matched anti-mouse IL-33 surrogate, qualified in a mouse EC assay, plus genetic confirmation (Il33⁻/⁻ or Il1rl1⁻/⁻) in one model.

**Models**
- Mouse-adapted SARS-CoV-2 in aged mice.
- Influenza A in C57BL/6.
- Optional: RSV in BALB/c.
- At least **two viruses** are required to support a "viral LRTD" label.

**Arms**
- Isotype control.
- Prophylactic: day −1.
- Early therapeutic: day +1.
- **Late therapeutic:** day +3, or at onset of weight loss. This is the clinically relevant arm.

**Timing.** Days 2, 4 and 7, plus 10–14 for resolution. Exact days are to be fixed by pilot kinetics.

**Endpoints and measures**
- **Primary:** BAL total protein or albumin at peak injury. This is vascular leak, which tests the endothelial hypothesis directly.
- **Secondary:** blinded histopathology score; weight-loss AUC; survival; SpO2/plethysmography; lung Sele, Vcam1, Icam1 and core-signature orthologues; BAL neutrophils; IL-6, GM-CSF, CXCL1, CCL20; serum sVCAM-1, E-selectin, Ang-2.
- **Target engagement / PK:** drug in serum and BAL; free vs total IL-33 in BAL.
- **Safety:** plaque-assay titres and time to clearance; secondary bacterial infection; repair (amphiregulin, epithelial proliferation); fibrosis at day 14–21.

**Design.** Randomised, blinded, with primary endpoint and analysis pre-registered. n=12 per arm per timepoint gives 80% power for an effect of 1.2 SD (α=0.05).

**Go criteria**
- Dosing at or after day +1 cuts the primary endpoint by ≥30% vs isotype (p<0.05) in **≥2 viruses**.
- ≥90% suppression of free IL-33 in BAL, with secondary endpoints moving the same way.
- Upper 95% CI for any viral-titre increase <0.5 log10.

**Stop criteria**
- No effect with therapeutic dosing in both viruses despite target engagement.
- Or any signal of impaired viral control.

### Stage 3 — Independent clinical biomarker validation (months 3–12, in parallel) → feeds **Gate 2**

- **Cohort:** prospective, multi-centre, hospitalised viral LRTD: SARS-CoV-2 (including vaccinated patients), influenza and RSV.
- **Sampling:** serum at admission, day 3 and day 7; BAL/ELF where clinically indicated.
- **Measures:** validated free and total IL-33 (by form), sST2, the cross-walk panel (IL-6, CCL20, OPG, IL-18R1, IL-1β, CCL7, CSF-1) and endothelial-injury markers (sVCAM-1, sICAM-1, E-selectin, vWF, Ang-2).
- **Outcome:** the same composite as mmc2.
- **Size:** n≈330–430, to detect OR 1.5 per SD with NEWS2 adjustment at 20–30% event rates.
- **Go criteria:**
  - sST2 (or IL-33) is prognostic at OR ≥1.5 per SD in ≥2 viruses;
  - free IL-33 is detectable (serum or ELF) in most severe cases.

### Timeline and decision points

| Gate | Month | Decision | Note |
|---|---|---|---|
| Gate 0 | 2 | Evidence usable? | Cheap; can stop or accelerate |
| Gate 1 | 6 | Human-relevant mechanism in infection? | |
| Gate 2 | 12 | Disease-modifying in vivo, and a validated biomarker? | Start IND-enabling work (GLP tox, CMC) only here |

Gate 2 is the only point at which IND-enabling spend should begin. First-in-human would then be at the earliest around months 21–24 (planning assumption).

---

## 6. What goes into the clinic (only if Gates 0–2 are passed)

- **Molecule:** AX-1177 with identity confirmed and documented potency against IL-33red, IL-33ox and full-length IL-33.
- **Nonclinical package:**
  - GLP toxicology in a cross-reactive species;
  - tissue cross-reactivity study;
  - PK;
  - the Stage 2 infection-safety data, including viral load.
- **Dose rationale:** a PK/PD model that keeps free IL-33 in lung ELF ≥90% suppressed through day 28 after a single IV dose. The in vitro 10 µg/mL (41:1 molar excess) is **not** a dose rationale.
- **First-in-human:** single ascending dose in healthy volunteers, covering safety, PK, immunogenicity and target engagement (free/total IL-33, drug–IL-33 complex).
- **Phase 1b/2a:**
  - Randomised, placebo-controlled, single IV dose on top of standard care.
  - Population: hospitalised adults with PCR-confirmed viral LRTD (SARS-CoV-2, influenza or RSV) on supplemental oxygen, not ventilated. Dosing within the Stage 2 window, provisionally ≤72 h from admission.
  - Stratified by virus and baseline sST2. This is pre-specified but **not an enrolment filter**: sST2 is prognostic and its predictive value is unproven.
  - Primary endpoints: safety, including viral-load kinetics; PD (free IL-33 suppression and endothelial-panel change from day 0 to day 7). That needs about 45–64 per arm for 0.5–0.6 SD.
  - Exploratory endpoints: the mmc2 composite (ICU/IMV/death by day 30) and oxygen-free days.
- **Scale the committee should expect.** A confirmatory trial on the composite, targeting a 25% relative reduction, needs:
  - about 306 per arm at the package's 44% event rate;
  - about 540–900 per arm at more contemporary 20–30% rates.

  That is why the biology must be de-risked first (`08_design_calculations.txt`).

---

## 7. What would change this recommendation

**Towards acceleration**
- Gate 0 shows that the withheld serum results include the IL-33 ligand, and that it is strongly and specifically prognostic.
- The per-line re-fit confirms blockade of E-selectin and VCAM-1 with valid uncertainty.
- In vivo or infection data exist elsewhere in the programme (none are in this package).

**Towards termination**
- Library-identity errors invalidate the transcriptomics.
- Infected human epithelium does not release bioactive IL-33.
- No effect in vivo with therapeutic dosing.
- Any sign of impaired viral control.

---

## 8. Analyses performed (reproducible; `/tmp/outputs/analysis/`)

| Script | Content |
|---|---|
| `01_postmortem_ihc.py` | Block vs donor analysis, mixed models, ICC, bootstrap, sensitivity and label/pathology audit, power |
| `02_rnaseq_integrity.py`, `02b_Bstat_implied_weights.py` | Single-model checks (AveExpr, df, BH), SE and B-statistic consistency |
| `03_rnaseq_efficacy.py` | IL-33 signature; Compound_47 reversal vs isotype; HGMEC projection; key-gene tables (`03b`, `03c`) |
| `04_proteomics.py` | Implied FDR test count, withheld-test bracketing, duplicate reconciliation, IL-33 axis, specificity |
| `05_crosswalk_invitro_serum.py` | In vitro IL-33 genes vs serum prognostic proteins (manual Olink→HGNC map; approximate) |
| `06_antibody_alone_offtarget.py` | Composition and reproducibility of antibody-alone DEGs |
| `07_figures.py` | Figures 1–4 |
| `08_design_calculations.py` | Molar ratio and sample sizes for the proposed studies (assumptions, not results) |

**Caveats on my own analyses**
- I had no counts, NPX values or images. So I could not re-fit the RNA-seq, standardise the ORs or re-score the IHC.
- Neutralisation estimates are exact for the group-means point estimates, but have no standard errors.
- The 44-event count and the 1,194-test count are inferences from the arithmetic, though they are tightly determined.
- The pathology re-classification is an analyst's reading.
