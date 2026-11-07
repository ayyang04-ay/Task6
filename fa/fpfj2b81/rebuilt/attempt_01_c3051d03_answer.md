# AX-1177 (anti-IL-33 mAb) in viral lower respiratory tract disease (vLRTD): programme committee proposal

**Recommendation: do not move AX-1177 into IND-enabling studies or the clinic on this package. Instead, approve a 9-month gated de-risking programme with pre-set stop rules. The first chance to stop early comes at month 3–4, and the full re-decision is at month 9.**

*Basis.* Everything here comes from the mounted package: the methods annex plus mmc2, mmc3, mmc4 and mmc5. Analysis scripts and result tables are in `/tmp/outputs/analysis/` (numbered 00–10, run in order), and figures are in `/tmp/outputs/figures/`. The annex calls the test article "Compound_47". I treat Compound_47 as AX-1177, but the package never documents that link, so it is item 0c in the plan.

---

## 1. Decision summary

**What the package shows (the in-vitro mechanism is solid)**
- **IL-33 strongly activates endothelial cells in vitro.** Reduced IL-33 (IL-33red) at 30 ng/mL (≈1.66 nM) switches on a large inflammatory (NF-κB) gene programme in HUVEC:
  - 4,031 genes change at FDR<5% at 6 h, and 1,836 at 24 h.
  - The Hallmark "TNFα signalling via NF-κB" gene set is strongly enriched (NES 3.12 at 6 h, 3.08 at 24 h; padj ≈10⁻¹⁹).
  - At 6 h the key genes rise sharply (log2 fold change): E-selectin (SELE) +11.2, GM-CSF (CSF2) +10.3, VCAM1 +8.7, CXCL8 +8.2, ICAM1 +6.0, IL6 +5.8.
- **Compound_47 abolishes that response.** It was used at 10 µg/mL (≈68.5 nM, a 41-fold molar excess over IL-33) and added at the same time as IL-33.
  - I measured blockade on cultures that were not used to choose the genes (see §3.1 for why this matters): **99%** (95% CI 94–104%) at 6 h and **93%** (86–100%) at 24 h.
  - With Compound_47 present, the IL-33-treated transcriptome looks like vehicle. The typical residual change is 0.17 log2, the same as the background noise between two antibody-only arms (0.17).
  - The isotype control antibody NIP228 does not affect the IL-33 response (−0.009 and −0.023 log2).
- **Compound_47 on its own does nothing reproducible.** Across 8 independent antibody-alone comparisons in 4 cell types there are 328 significant-gene calls, but only 3 genes recur, against 1.75 expected by chance. The hits are low-count, mostly non-coding transcripts, which looks like noise.

**What the package does not show (the disease link is not established)**
- **No evidence that IL-33 is present or raised in patients.**
  - IL-33 itself is not among the 1,094 serum assays delivered.
  - Post-mortem lung staining for stored IL-33 does not differ between COVID+ pneumonia, COVID− pneumonia and non-pneumonia lungs when analysed per donor (Kruskal–Wallis p = 0.65 for basal epithelium, 0.11 for endothelium, 0.16 for vascular smooth muscle). If anything, the trend is lower in COVID+ lungs.
- **No evidence that the IL-33 pathway is specifically linked to bad outcomes.**
  - Soluble ST2 (sST2, the IL-33 decoy receptor) is associated with ICU admission, mechanical ventilation (IMV) or death. The odds ratio is 3.02 per log unit (1.83–5.01), 2nd of 1,063 unique proteins.
  - But the whole serum proteome is shifted: **82% of all proteins have OR>1** (sign test p≈10⁻¹⁰¹).
  - Measured against that shifted background (an "empirical null"), sST2 is unremarkable (z = 2.07, p = 0.04), and no protein passes FDR 10%.
  - Serum proteins that correspond to the IL-33-induced, Compound_47-reversed endothelial genes are **not over-represented** among outcome-associated proteins: 69 proteins, 21.7% significant vs 19.5% of the rest; permutation p = 0.26.
- **Key pharmacology and safety data are absent:**
  - in-vivo efficacy, PK, and safety during infection;
  - potency (only one concentration tested);
  - any functional test on oxidised IL-33 (IL-33ox), even though dual-form binding is the annex's key property for the molecule;
  - activity against natural IL-33 released by virus-infected cells;
  - dosing after IL-33 exposure (the treatment setting for hospitalised patients);
  - lung endothelium, more than one donor per cell type, or any virus other than SARS-CoV-2.

**Integrity problems in the package that must be fixed before anyone relies on these data externally**
1. **RNA-seq statistics:** for 238 genes the reported standard errors are inflated a median 33-fold relative to their actual noise (e.g., CD93: reported SE 16,536 log2 vs an empirical 0.067).
   - The affected genes are mainly cell-type markers (44% of endothelial and 38% of epithelial markers, vs 0.9% of all genes) and the textbook IL-33 targets.
   - As a result, **SELE, VCAM1, CXCL8, CCL2 and IL1RL1 (the gene for ST2) are reported as not significant** (FDR 0.50, 0.51, 0.19, 0.77, 0.98) despite 2–11 log2 fold inductions.
   - This fits the annex's single model pooled across endothelial and cancer epithelial lines. The effect sizes, which all conclusions here rely on, are not affected.
