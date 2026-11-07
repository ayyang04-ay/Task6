**Recommendation: CONDITIONAL GO. Move AX-1177 into a gated de-risking phase of about 12 months, but do not fund a clinical efficacy study on this package. The package shows in vitro IL-33 neutralisation and a severity signal in patients from soluble ST2. It has no in vivo, infection, potency, safety or patient IL-33 (ligand) data, and its data-integrity defects need fixing first.**

# AX-1177 (anti-IL-33) in viral lower respiratory tract disease: proposal to the programme committee

*Basis: this proposal uses only the mounted package:*
- *the methods annex;*
- *`mmc2`: serum proteomics in 100 hospitalised COVID-19 patients;*
- *`mmc3`: immunohistochemistry (IHC) on post-mortem lung from 31 donors;*
- *`mmc4`/`mmc5`: in vitro RNA-seq contrasts.*

*All code, tables and figures are in `/tmp/outputs/analysis/`; `run_all.sh` re-runs everything from the raw files. Every number quoted below is listed with its source file in `analysis/results/key_numbers.csv`.*

*Abbreviations: IMV = invasive mechanical ventilation; q = Benjamini–Hochberg adjusted p; log2FC = log2 fold change. Group labels: V = vehicle, N = NIP228 (isotype control), C = Compound_47, I = IL-33red, IN = IL-33red + NIP228, IC = IL-33red + Compound_47.*

---

## 1. The decision in brief

**The package shows how the antibody works. It does not yet show therapeutic value.**

Three findings are robust:
1. **Mechanism in vitro.** Reduced IL-33 switches on a large NF-κB-type endothelial-activation programme in HUVEC. This includes E-selectin, VCAM-1, ICAM-1, IL-8, IL-6, tissue factor, GM-CSF and G-CSF. The test antibody, Compound_47, neutralises 93–99% of that programme, and shows no reproducible activity on its own.
2. **A signal in patients.** In 100 hospitalised COVID-19 patients, soluble ST2 (sST2, the IL-33 decoy receptor) is the 2nd-ranked of 1,094 serum assays for ICU admission, IMV or death within 30 days. This holds after adjustment for age, sex and NEWS2.
3. **The target is at the site of disease.** IL-33 protein is present in lung endothelium and basal epithelium in every post-mortem donor.

What would justify efficacy spend is missing:
- The IL-33 ligand itself was never measured in patients.
- Lung IL-33 staining is **not** higher in COVID-19 than in controls.
- There are no in vivo or virus-infection data, either for efficacy or for safety (viral clearance).
- There are no potency data.
- Nothing confirms that the tested "Compound_47" is AX-1177.
- No virus other than SARS-CoV-2 was studied.

Several datasets also carry analysis defects (Section 4) that must be corrected before anyone relies on them.

| Option | Assessment |
|---|---|
| Stop | Not justified. The mechanism is clean and large. sST2 is one of only two proteins that survive Bonferroni correction in an unbiased screen of 1,063 proteins. The gaps are testable within about 12 months. |
| Go to clinic now (first-in-human → Phase 2a) | Not justified. There is no dose rationale (no potency), no efficacy or viral-clearance safety data in infection models, and the molecule's identity is unconfirmed. A Phase 2a would cost more and answer less than Stage 1. |
| **Conditional GO (recommended)** | Fund Stage 0 (months 0–3) and Stage 1 (months 3–12) behind pre-specified Gates A and B. Clinical entry happens only at Gate C; the earliest Phase 2a start is about month 15–18 (Section 5). |

---

## 2. Evidence scorecard: does each link of the therapeutic hypothesis hold?

*The hypothesis: viral injury releases IL-33 → IL-33 activates lung endothelium through ST2 → endothelial activation and inflammation drive progression to ICU, IMV or death → AX-1177 neutralises IL-33 → less progression, without harming viral clearance.*

