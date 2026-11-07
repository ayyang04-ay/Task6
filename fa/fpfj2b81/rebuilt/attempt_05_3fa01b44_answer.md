**Recommendation: NOT YET. Do not start clinical development of AX-1177 for viral LRTD on this package. Instead, fund a gated translational programme of about 12 months with pre-specified stop rules. The first go/no-go comes at about 3 months and uses material we already hold.**

---

# AX-1177 (anti-IL-33 mAb), viral lower respiratory tract disease: programme committee proposal

**Evidence base.** This review uses only the mounted package: the methods annex and `mmc2`–`mmc5`. Every number below comes from those files or from re-analysis of them. The scripts and outputs are in `/tmp/outputs/analysis` and the figures in `/tmp/outputs/figures`. Where I used general biological background to interpret a result, I label it as *background*. Where I inferred something the package does not state, I label it as *inferred*.

## 1. Decision summary

**What the package establishes**

1. **In vitro neutralising pharmacology (strong).**
   - In HUVEC, reduced IL-33 (IL-33red, 30 ng/mL) induces a large NF-κB, inflammatory and interferon programme:
     - 4,031 genes change at FDR < 5% by 6 h;
     - Hallmark TNFα→NF-κB gene set NES 3.12, padj 2×10⁻⁵⁸.
   - Compound_47, at 10 µg/mL (a 41-fold molar excess), removes that programme:
     - neutralisation is **92% (95% CI 86–99%) and 98% (93–104%)** when estimated in a way that controls for selection bias;
     - it is **96–100%** for the most strongly induced genes.
   - The same programme is reversed in glomerular endothelium (HGMEC).
   - The antibody alone has no reproducible transcriptional effect in any of the four cell types tested.
2. **A prognostic signal on the IL-33 decoy receptor (moderate, but not specific).**
   - Among 1,063 unique serum proteins measured in 100 patients hospitalised with COVID-19, soluble ST2 at enrolment ranks **2nd** for the outcome of ICU admission, invasive mechanical ventilation (IMV) or death.
   - OR **3.02 (95% CI 1.83–5.01) per log unit**, adjusted for age, sex and NEWS2; BH q = 0.009.

**What the package does not establish**

3. **That IL-33 is raised or released in viral LRTD.**
   - IL-33 itself was never measured in serum.
   - In post-mortem lung, IL-33 staining is *not* higher in COVID-19. Donor-level endothelial medians are 4.8 (COVID+) vs 5.5 vs 5.5 (controls); Kruskal–Wallis p = 0.16.
   - The assay is also at its ceiling in controls, so it could not have detected an increase.
4. **That the IL-33-driven endothelial programme is active in patients.**
   - Serum proteins whose genes IL-33 induces in HUVEC are no more outcome-associated than any other protein: 19.3% vs 19.3% significant; Fisher p = 1.0.
5. **Anything beyond SARS-CoV-2 in vitro biology.** The package contains:
   - no in vivo efficacy;
   - no virus other than SARS-CoV-2;
   - no PK, dose rationale or safety data;
   - no document linking test article "Compound_47" to AX-1177.

**Data-integrity problems to fix before any of these results is quoted outside the team**

- **(a) Transcriptomics model.** The single pooled limma model (annex §5) produced numerically impossible statistics for ≥164 genes. These include the headline endothelial markers SELE, VCAM1, CXCL8 and CXCL1, and the receptor itself, IL1RL1/ST2.
- **(b) Missing serum assays.** The serum multiplicity correction implies 1,194 tests, but only 1,094 assays were delivered. The 100 missing assays include ≥5 with p < 0.01.
- **(c) Double counting.** 27 serum proteins are counted on 2–4 panels.
- **(d) IHC scoring.** Scores exceed the documented 0–5 scale (53% of endothelial block scores are 5.5), and blocks (1–8 per donor) were not independent samples.

