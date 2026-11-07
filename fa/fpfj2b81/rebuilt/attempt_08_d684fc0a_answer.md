**Recommendation: No. This package does not support carrying AX-1177 into IND-enabling or clinical development. Fund only a 9-month gated target-validation stage with pre-set stop criteria; the first gate is at week 6.**

---

# AX-1177 (anti-IL-33 IgG1): proposal to the Programme Committee

*Scope.* Everything below comes from the four delivered tables (mmc2–mmc5) and the methods annex. Statements that rely on outside knowledge are marked *[external]*. Timings in the plan are planning estimates and cannot be derived from the package. Every number can be regenerated from `/tmp/outputs/analysis/` (see Appendix B).

## 1. Summary for the committee

| Question the committee will ask | What the package shows | Verdict |
|---|---|---|
| Does the antibody block IL-33 signalling? | Yes, in vitro, against reduced IL-33 in endothelial cells. In HUVEC at 6 h it reverses **99.7%** (median) of the IL-33 transcriptional programme against an isotype-treated comparator. | **Supported, narrowly**: one concentration, one IL-33 form, non-lung cells |
| Is it clean on its own? | With no IL-33 added, Compound_47 leaves **no reproducible transcriptional footprint** in 4 cell types. | **Supported, in vitro only** |
| Is IL-33 involved in severe viral LRTD? | IL-33 itself was **not delivered**. Lung-tissue IL-33 is **not higher** in COVID-19. The only supportive serum signal is sST2, and it sits in a proteome where **82% of proteins rise with severity**. | **Not supported** |
| Does the IL-33-driven endothelial programme track severity in patients? | Serum proteins from that programme are **not enriched** among severity markers (p = 0.27). | **Not supported** |
| Does blocking IL-33 help, or harm, in infection? Does it affect viral clearance? | No in vivo, infection or PK data. | **Untested** |
| Can we choose a dose? | A single saturating concentration was tested (41-fold molar excess), so there is no potency estimate. | **Not possible** |
| Are the data fit for an investment decision? | There are material defects. The RNA-seq statistics come from a broken pooled variance model. **100 analysed Olink assays were withheld**, IL-33 probably among them. The IHC scale does not match the annex. | **No, until remediated** |

In short, the package shows that the molecule is a competent IL-33 blocker in a dish. It does not show that IL-33 is a driver of viral lower-respiratory-tract disease. Development spend is justified only by the second point. Three things argue against stopping now:
- the IL-33 hypothesis has not been refuted, only left untested;
- sST2 is a genuine top-ranked signal (2 of 1,094);
- the cheapest and fastest information — withheld data that already exists — could settle the largest uncertainty.

---

## 2. What the package supports

### 2.1 Compound_47 neutralises IL-33red in endothelial cells in vitro (Fig. 1)

**Method.** All 26 delivered contrasts come from one fitted model; I confirmed that per-gene AveExpr is identical across contrasts and that df.total is ≈ 85 = 76 residual + 9 prior. Because of that, log-fold-changes combine exactly, e.g. (IL-33+Cmpd47 − vehicle) = (IL-33 − vehicle) + (IL-33+Cmpd47 − IL-33).

- The primary test compares the IL-33 effect (I − V) with the **isotype-controlled** antibody effect (IC − IN). These two contrasts share no group, so shared noise cannot create a spurious "reversal".
- The comparison against IL-33 alone (IC − I) shares group I with the IL-33 effect. That builds in a negative correlation even under pure noise, so I used it only as a secondary check.
- The gene set is the IL-33 programme defined by effect size and expression (|log2FC| > 1, AveExpr > 2). It does not use the delivered p-values, which are unreliable (§4).

| HUVEC | 6 h | 24 h |
|---|---|---|
| IL-33 programme genes | 281 | 108 |
| Slope of (IC−IN) on (I−V); r | −0.93; −0.95 | −0.78; −0.87 |
| Median isotype-controlled reversal [IQR] | **99.7%** [90.6–104.6] | **84.6%** [65.1–94.0] |
| Median reversal vs IL-33 alone | 99.7% | 99.6% |
| Residual IL-33 effect left with antibody, (IC−V)/(I−V), median [IQR] | 0.3% [−3.6 to 7.0] | 0.4% [−6.6 to 17.5] |

