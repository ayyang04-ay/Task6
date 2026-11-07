**Recommendation: NOT YET. Do not start IND-enabling work or clinical dosing of AX-1177 on this package. Approve a 9-month programme of target validation and translational work, with pass/fail criteria fixed in advance, and take the clinical-entry decision at month 9.**

---

# AX-1177 (anti-IL-33): proposal to the programme committee

**Scope.** I read the whole package in `/tmp/world/filesystem`: the methods annex, `mmc2` (serum proteomics), `mmc3` (post-mortem lung IHC), `mmc4` and `mmc5` (RNA-seq contrasts). I re-analysed it from the delivered tables. Every number below comes from those files. Scripts, tables and figures are in `/tmp/outputs/analysis/`, and `run_all.sh` regenerates everything. Where I use general scientific background that is not in the package, I label it *[background]*.

**Naming.** The test article in the package is **Compound_47**. The package never says that Compound_47 *is* AX-1177. I use "Compound_47" for data and "AX-1177" for the programme. Confirming that they are the same molecule is the first gate (G0).

---

## 1. The decision in brief

1. **The package shows one thing well: the antibody works in a dish.** In HUVEC, reduced IL-33 (IL-33red, 30 ng/mL) switches on a large NF-κB inflammatory and adhesion programme: 4,031 genes change at FDR < 0.05 at 6 h.
   - Compared with the isotype control, Compound_47 blocks **96.1 %** of a 153-gene core IL-33 signature at 6 h (gene-bootstrap 95 % CI 91.9–100.0).
   - It blocks **73.5 %** at 24 h (67.2–79.3).
   - On its own, with no IL-33 added, it has no reproducible effect on gene expression in any of the four cell lines.
2. **The package does not show that IL-33 drives viral lower respiratory tract disease (LRTD).** Three observations:
   - **IL-33 was never measured in patients.** It is absent from all 1,094 delivered serum assays.
   - **Lung IL-33 staining is not higher in COVID-19.** At donor level it is, if anything, lower in COVID-19 lungs than in controls: endothelium median 4.81 vs 5.50; one-sided p = 0.98 for "higher in COVID+".
   - **The severity signal in serum is generic inflammation, not IL-33.** Serum proteins that IL-33 induces in endothelium are no more likely than other proteins to track outcome (20.4 % vs 18.6 %; OR 1.12; p = 0.68).
3. **The only IL-33-pathway signal in patients is soluble ST2 (sST2), and it is indirect.** sST2 is one of the two strongest of 1,063 proteins: OR 3.02 per log unit (95 % CI 1.83–5.01), adjusted for age, sex and NEWS2; q ≈ 0.01. But it sits among 186–194 proteins associated at q < 0.05, so it is part of a broad severity signal. It is also SARS-CoV-2-only, from a single centre in the pre-vaccination era.
4. **Everything else needed to go to the clinic is absent:**
   - potency or IC50 (only one 41:1 antibody-to-IL-33 molar ratio was tested);
   - any test of oxidised IL-33, although dual binding is the molecule's stated property;
   - lung cells, and any virus;
   - in vivo efficacy, PK and safety;
   - any virus other than SARS-CoV-2.
5. **Data-integrity problems mean even the positive result must be re-derived before anyone relies on it.** The main ones:
   - The delivered p-values cannot be used for 167 genes. Among them are the classic endothelial-activation genes SELE, VCAM1, CXCL8, CXCL1 and CCL2, which the delivered FDRs call "not significant" despite 4–11 log2 induction.
   - The serum adjusted p-values were computed over 1,194 tests, but only 1,094 were delivered.
   - The IHC scores exceed their documented 0–5 scale, and 49 % of COVID+ blocks come from three donors.
6. **Why "not yet" rather than "stop".** The human data are *uninformative* about IL-33 release rather than negative. IHC shows stored IL-33, and serum IL-33 was not measured. The molecule does what it should in vitro. The decisive experiments are cheap and can use samples that already exist: the same 100 sera, and tissue RNA already extracted from 22 of the 31 post-mortem donors.

---

