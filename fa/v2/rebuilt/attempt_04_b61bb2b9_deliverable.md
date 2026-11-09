# AX-1177 (anti-IL-33 IgG1) — Portfolio Audit Recommendation

**Sources.** This review uses only the AX-1177 data package:

- the methods annex;
- `mmc2`: serum proteomics, 100 hospitalised COVID-19 patients;
- `mmc3`: post-mortem lung immunohistochemistry, 31 donors / 74 blocks;
- `mmc4`/`mmc5`: endothelial and epithelial RNA-seq, 26 contrasts.

Every number below was recomputed from those files. Supporting tables are in `AX-1177_supporting_analyses.xlsx`; figures are in `figures/`.

---

## 1. Recommendation

### Do not keep AX-1177 in the portfolio as a viral-LRTD asset

- Close the viral-LRTD programme.
- Do not commit IND-enabling spend.

**The case in one sentence:** our data prove the antibody works, but they do not show that its target matters in viral LRTD.

**Pharmacology: proven.** AX-1177 removes IL-33-driven activation of endothelial cells in vitro:

- median inhibition of IL-33-induced genes is 98% at 6 h and 87% at 24 h;
- no detectable off-target transcriptional activity.

**Link to disease: not shown, and the one well-powered test is negative.**

- IL-33 itself was never reported in patient serum.
- Lung IL-33 is not increased by SARS-CoV-2 infection.
- The proteins IL-33 induces in endothelium, and AX-1177 blocks, are no more likely to predict ICU / ventilation / death than other proteins: 17% vs 17%. The test had 95% power to detect a two-fold enrichment.

**The one supportive human signal is prognostic, not causal.**

- Soluble ST2 (sST2) is the 2nd-strongest of 1,063 serum proteins for 30-day ICU / ventilation / death.
- However, 82% of all proteins in this cohort lean the same way.
- sST2 is a decoy receptor that rises with inflammation of any cause.

**What we would be dropping.** A clean, potent anti-IL-33 antibody with validated in vitro pharmacology, tied to an indication hypothesis our own human data do not support.

**What the data point at instead.**

- Not broad viral LRTD, and nothing chronic (COPD, asthma / type-2 disease, kidney, lung fibrosis).
- The only setting with any human signal is narrower and not virus-specific: **patients hospitalised with pneumonia who show endothelial activation (high sST2 at admission), treated to prevent progression to ICU, invasive ventilation or death.** In effect, ARDS prevention.
- If the committee wants to keep an option, tie it to that setting and to the gated plan in Section 5. The first step costs nothing because the data already exist.

**Before sign-off.** The serum delivery omits 100 assays that were analysed, almost certainly including IL-33 itself (Section 4). Ask for them.

- **Pre-set trigger for revisiting:** serum IL-33 detectable in most patients and associated with the endpoint independently of NEWS2.
- Even then, that would fund the Gate-1 target-validation study, not resume development.

---

## 2. The evidence

### 2.1 Solid: AX-1177 neutralises IL-33 signalling in endothelium (Fig. 1)

**IL-33 response.** IL-33red (30 ng/mL) triggers a large, reproducible programme in HUVEC:

- 846 genes change at 6 h (560 up) and 379 at 24 h;
- the same genes change in the IL-33red + isotype-control arm.

The programme is an NF-κB / TNF-like endothelial activation, comprising:

- neutrophil chemokines (CXCL1/2/3/5/6/8);
- GM-CSF and G-CSF (CSF2 +10.3 log2, CSF3 +8.3);
- IL-6 and IL-1α/β;
- tissue factor (F3 +5.6);
- complement (C3, CFB);
- an interferon-stimulated arm.

Pathway enrichment: Hallmark TNFα–NF-κB q = 7×10⁻⁹⁸; interferon-γ response q = 1×10⁻³⁴.

**Blockade.** Compared with the isotype-control arm, AX-1177 inhibits IL-33-induced genes by:

| Time | Median inhibition | IQR | Fit |
|---|---|---|---|
| 6 h | 98% | 80–104% | slope −0.87, r = −0.92 |
| 24 h | 87% | 48–103% | — |