- **Canonical NF-κB/IL-33 targets return to vehicle level.** With antibody present, the residual (IC−V) at 6 h is within ±0.3 log2 for NFKBIA (IL-33 effect +3.13), TNFAIP3 (+4.75), TRAF1 (+5.89), CXCL2 (+6.77), CXCL3 (+8.28), IL6 (+5.82), CSF3 (+8.32) and ICAM1 (+5.97).
- **The 24 h gap between 84.6% and 99.6% is a comparator effect, not leftover IL-33 activity.** The isotype+IL-33 arm shows about 13% less IL-33 response than IL-33 alone (slope of (IN−I) on (I−V) = −0.127). The residual (IC−V) stays at a median of 0.4%. The 24 genes with >25% residual are not canonical targets (e.g. SHANK2, ADAM8, AKR1B10, CD24), and their residual does not track any antibody-alone effect (r = 0.01).
- **HGMEC (glomerular microvascular) cells.** The antibody's effect in IL-33-stimulated HGMEC mirrors the HUVEC programme at 6 h (r = −0.79, slope −0.58, 94% opposite sign) but only weakly at 24 h (r = −0.30, slope −0.07). The design has no HGMEC vehicle arm, and the IL-33+NIP228 vs NIP228 contrast was not delivered. **The HGMEC IL-33 response, and therefore how complete neutralisation is there, cannot be estimated.**
- **Scope limits** (annex §1–3):
  - Only one antibody concentration was used: 10 µg/mL, i.e. 68.5 nM IgG against 1.66 nM IL-33, a **41-fold molar excess** (83-fold in binding sites). This shows maximal blockade, not potency.
  - Only the **reduced** form was tested, although the annex credits the antibody with binding both reduced and oxidised forms.
  - Antibody and IL-33 were added at the same time, with no pre-incubation.
  - Each endothelial line comes from a single donor; n = 3 means culture replicates, not donors.
  - The readout is RNA only, at 6 h and 24 h.
  - Neither endothelial cell type comes from lung.
- **Kinetics.** In HUVEC the response to a single dose of IL-33 is front-loaded. Across the 281 programme genes, median |log2FC| is 1.37 at 6 h and 0.51 at 24 h; the slope of the 24 h effect on the 6 h effect is 0.36. This bears on treatment timing (§6–7) but needs confirming in vivo.

### 2.2 No antibody-alone footprint (selectivity, in vitro)

- The 16 antibody-alone contrasts (Compound_47 vs NIP228, PBS or DMSO in HUVEC, HGMEC, A549 and MCF7) produce 632 calls at FDR < 0.05.
- Of these, **490 (78%) are barely-expressed genes** (pooled AveExpr ≤ 0), and **only 1** is a well-expressed gene (AveExpr > 2) with |log2FC| > 1.
- The hits do not replicate. Only 3 genes are significant in ≥2 of the 8 isotype-controlled contrasts, against ~1.75 expected by chance. The correlation between 6 h and 24 h antibody-alone log2FC is −0.06 to 0.18.
- **Conclusion:** there is no reproducible off-target programme.
- **Limits:** A549 and MCF7 were never stimulated with IL-33, and DMSO is not a meaningful vehicle for an IgG. This says nothing about tissue cross-reactivity or in vivo safety.

---

## 3. What the package does not support

### 3.1 IL-33 involvement in human disease: not supported (Figs. 3, 4)

