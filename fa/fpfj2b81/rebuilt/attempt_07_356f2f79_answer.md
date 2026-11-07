**Recommendation: Do not take AX-1177 into IND-enabling or clinical work on this package. Instead, fund a ~9-month de-risking programme with three pass/fail checkpoints ("gates"). The antibody clearly neutralises IL-33 in vitro, but the package does not show that IL-33 drives human viral lower respiratory tract disease (LRTD).**

# AX-1177 (anti-IL-33 mAb): proposal to the Programme Committee

**What this is based on.** The whole mounted package:
- `AX-1177_methods_annex.md`
- `mmc2.xlsx`: serum proteomics
- `mmc3.xlsx`: post-mortem lung
- `mmc4.xlsx` and `mmc5.xlsx`: RNA-seq contrasts

**How the numbers were produced.**
- I recomputed every number here from those files. Nothing was taken from the spreadsheets' visible views: several sheets hide rows, columns or contrasts, so I parsed the underlying workbook XML.
- Code, output tables and an evidence register (`analysis/evidence_register.tsv`, with claim IDs E01–E40) are in `/tmp/outputs/analysis/`. Figures are in `/tmp/outputs/figures/`.
- No external data were used. Where general domain knowledge shaped a *design proposal* (not a finding), I say so.

**Terms used below.**
- **IL-33red**: the reduced form of recombinant IL-33 used in the experiments.
- **C47**: "Compound_47", the antibody actually tested.
- **NIP228**: the isotype (non-binding) control antibody.
- **sST2**: soluble ST2, the circulating form of the IL-33 receptor. It acts as a decoy that mops up IL-33.
- **OR**: odds ratio. **q**: false-discovery-rate (FDR)-adjusted p value. **FDR 5%**: q < 0.05.
- **HUVEC**: umbilical vein endothelial cells. **HGMEC**: kidney glomerular endothelial cells.
- **Arm shorthand**: V = vehicle; I = IL-33 alone; IN = IL-33 + isotype; IC = IL-33 + C47; N = isotype alone; C = C47 alone.

---

## 1. The decision in one page

| # | Question the committee needs answered | What the package actually shows | Strength |
|---|---|---|---|
| 1 | Does the antibody neutralise IL-33 signalling? | **Yes, in vitro.** IL-33red (30 ng/mL) switches on a large inflammatory (NF-κB) gene programme in HUVEC: 4,031 genes change at FDR 5% at 6 h (e.g., GM-CSF/CSF2 +10.3 log2 fold-change, G-CSF/CSF3 +8.3, TNF +7.9, IL6 +5.8). C47 reverses **98.6%** of the induced programme at 6 h (95% CI 93–105%) and **90.0%** at 24 h (82–99%). The isotype control changes it by −1%. C47 alone does nothing to it. HGMEC give the same answer. | Strong, but narrow (§2.1) |
| 2 | Is the tested antibody AX-1177? | **Not documented.** The annex is headed "AX-1177", but every experiment uses "Compound_47". Nothing links sequence, lot or certificate of analysis. The epithelial arms use a DMSO vehicle, which is unusual for an antibody. | Gap: must be closed |
| 3 | Is the IL-33 axis linked to severe human disease? | **Only indirectly.** sST2 is the #2 of 1,063 unique serum proteins associated with 30-day ICU/ventilation/death: OR 3.02 (1.83–5.01) per log unit, adjusted for age, sex and NEWS2; 44/100 patients had an event. But **IL-33 itself is not in the delivered data**. And 193 proteins pass FDR 5%, 190 of them elevated, including proteins that normally sit inside cells. That is a general severity/tissue-damage signal, not an IL-33-specific one. | Weak and indirect (§2.2) |
| 4 | Does the programme AX-1177 blocks in vitro track severity in patients? | **No.** Among serum proteins, the ones IL-33 induces are no more likely to be severity-associated than any others: 20.0% vs 19.3% (OR 1.04, p = 0.89). A generic inflammation gene set (Hallmark TNFα/NF-κB) *is* enriched: 38.6% (OR 2.79, p = 0.0026). The strongest C47-reversible mediators show no outcome association: G-CSF, CXCL10, CXCL6, CXCL5, TNF. | Not supported (§2.3) |
| 5 | Is IL-33 increased in diseased lung? | **No.** Analysed per donor, IL-33 staining is not higher in COVID-19 lungs than in non-COVID pneumonia or controls, in any compartment. Endothelium medians: 4.81 vs 5.50 vs 5.50 (Kruskal–Wallis p = 0.16). But the scoring is already at its maximum in 60–80% of control donors, so this stain **could not** have shown an increase. | Not supported; the stain can't answer the question (§2.4) |
| 6 | In vivo efficacy, PK, safety (including viral clearance) | **None in the package.** No in vivo data, no dose–response, no oxidised IL-33, no virus in any experiment. | Absent |
| 7 | Is the package complete and analytically sound enough to build on? | **No.** 100 tested serum assays were withheld, ≥4 of them FDR-significant. The single-model RNA-seq fit makes 171 genes unevaluable, including E-selectin, VCAM-1, IL-8 and ST2. Rows, columns and contrasts are hidden. Tissue group labels contradict the autopsy text for 6–7 of 15 control donors. | Needs fixing first (§3) |

