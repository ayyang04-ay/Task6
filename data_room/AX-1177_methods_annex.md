# AX-1177 — Methods Annex

**Programme:** AX-1177 (anti-IL-33 monoclonal antibody)
**Document type:** Methods annex and dataset annotation
**Applies to:** in vitro transcriptomics dataset; clinical serum proteomics dataset
**Status:** Final

This annex records materials, experimental design, instrument settings and analysis
parameters. It records no results and no interpretation.

---

## 1. Test and control articles

| Article | Description | Format | Working concentration |
|---|---|---|---|
| Compound_47 | Anti-IL-33 monoclonal antibody, binds the reduced and oxidised forms of human IL-33 | Human IgG1 | 10 µg/mL |
| NIP228 | Non-binding isotype control antibody; no known human antigen | Human IgG1 | 10 µg/mL |
| IL-33red | Recombinant human IL-33, reduced form, mature processed species (residues 112–270) | Recombinant protein | 30 ng/mL |

Compound_47 is the research designation for AX-1177. NIP228 is the isotype
control.

Compound_47 nominal molecular weight 146 kDa. NIP228 nominal molecular weight 146 kDa.
IL-33red nominal molecular weight 18.1 kDa.

Vehicle articles: PBS and DMSO.

Affinity, potency and binding characterisation for Compound_47 are held in the
programme biologics file and are not part of this dataset.

---

## 2. Cell lines

| Label | Cell type | Vascular bed | Source | Donor | Passage used |
|---|---|---|---|---|---|
| HUVEC | Human umbilical vein endothelial cells | Macrovascular, venous | Commercial primary | Single donor | P2 |
| HGMEC | Human glomerular microvascular endothelial cells | Microvascular | Commercial primary | Single donor | P5 |
| A549 | Human lung adenocarcinoma epithelial line | n/a | ATCC CCL-185 | n/a | — |
| MCF7 | Human breast adenocarcinoma epithelial line | n/a | ATCC HTB-22 | n/a | — |

Endothelial lines were maintained in endothelial growth medium with supplements and
2% FBS. A549 and MCF7 were maintained in DMEM with 10% FBS. All lines were confirmed
mycoplasma negative prior to plating. Cells were plated to 80–90% confluence and
serum-reduced for 4 h before treatment.

---

## 3. Experimental design

Cells were treated for 6 h or 24 h. All arms were plated and harvested in parallel
within each cell line and timepoint.

**Arms, endothelial lines:**

| Arm | IL-33red | Antibody | Lines |
|---|---|---|---|
| Vehicle | — | — | HUVEC |
| NIP228 | — | NIP228 | HUVEC, HGMEC |
| Compound_47 | — | Compound_47 | HUVEC, HGMEC |
| IL-33red | 30 ng/mL | — | HUVEC, HGMEC |
| IL-33red + NIP228 | 30 ng/mL | NIP228 | HUVEC, HGMEC |
| IL-33red + Compound_47 | 30 ng/mL | Compound_47 | HUVEC, HGMEC |

**Arms, epithelial lines (A549, MCF7):**

| Arm | IL-33red | Antibody |
|---|---|---|
| PBS | — | — |
| DMSO | — | — |
| NIP228 | — | NIP228 |
| Compound_47 | — | Compound_47 |

**Replication:** n = 3 biological replicates per arm per timepoint.

**Total samples:** 38 arm × timepoint groups, 114 libraries.

Antibody, where present, was added concurrently with IL-33red. No pre-incubation step
was used.

---

## 4. RNA extraction and sequencing

Total RNA was extracted using column-based purification with on-column DNase
treatment. RNA integrity was assessed on an Agilent TapeStation; all samples carried
forward had RIN ≥ 8.0. Libraries were prepared with ribosomal RNA depletion. Sequencing was
performed on an Illumina NovaSeq 6000, paired-end 2 × 100 bp, targeting 25 M read
pairs per library.

All 114 libraries were prepared in a single batch and sequenced across one flow cell.

