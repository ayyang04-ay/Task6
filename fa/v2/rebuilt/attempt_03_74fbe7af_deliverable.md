# AX-1177 (anti-IL-33): portfolio audit recommendation and forward view

**Prepared for:** Respiratory portfolio audit committee
**Evidence base:** Only the AX-1177 data package: `mmc2` (serum proteomics in hospitalised COVID-19), `mmc3` (post-mortem lung IHC), `mmc4`/`mmc5` (endothelial and epithelial transcriptomics), and the methods annex. All numbers below come from re-analysis of these files. Scripts, tables and figures are in `/tmp/outputs/`.

---

## 1. Recommendation

**No. Do not keep AX-1177 in the active portfolio as a viral-LRTD asset.** Stop spending on viral LRTD. Archive the molecule, reagents and data so the asset can be reopened, and do not repurpose it on the current evidence.

**Why, in one sentence.** In the dish the molecule does exactly what it should. But none of our three human datasets shows that IL-33 is released, active or linked to outcome in the disease, and all of our human data come from pre-vaccination COVID-19, not viral LRTD.

**How confident I am**
* *High* that our data do not support viral LRTD as the indication.
* *Moderate* that IL-33 plays no role. That conclusion rests on absence of evidence, and the key measurement is missing:
  * The serum file was trimmed before delivery. The multiple-testing correction was run on **1,194 assays**, but only **1,094** were delivered (§6).
  * IL-33 is on one of the panels that was run, but it is not in the file.
  * Retrieving those ~100 withheld results is a data request that should take days. It is the one item that could change this recommendation quickly.

---

## 2. What our data show: the chain of evidence an indication needs

| # | Link in the chain | Our evidence | Verdict |
|---|---|---|---|
| 1 | AX-1177 neutralises IL-33 | Complete, isotype-controlled block of the IL-33red endothelial response (HUVEC; inferred in HGMEC) | ✔ Strong (in vitro) |
| 2 | AX-1177 is specific | With no IL-33 present, it changes the transcriptome of 4 cell types no more than swapping one vehicle for another | ✔ Strong (in vitro) |
| 3 | IL-33 is present in the target tissue | IL-33 is abundant in lung endothelium, basal epithelium and vascular smooth muscle in **every** donor | ✔ but not disease-specific |
| 4 | IL-33 is released or active in the disease | Not measured in serum. Tissue levels are unchanged by COVID status. The serum signature has no IL-33-specific fingerprint | ✘ Not shown |
| 5 | IL-33 activity tracks with outcome | sST2 is prognostic but travels with the whole IL-1-family decoy set. The AX-1177-reversible programme is not enriched among prognostic proteins | ✘ Not shown |
| 6 | Result generalises to "viral LRTD" | Human data cover only SARS-CoV-2, single centre, pre-vaccination | ✘ No data |
| 7 | Efficacy in vivo | No data in the package | – |

Links 1–3 qualify the molecule. Links 4–7 qualify the indication, and they are the ones missing.

### 2A. The molecule (in vitro transcriptomics, `mmc4`/`mmc5`)

**IL-33 strongly activates endothelium.** IL-33red at 30 ng/mL gave a large NF-κB-type programme in HUVEC at 6 h: 1,068 genes changed ≥2-fold (BH adj.p < 0.05). Top hits by log2 fold change:

| Gene | log2FC at 6 h |
|---|---|
| E-selectin (SELE) | +11.2 |
| GM-CSF (CSF2) | +10.3 |
| CXCL6 | +9.4 |
| CCL20 | +9.2 |
| VCAM-1 | +8.7 |
| G-CSF (CSF3) | +8.3 |
| IL-8 (CXCL8) | +8.2 |
| TNF | +7.9 |
| ICAM-1 | +6.0 |
| IL-6 | +5.8 |
| Tissue factor (F3) | +5.6 |

Complement C3 also rose (+6.1 at 24 h).