1. **Target not measured.** No IL-33 assay is in the proteomics delivery. IL-33 is on the Olink Inflammation panel *[external: vendor panel content]*, but only 77 Inflammation assays were delivered. The canonical assays missing include IL33, TSLP, IL4, IL5 and IL13 *[external panel list]*. The package therefore has no circulating IL-33 or type-2 cytokine result.
2. **sST2 is the only supportive signal, and it is not specific.**
   - Soluble ST2 ("ST2", Cardiovascular III panel) has OR **3.02 (95% CI 1.83–5.01)** per log unit, p = 1.7×10⁻⁵, adjusted p = **0.0075**. It ranks **2nd of 1,094** assays, after adjustment for age, sex and NEWS2.
   - However, **893/1,094 ORs (81.6%) are >1** (binomial p = 1.6×10⁻¹⁰⁴), and 176 of the 178 FDR-significant assays have OR > 1. The top hit is HGF (OR 4.99). sST2 is one member of a broad "everything rises with severity" shift.
   - sST2 is a decoy receptor, so a high level does not show that free IL-33 is biologically active.
3. **Type-2 IL-33 effectors are null in serum:**
   - IL5: OR 1.00 (0.66–1.52), p = 0.997
   - CCL11: OR 1.08 and 0.98 (two panels)
   - CCL24: OR 0.92
   - Tryptase (TPSAB1): OR 1.07
   - KIT: OR 1.05
4. **The endothelial IL-33 programme does not track severity.**
   - I mapped 916 assays to genes and took the 79 proteins whose genes are IL-33-induced (>2-fold) and Compound_47-reversed (>2-fold) in HUVEC at 6 h.
   - Their severity z-scores are no higher than those of other proteins: median 1.49 vs 1.43; one-sided Mann–Whitney p = 0.28; permutation p = 0.27. FDR-significant share: 21.5% vs 17.9% (Fisher OR 1.26, p = 0.26). With the 24 h programme, p = 0.82.
   - Specific classic markers: VCAM1 OR 1.28 (p = 0.43), ICAM1 OR 1.67 (p = 0.11), SELE OR 2.08 (adjusted p = 0.09).
5. **Lung tissue (donor-level analysis, 31 donors).** IL-33 is *not* higher in COVID-19 pneumonia than in COVID-negative pneumonia in any compartment:

   | Compartment | COVID+ median (n = 16) | COVID− pneumonia median (n = 10) | Shift [bootstrap 95% CI] | Exact p |
   |---|---|---|---|---|
   | Endothelium | 4.81 | 5.50 | −0.19 [−1.00, 0.00] | 0.16 |
   | Basal epithelium | 4.25 | 4.50 | 0.00 [−0.75, 0.88] | 0.92 |
   | Vascular smooth muscle | 2.38 | 3.25 | −0.50 [−1.47, 0.25] | 0.15 |

   - Shifts are Hodges–Lehmann estimates.
   - Eosinophil (EPX), mast-cell (tryptase) and neutrophil-elastase scores also do not differ (p ≥ 0.67).
   - Chronic airway disease is balanced across groups (COPD/asthma in 38–40%) and does not shift IL-33 scores (p = 0.13–0.52).
   - *Caveat:* lower staining is compatible with IL-33 *release* from stored pools. The tissue data are therefore uninformative rather than refuting, but they provide no support.

### 3.2 Efficacy, safety and dose: untested

- There are no in vivo, infection-model, PK, tissue cross-reactivity or toxicology data.
- The effect of IL-33 blockade on viral clearance and epithelial repair is unknown. This is a mechanism-class safety question that must be answered before patients are dosed during an active infection.
- Affinity and potency are "held in the programme biologics file and are not part of this dataset" (annex §1).
- The link between the test article (Compound_47) and AX-1177 is implied by the annex header but **not documented**: there is no lot, sequence or batch record.

---

## 4. Data-integrity and methodology findings that must be fixed