**Why not Go now.** A clinical programme needs two things:
- evidence that IL-33 is active in the human disease;
- evidence that blocking it changes disease in a living system.

Both are missing. The one human signal (sST2) sits inside a broad, non-specific severity proteome. The IL-33 programme we block in vitro is not what tracks severity. Tissue IL-33 is not increased. The in vitro work also has gaps: one antibody:IL-33 ratio (41:1 molar, no potency estimate), reduced IL-33 only, one donor per endothelial type, and non-lung endothelium. There is no virus anywhere in the package.

**Why not stop.** Three reasons to keep going:
- The pharmacology is clean and specific. Near-complete reversal at 6 h, no isotype effect, and a negligible antibody-alone transcriptome.
- sST2, the IL-33 decoy receptor, ranks #2 of 1,063 proteins even after adjusting for NEWS2. It is a plausible enrichment and patient-selection biomarker.
- The negative tissue result comes from a saturated stain and mislabelled groups, so it is not a true negative.

The cheapest, most decisive experiments use **material the programme already holds**: stored sera, archived tissue RNA and the count matrices. They can be run in weeks.

**The ask.** Approve Gates 0–3 in §4 with the pre-specified pass and kill criteria, and a decision at about month 9. Make no IND-enabling, CMC scale-up or clinical commitments before that decision.

---

## 2. Evidence review

### 2.1 In vitro pharmacology (mmc4, mmc5): strong but narrow

**Design facts (annex).**
- Cells: HUVEC (single donor, passage 2) and HGMEC (single donor, passage 5). A549 and MCF7 cancer lines received antibody only, never IL-33.
- n = 3 wells per arm at 6 h and 24 h; 114 libraries.
- C47 at 10 µg/mL = 68.5 nM; IL-33red at 30 ng/mL = 1.66 nM. That is a **41:1 molar excess** (83:1 in binding sites).
- The antibody was added at the same time as IL-33, with no pre-incubation.
- All contrasts come from one limma/voom statistical model fitted across all four cell types (E01).

**IL-33 response in HUVEC.**
- At 6 h: 4,031 genes at FDR 5% (2,191 up, 1,840 down); 1,068 change by more than 2-fold (645 up, 423 down).
- At 24 h: 1,836 genes; 512 change by more than 2-fold (E09–E10).
- The induced set is dominated by the Hallmark TNFα/NF-κB programme: 92 of its 197 genes, OR 40, q = 5×10⁻⁹³. Interferon-γ, inflammatory-response and IL6/JAK/STAT3 sets follow (E11).

**How I measured neutralisation.**
- **Primary estimate.** I compared IL-33 + C47 against IL-33 + isotype (IC vs IN). This contrast shares no samples with the IL-33-vs-vehicle contrast used to pick the signature genes. The alternative, IL-33 + C47 vs IL-33 alone, shares the IL-33-alone samples. That builds in a negative correlation that inflates apparent neutralisation: 98%/82%/84%/72% against 95%/41%/73%/19% (genes up and down at 6 h and 24 h).
- **Cross-timepoint selection.** Picking genes because they were significant also inflates their IL-33 effect ("winner's curse"). I therefore chose genes at one timepoint and measured them at the other, which uses independent samples.

**Results.**

| Metric (IL-33-induced genes, HUVEC) | 6 h | 24 h |
|---|---|---|
| % inhibition, genes chosen at the other timepoint (sum ratio; gene-bootstrap 95% CI) | **98.6% (93–105)** | **90.0% (82–99)** |
| Median % inhibition per gene, same timepoint (IQR) | 95% (43–105) | 73% (22–90) |
| Signature genes significantly reversed vs. moved the same way | 438/645 vs 8 | 147/314 vs 4 |
| Isotype effect on the IL-33 response (IN − I, as % of IL-33 effect) | −1% | −3% |
| C47 alone vs isotype, regression slope on the signature | 0.006 | 0.031 |

Reversal of IL-33-*repressed* genes was only partial: 41% median at 6 h, 19% at 24 h (E12–E15). The bootstrap CIs treat genes as independent, which they are not, so they are optimistic.

**Key mediators.** The last two columns are the IL-33 effect left over with C47 present (IC − V). It is derived exactly because fold-changes from one model add: (IC − I) + (I − V).

