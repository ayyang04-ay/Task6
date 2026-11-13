# AX-1177 (anti-IL-33 IgG1): portfolio audit, recommendation and forward view

**Basis:** the five files delivered for AX-1177 only (methods annex; in vitro RNA-seq, two workbooks; serum proteomics; post-mortem lung IHC). Every number below comes from those files. Statements that rely on outside knowledge are marked *[external]*. All analysis code, tables and figures are in the accompanying folders.

---

## 1. Recommendation: KEEP, but re-scoped and gated (not "continue as planned")

**Proposed resolution for the committee:**

1. Retain AX-1177.
2. Retire the current claim of *"severe lower respiratory viral infection"* as an all-comer indication. Our data do not support it as framed.
3. Re-scope the asset to the one setting our data actually point at: **IL-33-driven endothelial activation in hospitalised severe pneumonia, enriched by high soluble ST2 (sST2) at admission.**
4. Release funds only for Stage 0, an ~8-week package that re-analyses data we already own and needs no new wet lab.
5. Release Stage 1 funds only if Gate A is passed. The kill criteria are written in advance (Section 6.2).

**Why keep.** The data support three points:

- **The molecule does what it should, and cleanly.**
  - In HUVEC, reduced IL-33 (IL-33red) switches on a large NF-κB / inflammatory / procoagulant program: 4,031 genes at FDR < 0.05 at 6 h, including 446 robust genes.
  - AX-1177 reverses a median **97%** of that program at 6 h (slope −0.80, r = −0.92; 354/446 genes significantly reversed) and 80% at 24 h.
  - The same program is opposed in a second vascular bed, glomerular microvascular endothelium (HGMEC), at 6 h (r = −0.73; 227 genes).
  - On its own, AX-1177 has no coherent transcriptional effect in four cell types. Of 632 FDR-significant rows across 16 contrasts, 490 are low-expression noise. No immune or IL-33-pathway genes are among them, and there is no agonist signature (slopes vs. the IL-33 program ≈ 0).
- **The IL-33 receptor axis tracks outcome in sick patients.** In 100 hospitalised COVID-19 patients, serum sST2 (the soluble IL-33 decoy receptor) at enrolment predicts ICU / invasive ventilation / death by day 30:
  - OR 3.02 per log unit (95% CI 1.83–5.01), q = 0.0075, adjusted for age, sex and NEWS2.
  - It ranks **2nd of 1,064 unique proteins** measured.
- **The decisive missing evidence is cheap, and partly generated already.**
  - An IL-33 assay was on the Olink Inflammation panel and was counted in the multiple-testing correction, but it is absent from our copy.
  - The 100 enrolment sera were stored at −80 °C (per the annex), so they can be re-assayed if volume remains.
  - Resolving whether IL-33 is actually engaged in patients therefore costs weeks, not a programme.

**Why not "as is".** Our data also show the following:

- **No direct human evidence that IL-33 is released or active in patients.** Serum IL-33 is not in our data, and lung IL-33 staining is *not* higher in COVID-19 (Section 3.3).
- **The serum signal is non-specific.**
  - Severe patients have higher levels of almost everything: 82% of the 1,094 assays have OR > 1, and 384 reach p < 0.05 (55 expected by chance).
  - The IL-33 program defined in vitro is **not enriched** among outcome-linked serum proteins (68 proteins; median z 1.38 vs 1.42; p = 0.86).
- **The in vitro package lacks the cells and conditions that matter for a lung indication.**
  - No lung microvascular endothelium or airway epithelium was tested.
  - No oxidised IL-33 was tested, even though AX-1177 binds both forms.
  - There is no dose–response, single donors were used, and there are no in vivo data.

**Confidence:** high that AX-1177 neutralises IL-33red in endothelium in vitro; low that IL-33 drives disease in our target population. The plan below moves the second question fastest and cheapest.

---

## 2. Evidence at a glance