| # | Finding (evidence) | Impact | Fix |
|---|---|---|---|
| T1 | **Broken variance model.** A single limma fit over 4 unrelated cell types (annex §5) pools one variance per gene. Implied SEs are pathological: SELE **8.9** log2 units against a typical 0.71 at its expression level; CXCL1 1,155; CDH5 926; CD93 16,536; GAPDH 9.6. KRT8's SE differs **2,269-fold** between A549 (0.013) and HUVEC (28.8). 164 genes have SE >10× their expression-matched median. Consequences: SELE +11.2 log2 (P = 0.21), VCAM1 +8.7 (P = 0.22) and CXCL1 +8.2 (P = 0.99) are "non-significant", while AKR1C2 +0.11 (an 8% change) has t = 169, P = 10⁻⁹⁹ and DYNC1H1 −0.18 has P = 3×10⁻²⁶. Marker-set screening showed no coherent cell-identity shift, so I do **not** claim a sample swap. | Delivered DE counts (e.g. "4,031 genes at 6 h") and FDRs **cannot be used as evidence**. Log-fold-changes, which are differences of group means, are far less affected; my conclusions rest on them. | Re-fit each cell line separately from the archived counts (voom/limma or DESeq2); use TREAT with a fold-change threshold; run sample-identity QC (sex genes, marker genes, PCA). |
| T2 | HGMEC has no vehicle arm, and IL-33+NIP228 vs NIP228 was not delivered. | HGMEC IL-33 response is not estimable. | Deliver that contrast. |
| T3 | Both mmc5 sheets ("6h", "24h") contain all 24 contrasts and are **identical** (max difference 0). The 6h sheet declares 1,048,576 rows (data stop at 629,041) and has an active filter. mmc4 calls the vehicle arm "Nontreated". The epithelial arms include a DMSO vehicle (irrelevant to an IgG) and no IL-33. | Labelling and design clarity. | Correct the labels. Re-design the epithelial arms with an IL-33 stimulus. |
| P1 | **100 analysed Olink assays withheld.** The reported adjusted p-values are BH over **M = 1,194** tests: 97.6% of BH-determining rows give integer implied counts, rising monotonically 0→99. Only 1,094 were delivered. The annex says BH was "across all assays in the delivery", which is false. Of the withheld assays, **16 had p ≤ 0.05** (5 expected by chance) and **4 would have passed FDR < 0.05**; the best withheld p falls between 2.1×10⁻⁴ and 3.1×10⁻⁴ (~20th overall). Re-running BH on the delivered set gives 206 rather than 178 significant assays. | Incomplete record. IL-33's own result may exist but is missing. | Release all 1,194 results with LOD, missingness and filter rules. |
| P2 | "OR per log unit" is undefined. NPX is already log2 *[external]*, and re-logging would drop non-positive values. The `composite_endpoint_0/1` columns are undefined; they are consistent with per-group missing fractions (denominators 56/44 ⇒ **44 events/100**; maximum 8% missing). | ORs cannot be compared across assays; I ranked by z instead. | Document the transformation and column definitions. |
| P3 | 26 proteins are measured on 2–4 panels (30 extra rows), e.g. IL-6 ×4, HGF ×2. Positive QC: duplicates agree (log-OR r = 0.974; 32/35 pairs in the same direction). | Inflates the count of "hits" (IL-6 counted 4 times). | Collapse to protein level for claims. |
| H1 | IHC: the annex states a 0–5 scale, but IL-33 values reach **5.5**. The numeric cell-marker columns are exactly "n+" → n+0.5 (0 mismatches in 74 rows). IL-33 quarter-points (e.g. 4.25, 4.75) imply an undocumented averaging step. **39/74** endothelial blocks sit at the 5.5 ceiling. A single reader scored everything. | Ceiling effect limits detection of any increase. No reliability estimate. | Document the derivation; add a second blinded reader plus digital quantification. |
| H2 | 74 blocks come from 31 donors, and 3 donors supply 24 of the 49 COVID+ blocks. Donor 1905 has no SARS-CoV-2 status although it is labelled "COVID neg". Controls are non-viral pneumonias. All donors are white, with mean age 81–84. | Block-level tests would be pseudo-replicated; I analysed at donor level. Generalisability is limited. | Fix metadata; include other viral pneumonias. |

---

## 5. Decision logic

- **Why not "Go"?** Moving to IND-enabling needs three things:
  - disease relevance of the target;
  - a dose rationale;
  - in vivo proof of benefit without harm to viral clearance.

  The package provides none of them. Its disease-side evidence rests on one non-specific serum marker. Direct tests of the pathway come back null or missing: IL-33 not delivered, tissue IL-33 not increased, type-2 axis null, programme enrichment null.