## 2. Evidence scorecard: each link in the therapeutic hypothesis

| Link the programme needs | What the package contains | Key numbers | Verdict |
|---|---|---|---|
| **A. Compound_47 = AX-1177, with adequate potency and species cross-reactivity** | Annex: potency and affinity "held in the programme biologics file… not part of this dataset" | none | **Absent** |
| **B. IL-33red activates endothelium** | HUVEC RNA-seq, IL-33red vs vehicle (`mmc4`) | 4,031 / 1,836 genes at FDR < 0.05 (6 h / 24 h). SELE +11.2, CSF2 +10.3, CCL20 +9.2, VCAM1 +8.7, CXCL8 +8.2, ICAM1 +6.0, IL6 +5.8 log2FC at 6 h. Induced genes include 49 % (91/186) of MSigDB Hallmark TNFα→NF-κB genes (OR 43.7) | **Strong in vitro** (single donor, non-lung endothelium) |
| **C. Compound_47 neutralises IL-33red** | IL-33+Compound_47 vs IL-33+isotype (NIP228), HUVEC and HGMEC (`mmc5`) | Core signature (n = 153): 96.1 % (91.9–100) at 6 h, 73.5 % (67.2–79.3) at 24 h. ≥ 80 % neutralisation in 81.7 % / 55.6 % of genes. HGMEC: 93.5 % / 78.4 % of core genes reduced | **Strong in vitro, at one 41:1 molar ratio, antibody added at the same time as IL-33** |
| **D. No IL-33-independent activity** | Compound_47 vs NIP228 / PBS / DMSO alone, 4 lines × 2 times | 14–73 "hits" per contrast, 53–95 % of them low-abundance. 0–1 hits shared between 6 h and 24 h; genome-wide ρ(6 h, 24 h) between −0.09 and 0.04. No relation to the IL-33 programme (ρ ≤ 0.04, p ≥ 0.45) | **Supported** (transcriptome level only; no Fc-effector cells tested) |
| **E. IL-33 is released or active in viral LRTD lungs** | Post-mortem IHC (`mmc3`), 31 donors | COVID+ vs COVID− donors: endothelium Cliff's δ −0.38 (p = 0.052); vascular smooth muscle δ −0.39 (p = 0.068); basal epithelium δ −0.07 (p = 0.76). None higher in COVID+ | **Not supported** (IHC cannot measure release) |
| **F. IL-33 pathway activity predicts severity** | Serum Olink panels, 100 patients (`mmc2`) | IL-33 absent. sST2 OR 3.02 (1.83–5.01), q ≈ 0.01. IL-33-induced endothelial products not enriched among outcome-associated proteins (OR 1.12, p = 0.68) | **Weak / indirect** |
| **G. Relevant beyond SARS-CoV-2** | none | all human data are SARS-CoV-2, pre-vaccination | **Absent** |
| **H. Efficacy, PK, safety and dose in vivo** | none | none | **Absent** |

---

## 3. Problems that change how the package must be read

