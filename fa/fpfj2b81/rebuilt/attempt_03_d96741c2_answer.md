**Recommendation: CONDITIONAL GO, limited to a gated, time-boxed (~12-month) de-risking phase for AX-1177 in viral LRTD. The package does not support starting IND-enabling work or committing to clinical entry.**

---

# AX-1177 (anti-IL-33 mAb): proposal to the Programme Committee

**Indication:** viral lower respiratory tract disease (LRTD)
**Evidence base:** everything in the mounted package, namely the methods annex plus mmc2 (serum proteomics), mmc3 (post-mortem IHC), mmc4 and mmc5 (in vitro transcriptomics). Every number below comes from those files or from re-analysis of them; scripts and outputs are in `/tmp/outputs/analysis/`. Statements that rely on general domain knowledge rather than the package are labelled *[background]*.

## 1. Decision summary

1. **Proven in vitro: the antibody neutralises reduced IL-33 completely and specifically in endothelial cells.**
   - IL-33red switched on a large NF-κB/endothelial-activation programme in HUVEC: 4,031 genes changed at 6 h.
   - With Compound_47 present, that programme was abolished. Bias-corrected blockade against the isotype control was 101% (95% CI 93–109%) at 6 h and 86% (76–97%) at 24 h, rising to 93% (88–99%) in well-expressed genes.
   - Compound_47 alone did not move the IL-33 programme in any of the four cell lines.
2. **Not shown: that IL-33 drives viral LRTD.**
   - IL-33 itself is absent from the clinical dataset, and 100 analysed serum assays were withheld from the delivery.
   - The only IL-33-axis clinical signal is soluble ST2 (OR 3.02 per log unit, 95% CI 1.83–5.01, FDR 0.0075). It is one of 169 outcome-associated proteins, is a non-specific severity marker *[background: sST2 is the decoy form of the IL-33 receptor]*, and all of the data come from SARS-CoV-2 patients.
   - Proteins from the IL-33-induced endothelial programme are **not** over-represented among outcome-associated serum proteins (OR 1.08, p = 0.78).
   - In post-mortem lungs, IL-33 is **not** higher in COVID-19 than in controls. The trend goes the other way: endothelium median 4.81 vs 5.50, p = 0.052.
3. **Missing entirely:**
   - any document linking "Compound_47" to AX-1177;
   - affinity and potency data, and any functional data for oxidised IL-33;
   - lung-derived cells;
   - in vivo efficacy, PK, toxicology and virology data;
   - any human data outside single-centre, pre-vaccination SARS-CoV-2.
4. **New safety question raised by the data.** IL-33red induced 38 interferon-stimulated genes (ISGs) in endothelium at 24 h, and the antibody lowered all 38 (26 at FDR < 0.05). Antiviral safety must be an explicit gate.
5. **The package has data-integrity defects that must be fixed before any external use** (Section 4).
   - Delivered statistics are uninterpretable for 274 genes, including E-selectin, VCAM-1, IL-8 and MCP-1.
   - The serum FDR was computed over 1,194 tests, but 1,094 assays were delivered.
   - IHC scores exceed the stated scale, and the disease labels conflict with the pathology text.

**Decision requested:** approve Stages 0–2 (Section 5), with pre-specified go and kill criteria and a committee decision at about Month 12 on whether to start IND-enabling work.

**Why not stop now?**
- The mechanism works cleanly in vitro.
- The human sST2 association is real within its cohort.
- Nothing in the package is a hard negative.

**Why not go faster?**
- Causality, in vivo efficacy under therapeutic dosing, potency and antiviral safety are all untested.
- Spending on GLP toxicology and CMC before those answers would commit substantial funds against an unvalidated hypothesis.

---

## 2. Evidence scorecard