| # | Link | Status | Best evidence in the package | Main limitation |
|---|---|---|---|---|
| 1 | Target present at the disease site | **Supported** | IL-33 stained in endothelium and basal epithelium in all 31 donors; donor-median endothelial score 4.8–5.5 in every group | Scores are off the documented scale; no increase in COVID-19 |
| 2 | Target released or active in viral LRTD | **Not shown** | None. There is no IL-33 ligand assay, and IHC cannot measure release | This is the central gap |
| 3 | IL-33 activates endothelium | **Supported in vitro** | HUVEC at 6 h: 645 genes up, 423 down. SELE +11.2, VCAM1 +8.7, CXCL8 +8.2, ICAM1 +6.0, IL6 +5.8, F3 +5.6 log2FC. Hallmark TNFα/NF-κB set: 98 of 196 genes (19.8-fold enriched) | One donor; umbilical-vein (not lung) endothelium; one IL-33 dose; reduced IL-33 only |
| 4 | Pathway activity tracks severity in patients | **Partial** | sST2 OR 3.02 per log unit (95% CI 1.83–5.01), q = 0.0075, rank 2 of 1,094 | sST2 is not IL-33-specific; 169 proteins pass q < 0.05; the in vitro IL-33 programme is not enriched among severity proteins (p = 0.35) |
| 5 | The antibody neutralises IL-33 | **Supported for Compound_47, at one ratio** | IL-33 signature 93–99% neutralised (measured on independent samples); ≥97% for canonical genes | 41:1 molar excess, added at the same time as IL-33; no IC50; identity with AX-1177 unconfirmed |
| 6 | Neutralisation improves the course of viral LRTD | **Not addressed** | None | No animal or infection model |
| 7 | Safe to block IL-33 during infection | **Not addressed** | None | Viral clearance and tissue repair untested |
| 8 | No off-target activity | **Supported (transcripts only)** | No reproducible antibody-alone signal in 4 cell types and 16 contrasts | Transcript level only; no toxicology |

---

## 3. What the data show, and how robust it is

### 3.1 Serum proteomics (`mmc2`): 100 hospitalised COVID-19 patients, 44 composite events

**Design.**
- One logistic model per assay, adjusted for age, sex and NEWS2. Events per variable = 11 (44 events, 4 parameters).
- 1,094 assays across 13 Olink panels, covering **1,063 unique proteins**; 27 proteins are measured on 2–4 panels.
- The event count is not documented. I recovered it from two undocumented columns: every value in them is an exact multiple of 1/56 or 1/44, which fits 56 patients without the event and 44 with it.

**sST2 (assay "ST2").**
- OR **3.02** per log unit (95% CI **1.83–5.01**), p = 1.7×10⁻⁵, delivered q = **0.0075**.
- Rank **2 of 1,094**; it is the second unique protein, after HGF.
- Bonferroni-adjusted p across the 1,194 tests implied by the q-values = **0.020**. HGF and sST2 are the only two proteins that survive Bonferroni.
- Converted approximately to a per-SD scale, the OR is about 2.4–3.1, depending on how strongly sST2 correlates with the covariates (`planning_calculations.csv`).

**Context: a broad severity proteome, not an IL-33 fingerprint.**
- **178 assays (169 proteins) have q < 0.05, and 176 of the 178 have OR > 1.** Examples:
  - IL-6: OR 2.07–2.31 on four separate panels.
  - PTX3: OR 11.6, q 0.012.
  - IL-8: OR 2.23, q 0.023.
  - CCL20: OR 1.83, q 0.020.
  - MCP-1: OR 2.26, q 0.051.
  - vWF: OR 3.86, q 0.050.
  - ANGPT2: OR 2.21, q 0.052.
- **No IL-33 ligand assay appears in the delivery.** So the human evidence rests on a decoy receptor, not on the molecule AX-1177 binds.
- Because sST2 binds and buffers IL-33, high sST2 can mean either pathway activation or endogenous neutralisation. This package cannot tell the two apart.

**Consistency checks that passed.**
- Every OR lies inside its CI, and the CIs are symmetric on the log scale.
- The p-values can be reproduced from the CIs (maximum deviation 0.0002 log10 units).
- Proteins measured on more than one panel give concordant log-ORs (r = 0.97).