| # | Problem | Evidence | Consequence and fix |
|---|---|---|---|
| 1 | **Implausible standard errors for 167 genes in the RNA-seq tables** | I derived each SE as \|logFC / t\| (`tables/tx_gene_SE_flags.csv`, `figures/fig3_SE_anomalies.png`).<br>• Median SE is 0.33; the maximum is **36,723 log2 units**.<br>• For the same gene, SEs differ up to **225,000-fold** between contrasts. One fit shares each gene's variance across contrasts, so that would need precision weights differing about 10¹⁰-fold.<br>• A simulation of the annex's pipeline (same 114 libraries and 38 groups, deliberately harsh conditions) never gave an SE above **3.7**, below **0.08**, or a within-gene ratio above **3.6** (`sim_voom_pooled_model.R`).<br>• The affected genes are cell-type-restricted (CDH5, CD93, VWF, PECAM1; KRT8/19). That fits the annex's single model across four very different cell lines being mis-specified. | The delivered FDRs call **SELE +11.2 (q = 0.50), VCAM1 +8.7 (0.51), CXCL8 +8.2 (0.19), CXCL1 +8.2 (1.00), PTGS2 +4.4 (0.98), CCL2 +4.2 (0.77)** not significant. Any count of "significant genes", or any biomarker choice based on those q-values, is unreliable. I used effect sizes and isotype-controlled contrasts instead. **Fix:** re-fit from the archived counts, one cell type per model. |
| 2 | **The wrong comparator inflates neutralisation** | Using the IL-33-alone arm as reference (`Compound_47_IL33_vs_IL33`) gives 82 % reversal of IL-33-repressed genes; the isotype comparator gives 41 %. The gap comes from noise in the shared IL-33-alone libraries. When genes are selected and evaluated on independent libraries, NIP228 itself does nothing (median −0.08 to +0.05 log2FC). | The primary readout must be **IL-33+Compound_47 vs IL-33+NIP228**. IL-33-repressed genes are mostly low-abundance transcripts (190 of 208 with AveExpr < 0) and poorly reproducible, so neutralisation claims rest on the induced programme. Genes "induced" only at 24 h show the same artefact, so the 153-gene core signature requires induction at both timepoints. |
| 3 | **Sheets mislabelled and padded** | `mmc5` sheets "6h" and "24h" hold the *same* 24 contrasts (both timepoints), with identical values. Sheet "6h" is padded with 419,535 blank rows up to Excel's 1,048,576-row limit. The `mmc4` contrast is labelled "Nontreated", not "Vehicle". | No data were lost, but reading sheet names at face value gives the wrong timepoint. |
| 4 | **Design gaps in vitro** | No vehicle arm in HGMEC, so the IL-33 effect there cannot be estimated. A549/MCF7 never received IL-33. DMSO is not a vehicle for an antibody. One donor per endothelial line (HUVEC P2, HGMEC P5), so "n = 3" means three wells from one donor. | HGMEC supports neutralisation in direction only. The epithelial lines test nothing about IL-33 biology. |
| 5 | **Serum delivery incomplete; multiplicity mismatch** | Delivered adj.p reproduces BH over **1,194 tests** exactly at the top ranks (over 1,094 it misses by up to 0.013), so **100 tested assays were not delivered**. 102 of 1,196 nominal panel slots are empty. 27 proteins appear on 2–4 panels (58 assays), with good agreement (r = 0.96 for log OR). | Retrieve the missing assays and the LOD/QC table, and confirm whether IL-33 was run. The re-adjustment on 1,063 unique proteins changes nothing material (sST2 q 0.0075 → 0.010). |
| 6 | **Event count not documented** | The undefined columns `composite_endpoint_0/1` are fractions with denominators 56 and 44. | I infer **44 events in 100 patients**, about 11 events per model parameter. The ORs are imprecise (e.g. CSF-1 OR 90, CI 4–1,933) and prone to winner's curse, so I rank markers by Wald z, not OR. |
| 7 | **IHC scale and coding undocumented** | IL-33 scores reach **5.5** on a scale documented as 0–5. The other numeric IHC columns equal the ordinal "n+" grade + 0.5 in every block (74/74, 71/71, 71/71). The IL-33 quarter-point values (x.25, x.75) have no documented derivation. **53 %** of endothelial blocks sit at the maximum, so there is a ceiling. | Treat the scores as ordinal and analyse at donor level. Re-score blinded with two readers. |
| 8 | **IHC pseudo-replication and labelling** | 74 blocks from 31 donors, 1–8 blocks each. Three COVID+ donors supply 24/49 (49 %) of COVID+ blocks. Block-level tests would give p = 0.017 (endothelium) and 0.007 (vascular smooth muscle); the correct donor-level values are 0.052 and 0.068. Donor 1905 has no SARS-CoV-2 status. Donor 1976 is labelled "non-pneumonia" but the report says "acute and organizing pneumonia". Emphysema or fibrosis appears in both groups. Single reader; blinding not stated. | The donor is the unit of analysis. Clean the labels. |

---

## 4. Evidence in detail

### 4.1 In vitro (`mmc4`, `mmc5`): a clean, narrow positive