2. **Serum proteomics:** the delivered multiple-testing adjustment (Benjamini–Hochberg, BH) only reproduces if **1,194 tests** were run. Only 1,094 are delivered, and **≥4 of the 100 missing tests were FDR-significant**. The annex says the adjustment covered "all assays in the delivery". IL-33 is not among the delivered assays.
3. **Pathology:**
   - 39 of 74 endothelial IL-33 scores are 5.5 on a stated 0–5 scale, and one score is a spreadsheet formula.
   - Three donors contribute 24 of the 49 COVID+ tissue blocks.
   - Counting blocks rather than donors inflates significance: block-level p = 0.012 becomes p = 0.11 when analysed per donor.

**Why I am not recommending termination.** The mechanism and specificity data are clean. The decisive open question — is IL-33 present and driving endothelial injury at the point when patients can be treated? — can be answered quickly and cheaply with material the programme already holds: 100 archived enrolment sera and 22 archived post-mortem lung RNA samples. That gives an early stop/continue read-out at month 3–4, before significant spend.

---

## 2. Evidence scorecard against the therapeutic hypothesis

*Hypothesis:* in vLRTD, IL-33 released from virus-damaged airway epithelium activates lung endothelium (adhesion molecules, chemokines, GM-CSF). That drives leukocyte recruitment, vascular leak and progression to ICU, IMV or death. Neutralising IL-33 (reduced and oxidised) after the patient presents prevents that progression.

| Step in the hypothesis | What the package shows | Key values | Status |
|---|---|---|---|
| 1. IL-33 is released or raised in vLRTD patients | Not measured. No IL-33 assay among the delivered serum data. IHC measures *stored* nuclear IL-33, and it is not increased | IL-33 absent from 1,094 assays; IHC donor-level p = 0.65 / 0.11 / 0.16 | **Not shown** |
| 2. IL-33 pathway activity tracks severity | sST2 is associated, but so is most of the proteome | sST2 OR 3.02 (1.83–5.01), rank 2/1,063; empirical-null z = 2.07 | **Weak, non-specific** |
| 3. IL-33 activates endothelium | Strong in HUVEC (one donor); Compound_47-suppressible programme in HGMEC, though HGMEC's own IL-33 response cannot be sized | 4,031 genes at 6 h; NF-κB NES 3.12; SELE +11.2 log2 | **Shown in vitro** |
| 4. That endothelial programme relates to outcome | Its serum protein counterparts are not enriched among outcome-associated proteins | 69 proteins; 21.7% vs 19.5%; permutation p = 0.26 | **Not shown** |
| 5. AX-1177 neutralises IL-33 | Yes, for recombinant IL-33red (residues 112–270) at 41× molar excess, added at the same time | 99% (94–104%) / 93% (86–100%) | **Shown, under narrow conditions** |
| 6. …including IL-33ox, other IL-33 forms, and IL-33 released in tissue | No data | — | **Not shown** |
| 7. Neutralising IL-33 *after* onset improves disease | No in-vivo data; no delayed-addition experiment | — | **Not shown** |
| 8. Safe in an infected host | Inert on its own in vitro. IL-33 turns on interferon-response genes in HUVEC (IFN-α NES 2.64, IFN-γ 2.79 at 6 h) and Compound_47 abolishes this, so impact on antiviral defence is a real question. No infection data | 3 recurrent hits vs 1.75 expected | **In-vitro only** |
| 9. Generalises beyond SARS-CoV-2 | All human data are SARS-CoV-2 (pre-vaccination serum) or COVID± autopsy | — | **Not shown** |

---

## 3. Findings by dataset

### 3.1 In-vitro transcriptomics (mmc4, mmc5)

**Design (from the annex).**
- Two endothelial cell types: HUVEC (umbilical vein, single donor, passage 2) and HGMEC (kidney glomerular microvascular, single donor, passage 5).
- n = 3 replicate cultures per arm at 6 h and 24 h.
- Treatments: IL-33red 30 ng/mL; antibody 10 µg/mL added at the same time as IL-33, with no pre-incubation.
- **HGMEC has no vehicle arm.**
- The epithelial lines A549 (lung cancer) and MCF7 (breast cancer) received antibody or vehicle (PBS or DMSO) only, never IL-33.
- All 114 libraries from all four cell types were analysed in one shared statistical model (voom/limma, 38 groups), with AveExpr averaged over all 114 libraries.

**Internal QC** (`01_transcriptomics_qc.py` → `transcriptomics_contrast_summary.csv`).
- 26 comparisons × 26,210 genes, with the same gene set throughout.
- P-values agree with the t-statistics (implied degrees of freedom ≈ 85).
- The within-comparison multiple-testing adjustment reproduces exactly (differences <10⁻¹³).
- Packaging defects:
  - the mmc5 sheets labelled "6h" and "24h" are **identical copies**, each holding both timepoints;
  - mmc4 calls the reference arm "Nontreated" where the annex says "Vehicle".