| Question | What our data show | Strength |
|---|---|---|
| Does AX-1177 neutralise IL-33 signalling? | Yes, for IL-33red in HUVEC (median 97% reversal at 6 h, 80% at 24 h) and HGMEC at 6 h. Tested at a single ~41:1 molar excess (≈83:1 binding sites), so no potency estimate exists in this dataset. | Strong (in vitro, 2 single-donor endothelial lines) |
| Is AX-1177 inert on its own? | Yes; no coherent transcriptional signal in HUVEC, HGMEC, A549 or MCF7 at 6 or 24 h. | Strong (in vitro) |
| What does IL-33 do to endothelium? | NF-κB / TNF-signalling, inflammatory, IL-6/JAK/STAT3, interferon, complement and coagulation programs. Robust secreted or surface products: GM-CSF, G-CSF, M-CSF, IL-6, IL-1α/β, TNF, CXCL2/3/5/6, CCL20, CX3CL1, CCL5, CXCL10, C3, CFB, MMP-10, **tissue factor (F3) +5.6 log2**, PAI-1, uPA. Also ↓ thrombomodulin (all reversed by AX-1177). | Strong (HUVEC), partial (HGMEC) |
| Are E-selectin, VCAM-1, IL-8, MCP-1, PTX3 or sST2 IL-33-regulated in our cells? | **Not established.** Large log2FCs, but standard errors > 2 log2 units in every contrast; not significant. | None |
| Is the IL-33 axis linked to outcome in patients? | sST2 rank 2/1,064 (q = 0.0075), independent of NEWS2. IL-33 itself: no data. | Moderate, single cohort, non-specific |
| Do IL-33-driven endothelial proteins predict outcome more than other proteins? | No (p = 0.86). Seven of them are individually outcome-associated (IL-6, CCL20, MCP-3/CCL7, OPG, IL-18R1, CSF-1, IL-1β; q 0.012–0.046). | Negative for specificity |
| Is IL-33 increased in diseased lung? | No. High in endothelium and basal epithelium in all groups (endothelium near the scale ceiling). No significant difference at donor level; trend is *lower* in inflamed lungs. | Weak data (post-mortem, single reader) |
| Is there a type-2 / eosinophil link? | No. Lung IL-33 is not correlated with EPX/EDN/MBP (ρ −0.17 to +0.08). Serum IL-5 (p = 0.997), eotaxin-1 (p = 0.84) and CCL24 (p = 0.58) are not associated with outcome. | Consistent negative |

Figures: `figures/Fig1_invitro_pharmacology.png`, `Fig2_serum_proteomics.png`, `Fig3_postmortem_IL33.png`, `Fig4_gated_plan.png`.

---

## 3. The case in detail

### 3.1 In vitro pharmacology (RNA-seq; 114 libraries, 4 cell types, 6 h and 24 h)

- **IL-33 response.** IL-33red (30 ng/mL) vs vehicle in HUVEC changes 4,031 genes at 6 h and 1,836 at 24 h (FDR < 0.05). Robust subset (FDR < 0.05, |log2FC| > 1, expressed, SE < 1): 446 genes at 6 h and 169 at 24 h.
  - Top genes by significance: NFKBIA, RIPK2, SDC4, CSF1, TNFAIP3, NFKB1/2, TRAF1, NFKBIZ, RELB, CXCL2/3, TNF, BIRC3, F3.
  - Hallmark TNFα/NF-κB NES +3.1.
- **Neutralisation.** I used AX-1177 + IL-33 vs isotype + IL-33 as the conservative comparison.
  - HUVEC 6 h: median 96.5% reversal (IQR 77–104%); up-regulated genes 100%, down-regulated genes 75%.
  - HUVEC 24 h: median 80%.
  - Pathway-level mirror images at both timepoints (e.g. TNFα/NF-κB NES −3.1 / −3.0).
- **Second vascular bed (HGMEC).**
  - 6 h: AX-1177 opposes the HUVEC-defined IL-33 program (r = −0.73; 227 genes significantly opposed; TNFα/NF-κB NES −3.7).
  - 24 h: weak (r = −0.24; 19 genes).
  - The HGMEC design has **no vehicle arm**, so the HGMEC IL-33 response itself cannot be estimated. The 24 h result may reflect a waning IL-33 response (as in HUVEC) rather than loss of neutralisation.