**Second endothelial type.** The same programme is reversed in glomerular microvascular endothelium (HGMEC):

- at 6 h: correlation with HUVEC r = 0.76, at about half the magnitude;
- at 24 h: weak (r = 0.37).

**Specificity.**

- AX-1177 alone (vs isotype, PBS or DMSO) gives 14–73 nominal differentially expressed genes per contrast across four cell lines.
- All are low-count noise or statistical artefacts, with no coherent biology and no correlation with the IL-33 programme (\|r\| ≤ 0.09).
- The isotype control reproduces the IL-33 response (ratio 1.00 at 6 h, 0.88 at 24 h).

**What this does *not* show.**

- Cells are single-donor, umbilical and glomerular endothelium, not lung.
- One antibody dose was tested, at ~41-fold molar excess (68.5 nM vs 1.66 nM IL-33).
- Only reduced IL-33 was used. The oxidised-IL-33 route is untested, although binding both forms is the antibody's differentiator.
- The antibody was added at the same time as IL-33 (no pre-incubation).
- No virus, no in vivo data.
- Interferon-stimulated genes partly escape blockade at 24 h (CXCL10 47%, RSAD2 33%, OASL 18% inhibited).

### 2.2 Missing: evidence that IL-33 drives viral LRTD

#### Serum: 100 hospitalised COVID-19 patients, 44 events (Fig. 2)

**sST2 is the strongest asset-relevant finding.** Soluble ST2 ranks #2 of 1,063 unique proteins for 30-day ICU / invasive ventilation / death, adjusted for age, sex and NEWS2:

- OR 3.02 per log unit (95% CI 1.83–5.01);
- Benjamini–Hochberg adjusted p = 0.0075;
- only HGF ranks higher.

**The backdrop is a global severity shift.**

- 82% of assays have OR > 1.
- About half of the proteome is associated with the endpoint (estimated proportion of true nulls π₀ ≈ 0.50).
- Severe patients simply have more of almost every protein, so one prognostic protein says little about a specific pathway.

**IL-33 was never reported.** Neither were TSLP, IL-4, IL-5 or IL-13.

**The decisive test is negative.** If IL-33-driven endothelial activation contributed to deterioration, the proteins IL-33 induces in endothelium (and AX-1177 blocks) should be over-represented among prognostic proteins. They are not:

- 14 of 83 (17%) vs 131 of 751 (17%);
- risk ratio 0.97 (95% CI 0.59–1.60);
- 95% power to detect a two-fold enrichment;
- within the set, the size of in vitro induction bears no relation to prognosis (ρ = 0.02).

**The most IL-33-specific outputs do not predict outcome:**

| Protein | In vitro induction (log2) | Serum OR |
|---|---|---|
| CXCL6 | +9.4 | 1.02 |
| G-CSF | +8.3 | 1.25 |
| CX3CL1 | +8.4 | 1.99 |
| TNFRSF9 | +7.1 | 1.10 |
| CXCL10 | +6.9 | 1.30 |
| CXCL5 | +5.3 | 1.17 |

All serum associations above are non-significant.

- The proteins that do overlap (IL-6, OPG, CCL20, IL-18R1) are generic NF-κB products.
- The top prognostic proteins (HGF, HDGF, SEMA4C, ANXA1, CLEC5A) are not IL-33-inducible.

#### Lung tissue: 31 donors, 74 blocks, analysed per donor (Fig. 3)

**IL-33 is abundant in every lung.** It is high in basal airway epithelium and endothelium of all donors, including uninfected ones; 39 of 74 endothelial blocks score at or above the scale maximum.

**SARS-CoV-2 infection does not increase it.**

- Epithelium: no difference (p = 0.76).
- Vessels: if anything lower in COVID+ lungs (endothelium median 4.8 vs 5.5, p = 0.05; vascular smooth muscle 2.4 vs 3.3, p = 0.07).
- The vascular difference disappears against pneumonia controls with a different infection (p = 0.34 and 0.16).
- It also disappears after adjusting for age, its strongest correlate (ρ ≈ 0.55): adjusted p = 0.17 and 0.13.
- Immunohistochemistry measures IL-33 stored in the nucleus; it cannot show release.