**IL-33 response (HUVEC).**
- Genes changed at FDR<5% with at least a 2-fold change: 1,068 at 6 h (645 up, 423 down) and 512 at 24 h (314 up, 198 down).
- Enriched gene sets (t-ranked GSEA, `04_fgsea_hallmark.R`), NES at 6 h / 24 h:

| Hallmark gene set | 6 h | 24 h |
|---|---|---|
| TNFα via NF-κB | 3.12 | 3.08 |
| Interferon-γ response | 2.79 | 3.03 |
| Interferon-α response | 2.64 | 2.94 |
| Inflammatory response | 2.69 | 2.69 |
| IL6/JAK/STAT3 | 2.58 | 2.61 |
| Complement | 2.22 | 2.19 |
| Coagulation | 1.57 | 1.44 |

- All padj ≤0.02. The same sets are recovered when genes are ranked by fold change instead.

**Compound_47 blockade (HUVEC)** (`03_blockade.py` → `blockade_HUVEC_summary.csv`; Fig. 1).
- *How it is calculated.* All comparisons come from one fitted model, so they add up exactly. That means "IL-33 + NIP228 vs vehicle" and "IL-33 + Compound_47 vs vehicle" can be derived from the delivered log2 fold changes.
- *A pitfall I avoided.* If you pick the IL-33-responsive genes and score the blockade using the same IL-33-alone and vehicle cultures, you get regression to the mean. That trap lowers the apparent blockade to 82% (6 h) and 67% (24 h), and creates a fake isotype effect of −0.28 / −0.48 log2.
- *What I did instead.* I chose genes at one timepoint and scored them at the other. Those are separate cultures.

| Genes chosen at → scored at | n genes | IL-33 + isotype vs vehicle | Compound_47 vs isotype (+IL-33) | **Blockade (95% CI)** | Isotype effect | Median gene: residual change |
|---|---|---|---|---|---|---|
| 24 h → 6 h (up) | 314 | +1.72 log2 | −1.70 | **99% (94–104%)** | −0.009 | 1.4% of IL-33 effect |
| 6 h → 24 h (up) | 645 | +0.80 | −0.74 | **93% (86–100%)** | −0.023 | 4.2% |
| 24 h → 6 h (down) | 198 | −0.37 | +0.34 | 91% (62–127%) | −0.10 | 7.8% |
| 6 h → 24 h (down) | 423 | −0.21 | +0.18 | 85% (53–123%) | +0.05 | 21.7% |

- Among well-expressed genes, the number changed ≥2-fold vs vehicle falls from 411 to 48 at 6 h, and from 192 to 65 at 24 h, once Compound_47 is present.
- The Hallmark changes reverse in the Compound_47 vs isotype comparison (TNFα/NF-κB NES −3.08 at 6 h, −3.02 at 24 h).
- The response is reversed by the specific antibody but not by the isotype. That argues against a contaminant in the IL-33 preparation (such as endotoxin) as the driver.
- *Scope.* One donor, one IL-33 concentration, one antibody concentration, concurrent addition. The confidence intervals are bootstrapped over genes, so they describe consistency across the transcriptome, not donor-to-donor variation.

**HGMEC.**
- HGMEC's own IL-33 response cannot be estimated. There is no vehicle arm, and the "IL-33 + NIP228 vs NIP228" comparison, which the design would allow, was not delivered.
- For the genes IL-33 induces in HUVEC, Compound_47 (vs isotype, +IL-33) suppresses them in HGMEC at 59% (6 h) and 40% (24 h) of the HUVEC magnitude. Rank correlation (Spearman) is 0.56 and 0.25, and 83% / 68% move in the same direction (`blockade_HGMEC_vs_HUVEC.csv`).
- Key genes at 6 h (log2): SELE −8.7, VCAM1 −11.7, CSF2 −7.1, ICAM1 −5.4, CXCL8 −4.2, IL6 −2.9.
- I cannot tell whether the smaller magnitude reflects a weaker IL-33 response in HGMEC or weaker blockade.

**Antibody alone.**
- Each Compound_47 vs NIP228 comparison gives 21–73 significant genes, typically very low-expressed (median AveExpr −1.3 to −2.7). They do not recur across the 8 independent comparisons (3 recurrent vs 1.75 expected).
- With fold-change ranking, no inflammatory or interferon gene set is significant in any of the 16 antibody-alone comparisons.
- With t-statistic ranking, some proliferation and metabolism gene sets come up, but with **opposite signs in different cell lines** (MYC targets NES +2.81 in HGMEC at 24 h vs −2.95 in HUVEC at 24 h). That pattern looks like differences in culture state between arms rather than a drug effect. It also means that replicate wells from one donor understate the true variability between arms.
- PBS vs DMSO differences are at noise level. DMSO is not a meaningful vehicle for an antibody in any case.

**Standard-error artefact** (`02_se_calibration.py` → `se_calibration_per_gene.csv`; Fig. 2).
- *The test.* If there is no true effect, the observed fold changes should scatter on the scale of their reported SE. The four Compound_47 vs NIP228 endothelial comparisons are independent and close to null, so for each gene I compared the reported SE with the actual root-mean-square of those four fold changes.
- **Well-behaved genes:** the ratio of reported to observed SE has median 1.03 (IQR 0.77–1.46), i.e. well calibrated.
- **238 flagged genes** (SE>2 in at least one comparison; 82 in all 26): median ratio **33** (IQR 10–114).