| Gene (protein) | IL-33 vs vehicle, 6 h (q) | C47 + IL-33 vs isotype + IL-33, 6 h | Left over with C47, 6 h | IL-33 vs vehicle, 24 h | Left over, 24 h |
|---|---|---|---|---|---|
| CSF2 (GM-CSF) | +10.30 (5×10⁻²³) | −12.21 | −1.93 | +8.11 | −0.85 |
| CSF3 (G-CSF) | +8.32 (2×10⁻¹⁸) | −8.28 | +0.05 | +6.66 | +0.46 |
| CCL20 | +9.21 (3×10⁻²⁰) | −9.84 | −0.58 | +5.57 | −0.10 |
| IL6 | +5.82 (2×10⁻¹³) | −5.97 | −0.14 | +2.81 | −0.05 |
| TNF | +7.89 (2×10⁻³¹) | −7.67 | +0.02 | −0.09 (not significant) | — |
| CXCL10 | +6.89 (7×10⁻¹⁸) | −7.51 | −0.44 | +4.97 | **+2.43** |
| F3 (tissue factor) | +5.64 (2×10⁻²⁶) | −5.47 | +0.27 | +1.16 (not significant) | — |
| TNFRSF11B (OPG) | +4.80 (3×10⁻¹⁹) | −4.99 | 0.00 | +2.36 | −0.34 |
| C3 | +4.79 (3×10⁻¹⁰) | −4.62 | +0.15 | +6.13 | **+1.40** |
| SELE (E-selectin) | +11.21 (q = 0.50)* | −10.99 | +0.31 | +4.74 | −0.38 |
| VCAM1 | +8.74 (q = 0.51)* | −8.76 | +0.09 | +3.41 | −0.25 |

\*Large effect but not significant because of the variance problem in §3, issue 3. Full table: `analysis/key_mediators_IL33_and_neutralisation.tsv`.

**What is left over.**
- At 6 h the median leftover is 8% of the IL-33 effect (346 genes with a >4-fold induction).
- At 24 h it is 28% (176 genes). Most of the large 24 h leftovers are low-count unannotated transcripts, which looks like noise. The mediator exceptions are CXCL10 and C3 (E16).

**HGMEC.**
- The delivery has no IL-33-vs-control contrast for HGMEC, and none can be derived: there is no vehicle arm, and IL-33-vs-isotype was not delivered (E18).
- Still, C47 + IL-33 vs isotype + IL-33 gives 1,460 changed genes at 6 h. They are a textbook NF-κB core: NFKBIA t = −28.1, TNFAIP3, TRAF1, NFKB2, RELB.
- C47 reverses 270 of the 645 HUVEC-induced genes (slope −0.64). Of the 977 genes changed in both cell types, 97.3% move in the same direction. At 24 h the effect is weaker (269 genes; E17).

**Specificity (antibody alone).**
- C47 vs isotype gave 21–73 changed genes per cell line and timepoint: 632 hits in total across 16 contrasts.
- 70% of hits are very low-count transcripts (median 7.8-fold "change"). 94 are abundant genes with a median change of about 8% (0.11 log2 units).
- Only 4 of 562 genes recur in two cell lines. There is no coherent antibody-alone programme (E19).

**Limits of this evidence.**
- One antibody concentration, so no IC50 and no link to a clinical exposure.
- The 30 ng/mL IL-33 dose is not justified against any measured concentration.
- Reduced IL-33 only. The annex says C47 binds the oxidised form too, but that is untested here.
- One donor per endothelial cell type, and neither is lung endothelium.
- No IL-33-stimulated epithelium. MCF7 (breast) is irrelevant to the lung.
- No virus, and no endogenous IL-33 release.

### 2.2 Serum proteomics (mmc2): an IL-33-axis signal, but not IL-33 and not specific

**Cohort (annex).**
- 100 hospitalised patients with PCR-confirmed SARS-CoV-2; single centre; before vaccination.
- Serum taken at enrolment.
- Endpoint: ICU, invasive ventilation or death within 30 days.
- **44 events and 56 non-events.** I derived this from the columns labelled `composite_endpoint_0/1`. They are exact multiples of 1/56 and 1/44, i.e. fractions of missing/below-detection samples per outcome group (E20).

**Results.** All ORs are per log unit, adjusted for age, sex and NEWS2.

| Protein (assay) | OR (95% CI) | p | q, after removing duplicate assays |
|---|---|---|---|
| HGF | 4.99 (2.53–9.82) | 3.4×10⁻⁶ | 0.004 |
| **sST2 (IL1RL1)** | **3.02 (1.83–5.01)** | **1.7×10⁻⁵** | **0.009** (rank 2/1,063) |
| HDGF | 2.74 (1.67–4.50) | 7.1×10⁻⁵ | 0.012 |
| PTX3 | 11.6 (3.40–39.4) | 8.9×10⁻⁵ | 0.012 |
| IL-6 (measured on 4 panels) | 2.14 (1.45–3.15) | 1.3×10⁻⁴ | 0.012 |
| IL-5 / CCL11 (eotaxin) / CCL17 / CCL24 (type-2 markers) | 1.00 / 1.08 & 0.98 / 0.85 / 0.92 | all ≥0.39 | — |
| **IL-33** | **not in the delivery** | — | — |