- **What IL-33red does (HUVEC, vs vehicle).** It triggers a canonical NF-κB programme:
  - the top genes by t are NFKBIA, RIPK2, TNFAIP3, NFKB1/2, TRAF1 and RELB;
  - the biggest inductions are in adhesion molecules, chemokines and growth factors (table below) and tissue factor (F3 +5.6);
  - Hallmark pathways: TNFα→NF-κB (91/186 genes, OR 43.7), IFN-γ, inflammatory response, IL6/JAK/STAT3;
  - the response is larger at 6 h (4,031 genes) than at 24 h (1,836).

  *Implication:* this is the same programme that TNF and IL-1 drive *[background]*. In patients, IL-33 would be one of several redundant inputs. The reversal by an IL-33-specific antibody does, however, argue that the in vitro response is IL-33-mediated, and not from a contaminant of the recombinant protein.
- **Neutralisation, using the isotype comparator** (`figures/fig1`, `tables/tx_core_signature_neutralisation.csv`). The slope of (Compound_47 vs isotype) on the IL-33 response is −0.98 across the 644 genes induced at 6 h and −0.75 across the 314 induced at 24 h (−1 means full reversal).
- **Why the core signature requires induction at both timepoints.** The 6 h and 24 h libraries are independent, so requiring both filters out noise.
  - Genes induced ≥ 4-fold at 24 h *and* at 6 h (n = 85): 80 % median reversal.
  - Genes "induced" only at 24 h (n = 91; low abundance; 6 h log2FC 0.03): 22 % median reversal. They behave like noise in the shared IL-33-alone arm (`tables/tx_24h_replication_check.csv`).

  For canonical genes, the remaining response with Compound_47 is near zero at 6 h:

  | Gene | IL-33 log2FC, 6 h / 24 h | % neutralised, 6 h / 24 h |
  |---|---|---|
  | SELE | 11.2 / 4.7 | 98 / 87 |
  | VCAM1 | 8.7 / 3.4 | 100 / 88 |
  | ICAM1 | 6.0 / 2.2 | 99 / 94 |
  | CXCL8 | 8.2 / 5.6 | 103 / 94 |
  | CCL20 | 9.2 / 5.6 | 107 / 94 |
  | CSF2 | 10.3 / 8.1 | 119 / 104 |
  | IL6 | 5.8 / 2.8 | 103 / 84 |
  | CXCL10 | 6.9 / 5.0 | 109 / **43** |

  Neutralisation is less complete at 24 h (73.5 % vs 96.1 %).

  *Why that matters:* antibody and IL-33 were added at the same time, with no pre-incubation and no delayed-addition arm. This design resembles prophylaxis. Whether AX-1177 can reverse an activation that is already running, which is the situation in hospitalised patients, is untested.
- **HGMEC.** IL-33+Compound_47 vs IL-33+NIP228 lowers 93.5 % of core genes at 6 h (SELE −8.7, VCAM1 −11.7, CSF2 −7.1, CSF3 −6.5 log2FC). The percentage neutralised cannot be computed because the HGMEC IL-33 response was never delivered or designed.
- **Antibody alone.** There is no reproducible signal (see section 2, row D). Among 10,776 well-expressed genes, 11–43 have |log2FC| > 1. That matches the 8–37 seen when two control arms are compared with each other (NIP228 vs PBS, DMSO vs PBS).
- **Pharmacology, derived from the annex.** Compound_47 at 10 µg/mL is 68.5 nM; IL-33red at 30 ng/mL is 1.66 nM. That is a **41:1 molar excess** at a single concentration, so potency is unknown. A weak antibody could look just as complete at this ratio.

### 4.2 Clinical serum proteomics (`mmc2`): a real but unspecific signal