| Gene | Reported SE (log2) | Observed scatter (log2) |
|---|---|---|
| CD93 | 16,536 | 0.067 |
| CDH5 | 926 | 0.068 |
| VWF | 144 | 0.096 |
| GAPDH | 10.8 | 0.113 |
| PTX3 | 10.9 | 0.095 |
| VCAM1 | 10.4 | 0.23 |
| SELE | 9.2 | 0.70 |
| IL1RL1 (ST2) | 8.3 | 0.097 |
| CCL2 | 6.6 | 0.086 |
| CXCL8 | 4.0 | 0.12 |

- Flagged genes make up 44% of canonical endothelial markers, 38% of epithelial markers, 10% of housekeeping genes, and 0.9% of all genes.
- The SEs are implausible for these libraries (RIN ≥8). Whatever the mechanism, which needs the raw counts to diagnose, the delivered p-values for these genes are wrong by orders of magnitude, in the over-cautious direction.
- **Consequence:** anyone reading the FDR-filtered gene lists would wrongly conclude that IL-33 does not induce E-selectin, VCAM-1, CXCL8, CCL2 or ST2.
- All my conclusions use effect sizes. These are coherent: for example, SELE goes +11.2 with IL-33 and −11.0 with Compound_47.

### 3.2 Serum proteomics (mmc2; 100 hospitalised SARS-CoV-2 patients, pre-vaccination, single centre)

Outputs: `06_proteomics.py` → `proteomics_unique_protein_table.csv`, `proteomics_signature_enrichment.csv`, `olink_undelivered_tests_reconstruction.csv`; Fig. 3 and 5.

- **Events.** The undocumented `composite_endpoint_0/_1` columns are exact multiples of 1/56 and 1/44. I read them as the fraction below the detection limit in each outcome group, which implies **44 events and 56 non-events**. Each single-marker model has 4 parameters, giving ≈11 events per parameter: adequate.
- **Odds ratios "per log unit" are not comparable across assays.** Examples:
  - CSF-1: OR 90.1 (4.2–1,933)
  - GSTP1: 24.6 (3.9–155)
  - CTSS: 23.2 (2.7–200)
  - SEMA4C: 20.9 (4.6–94)
  - CALR: 19.7 (3.8–102)

  These are scaling artefacts. Rank by p-value instead, or re-express per SD (which needs patient-level data). The "log transform" applied is also unspecified, although the vendor's NPX units are already log2.
- **Duplicate measurements.** 27 proteins are measured on more than one panel (58 assays). The 178 FDR-significant assays correspond to 169 unique proteins.
  - After collapsing duplicates, BH over 1,063 proteins gives 193 significant.
  - Counting the 100 undelivered tests as nulls gives 157.
- **Undelivered tests.** The delivered adjusted p-values are reproduced *only* with m = 1,194 tests. That value, and no other, yields whole-number implied ranks (in 639 rows). From the rank gaps, the 100 missing tests are spread across the whole p-value range:
  - ≥1 with p<0.001
  - ≥5 with p<0.01
  - ≥15 with p<0.05
  - **4 with adjusted p<0.05**

  This is consistent with an undocumented post-hoc detectability filter (the highest below-detection fractions in the delivered table are 5/56 and 4/44, ≈9%). The Inflammation panel delivers only 77 assays, and IL-33 is not among them.
- **IL-33 axis.**
  - sST2: OR 3.02 (1.83–5.01), p = 1.7×10⁻⁵, delivered adjusted p = 0.0075; rank 2 of 1,063 unique proteins, behind HGF (4.91, 2.44–9.89).
  - Other IL-1-family receptors rank close behind: IL-1R2 decoy 4.52 (1.95–10.47) and IL-18R1 6.07 (2.23–16.53), ranks 23 and 21. That points to a broad IL-1-family/inflammation signal rather than an IL-33-specific one.
  - In vitro, IL-33 raises HUVEC *IL1RL1* only modestly and transiently (+1.60 log2 at 6 h, +0.36 at 24 h), and Compound_47 barely changes it in HGMEC (+0.19). Endothelium is therefore an uncertain source of serum sST2.
- **Proteome-wide shift.**
  - 81.7% of proteins have OR>1 (sign test p = 8.5×10⁻¹⁰²), with median z = 1.37.
  - Central matching gives an empirical null of mean 1.37, SD 1.42. Against it, sST2 has z = 2.07 (p = 0.039), HGF z = 2.18, and **no protein passes FDR<0.10**.
  - The models were not adjusted for kidney function, time since symptom onset, or treatment. All three could create a dominant "severity" factor. Either this is a confounding artefact, or the biology is real but so widespread that sST2 is just one of hundreds. **In both cases the data cannot single out the IL-33 pathway.**
