# AX-1177 (anti-IL-33 IgG1): Portfolio audit position paper

**Question from the committee:** Should AX-1177 stay in the respiratory portfolio? What do our data support, what would we drop, and what comes next?

**Evidence base:** only the five delivered AX-1177 files:
- methods annex
- HUVEC IL-33 RNA-seq
- RNA-seq contrasts
- serum proteomics (n = 100 hospitalised SARS-CoV-2 patients)
- post-mortem lung (31 donors, 74 blocks)

Every number below was recomputed from those files. The figures, tables and scripts are listed in Section 8. Where a statement depends on anything other than our data, it is flagged as such.

---

## 0. Decision on one page

> **Recommendation: KEEP AX-1177, as a re-scoped, gated asset. Do not progress it in "severe lower respiratory viral infection" on the current evidence.**
>
> Hold AX-1177 at the preclinical stage for one ~6-month translational gate. Most of that work runs on material we already own. Fix the go/kill criteria now (Section 6.2). If the gate fails, drop the asset; the drop statement is in Section 6.5.

**Why keep. What our data support:**

1. **The molecule works and is clean.** In human umbilical-vein endothelial cells (HUVEC), AX-1177 reverses the reduced-IL-33 transcriptional response essentially completely at 6 h:
   - slope −0.98 across the 645 IL-33-induced genes, with a median reversal of 95%;
   - median residual effect 0% among expressed genes with valid statistics;
   - the antibody was added at the same time as IL-33, with no pre-incubation;
   - the isotype control leaves 99% of the response intact;
   - AX-1177 alone does nothing transcriptionally in four human cell types (slope ≈ 0 on the IL-33 program; 0–6 scattered genes per contrast).
2. **The pathway has a patient signal.** Soluble ST2 (sST2; the IL-33 receptor/decoy) is the #2 of 1,063 unique serum proteins associated with ICU, invasive ventilation or death within 30 days:
   - OR 3.02 per log unit (95% CI 1.83–5.01), p = 1.7×10⁻⁵, protein-level q = 0.009;
   - independent of age, sex and NEWS2;
   - no missing values in either outcome group.
3. **The biology AX-1177 blocks overlaps with patient biology at specific, measurable nodes.** Several proteins are all three of: induced by IL-33 in HUVEC with valid statistics, reversed by AX-1177, and prognostic in patients (q < 0.05). The most interpretable secreted mediators among them are IL-6, CCL20, MCP-3/CCL7, OPG, IL-18R1, CSF-1, IL-1β and tissue factor. That is a ready-made pharmacodynamic panel.
4. **The decisive missing evidence is cheap and largely in-house.** Three things already exist:
   - IL-33 itself was very probably on the serum run but was not delivered;
   - 22 lung RNA samples are banked against the post-mortem blocks;
   - the count matrices and model object are archived.

   Dropping now would mean deciding on data we have not yet looked at.

**Why not progress now. What our data do not support:**

1. **Nothing in our data shows IL-33 is elevated or released in severe viral pneumonia.**
   - IL-33 is absent from the serum delivery.
   - Lung IL-33 immunostaining is no higher in COVID+ than in COVID− pneumonia or non-pneumonia lungs (Kruskal–Wallis p = 0.11–0.65).
   - Endothelial IL-33 is at the scale ceiling in 39 of 74 blocks.