- **Design.** 100 hospitalised SARS-CoV-2 patients; 44 composite events (inferred). Logistic regression per assay, adjusted for age, sex and NEWS2.
- **Breadth of the signal.** **186–194 of 1,063 unique proteins (≈ 18 %)** are associated at q < 0.05. They include intracellular proteins (NPM1, CALR, PXN, APBB1IP), which points to a broad signal of injury and severity.
- **IL-33 axis.**
  - IL-33 and IL1RAP are not in the delivery.
  - **sST2:** OR 3.02 (1.83–5.01), p = 1.7 × 10⁻⁵, rank 1–2 of 1,063, approximate per-SD OR ≈ 2.4.
  - IL-1R2 (decoy receptor): 4.52, q = 0.018.

  *[background]* sST2 is a decoy receptor that binds IL-33, and inflammatory stimuli other than IL-33 also raise it. High sST2 therefore does not mean high free IL-33 activity.
- **Bridge to the in vitro data** (`tables/bridge_*`, `figures/fig4`). Method: of the 910 serum proteins whose genes are in the RNA-seq table, I marked the 93 that IL-33red induces in HUVEC, then asked whether those 93 are more often outcome-associated than the rest.
  - **Result:** they are not. 19/93 (20.4 %) vs 152/817 (18.6 %); Fisher OR 1.12, p = 0.68. Excluding the flagged genes gives OR 1.08, p = 0.77.
  - **Adjusted model:** outcome association tracks membership of generic NF-κB/inflammatory gene sets (OR 2.79, 1.53–5.08). Once that is accounted for, IL-33 inducibility adds nothing (OR 0.68, 0.36–1.29; p = 0.24).
  - **The two strongest serum markers** (sST2, HGF) are not induced by IL-33 in HUVEC (HGF +0.5, not significant).
  - **The most IL-33-inducible products do not track outcome:** VCAM-1 OR 1.28 (p = 0.43), G-CSF 1.25 (p = 0.23), CXCL6 1.02 (p = 0.95), ICAM-1 1.67 (p = 0.11).
- **Candidate biomarkers for drug effect (PD).** A subset of proteins is IL-33-inducible, reversed ≥ 80 % by Compound_47 at both timepoints, *and* associated with outcome:

  | Protein | IL-33 log2FC 6 h / 24 h | Neutralised 6 h / 24 h | Serum OR (q) |
  |---|---|---|---|
  | IL-6 | 5.8 / 2.8 | 103 % / 84 % | 2.07–2.31 on 4 panels (q 0.012–0.019) |
  | CCL20 | 9.2 / 5.6 | 107 % / 94 % | 1.83 (0.020) |
  | OPG (TNFRSF11B) | 4.8 / 2.4 | 104 % / 88 % | 4.40–6.77 (0.014–0.020) |
  | IL-18R1 | 3.6 / 1.2 | 96 % / 81 % | 6.07 (0.018) |
  | IL-8 (CXCL8; flagged) | 8.2 / 5.6 | 103 % / 94 % | 2.23 (0.023) |
  | sE-selectin (SELE; flagged) | 11.2 / 4.7 | 98 % / 87 % | 2.08 (q ≈ 0.09) |

  These are the panel I propose below. They are generic NF-κB outputs, so they work as a drug-effect readout only against placebo, not as proof of mechanism in isolation.

### 4.3 Post-mortem lung IHC (`mmc3`): target present, not increased

- **Groups.** 31 donors: 16 COVID+ pneumonia, 10 COVID− pneumonia, 5 COVID− non-pneumonia; aged 64–98, all white. Comparisons are donor-level, Mann–Whitney with Hodges–Lehmann (HL) shift estimates (`tables/ihc_*`, `figures/fig5`).
- **Results, COVID+ vs all COVID−:**

  | Compartment | Median, COVID+ vs COVID− | HL shift (95 % CI) | One-sided p for "higher in COVID+" |
  |---|---|---|---|
  | Endothelium | 4.81 vs 5.50 | −0.19 (−1.0 to 0.0) | 0.98 |
  | Vascular smooth muscle | 2.38 vs 3.25 | −0.63 (−1.47 to 0.0) | 0.97 |
  | Basal epithelium | 4.25 vs 4.75 | 0.0 (−0.75 to +0.5) | 0.63 |