**Why not "Go"**
- The disease hypothesis (IL-33 drives progression of viral LRTD) rests on one indirect human datapoint (sST2).
- Against it sit one non-supportive tissue dataset and one null specificity test.
- There is no in vivo efficacy, no PK, no safety data and no evidence for other viruses.
- The package also raises a specific safety question. In endothelium, IL-33 switches on antiviral genes (CXCL10 +6.9, IFIH1 +2.4, DDX58 +1.6, MX1 +1.9 log₂FC at 6 h), and the antibody removes them. Viral clearance therefore has to be checked before we dose infected patients.

**Why not "Stop"**
- The molecule behaves well: potent, essentially complete neutralisation and a clean profile when given alone.
- sST2 is the strongest IL-1-family signal in the serum panel. An unmeasured confounder would need a risk ratio of about 2.9 with both sST2 and the outcome to explain it away (E-value).
- The IHC null cannot rule out IL-33 release, because the assay was saturated.
- The decisive uncertainties can be tested quickly with material the annex says already exists:
  - the banked enrolment sera;
  - tissue RNA from 22 post-mortem donors;
  - the archived count matrices;
  - the biologics file.

---

## 2. The evidence chain, link by link

| Link needed for a clinical programme | What the package shows (key numbers) | Verdict |
|---|---|---|
| 1. IL-33 activates the relevant cell | HUVEC at 6 h: 4,031 DE genes, 1,068 with \|log₂FC\| ≥ 1. Top genes are NF-κB targets (NFKBIA t = 44; TNFAIP3 +4.75; TRAF1 +5.89) and leukocyte chemokines/CSFs (CSF2 +10.3, CXCL6 +9.4, CCL20 +9.2, CX3CL1 +8.4, CSF3 +8.3). The response is smaller at 24 h (1,836 DE genes). Only one donor per cell type, no lung microvascular endothelium, exogenous IL-33red only. | **Supported in vitro**, in a non-lung, single-donor system |
| 2. AX-1177 blocks it | Neutralisation 92–100% (bias-controlled, isotype-matched). The isotype arm keeps 94–103% of the IL-33 response. Tested at a single concentration and a 41:1 molar ratio, so no IC₅₀/IC₉₀. | **Supported** (efficacy at saturation, not potency) |
| 3. AX-1177 is inert without IL-33 | Across 8 cell × time contrasts, 21–73 FDR hits each. The hits are mostly low-expressed (56–91% with AveExpr < 0), almost never recur (3 genes in ≥ 2 contrasts) and show no cross-contrast correlation (ρ −0.10 to 0.05) or relation to the IL-33 programme (ρ −0.08 to 0.03). | **Supported** |
| 4. IL-33 is released/elevated in viral LRTD | Serum IL-33 not measured. Post-mortem IHC shows no increase (section 3.4). | **Not shown** |
| 5. The IL-33 axis is linked to poor outcome | sST2 OR 3.02 (1.83–5.01), rank 2/1,063. But 193/1,063 proteins pass FDR 5% (190 with OR > 1), so the whole proteome tracks severity. | **Partially**: prognostic, not causal or specific |
| 6. The IL-33-driven programme is active in patients | Bridge test null (19.3% vs 19.3%; Mann–Whitney p = 0.80) | **Not shown** |
| 7. Blocking IL-33 improves disease in vivo | No data | **Not addressed** |
| 8. Viral LRTD beyond SARS-CoV-2 | All human data are from pre-vaccination COVID-19, single centre | **Not addressed** |
| 9. Dose, PK, safety, identity of test article | Not in package. Affinity/potency are "held in the biologics file" (annex §1). "Compound_47" is never linked to "AX-1177". | **Not addressed** |

---

## 3. Findings

### 3.1 In vitro pharmacology (mmc4, mmc5)

**Design (annex §1–3)**
- Four cell types:
  - HUVEC and HGMEC are primary cells, each from a **single donor** (P2 and P5);
  - A549 and MCF7 are cancer lines.