**How to read this.**
- **The signal is pervasive.** 35.1% of assays have p < 0.05, against 5% expected by chance. 190 of the 193 FDR-significant proteins are elevated, including intracellular proteins that leak from damaged cells (NPM1, PXN, CALR, GSTP1, PRDX1/6, CASP8). sST2 is a strong member of a general severity/tissue-injury axis; on its own it is not evidence that IL-33 drives disease.
- **sST2 points both ways.** As a decoy receptor, high sST2 could mean IL-33 activity is *up* or IL-33 is being *soaked up*. The data cannot tell which.
- **There is no type-2 signal** (E26).
- **Scope is narrow.** COVID-only, single centre, pre-vaccination, no replication cohort. Top ORs will be inflated by selection.
- **ORs can't be compared across assays.** They are "per log unit" (e.g., CSF-1 OR 90, CI 4.2–1,933), so I ranked by z statistic.
- **Unclear transform.** The annex says values were "log transformed". Olink NPX is already on a log2 scale, so the transform needs clarifying.
- **Incomplete.** The delivered multiple-testing adjustment covered 1,194 tests, not the 1,094 delivered (§3, issue 5).

### 2.3 Does the programme C47 blocks in vitro track severity in patients? (mmc2 × mmc4/5)

**Method.**
- I mapped all 1,063 unique serum proteins to gene symbols via org.Hs.eg.db aliases plus a curated Olink dictionary; all mapped.
- 913 also appear in the RNA-seq.
- "IL-33-induced" = FDR 5% and more than 2-fold up in HUVEC at 6 h or 24 h: 90 proteins.
- "Severity-associated" = after-deduplication q < 0.05 and OR > 1.

**Results** (`analysis/serum_endothelium_link_*.tsv`; Figure 3).

| Gene set | % of set severity-associated | OR, p |
|---|---|---|
| IL-33-induced in HUVEC (n = 90) | 20.0% | **1.04, p = 0.89** |
| IL-33-induced **and** reversed by C47 (n = 71) | 21.1% | 1.12, p = 0.75 |
| IL-33-induced, more than 4-fold (n = 48) | 20.8% | 1.10, p = 0.85 |
| IL-33-induced, excluding NF-κB Hallmark genes (n = 58) | 15.5% | 0.75, p = 0.50 |
| *Comparator:* Hallmark TNFα/NF-κB (n = 44) | 38.6% | **2.79, p = 0.0026** |
| *Comparator:* Hallmark inflammatory response (n = 59) | 32.2% | 2.09, p = 0.016 |

Background rate: 19.3%.

- The null result held across nine sensitivity variants: OR 0.75–1.12, all p > 0.4 (E28–E29).
- There is a **weak, diffuse** overall correlation between IL-33 induction and severity (Spearman ρ = 0.15 at 6 h). After adjusting for expression level, panel and Hallmark membership it explains ~1.2% of the variance (p = 0.0014). It disappears at 24 h (p = 0.65) (E30).
- Strongly induced, C47-reversible mediators with **no** outcome association: G-CSF (OR 1.25, p = 0.23), CXCL10 (1.30, p = 0.25), CXCL6 (1.02, p = 0.95), CXCL5 (1.17, p = 0.52), TNFRSF9 (1.09, p = 0.68), TNF (1.54, p = 0.16).
- Endothelial injury markers that *do* track severity are not induced by IL-33 in HUVEC: PTX3 (OR 11.6), vWF (3.86) and ANGPT2 (2.21); ANGPT2 changes by +0.09 log2.

**Useful by-product: a candidate PD panel.** 15 proteins are IL-33-induced, C47-reversed *and* severity-associated; 12 of them are extracellular (`analysis/candidate_PD_panel.tsv`):
- IL-6 (q = 0.012), OPG/TNFRSF11B (0.014), sIL-18R1 (0.020), MCP-3/CCL7 (0.020), CCL20 (0.020);
- CSF-1 (0.035), CTSS (0.036), IL-1β (0.044), tissue factor (0.049), IL-15 (0.049).

These are shared NF-κB mediators, not IL-33-specific. That makes them suitable **pharmacodynamic** readouts in a placebo-controlled study, not evidence of IL-33 causality.

### 2.4 Post-mortem lung (mmc3): target present everywhere, no disease-associated increase detectable

**Design (after repair; §3).**
- 31 donors and 74 tissue blocks: COVID+ pneumonia 16 donors/49 blocks, COVID− pneumonia 10/15, COVID− non-pneumonia 5/10.
- Ages 64–98, medians 82–84 by group (Kruskal–Wallis p = 0.70); all donors recorded as white.
- Three COVID+ donors supply 24 of the 49 COVID+ blocks. Blocks from the same donor are strongly correlated (intraclass correlation 0.40–0.63), so **the donor is the unit of analysis**.

| IL-33 compartment (median of donor medians) | COVID+ pneumonia | COVID− pneumonia | COVID− non-pneumonia | 3-group p (Kruskal–Wallis) | COVID+ vs COVID− pneumonia: median shift (95% CI); p | Mixed model, COVID+ effect (95% CI) |
|---|---|---|---|---|---|---|
| Endothelium | 4.81 | 5.50 | 5.50 | 0.16 | 0.00 (−1.00, 0.00); 0.20 | −0.34 (−0.83, 0.15) |
| Basal epithelium | 4.25 | 4.50 | 4.88 | 0.61 | 0.00 (−0.75, 0.75); 0.96 | +0.10 (−0.50, 0.71) |
| Vascular smooth muscle | 2.38 | 3.25 | 3.50 | 0.18 | −0.50 (−1.50, 0.25); 0.19 | −0.56 (−1.36, 0.25) |