- **Bridge from the in-vitro programme to patients.** I mapped the genes IL-33 induces and Compound_47 reverses in HUVEC to the proteins measured in serum, with 916 measured proteins as background.
  - FDR-based gene set, 455 genes, 69 of them measured as proteins: 21.7% FDR-significant vs 19.5% of other proteins. Fisher p = 0.37; permutation p = 0.26; permutation p = 0.15 when stratified by panel.
  - Effect-size-based set, 280 genes, 47 measured: 25.5% vs 19.3%. Fisher p = 0.19; permutation p = 0.31.
  - Per marker (`pd_marker_candidates.csv`):

| Serum marker (in-vitro gene) | Serum OR (95% CI) | Association |
|---|---|---|
| IL-6 | 2.17 (1.44–3.29) | yes |
| CXCL8 | 2.23 (1.35–3.68) | yes |
| CCL20 | 1.83 (1.28–2.61) | yes |
| PTX3 | 11.6 (3.4–39.4) | yes |
| E-selectin | 2.08 (1.11–3.87) | nominal only (FDR 0.09) |
| VCAM-1 | 1.28 (0.69–2.37) | no |
| ICAM-1 | 1.67 (0.89–3.11) | no |
| G-CSF | 1.25 (0.87–1.79) | no |
| CXCL6 | 1.02 (0.63–1.64) | no |
| GM-CSF | not on the delivered panels | — |

### 3.3 Post-mortem lung IHC (mmc3)

Outputs: `07_pathology.py` → `pathology_donor_level.csv`, `pathology_group_comparisons.csv`; Fig. 4.

- **Structure.**
  - 78 rows resolve to 74 tissue blocks from 31 donors: 16 COVID+ pneumonia (49 blocks), 10 COVID− pneumonia (15), 5 non-pneumonia (10).
  - Donors 2067, 2072 and 2073 contribute 8 blocks each.
  - Blocks from the same donor are correlated (ICC 0.44–0.63), so **the donor is the unit of analysis**.
  - All donors are white, aged 64–98.
  - Donor 1905's SARS-CoV-2 status is missing despite being labelled "COVID neg".
- **Scores.**
  - The numeric columns appear to convert "n+" to n + 0.5, so values reach 5.5 on a stated 0–5 scale: 39/74 endothelial, 16/71 basal-epithelial and 6/71 neutrophil-elastase scores.
  - The IL-33 columns hold undocumented quarter-point averages, including one in-cell formula, `=(2+4.5)/2`.
  - 53% of endothelial IL-33 scores sit at the ceiling.
  - A single reader scored everything.
- **Results at donor level** (medians: COVID+ / COVID− / non-pneumonia):

| Score | COVID+ | COVID− | Non-pneumonia | Kruskal–Wallis p | Notes |
|---|---|---|---|---|---|
| IL-33, basal epithelium | 4.25 | 4.50 | 4.88 | 0.65 | |
| IL-33, endothelium | 4.81 | 5.50 | 5.50 | 0.11 | COVID+ vs non-pneumonia shift −0.53 (−1.13 to 0), exact p = 0.11; per-block p = 0.012 (pseudo-replication); mixed model p = 0.083 |
| IL-33, vascular smooth muscle | 2.38 | 3.25 | 3.50 | 0.16 | |
| Neutrophil elastase | 4.25 | 4.25 | 3.00 | 0.023 | Higher in *both* pneumonia groups (+1.0; p = 0.006 and 0.028); COVID+ vs COVID− p = 1.0 |
| Eosinophil peroxidase | — | — | — | 0.32 | No eosinophil signal |
| Tryptase (mast cells) | — | — | — | 0.48 | |

- **Interpretation.**
  - The tissue data do not show more IL-33 in COVID-19 lungs.
  - Nuclear IL-33 staining reflects *stored* IL-33. A lower score could mean release or could mean nothing, and these data cannot tell the two apart.
  - Of the 22 tissue RNA samples referenced (9 COVID+ pneumonia / 9 COVID− pneumonia / 4 non-pneumonia donors), none are delivered. They are the fastest route to a direct human tissue test (item 1b below).

### 3.4 Integrity and method register (ranked by impact on the decision)

| # | Issue | Evidence | Consequence | Remedy (plan item) |
|---|---|---|---|---|
| 1 | Serum delivery is incomplete relative to its own multiple-testing adjustment; IL-33 ligand absent | m = 1,194 is the only consistent value; 100 tests undelivered, 4 of them FDR-significant | Cannot assess the drug's actual target in patients; risk of selective reporting | 0b |
| 2 | Proteome-wide outcome shift | 82% OR>1; no protein passes FDR under the empirical null | Specificity of sST2 (and any single protein) not established | 0b, 4 |
| 3 | Inflated RNA-seq standard errors from the pooled model | 238 genes; median 33×; endothelial markers 44% | FDR lists omit SELE / VCAM1 / CXCL8 / CCL2 / IL1RL1; the pipeline needs rerunning before any filing or publication | 0a |
| 4 | One donor per endothelial cell type; replicate wells; HUVEC/HGMEC are not lung | Annex | No generalisation across donors or to lung; arm-level effects visible in antibody-alone gene-set results | 2 |
| 5 | One IL-33 form at one concentration, concurrent addition, one antibody dose | Annex | No potency, no IL-33ox test, no therapeutic-window test | 2a–2c |
| 6 | HGMEC vehicle arm and key comparisons missing | Annex arm table; mmc5 contents | HGMEC IL-33 effect cannot be estimated | 0a |
| 7 | Pathology data handling | Values > scale, formula cell, block-level pseudo-replication, missing status | Tissue evidence is uninformative | 1c |
| 8 | Duplicates across panels; per-log-unit ORs | 27 proteins / 58 assays; OR up to 90 | Discoveries overcounted; ORs not comparable | 0b |
| 9 | Traceability | Compound_47 ↔ AX-1177 link undocumented; affinity/potency "held elsewhere"; counts and fitted model not delivered | The package cannot be tied to the clinical candidate | 0c |
| 10 | Packaging | Duplicate mmc5 sheets; "Nontreated" vs "Vehicle" labels | Risk of double-counting | 0a |