| Question the committee needs answered | What the package shows (key numbers) | Strength | Main gap |
|---|---|---|---|
| Does the antibody neutralise IL-33? | Yes, for IL-33red in HUVEC and HGMEC (§3.1) | **Strong** internally | No link to AX-1177; single concentration; no potency; no oxidised IL-33 |
| Is the effect specific? | Antibody alone vs isotype: no shift in the IL-33 programme (Spearman −0.08 to +0.09 across 4 lines); 14–73 FDR hits per contrast, mostly low-count noise | **Strong** | No Fc or safety pharmacology |
| Is the IL-33 pathway engaged in severe viral LRTD? | Indirectly only. sST2 OR 3.02 (1.83–5.01); IL-33 not delivered | **Weak–moderate** | IL-33 measurement; non-COVID viruses; replication |
| Does IL-33 *cause* disease? | No data | **None** | In vivo therapeutic-dosing studies |
| Is IL-33 present in target tissue? | Yes: near-maximal staining in lung endothelium and basal epithelium in all groups; not increased in COVID-19 | Presence: **moderate**; disease-specific change: **none** | Blinded re-read; RNA; earlier-stage tissue |
| Will blockade work when given therapeutically? | Antibody was added concurrently with IL-33 (annex §3) | **None** | Delayed-addition and in vivo studies |
| Is blockade safe during active viral infection? | In vitro, the antibody removes IL-33-induced ISGs (§3.1) | **Open risk** | Viral-load readouts in vitro and in vivo |
| Does it generalise beyond SARS-CoV-2? | All human data are SARS-CoV-2, pre-vaccination, single centre | **None** | Multi-virus cohort |

---

## 3. What the data show

### 3.1 In vitro pharmacology (mmc4, mmc5; annex §1–5)

**Design.**
- IL-33red: 30 ng/mL, about 1.66 nM.
- Compound_47: 10 µg/mL, about 68.5 nM, i.e. a 41-fold molar excess (83-fold in binding sites).
- Antibody was added *concurrently* with IL-33, without pre-incubation.
- Cells: single-donor HUVEC (umbilical vein) and HGMEC (kidney glomerulus), n = 3 cultures per arm, harvested at 6 h and 24 h.
- The epithelial lines (A549 lung adenocarcinoma; MCF7 breast) **received no IL-33**.

**IL-33red activates endothelium strongly.** In HUVEC at 6 h, 4,031 genes changed at FDR < 0.05 (2,191 up, 1,840 down); at 24 h, 1,836 changed. Table 1 gives log2 fold changes at 6 h.

*Table 1. Selected genes, HUVEC, 6 h. Values are log2 fold changes.*

| Gene | IL-33red vs vehicle | (IL-33red + Cpd47) vs (IL-33red + isotype) | Residual: (IL-33red + Cpd47) vs vehicle |
|---|---|---|---|
| NFKBIA | +3.13 | −3.24 | −0.10 |
| TNFAIP3 | +4.75 | −4.81 | −0.01 |
| TRAF1 | +5.89 | −5.95 | −0.11 |
| CSF2 (GM-CSF) | +10.30 | −12.21 | −1.93 |
| CSF3 (G-CSF) | +8.32 | −8.28 | +0.05 |
| IL6 | +5.82 | −5.97 | −0.14 |
| TNF | +7.89 | −7.67 | +0.02 |
| F3 (tissue factor) | +5.64 | −5.47 | +0.27 |
| CX3CL1 | +8.40 | −8.67 | −0.24 |
| SELE (E-selectin)† | +11.21 | −10.99 | +0.31 |
| VCAM1† | +8.74 | −8.76 | +0.09 |
| CXCL8 (IL-8)† | +8.19 | −8.45 | −0.17 |
| CCL2 (MCP-1)† | +4.15 | −4.29 | −0.10 |
| IL1RL1 (ST2)† | +1.60 | −1.68 | 0.00 |

† Delivered standard errors for these genes are implausibly inflated (audit B1). For example, SELE has FDR 0.50 despite +11.2 log2. **Point estimates only.**