**Caveats.**
- The delivered q-values were computed over about **1,194 tests, not the 1,094 delivered**, so about 100 analysed assays are missing from the file.
- The ORs are per "log unit" of an unstated transform. At similar strength of evidence (z ≈ 4) they range from 2.1 (IL6) to 20.9 (SEMA4C), so OR magnitudes cannot be compared across assays; rank by z or p instead.
- Single centre, pre-vaccination, SARS-CoV-2 only.
- Time from admission to sampling is unstated, so reverse causation cannot be excluded.

### 3.2 Post-mortem lung IHC (`mmc3`): 31 donors, 74 blocks

**Unit of analysis.** The unit is the **donor**, not the block. Three COVID+ donors supply 24 of the 49 COVID+ blocks, so a block-level test would largely be a test of those three people. Figure: `analysis/figures/fig_ihc_il33_donor_level.png`.

**IL-33 is high in all three groups and not raised in COVID-19.** Donor-level comparison of COVID+ pneumonia (n = 16) against all COVID− donors (n = 15):

| Compartment | COVID+ median | COVID− median | Mann–Whitney p | Cliff's δ |
|---|---|---|---|---|
| Endothelium | 4.81 | 5.50 | 0.052 (permutation p 0.044) | −0.38 |
| Vascular smooth muscle | 2.38 | 3.25 | 0.068 (permutation p 0.049) | −0.39 |
| Basal epithelium | 4.25 | 4.75 | 0.76 | −0.07 |

The endothelial and smooth-muscle trends point **downwards** in COVID-19, but they do not survive correction for three compartments. When the 7 donors whose category labels conflict with their pathology are excluded, the p-values become 0.27, 0.26 and 0.55.

**Pseudoreplication matters here.** Testing at block level would have reported p = 0.017 (endothelium) and p = 0.007 (smooth muscle).

**The scale is not as documented.**
- The documented maximum is 5, but the delivered values reach 5.5 in 39 of 74 endothelial blocks and 16 of 71 epithelial blocks.
- The derived eosinophil peroxidase, neutrophil elastase and tryptase columns equal the ordinal score + 0.5 in 100% of blocks, so these are display values, not raw scores.
- 53% of endothelial blocks sit at the ceiling value, which limits how well the scale can discriminate.

**Interpretation.**
- The target is present at the site.
- IHC cannot show release. Lower staining could reflect release of stored IL-33 or loss of tissue; the data cannot distinguish these.
- Endothelial IL-33 correlates inversely with neutrophil elastase (ρ = −0.43, p = 0.016), but this does not survive correction for the 12 tests run. It is compatible with release-associated depletion and is worth testing (Stage 1).

### 3.3 In vitro RNA-seq (`mmc4`/`mmc5`): HUVEC, HGMEC, A549, MCF7; 6 h and 24 h; n = 3 per arm

**IL-33 response in HUVEC.**
- 6 h: **4,031 genes at q < 0.05**; with |log2FC| > 1, **645 up and 423 down**.
- 24 h: 1,836 genes at q < 0.05; 314 up and 198 down. 153 genes are up at both timepoints.
- The induced genes form a canonical inflammatory programme (Hallmark enrichment):
  - TNFα/NF-κB: 98 of 196 genes, 19.8-fold, q = 6×10⁻¹⁰²;
  - inflammatory response;
  - interferon-γ and interferon-α responses;
  - IL-6/JAK/STAT3.
- The repressed genes show no coherent pathway (best q ≥ 0.6), which is consistent with them being largely noise.

**Neutralisation by Compound_47.**
- *Method.* The primary estimate uses sample groups that share no arm, with genes selected at the other timepoint. For example, a signature defined at 6 h is scored on the 24 h samples. This avoids a regression-to-the-mean artefact (see below).
- *Signature defined at 6 h, scored at 24 h:*
  - IL-33 + isotype vs vehicle: **+0.80 log2**;
  - IL-33 + Compound_47 vs vehicle: **+0.06 log2**;
  - → **93% neutralised**.
- *Signature defined at 24 h, scored at 6 h:* +1.72 → +0.01 log2 → **99% neutralised**.
- The isotype control is inert: it moves the signature by ≤ 0.03 log2.
- Compound_47 without IL-33 moves the signature by −0.00 to −0.03, so there is no sign of endogenous IL-33 tone in these cultures.
- *Canonical genes chosen in advance (6 h), IL-33 effect → residual effect with Compound_47:*