- **Why not "Stop"?**
  - Pharmacology is clean: near-complete, isotype-controlled neutralisation with no off-target footprint.
  - sST2 is a real top-ranked association.
  - The tissue null is ambiguous, since release and absence look the same.
  - Decisive data already exist but were not delivered: the IL-33 Olink result, the RNA-seq counts, and lung RNA from 22 donors (22 of 31 donors carry "Tissue RNA" IDs).
- **Asymmetry.** The first 6 weeks are cheap (re-analysis and data release) and could settle the biggest uncertainty. The in vivo and cohort work is the minimum needed before committing to tox and CMC spend.

---

## 6. The plan: what we measure, in which model, when (Fig. 5)

### Gate 0 — week 6: data remediation
- **Measure:**
  - identity records linking Compound_47 to AX-1177;
  - per-cell-line re-analysis of the RNA-seq counts, with sample QC and delivery of the HGMEC IL-33 contrast;
  - all 1,194 Olink results, including IL-33, with LOD and missingness;
  - corrected IHC metadata and a second reader.
- **Pass:**
  - identity confirmed;
  - isotype-controlled reversal of the HUVEC 6 h programme stays ≥80% after re-analysis (currently 99.7%);
  - the HGMEC IL-33 response is estimable and ≥80% reversed at 6 h.
- **Stop if:** identity cannot be established, or neutralisation does not survive re-analysis.

### Workstream A — months 1–5: human pharmacology that informs dose (Gate 1)
| Experiment | System | Readouts | Pass criterion (proposed) |
|---|---|---|---|
| A1 Potency | 8-point antibody titration against IL-33red **and IL-33ox** at EC80; pre-incubated vs concurrent addition | IL-6, IL-8 and GM-CSF secretion; NFKBIA/TNFAIP3 at 1–2 h; E-selectin and VCAM-1 at 4–6 h | IC50/IC90 defined for both IL-33 forms; ≥90% maximal inhibition of each |
| A2 Lung-relevant cells | Primary human lung microvascular endothelium, airway epithelium at air–liquid interface, IL-33-responsive immune cells; ≥3 donors each | Protein plus function: barrier (TEER/dextran), leukocyte adhesion under flow | ≥80% inhibition of IL-33-induced protein and functional readouts in cells from ≥3 donors |
| A3 Infection context | Influenza, RSV or SARS-CoV-2 infected air–liquid-interface cultures | Kinetics of IL-33 release (reduced vs oxidised); viral titre with and without antibody | Release measured; no increase in viral replication (>0.5 log10) |

### Workstream B — months 1–9: in vivo target validation (Gate 2)
- **B1 (months 1–2.5): choose the model.** Test whether AX-1177 binds mouse, hamster and cynomolgus IL-33. If it does not, use a matched surrogate antibody or human-IL-33 knock-in mice, and tox must then run in a cross-reactive species.
- **B2 (months 2.5–9): ≥2 virus models** (e.g. influenza plus SARS-CoV-2 or RSV).
  - **Arms:**
    - prophylactic dosing (proof of mechanism);
    - therapeutic dosing starting day 2–3 after infection, to mirror hospitalised patients;
    - a late start, to map the treatment window;
    - isotype control throughout.
  - **Efficacy endpoints:**
    - BAL protein/albumin (vascular leak);
    - blinded lung-injury histology;
    - oxygen saturation;
    - weight and survival;
    - endothelial activation (E-selectin and VCAM-1 on lung endothelium).
  - **Mechanism endpoints:**
    - free and complexed IL-33 and sST2 in BAL and serum;
    - the mouse orthologues of the bridge panel (§7);
    - lung endothelial RNA compared with the in vitro programme.
  - **Safety endpoints:**
    - lung viral titre at days 3, 5 and 7, and time to clearance;
    - virus-specific T-cell and antibody responses;
    - epithelial repair.
  - **Pass (proposed):** in ≥2 models, therapeutic dosing gives a ≥30% reduction in the primary lung-injury endpoint with no increase in viral titre >0.5 log10 and no delay in clearance.