**AX-1177 blocks it completely.**
* The antibody was at ≈41-fold molar excess (10 µg/mL ≈ 68.5 nM vs 1.66 nM IL-33), added at the same time as IL-33 with no pre-incubation.
* Median neutralisation per gene was 92% at 6 h (IQR 62–102%) and 78% at 24 h.
* The IL-33 effect measured in the IL-33 and vehicle libraries is reproduced by the AX-1177-vs-isotype comparison, which uses a completely separate set of libraries: r = 0.92 at 6 h and 0.73 at 24 h (Fig 1).

**Microvascular endothelium shares the programme, briefly.**
* HGMEC has no vehicle arm, so its response can only be inferred from the reversal by AX-1177.
* At 6 h, 556 genes were reversed. The profile tracks HUVEC (r = 0.63), at ~80% of the HUVEC magnitude (VCAM-1 −11.7, E-selectin −8.7, G-CSF −6.5, CXCL1 −6.3 log2).
* By 24 h the HGMEC response has largely decayed (r = 0.31), and the two HGMEC estimates disagree (only 45 genes in common) (Fig 2).

**AX-1177 alone is inert.**
* With no IL-33 added, the antibody vs isotype comparison gave 21–73 nominal "hits" per contrast. Of these, 56–91% were genes with low average expression (below the dataset mean).
* No hit reproduced in the same direction in 2 or more of the 8 contrasts.
* The |log2FC| distribution matches the vehicle-vs-vehicle noise floor (DMSO vs PBS) (Fig 3).
* There is no sign of agonism and no suppression of the IL-33 programme at baseline (|ρ| ≤ 0.09).

**Secondary observation (relevant to safety).** IL-33 also induced an interferon-stimulated gene module in endothelium, and AX-1177 blocked it:

| Gene | IL-33 log2FC | Timepoint |
|---|---|---|
| CXCL10 | +6.9 | 6 h |
| OASL | +3.4 | 6 h |
| IFIH1 | +2.4 | 6 h |
| MX2 | +3.7 | 24 h |
| GBP5 | +4.7 | 24 h |

Blocking at 24 h was incomplete for some of these genes (table T15). In a viral indication this needs watching.

**What the molecule data cannot tell us**
* Potency: there is a single concentration of each article, so no IC50.
* Oxidised IL-33: not tested, although the annex says AX-1177 binds it.
* Epithelial IL-33 signalling: A549 and MCF7 never received IL-33.
* Lung endothelium: not tested.
* Donor variability: one donor per endothelial type.
* Whether endothelium ever sees 30 ng/mL IL-33 in patients.

### 2B. The patients (serum proteomics, `mmc2`)

**Cohort.** 100 hospitalised, pre-vaccination COVID-19 patients, serum taken at enrolment. Results are 1,094 one-protein logistic models adjusted for age, sex and NEWS2. The per-group columns imply **56 non-events and 44 events**.

**sST2 is a strong prognostic marker.** It ranked 2nd of 1,094 assays: OR 3.02 per log unit (95% CI 1.83–5.01), p = 1.7×10⁻⁵, BH adj.p = 0.0075. This is on top of NEWS2.

**The sST2 signal is not IL-33-specific.**
* The other IL-1-family soluble and decoy receptors rise with it: IL-1R2 (OR 4.5, adj.p 0.018), IL-18R1 (OR 6.1, adj.p 0.018) and IL-1ra (OR 3.2, p 0.019).
* In vitro, IL-33 induced its own receptor (IL1RL1) only modestly in HUVEC (+1.6 log2 at 6 h, +0.4 at 24 h), the statistics for that gene are unreliable (§6), and there was no induction in HGMEC.
* sST2 is the IL-33 decoy receptor, so a high level could equally mean IL-33 is already being soaked up.

**IL-33 itself was never delivered.** It is one of 15 assays missing from the 92-assay Inflammation panel. TSLP and IL-1α, the other epithelial alarmins on that panel, are also missing.