**IL-33 does not track other lung conditions** (COPD/emphysema, asthma, fibrosis) or eosinophil stains.

### 2.3 Why this adds up to "drop"

1. **Target presence in disease: not shown.** IL-33 was not measured in serum and is not increased in infected lung.
2. **Target activity in disease: not shown.** A well-powered test of the one mechanism we characterised is negative.
3. **The only human support is prognostic and non-specific.** sST2 sits in a cohort with a global severity shift.
4. **The human evidence comes from a single-centre, pre-vaccination SARS-CoV-2 cohort.** Nothing covers RSV, influenza or vaccinated populations, which define today's viral LRTD.
5. **The data-integrity issues (Section 4) mostly weaken the positive reading.**
   - The headline adhesion-molecule statistics cannot be verified.
   - "COVID lowers vascular IL-33" is an artefact of counting blocks instead of donors.
   - The exception is the omitted serum assays, which could cut either way; hence Gate 0.

---

## 3. Anticipated challenges and our answers

**"sST2 is the #2 predictor. Isn't that target validation?"**

- It validates sST2 as a prognostic marker, not the target.
- sST2 is a decoy receptor that rises with inflammation generally.
- It sits in a proteome where 82% of proteins lean the same way.
- A high level could mean *more* IL-33 is sequestered, not more signalling.
- Use it to select high-risk patients, not as proof of mechanism.

**"AX-1177 blocks about 98% of the IL-33 response."**

- Yes, but at ~41-fold molar excess against 30 ng/mL reduced IL-33, in single-donor umbilical and glomerular cells.
- It shows the molecule works, not that the disease needs it.

**"The lung is full of IL-33."**

- It is, in every lung, including uninfected ones, and near the scale ceiling.
- It is not increased by SARS-CoV-2, and it tracks age.

**"E-selectin, VCAM-1 and IL-8 are huge hits; that looks like severe COVID."**

- Their statistics cannot be verified: the standard errors are impossible (SELE log2FC 11.2 has p = 0.21; Fig. 4).
- The verifiable IL-33-specific outputs do not track severity.

**"Just run the trial enriched for high sST2."**

- Enrichment raises the event rate, not the chance that blocking IL-33 works.
- Without evidence of IL-33 activity in patients, the trial would test an unvalidated hypothesis.
- It would do so in a population (2020 COVID) that no longer represents viral LRTD.

**"The omitted serum assays might hide a strong IL-33 signal."**

- Possible: at least 5 omitted assays had p < 0.01. That is why retrieving them is Gate 0.
- However, every delivered assay has ≤ 9% of values below the detection limit, which implies the omitted ones were poorly detected. Any IL-33 association would be fragile.

**"Why not COPD, where anti-IL-33 is being developed elsewhere?"**

- Nothing in our data addresses COPD.
- There is no COPD cohort, and tissue IL-33 does not differ by COPD/emphysema (p = 0.14–0.91).
- A COPD case would rest entirely on external evidence.

**"Is the control design sound?"**

- The isotype control is inert on the robust programme.
- However, there is no vehicle arm for HGMEC, and the epithelial lines have no IL-33 arms.
- DMSO is used as "vehicle" for an antibody, and MCF7 (breast cancer) is irrelevant to lung.

---

## 4. Data-integrity findings the committee should know

The full log is in workbook sheet `01_data_integrity`. The material points:

### 4.1 Serum delivery is incomplete, and the annex is inaccurate

- The adjusted p-values reconstruct exactly when the multiple-testing family is 1,194 assays (exact integer ranks for 642 rows), not the 1,094 delivered.
- So 100 assays were analysed but omitted after adjustment. Of these, at least 15 had p < 0.05, at least 5 had p < 0.01, and one had p ≈ 0.0002–0.0003 (it would rank in the top 20).
- The Inflammation panel shows 77 of 92 assays. Going by the vendor's published panel content, the missing ones include IL-33, TSLP, IL-4, IL-5 and IL-13.