- **Kinetics.** The IL-33 signal and its reversal are front-loaded: largest at 6 h, decaying by 24 h. This argues for treating and sampling early (Section 6.4).
- **Specificity.** Antibody-alone contrasts (vs isotype, PBS, DMSO) show no IL-33-like or immune signal. Isotype IC119 is inert in HGMEC but attenuates the IL-33 response in HUVEC by ~11% (6 h) and ~22% (24 h). That is why I use the isotype-matched comparison throughout.

### 3.2 Serum proteomics (100 hospitalised SARS-CoV-2 patients; 13 Olink panels; composite ICU / IMV / death ≤ 30 d)

- **sST2:** OR 3.02 (1.83–5.01) per log unit, p = 1.7×10⁻⁵, q = 0.0075; z = 4.30 vs a proteome median of 1.37 (99.8th percentile).
- **Other leading proteins:**
  - HGF: q = 0.004; not IL-33-regulated in our cells.
  - PTX3: q = 0.012.
  - IL-6: four concordant assays, q 0.012–0.019.
  - Endothelial injury markers: vWF (q = 0.050), ANGPT2 (q = 0.052), sFLT1 (q = 0.052), E-selectin (q = 0.091).
- **Related IL-1-family receptors:** IL-18R1 (q = 0.018) and IL-1R2 (q = 0.018) are associated. IL-1R1 is not (q = 0.28).
- **Caveats:**
  - The proteome-wide shift makes single markers non-specific.
  - ORs "per log unit" are not comparable across proteins; CSF-1's OR is 90 with a CI of 4–1,933.
  - The log scale is unstated.
  - n = 100, single centre, pre-vaccination era.
- **Bridge test:** 68 proteins were both in the serum panels and in the IL-33-induced, AX-1177-reversed HUVEC program. They are no more outcome-associated than the other 845 measured proteins (p = 0.86). The HGMEC-defined and two-bed-defined sets give the same result (p = 0.66 and 0.29).

### 3.3 Post-mortem lung (31 donors, 74 blocks)

- **IL-33 staining at donor level** (COVID+ "pneumonia" / COVID− "pneumonia" / "non-pneumonia"), Kruskal–Wallis p:
  - Endothelium: 4.81 / 5.50 / 5.50 (p = 0.11).
  - Basal epithelium: 4.25 / 4.50 / 4.88 (p = 0.65).
  - Vascular smooth muscle: 2.38 / 3.25 / 3.50 (p = 0.16).
- **No increase in COVID-19.**
  - If anything, staining is lower where the lung is injured. Diffuse alveolar damage (DAD) vs no DAD, smooth muscle: 1.78 vs 3.25, p = 0.055.
  - Donor-level endothelial IL-33 is inversely correlated with neutrophil elastase (ρ = −0.43, p = 0.02).
  - Lower staining is what release of stored IL-33 would look like. It is also what endothelial loss would look like, and IHC cannot tell the two apart. All of this is exploratory and uncorrected for multiple comparisons.
- **Inflammatory-cell markers** (EDN, MBP, IL-5Rα, neutrophil elastase) separate pneumonia from non-pneumonia (donor-level p 0.004–0.009). They do **not** separate COVID+ from COVID− pneumonia (p 0.44–1.0).
- **Implication:** IL-33 target tissue is present in every donor, so the target is there. IL-33 IHC is useless for patient selection, and nothing here is specific to SARS-CoV-2.

### 3.4 Anticipated challenges and responses

| Challenge | Response grounded in our data |
|---|---|
| "sST2 is just a severity marker." | Partly true: 82% of proteins rise with severity. sST2 is nonetheless 2nd of 1,064 after adjustment for NEWS2. We propose it for prognostic enrichment, not as proof of mechanism. Mechanism is tested directly at Gate B. |
| "There is no evidence IL-33 is elevated." | Correct. The IL-33 assay was run and counted in the BH correction but not delivered to us. Retrieving it is Stage 0, step 1. |
| "Lung IL-33 isn't increased in COVID-19." | IHC measures stored IL-33, not released IL-33. Staining is at ceiling in endothelium, and the trend is lower in injured lung. IHC is not the right read-out and we do not propose it for patients. |
| "HUVEC aren't lung cells." | Agreed. A second bed (HGMEC) replicates at 6 h. Primary lung microvascular endothelium (≥ 3 donors) is the first wet-lab experiment. |
| "The effect fades by 24 h." | The IL-33 response itself fades (4,031 → 1,836 genes). Reversal of what remains is still 80% in HUVEC. The implication is to treat early and sample early. |
| "Why not COPD, like others?" *[external]* | Our data contain no COPD cohort and no epithelial IL-33 experiment. Lung IL-33 does not differ by COPD history (11 vs 20 donors; p = 0.21–0.59). COPD would be a literature bet, not a data-driven call. |
| "Severe COVID-19 has become rare." *[external]* | Nothing in our tissue or cell data is SARS-CoV-2-specific. The next human-sample work should span COVID-19, influenza/RSV and bacterial pneumonia. |