**How to read it (E32–E35).**
- **The stain is saturated.** Endothelial IL-33 is already at the maximum recorded value (5.5) in 60% of COVID− pneumonia and 80% of non-pneumonia donors, so it cannot register an increase. With 16 vs 10 donors there is 80% power only for very large shifts (about 1.2 SD).
- **Counting blocks as independent misleads.** Doing so would report COVID+ endothelial IL-33 as significantly *lower* than in non-pneumonia controls (p = 0.012); the correct donor-level p is 0.11.
- **The stain can't show release.** It measures stored IL-33, so it cannot tell reduced expression from release. The slightly lower COVID+ scores fit either.
- **Cell markers track pneumonia, not COVID.** Eosinophil (EDN, MBP), neutrophil-elastase and IL-5Rα scores separate both pneumonia groups from non-pneumonia, but COVID+ does not differ from COVID− pneumonia. Neutrophil elastase median is 3.75 in both.
- **Fixing the group labels doesn't change it.** Restricting to donors whose autopsy text matches their label still shows no COVID-associated increase (all p > 0.09).

---

## 3. Data-integrity and methodology findings (must be fixed before any external or regulatory use)

| # | Issue | Evidence | Consequence | Fix |
|---|---|---|---|---|
| 1 | mmc5 sheet names don't match contents | The "6h" and "24h" sheets are identical: each holds **all 24 contrasts at both timepoints** (629,040 rows). Each has an active filter showing one HUVEC contrast and hiding the other 23. The "6h" sheet also declares 1,048,576 rows (E02–E03). | Anyone using the Excel view sees 1 of 24 contrasts; anyone reading "24h" by code gets 6 h data. | I filtered every analysis on the `Comparison` column. Reissue one clean table. |
| 2 | mmc4 reference arm mislabelled | Sheets say "Vehicle"; rows say "Nontreated". | Unclear what the reference arm received. | Clarify. |
| 3 | **Variance problem from fitting one model to four cell types** | 171 genes have standard errors >10× the norm for their expression level (70 >100×). CXCL1's SE is 1,062–2,823 log2 units in *every* contrast (t = 0.007 for a +8.2 change). For the same contrast type, SEs differ up to ~10⁵-fold between cell lines (XBP1: 0.24 in MCF7 vs 1,840 in A549). 98.8% of these genes are the ones the model flagged as variance outliers, against 4.9% of all genes (E06–E08; Figure 2). | E-selectin (+11.2, t 1.26), VCAM-1, IL-8, CXCL1, CCL2, PTGS2 and **ST2 (IL1RL1)** cannot be evaluated. There are also spurious hyper-significant tiny changes (AKR1C2: 0.11 log2, t = 169). | Refit each cell line separately from the archived counts (voom/limma with quality weights, or edgeR quasi-likelihood) and report per-sample QC. |
| 4 | Degrees of freedom don't match the annex | Working back from t and p: 23,337 genes have 85.128 df and the floor is 75.053, so **residual df ≤ 75**. 114 libraries minus 38 groups should give 76 (E05). | One library was dropped or an extra covariate was fitted, and neither is recorded. | Document the final sample set and design matrix. |
| 5 | **Serum delivery is incomplete** | Multiple-testing adjustment was run over **1,194 tests**, not the 1,094 delivered. Working back from the adjusted p-values gives exact-integer ranks at 639/655 positions under m = 1,194. **≥4 withheld assays were FDR-significant** and ≥8 reached FDR 10%. The annex says the adjustment covered the assays "in the delivery" (E22; Figure 5). | Selective delivery. Whether IL-33 was measured is unknowable. | Release all 1,194 results, raw NPX, below-detection flags and the exclusion rule. |
| 6 | Duplicate assays across panels | 27 proteins are measured on 2–4 panels (58 rows), e.g., IL-6 ×4 and HGF ×2. The adjustment counts them as separate tests (E23). | Inflated multiplicity and top-hit lists (178 rows = 169 proteins). | Deduplicate before the adjustment (done here: 1,063 proteins). |
| 7 | Hidden content in mmc2 | The 95% CI columns are hidden. Two rows (HGF-ONCII, IL6-ONCII) are hidden, while other duplicates stay visible (E27). | Manual curation that isn't recorded. | Deliver an unfiltered export. |
| 8 | Hidden content in mmc3 | **All IHC score columns (L–Z), including all three IL-33 columns, are hidden** (E37). | The programme's key tissue readout is invisible in the delivered view. | Same. |
| 9 | Tissue scores are transformed and partly undocumented | The numeric scores equal the raw "n+" score + 0.5 in all 74 rows, exceeding the stated 0–5 scale: IL-33 endothelium is 5.5 in 39/74 blocks. IL-33 scores are averages of unrecorded sub-scores (live formula `=(2+4.5)/2`). No raw IL-33 scores exist. A single reader scored everything with no blinding recorded (E36). | Ceiling effect; ordinal data treated as interval. | Blinded two-reader re-scoring with an unbounded digital metric. |
| 10 | Tissue table structure errors | One merged cell carries the SARS-CoV-2 status of **two donors** (1910 and 1905). Lung-condition notes for donors 2045 and 2040 sit on the second block, contrary to the annex. Donor IDs mix number and text types (E38). | Anyone extracting "first block" fields gets donor data wrong. | Reissue as tidy long format. |
| 11 | **Tissue group labels contradict the autopsy text** | 4/10 "COVID− pneumonia" donors have no pneumonia in their diagnoses (1905, 1970, 1968, 1961). 2/5 "non-pneumonia" donors have pneumonia or pneumonitis (1956, 1976), and one has pulmonary coccidioidomycosis (1944) (E39). | The control groups are not what they say they are. | Pathologist re-adjudication before any reuse. |
| 12 | Test-article identity and epithelial design | "Compound_47" is never linked to AX-1177. Epithelial arms use PBS *and* DMSO vehicles and were never given IL-33. | The in vitro evidence may not apply to AX-1177. | Provide identity, lot and formulation documentation. |