| Gene | IL-33 vs vehicle (log2FC) | Residual with Compound_47 (log2FC) |
|---|---|---|
| SELE | +11.21 | +0.31 |
| VCAM1 | +8.74 | +0.09 |
| ICAM1 | +5.97 | +0.11 |
| CXCL8 | +8.19 | −0.17 |
| IL6 | +5.82 | −0.14 |
| CCL2 | +4.16 | −0.10 |
| CSF3 | +8.32 | +0.05 |
| TNF | +7.89 | +0.02 |

  Each of these is at least 97% neutralised. Results: `analysis/results/tx_key_genes.csv`; figure: `analysis/figures/fig_tx_neutralisation_and_se.png`.
- *Why the naive estimates are not quoted.* Contrasts that share an arm (IC−I against I−V) have correlated noise. Analysed within a single timepoint, they suggest a +0.97 log2 "isotype effect" on repressed genes at 24 h. With independent selection, that effect shrinks to +0.05 (`analysis/results/tx_neutralisation_summary.csv`).

**HGMEC.**
- Compound_47 lowers the HUVEC-defined IL-33 genes in HGMEC by a median of −0.79 log2 at 6 h (HUVEC: −1.50) and −0.33 at 24 h (HUVEC: −1.06).
- 42% of these genes fall significantly at 6 h, and 8% at 24 h.
- The HGMEC IL-33-versus-control contrast was **not delivered**, and HGMEC has no vehicle arm. The % neutralisation in a second endothelial type therefore cannot be computed.

**Antibody alone (no IL-33): 16 contrasts across 4 cell types.**
- 632 gene-level hits at q < 0.05:
  - 78% are low-abundance transcripts;
  - 16% have |log2FC| < 0.5;
  - only 6 (1%) are moderately expressed with |log2FC| ≥ 0.5.
- Between 6 h and 24 h, 0–1 genes overlap in any cell line.
- **There is no reproducible off-target transcriptional signal.**

**The delivered RNA-seq statistics are mis-calibrated for a subset of genes. This is the most consequential methodological finding.**
- I compared each gene's delivered standard error with the spread of logFC across 8 internal null contrasts:
  - Compound_47 vs NIP228, and IL-33 + NIP228 vs IL-33;
  - in both endothelial lines, at both timepoints.
- For typical genes the delivered SEs are correct: median ratio 0.99, against an expected 99% range of 0.60–2.44.
- But **364 genes are inflated more than 5-fold, 212 more than 10-fold and 69 more than 100-fold**. These are mostly genes restricted to one cell type.
- As a result, the delivered q-values **miss canonical IL-33 targets** at 6 h:

| Gene | Delivered q | Empirical z |
|---|---|---|
| SELE | 0.50 | 18 |
| VCAM1 | 0.51 | 25 |
| CXCL8 | 0.19 | 35 |
| CCL2 | 0.77 | 40 |
| CXCL1 | 0.999 | 39 |
| PTX3 | 0.98 | 26 |
| IL1RL1 (ST2) | 0.98 | 18 |

- Compound_47 also mirrors every one of these effects.
- The opposite error occurs too. AKR1C2 in A549 gets t = 169 for a log2FC of only 0.11.
- This pattern fits the documented choice of one voom/limma model across four unrelated cell types. Counts of differentially expressed genes from this file are therefore not reliable, while the log2FC effect sizes are.

**Design limits.**
- One concentration of each article: antibody 68.5 nM against IL-33red 1.66 nM (41:1 molar; 83:1 binding sites).
- Antibody added at the same time as IL-33, with no pre-incubation.
- Only the reduced form of IL-33 was tested, although the annex says the antibody also binds the oxidised form.
- One donor per endothelial type, so n = 3 are culture replicates from that donor.
- Neither endothelial type is from lung.
- The epithelial lines were never challenged with IL-33.
- MCF7 (a breast line) has no relevance to lung.
- A DMSO vehicle is irrelevant to an IgG1.

### 3.4 Linking in vitro and clinical data