---

## 4. Data-integrity findings the committee should know

The full log is in the supporting workbook (`AX-1177_supporting_tables.xlsx`, sheet `1_Data_integrity_log`; 19 items). These are the ones that change how the evidence should be read.

1. **Hidden content.**
   - Post-mortem workbook: all 15 IHC score columns, including all IL-33 scores, are hidden (several at zero width).
   - Proteomics workbook: both 95% CI columns and two duplicate rows are hidden.
   - I analysed every cell. Anyone reading the sheets as displayed would not see the IL-33 tissue data or how imprecise the ORs are.
2. **Incomplete proteomics delivery.**
   - BH correction was computed over 1,194 tests (implied m = 1194.0), but 1,094 assays were delivered.
   - The missing 100 are interspersed in the ranking: about 4 were at q < 0.05, one at p ≈ 2–3×10⁻⁴.
   - They include the Inflammation-panel IL-33 assay (inferred from panel composition; to be verified against the vendor manifest).
3. **Duplicated proteins.** 26 proteins are measured on more than one panel. IL-6 alone occupies 4 of the top 28 rows. At q < 0.05 there are 178 assays but only 169 unique proteins.
4. **RNA-seq presentation.**
   - The "6h" and "24h" sheets are identical in content; each holds all 24 contrasts at both timepoints.
   - The HUVEC IL-33 sheets are sorted by fold change, and 4 of their top-20 genes (SELE, VCAM1, CXCL8, CXCL1) are not significant.
   - A set of endothelial genes carry standard errors > 2 log2 units everywhere. This is consistent with a single model across four cell types; a per-cell-type re-fit is needed.
   - The implied residual df is 75, not the 76 implied by the annex.
5. **Post-mortem labels and structure.**
   - 4/10 "COVID-negative pneumonia" donors have no pneumonia documented.
   - 3/5 "non-pneumonia" controls have acute pneumonia, pneumonitis or fungal lung infection.
   - Three COVID+ donors contribute 24 of 49 COVID+ blocks. Block-level statistics make non-significant IL-33 differences look significant (p = 0.028 / 0.016 vs donor-level 0.11 / 0.16).
   - MBP staining shows a batch effect by block series.

None of these reverses the core conclusions above. Items 1, 2 and 4 must be fixed before any of this material is used externally.

---

## 5. Forward view

### 5.1 What indication the data actually point at

**The mechanism:** IL-33 → endothelium (NF-κB activation, leukocyte-recruiting chemokines and colony-stimulating factors, and a procoagulant switch: tissue factor ↑, PAI-1 ↑, thrombomodulin ↓).

**The only human setting with a signal:** hospitalised severe pneumonia at risk of progression to respiratory failure, where admission sST2 predicts ICU / IMV / death.

The data therefore point to a **narrower, host-directed, vascular version of the current indication**: *"hospitalised severe pneumonia (viral; COVID-19 is the only aetiology with data) with IL-33/ST2-axis activation, treated early to prevent progression to ICU / IMV / death."* This is not a different disease. No repurposing candidate has support in our data (Section 7).