### 4.2 Serum results need reinterpretation

- **Duplicates:** 27 proteins are measured on 2–4 panels (IL-6 appears 4 times in the top 30).
- **OR scale is ambiguous:** Olink values are already on a log2 scale and were "log transformed" again, so ORs are "per log unit" of an unclear scale. Examples: CSF-1 OR 90, SEMA4C OR 20.9.
- **Handling:** I ranked proteins by signed z-score on 1,063 unique proteins.

### 4.3 About 0.8% of genes (216) have impossible standard errors in the RNA-seq statistics (Fig. 4)

- The implied SE reaches 16,536 log2 units, and 18 genes have SE < 0.01.
- The same values recur across contrasts, so this is a gene-level artefact of the pooled fit or the counts.
- Affected genes include SELE, VCAM1, CXCL8, CXCL1, CCL2, PTGS2, SERPINE1, PTX3, VWF and IL1RL1 (ST2).
- Their p-values are meaningless. I excluded them from significance claims (25,994 of 26,210 genes retained).
- The archived count matrices are needed to refit the model per cell line.

### 4.4 Model and file structure

- One model was fitted across all four cell types, so average expression (AveExpr) is not a per-line measure.
- The top IL-33 responders have negative AveExpr (CSF2 −3.2); filtering on AveExpr would delete the signal.
- The mmc5 sheets named "6h" and "24h" are identical, and each contains both timepoints.

### 4.5 Tissue labels and double-counting

**Labels contradict the pathology text for 7 of 31 donors.**

- 4 "pneumonia" donors have no pneumonia (1905, 1961, 1968, 1970).
- 3 "non-pneumonia" donors have lung infection: 1944 (coccidioidomycosis), 1956 (acute pneumonitis), 1976 (organising pneumonia).
- Donor 1905 has no SARS-CoV-2 result.

**Other recording issues.**

- Lung-condition notes for 2 donors (2040, 2045) sit on a non-first block, contrary to the annex.
- Scores exceed the 0–5 scale (5.5) and come from a single reader.

**Pseudo-replication.** Three donors contribute 24 of 74 blocks.

- Counting blocks as independent would report lower vascular IL-33 in COVID (p = 0.007–0.017).
- That does not hold when analysed per donor.

### 4.6 Design limits

- No vehicle arm for HGMEC; reduced IL-33 only; one antibody dose; antibody added at the same time as IL-33; single cell donors.
- Patients: n = 100, single centre, pre-vaccination.
- Treatment at the time of sampling was not recorded. The glucocorticoid-inducible decoy receptor IL-1R2 ranks #23, so steroid exposure may confound.

---

## 5. Forward view

### 5.1 What indication do our data point at?

**Patients hospitalised with pneumonia and endothelial activation, selected by high sST2 at admission; goal: prevent progression to ICU admission, invasive ventilation or death.** In effect ARDS prevention, probably not virus-specific.

Why this, and only this:

- **The mechanism AX-1177 demonstrably blocks is endothelial.** IL-33 drives neutrophil recruitment (CXCL chemokines, G-/GM-CSF), IL-6, tissue factor and complement in both large-vessel and microvascular endothelium.
- **The only human signal is in exactly this population.** sST2 at enrolment predicts 30-day ICU / ventilation / death beyond NEWS2, alongside endothelial and neutrophil injury markers (PTX3, HGF, vWF, PRTN3, CLEC5A).
- **The signal is not virus-specific.** Tissue IL-33 looks the same in COVID and non-COVID pneumonia. If IL-33 matters, it is not because of the virus, so the "viral" qualifier adds nothing.
- **Nothing in the data supports a chronic indication** (Section 6).

This is an honest description of what would be dropped, and it is also the only path back in.

### 5.2 What the next studies would have to establish (stop at the first failure)

#### Gate 0: complete the existing data (no new experiments)