- 38 arm × time groups with n = 3 each (114 libraries), all run in one batch.
- IL-33red was given at 30 ng/mL, which is **1.66 nM**. Compound_47 and the NIP228 isotype were given at 10 µg/mL, which is **68.5 nM**. That is a **41:1 IgG:IL-33 ratio, or 83:1 counting binding sites**. The antibody was added at the same time as IL-33, with no pre-incubation.
- The epithelial lines were **never exposed to IL-33**. In HGMEC there is **no vehicle arm**, and no HGMEC IL-33-effect contrast was delivered.

**IL-33 response, HUVEC, IL-33red vs vehicle**

| | 6 h | 24 h |
|---|---|---|
| FDR < 5% (up / down) | 4,031 (2,191 / 1,840) | 1,836 (1,281 / 555) |
| FDR < 5% and \|log₂FC\| ≥ 1 | 1,068 | 512 |

- Only 181 genes pass at both timepoints (173 in the same direction). The early NF-κB wave fades, and later genes such as C3 rise (+4.8 at 6 h, +6.1 at 24 h).
- The Hallmark sets enriched at 6 h are TNFα→NF-κB (NES 3.12), IFN-γ (2.81), inflammatory response (2.70), IFN-α (2.70) and IL-6/JAK/STAT3 (2.59), all padj ≤ 3×10⁻¹⁵ (`04_hallmark_fgsea_all.csv`).

**Neutralisation**

The primary readout compares (IL-33 + Compound_47) with (IL-33 + isotype). These two arms share no cultures with the IL-33-vs-vehicle estimate.

*Why the naive estimate is biased.* If you define the IL-33 signature and measure its reversal in the same cultures, you suffer winner's-curse bias. That naive approach gives 79% neutralisation at 6 h and 69% at 24 h. It also makes the isotype look as if it removes 21–31% of the IL-33 response.

*How I corrected it.* I selected signature genes at one timepoint and evaluated them in the independent cultures of the other timepoint (`03_neutralisation_crossselected.csv`):

| Genes selected at → evaluated at | Genes | % of IL-33 response removed by Compound_47 (95% CI*) | Isotype-arm response as % of IL-33 alone |
|---|---|---|---|
| 6 h → 24 h | 1,067 | **92.1%** (85.5–99.2) | 94.3% (87.9–101.4) |
| 24 h → 6 h | 512 | **98.1%** (92.5–104.3) | 102.9% (97.8–108.4) |
| Strongest genes (\|t\| ≥ 10), 6 h → 24 h | 270 | **100.3%** (96.3–104.6) | 88.8% (86.4–91.3) |

\*The CIs come from bootstrapping over genes. They do **not** include variation between cultures, which cannot be estimated without the count matrix (annex §5).

Key genes at 6 h (log₂FC with FDR in brackets):

| Gene | IL-33 vs vehicle | C47 vs isotype (+IL-33), HUVEC | same, HGMEC | C47 alone vs isotype |
|---|---|---|---|---|
| CSF2 | +10.30 (5×10⁻²³) | −12.21 | −7.10 | −0.36 (1.0) |
| CCL20 | +9.21 (3×10⁻²⁰) | −9.84 | −5.55 | −0.01 (1.0) |
| CXCL6 | +9.41 (3×10⁻¹⁵) | −8.14 | −3.86 | −0.78 (1.0) |
| CSF3 | +8.32 (2×10⁻¹⁸) | −8.28 | −6.51 | +0.34 (1.0) |
| CXCL10 | +6.89 (7×10⁻¹⁸) | −7.51 | −2.82 | +0.01 (1.0) |
| IL6 | +5.82 (2×10⁻¹³) | −5.97 | −2.86 | +0.07 (1.0) |
| ICAM1 | +5.97 (0.010) | −5.91 | −5.40 | +0.07 (1.0) |
| TNFAIP3 | +4.75 (3×10⁻⁴⁵) | −4.81 | −3.67 | +0.01 (1.0) |

**HGMEC**
- With IL-33 present, Compound_47 vs isotype changes **1,457 genes at 6 h** and 269 at 24 h.
- It reverses the HUVEC IL-33 signature: Spearman −0.53; 311 of 1,067 signature genes are significantly reversed; Fisher OR 10.3.
- Because HGMEC has no vehicle arm, neither the size of its IL-33 response nor the completeness of neutralisation can be estimated.