- **Pathogen scope.** Tissue IL-33 and inflammatory infiltrates look the same in COVID-negative bacterial bronchopneumonia as in COVID-19. The biology in our data is therefore pathogen-agnostic, but the clinical evidence is COVID-only. The validation work must include influenza/RSV and bacterial pneumonia before a label scope is chosen.
- **Thrombo-inflammation** is a coherent sub-theme but not a stand-alone indication:
  - In vitro: F3 +5.6 log2 and PAI-1 +1.7, both reversed by AX-1177.
  - Pulmonary thromboemboli in 4/16 COVID+ donors vs 0/15 COVID− (Fisher p ≈ 0.10).
  - Serum uPAR (q = 0.025), vWF (q = 0.050), uPA (q = 0.066), TFPI (q = 0.12) and PAI-1 (q = 0.15) are nominally associated with outcome (p 0.002–0.048). That is consistent with the mechanism, but not specific given the proteome-wide shift.
  - It is carried forward as a pharmacodynamic module.

### 5.2 What the next studies must establish (with proposed go / kill criteria)

| # | Must establish | Study | Proposed go criterion | Kill signal |
|---|---|---|---|---|
| 1 | IL-33 is released in patients, which redox form, and whether it tracks outcome | (a) Retrieve the withheld Olink IL-33 result. (b) High-sensitivity reduced / oxidised / total IL-33 and IL-33:sST2 complex in the 100 banked enrolment sera. | Detectable in ≥ 30% of sera, and higher in patients with events **or** correlated with sST2 / the 7-plex panel (p < 0.05) | Undetectable or unrelated |
| 2 | sST2 adds prognostic information beyond clinical severity and generic inflammation | Patient-level re-fit: sST2 on top of age/sex/NEWS2 **plus IL-6 and HGF**; ΔAUC, calibration, bootstrap cut-point. Then external replication (COVID-19, influenza/RSV, bacterial CAP). | Remains independent (p < 0.05) with IL-6 + HGF in the model; ΔAUC ≥ 0.03 over the NEWS2 model | Loses significance once IL-6/HGF are added; enrichment strategy then needs rethinking |
| 3 | Endothelial activation driven by patient material is IL-33-dependent (the pivotal test) | Enrolment sera (sST2-high vs -low) on primary lung microvascular endothelium (≥ 3 donors) ± AX-1177 vs isotype; 6 h read-out of the IL-33 panel | AX-1177 reduces serum-induced activation by ≥ 30% vs isotype, more in sST2-high sera | No AX-1177 effect on patient sera |
| 4 | Potency and breadth | Lung microvascular endothelium + primary airway epithelium; IL-33red **and** IL-33ox; dose–response (IC50/IC90); 1, 3, 6, 24 h; TNF and IL-1β comparators to define an IL-33-specific signature; protein read-outs | ≥ 80% reversal at achievable concentrations; defined IL-33-specific panel | Activity confined to HUVEC |
| 5 | In vivo proof of concept | Viral pneumonia model with therapeutic (post-infection) dosing. Species cross-reactivity must first be confirmed; it is not in our data. | Reduced lung injury, vascular leak or thrombosis | No effect with confirmed target engagement |

**Termination rule:** if items 1 **and** 3 are both negative, terminate.

**Risks our data cannot address (they need separate work-streams):**
- AX-1177 potency and affinity (held in the biologics file, not in this dataset).
- Species cross-reactivity, PK and safety.
- The effect of neutralising IL-33 on host defence and tissue repair *[external]*.
- Feasibility of enrolling severe-pneumonia trials in the current epidemiology *[external]*.
- Competitive anti-IL-33 programmes *[external]*.

### 5.3 Biomarkers: which could go into patients, and in what role