- **The result is robust** to how blocks are combined per donor: mean, first block or maximum block.
- **The scoring can detect differences.** Neutrophil elastase is clearly higher in COVID+ than in non-pneumonia controls (δ 0.80, p = 0.008).
- **Reading it correctly.** *[background]* IL-33 is a stored alarmin, so these scores measure the tissue store, not released IL-33. Lower staining in COVID+ fits release, cell loss or lower production equally well. What the data do establish is that the target sits abundantly in lung endothelium and basal epithelium in every group. What they do not support is any claim that IL-33 is "upregulated in COVID-19 lung".
- **Power.** With 16 vs 15 donors, power to detect a 0.8-SD shift is about 52 %; about 30 donors per group are needed for 80 %.

### 4.4 Not in the package: this is what blocks clinical entry

- The Compound_47 ↔ AX-1177 link, affinity, IC50, and species cross-reactivity.
- Any test of oxidised IL-33.
- Lung microvascular endothelium or airway/alveolar epithelium.
- Any viral infection, in vitro or in vivo.
- Any in vivo pharmacology, PK, toxicology or immunogenicity.
- Patient IL-33 levels, kinetics or airway samples.
- Any non-SARS-CoV-2 virus.
- The RNA-seq count matrices (held in archive).
- The tissue RNA already extracted from 22 of the 31 post-mortem donors (IDs `Zr4940_*`; data not delivered).

---

## 5. Why "not yet" rather than "go" or "stop"

- **Not "go".** Clinical entry needs three things, and none is in the package:
  - evidence that IL-33 is active in the target patients (links E and F are absent or indirect);
  - a dose rationale (no potency, PK or target-concentration data);
  - safety in an infected host *[background: IL-33 also supports antiviral CD8/NK responses and epithelial repair, so blocking it could slow viral clearance]*.

  The serum proteomics also points to a **redundancy risk**: severity tracks generic NF-κB inflammation, not the IL-33-specific endothelial programme.
- **Not "stop".** No result in the package *refutes* the hypothesis:
  - IHC cannot see release, and serum IL-33 was never measured;
  - sST2 is among the top prognostic signals after adjusting for NEWS2;
  - the antibody neutralises cleanly.

  The cheapest decisive tests use material that already exists.

---

## 6. The plan: what we measure, in which model, and when

Timing is in months from approval. Each gate's criteria are fixed in advance; failing a gate triggers the stated consequence.