**Interferon programme (safety-relevant)**
- IL-33 induces interferon-stimulated genes in HUVEC: CXCL10 +6.89, IFIH1 +2.36, DDX58 +1.59, MX1 +1.91, IFIT1 +1.94 at 6 h; MX1 +2.49 and RSAD2 +2.60 at 24 h.
- Compound_47 reverses them (for example, CXCL10 −7.51).
- *Background:* in a virally infected patient, this could reduce local antiviral priming. It is testable, so viral load has to be a safety endpoint (section 4).

### 3.2 Integrity and methodology of the transcriptomic deliverables

1. **The pooled model produced invalid gene-level statistics.**
   - Each reported SE can be recovered as |logFC / t|. The median is 0.34 log₂ units.
   - 164 genes have SE > 5 in at least one contrast. Extreme values include CD93 at 16,536, CXCL1 at 1,155 and CDH5 at 926 (Fig. 2).
   - Within one model and the same 3-vs-3 design, a gene's SE varies across contrasts by up to 225,439-fold. AKR1C2, for example, has SE 0.0006 in A549 but 146 in HUVEC. 515 genes vary more than 10-fold (`02_SE_range_across_contrasts.csv`).
   - The affected genes are ones with extreme, cell-type-restricted expression:
     - endothelial: CDH5, CD93, VWF, PECAM1, KDR;
     - MCF7: TFF1, GATA3, XBP1, KRT8;
     - A549: AKR1C2/3, ALDH3A1, NQO1.
   - That pattern is what you would expect from fitting **one** voom/limma model across four unrelated cell types, with precision weights and residual variance pooled across them (annex §5). I cannot confirm the exact mechanism without the archived counts.
   - *Consequences:*
     - The delivered p-values for **SELE (+11.2 log₂FC, P = 0.21), VCAM1 (+8.7, P = 0.22), CXCL8 (+8.2, FDR 0.19), CXCL1 (+8.2, P = 0.99), CCL2, PTGS2, PTX3 and IL1RL1** cannot be interpreted, either way.
     - Conversely, some "hits" come from implausibly small SEs. For example, DCBLD2 in A549 has log₂FC 0.09 with SE 0.002.
     - My signature-level analyses use log₂FC (a difference of group means, which is essentially unaffected) and exclude the 164 flagged genes.
2. **mmc5 is duplicated and mislabelled.** The sheets labelled "6h" and "24h" are identical copies: 24 contrasts covering *both* timepoints, with zero numerical difference. mmc4 sheets say "Vehicle"; their rows say "Nontreated".
3. **Other checks passed.**
   - BH adjustment within each contrast reproduces exactly (max difference 5×10⁻¹⁵).
   - AveExpr is identical across all contrasts, which is consistent with one fit. (Because AveExpr is averaged over all 114 libraries, it says nothing about endothelial expression.)
   - Contrast labels agree with the biology: on the 4,946 IL-33-responsive genes, the 6 h signature correlates ρ = −0.80 with the 6 h reversal and ρ = −0.43 with the 24 h reversal.
4. **Design limits that matter for translation.**
   - One donor per primary cell type.
   - No lung microvascular endothelium and no primary airway epithelium.
   - No virus anywhere in the system.
   - Only the reduced form of IL-33, although Compound_47 is described as binding the oxidised form too.
   - One dose level, so no potency estimate.
   - A DMSO "vehicle" arm, which is irrelevant to an antibody.

### 3.3 Clinical serum proteomics (mmc2)

**Cohort**
- 100 patients hospitalised with COVID-19, from a single centre in the pre-vaccination period.
- *Inferred:* 44 had the composite endpoint and 56 did not. The undocumented columns `composite_endpoint_1` and `composite_endpoint_0` contain only exact multiples of 1/44 and 1/56, which is most likely the fraction below the limit of detection per group.
- That gives **11 events per variable** for the 4-parameter models, which is adequate.
- The delivered ORs and CIs are internally consistent Wald estimates (CI midpoint = log OR to 10⁻¹⁴).