**The serum signature of severe disease does not carry the AX-1177-reversible endothelial fingerprint (Fig 4):**

| Proteins compared | Proportion prognostic (adj.p < 0.05) | Comparison |
|---|---|---|
| All 99 endothelial IL-33-response proteins measured | 17% | vs 17% background; Fisher OR 0.99, p = 1.0 |
| Strictly defined subset (68 proteins) | 19% | OR 1.14, p = 0.62 |
| Proteins induced ≥8-fold | 21% | OR 1.26, p = 0.62 |
| Unchanged proteins | 20% | reference |

**The most IL-33-driven, AX-1177-reversible proteins are not prognostic:**

| Protein | OR | p |
|---|---|---|
| G-CSF | 1.25 | 0.23 |
| CXCL1 | 1.40 | 0.28 |
| CXCL5 | 1.17 | 0.52 |
| CXCL6 | 1.02 | 0.95 |
| sVCAM-1 | 1.28 | 0.43 |
| sICAM-1 | 1.67 | 0.11 |
| TNFRSF9 | 1.09 | 0.68 |
| sE-selectin | 2.08 | 0.022 (nominal only; adj.p 0.09) |

**The IL-33-inducible proteins that are prognostic are generic NF-κB outputs:**

| Protein | OR | adj.p |
|---|---|---|
| IL-6 | 2.14 | 0.012 |
| OPG | 6.77 | 0.014 |
| CCL20 | 1.83 | 0.020 |
| IL-8 | 2.23 | 0.023 |
| IL-1β | 2.45 | 0.046 |

**Endothelial injury shows up, but it is not IL-33-driven.** Injury markers that IL-33 does *not* induce in vitro are at least as prognostic: vWF (OR 3.86), ANGPT2 (OR 2.21), HGF (ranked 1st). Severe disease shows endothelial injury, not an IL-33-specific activation pattern (Fig 6).

**No type-2 downstream signal.** IL-5 (OR 1.00), eotaxin (CCL11, 1.08), CCL24 (0.92), TARC (CCL17, 0.85) and tryptase (1.07) are all flat.

### 2C. The tissue (post-mortem lung IHC, `mmc3`; 31 donors, 74 blocks, analysed per donor)

**IL-33 is everywhere, and at ceiling.**
* 39 of 74 endothelial blocks score 5.5, above the stated 0–5 scale.
* Median endothelial score by group:

| Group | Donors | Median endothelial IL-33 |
|---|---|---|
| Non-pneumonia | 5 | 5.5 |
| COVID-negative pneumonia | 10 | 5.5 |
| COVID-positive pneumonia | 16 | 4.8 |

* Group difference p = 0.11. Epithelial (p = 0.65) and smooth-muscle (p = 0.16) scores also do not differ.
* The only trend is **downward** in COVID-positive lungs.

**Pneumonia, not SARS-CoV-2, separates the inflammatory cell scores.**
* Pneumonia vs non-pneumonia: neutrophil elastase p = 0.007, EDN p = 0.004, MBP p = 0.006, IL-5Rα p = 0.005–0.009.
* COVID-positive vs COVID-negative pneumonia: no marker differs (all p ≥ 0.15).

**Possible release signal, but ambiguous.**
* Nuclear endothelial IL-33 falls as neutrophilic inflammation rises (ρ = −0.43, p = 0.016; still p = 0.016 after adjusting for age).
* This fits IL-33 release. It equally fits endothelial injury, or down-regulation on activation (IL-33 mRNA fell 0.9 log2 in HUVEC at 24 h, p = 0.055).
* One reader, a ceiling-limited scale and n = 31 mean this is hypothesis-generating only (Fig 5).

---

## 3. The case for keeping it, taken seriously, and why it does not hold