| Marker | Our evidence | Role | Specimen / timing | Into patients? |
|---|---|---|---|---|
| **sST2** | Serum rank 2/1,064, q = 0.0075, independent of NEWS2. In vitro IL-33 regulation not established. | **Prognostic enrichment / stratification** | Serum, at enrolment (pre-dose) | **Yes, now.** Stratification factor, or enrichment once a cut-point is validated (clinical-grade assays exist *[external]*). **Not** a PD marker; predictive value unproven, so test it as a pre-specified interaction. |
| **IL-33** (total, free; reduced/oxidised) | None delivered (assay run, not in our copy) | **Target engagement** (total / drug-bound IL-33); candidate predictive marker if baseline is detectable | Serum: pre-dose, then PD times | **Yes, after assay qualification** (Phase 1b/2 TE). Selection role only if Study 1 is positive. |
| **IL-33 endothelial response panel (7-plex):** IL-6, CCL20, MCP-3/CCL7, OPG, IL-18R1, CSF-1, IL-1β | All three: IL-33-induced in HUVEC, reversed by AX-1177 in HUVEC **and** HGMEC at 6 h, and serum-associated with outcome (q 0.012–0.046) | **Pharmacodynamic** (pathway modulation vs placebo); secondary prognostic | Serum: pre-dose, 6 h, 24 h, day 3, day 7 | **Yes, exploratory PD.** Not for selection: not IL-33-specific (bridge test negative; shared with TNF/IL-1 biology). |
| **Procoagulant module:** PAI-1, uPA, tissue-factor activity, thrombomodulin | In vitro induced (TF, PAI-1, uPA) or repressed (thrombomodulin) and reversed by AX-1177. Serum PAI-1 q = 0.15, uPA q = 0.066. | Exploratory PD and mechanistic safety read-out | Plasma, same schedule (TF activity needs plasma, not serum) | Yes, exploratory |
| HGF, PTX3, vWF, ANGPT2 | Outcome-associated, but not IL-33-linked in our cells (HGF, ANGPT2 not induced; PTX3, vWF unreliable) | Prognostic covariates only | Enrolment | Yes, as covariates, **not** as IL-33 markers |
| Lung IL-33 IHC | No group discrimination; ceiling effect; post-mortem | Research only | — | **No** |
| Eosinophil / type-2 markers | No link to IL-33 or outcome | None | — | **No** |

### 5.4 Sampling timepoint

**Primary timepoint: enrolment / hospital admission, before ICU or IMV, pre-dose.** Three reasons:

1. It is the only timepoint at which we have outcome-linked human data. Serum taken at enrolment predicts 30-day ICU / IMV / death.
2. In our cells the IL-33 program and its reversal are largest at 6 h and decay by 24 h:
   - 4,031 → 1,836 genes.
   - Reversal 97% → 80%.
   - HGMEC r −0.73 → −0.24.
   This points to an early therapeutic window.
3. Enrichment must be decided before dosing.

**PD sampling should be front-loaded:** pre-dose, then 6 h and 24 h post-dose, day 3 and day 7, with outcome at day 30 (matching our endpoint). The 6 h in vitro optimum is also the read-out time for the patient-serum transfer assay (Study 3). In vivo kinetics are unknown and must be measured in the first patient study.

### 5.5 Staged plan (`figures/Fig4_gated_plan.png`)

**Stage 0 (weeks 0–8; no new wet lab)**
- Retrieve the 100 withheld assays and the patient-level data.
- Run Study 2.
- Re-fit the RNA-seq per cell type from archived counts, including the missing HGMEC IL-33 vs isotype contrast.
- Blinded second-reader IHC re-score at donor level.

**Gate A.** Go if sST2 survives IL-6 + HGF adjustment and/or the IL-33 assay is informative.

**Stage 1 (months 2–8)**
- Studies 1, 3 and 4.

**Gate B.** Go if Studies 1 and 3 are positive; kill if both are negative.

**Stage 2 (months 8–18)**
- External, pathogen-spanning validation cohort.
- In vivo model.
- Clinical-grade assays.

**Gate C → Phase 1b/2a design**
- Hospitalised pneumonia patients not on IMV, enrolled at admission.
- Stratified by sST2.
- Endpoint: ICU / IMV / death by day 30.
- 7-plex PD panel plus target engagement.

---

## 6. If the committee drops AX-1177: what we are dropping, and why

**What we would drop:**
- A specific anti-IL-33 IgG1 that, in our hands, nearly abolishes reduced-IL-33 signalling in two endothelial beds without detectable off-target transcriptional activity.
- An unvalidated but mechanism-consistent prognostic-enrichment hypothesis: admission sST2 in hospitalised COVID-19 pneumonia.

**The defensible reasons to drop:**
- There is no direct evidence that IL-33 is released or active in the target population.
- The only clinical signal is non-specific.
- Lung IL-33 is not increased.
- The package lacks lung cells, the oxidised form, potency data and in vivo efficacy.

**What dropping now would cost:** the chance to settle the central question with data and samples we already hold, for negligible spend. That is why the recommendation is a gated keep rather than a drop.

---

## 7. What I considered and ruled out

**Indications**