**The in vitro IL-33 programme does not explain the clinical severity proteome.**
- 910 of the 1,063 Olink proteins map to genes in the RNA-seq table.
- Of those, 83 are IL-33-induced and reversed by Compound_47; 812 are not induced.
- Their severity associations are the same: median z 1.39 vs 1.41 (one-sided Mann–Whitney p = 0.35; permutation p = 0.25). The share at q < 0.05 is 19% vs 17% (Fisher p = 0.35).
- The endothelial-injury markers that do track severity are **not** IL-33-inducible in HUVEC: HGF (the top serum hit) +0.50 log2FC, ANGPT2 +0.09, vWF −0.08.
- Among the severity proteins, sST2 remains the only direct link to the IL-33 pathway.

**The overlap still gives a rational pharmacodynamic (PD) panel.** These markers meet all three criteria: IL-33-induced in HUVEC, reversed by Compound_47, and severity-associated in patients (`bridge_il33_induced_reversed_olink_proteins.csv`):

| Marker | Severity association (q) | In vitro evidence |
|---|---|---|
| sST2 | 0.0075 | IL1RL1 mRNA +1.60 log2 at 6 h (empirical z 18), reversed −1.68 |
| PTX3 | 0.012 | Induced and reversed |
| IL-6 | 0.012 | Induced and reversed |
| OPG | 0.014 | Induced and reversed |
| IL-18R1 | 0.018 | Induced and reversed |
| MCP-3 | 0.020 | Induced and reversed |
| CCL20 | 0.020 | Induced and reversed |
| IL-8 | 0.023 | Induced and reversed |
| IL-1β | 0.046 | Induced and reversed |
| MCP-1 | 0.051 | Induced and reversed |
| E-selectin | 0.091 | Induced and reversed |

None of these is IL-33-specific, so in the clinic they must be read against placebo and alongside direct target-engagement measures.

---

## 4. Data-integrity and methodology findings (closed in Stage 0)

Full log with evidence: `analysis/results/integrity_log.csv`.

| ID | Severity | Finding | Consequence | Action |
|---|---|---|---|---|
| G1 | High | The test article is "Compound_47". The annex never states that it is AX-1177, and it places affinity and potency data outside the package. | Every in vitro conclusion applies to Compound_47. | Sequence/lot identity, or comparability data. |
| T1 | High | RNA-seq standard errors are mis-calibrated: 364 genes inflated >5-fold, plus some deflated rows. | Delivered q-values miss SELE, VCAM1, CXCL8, CCL2 and IL1RL1. | Re-fit per cell line from the archived counts. |
| T6 | High | One dose of each article, added at the same time; reduced IL-33 only; one donor; non-lung endothelium; no IL-33 challenge of epithelium. | No potency, therapeutic-window or redox-form information. | Stage 0/1 experiments. |
| P2 | High | No IL-33 ligand assay delivered. | The human link rests on sST2 alone. | Release the IL-33 assay result, or measure IL-33 with a high-sensitivity assay. |
| H1 | High | IHC values exceed the documented 0–5 scale; derived columns are score + 0.5. | Only ordinal use is defensible. | Release raw scores; add a blinded second reader. |
| H2 | High | IHC blocks are pseudoreplicates. | Block-level p-values are falsely small (0.017 and 0.007). | Analyse at donor level (done here). |
| P1 | Medium | q-values were computed over about 1,194 tests; only 1,094 were delivered. | About 100 assays withheld. | Deliver all assays, with detection rates. |
| P4 | Medium | ORs are per unstated "log unit". | OR sizes cannot be compared across assays. | Report per-SD ORs. |
| T2 | Medium | The HGMEC IL-33 contrast was not delivered. | Neutralisation in HGMEC is unknown. | Deliver it from the archive. |
| T5 | Medium | AveExpr is averaged over all 114 libraries (4 cell types). | Filtering on it would remove the IL-33 programme (e.g. TNF −3.85, CSF2 −3.19). | Report per-group expression. |
| H3 | Medium | Disease labels conflict with the pathology text for 7 of 31 donors; SARS-CoV-2 status is missing for one. | Group contrasts are noisy. | Adjudicate the labels. |
| T3, T4, P3, P5, H4 | Low | The `mmc5` "6h" and "24h" sheets are identical copies. The implied residual df is ≤ 75 against 76 expected. There are undocumented columns, cross-panel duplicates, and inconsistently placed donor fields. | Risk of misreading. | Clean re-issue. |