| Argument for keeping | Response from our data |
|---|---|
| "sST2 is the #2 predictor of 1,094. The IL-33 axis is obviously engaged." | sST2 is prognostic, and I propose using it for enrichment. But IL-1R2, IL-18R1 and IL-1ra rise alongside it, so the signal is a family-wide innate response. IL-33 barely induces ST2 in our endothelial cells. Being prognostic is not the same as being caused by IL-33. |
| "IL-6, OPG, IL-8, CCL20 and PTX3 are IL-33-inducible and prognostic." | They are canonical NF-κB products, and IL-33-inducible proteins as a group are no more often prognostic than unchanged proteins (17% vs 17%). The proteins most specific to the IL-33 endothelial response (G-CSF, CXCL1/5/6, VCAM-1, TNFRSF9) are not prognostic. |
| "IL-33 sits in lung endothelium, exactly where COVID damage happens." | It sits there at the same level in lungs without pneumonia. Presence is not activity. |
| "Lower endothelial IL-33 in inflamed lungs means it was released." | That is possible, and it is the most interesting observation in the package. But it is not COVID-specific, it cannot be told apart from endothelial injury or transcriptional down-regulation, and it rests on one reader, 31 donors and a ceiling-limited scale. It is a reason to run Stage 1, not a reason to carry the asset. |
| "The molecule is clean and blocks completely. Why drop a good antibody?" | We are not dropping it for molecule reasons; the indication hypothesis is what fails. Even on the molecule, potency (IC50), oxidised IL-33 and lung endothelial/epithelial activity are not yet established. |
| "Absence of evidence is not evidence of absence." | Agreed, which is why §4.7 sets a concrete re-entry test. But a portfolio slot needs positive evidence. The data we generated to supply it came back negative or non-specific, and the one direct measurement (serum IL-33) was not delivered. |

---

## 4. Forward view

### 4.1 What indication our data actually point at

Read strictly, our data point at **one population: adults hospitalised with severe pneumonia at risk of ICU, ventilation or death, who show a systemic host response of endothelial injury plus innate inflammation at admission, with high sST2 marking the highest risk.**

* **COVID-19 is the only cause we have serum data for.**
* **The tissue data argue against tying the indication to a virus.** Every IL-33 and inflammatory-cell score we measured was the same in COVID-positive and COVID-negative pneumonia. If anything, the data favour a host-response-defined, pathogen-agnostic "severe pneumonia" framing over a virus-defined "viral LRTD" one.
* **Even in that population, nothing shows IL-33 is the driver.** This is a narrowing of the current space, not a new indication.

**No other indication is supported.** I checked the directions the data might suggest (§5): chronic airway disease, kidney, thrombo-inflammation and oncology. None is supported by our data. Any repurposing would be a literature-led bet and should be run as a new programme held to the Stage-1 evidence bar below.

### 4.2 What we would be dropping, and why (a statement you can use)

> We are stopping development of AX-1177 for viral lower respiratory tract disease.
>
> **What we are dropping:** a specific, well-behaved IL-33 neutraliser. It completely blocks IL-33-driven activation of both large-vessel and microvascular endothelium (adhesion molecules, neutrophil chemokines, G-CSF and GM-CSF, IL-6, tissue factor, complement), with no IL-33-independent activity in four cell types. It comes with a prognostic marker, sST2, for severe COVID-19.
>
> **Why we are dropping it:** the data we generated to show that IL-33 drives the disease did not show it.
> * Circulating IL-33 was not delivered.
> * Lung IL-33 is no different with or without COVID.
> * The serum signature of severe disease carries no IL-33-specific fingerprint.
> * All patient data come from pre-vaccination COVID-19, not the wider viral-LRTD population.
>
> The molecule and data package are archived, and the asset can be reopened if the defined re-entry test is met.

### 4.3 What the next studies must establish

These are listed in order of decision value.