---

## 4. The plan: what we would measure, in which model, and when

### 4.1 Workstreams

| # | Question it answers | Model / material | What we measure (and timepoints within the study) | Calendar | Pass criterion |
|---|---|---|---|---|---|
| **0a** | Do the in-vitro conclusions survive a correct analysis? | Archived counts (all 114 libraries) | Re-fit each cell line separately (voom + eBayes per line). Extract "IL-33 + NIP228 vs NIP228" (HGMEC) and "NIP228 vs vehicle" (HUVEC). Check SE calibration | Weeks 0–6 | SE calibration ratio ≈1 for all genes; HUVEC blockade ≥80% at both timepoints; HGMEC IL-33 response can be sized and is ≥80% blocked |
| **0b** | Is the sST2 signal specific, and what happened to IL-33? | Full Olink output (1,194 tests + detection-limit flags); patient-level NPX values and covariates | Per-SD ORs; adjust additionally for kidney function (eGFR) and a proteome-wide severity factor (first principal component); time since onset; steroids / IL-6R / JAK treatment; bootstrap internal validation | Weeks 0–6 | sST2 per-SD OR lower 95% limit >1 after eGFR and principal-component adjustment; IL-33 result disclosed |
| **0c** | Is Compound_47 the candidate, and does it bind what we claim? | Biologics file | Sequence/lot identity vs AX-1177; binding affinity (SPR) to human IL-33red, IL-33ox and full-length IL-33; cross-reactivity with cynomolgus, mouse and hamster IL-33; ST2-reporter IC50; epitope | Weeks 0–6 | Identity confirmed; IL-33ox binding documented; a pharmacologically relevant species identified for in-vivo work and toxicology |
| **1a** | Is the IL-33 ligand present in patients and linked to outcome? **(fast-fail)** | The 100 enrolment sera (stored at â80 Â°C) | Ultrasensitive total and free IL-33, and IL-33–sST2 complex; sST2 by immunoassay | Months 1–3 | IL-33 ligand (total or complex) measurable in ≥50% of patients and associated with the composite endpoint (adjusted per-SD OR lower limit >1) |
| **1b** | Is the IL-33 endothelial programme switched on in human lung? **(fast-fail)** | The 22 lung tissue RNAs referenced in mmc3 (Zr4940 series; 9 / 9 / 4 donors) | RNA-seq; per-donor score for the 455-gene IL-33/Compound_47 signature and its endothelial-restricted subset | Months 1–3 | Signature ≥0.5 SD higher in COVID+ pneumonia than non-pneumonia (pre-specified; directional given n = 9 vs 4) |
| **1c** | A proper tissue read-out | All 74 blocks | Re-score IL-33 and ST2 with 2 blinded readers plus digital H-score; pre-specified scoring with no values above scale; analysis per donor | Months 1–3 | Inter-reader agreement (κ) ≥0.6; result feeds 1a/1b |
| **2a** | Potency | Primary human **lung microvascular** endothelial cells, ≥3 donors (plus HUVEC, ≥3 donors, to bridge); randomised plate layout; donor as the unit | IL-33red titration 0.01–30 ng/mL (EC50/EC80), then an 8-point AX-1177 titration at EC80 (IC50/IC90) vs isotype. **4–6 h:** surface E-selectin, VCAM-1, ICAM-1 by flow cytometry. **6 and 24 h:** secreted GM-CSF, IL-6, CXCL8, CCL2, CCL20, G-CSF, sST2. **6 h:** targeted signature RNA panel | Months 1–4 | IC90 compatible with achievable exposure (set against the PK/PD model) |
| **2b** | Is there a therapeutic window? | Same cells | AX-1177 added at −1 h (pre-complexed), 0, +1, +3 and +6 h relative to IL-33; read at 6 h and 24 h | Months 1–3 | ≥50% inhibition retained when added 3 h after IL-33 |
| **2c** | Does the claimed dual-form binding matter? | Oxidised IL-33 and full-length IL-33; primary bronchial epithelium at air–liquid interface (ALI) | Binding, plus neutralisation in an ST2-independent epithelial read-out | Months 2–4 | Functional IL-33ox neutralisation shown; if not, drop the claim (not a stop) |
| **2d** | Does it block natural, virus-released IL-33? | Airway epithelial ALI cultures infected with SARS-CoV-2, influenza A and RSV; medium transferred (or transwell) onto lung microvascular endothelial cells | IL-33 release over 0–72 h; endothelial activation panel; barrier function (impedance, 0–48 h); neutrophil adhesion under flow; **epithelial viral titre** | Months 2–5 | ≥70% inhibition of the IL-33-attributable endothelial activation; no increase in viral titre |
| **2e** | Does it add to standard of care? | Lung microvascular endothelial cells | IL-33-driven activation with dexamethasone, IL-6R blockade or baricitinib, each ± AX-1177 | Months 3–5 | Additional suppression on top of standard care |
| **3** | Does dosing *after* onset help, without harming viral clearance? | Species and molecule per 0c: AX-1177 if it cross-reacts; otherwise a surrogate anti-mouse IL-33 matched for affinity and red/ox binding, or human-IL-33 knock-in mice. Mouse influenza A (sublethal and lethal); mouse-adapted SARS-CoV-2 (or hamster); RSV in BALB/c | Isotype vs antibody, **prophylactic (day −1) and therapeutic (day +2/+3, after weight loss begins)**, 2 dose levels, n = 12–16 per group, randomised and blinded. **Daily to day 14:** weight, clinical score, survival. **Days 3, 5, 7 (10 for clearance):** lung viral titre and RNA; BAL protein and IgM; BAL cell counts; blinded histopathology; lung endothelial E-selectin and VCAM-1 (flow on CD31+ cells); sorted lung endothelial signature RNA; BAL and serum IL-6, KC, GM-CSF, sST2; free and total IL-33; PK in serum and BAL | Months 3–9 | Therapeutic dosing cuts the pre-specified primary endpoint (BAL protein at day 5, or weight-loss AUC) by ≥30% vs isotype in ≥2 viruses; viral titre rises ≤0.5 log10; no delay in clearance; target engagement shown in BAL |
| **4** | Does the human signal replicate beyond SARS-CoV-2 and beyond severity? | Independent cohort of ≥250 hospitalised adults: COVID-19 (vaccinated era), influenza and RSV. Serum at days 0 / 3 / 7 (plus nasal sampling); symptom onset and treatment recorded | Total/free IL-33, sST2, and the endothelial panel (E-selectin, VCAM-1, ICAM-1, ANGPT2, vWF, PTX3, IL-6, CXCL8, CCL2, CCL20, GM-CSF). Pre-registered per-SD ORs adjusted for age, sex, NEWS2, eGFR and a severity factor | Months 2–9 | sST2 or IL-33 per-SD OR lower limit >1 after adjustment, in ≥2 viruses; enrichment threshold and treatment window defined. About 230 patients gives 90% power for OR 1.8 per SD at a 25% event rate (`power_calculations.csv`) |