- **Question:** is there evidence we have not yet seen?
- **Material:**
  - the 100 omitted Olink results and the Olink value scale;
  - the archived RNA-seq count matrices, refitted per cell line, plus the missing contrasts (IL-33 effect in HGMEC);
  - corrected tissue labels and a blinded second-reader re-score.
- **Go criterion:** serum IL-33 detectable in most patients and associated with the endpoint beyond NEWS2 → fund Gate 1 now. Otherwise, run Gate 1 only if the committee keeps the option.

#### Gate 1: target presence and activity in patients (the decisive gate)

- **Question:** do patients have IL-33 activity that AX-1177 removes, and does it track deterioration?
- **Material:**
  - **(a) Serum bioassay.** Banked enrolment sera (if aliquots remain) applied to primary lung microvascular endothelium from ≥ 3 donors. Stimulate for 6 h with and without AX-1177 vs isotype. Read the 53-gene IL-33 module derived from our data (workbook sheet 05).
  - **(b) Direct measurement.** Ultrasensitive free and total IL-33, plus IL-33:sST2 complex, in the same sera.
  - **(c) Existing lung RNA.** Measure the module in the 22 lung RNA samples that already exist (9 COVID+, 13 COVID−).
- **Go criterion (fix before unblinding):**
  - AX-1177-reversible serum activity in a meaningful share of patients, e.g. ≥ 25% of the activity reversible in ≥ 30% of patients;
  - higher in sST2-high patients;
  - associated with the endpoint;
  - IL-33 measurable and associated.
- **Kill criterion:** if both (a) and (b) are negative, terminate.

#### Gate 2: remove mechanism risk

- **Question:** is the mechanism IL-33-specific, potent at relevant concentrations, and safe in infection?
- **Material:**
  - lung microvascular endothelium and primary airway epithelium, several donors;
  - reduced and oxidised IL-33, full dose-response, and AX-1177 IC50;
  - pre-incubation vs concurrent addition of antibody;
  - comparison stimuli (TNF, IL-1β, viral mimics or supernatant from infected epithelium) to find readouts specific to IL-33;
  - interferon-stimulated genes and viral replication, with and without AX-1177.
- **Go criterion:**
  - an IL-33-specific readout set is defined;
  - potency is adequate at patient-relevant IL-33 levels;
  - no loss of antiviral control.

#### Gate 3: prospective biomarker cohort

- **Question:** can we find the patients, and when should we sample?
- **Material:** patients hospitalised with LRTD from several pathogens (COVID, influenza, RSV), in the post-vaccination era; serial samples at enrolment, 24 h, 72 h and day 7.
- **Go criterion:**
  - sST2 cut-point validated on a clinical assay, adding value over NEWS2;
  - time-course of IL-33, serum bioactivity and PD markers established;
  - timing of clinical events established.

In vivo efficacy in an IL-33-dependent lung-injury model, and IND-enabling work, come only after Gates 1–3.

### 5.3 Biomarkers: role, patient readiness and evidence

**sST2**
- **Role:** prognostic enrichment and stratification.
- **Evidence in our data:** OR 3.02 (1.83–5.01); adjusted p = 0.0075; rank 2 of 1,063; independent of NEWS2.
- **Into patients?** Yes, now, as an enrichment / stratification factor. Quantitative clinical sST2 immunoassays already exist; it needs a cut-point and validation across pathogens.
- **Limit:** not a pharmacodynamic (PD) or target-engagement marker.

**IL-6**
- **Role:** prognostic covariate; secondary, non-specific PD marker.
- **Evidence in our data:** 4 consistent assays, OR 2.1–2.3, adjusted p ≤ 0.019. IL-33-induced in vitro and ~100% reversed by AX-1177.
- **Into patients?** Yes, as a covariate or stratifier (clinical assays exist); not for patient selection.

**CCL20, OPG, IL-18R1, CSF-1 (with IL-6)**
- **Role:** exploratory PD (change vs placebo).
- **Evidence in our data:** the only proteins that are IL-33-induced, AX-1177-reversed *and* prognostic in serum (adjusted p 0.012–0.037). CCL20, IL-6 and OPG persist at 24 h.
- **Into patients?** Only as exploratory endpoints (research-use Olink).
- **Limit:** not IL-33-specific.