1. **IL-33 is released or active in the target patients,** measured directly (free and total, ideally reduced vs oxidised) or through an IL-33-specific activity score, and not just as generic inflammation.
2. **That activity tracks with outcome,** independent of NEWS2, IL-6 and sST2.
3. **The finding holds outside SARS-CoV-2** (RSV, influenza, hMPV) **and in today's vaccinated population,** or is shown to be pathogen-agnostic in severe pneumonia.
4. **IL-33 acts on the relevant human cells at concentrations patients actually have:**
   * primary lung microvascular endothelium and airway epithelium;
   * reduced and oxidised IL-33;
   * three or more donors.
5. **AX-1177 has adequate potency and timing:**
   * IC50 determined;
   * block holds with and without pre-incubation;
   * it does not impair antiviral defence (the interferon module).
6. **In vivo proof of concept,** plus a target-engagement assay.

### 4.4 Biomarkers: candidates, roles, and which can go into patients

| Marker | Role in patients | Ready now? | Basis in our data |
|---|---|---|---|
| **sST2** | **Prognostic enrichment and stratification at baseline** | **Yes.** Needs a clinical-grade assay and cut-off; Olink "per log unit" cannot set a threshold. | Ranked 2nd of 1,094; OR 3.02 (1.83–5.01); adj.p 0.0075; independent of NEWS2. Not a PD marker (non-specific, weakly IL-33-induced). Predictive value untested; pre-specify a treatment × sST2 interaction. |
| IL-6 | Stratification covariate; exploratory PD | Yes | Reproduced on 4 panels (OR 2.07–2.31). IL-33-inducible and reversed in vitro, but not specific. |
| **Endothelial IL-33 response panel:** CCL20, OPG, IL-8, sE-selectin, G-CSF, CXCL1, CXCL5, CXCL6, fractalkine, sVCAM-1, sICAM-1 | **Exploratory PD:** change from baseline on drug vs placebo. Not for selection or go/no-go. | Yes, as exploratory | All induced by IL-33 in both endothelial types, fully reversed by AX-1177 at 6 h and 24 h, and measurable in patient serum (all delivered on Olink). Not IL-33-specific without TNF/IL-1 comparators (§4.6, Stage 2). |
| CCL20, OPG | Mechanism-linked prognostic and PD candidates | Exploratory | The only markers that are both clean IL-33 responders in vitro and prognostic (adj.p 0.020 and 0.014) |
| Free/total IL-33 | **Target engagement** | **No.** Needs an assay first. | Not in the delivered data |
| Viral load/clearance, plus CXCL10 as an interferon readout | **Safety** | Yes | IL-33 induces an interferon-stimulated gene module (CXCL10, MX1/2, IFIT1–3, OASL, RSAD2) that AX-1177 blocks |
| HGF, PTX3, vWF, ANGPT2, IL-1R2 | Covariates only | Yes | Prognostic, but not IL-33-driven |
| Lung IL-33 IHC | None (research use only) | No | At ceiling in all groups, does not discriminate, post-mortem only |

No predictive biomarker is validated. Treatment × sST2 and treatment × endothelial-score interactions should be pre-specified as exploratory analyses.

### 4.5 Sampling timepoint

**Primary (patients): at enrolment, before the first dose, as early as possible after admission (target ≤ 24 h), with days since symptom onset recorded.**

* This is the timepoint of the only human evidence we have: the Olink associations were measured on enrolment serum. sST2 enrichment can therefore be carried forward without re-validating timing.
* Our in vitro data show that **the IL-33-dependent programme is front-loaded**. From 6 h to 24 h:
  * HUVEC genes responding ≥2-fold fall from 1,068 to 512;
  * reproducibility across independent libraries falls from r 0.92 to 0.73;
  * the HGMEC response largely disappears (agreement with HUVEC r 0.63 → 0.31).
* If that holds in patients, IL-33 activity is an early event and late samples will under-read it. This may be why enrolment serum showed no IL-33 fingerprint. Early sampling plus recorded onset time is the fix.

**Pharmacodynamic pair: 24 h after the first dose, paired with baseline.** The serum-measurable response proteins are still strongly induced at 24 h in vitro, and AX-1177 still suppresses them then (log2 vs isotype):