**Compound_47 abolishes the response.** The naive metric (compare "IL-33 vs vehicle" with "Cpd47 + IL-33 vs IL-33 alone") is biased, because both contrasts share the IL-33-alone arm. A pure-noise simulation shows the bias alone produces 50% apparent "inhibition" (audit B3).

I therefore used a bias-free design: select the IL-33-responsive genes on the *other* timepoint's libraries, then estimate blockade at signature level against the isotype arm, with bootstrap 95% CIs (`tx/blockade_signature_level_crossvalidated.tsv`, Fig. 1–2).

| Timepoint | Genes | Blockade vs isotype | Residual IL-33 effect under Cpd47 |
|---|---|---|---|
| 6 h | all (n = 510) | **101% (93–109)** | 1.9% (−3.9 to 7.5) |
| 6 h | AveExpr > 2 (n = 73) | 98% (94–103) | 1.4% (−2.6 to 5.2) |
| 24 h | all (n = 1,061) | **86% (76–97)** | 8.2% (0.6 to 15.0) |
| 24 h | AveExpr > 2 (n = 253) | 93% (88–99) | −6.3% (−12.0 to −1.9) |

**HGMEC, a second endothelial type.** The HGMEC IL-33 response contrast was never extracted, so blockade cannot be expressed as a percentage there. Using the HUVEC-defined programme instead, the isotype-controlled contrast is clearly reversed:
- 6 h: Spearman −0.53; mean sign-aligned effect −0.72 log2 (95% CI −0.79 to −0.64);
- 24 h: weaker, −0.31 (−0.40 to −0.23);
- the most-reversed HGMEC genes are the same NF-κB core: NFKBIA, TNFAIP3, TRAF1, NFKB2, RELB.

**Specificity.**
- Compound_47 alone vs isotype produced no shift in the IL-33 programme in HUVEC, HGMEC, A549 or MCF7: Spearman −0.08 to +0.09; signature-level effect −0.02 log2 (−0.06 to 0.02) in HGMEC at 6 h.
- Each of the 16 antibody-alone contrasts yielded only 14–73 FDR < 0.05 genes, mostly low-count noise (median AveExpr −1.3 to −2.8).
- Only 10 genes recur in ≥ 3 contrasts, and the expressed ones move by |log2FC| ≤ 0.24.
- There is no sign of off-target activity.

**Caveats inside the in vitro data.**
- **The isotype control is not fully inert at 24 h.** NIP228 attenuated the IL-33 response by 13.6% (95% CI 9.2–17.7%) in expressed genes at 24 h, but not at 6 h (−3.0%, CI −8.5 to 2.1). Specific blockade should therefore be quoted against the isotype arm, as above.
- **IL-33 induces an interferon-stimulated programme, which the antibody removes.** At 24 h, 38 ISGs were induced (median +1.21 log2), for example CXCL10 +4.97, GBP5 +4.74, CCL5 +3.58, MX1 +2.49 and OAS3 +1.29. Compound_47 lowered all 38 relative to isotype (26 at FDR < 0.05; e.g. GBP5 −4.35, CCL5 −3.57, MX1 −1.84).
  - Whether this affects viral control is unknown. It is the main mechanism-based safety question.
- **What this experiment cannot tell us:**
  - potency, because one concentration at 41× molar excess gives no IC50 or IC90;
  - the therapeutic window, because there was no delayed addition;
  - activity against oxidised IL-33;
  - any epithelial biology, because no IL-33 was given to A549 or MCF7;
  - lung endothelium, or donor-to-donor variability.

### 3.2 Serum proteomics: hospitalised SARS-CoV-2 (mmc2; annex §6)