**Serum IL-33 bioactivity** (AX-1177-reversible endothelial module)
- **Role:** candidate predictive / mechanism marker.
- **Evidence in our data:** the 53-gene module itself is derived from our data.
- **Into patients?** Not yet; it must be built and qualified in Gate 1 on banked sera.

**Free/total IL-33; IL-33:sST2 and drug:IL-33 complexes**
- **Role:** target engagement and mechanism.
- **Evidence in our data:** not measured.
- **Into patients?** Not yet; needs an ultrasensitive assay.

**Tissue IL-33 immunohistochemistry; type-2 markers**
- **Role:** none.
- **Evidence in our data:** tissue IL-33 is constitutive, at the ceiling and age-driven; type-2 markers show no association.
- **Into patients?** No.

### 5.4 Sampling timepoint

**Enrichment: at enrolment, before dosing.** This is the only timepoint our clinical data validate; sST2 measured at enrolment predicted 30-day outcome.

**PD: before dosing and 24 h after.** In vitro, the AX-1177-reversible outputs that can be measured in serum persist at 24 h and remain blocked:

| Protein | Induction at 24 h (log2) | Inhibition |
|---|---|---|
| CCL20 | +5.6 | 102% |
| IL-6 | +2.8 | 102% |
| OPG | +2.4 | 120% |
| CXCL6 | +7.5 | — |
| G-CSF | +6.7 | — |

By contrast, the short-lived outputs have largely faded by 24 h (TNF +7.9 → −0.1; tissue factor +5.6 → +1.2; CX3CL1 +8.4 → +3.2), so they make poor PD markers. Serial samples at 72 h and day 7 in Gate 3 must confirm the kinetics in patients.

**Ex vivo bioassay: 6 h stimulation.**

- It gives the widest dynamic range: 846 robust genes at 6 h vs 379 at 24 h.
- Blockade is most complete then (98% vs 87%).
- It is the only timepoint at which the microvascular (HGMEC) response is clear.

---

## 6. What I considered and ruled out

### Indications

- **Broad viral LRTD: ruled out on current data** (Section 2).
- **COVID-19 specifically: ruled out.** There is no COVID-specific IL-33 signal against pneumonia controls with a different infection, and the cohort is pre-vaccination.
- **COPD / chronic airway disease: not supported by our data.**
  - There is no COPD cohort.
  - Tissue IL-33 does not differ with COPD/emphysema (p = 0.14–0.91), asthma or chronic airway disease.
  - This is absence of evidence, not evidence against.
- **Asthma / type-2 eosinophilic disease: ruled out on our data.**
  - Tissue IL-33 does not correlate with eosinophil stains (\|ρ\| ≤ 0.20, all p ≥ 0.28).
  - Serum eotaxin-1/-2, TARC and IL-5Rα are not prognostic (OR 0.85–1.6).
  - The type-2 cytokine assays were not delivered.
- **Kidney (glomerular endothelium): ruled out as the lead.**
  - The HGMEC response is about half the HUVEC magnitude and fades by 24 h.
  - There is no HGMEC vehicle arm and there are no kidney patients.
  - Serum KIM-1: adjusted p = 0.11.
- **Immunothrombosis: kept only as one mechanism within the pneumonia setting.**
  - IL-33 induces tissue factor and PAI-1 and lowers thrombomodulin, all reversed by AX-1177.
  - Serum tissue factor: OR 3.0 (adjusted p = 0.051).
  - Thromboemboli in 4 of 16 COVID+ donors vs 0 of 15 COVID− donors (p = 0.10).
  - Too thin to stand alone.
- **Lung fibrosis / interstitial lung disease: ruled out.** No IL-33 difference (p = 0.30–0.48).

### Analyses

- Counting tissue blocks as independent (pseudo-replication).
- Taking the delivered tissue labels at face value.
- Ranking genes on fold change or p-value alone (the standard-error artefact).
- Filtering genes on the pooled AveExpr.
- Using DMSO or IL-33-alone as the reference arm.
- Counting duplicate Olink assays as independent evidence, or comparing OR magnitudes across assays.