---

## 5. Analysis parameters

Reads were aligned to GRCh38 and summarised to Ensembl gene identifiers. Low-expression genes were removed. Counts were
normalised and transformed with voom.

**A single linear model was fitted across the full 114-library dataset.** The design
matrix encoded cell line, timepoint and treatment arm, with one coefficient per
arm × timepoint × cell line group. Empirical Bayes moderation was applied across the
whole fit. All reported contrasts were extracted from this single fitted model.

Column definitions in the delivered tables:

| Column | Definition |
|---|---|
| `Comparison` | the contrast extracted from the fitted model |
| `ensembl` | Ensembl gene identifier |
| `logFC` | log2 fold change for the named contrast |
| `AveExpr` | average log2 expression for the gene, computed across all 114 libraries in the fit |
| `t` | moderated t statistic |
| `P.Value` | unadjusted p value |
| `adj.P.Val` | Benjamini–Hochberg adjusted p value, computed within contrast |
| `B` | log-odds of differential expression |
| `symbol`, `entrez`, `gene_name` | gene annotation |

Count matrices and the fitted model object are retained in the programme archive and
are not part of this delivery.

---

## 6. Clinical serum proteomics

**Cohort:** 100 patients hospitalised with PCR-confirmed SARS-CoV-2 infection,
single-centre, pre-vaccination period. Serum collected by venesection at enrolment,
clotted, separated by centrifugation, stored at −80 °C.

**Composite endpoint:** admission to intensive care, requirement for invasive
mechanical ventilation, or death within 30 days of hospitalisation. Recorded as a
binary variable.

**Assay:** Olink Target 96 proximity extension assay. Panels run:

Inflammation (v.3022), Cardiovascular II (v.5006), Cardiovascular III (v.6114),
Cardiometabolic (v.3603), Cell Regulation (v.3703), Development (v.3521),
Immune Response (v.3203), Metabolism (v.3403), Neuro Exploratory (v.3911),
Neurology (v.8013), Oncology II (v.7004), Oncology III (v.4001),
Organ Damage (v.3311).

Each panel reports its own assay set. Assay identifiers are panel-specific and are
reported as delivered by the vendor without renaming or reconciliation across panels.

**Model:** logistic regression of the composite endpoint on each assay, one assay per
model. Biomarker values were log transformed. Models were adjusted for age, sex and
National Early Warning Score 2 at enrolment. Odds ratios are reported per log unit
with 95% confidence intervals. Benjamini–Hochberg adjustment was applied across all
assays in the delivery.

---

## 7. Post-mortem lung tissue

Tissue was obtained from a longitudinal clinicopathological donation programme. Donors
consented to autopsy and post-mortem tissue donation. Diagnostic examination, including
gross and microscopic assessment, was performed by medically licensed pathologists
under standardised protocols. SARS-CoV-2 status was determined by licensed laboratories
under Emergency Use Authorization protocols.

Multiple histology blocks were taken per donor, sampled from different lobes where
available. Each delivered row corresponds to one histology block. Donor-level fields
are recorded against the first block for that donor.

Immunohistochemistry was scored semi-quantitatively on a 0–5 scale (0, no expression;
5, high expression) by a single reader. Scores were recorded separately for bronchial
and bronchiolar basal epithelium, endothelium, and vascular smooth muscle. Eosinophil,
neutrophil and mast cell panels were scored on the same scale on serial or duplex
sections as indicated in the column headers.

---

## 8. Delivered files

| File | Contents |
|---|---|
| `mmc2.xlsx` | per-assay odds ratios, confidence intervals, p values and adjusted p values against the composite endpoint |
| `mmc3.xlsx` | per-block donor demographics, pathology text, SARS-CoV-2 status and immunohistochemistry scores |
| `mmc4.xlsx` | contrast output, IL-33red versus vehicle in HUVEC, both timepoints |
| `mmc5.xlsx` | contrast output, all remaining contrasts extracted from the fitted model |

---

*End of annex.*