| Protein | Suppression at 24 h |
|---|---|
| CCL20 | −5.3 |
| G-CSF | −5.7 |
| CXCL6 | −7.1 |
| CXCL1 | −5.5 |
| IL-8 | −5.3 |
| OPG | −2.1 |

**In vitro follow-up: 6 h as the primary readout** (largest, most reproducible and most completely neutralised signal), with 24 h as secondary.

### 4.6 Plan and decision gates

**Stage 0: close the gaps in data we already own (≈2–4 weeks; no new samples)**

* **0a. Retrieve the ~100 Olink assays that were analysed but not delivered,** with their LOD and QC flags, IL-33 first. This is the cheapest item that could change the decision.
* **0b. Re-fit the RNA-seq per cell line** from the archived counts, with library-level QC.
  * Add an IL-33 vs isotype contrast for HGMEC.
  * Rebuild the PD panel on stable statistics.
* **0c. Re-analyse Olink at patient level.**
  * Odds ratios per SD.
  * sST2, IL-6 and NEWS2 in one joint model.
  * A per-patient AX-1177-reversible endothelial score, tested against outcome and against sST2.
* **0d. Re-score the IHC** with a second, blinded reader, digital nuclear quantification, donor-level models and a defined scale.

**Stage 1: the decisive human-biology test (≈3 months; the gate for any further spend)**

* **1a. Banked enrolment serum (n = 100):** validated high-sensitivity IL-33 assay (free and total), clinical-grade sST2 and the PD panel.
* **1b. The 22 banked post-mortem lung RNAs already linked to the IHC blocks** (9 COVID-positive pneumonia, 9 COVID-negative pneumonia, 4 non-pneumonia): targeted expression of the AX-1177-reversible endothelial programme, related to nuclear IL-33 and neutrophil scores.
* **1c. One non-COVID viral-LRTD cohort** (RSV, influenza or hMPV; vaccinated era), sampled at admission (≤ 24 h) and at 24–72 h, with onset time recorded.

**Go criteria (proposed; fix them before unblinding). All must be met:**
* IL-33, or the IL-33-specific score, is measurable in most patients.
* It is associated with the composite endpoint independently of age, sex, NEWS2 and IL-6 (for example, OR per SD ≥ 1.5 with the 95% CI excluding 1).
* The association is reproduced in the non-COVID viral cohort.
* The programme is elevated in pneumonia lung RNA.

**If the criteria are not met, close the asset.**

**Stage 2: mechanism gaps (≈3 months; run in parallel only if Stage 0 is encouraging)**
* Primary human lung microvascular endothelium (≥ 3 donors) and primary airway epithelium at air–liquid interface, with and without virus.
* Reduced and oxidised IL-33.
* IL-33 concentration–response spanning the levels found in Stage 1.
* AX-1177 dose–response (IC50 and IC90), with and without pre-incubation.
* **TNF and IL-1β comparator arms**, to separate IL-33-specific genes from generic NF-κB genes.
* 6 h primary readout.
* Antiviral safety: the interferon module and viral replication, with and without AX-1177.
* Per-cell-line statistical models.

**Stage 3: only if Stage 1 passes**
* In vivo proof of concept in an infection model.
* Then a biomarker-anchored Phase 1b/2a in hospitalised severe pneumonia:
  * sST2-high enrichment;
  * PD sampling at baseline and 24 h post-dose;
  * target-engagement assay;
  * viral-kinetics safety monitoring.

### 4.7 What would change my recommendation

* **IL-33 is among the withheld Olink assays, above LOD in most patients, and associated with outcome independently of NEWS2** (and not simply tracking IL-6 or sST2). Two of the withheld assays had p ≤ 0.002; we do not know which.
* **The AX-1177-reversible programme is demonstrably active in diseased lung RNA.**
* **Either of those two findings is replicated in a non-COVID viral cohort.**

Either of the first two would justify reopening at Stage 1. All three would justify clinical planning.