**Cohort.**
- n = 100, single centre, pre-vaccination.
- Olink panels: 13, giving 1,094 assays, or 1,063 unique proteins once the 27 proteins measured on 2–4 panels are collapsed.
- The undocumented group columns are exact multiples of 1/56 and 1/44. This implies **44 patients with the 30-day composite endpoint** (44%, 95% CI 35–54%).

**Broad, non-specific severity signature.**
- 178 assay rows reach FDR < 0.05, corresponding to 169 proteins; 176 of them have OR > 1.
- The top hits include HGF (OR 4.99), sST2, HDGF, SEMA4C, PTX3 and IL-6. IL-6 is concordant on all four panels (OR 2.07–2.31), which supports assay reliability.
- Nominal p < 0.05: 384 assays, against 55 expected under the null.

**The IL-33 axis.**
- **sST2: OR 3.02 per log unit (95% CI 1.83–5.01), p = 1.7×10⁻⁵, FDR 0.0075, rank 2 of 1,094**, adjusted for age, sex and NEWS2. sST2 is also IL-33-inducible in HUVEC (+1.60 log2) and reversed by Cpd47 (−1.68), which makes it a candidate PD marker.
  - As a decoy receptor and general stress marker, it cannot show that IL-33 *drives* outcome *[background]*.
- **IL-33 itself is absent.**
  - The delivered Inflammation panel has 77 of 92 assays. The vendor's standard Inflammation panel includes IL-33 *[background; confirm with vendor]*.
  - The reported adjusted p-values reproduce only for a BH family of **1,194** tests (top row: 0.004041 / 3.385×10⁻⁶ = 1,194.0). So 100 analysed assays were withheld.
  - The withheld assays are **not null**: 5 had p < 0.01 and 15–16 had p < 0.05. One had p between 2.1×10⁻⁴ and 3.1×10⁻⁴, which would rank about 19th of 1,194.
- **The alternative IL-33 receptors are not associated:**
  - sRAGE: OR 2.34 (0.98–5.56), p = 0.055;
  - EGFR: OR 1.16 (0.40–3.36), p = 0.78.
- **No type-2 signal** *[background: the canonical downstream axis of IL-33]*:
  - IL-5: OR 1.00 (0.66–1.52);
  - eotaxin (CCL11): 1.08 and 0.98;
  - CCL17: 0.85; CCL24: 0.92;
  - IL-5Rα: 1.61 (p = 0.059);
  - the exceptions are IL-4Rα (2.69, FDR 0.020) and amphiregulin (2.2 and 2.0, FDR 0.030 and 0.045).

**Bridge between the in vitro and clinical data** (`bridge_candidate_PD_markers.tsv`).
- Of 929 assays mapped to the transcriptome, those encoded by IL-33-induced HUVEC genes were **not enriched** among outcome-associated proteins: unique-gene Fisher OR 1.08, p = 0.78 (19/103 vs 139/801).
- The severity signature is therefore not specifically "IL-33-shaped".
- Endothelial adhesion molecules are weak:
  - sVCAM-1: OR 1.28, p = 0.43;
  - sICAM-1: 1.67, p = 0.11;
  - sE-selectin: 2.08, p = 0.022, FDR 0.091.
- A subset of proteins is IL-33-inducible, Cpd47-reversible *and* outcome-associated. These are the candidate **PD panel**:

| Marker | Serum OR (FDR) | In vitro: IL-33 effect / reversal vs isotype (log2) |
|---|---|---|
| sST2 | 3.02 (0.0075) | +1.60 / −1.68 |
| IL-6 | 2.07–2.31 (0.012–0.019) | +5.82 / −5.97 |
| OPG | 6.77 (0.014) | +4.80 / −4.99 |
| IL-18R1 | 6.07 (0.018) | +3.59 / −3.45 |
| CCL20 | 1.83 (0.020) | +9.21 / −9.84 |
| IL-8 | 2.23 (0.023) | +8.19 / −8.45 |
| PTX3 | 11.6 (0.012) | +2.18 / −2.26 |
| IL-1β | 2.45 (0.046) | +3.65 / −3.97 |
| MCP-1 | 2.26 and 1.96 (0.051 and 0.054) | +4.15 / −4.29 |