---

## 4. Forward plan: what we'd measure, in which model, when

The gates run partly in parallel, and the thresholds are set before any data come in. The thresholds are **proposals** for the committee to ratify; they are not findings. Exposure-based criteria need the biologics file, which is not in this package.

### Gate 0: traceability and re-analysis (weeks 0–6; no new lab work)

| What | How | Pass | Kill |
|---|---|---|---|
| Prove C47 is AX-1177 | Sequence, lot, certificate of analysis, formulation; affinity, potency and species cross-reactivity from the biologics file | Documented identity | No link and no AX-1177 lot → repeat the core HUVEC experiment with AX-1177 before spending anything else |
| RNA-seq re-analysis | Per-cell-line fits from archived counts; reconcile the 114-vs-113 library question; IL-33 vs isotype in HGMEC (estimable from counts) | ≥80% inhibition of the IL-33-induced programme at 6 h is reproduced (this review: 98.6%); valid statistics for SELE, VCAM1, CXCL8, CXCL1, CCL2, PTGS2, IL1RL1 | Inhibition <50% |
| Full serum release | All 1,194 tests, raw NPX, below-detection flags; IL-33 status; ORs per SD; deduplicated | Complete data; IL-33 result known | — (feeds Gate 2) |

### Gate 1: pharmacology in disease-relevant human systems (months 1–4)

**Models.** Two pieces of design rationale:
- The current cells are umbilical-vein and kidney endothelium. They should be replaced with **primary human lung microvascular endothelial cells (≥3 donors)**, keeping HUVEC as a bridge to the existing data.
- Add **primary human bronchial epithelium grown at an air–liquid interface (≥3 donors)** and an **epithelium–endothelium co-culture (transwell or lung-on-chip)**. Optionally add human precision-cut lung slices.

**What we'd measure, and when.**
- **Potency.** An 8-point AX-1177 concentration series (about 0.03–300 nM), tested against IL-33red **and** oxidised IL-33. The IL-33 dose is set at 80% of its maximal effect, so IL-33 needs its own dose–response first; the package never justified 30 ng/mL. Test with concurrent addition and with pre-incubation.
- **Readouts at 6 h and 24 h.** These are the two timepoints where the signature was defined; inhibition was weakest at 24 h.
  - secreted GM-CSF, G-CSF, IL-6, CCL20, CXCL10, OPG, tissue factor;
  - surface E-selectin, VCAM-1 and ICAM-1 by flow cytometry, which recovers the genes issue 3 made unevaluable;
  - a targeted ~50-gene panel taken from this signature.
- **Endogenous, virus-induced IL-33.**
  - Infect the airway epithelium with influenza A, RSV and SARS-CoV-2 (the last at containment level 3).
  - Measure free IL-33 in the apical and basal media at 24, 48 and 72 h.
  - Transfer the medium, or co-culture, onto lung endothelium with AX-1177 or isotype, and measure the endothelial panel at 6 h and 24 h.
- **Antiviral safety in vitro.** Viral titre and interferon output in the infected epithelium with and without AX-1177. Interferon-γ from CD8 T cells and NK cells in blood-cell assays, with IL-33 ± AX-1177.

**Gate criteria.**
- **Pass:** all of the following.
  - IC90 is at or below the projected trough exposure (to be set once PK/biologics data arrive).
  - ≥80% inhibition of the secreted panel at 6 h and ≥70% at 24 h, against both IL-33 forms.
  - Virus-induced IL-33 release is detectable, and AX-1177 cuts its endothelial effect by ≥50% versus isotype.
  - Viral titre rises by no more than 0.5 log10.
- **Kill:** infected human epithelium releases no detectable IL-33 *and* the co-culture has no AX-1177-sensitive component.

### Gate 2: human disease linkage from existing material plus a new cohort (months 1–6, parallel)

**1. Existing biobank (100 sera at −80 °C, enrolment samples).**
- Measure **free IL-33, total IL-33 and sST2** with validated immunoassays of documented sensitivity.
- Reuse the same adjusted logistic model, with ORs per SD and the gain in AUC over NEWS2.
- Use the results to set a candidate **sST2/IL-33 enrichment threshold**.