**Integrity**

| Issue | Evidence | Consequence |
|---|---|---|
| Multiplicity base ≠ delivery | Top assay adj p / p = **1,194.0**. The BH ranks imply 100 analysed assays are missing, including at least 1 with p between 2.1×10⁻⁴ and 3.1×10⁻⁴, at least 5 with p < 0.01 and at least 15 with p < 0.05. | We cannot confirm that the IL-33-axis assay set is complete. This contradicts annex §6 ("across all assays in the delivery"). |
| Cross-panel duplicates | 1,094 rows = **1,063 proteins**. 27 proteins appear on 2–4 panels (IL6 ×4, with ORs 2.07–2.31). | 178 delivered "hits" are 169 distinct proteins. After re-applying BH across 1,063 unique proteins, **193** pass FDR 5% (186–194 depending on which duplicate is kept). |
| OR scale | "Per log unit" on assays with different dynamic ranges (e.g. CSF-1 OR 90 [4–1,933]) | Compare proteins by rank or p-value, not by OR size. |

**IL-33 axis**

| Protein | OR per log unit (95% CI) | q (BH across unique proteins) |
|---|---|---|
| sST2 | **3.02 (1.83–5.01)**, rank 2/1,063 | **0.009** |
| IL-33, IL1RAP | **not measured** | — |
| IL-1RT2 (IL1R2 decoy) | 4.52 (1.95–10.47) | 0.020 |
| IL-18R1 | 6.07 (2.23–16.53) | 0.020 |
| IL1B | 2.45 (1.28–4.66) | 0.044 |
| IL-1RT1 | 1.80 (0.84–3.88) | 0.27 |

- Other IL-1-family receptors and decoys track outcome in the same way, which fits a general shedding/severity pattern rather than anything specific to IL-33.
- Endothelial injury markers are prognostic: PTX3 11.6 (q = 0.012), vWF 3.86 (q = 0.048), ANGPT2 2.21 (q = 0.0495).
- But activation markers are weak: SELE 2.08 (q = 0.087), ICAM1 1.67 (q = 0.24), VCAM1 1.28 (q = 0.60).
- sST2 E-value is **2.87** (2.04 at the lower confidence bound). A confounder such as cardiac strain or sepsis would need a risk ratio of about 2.9 with both sST2 and the outcome to explain the association away.

**Bridge test** (`05_olink_bridge_IL33_induced_genes.csv`, Fig. 3)
- *Question:* are serum proteins whose genes IL-33 induces in HUVEC more outcome-associated than the rest? If an IL-33→endothelium mechanism were active in these patients, they should be.
- *Set-up:* of 865 proteins whose genes were tested in the RNA-seq, 88 are IL-33-induced (FDR < 5%, log₂FC ≥ 1 at either timepoint).
- *Result:* they are not enriched.
  - 17/88 (19.3%) vs 150/777 (19.3%) at FDR 5%; Fisher OR 1.00, p = 1.0.
  - Median Wald z 1.38 vs 1.49; Mann–Whitney p = 0.80; permutation p = 0.96.
- The most strongly induced genes show no serum association:
  - CXCL6 (+9.4 in vitro): OR 1.02, p = 0.95;
  - G-CSF/CSF3 (+8.3): OR 1.25, p = 0.23;
  - CXCL5 (+5.3): OR 1.17, p = 0.52.
- *Caveat:* serum proteins come from many tissues. This test speaks to *specificity*; it does not show that IL-33 is absent.

### 3.4 Post-mortem lung IHC (mmc3)

**Handling**
- There is one row per block, and donor-level fields appear only on each donor's first block, so I forward-filled them within donor.
- Donor 1905's SARS-CoV-2 cell is an Excel merge spanning donors 1910 and 1905; the value is "neg", consistent with its category.
- **The donor is the unit of analysis.**

**Sample**