---

## 5. What I considered and ruled out

| Considered | Outcome | Reason (our data) |
|---|---|---|
| Keep in viral LRTD as currently scoped | Ruled out | No IL-33-specific human signal; only pre-vaccination COVID data |
| Read sST2 as evidence of IL-33 activity or target engagement | Ruled out | IL-1-family decoys co-rise; IL-33 → ST2 induction in vitro is small, statistically unreliable and absent in HGMEC; sST2 is a decoy |
| Read the severe-COVID serum signature as an IL-33 signature | Ruled out | No enrichment (OR 0.99–1.26, p ≥ 0.29); the strongest IL-33 responders are not prognostic |
| IL-33 is up-regulated in COVID lungs | Ruled out | No group difference; ceiling effect; the only trend is downward |
| A COVID-specific eosinophil or type-2 component | Ruled out | IL-5Rα COVID+ vs COVID− pneumonia is p = 0.025 if blocks are counted as independent, but p = 0.49 per donor. Serum IL-5, eotaxins, TARC and tryptase are flat. |
| Off-target activity of AX-1177 | Ruled out | Antibody-alone changes sit at the vehicle-vs-vehicle noise floor; no reproducible gene |
| Repurpose to COPD or asthma | Not supported by our data | No airway-epithelial IL-33 experiments. IHC IL-33 and eosinophil scores do not differ by donor COPD or asthma notes (11 and 6 donors; all p ≥ 0.15). It would be a literature-led bet. |
| Repurpose to kidney (glomerular endothelium) | Not supported | HGMEC responds at 6 h but the response is transient; no renal disease data; serum KIM-1 weak (OR 1.66, adj.p 0.11) |
| Thrombo-inflammation or coagulopathy | Not supported | IL-33 induces tissue factor 5.6 log2 in vitro, but serum tissue factor is borderline (adj.p 0.051) and it is a generic NF-κB product |
| Oncology (A549 / MCF7) | Not supported | These lines were specificity controls: no IL-33 arm, antibody inert |
| Oxidised IL-33 / RAGE–EGFR epithelial axis as support | Not testable | No oxidised-IL-33 or epithelial IL-33 arms; serum RAGE p = 0.055, EGFR p = 0.78 |
| Early or outpatient viral LRTD (in vitro kinetics suggest an early window) | Not proposable | No data in that population; kept as a hypothesis for Stage 1c timing |
| Take adj.P lists from the single-model fit at face value | Ruled out | Gene-level statistics are distorted (§6); I used effect sizes plus reproduction in separate libraries |
| Rank serum markers by OR size | Ruled out | OR "per log unit" depends on each assay's scale (e.g., CSF-1 OR 90, CI 4–1,933). I ranked by p and checked consistency across panels. |
| Analyse IHC by block | Ruled out | Pseudo-replication: 3 donors supply 24 of the 49 COVID-positive blocks. I analysed per donor. |

---

## 6. Data-quality findings the committee should know