**2. Existing tissue.**
- Blinded two-reader re-scoring of IL-33 staining with an unbounded digital metric (H-score or % positive nuclei), recording nuclear vs cytoplasmic/extracellular staining to capture release.
- Pathologist re-adjudication of the group labels (issue 11).
- Score the **archived tissue RNA** (the `Tissue RNA` IDs Zr4940_\*) for the HUVEC IL-33-induced, C47-reversible signature, per donor, COVID+ vs COVID− pneumonia.

**3. New prospective cohort.**
- Multi-pathogen viral LRTD (influenza, RSV, SARS-CoV-2, hMPV), hospitalised adults, several centres, current era.
- Serial samples at admission, 24–48 h, day 3 and day 7: free IL-33, sST2, the candidate PD panel (§2.3), and injury markers (PTX3, vWF, ANGPT2, sE-selectin).
- This fixes PD variance and enrichment for Phase 2a.
- Indicative size: **~230–290 patients** to confirm an OR of 1.5 per SD at a 30% event rate with 80% power (98 patients if OR = 2.0).

**Gate criteria.**
- **Pass:**
  - free IL-33, or the IL-33/sST2 axis, predicts the composite endpoint independently of NEWS2 in the biobank, and replicates in direction in the new cohort, including non-COVID viruses;
  - **and** the IL-33 signature is higher in COVID+ than COVID− pneumonia lung RNA.
- **Kill:** IL-33 is undetectable or unrelated to outcome **and** no tissue signature is found.

### Gate 3: in vivo efficacy and antiviral safety (months 3–9)

**Prerequisite.** Species cross-reactivity from the biologics file. If AX-1177 does not bind rodent IL-33, use a surrogate anti-mouse IL-33 antibody matched for redox-form specificity, or a human-IL-33 knock-in mouse.

**Models** (standard choices; design rationale, not findings):
- **mouse influenza A (PR8)** as the primary model;
- **SARS-CoV-2 in Syrian hamster or K18-hACE2 mouse** as the second, which matches the human data;
- RSV optional.

**Arms.**
- Isotype versus ≥2 AX-1177 doses.
- **Prophylactic** dosing at day −1 and **therapeutic** dosing at day +2 to +3 after infection, which models presentation to hospital.
- Randomised, with blinded scoring. Group sizes from a pilot: indicatively 10–12 per arm for survival and weight, 6–8 per timepoint for tissue.

**What we'd measure, and when.**
- **Days 1, 3, 5, 7, 10, with survival to day 14–21:**
  - drug levels (PK);
  - free/total IL-33 as target engagement (the target is ≥90% suppression of free IL-33);
  - sST2;
  - G-CSF, GM-CSF, IL-6, CCL20, CXCL10 and KC in lung fluid and serum.
- **Day 7 primary endpoint: vascular leak** (lung-fluid protein/albumin, lung wet:dry ratio). Also lung endothelial E-selectin/VCAM-1/ICAM-1 by flow cytometry, and blinded histopathology.
- **Throughout:** weight, oxygen saturation, survival.
- **Safety:**
  - viral titre by plaque assay and viral RNA on days 3, 5 and 7;
  - virus-specific CD8 T cells on days 7–10;
  - surveillance for secondary bacterial infection.

**Gate criteria.**
- **Pass:**
  - therapeutic dosing reduces day-7 vascular leak or lung injury score by ≥30% versus isotype, with a dose–response, in ≥1 model and in the same direction in the second;
  - ≥90% free IL-33 suppression at the effective dose;
  - viral titre rises by no more than 0.5 log10, and clearance is not delayed.
- **Kill:** no benefit from therapeutic dosing in either model, or higher viral burden.

**Decision point (about month 9).** IND-enabling work starts only if Gates 0–3 all pass. If Gates 1 and 2 both fail, stop the programme.

**Timing principle.** The in vitro response is largest at 6 h (4,031 vs 1,836 genes at 24 h), and neutralisation is most complete when the antibody is present from the start. Everything therefore points to **early** intervention and early PD sampling. The in vivo therapeutic-window arms test how late dosing can start and still work.

---

## 5. What goes into the clinic (only if Gates 0–3 pass)

**5.1 Clinical entry package.**
- GLP toxicology in a pharmacologically relevant species, chosen by cross-reactivity.
- CMC.
- A PK/PD model linking exposure to ≥90% free IL-33 suppression through day 7.
- Validated assays for free/total IL-33, sST2 and the PD panel.
- The fixed data package from §3.

**5.2 First-in-human.** Single and multiple ascending doses in healthy volunteers, measuring:
- safety, PK and anti-drug antibodies;
- target engagement: rise in total IL-33 as drug–IL-33 complex, and suppression of free IL-33.

**5.3 Phase 2a proof-of-mechanism in hospitalised viral LRTD.**

*Population.*
- Adults with PCR-confirmed viral LRTD (multi-pathogen), randomised within 48 h of admission. That matches the cohort's enrolment sampling and the early-intervention principle.
- Stratified by NEWS2, the covariate used in the cohort.
- **Enriched by sST2 and/or free IL-33** above the Gate-2 threshold.