---

## 5. Proposal: what we measure, in which model, and when

### Stage 0 (months 0–3): make the existing package decision-grade

| Activity | What is measured | Gate A criterion (month 3) |
|---|---|---|
| 0.1 Molecule identity | Sequence/lot identity of Compound_47 and AX-1177. If they differ: SPR affinity for reduced and oxidised IL-33, plus functional comparability. | Identity confirmed, **or** AX-1177 potency within 3-fold of Compound_47 |
| 0.2 Potency and species | First, titrate IL-33red (0.1–100 ng/mL) to find its EC50 and EC80. Then run a 10-point AX-1177 dose–response (0.01–100 nM) against IL-33red at EC80 in HUVEC. Readouts at 6 h and 24 h: E-selectin and VCAM-1 surface protein; IL-6, IL-8 and CCL20 secretion. Also test cross-reactivity with cynomolgus and mouse IL-33. | IC50 and IC90 defined. This sets the toxicology species and whether a surrogate antibody is needed. |
| 0.3 RNA-seq re-analysis (archived counts) | Per-cell-line models; the HGMEC IL-33 vs NIP228 contrast; % neutralisation with CIs | IL-33 programme reproduced with calibrated statistics and ≥ 80% neutralisation; HGMEC response quantified |
| 0.4 Olink completion | All 1,194 analysed assays, **including IL-33** (with detection rate); per-SD ORs; AUC; sST2 distribution; the transform used | sST2 association confirmed per SD; detectability of IL-33 known |
| 0.5 IHC re-read | Raw 0–5 scores; a second blinded reader; adjudicated categories | Weighted κ ≥ 0.6; corrected labels |

### Stage 1 (months 3–12): test the hypothesis where it matters

| Question | Model | Readouts | Timing | Gate B criterion (month ~12) |
|---|---|---|---|---|
| Does viral infection release IL-33, and in which redox form? | Primary human bronchial / small-airway epithelium at air–liquid interface (ALI), ≥ 3 donors, infected with SARS-CoV-2, influenza A and RSV | IL-33 in apical and basolateral media (total; reduced vs oxidised); LDH; viral titre | 24, 48, 72 and 96 h after infection | IL-33 release ≥ 2× mock for ≥ 2 of the 3 viruses |
| Does AX-1177 block IL-33 in **lung** endothelium at realistic timing? | Primary human lung microvascular endothelial cells (≥ 3 donors), with HUVEC as a bridge to the existing data. Stimuli: IL-33red, IL-33ox, and conditioned medium from the infected ALI cultures | Surface SELE/VCAM-1/ICAM-1; secreted IL-6, IL-8, CCL2, CCL20, G-CSF and GM-CSF; the 645-gene signature (as a targeted panel); barrier function (impedance, dextran flux) | Antibody added 30 min before, at the same time as, 1 h after, or 4 h after IL-33; readouts at 6, 24 and 48 h | IC90 achievable at the projected clinical exposure; ≥ 50% inhibition retained when the antibody is added 1–4 h late |
| Does neutralisation in infected human lung reduce injury without raising virus? | Human precision-cut lung slices (≥ 4 donors) infected with influenza or SARS-CoV-2, ± AX-1177 | IL-33 release; the PD panel; endothelial markers; viral titre; viability | 24–72 h | PD markers fall; no ≥ 0.5 log10 rise in viral titre |
| Does therapeutic blockade improve viral LRTD in vivo, and is it safe? | Mouse influenza A (sublethal and lethal doses) and SARS-CoV-2 MA10 in aged BALB/c mice. Use AX-1177 if it cross-reacts; otherwise a surrogate anti-mouse IL-33 antibody with an isotype control. IL-33- or ST2-deficient mice serve as a genetic benchmark. | Survival, weight and SpO₂; BAL protein/albumin and lung wet/dry ratio; blinded histology (diffuse alveolar damage score); BAL and serum sST2, IL-6, CXCL1/KC, CCL20 and E-selectin; lung viral titre and clearance; antiviral antibody and CD8 T-cell responses; repair and fibrosis at day 21 | Dose on day 1 **and** day 3 after infection (therapeutic), plus day −1 as a mechanistic control; readouts on days 3, 7, 10, 14 and 21; n ≈ 12–16 per group per timepoint (assumes CV 25–30% for BAL protein) | ≥ 30% reduction in BAL protein or histology score against isotype in ≥ 1 model, in the same direction in the second; **no** rise in lung viral titre > 0.5 log10 and no delay in clearance; PD markers move as predicted |