### 4.2 Gates and stop rules

- **Gate 0 (week 6).**
  - Stop if Compound_47 is not AX-1177, or if re-analysis from counts overturns the blockade result.
  - Otherwise proceed.
- **Gate 1 (month 4).**
  - **Stop** if *both* 1a and 1b fail (no IL-33 ligand in patients and no lung signature), **or** if 2b shows <20% inhibition when AX-1177 is added ≥1 h after IL-33 (no therapeutic window even in a dish).
  - If exactly one of 1a/1b fails, continue but narrow the population to where the signal exists.
- **Gate 2 (month 9): go to IND-enabling only if all of the following hold:**
  - 3 passes in ≥2 viruses with therapeutic dosing;
  - no viral-clearance or titre signal;
  - 4 replicates the adjusted association;
  - 2a potency is compatible with achievable exposure.
  - **Stop** if therapeutic dosing fails in all models, **or** if any model shows higher viral titre / delayed clearance attributable to IL-33 blockade, **or** if the adjusted association fails to replicate in 4.
- **Planning horizon if Gate 2 passes:** IND-enabling work (GLP toxicology in the relevant species, tissue cross-reactivity, cytokine-release assay, manufacturing, PK/PD model) over roughly months 9–21; first-in-human around months 21–24.

---

## 5. What goes into the clinic (only if Gate 2 passes)

- **Molecule:** AX-1177 (human IgG1), IV. Identity to the tested Compound_47 must be confirmed (0c). Starting dose and regimen come from a PK/PD model combining the 2a IC90 and the BAL exposure from 3.
  - The only dose anchor in this package is in vitro: 10 µg/mL gave ≥93% blockade of 30 ng/mL IL-33red. It is not a clinical dose rationale.