Two caveats apply to these ORs:
- They are "per log unit" on assay-specific scales, so they are **not comparable across assays** (for example, CSF-1's OR of 90 has a 95% CI of 4–1,933).
- The data are cross-sectional and from one centre, with no replication.

### 3.3 Post-mortem lung IHC (mmc3; annex §7)

**Cohort and method.**
- 31 donors across 74 blocks: 16 COVID+, 10 "COVID− pneumonia", 5 "COVID− non-pneumonia". Mean age 81–84 years.
- Scored by a single reader.
- The unit of analysis is the **donor**. Three donors contribute 24 of the 74 blocks (32%).
- Block-level tests would be pseudo-replicated: they give p = 0.017 and 0.007, against donor-level p = 0.052 and 0.068.

**IL-33 is abundant everywhere and near the scale ceiling.** Endothelial scores were at maximum in 41% of COVID+ blocks, 67% of COVID− pneumonia blocks and 90% of COVID− non-pneumonia blocks.

**It is not increased in COVID-19.** Donor medians, COVID+ vs COVID− pneumonia vs COVID− non-pneumonia (p = COVID+ vs all COVID−):

| Compartment | COVID+ | COVID− pneumonia | COVID− non-pneumonia | p |
|---|---|---|---|---|
| Endothelium | 4.81 | 5.50 | 5.50 | 0.052 |
| Vascular smooth muscle | 2.38 | 3.25 | 3.50 | 0.068 |
| Basal epithelium | 4.25 | 4.50 | 4.88 | 0.76 |

- Lower staining in COVID+ lungs is compatible with release of the nuclear alarmin or with cell loss *[background]*. The design cannot tell these apart.
- There is no COVID-specific difference in eosinophil, mast-cell or neutrophil scores against COVID− pneumonia (p = 0.44–1.0). None of the 11 markers survives BH correction (minimum q = 0.25).
- The study can only detect large effects (minimal detectable Cohen's d ≈ 1.0).
- **Conclusion:** the tissue data show the target is present in lung, but not that it is involved in disease.

---

## 4. Data-integrity findings that bear on the decision

Full table with evidence: `analysis/data_integrity_audit.md`.

1. **No identity link between Compound_47 and AX-1177** (annex §1). Every in vitro result above is for Compound_47.
2. **Delivered statistics are uninterpretable for a subset of genes in the pooled 114-library model.**
   - Implied SEs reach 1,155 log2 units for CXCL1, 926 for CDH5 and 8.9 for SELE. The typical range is 0.05–0.8.
   - 274 genes are flagged, and they are enriched 8-fold among the most strongly IL-33-induced genes (p = 3×10⁻⁷). 97 of 99 are robust-eBayes variance outliers (implied df 75.1 vs 85.1).
   - As a result, FDR-based gene lists from this package systematically omit E-selectin, VCAM-1, IL-8, MCP-1, PTX3 and ST2.
   - The fix is a refit from counts, one model per cell line. The counts are in the archive (annex §5).
3. **Shared-arm bias.** Any "% genes reversed vs IL-33 alone" claim is inflated. Under pure noise, that metric alone yields 50% apparent inhibition.
4. **Serum FDR family mismatch.** The FDR was computed over 1,194 tests, but the annex says it was computed over all assays in the delivery. The 100 withheld assays contain real signals, possibly including IL-33.
5. **IHC data quality.**
   - Scores reach 5.5 on a stated 0–5 scale (39 of 74 endothelial blocks). The numeric columns equal the ordinal score + 0.5 in 74 of 74 blocks.
   - 4 of 10 "COVID− pneumonia" donors have no pneumonia, pneumonitis or diffuse alveolar damage in their pathology text, and 2 of 5 "non-pneumonia" donors do.
   - One donor lacks a SARS-CoV-2 status.
6. **Minor curation issues.** The mmc5 sheets labelled "6h" and "24h" are identical, each holding both timepoints. The vehicle arm is labelled "Nontreated" in mmc4.
7. **Reassurance.** Apart from item 2, the transcriptomic tables are internally consistent with a single fit: the same 26,210 genes, identical AveExpr, a common df of 85.13, BH reproducing within each contrast, and no logFC/t sign conflicts. The serum ORs, CIs and p-values are mutually consistent (Wald), and duplicated proteins agree across panels.

---

## 5. Proposed de-risking plan: what we measure, in which model, and when

Timings are planning estimates from approval. Go and kill thresholds are proposals for the committee to ratify before work starts.

### Stage 0 (Months 0–2): make the package decision-grade

Cost is low; these are mostly existing data and documents.

| What | How | Go | Kill / escalate |
|---|---|---|---|
| Identity: Compound_47 = AX-1177? | Sequence, cell line, lot, CoA; if not identical, repeat the HUVEC 6 h experiment with AX-1177 | Identity documented | Not the same molecule **and** AX-1177 fails to reproduce ≥ 90% blockade |
| Biologics file | KD for IL-33red **and** IL-33ox; cell IC50; cyno and mouse cross-reactivity; Fc format and effector function | Sub-nM to low-nM potency against both forms; species for tox and in vivo identified | No functional activity vs IL-33ox, which would require the claim and strategy to be revised |
| Transcriptomics refit | Counts → per-cell-line voom/limma; library identity QC using lineage markers per library; resolve the SE inflation | Blockade vs isotype ≥ 90% (6 h) and ≥ 80% (24 h) reproduced | Blockade not reproduced |
| Full serum data | All 1,194 assays, including IL-33 with detection rate and LOD; per-SD ORs from raw NPX | Data delivered | — |
| IHC re-read | 2 blinded pathologists, raw 0–5 scale, adjudicated case definitions; digital % IL-33⁺ nuclei | Done | — |

### Stage 1 (Months 1–6): pharmacology in disease-relevant human systems, plus human target validation

**1a. In vitro models.**
- Primary human lung microvascular endothelial cells (≥ 3 donors).
- Primary bronchial or small-airway epithelium at air–liquid interface (≥ 3 donors, including COPD donors; 11 of 31 autopsy donors carried a COPD annotation).
- Endothelial–epithelial co-culture infected with influenza A, RSV and SARS-CoV-2, which generates *endogenous* IL-33 release.

**1a. What we measure.**
- An 8–10-point concentration–response of AX-1177 against IL-33red, IL-33ox and full-length IL-33 at EC80, giving IC50 and IC90.
- Timing of addition: pre-incubation, concurrent, and +1 h, +4 h and +24 h after stimulation.
- Transcript PD panel from this package's NF-κB core: NFKBIA, TNFAIP3, TRAF1, CSF2, CSF3, IL6, CXCL2, F3.
- Secreted proteins: IL-6, GM-CSF, G-CSF, IL-8, sE-selectin, sVCAM-1, PTX3, sST2.
- Barrier function: TEER and permeability.
- **Viral titre and ISG kinetics**: CXCL10, MX1, IFIT1, OAS3.

**1a. Gates.**
- **Go:**
  - IC90 against both redox forms is achievable at clinically plausible exposure;
  - inhibition is ≥ 70% when AX-1177 is added ≥ 4 h after stimulation;
  - viral titre rises by ≤ 0.5 log10 relative to isotype.
- **Kill:** AX-1177 increases viral replication by > 0.5 log10 reproducibly in 2 viruses.

**1b. Human target validation.**
- Measure free and total IL-33 (high-sensitivity immunoassay) and sST2:
  - in the stored sera of the 100-patient cohort (kept at −80 °C, annex §6);
  - in an independent, contemporary cohort of about 150–200 patients hospitalised with non-COVID viral LRTD (influenza, RSV, hMPV).
- Analysis plan: the same composite endpoint, adjusted for age, sex and NEWS2, plus eGFR and NT-proBNP to test whether sST2 is specific.

**1b. Gates.**
- **Go:** free IL-33 or sST2 is prognostic outside SARS-CoV-2, with adjusted OR per SD ≥ 1.5 and lower CI > 1.
- **Kill:** IL-33 is undetectable in patients **and** the sST2 association does not replicate outside SARS-CoV-2.

### Stage 2 (Months 4–12): in vivo proof of concept and antiviral safety

**Models.** At least two virus models, for example mouse-adapted influenza A and either RSV in mice or SARS-CoV-2 in K18-hACE2 mice. Use AX-1177 if it cross-reacts; otherwise use a surrogate anti-mouse IL-33 antibody that binds both redox forms, or human-IL-33 knock-in mice. A surrogate may add about 3 months.

**Controls and dosing.**
- Fc-matched isotype control.
- **Therapeutic dosing at ≥ 48 h after infection** is the decision-relevant arm; a prophylactic arm serves as the mechanistic positive control.
- A dose–response with PK.

**What we measure, and when** (days 3, 5, 7, 10 and 14 after infection):
- survival, weight and SpO2;
- blinded lung histopathology score;
- BAL protein and albumin (barrier);
- BAL cells (neutrophils, eosinophils, ILC2);
- lung endothelial activation (E-selectin and VCAM-1 IHC);
- BAL and serum IL-6 and sST2;
- free and total IL-33 in BAL and serum (target engagement);
- **lung viral titre** (plaque assay and qPCR);
- ISGs;
- repair markers, such as amphiregulin.

**Gates.**
- **Go:** with therapeutic dosing in ≥ 2 models:
  - ≥ 30% reduction in a pre-specified lung-injury composite (or in BAL protein) vs isotype;
  - a dose–response;
  - ≥ 90% suppression of free IL-33 in BAL;
  - peak viral titre not raised by > 0.5 log10, and clearance not delayed.
- **Kill:**
  - efficacy only with prophylactic dosing; or
  - increased viral burden or secondary infection.

**Month-12 committee decision: IND-enabling go or no-go.**
If the answer is go, Stage 3 runs Months 12–24: GLP toxicology in a pharmacologically relevant species (cynomolgus if cross-reactive), tissue cross-reactivity, immunogenicity, Fc effector assessment, CMC, and an FIH dose from PK/PD modelling of free-IL-33 suppression.

---

## 6. What would go into the clinic (only if Stages 0–2 are passed)

**Molecule.** AX-1177 with documented identity (currently a human IgG1 per the annex), given as a single IV dose.
- Dose rationale: maintain ≥ 90% suppression of free IL-33 in serum for at least the 28-day acute course, modelled from Stage 1 potency and Stage 2 PK/PD.
- The package's 10 µg/mL tells us nothing about the minimum effective concentration.

**First-in-human.** A single-ascending-dose study in healthy adults, measuring:
- PK, safety and immunogenicity;
- target engagement: free IL-33 falling and total (drug-bound) IL-33 rising, plus sST2.

**Phase 2 in two parts.** Randomised, double-blind, placebo-controlled, added to standard of care.

*Population.*
- Adults hospitalised with PCR-confirmed viral LRTD: influenza, RSV, SARS-CoV-2 or hMPV, **stratified by virus**.
- On supplemental oxygen but not IMV.
- Randomised within ≤ 72 h of admission. Early treatment matters: IL-33 is a pre-stored alarmin, and the autopsy data suggest the tissue pool may be depleted late in disease.
- **Enriched for high baseline sST2**, using a threshold fixed in Stage 1b.

*Part A (PD and safety, n ≈ 60, 2:1).*
- Target engagement in patients.
- PD trajectories at baseline and days 1, 3, 5, 7, 14 and 28: sST2, IL-6, PTX3, OPG, CCL20, IL-8.
- **Viral-load safety**: nasopharyngeal qPCR on days 1, 3, 5, 7 and 14; time to clearance; secondary infections.
- Go to Part B if target engagement ≥ 90%, PD moves in the direction seen in vitro, and viral clearance is not delayed.

*Part B (efficacy).*
- Primary endpoint: the **30-day composite of ICU admission, invasive mechanical ventilation or death**, the same endpoint on which the sST2 signal was found.
- Sample size, for 80% power to detect a 30% relative risk reduction:

| Control event rate | One-sided α = 0.10 | Two-sided α = 0.05 |
|---|---|---|
| 44% (as in mmc2) | ~121 per arm | ~210 per arm |
| 30% | ~210 per arm | ~366 per arm |
| 20% | ~351 per arm | ~611 per arm |

- Hence the enrichment and a blinded sample-size re-estimation.
- Key secondary endpoints: days alive and free of respiratory support, and time to recovery.

---

## 7. Risks, and what would change this recommendation

**Accelerate** if:
- the withheld IL-33 assay shows a robust, NEWS2-independent association; and
- therapeutic-dosing efficacy holds in two models with no viral penalty.

Then compress Stage 3 and parallelise the CMC work.

**Stop** if any of the following occurs:
- AX-1177 increases viral burden or delays clearance (in vitro or in vivo);
- efficacy appears only with prophylactic dosing;
- neither IL-33 nor sST2 is prognostic outside SARS-CoV-2;
- AX-1177 lacks functional activity against oxidised IL-33 and the reduced form alone shows no in vivo benefit.

**Standing risks:**
- causality is unproven, and IL-33 may be a marker of injury rather than a driver;
- sST2 is non-specific;
- the in vitro systems are non-lung and single-donor;
- the isotype has non-specific effects at 24 h;
- the human evidence is single-centre, pre-vaccination SARS-CoV-2 only.

---

## 8. Methods and reproducibility

**Data conversion.** The xlsx files were converted with R readxl (`analysis/tx/convert.R`). All analyses used Python (pandas, scipy, statsmodels); scripts are in `analysis/scripts/00–13`.

**Transcriptomics.**
- Integrity: gene sets, AveExpr, df inferred from (t, P), BH recomputation, and an SE-inflation screen (SE > 5× the expression-matched rolling median).
- Blockade: signature-level estimates with genes selected on independent timepoint libraries, sign-aligned means, and 1,000 gene-bootstrap CIs.
- Derived contrasts use exact logFC arithmetic on point estimates from the single fit.

**Serum proteomics.**
- Duplicate proteins collapsed across panel suffixes.
- Wald consistency check.
- BH family reconstructed from implied ranks.
- Olink assays mapped to genes (direct symbol matches plus a curated alias map) to build the in vitro–clinical bridge.

**IHC.**
- Blank rows removed; donor-level fields propagated within donor; 'ND' treated as missing.
- Ordinal scores parsed from the text.
- Donor-level means compared with Kruskal–Wallis, Mann–Whitney and Hodges–Lehmann tests, with BH across 11 markers.

**Figures** (`/tmp/outputs/figures/`):
- Fig. 1: HUVEC blockade vs isotype.
- Fig. 2: bias-corrected blockade forest plot.
- Fig. 3: SE-inflation diagnostic.
- Fig. 4: serum volcano plot and BH audit.
- Fig. 5: donor-level IL-33 IHC.

**Limits of this re-analysis.**
- No count matrices, raw NPX values or images were available, so the SE inflation and isotype effect cannot be fully resolved here.
- AveExpr is averaged over all four cell types, so the expression filters are approximate for HUVEC-specific genes.
- All clinical-trial parameters are planning proposals, not findings.