### Stage 2 (months 6–15, in parallel): clinical enabling

- **Toxicology.** GLP toxicology in the species chosen in step 0.2, plus tissue cross-reactivity on human tissues.
- **Dose selection.** A PK/PD model to pick the clinical dose that keeps free antibody in the lung interstitium at least 10× above the IC90 through day 28.
- **Assays.** Validated assays for sST2, for free IL-33 and IL-33–sST2 complexes, for total (drug-bound) IL-33 as the target-engagement readout, and for the Section 3.4 PD panel.
- **sST2 validation in banked sera.** Use sera from patients hospitalised with influenza, RSV and COVID-19, with the same composite endpoint and the same adjustment for age, sex and NEWS2, under a pre-registered analysis plan. About **130–300 patients per virus** gives 80–90% power for a per-SD OR of 1.8 at event rates of 15–30%. IL-33 is measured in the same samples.
- **First in human.** If AX-1177 has not yet been dosed in humans, run a single-ascending-dose study in healthy volunteers covering PK, safety, immunogenicity and target engagement.

### Gate C: clinical entry (around month 15)

Clinical entry requires all of the following:
- Gates A and B passed.
- Clean toxicology.
- First-in-human PK supports target coverage from a single dose.
- sST2 replicated (lower 95% CI of the per-SD OR > 1) in at least one non-COVID viral cohort.
- IL-33 detectable in a meaningful fraction of severe patients.

### Kill criteria (any one stops the programme)

1. AX-1177 is not the tested molecule **and** its potency is > 3-fold weaker, with no path to fix it.
2. Fewer than 2 of the 3 viruses release IL-33 in human epithelium.
3. Therapeutic dosing gives no benefit in either in vivo model.
4. IL-33 blockade increases viral burden or delays clearance.
5. The sST2 signal fails to replicate **and** IL-33 is undetectable in patients.

---

## 6. What goes into the clinic (after Gate C)

**What we take in.**
- The AX-1177 GMP drug product (IV).
- Validated assays for sST2 (used for stratification), free and total IL-33 (target engagement), the PD panel and viral load.

**Phase 2a proof-of-mechanism: design.**

| Element | Proposal | Basis |
|---|---|---|
| Design | Randomised 1:1, double-blind, placebo-controlled, on top of standard of care | |
| Population | Adults hospitalised with PCR-confirmed viral LRTD (SARS-CoV-2, influenza, RSV); on supplemental oxygen; not mechanically ventilated; enrolled early after admission, with the exact window set from the Stage 1 timing data | `mmc2` sampled at enrolment in this setting |
| Stratification | Virus; baseline sST2 (validated cut-point); NEWS2; use of corticosteroids or IL-6/JAK inhibitors | These drugs directly perturb the IL-6-linked PD markers |
| Dose | A single IV dose of AX-1177, at the dose Stage 2 predicts gives ≥ 90% IL-33 neutralisation to day 28 | |
| Primary endpoint | Change from baseline to day 3 in a composite endothelial IL-33 response score: the mean z of IL-6, IL-8, CCL20, MCP-1, E-selectin and PTX3. The endpoint is locked after the Stage 1 in vivo PD time-course. | Section 3.4 |
| Co-primary safety | Nasopharyngeal viral load: area under the curve, days 1–14 | |
| Key secondary | Target engagement (suppression of free IL-33; accumulation of total IL-33); change in sST2; time to clinical improvement; oxygen-free days; the composite of ICU, IMV or death by day 30 | The composite is the `mmc2` endpoint |
| Sampling | Serum before dosing, at 6–24 h, and on days 3, 7, 14 and 28. Viral load daily on days 1–7, then days 10 and 14. NEWS2 daily. Safety follow-up to day 90. | |
| Size | About **65 per arm** detects a 0.5-SD PD difference (80% power, two-sided α 0.05); 85 per arm gives 90% power. Allowing for strata and dropout: about 150 in total. | |