- **Phase 1 (healthy volunteers), single ascending dose, ± multiple ascending dose:** safety, PK, immunogenicity. Target engagement by accumulation of total IL-33 / drug–IL-33 complex in serum.
- **Phase 2a, proof of mechanism, in hospitalised vLRTD.**
  - *Patients:* adults with PCR-confirmed SARS-CoV-2, influenza or RSV LRTD, needing oxygen but *not* mechanically ventilated, within the treatment window defined in 4. Enriched for sST2 (or IL-33) above the threshold set in 4.
  - *Design:* randomised 2:1, double-blind, single IV dose vs placebo on top of standard care; n ≈ 60–90.
  - *Primary:* safety, plus change from day 0 to days 3 and 7 in a pre-specified IL-33/endothelial pharmacodynamic composite: soluble E-selectin, IL-6, CXCL8, CCL2, CCL20 and GM-CSF.
    - These are chosen because they are the most strongly IL-33-induced, Compound_47-reversed secreted products in the package (6 h log2 +11.2, +5.8, +8.2, +4.2, +9.2, +10.3; reversal −11.0, −6.0, −8.4, −4.3, −9.8, −12.2).
    - Three of them also track outcome in mmc2 (IL-6, CXCL8, CCL20).
  - *Secondary:* suppression of free IL-33; sST2.
  - *Safety focus:* **viral load kinetics** (nasopharyngeal swabs at days 1, 3, 5, 7, 14), secondary infections, infusion reactions.
  - *Exploratory:* 30-day composite of ICU/IMV/death (the same endpoint as mmc2), and time to recovery.
- **Phase 2b, efficacy on the 30-day composite.** The sample size depends heavily on the current event rate. The package's 44% comes from a pre-vaccination cohort and is unlikely to hold today, which is why enrichment is needed.
  - At a 35% relative risk reduction, 80% power, two-sided α 0.05:
    - 44% event rate → **304** patients total;
    - 25% → **666**;
    - 15% → **1,224**.
  - With one-sided α 0.10: 174 / 382 / 702 (`power_calculations.csv`).

---

## 6. Assumptions and limitations of this review

1. Compound_47 = AX-1177. The annex does not state this.
2. The 44/56 event split is inferred from undocumented columns: their values are exact multiples of 1/56 and 1/44.
3. Only summary statistics were delivered: no counts and no patient-level data.
   - The cause of the SE artefact cannot be diagnosed.
   - Proteomics re-analysis is limited to the reported ORs and confidence intervals.
   - Per-SD ORs are not computable.
4. The empirical-null analysis assumes most proteins are truly null. If the shift is real biology, sST2 stays associated, but it is then one of hundreds. Either way the data do not make it specific.
5. Olink names were mapped to genes by hand where they differ from gene symbols (`olink_assay_to_gene_map.csv`); 916 of 1,063 proteins map to genes in the RNA table. The enrichment result holds for both signature definitions, with and without stratifying by panel.
6. Blockade confidence intervals are bootstrapped over genes and rest on one donor per cell type. The cross-timepoint design assumes the 6 h and 24 h arms are separate cultures, which is what the annex's design implies.
7. Pathology scores were used as delivered; "ND" and "N/A" were treated as missing.
8. Thresholds in the gates are proposed decision rules (judgement), not quantities estimated from the package. Power calculations list their inputs.

---

## 7. Files produced (`/tmp/outputs`)

| Output | Content |
|---|---|
| `analysis/00_extract_tables.py` | Extracts the Excel tables to CSV; shows the mmc5 sheets are duplicates |
| `analysis/01_transcriptomics_qc.py` → `transcriptomics_contrast_summary.csv` | Internal consistency checks; significant-gene counts per comparison |
| `analysis/02_se_calibration.py` → `se_calibration_per_gene.csv` | SE calibration and flagged genes (Fig. 2) |
| `analysis/03_blockade.py` → `blockade_HUVEC_summary.csv`, `blockade_HGMEC_vs_HUVEC.csv`, `blockade_per_gene_{6h,24h}.csv.gz` | Cross-timepoint blockade, isotype effect, residual transcriptome, antibody-alone reproducibility |
| `analysis/04_fgsea_hallmark.R` → `hallmark_fgsea_all_contrasts.csv`, `hallmark_fgsea_summary.csv` | Hallmark GSEA for all 26 comparisons, t-ranked and fold-change-ranked |
| `analysis/05_olink_map.py` → `olink_assay_to_gene_map.csv` | Olink assay → gene mapping; cross-panel duplicates |
| `analysis/06_proteomics.py` → `proteomics_unique_protein_table.csv`, `proteomics_signature_enrichment.csv`, `olink_undelivered_tests_reconstruction.csv`, `HUVEC_IL33_signature_*.csv` | Reconstruction of the 1,194 tests; duplicate-collapsed BH; empirical null; signature bridge |
| `analysis/07_pathology.py` → `pathology_blocks_clean.csv`, `pathology_donor_level.csv`, `pathology_group_comparisons.csv` | Donor-level IHC analysis, block-level and mixed-model sensitivity, ICC |
| `analysis/08_pd_marker_table.py` → `pd_marker_candidates.csv` | Candidate pharmacodynamic markers: in-vitro response and reversal vs serum association |
| `analysis/09_power_calcs.py` → `power_calculations.csv` | Sample sizes for the replication cohort, Phase 2b and in-vivo studies |
| `analysis/10_make_figures.py` → `figures/fig1–fig5` | Fig. 1 blockade; Fig. 2 SE calibration; Fig. 3 serum proteomics; Fig. 4 IHC by donor; Fig. 5 undelivered Olink tests |