| ID | Question | What we measure | Model / samples | When | Pass | Fail → consequence |
|---|---|---|---|---|---|---|
| **G0** | Is the positive result real, and does it belong to AX-1177? | Sequence and lot identity of Compound_47 vs AX-1177. KD and IC50 for IL-33red and IL-33ox. Cross-reactivity (cynomolgus, mouse, hamster, cotton rat). Re-fit the RNA-seq per cell type from archived counts, with replicate-level CIs. Retrieve the 100 undelivered Olink assays and the LOD table. Settle the IHC coding. | Biologics file; archive | 0–1.5 | Identity confirmed. Core-signature neutralisation ≥ 80 % at 6 h (lower CI ≥ 70 %) after re-analysis. | If not the same molecule: repeat the HUVEC experiment with AX-1177 before anything else. |
| **A1** | Is IL-33 released, and does it track severity? | Free IL-33, IL-33:sST2 complex, sST2 (quantitative). Same adjusted logistic model as the annex. | Existing 100 sera (44 events) | 1–3 | An IL-33 measure with adjusted per-SD OR ≥ 1.8 and p < 0.05; n = 100 gives about 50–70 % power (`power_replication_cohort.csv`) | No association and IL-33 undetectable in most sera → LRTD indication only survives if A3 airway fluid is positive. |
| **A2** | Is the IL-33 endothelial programme active in diseased lung? | RNA-seq of existing tissue RNA, scored with the 153-gene core signature plus an IL-33-specific sub-signature (from the B1 counter-screen). | 22 donors with RNA (9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia) | 1–4 | Signature higher in COVID+ than COVID− pneumonia (donor-level δ ≥ 0.4) | Negative → lowers priority of the endothelial mechanism. |
| **B1** | Potency, specificity and the treatment window in lung endothelium | Full dose–response of IL-33red and IL-33ox (0.1–100 ng/mL) × 8-point AX-1177 titration (IC50/IC90). Antibody added at −1, 0, +1, +4, +8 h relative to IL-33. Readouts at 2, 6, 24, 48 h: surface E-selectin/VCAM-1/ICAM-1; secreted IL-6, CCL20, GM-CSF, IL-8; RNA-seq; barrier (ECIS/TEER). Counter-screens with TNF, IL-1β and LPS. | Primary human lung microvascular endothelial cells, ≥ 3 donors; HUVEC as bridge | 1–5 | IC90 defined. ≥ 80 % inhibition of E-selectin/VCAM-1 in every donor. ≥ 50 % inhibition kept with +4 h addition. | Works only when given first → limit to prophylaxis or stop. |
| **B2** | Is IL-33 released by infected epithelium, and is antiviral defence intact? | IL-33 release (apical and basal), IL-33ox, barrier, LDH, interferon response, viral titre ± AX-1177 vs isotype | Primary bronchial air-liquid-interface and alveolar cultures, infected with SARS-CoV-2, influenza A, RSV (≥ 3 donors) | 2–6 | IL-33 release with ≥ 2 of 3 viruses. Injury readouts down ≥ 30 %. Viral titre up no more than 0.5 log₁₀. | Titre increase → stop. |
| **B3/B4** | Integrated lung tissue; immune safety | Endothelial activation, leak and cytokines in infected human precision-cut lung slices. NK/CD8 IFN-γ and granzyme with IL-33 ± AX-1177. | Human precision-cut lung slices; blood immune cells | 3–7 | ≥ 30 % reduction in lung-slice activation. No > 20 % loss of antiviral effector function. | Loss of antiviral function → stop. |
| **C1** | Efficacy in vivo, target engagement, dose | Free and total IL-33 in BAL and serum (target engagement). PK. BAL protein (vascular leak). Blinded histopathology. Weight and survival. Viral titre. Dosing at day −1, +1 and +3. | Influenza A mouse model plus one SARS-CoV-2 or RSV model. Species set by G0 cross-reactivity (human-IL33 knock-in or a matched surrogate antibody). About 12–15 per group, repeated once. | 4–9 | Early-treatment arm: ≥ 30 % fall in leak or injury score in ≥ 1 model. Target engagement ≥ 90 %. No rise in viral titre. | No effect when dosed after infection in two models → stop. |
| **A3** | Does it apply to other viruses, and what is the treatment window? | IL-33 (serum and nasal fluid/BAL), sST2 and the PD panel at day 0, 1, 3, 7 | Hospitalised influenza, RSV and SARS-CoV-2 adults (biobanks first); about 200 per virus for 80 % power at per-SD OR 1.8 | 2–9 (interim) | Association replicated in ≥ 1 non-COVID virus. Kinetics define the dosing window. | COVID-only → narrow the indication before any trial. |

**Decision points.**
- **Gate 1 (month 5):** G0 + A1 + B1 must all pass.
- **Gate 2 (month 9):** clinical-entry decision, requiring A2/A3 interim + B2–B4 + C1.
- **Before Gate 1:** no GLP toxicology and no GMP manufacture. At-risk work on a research cell bank is reasonable only after G0.

---

## 7. What goes into the clinic, if Gate 2 passes