### Workstream C — months 1–8: human biomarker validation
- **C1 (months 1–4): existing cohort (n = 100).**
  - Measure free and sST2-bound IL-33 with a high-sensitivity assay, plus clinical-grade sST2.
  - Re-test sST2 with IL-6 and renal function added to the model, to check specificity.
  - *Pass:* sST2 or IL-33 OR stays >1 with a CI excluding 1 after adding IL-6.
- **C2 (months 2–8): independent longitudinal viral-LRTD cohort**, including influenza, RSV and hMPV, sampled at admission, day 2–3 and day 5–7.
  - Replicate sST2 and establish when IL-33 and sST2 peak.
  - Define an enrichment cut-off and the event rate in the enriched group.
- **C3 (months 1–4): archived lung RNA from 22 donors.**
  - Score the HUVEC IL-33 programme and IL33/IL1RL1 in COVID+ vs COVID− pneumonia. Make a pre-specified effect-size comparison; n = 9 vs 9 is too small for p-values alone.
  - Re-score IHC with two blinded readers (target weighted κ ≥ 0.6).

**Overall stop rule:**
- Stop if IL-33 is not elevated or associated (C1/C2) **and** C3 shows no programme in COVID-19 lungs.
- Stop if therapeutic dosing fails in both virus models, or viral titres rise.
- If sST2 fails to replicate, drop the enrichment strategy and re-decide.

---

## 7. What goes into the clinic (only if Gates 0–2 pass)

1. **First-in-human:** intravenous SAD/MAD of AX-1177 (identity-confirmed lot) in healthy volunteers.
   - Measure PK, safety, immunogenicity and target engagement (free IL-33 suppression; accumulation of antibody–IL-33 complexes).
   - **Dose:** set by PK/PD modelling from the A1 IC90 for both IL-33 forms. The package gives no basis for a dose.
   - Confirm the Fc format. With wild-type IgG1, check Fc-receptor effects of IL-33–antibody complexes.
2. **Phase 2a, randomised, double-blind, placebo plus standard of care.**
   - **Population:** adults hospitalised with PCR-confirmed viral LRTD who need supplemental oxygen. This matches the cohort population but should extend beyond SARS-CoV-2, using the sST2 enrichment cut-off from C1/C2.
   - **Timing:** randomise early, ≤48 h from starting oxygen. The in vitro response is front-loaded, but the final window comes from B2/C2.
   - **Endpoints:** progression to ICU admission, invasive ventilation or death by day 28–30 (the cohort composite), or an ordinal scale if it is more sensitive.
   - **Safety:** nasopharyngeal viral-load kinetics on days 1–7, secondary infections and anti-drug antibodies.
3. **PD "bridge" panel.**
   - These are serum proteins induced by IL-33 and reversed by Compound_47 in HUVEC (both >2-fold) that are also FDR-significant for severity: sST2 (OR 3.02), PTX3 (11.6), IL-6 (2.14), OPG (6.77), IL-18R1 (6.07), MCP-3 (1.72), CCL20 (1.83), IL-8 (2.23), CSF-1, CTSS, IL-1β and others (17 in total; `candidate_bridge_biomarkers.csv`).
   - The most consistent in vitro are IL-6, OPG, CCL20, IL-8, IL-1β, CTSS, IL-18R1 and CSF-1: reversed in HUVEC at 6 h and 24 h and in HGMEC at 6 h.
   - sST2 itself is only weakly linked in vitro: +1.6 log2 at 6 h, +0.36 at 24 h, +0.19 in HGMEC.
   - These markers are **not IL-33-specific**. Pair them with free and complexed IL-33 for target engagement.
4. **Sizing:**
   - Using the cohort's implied control event rate of **44%** (two-sided α = 0.05, 1:1), per-arm numbers are:

     | Relative reduction | 80% power | 90% power |
     |---|---|---|
     | 40% | 115 | 153 |
     | 33% | 172 | 230 |
     | 25% | 306 | 410 |

   - At an *assumed* contemporary rate of 20%, 80% power needs 329, 501 and 906 per arm for the same reductions.
   - The pre-vaccination single-centre rate is not a safe planning basis; C2 supplies the real one.