**Progression to Phase 2b requires:**
- a PD effect of at least 0.5 SD, with target engagement of at least 90%;
- a viral-load AUC difference within 0.5 log10;
- a favourable trend in clinical endpoints, especially in the sST2-high stratum.

**Why enrichment matters for Phase 2b/3.** Sample sizes on the composite endpoint (80% power, two-sided α 0.05):

| Control event rate | Per arm, 25% relative risk reduction | Per arm, 33% relative risk reduction |
|---|---|---|
| 44% (the pre-vaccination `mmc2` cohort) | **306** | **172** |
| 20% (a plausible current rate) | **906** | **501** |

Current hospitalised populations are likely to have lower event rates than the `mmc2` cohort. That makes a validated enrichment biomarker (sST2, or IL-33 itself) the main cost lever for the programme.

---

## 7. Key risks

1. **Correlation, not causation.** The human evidence is association only. sST2 is non-specific and may reflect buffering rather than IL-33 activity. *Mitigation:* the Stage 1 in vivo, ex vivo and IL-33 release work, plus measuring IL-33 itself.
2. **Timing.** An alarmin may act before patients reach hospital. *Mitigation:* the delayed-addition and therapeutic-dosing designs; day-3 PD in the Phase 2a.
3. **Safety during infection.** Blocking IL-33 could slow viral clearance or tissue repair. *Mitigation:* viral load as a gate in both animals and humans; readouts to day 21 in mice and day 90 in the clinic.
4. **Narrow evidence base.** All clinical data are single-centre, pre-vaccination and COVID-19 only. *Mitigation:* multi-virus validation cohorts.
5. **Molecule.** Identity, potency and redox-form coverage are all unverified. *Mitigation:* Gate A.
6. **Data quality.** The issues in Section 4 could shift details once corrected. The headline effect sizes above were computed in ways that do not depend on the flawed statistics (donor level; independent-sample neutralisation; effect sizes rather than the delivered q-values).

---

## 8. Methods and reproducibility

Code lives in `analysis/`; Python runs in the `singlecell` environment and R (limma, msigdbr, org.Hs.eg.db) in `renv`. `run_all.sh` re-runs the full pipeline from the mounted files in about 4 minutes.

| Script | What it does |
|---|---|
| `01` | File checksums; structure of the `mmc5` sheets (identical copies); gaps between delivered contrasts and the design. |
| `02` | Proteomics: OR/CI/p consistency; reconstruction of the family size used for the q-values; recovery of the event count; reconciliation of cross-panel duplicates; z-based comparisons. |
| `03` | IHC: donor-level aggregation; Mann–Whitney, permutation, Hodges–Lehmann and Cliff's δ; block-level tests shown only as a pseudoreplication contrast; audit of labels against pathology text; sensitivity analysis; checks of the score scale. |
| `04` | RNA-seq: SE calibration against internal null contrasts; neutralisation estimated from arms with no shared samples plus cross-timepoint selection; antibody-alone analysis; degrees of freedom implied by t→P. `04a`/`04b`: Hallmark over-representation. |
| `05` | Link between the in vitro programme and the serum proteome (Olink names mapped to HGNC symbols; Mann–Whitney, permutation and Fisher tests). |
| `06` | Planning calculations. |
| `07` | Integrity log. |
| `08` | Key-numbers table. |

**Assumptions and limits of this re-analysis.**
- Only summary statistics were delivered: no counts, no patient-level proteomics, and no raw IHC scores. The findings are therefore limited to what those statistics support.
- Figures in the plan that rest on general domain knowledge rather than the package are marked as assumptions in the tables: model choices, CVs, and the n per group in animal studies.
- The identity of Compound_47 with AX-1177 is treated as **unverified** throughout.