### Biomarkers

- **The largest in vitro IL-33 outputs as selection markers:** not prognostic in serum.
- **The top prognostic proteins as IL-33 PD markers:** not IL-33-inducible.
- **E-selectin, VCAM-1 and vWF:** statistics cannot be verified.
- **ANGPT2:** not regulated by IL-33.
- **RAGE / EGFR (the oxidised-IL-33 route):** OR 2.3 and 1.16, both not significant; oxidised IL-33 was never tested.
- **Tissue IL-33 immunohistochemistry:** not usable as a patient marker.

---

## Appendix A: How the numbers were derived

### Serum (mmc2)

- Olink assay names were mapped to genes.
- 57 panel-suffixed duplicates (27 proteins) were collapsed to 1,063 unique proteins by averaging the signed z-score, where z = sign(log OR) × Φ⁻¹(1 − p/2).
- The size of the Benjamini–Hochberg family was recovered by solving r = m·p / p_adj for integer ranks. The numbers of omitted assays are lower bounds.
- Enrichment: Fisher exact and Mann–Whitney tests among the 853 proteins whose gene statistics are plausible. Power was estimated by simulation (2,000 draws).
- The `composite_endpoint_0/1` columns are multiples of 1/56 and 1/44. They are interpreted as the fraction of values below the detection limit among 56 non-events and 44 events.

### RNA-seq (mmc4/mmc5)

- Implied standard error = \|logFC / t\|. The plausibility window is 0.01–3 log2 units.
- Because all contrasts come from one model of group means, missing differences were derived exactly from contrasts that share arms. Notation: IN = IL-33 + NIP228 (isotype control), I = IL-33 alone, IC = IL-33 + Compound_47 (AX-1177), V = vehicle.
  - isotype effect: IN − I = (IC − I) − (IC − IN);
  - IL-33 effect in the isotype arm: IN − V.
- **Robust IL-33 gene:** q < 0.05 and \|log2FC\| ≥ 1 vs vehicle, *and* reproduced in the IL-33 + isotype arm (same sign, ≥ 50% of the magnitude).
- **Inhibition** = −(IC − IN) / (IN − V).
- Over-representation was tested by hypergeometric test on MSigDB Hallmark / Reactome (msigdbr 7.5.1), with Benjamini–Hochberg correction.

### Tissue (mmc3)

- Block scores were averaged per donor, and donor fields were collected across all blocks.
- A pathology-text reclassification was used as a sensitivity analysis.
- Tests: Mann–Whitney; Spearman correlation; linear models with age, acute infection and sex; a rank-based model as sensitivity.

### Limits of this review

- The model could not be refitted without count matrices.
- The identity of the 15 missing Inflammation-panel assays is inferred from the vendor's standard panel content, not from the delivery.
- The go/no-go thresholds in Section 5.2 are proposals to be fixed by the team before any unblinding.

## Appendix B: Files

- `AX-1177_portfolio_audit_recommendation.md` / `.html`: this report.
- `AX-1177_supporting_analyses.xlsx`: 14 sheets (integrity log; robust in vitro signatures at 6 h and 24 h with % inhibition; pathways; 53-gene ex vivo module; genes with impossible standard errors; serum proteins collapsed to unique proteins; in vitro–serum bridge; omitted-assay reconstruction; tissue at donor level and tests; biomarker plan; considered and ruled out).
- `figures/Fig1_invitro_pharmacology.png`: IL-33 programme and AX-1177 reversal (HUVEC 6 h / 24 h; HGMEC).
- `figures/Fig2_serum_bridge.png`: proteome-wide severity shift; in vitro induction vs serum prognosis; enrichment test.
- `figures/Fig3_lung_tissue_IL33.png`: donor-level IL-33 by pathology-based group; age confounding.
- `figures/Fig4_rnaseq_SE_artefact.png`: impossible standard errors in the delivered RNA-seq statistics.