---

## 8. Key risks and open questions

- **Biology.** The disease link rests on sST2, which may be a marker rather than a mediator. Lung tissue cannot tell IL-33 release apart from non-involvement.
- **Safety of the mechanism.** The effect of IL-33 blockade on viral clearance and tissue repair is untested (A3, B2).
- **Translational fidelity.**
  - Neither endothelial line comes from lung, and each is a single donor.
  - Oxidised IL-33 was never tested.
  - There is no potency estimate.
- **Clinical heterogeneity.**
  - The cohort is 100 patients from a single centre, SARS-CoV-2 only, pre-vaccination.
  - The "viral LRTD" indication assumes generalisation to other viruses that the package has not tested.

---

## Appendix A — Analyses performed

**Transcriptomics**
- **Parsing and integrity:** 26 contrasts × 26,210 genes. I confirmed the mmc5 sheets are identical, the gene universe is common, AveExpr is identical across contrasts, BH reproduces within each contrast (max error 5×10⁻¹⁵), and t and logFC signs agree.
- **Single fit:** df.total was inferred from (t, P) as 85.13 for all contrasts, i.e. 76 residual df (114 libraries − 38 groups).
- **Variance pathology:** implied SE = |logFC/t|, compared with genes of similar expression.
- **Neutralisation metrics:** built from exact contrast algebra on log-fold-changes, with a gene set defined without p-values; the isotype-controlled contrast is primary.
- **Off-target:** counts, expression strata, cross-contrast overlap against a hypergeometric expectation, and 6 h vs 24 h correlation.

**Proteomics**
- **Internal checks:** Wald CIs are exactly symmetric on the log scale, and the p-values implied by the CIs match the reported p-values.
- **BH family:** reconstructed by scanning M and keeping integer implied counts at rows where the reported value equals the raw BH value.
- **Multiplicity:** assays measured on more than one panel were collapsed to one protein for claims.
- **Bridge test:** a competitive rank test of Wald z-scores (protein-level), plus 10,000 permutations.

**IHC**
- Separator rows dropped and donor fields carried down to each donor's blocks.
- Ordinal scores parsed (trailing spaces and "ND" handled) and the numeric transform verified.
- Donor-level analysis by mean, with max and first-block sensitivity checks. Tests: exact Mann–Whitney, Hodges–Lehmann shift with donor-bootstrap CIs, and Kruskal–Wallis.

**Limits of my analysis**
- There are no count matrices or patient-level data, so all inference is on summary statistics.
- The bridge test is low-powered (79 proteins), and serum proteins have many cellular sources.
- Which assays were withheld is unknown. Only their p-value distribution could be reconstructed.

## Appendix B — Outputs (`/tmp/outputs/`)
- **`analysis/00a`–`22_*.py`:** all analyses, in run order.
- **`analysis/99_key_numbers.py`:** regenerates every number cited here into `analysis/key_numbers.json`.
- **Key tables:**
  - `neutralisation_HUVEC_summary.csv`
  - `hgmec_vs_huvec_signature.csv`
  - `antibody_alone_hits_summary.csv`
  - `se_inflation_genes_HUVEC6.csv`
  - `mmc2_bh_hidden_tests.csv`
  - `undelivered_assays_pvalue_brackets.csv`
  - `bridge_test_results.csv`
  - `candidate_bridge_biomarkers.csv`
  - `ihc_donor_level_tests.csv`
  - `mmc3_cleaning_log.txt`
  - `sample_size_composite.csv`
- **Figures (`figures/`):**
  - `fig1_neutralisation.png` — isotype-controlled reversal, HUVEC and HGMEC
  - `fig2_limma_pathology.png` — SE pathology
  - `fig3_proteomics.png` — global shift, bridge test, withheld assays
  - `fig4_ihc_donor_level.png`
  - `fig5_gated_plan.png`