| | COVID+ pneumonia | COVID− pneumonia | COVID− non-pneumonia |
|---|---|---|---|
| Donors | 16 | 10 | 5 |
| Blocks | 49 (3 donors supply 24 of these) | 15 | 10 |

- Donors are all White, with median age 82–84.
- Chronic airway disease is recorded in 12/16 COVID+, 4/10 COVID− pneumonia and 3/5 non-pneumonia donors. The "controls" are therefore not normal lungs.

**Scoring integrity**
- The scale is documented as 0–5, but grades written "n+" were coded as n + 0.5 in every one of 74, 71 and 71 entries checked, so "5+" becomes 5.5.
- The IL-33 values are averages of two components coded inconsistently. Cell X2 still holds the formula `=(2+4.5)/2`.
- **53% of endothelial block scores (39/74) and 23% of epithelial scores (16/71) are 5.5**, above the stated maximum.
- There is a single reader; blinding is not documented.

**Results (donor-level medians; Kruskal–Wallis across 3 groups)**

| Compartment | COVID+ | COVID− pneumonia | non-pneumonia | KW p |
|---|---|---|---|---|
| Endothelium | 4.81 | 5.50 | 5.50 | 0.16 |
| Basal bronchial epithelium | 4.25 | 4.50 | 4.88 | 0.61 |
| Vascular smooth muscle | 2.38 | 3.25 | 3.50 | 0.18 |

- All 9 pairwise IL-33 comparisons have Holm-adjusted p ≥ 0.97. Any trend points **down** in COVID-19, not up.
- **Ceiling.** Endothelial donor medians are already at the maximum in 4/5 non-pneumonia and 6/10 COVID− pneumonia donors. An increase was therefore undetectable by design.
- **Pseudo-replication.** Analysing blocks instead of donors would have produced "significant" results: endothelium COVID+ vs non-pneumonia p = 0.011 (donor level 0.11); VSM p = 0.009 (donor level 0.13).
- **Inflammatory cells.**
  - Eosinophil (EDN, MBP), neutrophil-elastase and IL-5Rα grades are higher in *both* pneumonia groups than in non-pneumonia controls, with donor-level p between 0.005 and 0.03.
  - None differ between COVID+ and COVID− pneumonia (p 0.44–0.98).
  - None correlate with IL-33 after BH correction (minimum q = 0.26).

**Unused resource.** RNA has been extracted from 22 blocks from 22 donors (IDs Zr4940_*: 9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia), but no expression data were delivered.

---

## 4. The plan: what we'd measure, in which model, and when

All thresholds below are proposed decision criteria and should be fixed before the data are unblinded. Whether AX-1177 cross-reacts with rodent IL-33 is in the biologics file, not in the package, and that determines the in vivo reagent.

### Gate A, months 0–3: decide with material already held (low cost)

| # | Question | What we measure | Material / model | Timing of measurement | Go criterion | Stop trigger |
|---|---|---|---|---|---|---|
| A1 | Is IL-33 itself elevated, and does it add to sST2? | IL-33 (reduced; oxidised/total), IL-33:sST2 complex, sST2 | The 100 banked enrolment sera (annex §6: stored at −80 °C) | Enrolment (the only timepoint available) | Association with the package composite endpoint in the package's model (age, sex, NEWS2), and still present after adding IL-6. Use Firth regression if EPV falls below 10. | No IL-33-form or complex association (OR 95% CI includes 1), **and** A2 null → recommend stopping this indication |
| A2 | Is the IL-33 response programme active in diseased lung? | IL33, IL1RL1, and a score from the 1,067-gene HUVEC IL-33 signature | The 22 existing tissue RNA samples | Post-mortem | Signature score higher in COVID+ / pneumonia than non-pneumonia, at donor level, in the direction pre-specified | Opposite direction |
| A3 | Are the in vitro claims robust? | Re-fit each cell line separately from the archived counts. Re-test SELE, VCAM1, CXCL8, IL1RL1 and the neutralisation estimates. | Archive (annex §5) | — | Neutralisation ≥ 80% at both timepoints; no gene set moved by antibody alone in ≥ 2 cell types | Neutralisation < 80% |
| A4 | Identity, potency, species | Documents showing Compound_47 = AX-1177 (sequence, lot, certificate of analysis, endotoxin); affinity for IL-33red and IL-33ox; IC₅₀; cross-reactivity | Biologics file | — | Identity confirmed | Identity not confirmable |
| A5 | Is the serum record complete? | Identity of the 100 analysed but undelivered assays; "log" definition (NPX vs linear) | Proteomics data owner | — | Disclosed | — |