| Element | Proposal | Basis |
|---|---|---|
| **Article** | AX-1177, identity confirmed at G0, given IV | G0 |
| **Before patients** | Cynomolgus GLP repeat-dose toxicology, tissue cross-reactivity and immunogenicity. First-in-human single ascending dose in healthy volunteers (safety, PK, anti-drug antibodies, target engagement). Indicative months 9–20. | standard *[background]* |
| **Population** | Hospitalised adults with PCR-confirmed viral LRTD, on supplemental oxygen but not ventilated. Restricted to the viruses where A3 showed IL-33 activity. Enriched for high sST2 (cut-off from A3), because sST2 is the only IL-33-axis marker that tracks outcome here (OR 3.02). | `mmc2`, A3 |
| **Design** | Phase 1b/2a: randomised, double-blind, placebo-controlled, on top of standard care. Single IV dose given within the window defined by A3/B1. | B1 delayed-addition arms, A3 kinetics |
| **Dose** | Chosen to keep free IL-33 suppressed beyond IC90 in lung lining fluid through the illness. It **cannot be set from this package**: it needs the B1 IC90 and C1/first-in-human PK. | §4.1 (41:1 ratio only) |
| **Target engagement** | Free and total (drug-bound) IL-33 in serum and, where feasible, airway fluid | C1 |
| **PD (primary mechanistic endpoint)** | Change from baseline at day 3 and day 7 in the endothelial PD composite: IL-6, CCL20, OPG, IL-18R1, IL-8, sE-selectin. All are IL-33-induced, ≥ 80 % neutralised in vitro at both timepoints, and outcome-associated in `mmc2`. | §4.2 table |
| **Safety** | Viral load over time, secondary infections, standard safety | B2/B4 |
| **Clinical (secondary)** | ICU / ventilation / death by day 30 (same composite as `mmc2`); time to recovery; oxygen-free days | `mmc2` endpoint |
| **Sampling** | Pre-dose; 6–24 h; days 3, 7, 14, 28 (plus day 60 for PK/anti-drug antibodies) | in vitro kinetics (6 h peak; partial escape at 24 h) |
| **Size** | Powered for the PD composite. The SD will be taken from A3, since the package has no variance data for it. Not powered for clinical outcomes. | — |

**Kill criteria** (any one stops the LRTD indication):
- AX-1177 ≠ Compound_47, or IC90 is not reachable at feasible doses.
- No IL-33 measure tracks outcome (A1) and none is raised in airway fluid (A3).
- Activity only when the antibody is given first (B1).
- Viral titre rises by more than 0.5 log₁₀, or antiviral effector function is impaired (B2/B4).
- No effect when dosed after infection in two in vivo models (C1).

**What could speed things up:** if IL-33 turns out to be among the 100 undelivered assays and shows a positive association, or if the biologics file already holds potency, cross-reactivity or in vivo data, A1 and parts of G0 and C1 could close within weeks.

---

## Appendix: how this review was done, and its limits

- **Pipeline.** `analysis/run_all.sh` runs 01–09 plus `sim_voom_pooled_model.R`, using the `singlecell` (Python) and `renv` (R: limma/edgeR) environments. Annotation comes from offline org.Hs.eg.db 3.18 and MSigDB Hallmark (msigdbr 7.5.1).
- **RNA-seq checks.** The limma output is internally consistent: identical AveExpr across all 26 contrasts (one fit); total df 85.13 (76 residual + prior); within-contrast BH reproduced to 5 × 10⁻¹⁵.
- **Derived contrasts** (e.g. IL-33+Compound_47 vs vehicle) are logFC arithmetic on that single fit. They are point estimates without SEs.
- **Neutralisation estimate.** Percent neutralised = −Σ(Compound_47 vs isotype) / Σ(IL-33 vs vehicle) over the core genes. The two contrasts share no libraries. Selecting genes with large IL-33 effects biases this estimate *downward*, so it is conservative. The CIs come from resampling genes, so they describe the gene set, not replicate-level uncertainty. Replicate-level data were not delivered.
- **Serum.** Olink names were mapped to HGNC symbols (`olink_symbol_map.py`; 15 mapped through aliases, listed in the log). Duplicates were collapsed to 1,063 proteins and BH re-run. The "per-SD OR" values are approximations, exp(z/√(n·p·(1−p))), and conservative.
- **IHC.** Donor-level Mann–Whitney, HL shifts with bootstrap CIs, Cliff's δ; block-level results are shown only to illustrate pseudo-replication.
- **Limits.**
  - The SE flag (max SE > 5 or min SE < 0.005 log2 units) is a heuristic, backed by the data range (AveExpr −5.1 to 13.5) and the simulation.
  - The event count (44) is inferred.
  - I had no raw counts, patient-level serum data or images, so all inference is from summary statistics.