| Option | Verdict | Reason (our data) |
|---|---|---|
| Continue "severe lower respiratory viral infection", all-comers | Ruled out as framed | The human data are COVID-only, single-centre and pre-vaccination. There is no evidence IL-33 itself rises. The serum signal is non-specific, so an unselected population would dilute any effect. |
| COVID-19-specific positioning | Ruled out as sole focus | Nothing in tissue or cell data is SARS-CoV-2-specific. COVID+ and COVID− pneumonia do not differ in IL-33 or inflammatory cells. |
| Asthma / type-2 airway disease | Ruled out | IL-33 is uncorrelated with eosinophil markers and does not differ by asthma history. Serum IL-5 and eotaxins show no association. No epithelial, ILC2 or mast-cell experiments exist. |
| COPD | Ruled out on our data | No COPD cohort. IL-33 does not differ by COPD history. No airway-epithelial IL-33 data. This would be a literature-driven bet *[external]*. |
| Kidney (glomerular endothelium) | Ruled out as lead | One single-donor HGMEC line, no vehicle arm, and neutralisation fades by 24 h. No kidney patient data. Serum kidney markers are unremarkable (KIM-1 q = 0.11; cystatin C p = 0.18). |
| Oncology | Ruled out | A549 and MCF7 were antibody-alone specificity controls only; there was no IL-33 arm. |
| Thrombosis / VTE stand-alone | Folded into the lead indication | Mechanistically consistent but not specific. Kept as a PD module. |
| All-cause ARDS | Closest neighbour; not separate yet | Our DAD donors are all COVID+. It is covered by the "pneumonia at risk of respiratory failure" framing. |

**Biomarkers ruled out:**
- Lung IL-33 IHC.
- Serum IL-33 as delivered (absent).
- The largest-OR proteins (GSTP1 24.6 [3.9–155], SEMA4C 20.9, CALR 19.7, CSF-1 90 [4–1,933]): these are artefacts of per-log-unit scaling.
- HGF as an IL-33 marker (prognostic only).
- PTX3, E-selectin, VCAM-1, IL-8, MCP-1 and sST2 as IL-33 PD markers (in vitro estimates unusable).
- Soluble IL-4Rα (q = 0.020), generic and with no IL-33 link.
- Eosinophil and type-2 markers.

**Analytical shortcuts ruled out:**
- Block-level IHC statistics.
- Ranking genes by fold change.
- Taking the delivered q-values and hit counts at face value.
- Reading the "6h"/"24h" sheet names as timepoints.
- Comparing ORs across proteins.
- Inferring an HGMEC IL-33 response without a vehicle arm.
- Treating group labels as pathology-verified.

---

### Appendix A: methods in brief

- **RNA-seq.** Used the delivered limma-voom contrasts as-is.
  - Verified: AveExpr identical across all 26 contrasts; P consistent with t under robust eBayes (df.total 75.05–85.13); BH reproduces within each contrast.
  - "Robust" = FDR < 0.05, |log2FC| > 1, AveExpr > 0, SE < 1.
  - Reversal = −(AX-1177+IL-33 vs isotype+IL-33) / (IL-33 vs vehicle), per gene.
  - fgsea on moderated t with MSigDB Hallmark sets.
- **Proteomics.** Wald z = ln(OR)/SE, with SE from the CI width (p-values reproduce to 10⁻⁴ in log10).
  - Protein-level collapse across panels.
  - Olink-name → HGNC mapping for the bridge test (Mann–Whitney).
- **Post-mortem.**
  - All cells read, including hidden columns; "n+" grades parsed to n.
  - Donor-level means.
  - Kruskal–Wallis and Mann–Whitney tests, Spearman correlations; exploratory and uncorrected.
  - Pathology re-read documented per donor in `code/pm_curation.py`.

### Appendix B: deliverables

- `AX-1177_portfolio_audit_memo.md` / `.pdf`: this memo.
- `AX-1177_supporting_tables.xlsx`: integrity log, DE burden, reversal, signature genes, GSEA, serum protein-level table, bridge test, biomarker evidence, post-mortem donor table and comparisons.
- `figures/`: Fig 1–4.
- `code/`: 01–07 scripts (Python, plus R for fgsea); re-run from the raw files.