### Gate B, months 3–12: human validation, disease models and efficacy in living animals

| # | Question | Measure | Model | When | Go criterion |
|---|---|---|---|---|---|
| B1 | Is the signal present across viruses, and does it appear early enough to treat? | IL-33 forms, IL-33:sST2, sST2, endothelial panel (ANGPT2, vWF, PTX3 and sE-selectin, all already prognostic or measured in mmc2), IL-6, viral load | Hospitalised viral LRTD cohort (prospective or biobank), stratified into SARS-CoV-2, influenza and RSV. Size each stratum for ≥ 40–50 events (the package's 44 events supported a 4-parameter model at EPV 11). | Serial: admission, day 2–3, day 5–7, day 10–14, with time from symptom onset recorded; lower-airway samples where the patient is ventilated | IL-33-axis marker predicts progression independently of NEWS2 and IL-6 in ≥ 2 of 3 virus families, **and** is raised at presentation, i.e. within a treatable window |
| B2 | Does AX-1177 block **endogenous** IL-33 in a lung-relevant system? | Barrier function (TEER / dextran flux), leukocyte adhesion under flow, E-selectin/VCAM-1 **protein**, cytokines, interferon-stimulated genes, viral replication; 8-point AX-1177 dose–response with matched isotype, against both IL-33red and IL-33ox | Primary human lung microvascular endothelium plus air–liquid-interface airway epithelium, ≥ 3 donors each, infected with SARS-CoV-2, influenza or RSV (or exposed to infected-epithelium medium) | 6, 24 and 72 h; antibody given both before and after IL-33 release | Concentration-dependent rescue of endothelial dysfunction with IC₉₀ defined; no increase in viral replication |
| B3 | Does blocking IL-33 help **after** infection is established? | Lung injury (blinded histology, BAL protein, vascular leak), oxygenation, weight/survival; BAL IL-33/sST2 as PD markers; viral titres and bacterial superinfection as safety markers | ≥ 2 virus families (e.g. influenza A in mice; SARS-CoV-2 in hamster or mouse-adapted virus; RSV optional). Use AX-1177 if it cross-reacts, otherwise a surrogate with the same mechanism (binds reduced and oxidised IL-33) or human-IL-33 knock-in mice. Include ± dexamethasone to mimic standard of care. | **Therapeutic** dosing starting when disease appears (not only prophylaxis), plus a delayed-dose arm to map the window | ≥ 30% reduction in the primary lung-injury endpoint vs isotype with therapeutic dosing in ≥ 2 models, with dose–response, and viral titre rising by no more than 0.5 log₁₀ |

### Gate C, about months 9–18: IND-enabling work, started only if Gates A and B pass

- GLP toxicology in a relevant species.
- PK/PD model based on affinity, IC₉₀ and the IL-33 levels measured in B1. Target: suppression of free IL-33 in lung lining fluid throughout the acute window defined in B1/B3.
- CMC, with lot traceability to the material tested.

## 5. What goes into the clinic (only if Gates A–C pass)

**1. First-in-human.** The package contains no human AX-1177 data. The first study would be a single-ascending-dose study in healthy volunteers, covering:
- safety, PK and immunogenicity;
- target engagement, for example build-up of drug-bound total IL-33.

**2. Phase 2a proof of concept** in hospitalised viral LRTD.

| Element | Proposal | Basis in package |
|---|---|---|
| Population | Adults with PCR-confirmed viral LRTD on supplemental oxygen but not IMV, stratified by virus, enrolled within the window found in B1 | Package covers COVID-19 only, so virus breadth must come from B1/B3 |
| Enrichment | Stratify (not restrict) by baseline sST2 until B1 validates a cut-off | sST2 OR 3.02/log unit, rank 2/1,063 |
| Intervention | Single IV dose of AX-1177 at 1–2 levels chosen by PK/PD, vs placebo, added to standard care | One-concentration in vitro data cannot set a dose |
| Primary endpoint | Day-30 ICU/IMV/death (as in the package) or an ordinal recovery scale | mmc2 endpoint definition |
| Key secondary | Change in ANGPT2, vWF, PTX3 and sE-selectin; oxygen-free days; target engagement | These were prognostic in mmc2 |
| Safety | Viral-load kinetics, secondary infection | IL-33-induced interferon genes are removed by the antibody (section 3.1) |

**Illustrative size** (`08_illustrative_sample_sizes.csv`; the control risks are assumptions, not data). The package's 44% event rate comes from unvaccinated patients and is an upper bound.

| Control risk | Relative risk reduction | n per arm, 2-sided α 0.05, 80% power | n per arm, 1-sided α 0.10 |
|---|---|---|---|
| 44% | 35% | 152 | 88 |
| 30% | 35% | 264 | 152 |
| 20% | 35% | 441 | 253 |
| 10% | 35% | 969 | 557 |

At current event rates an outcome-powered trial is large. This is why the Phase 2a go/no-go should rest on target engagement plus a pre-specified movement in the endothelial-injury biomarkers, with enrichment, before anyone commits to a Phase 2b/3 outcome trial.

## 6. Immediate requests to data owners (needed for Gate A)

1. Archived count matrices and the fitted model object, so the data can be re-fitted per cell line (see 3.2).
2. Documentation linking Compound_47 to AX-1177, plus affinity, potency and species cross-reactivity from the biologics file.
3. For mmc2:
   - the 100 assays included in the BH correction but not delivered;
   - the transform behind "log";
   - patient-level data, so ORs can be expressed per SD and IL-6 / time-from-onset adjustment added;
   - how much banked serum remains.
4. For mmc3:
   - the component scores behind each IL-33 value;
   - the scoring SOP, blinding status and a second reader;
   - confirmation that "5+" = 5.5 was intended.
5. A corrected mmc5: one sheet, correctly labelled.

## 7. Methods, reproducibility and limitations of this review

**Scripts** (`/tmp/outputs/analysis`)
- `01` reproduces BH within each contrast and back-infers degrees of freedom.
- `02` and `02b` quantify the IL-33 response, neutralisation, HGMEC reversal, antibody-alone specificity and the SE anomaly, and build the report tables.
- `03` gives the bias-controlled neutralisation estimates.
- `04` and `04b` run pre-ranked fgsea on the MSigDB Hallmark sets (msigdbr 7.5.1), excluding genes with implausible SEs.
- `05` re-analyses the serum proteomics: Wald checks, inference of the BH test count, de-duplication with an outcome-blind rule (annex panel order) plus min-p and max-p sensitivity versions, and the bridge test.
- `06` re-analyses the IHC: donor-level Kruskal–Wallis / Mann–Whitney, Cliff's δ with bootstrap CIs, Holm correction, and a block-level contrast to show pseudo-replication.
- `07` draws the figures.
- `08` covers stoichiometry, EPV, E-values and sample sizes.

**Figures** (`/tmp/outputs/figures`)
- `fig1_neutralisation.png`
- `fig2_implausible_SE.png`
- `fig3_serum_proteomics.png`
- `fig4_postmortem_ihc.png`

**Limitations**
- I worked from summary statistics only, because no counts or patient-level data were delivered.
- Gene-bootstrap CIs do not capture variation between cultures.
- The 44/56 event split is inferred.
- The bridge test assumes each transcript maps to a serum protein and depends on the 865 proteins that overlap.
- The IHC comparisons have low power (5–16 donors per group), so a null is weak evidence, and the ceiling makes it weaker still.
- Nothing in this review can establish in vivo efficacy. Only Gate B can.