| Issue | Evidence | Impact | How I handled it |
|---|---|---|---|
| **Serum file is a subset of what was analysed** | Reconstructed BH adjustment uses **N = 1,194** tests, not the 1,094 delivered; implied ranks match to integers. About 100 analysed assays are missing: ~2 with p ≤ 0.002, ~16 with p < 0.05. | The drug's own target (IL-33) may have been measured and withheld, against the annex statement "BH across all assays in the delivery". | Flagged. Retrieval is step 0a. |
| IL-33, TSLP and IL-1α absent | 15 of 92 Inflammation-panel assays missing | No patient IL-33 data | No IL-33 claims made; assay development in Stage 1 |
| Single statistical model across 4 very different cell types | 73 large endothelial effects have implausible standard errors: E-selectin log2FC 11.2 but t = 1.26; CXCL1 standard error ≈ 1,150 log2 units. Conversely, trivial antibody-alone effects reach extreme significance: AKR1C2 log2FC 0.11, t = 169, p = 10⁻⁹⁹. | Gene-level p-values and DE counts are unreliable, in both directions | Conclusions use effect sizes checked across separate libraries, cell types and timepoints. Refit per line (step 0b). |
| AveExpr averaged over all 114 libraries | Annex definition | Cannot say whether a gene (e.g., ST2) is expressed in a particular cell type | Not used for cell-type claims |
| HGMEC lacks a vehicle arm; 24 h estimates inconsistent | 1,032 vs 269 reversed genes, 45 overlapping | HGMEC IL-33 effect inferred; 24 h unreliable | HGMEC used at 6 h only |
| One donor per endothelial type; passage 2 vs 5; one concentration; IL-33red only; no pre-incubation; epithelial lines never given IL-33; DMSO vehicle irrelevant to an antibody | Annex | No potency, donor-variability or epithelial/IL-33ox conclusions possible. Comparisons vs DMSO or PBS are not specificity tests. | NIP228 (isotype) used as the comparator; gaps go to Stage 2 |
| `mmc5` sheets "6h" and "24h" are identical | Each holds all 24 contrasts for both timepoints | Sheet names are misleading | Keyed on the `Comparison` column |
| `mmc4` labels | Sheet says "Vehicle"; `Comparison` says "Nontreated" | Minor | Assumed to be the same arm |
| Olink effect scale undefined | NPX is already log2; "log transformed, OR per log unit" | OR sizes not comparable across assays; cannot set cut-offs | Ranked by p; ORs per SD requested (step 0c) |
| Olink per-group columns undocumented | Multiples of 1/56 and 1/44 | Implies 44 events in 100; most likely fraction below LOD | Inferred and stated as such |
| 27 proteins measured on more than one panel | e.g., IL-6 on 4 panels | BH run over non-independent tests. Useful reproducibility check: IL-6 OR 2.07–2.31 across panels. | Collapsed to one row per protein for enrichment |
| IHC structure | Donor fields only on first block; notes on later blocks for donors 2040 and 2045; 3 donors = 24 of 49 COVID-positive blocks; scores of 5.5 on a 0–5 scale (53% of endothelial blocks); single reader; "ND" entries; donor 1905 SARS-CoV-2 status missing; all donors white, aged 64–98 | Pseudo-replication; ceiling; ordinal data only | Forward-filled donor fields; donor-level, rank-based tests |
| Clinical scope | Single centre, pre-vaccination, COVID-only; time from symptom onset not recorded | Cannot generalise to viral LRTD | Drives the recommendation and Stage 1c |

---

## 7. Methods (brief) and files

**Transcriptomics**
* Contrasts were pivoted from `mmc4` and `mmc5`.
* IL-33-responsive genes: BH adj.p < 0.05 and |log2FC| ≥ 1 in IL-33 vs vehicle.
* Neutralisation = 1 − (AX-1177+IL-33 vs vehicle) / (IL-33 vs vehicle).
* Replication: IL-33 vs vehicle compared with −(AX-1177+IL-33 vs isotype+IL-33), which use separate groups of libraries.
* HGMEC response inferred from reversal.
* Specificity: AX-1177 vs isotype compared with a vehicle-vs-vehicle noise floor derived from the epithelial contrasts.

**Serum**
* Assay names mapped to gene symbols (`olink_map.py`) and collapsed to one row per protein.
* Enrichment of the in-vitro IL-33 programme among outcome-associated proteins by Fisher and Mann–Whitney tests.
* BH denominator reconstructed from adj.p/p ratios.

**IHC**
* Donor-level fields forward-filled; block scores averaged per donor.
* Kruskal–Wallis and Mann–Whitney tests, Spearman correlations, and age-adjusted rank regression.

**Files**
* Scripts `00`–`04` regenerate every number here.
* Tables: `tables/T1`–`T15`.
* Figures: `figures/Fig1`–`Fig6`.
* `AX-1177_audit_tables.xlsx` bundles the key tables.