2. **The severity signature is broad and not IL-33-specific.**
   - 193 proteins reach q < 0.05, and 98% of nominal hits point the same way.
   - sST2 travels with other shed IL-1-family receptors (IL-18R1 #20, IL-1R2 #23).
   - The AX-1177-reversible endothelial secretome is not enriched among severity markers (Fisher OR 1.11, p = 0.70).
3. **Nothing is virus-specific, and only one virus was studied.**
   - Granulocyte infiltration is the same in COVID+ and COVID− pneumonia (p = 0.37–0.87, batch-matched).
   - All patient data are SARS-CoV-2, pre-vaccination and single-centre. The label "severe LRVI" is wider than the evidence.
4. **Differentiation, potency and therapeutic window are unproven.**
   - Only reduced IL-33 was tested, and only on endothelium. The "binds oxidised IL-33" claim has no functional data.
   - One antibody concentration was used, at ~41-fold molar excess. The annex states that potency data are held in the biologics file, outside this dataset.
   - Blockade falls from ~100% at 6 h to ~82% at 24 h, with interferon-stimulated genes escaping. In HGMEC the blocking slope falls from −0.64 to −0.29.
5. **All three datasets have quality defects that limit what can be claimed** (Section 4).
   - In the RNA-seq, the p-values for ~130 genes are unusable, including E-selectin, VCAM-1, IL-8, CXCL1 and ST2 itself.
   - In the post-mortem set, category labels contradict the autopsy text for 8 of 31 donors (9 counting a borderline case).
   - MBP and 2D7 staining is batch-confounded.

**Where the data point.** Toward a **host-response-defined severe pneumonia indication**: hospitalised patients with a high-sST2, neutrophilic/endothelial-activation phenotype, regardless of pathogen. This is an evolution of the current indication, not a new therapeutic area. The data do **not** point to:
- asthma/COPD;
- a type-2/eosinophilic population;
- kidney, cardiac or oncology indications.

**The gate in one sentence.** Using our own sera and banked lung RNA, show that IL-33 is released and free, and that it tracks outcome beyond NEWS2 and sST2. Replicate the sST2 signal outside SARS-CoV-2. Prove AX-1177 still neutralises when added late.

**Biomarkers and timepoint in one sentence.** Serum sST2 at enrolment (pre-dose, within 24 h of admission) enters patients now as a prognostic enrichment/stratification marker. Free and total IL-33 plus the IL-33:sST2 complex become the target-engagement markers once assays exist. An IL-33-reversible panel (IL-6, CCL20, CCL7, OPG, IL-18R1, CSF-1, IL-1β, tissue factor), sampled at 24 h post-dose, serves as exploratory PD. Type-2 markers and tissue IL-33 staining are not used (Section 5).

---

## 1. What the dataset can and cannot answer

| File | What it contains | What it can answer | Design limits that matter |
|---|---|---|---|
| Methods annex | Articles, cells, design, analysis settings | How results were produced | Potency/affinity held elsewhere; count data and model object archived, not delivered |
| `rnaseq_huvec_il33` | IL-33(red) vs vehicle, HUVEC, 6 h and 24 h | Does IL-33 activate endothelium, and how? | Single donor (P2), n = 3 wells per arm; reference labelled "Vehicle" in the sheet name but "Nontreated" in the data |
| `rnaseq_contrasts` | 24 contrasts: AX-1177 vs isotype ± IL-33 (HUVEC, HGMEC); AX-1177 vs isotype/PBS/DMSO (A549, MCF7) | Does AX-1177 block IL-33? Does it do anything on its own? | No HGMEC vehicle arm; epithelial lines never received IL-33; reduced IL-33 only; one antibody concentration; concurrent addition only |
| `serum_proteomics` | 1,094 Olink assays (13 panels) vs composite endpoint (ICU/IMV/death ≤ 30 d), adjusted for age, sex, NEWS2 | Which circulating proteins carry prognostic information in hospitalised COVID-19? | Summary statistics only; one timepoint; pre-vaccination, single centre; IL-33 itself not delivered |
| `postmortem_lung` | IHC (0–5) for IL-33 in three compartments, plus eosinophil, neutrophil and mast-cell markers | Is IL-33 or granulocyte infiltration different in COVID+ lung? | Elderly end-stage donors (mean age 81–84); single reader; no healthy controls; labels, batch and ceiling problems |

Not in the dataset at all:
- in vivo efficacy, PK or safety;
- non-SARS-CoV-2 infections;
- primary lung cells;
- oxidised IL-33;
- IL-33 levels in any patient fluid.

---

## 2. Evidence, dataset by dataset

### 2.1 In vitro pharmacology (RNA-seq, Figure 1)

**IL-33 activates endothelium through an inflammatory, neutrophil-recruiting and procoagulant program, not a type-2 program.**
- Reduced IL-33 (30 ng/mL) induced 645 genes in HUVEC at 6 h and 314 at 24 h (FDR < 0.05, log2FC > 1). It repressed 423 and 198.
- The induced program is dominated by:
  - neutrophil chemokines: CXCL2 (+6.8 log2), CXCL3, CXCL5, CXCL6 (+9.4);
  - GM-CSF (CSF2, +10.3) and G-CSF (CSF3, +8.3);
  - CCL20 (+9.2), CX3CL1 (+8.4);
  - IL-6 (+5.8), IL-1α/β and TNF (+7.9 at 6 h, back to baseline at 24 h);
  - NF-κB feedback genes (NFKBIA, TNFAIP3, TRAF1, BIRC3);
  - procoagulant genes: tissue factor (F3, +5.6) and PAI-1 (SERPINE1, +1.7).
- Canonical adhesion molecules and IL-8 show very large effects. E-selectin (+11.2), VCAM-1 (+8.7) and IL-8 (+8.2) have unusable statistics (Section 4). ICAM-1 (+6.0) reaches q = 0.01 despite an inflated standard error.
- There is no type-2 output. IL-5, IL-13 and eotaxin-1/-2 are not expressed in any arm (removed by the low-expression filter). IL-4, eotaxin-3 and TSLP are unchanged.
- The response peaks early: the 6 h response is about twice the size of the 24 h response.

**AX-1177 neutralises it, specifically, without pre-incubation.**

| Readout (HUVEC) | 6 h | 24 h |
|---|---|---|
| Slope of AX-1177+IL-33 vs isotype+IL-33 on the IL-33 effect (−1 = complete block) | −0.98 | −0.75 |
| Median reversal of IL-33-induced genes (vs isotype+IL-33 / vs IL-33 alone) | 95% / 98% | 73% / 84% |
| Median residual IL-33 effect under AX-1177 (expressed genes with valid SE; n = 299 / 124) | 0% | 18% |
| Median IL-33 effect retained with isotype control | 99% | 84% |
| AX-1177 alone vs isotype on the IL-33 program, four cell types | slopes −0.03 to +0.02 | slopes −0.03 to +0.03 |

- **Residual at 24 h.** What escapes is enriched for interferon-stimulated genes (IFIT1/2/3, OASL, RSAD2). This is consistent with secondary signalling that ligand neutralisation cannot reverse once started. The practical implication is that the antibody must be on board early.
- **HGMEC (glomerular microvascular endothelium).** The AX-1177 contrast reverses the HUVEC IL-33 program with slope −0.64 at 6 h and −0.29 at 24 h. Large reversals are seen for VCAM-1, E-selectin, BIRC3, CSF2 and CXCL1–3. Because HGMEC had no vehicle arm, we cannot tell whether this reflects a weaker IL-33 response or incomplete or short-lived blockade.
- **No off-target transcriptional signal.** AX-1177 alone produces 0–6 credible DE genes per contrast (AveExpr > 1, |log2FC| > 0.58, FDR < 0.05). They are scattered and not reproduced across timepoints. The remaining "significant" hits have biologically trivial effects (log2FC 0.06–0.19) with implausibly precise statistics (Section 4).
- **Stoichiometry.** 10 µg/mL AX-1177 ≈ 68.5 nM IgG, against 1.66 nM IL-33 (~41-fold molar excess, ~83-fold in binding sites). The blockade therefore demonstrates efficacy, not potency.

### 2.2 Clinical serum proteomics (Figure 2)

**Cohort.** 100 hospitalised PCR-confirmed SARS-CoV-2 patients; 44 had the composite event and 56 did not. Serum was drawn at enrolment. One logistic model was fitted per assay, adjusted for age, sex and NEWS2.

**Protein-level analysis.** 27 proteins are measured on 2–4 panels (58 assays). We collapsed these to 1,063 unique proteins (mean Wald z) and re-ran BH.
- Replicate assays agree closely (IL-6 ×4: ORs 2.07–2.31; HGF ×2: 4.99 and 4.84), which is reassuring on assay quality.
- The raw list over-counts hits: IL-6 alone occupies 4 of the top 28 assay slots.

**Key findings.**

| Finding | Numbers |
|---|---|
| sST2 (IL1RL1) is a leading independent prognostic marker | #2 of 1,063; OR 3.02 (1.83–5.01) per log unit; p = 1.7×10⁻⁵; q = 0.009; no missing values |
| …but it moves with other shed IL-1-family receptors | IL-18R1 #20 (OR 6.07), IL-1R2 #23 (OR 4.52), IL-1Ra (p = 0.019) |
| The severity signature is broad | 193 proteins at q < 0.05; 98% of the 384 nominal hits have OR > 1. Top ranks mix cytokines (HGF #1, IL-6, OSM), tissue injury (PTX3) and intracellular "leakage" proteins (NPM1, CALR, GSTP1, PRDX1/6) |
| Neutrophil and myeloid activation is prominent | PRTN3, CD177, IL-8, S100A12, LCN2 (q 0.02–0.03) |
| Endothelial injury is modest | VEGF-A, vWF, tissue factor, ANGPT2 (q ≈ 0.035–0.05); E-selectin, t-PA, PAI-1 nominal; VCAM-1, ICAM-1, PECAM-1, TIE2, ESM-1 null |
| The type-2 axis is flat | IL-5 OR 1.00 (p = 0.997; rank 1,060 of 1,063); eotaxin-1 (×2), eotaxin-2, TARC, tryptase, CD23, IL-17RB null; IL-5Rα 1.61 (p = 0.059); ECP 1.50 (q = 0.058) |
| Kidney and cardiac signals are weak | KIM-1 nominal, cystatin C null; troponin I null, NT-proBNP weak; GDF-15 (non-specific stress) q = 0.02 |
| The target ligand is missing | IL-33, IL-4, IL-13 and TSLP are absent from the Inflammation panel delivery (77 of the panel's 92 assays are present). That panel normally carries IL-33; this is external knowledge of Olink content. |

**Caveat on effect sizes.** ORs are "per log unit" on assay-specific scales, so they are not comparable across proteins. For example, CSF-1 has OR 90 and GSTP1 OR 25 because their distributions are narrow, not because they are better markers. This paper therefore ranks by p/z throughout.

### 2.3 Post-mortem lung (Figure 3)

The analysis is at **donor level (n = 31)**, not block level (n = 74), because three donors supply 24 blocks. Scores are treated as ordinal.

- **IL-33 does not discriminate disease.** Donor medians for COVID+ pneumonia / COVID− pneumonia / non-pneumonia:

  | Compartment | COVID+ pneumonia | COVID− pneumonia | Non-pneumonia | Kruskal–Wallis p |
  |---|---|---|---|---|
  | Epithelium | 4.25 | 4.50 | 4.88 | 0.65 |
  | Endothelium | 4.81 | 5.50 | 5.50 | 0.11 |
  | Vascular smooth muscle | 2.38 | 3.25 | 3.50 | 0.16 |

  - Endothelial IL-33 sits at the ceiling in 53% of blocks.
  - Donor 2067 has identical epithelial and endothelial IL-33 scores in all 8 blocks across two lobes.
- **Endothelial IL-33 staining is lower where granulocytes are present.** It correlates negatively with H&E eosinophils (ρ = −0.51, p = 0.004) and neutrophil elastase (ρ = −0.43, p = 0.016).
  - This is compatible with IL-33 release from injured endothelium.
  - It is equally compatible with down-regulation on activation.
  - IHC cannot tell the two apart, so we treat this as a *hypothesis* and not as evidence for the target.
- **Granulocytes track pneumonia, not the virus.** In the batch-matched series (B1: 4 COVID+, 5 COVID− pneumonia, 5 non-pneumonia):
  - neutrophil elastase, IL-5Rα⁺ cells and H&E eosinophils are higher in pneumonia than non-pneumonia (p = 0.003–0.004);
  - they are identical between COVID+ and COVID− pneumonia (p = 0.37–0.87);
  - re-classifying donors by their actual autopsy findings gives the same result for these three markers (p = 0.002–0.02).
- **Eosinophil granule proteins (EDN, MBP) do not track pneumonia.** Their apparent association with the "pneumonia" labels disappears once donors are classified by autopsy findings. MBP tracks staining batch instead (Section 4).
- **The only SARS-CoV-2-specific pathology is diffuse alveolar damage (DAD):** 7 of 16 COVID+ donors vs 0 of 15 COVID− (p = 0.007). Within COVID+, IL-33 does not differ by DAD. Thromboemboli appear in 4 of 16 COVID+ vs 0 of 15 (p = 0.10).
- **No link to chronic airway disease.** IL-33 and eosinophil scores do not differ by recorded COPD/emphysema (n = 18 vs 13) or asthma (6 vs 25); all p > 0.13.

### 2.4 Does the mechanism map onto patients? (integration)

We matched 914 Olink proteins to RNA-seq genes. Of these, 110 are IL-33-induced in HUVEC and reversed ≥ 50% by AX-1177.

- **Test 1: are they over-represented among severity markers? No.**
  - 21% vs 19% reach q < 0.05 (Fisher OR 1.11, p = 0.70).
  - Their median association z is 1.36 vs 1.43 (Mann–Whitney p = 0.64).
  - Several of the most strongly IL-33-induced endothelial products have no prognostic value at all: CXCL6 (p = 0.95), G-CSF (p = 0.23), CXCL5, CX3CL1, TNFRSF9, CXCL10.
- **Test 2: which individual nodes overlap? These are the PD candidates.**
  - Valid in vitro statistics and prognostic at q < 0.05: IL-6, CCL20, CCL7, OPG (TNFRSF11B), IL-18R1, CSF-1, IL-1β, tissue factor. CTSS, IL-15 and a few intracellular proteins also qualify (Table S2).
  - Prognostic, but the in vitro statistics are unusable, so they are pending re-analysis: sST2 (IL-33 induces IL1RL1 +1.6 log2, reversed by AX-1177), PTX3, IL-8, MCP-1, E-selectin.

**Bottom line of the integration.** The mechanism is *compatible* with patient biology at the level of IL-6, neutrophil-recruiting and procoagulant endothelium. However, the patient severity signature is not *driven selectively* by the IL-33 program. That is exactly the gap the next studies must close.

---

## 3. The position for the committee

### 3.1 Claims we can defend, and claims we must not make

| We can say | Strength | We must not say |
|---|---|---|
| AX-1177 specifically neutralises reduced-IL-33 signalling in human endothelial cells, even without pre-incubation | Strong in vitro (one donor, one concentration) | "AX-1177 is potent" (no dose–response in this dataset) |
| AX-1177 has no detectable off-target transcriptional activity in 4 human cell types | Moderate–strong (transcript level, 6/24 h) | "AX-1177 is safe" |
| sST2, the IL-33 receptor/decoy, is among the strongest independent prognostic markers of severe outcome in hospitalised COVID-19 | Strong within cohort (needs replication) | "sST2 predicts response to AX-1177"; "IL-33 drives severe COVID" |
| IL-33 activates a neutrophil-recruiting, IL-6-high, procoagulant endothelial program, and several of its products are prognostic in patients | Moderate | "The patient severity signature is an IL-33 signature" (not enriched) |
| IL-33 protein is abundant in human lung epithelium and endothelium | Moderate (semi-quantitative IHC) | "IL-33 is up-regulated/released in COVID lung" (not shown) |
| — | — | "Our data support viral LRTI beyond SARS-CoV-2"; "AX-1177 is differentiated by neutralising oxidised IL-33" (binding claim only); "severe COVID is eosinophilic/type-2" |

### 3.2 Challenges to expect, and answers grounded in our data

- **"sST2 is a generic injury marker. Why is it IL-33 evidence at all?"**
  Agreed: it co-moves with IL-1R2 and IL-18R1. It is pathway-*linked* prognostic evidence, not proof of pathway *activity*. Because sST2 is a decoy, high sST2 could even mean IL-33 is already buffered. This is exactly why the gate measures free IL-33 and the IL-33:sST2 complex.
- **"IL-33 isn't up in the lungs. Why keep?"**
  IHC is the wrong instrument to detect release. It saturates in 53% of endothelial blocks, and loss of nuclear IL-33 can mean release or down-regulation. Endothelial IL-33 is actually *lowest* in the most inflamed lungs. Release has to be measured in fluid.
- **"Pivot to COPD/asthma, where anti-IL-33 has precedent?"**
  Nothing in our data supports that: no epithelial IL-33 experiments, a null serum type-2 axis, and no association of tissue IL-33 or eosinophils with COPD/asthma history. It would be a bet on external precedent that needs a new data package, not a data-driven repositioning.
- **"Is the blockade an artefact of a large antibody excess?"**
  Partly a fair point: potency is not established, and dose–response is a gate item. But concurrent addition with no pre-incubation is the *harder* test, and blockade was complete at 6 h.
- **"Can we trust the RNA-seq?"**
  The conclusions rest on effect sizes restricted to genes with valid standard errors. In that subset the blockade holds (median residual 0% at 6 h). The defects invalidate p-values for ~130 genes and are fixed by re-fitting from the archived counts (Gate A).
- **"Any safety signal?"**
  AX-1177 alone is inert. In HUVEC, IL-33 also induces interferon-stimulated genes and AREG. Blocking IL-33 during infection could blunt these, so Phase 1b must monitor viral clearance. This is a hypothesis, not an observed liability.
- **"Is a pre-vaccination COVID cohort still relevant?"**
  Only as a host-response discovery set. That is why replication in a contemporary, non-SARS-CoV-2 cohort is a go criterion.

---

## 4. Data-integrity log (Figure 4)

| # | Dataset | Finding | Impact on conclusions | Remediation |
|---|---|---|---|---|
| 1 | RNA-seq | One limma-voom fit across four biologically distinct cell types, with variance pooled. Implied SEs (\|logFC/t\|) span ~8 orders of magnitude. **130 genes** have median SE > 2 log2 units, which is impossible for log-CPM data. These include E-selectin, VCAM-1, IL-8, CXCL1, MCP-1, PTGS2, PTX3, ST2 (IL1RL1), CD93, CDH5 and vWF. 267 gene×contrast cells have SE < 0.02. The same gene (AKR1C2) varies 225,000-fold in SE across contrasts. | P-values for the canonical endothelial-activation genes and the receptor are unusable. Headline DE counts are unreliable. This analysis uses effect sizes with an SE-validity filter. | Re-fit per cell line from archived counts (annex §5). Report CIs. |
| 2 | RNA-seq | The contrasts workbook sheets "6h" and "24h" are identical duplicates, each holding all 24 contrasts (both timepoints). The "6h" sheet is formatted to Excel's 1,048,576-row limit, but rows beyond 629,041 are empty (verified in the XML). | No data loss; the sheet names are misleading. | Re-issue with correct sheet names. |
| 3 | RNA-seq design | No HGMEC vehicle arm. Epithelial lines never given IL-33. DMSO vehicle is irrelevant to an antibody. Single donors for primary cells. One antibody concentration. Reduced IL-33 only. Concurrent addition only. | HGMEC response cannot be sized. No epithelial or oxidised-IL-33 biology. No potency or therapeutic window. | Gate B in vitro package. |
| 4 | RNA-seq annotation | 8,550 genes lack Entrez IDs, including CXCL8/IL-8. 97 duplicate symbols. "Vehicle" vs "Nontreated" naming mismatch. | Entrez-keyed pathway tools would silently drop IL-8. | Annotate by Ensembl ID. |
| 5 | Serum | 27 proteins measured on 2–4 panels (58 assays) are counted as independent tests. | Hit counts inflated. | Collapsed to 1,063 proteins (done). |
| 6 | Serum | Delivered adj. p-values are 4–9% higher than BH computed over the delivered assays. This implies ~1,160–1,190 tests, i.e. **~70–100 assays were tested but not delivered**. IL-33, IL-4, IL-13 and TSLP are absent. | The target ligand is missing. Provenance gap. | Request the full assay list, LOD/QC report and patient-level NPX. |
| 7 | Serum | ORs are "per log unit" on assay-specific scales. NPX is already log2, so the transform needs clarifying. | OR magnitudes are not comparable across proteins. | Request per-SD ORs, AUCs and incremental value over NEWS2. |
| 8 | Serum | Single centre, pre-vaccination, single timepoint, no validation cohort, standard of care unknown. | Generalisability. | Replication cohort (Gate B3). |
| 9 | Post-mortem | Category labels contradict the autopsy text for **8 of 31 donors**: 4 "COVID− pneumonia" donors with no pneumonia recorded (1905, 1961, 1968, 1970); 2 "non-pneumonia" controls with acute pneumonia/pneumonitis (1956, 1976) and 1 with pulmonary coccidioidomycosis (1944); 1 COVID+ donor with no acute lung pathology (2067, 8 blocks). In addition, 2101 shows only chronic changes and 1905 has a blank SARS-CoV-2 field. | Group comparisons are contaminated. | Analysed by pathology as a sensitivity check (done). Formal re-adjudication needed. |
| 10 | Post-mortem | The numeric columns convert "n+" to n+0.5, producing 5.5 on a 0–5 scale (39/74 endothelial IL-33 blocks; 6 neutrophil-elastase blocks). IL-33 is at the ceiling. | Out-of-range values; no dynamic range for IL-33. | Treat as ordinal (done). Re-score IL-33 quantitatively (digital H-score, nuclear vs non-nuclear). |
| 11 | Post-mortem | Accession-batch effect on MBP and 2D7: COVID+ B4 vs other batches p = 0.001 / 0.004. All non-pneumonia controls are in B1. | Eosinophil-granule comparisons are confounded. | Batch-matched analysis (done). Re-stain in a single run. |
| 12 | Post-mortem | Pseudo-replication: 3 donors supply 24 of 74 blocks. Donor fields sit on the first block, but "approved lung conditions" sometimes sits on the second. | Block-level tests overstate n. | Donor-level analysis (done). |
| 13 | Post-mortem | Single reader. IL-5Rα scored on two independent duplex stains agrees well (83% exact, ρ = 0.93). IL-33 reliability is unknown. No healthy-lung controls. | Reliability only partly checkable. | Second blinded reader (weighted κ); add normal lung. |

---

## 5. Biomarkers: which go into patients, in what role, and when

| Marker | Evidence in our data | Role in patients | Readiness |
|---|---|---|---|
| **Serum sST2** | #2 of 1,063 prognostic proteins; independent of NEWS2; no missing values. IL-33 induces IL1RL1 in HUVEC, reversed by AX-1177 (statistics pending re-fit). | **Prognostic enrichment and stratification** at screening: inclusion threshold and/or stratification factor, set from patient-level data. Pre-specified test of **predictive** value (treatment × sST2 interaction) in Phase 2. Exploratory PD (Day 3–7). | Quantitative clinical sST2 immunoassays exist (external knowledge). Cut-off to be derived (Gate A2). |
| **Free IL-33, total IL-33, IL-33:sST2 complex** | Not in the delivery; this is the central gap. | **Target engagement** in Phase 1b (free ↓, total/drug-bound ↑). **Candidate predictive/enrichment marker** if Gate B1 shows it is prognostic. | Needs ultrasensitive assay development and qualification. Distinguish reduced vs oxidised forms if feasible. |
| **PD panel:** IL-6, CCL20, CCL7, OPG, IL-18R1, CSF-1, IL-1β, tissue factor | IL-33-induced and AX-1177-reversed in HUVEC (valid statistics), and prognostic in serum (q < 0.05) | **Exploratory proof-of-mechanism PD** in Phase 1b/2. Not for selection. Read against standard of care: steroids, and IL-6R blockade, which raises serum IL-6 (external pharmacology). | Olink is research-grade; move to quantitative assays. |
| PTX3, IL-8, MCP-1, E-selectin | Prognostic; IL-33-inducible by effect size, but in vitro statistics invalid | Add to the PD panel only after the RNA-seq re-fit confirms them | Pending Gate A1 |
| HGF, OSM, GDF-15, PRTN3/CD177, LCN2, KRT19/SCGB3A2 | Prognostic but not IL-33-linked in vitro (e.g. HGF #1, no HUVEC response) | Baseline covariates and severity monitoring only. Not PD. | Research-grade |
| Not for use in patients: type-2 serum markers (IL-5, eotaxins, TARC, tryptase, CD23); tissue IL-33 IHC; MBP/2D7 | Null (type-2), ceiling/ambiguous (IHC), or batch-confounded (MBP/2D7). Blood eosinophil counts were not collected, so they are untested rather than ruled out. | None | — |

**Sampling timepoint to lock: enrolment, before first dose, ideally within 24 h of hospital admission.**
1. It is the only timepoint at which our data show prognostic value (sST2 and the PD panel were measured at enrolment).
2. IL-33 biology is front-loaded. In vitro, the endothelial program at 6 h is twice the 24 h program, and TNF is back to baseline by 24 h.
3. So is the drug effect. Added together with IL-33, AX-1177 blocks completely at 6 h but only ~82% at 24 h, with interferon-gene escape. Later exposure is untested (Gate B4).

The enrolment sample therefore serves as both the enrichment sample and the PD baseline. The dosing decision should be made from it.

**PD schedule (Phase 1b):**
- 24 h post-dose for the short-half-life secreted panel and free IL-33;
- Day 3 and Day 7 for sST2 and total IL-33 accumulation;
- outcome at Day 30, the same composite endpoint as our cohort.

---

## 6. Forward view

### 6.1 The indication our data point at

**Host-response-defined severe pneumonia (pathogen-agnostic): hospitalised patients with a high-sST2, neutrophilic, IL-6-high, endothelial-activation phenotype.**

- **Host-response-defined, not pathogen-defined.** The tissue response relevant to the mechanism is identical in COVID+ and COVID− pneumonia. The one discriminating patient signal (sST2) is a host marker.
- **Endothelial, not airway.** The only mechanism demonstrated is endothelial: a neutrophil chemokine, G-/GM-CSF, IL-6 and tissue factor/PAI-1 program. It matches the neutrophilic, IL-6 and procoagulant features of the patient severity signature.
- **Caveats.**
  - Our serum data are SARS-CoV-2-only, so pathogen-agnosticism is a hypothesis to test (Gate B3), not a finding.
  - Thrombo-inflammation (tissue factor/PAI-1 induction; serum tissue factor and vWF prognostic; thromboemboli in 4/16 COVID+ donors) is a mechanistic sub-hypothesis within this indication, not a standalone one.

### 6.2 What the next studies must establish, with go/kill criteria

**Gate A (months 0–2; desk work on existing data)**
- **A1.** Re-fit the RNA-seq per cell line from the archived counts. Confirm blockade, including of E-selectin, VCAM-1, ICAM-1, IL-8, CXCL1 and IL1RL1. Derive a locked "AX-1177-reversible endothelial IL-33 signature".
- **A2.** Obtain patient-level NPX, the full assay list (including undelivered IL-33) and the LOD/QC report. Compute per-SD ORs, AUC and the increment of sST2 over NEWS2 (+ IL-6). Test the specificity of sST2 against IL-1R2 and IL-18R1. Derive an sST2 cut-off.
- **A3.** Post-mortem re-adjudication:
  - reconcile labels with the autopsy text;
  - second blinded reader;
  - re-stain MBP/2D7 in one run;
  - quantitative IL-33 scoring, separating nuclear from non-nuclear staining.

**Gate B (months 1–6; translational proof of pathway activity)**
- **B1. Is IL-33 released and free in the patients we would treat?** Measure free IL-33, total IL-33 and the IL-33:sST2 complex in the 100 enrolment sera. Test their association with outcome beyond NEWS2 and sST2.
- **B2. Is the mechanism present in injured human lung?** RNA-seq the 22 banked lung RNAs (9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia; ID gaps suggest more in the archive). Score the locked signature against acute lung pathology and granulocyte scores.
- **B3. Is the patient signal pathogen-agnostic and current?** Measure sST2 (± IL-33) at admission in ≥ 1 contemporary hospitalised cohort of non-SARS-CoV-2 lower respiratory infection (influenza/RSV/hMPV; bacterial CAP).
- **B4. Does the drug work in the clinically relevant setting?**
  - time-of-addition (0, +2, +6, +24 h after IL-33 or viral infection);
  - 8-point concentration–response, with and without pre-incubation;
  - oxidised IL-33 with an epithelial readout;
  - primary lung microvascular endothelium and virus-infected primary airway epithelium (ALI) as an endogenous IL-33 source;
  - HGMEC with a vehicle arm;
  - ≥ 3 donors per primary cell type;
  - Olink on the culture supernatants, to bridge the transcript program to serum proteins.

**Go/kill criteria (proposed; ratify before the data are seen)**

GO to IND-enabling work and Phase 1b only if **all** of the following hold:
- **G1.** Free IL-33 and/or the IL-33:sST2 complex is quantifiable in ≥ 50% of enrolment sera *and* associated with the composite endpoint after adjustment for age, sex and NEWS2.
- **G2.** sST2 prognostic value replicates in ≥ 1 non-SARS-CoV-2 hospitalised cohort.
- **G3.** AX-1177 retains ≥ 50% neutralisation when added ≥ 6 h after IL-33/infection, *and* the re-fit confirms blockade.

KILL if **any** of the following occurs:
- **K1.** IL-33 activity is undetectable or non-prognostic (B1) *and* the signature is absent in injured lung (B2).
- **K2.** The therapeutic window is < 6 h.
- **K3.** sST2 fails to replicate outside SARS-CoV-2. The indication would then collapse to a shrinking COVID niche.

Modifier, not a kill: if oxidised-IL-33 function is not neutralised, remove the "dual-form" claim from the target product profile.

### 6.3 Plan after a GO

- **Phase 1b.** Hospitalised, oxygen-requiring pneumonia (any pathogen) with sST2 above the cut-off, dosed early (≤ 48 h from admission). Assess:
  - PK;
  - target engagement (free/total IL-33);
  - the PD panel at 0 h, 24 h, Day 3 and Day 7;
  - safety, including viral load and clearance.
- **Phase 2.** sST2-enriched and stratified by pathogen. Primary endpoint: ICU/IMV/death by Day 30, the composite our cohort already characterises (44% event rate unselected). Pre-specified sST2 × treatment interaction.

### 6.4 Timeline and effort

| Month | 0–2 | 1–6 | 6 | 7–18 (if GO) |
|---|---|---|---|---|
| Work | Gate A (internal re-analysis; no new wet lab) | Gate B (assays on banked sera and RNA; focused in vitro; replication-cohort access) | Committee go/kill | IND-enabling, Phase 1b |

Durations are planning estimates, not derived from our data.

### 6.5 If the committee drops AX-1177: what we are dropping and why

> We are dropping a functional, specific anti-IL-33 IgG1. It neutralises reduced-IL-33 endothelial signalling in human cells and shows no off-target transcriptional activity. We are dropping it **because our own disease data do not show that IL-33 is released or active in severe viral pneumonia**:
> - IL-33 was never measured in patient serum;
> - lung IHC shows no increase;
> - the only pathway-linked patient signal, sST2, is prognostic but non-specific and comes from a single pre-vaccination SARS-CoV-2 cohort;
> - the drug's mechanism is not selectively reflected in the patient severity signature;
> - the asset's stated differentiator (oxidised-IL-33 binding) has no functional support.
>
> The pathway has not been disproven; it has not been tested in patients. Leaving with the asset are the sST2-enriched, host-response-defined severe-pneumonia hypothesis and the PD panel defined here. Both are reusable if the asset is out-licensed.

---

## 7. Considered and ruled out

**Indications**

| Option | Verdict | Basis in our data |
|---|---|---|
| Continue "severe lower respiratory viral infection" as currently framed | **Ruled out as framed** | SARS-CoV-2-only, pre-vaccination patient data; no virus-specific tissue signal; target ligand unmeasured |
| Host-response-defined severe pneumonia (sST2-high, pathogen-agnostic) | **Retained as the forward hypothesis (gated)** | sST2 prognostic; tissue response identical across etiologies; endothelial mechanism |
| Asthma / COPD / viral-triggered exacerbations | Ruled out as data-driven | No epithelial IL-33 work; serum type-2 null; tissue IL-33/eosinophils unrelated to COPD/asthma history (all p > 0.13) |
| Eosinophilic / type-2 subset of pneumonia | Ruled out | IL-5 OR 1.00; eotaxins, TARC, tryptase null; IL-33 in vitro program not type-2; MBP batch-confounded |
| Kidney (AKI / glomerular endothelium) | Ruled out | HGMEC response unquantifiable (no vehicle) and blockade fades by 24 h; KIM-1 nominal, cystatin C null |
| Thrombo-inflammation as a standalone indication | Ruled out standalone; kept as a sub-hypothesis | Tissue factor/PAI-1 IL-33-inducible and blocked; serum tissue factor and vWF q ≈ 0.05; thromboemboli 4/16 vs 0/15 (p = 0.10) |
| Cardiac (sST2 is also a heart-failure marker) | Ruled out | Troponin I null, NT-proBNP weak |
| Oncology (A549, MCF7 were in the design) | Ruled out | No IL-33 challenge; AX-1177 inert |
| Sepsis / all-cause critical illness | Not evaluable | No data; consider only after the B3 replication |

**Biomarkers**

| Candidate | Verdict | Reason |
|---|---|---|
| Tissue IL-33 IHC for patient selection | Ruled out | Ceiling (53% of endothelial blocks at max); no disease discrimination; needs tissue |
| Type-2 serum markers (IL-5, eotaxin-1/-2, TARC, tryptase, CD23) | Ruled out | Null in serum. Blood eosinophil counts were not collected (untested). |
| MBP, 2D7 tissue scores | Ruled out | Batch effect (p = 0.001 / 0.004) |
| Highest-OR proteins (GSTP1, SEMA4C, CALR, CTSC, CSF-1) | Ruled out as leads | Scale artefact; intracellular leakage; very wide CIs |
| HGF (#1) | Covariate only | Not IL-33-responsive in vitro |
| IL-6 alone as the PD marker | Ruled out as sole marker | Confounded by steroids and IL-6R blockade; use within a panel |
| sST2 as a predictive marker | Not established | Prognostic only; no treated patients. Test prospectively. |

**Analytic interpretations**

| Interpretation | Verdict | Basis |
|---|---|---|
| The 6 h sheet was truncated at the Excel row limit | Ruled out | 419,520 empty formatted rows; both sheets identical |
| The isotype control distorts the IL-33 response | Ruled out for induced genes | 99% of the IL-33 effect retained at 6 h. The apparent effect on repressed genes fits shared-reference noise. |
| AX-1177 has agonist or off-target activity | Ruled out (transcript level) | Slopes ≈ 0; 0–6 scattered genes |
| Use block-level IHC statistics (n = 74) | Ruled out | Pseudo-replication |
| Eosinophilia is COVID-specific | Ruled out | COVID+ ≈ COVID− pneumonia |
| Lower endothelial IL-33 staining proves release | Not accepted | Cannot be distinguished from down-regulation |
| Take delivered DE/FDR counts at face value | Ruled out | Invalid SEs; duplicate proteins; undelivered tests |

---

## 8. Methods summary and output files

**RNA-seq**
- Both workbooks were parsed in full. We verified that the two contrast sheets are identical and that the "6h" sheet holds no data beyond row 629,041 (streamed XML).
- BH adjustment and AveExpr were checked for internal consistency.
- Effect sizes are log2FC from the single delivered fit.
  - "IL-33-induced" = FDR < 0.05 and log2FC > 1 in IL-33 vs vehicle (HUVEC).
  - Reversal = −(AX-1177+IL-33 vs isotype+IL-33) / (IL-33 vs vehicle).
  - The isotype effect was derived from the two AX-1177 contrasts of the same model.
  - The validity filter is implied SE = \|logFC/t\| < 2 (median across contrasts).

**Serum**
- Olink assay names were mapped to gene symbols (manual dictionary for non-standard names).
- Duplicates were collapsed by mean Wald z, with BH re-run over 1,063 proteins.
- Wald consistency of OR/CI/p was verified.
- Enrichment tests used Fisher's exact test and one-sided Mann–Whitney, restricted to the 914 Olink proteins with an RNA-seq match.
- The serum columns `composite_endpoint_0/1` are multiples of 1/56 and 1/44. We read them as per-outcome-group missing (below-LOD) fractions; they are undocumented in the annex.

**Post-mortem**
- Donor-level fields were forward-filled. "n+" was converted to the ordinal n, with ND treated as missing.
- Donor means were compared with Kruskal–Wallis, Mann–Whitney and Spearman tests.
- Sensitivity analyses covered pathology-text re-classification (regex plus manual verification), batch (accession series B1–B4), and the B1-only comparison.

**Outputs**
- **Figures:** `figures/Fig1_invitro_blockade.png`, `Fig2_serum_proteomics.png`, `Fig3_postmortem.png`, `Fig4_data_integrity.png`
- **Tables:**
  - `tables/S1_invitro_IL33_program_and_AX1177_blockade.csv` (1,422 genes)
  - `S2_serum_protein_level_with_invitro_annotation.csv` (1,063 proteins)
  - `S3_postmortem_donor_level.csv` (31 donors, with batch and label-discordance notes)
  - `AX-1177_audit_tables.xlsx` (all tables, plus the integrity log, biomarker plan and ruled-out list)
- **Code:** `scripts/` (all analyses are reproducible from the five input files)