*Treatment.*
- Randomised, double-blind, single IV dose of AX-1177 vs placebo on top of standard care.
- Dose chosen by the PK/PD model.

*Primary endpoint (pharmacodynamic).*
- Change from baseline to day 3 (with 6 h, 24 h and day 7 also sampled) in a composite score of the **package-derived PD panel**: IL-6, OPG, CCL20, MCP-3, IL-1β, tissue factor, CSF-1 and sIL-18R1.
- These are the serum proteins that are IL-33-inducible, C47-reversible and outcome-associated (§2.3).
- Free IL-33 serves as co-primary target-engagement readout.

*Secondary endpoints.*
- The cohort's composite endpoint (ICU/invasive ventilation/death by day 30).
- Ordinal clinical status and oxygen-free days.
- Endothelial injury markers: PTX3, vWF, ANGPT2, sE-selectin.

*Safety.*
- Quantitative viral load on days 1, 3, 5 and 7, with a pre-set threshold for unblinded review.
- Secondary infections; anti-drug antibodies.

*Size.*
- Sized on the PD endpoint, using the variance from the Gate-2 prospective cohort; indicatively 40–60 per arm.
- **A Phase 2a cannot be powered on outcomes.** At 80% power and two-sided α = 0.05, an outcome-powered trial needs:

| Control event rate | Assumed effect | Treated event rate | Patients per arm |
|---|---|---|---|
| 44% (this cohort) | 1/3 relative reduction | 29.5% | **172** |
| 30% | 1/3 relative reduction | 20.1% | **300** |
| 20% | 1/3 relative reduction | 13.4% | **501** |

The cohort's 44% comes from hospitalised COVID-19 before vaccination; today's event rates will be lower.

*Stop rule.* Target engagement is reached (≥90% free IL-33 suppression) but the PD composite doesn't move versus placebo → stop.

---

## 6. Requests to the programme team before the next review

1. Identity documentation linking Compound_47 to AX-1177, plus the biologics file (affinity to both IL-33 forms, potency, species cross-reactivity).
2. Count matrices and per-sample QC. Which library or covariate explains 75 residual df? The reference arm for mmc4 ("Vehicle" vs "Nontreated").
3. The complete serum proteomics release: 1,194 tests, raw NPX, below-detection flags, the exclusion rule, and whether IL-33 was run.
4. The tissue raw IL-33 sub-scores, the scoring SOP, reader blinding, a reconciliation of group labels with pathology, and access to the archived tissue RNA.
5. Patient-level clinical data: time from symptom onset to sampling, treatments, and vaccination/variant context.

---

## 7. How the analysis was done, and its limits

**Transcriptomics.**
- Parsed all 26 contrasts (26,210 genes each).
- Checked internal consistency: AveExpr identical across contrasts, adjusted p-values reproduced to 7×10⁻¹⁴, t→p inverted for df.
- Defined IL-33 signatures: FDR 5% and >2-fold (|log2FC| > 1) change.
- Measured neutralisation with contrasts that share no samples, plus cross-timepoint selection against winner's curse.
- Derived leftover IL-33 effects exactly from the additive fold-changes.
- Flagged gene-level SE problems against a rolling, expression-matched median.
- Ran Hallmark enrichment with Fisher tests (MSigDB via msigdbr).

**Serum proteomics.**
- Rebuilt the multiple-testing adjustment and worked back from it to count withheld tests.
- Mapped and deduplicated assays by an outcome-blind rule: least missingness, then a fixed panel order.
- Checked Wald CI–p agreement (exact).
- Tested enrichment with Fisher and Mann–Whitney tests; ran rank regression with covariates.

**Tissue.**
- Read merged cells and hidden columns from the workbook XML.
- Parsed the "n+" scores and verified the derived-score rule.
- Analysed at donor level: Kruskal–Wallis, Mann–Whitney and permutation tests; Hodges–Lehmann median shifts with bootstrap CIs; Cliff's delta.
- Sensitivity checks: mixed models with a donor random intercept, and label-concordant subsets.

**Limits.**
- I could not refit the RNA-seq from counts or re-model the serum data from patient-level values; neither is in the package. The corrected estimates above therefore rest on the delivered summary statistics.
- The gene-bootstrap CIs ignore correlation between genes, so they are optimistic.
- Two findings are inferences from the statistics rather than documented facts: the 100 withheld tests (from inverting the adjustment) and the ≤75 residual df (from inverting t→p). Both are internally exact, but they should be confirmed by the data owner.
- "IL-33-induced" refers to transcript changes in HUVEC; whether the protein appears in serum is assumed, not shown.

**Figures.**
- `figures/fig1_neutralisation.png`: C47 effect against the IL-33 effect, per gene, for HUVEC 6 h, HUVEC 24 h and HGMEC 6 h.
- `figures/fig2_variance_pathology.png`: the single-model variance problem.
- `figures/fig3_serum_link.png`: serum severity associations and the enrichment test.
- `figures/fig4_tissue_IL33.png`: donor-level IL-33 staining.
- `figures/fig5_undelivered_tests.png`: withheld serum tests, worked back from the adjusted p-values.

Full file index: `/tmp/outputs/README.md`.
