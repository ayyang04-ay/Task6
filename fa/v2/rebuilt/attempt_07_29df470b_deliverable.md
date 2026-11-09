---
title: "AX-1177 (anti-IL-33 mAb): portfolio audit recommendation and evidence dossier"
subtitle: "Based only on the AX-1177 data package: methods annex, mmc2 (serum Olink), mmc3 (post-mortem lung IHC), mmc4/mmc5 (cell RNA-seq contrasts)"
---

# 1. Recommendation

**Keep AX-1177, but only as a gated asset with a new scope. Stop running it as a viral-LRTD development programme in its current form.**

| | |
|---|---|
| **Keep** | The molecule, plus one testable hypothesis: *AX-1177 blocks IL-33-driven endothelial activation, and that activation contributes to poor outcome in hospitalised viral pneumonia.* |
| **Stop now** | The all-comer viral-LRTD positioning, and any clinical-development spend until a decision package of about 6 months reads out. Most of that package runs on samples and data we already hold (Section 7). |
| **Kill rule** | Drop the asset if the pre-agreed criteria in Section 7 fail. A ready-to-use drop statement is in Section 5. |
| **Why not advance** | We have shown that the drug works on its target in cell culture. We have not shown that IL-33 drives disease in patients. |
| **Why not drop today** | The evidence against the asset is mostly missing evidence, not negative evidence. The one missing result that matters most (IL-33 levels in patient serum) was generated and then left out of the delivery. The decisive experiments are cheap, quick and use material we already have. |

**Evidence scorecard**

| Question the committee will ask | What our data show | Strength |
|---|---|---|
| Does AX-1177 neutralise IL-33? | Blocks about 95% of the IL-33-induced transcriptional programme at 6 h and about 80–85% at 24 h, compared with the isotype control, in HUVEC. It also suppresses the same core programme in glomerular endothelium (HGMEC) | **Strong** (but one concentration, in vitro only) |
| Is it specific / clean? | Given alone, it has no effect on the IL-33 signature (at most ±0.11 log2) and no coherent off-target effect in any of 4 cell types at 2 timepoints | **Strong** (transcriptome level) |
| Is the target present in lung? | IL-33 is high in endothelium and basal epithelium in all 31 donor lungs | Moderate (single reader, semi-quantitative) |
| Is IL-33 raised or released in disease? | Tissue IL-33 is not increased in COVID-19. Endothelial IL-33 is, if anything, lower (p≈0.05). Serum IL-33 is **missing from the delivery** | **Weak / absent** |
| Is the pathway linked to patient outcome? | sST2 (IL-33 decoy receptor) ranks #2 of 1,094 serum assays. Ten proteins that IL-33 induces and AX-1177 reverses in vitro are prognostic | Moderate, but not specific to IL-33 |
| Does the AX-1177-sensitive programme *specifically* track outcome? | No. It makes up 17% of outcome-associated proteins against an 18% background (OR 1.03, p=1.0) | **Negative** (weak test) |
| Does it work when given after IL-33, in lung cells, in epithelium, or against oxidised IL-33? | Never tested | **Absent** |
| Do the findings hold beyond pre-vaccination COVID-19? | No data | **Absent** |

# 2. The case for keeping it (strongest evidence first)

## 2.1 AX-1177 is a clean, functional IL-33 neutraliser in human endothelium (mmc4, mmc5; Fig 1, Fig 4)

- **IL-33red (30 ng/mL) strongly activates HUVEC through NF-κB.**
  - 4,031 genes change at 6 h and 1,836 at 24 h (FDR<0.05).
  - The top pathway is Hallmark *TNFα signalling via NF-κB* (76 of 173 genes; FDR 2×10⁻⁷⁷). IFN-γ/α and IL-6/JAK/STAT3 programmes are also enriched.
  - In concrete terms:
    - neutrophil-recruiting chemokines: CXCL1/2/3/5/6/8, +5 to +9 log2
    - GM-CSF (CSF2) +10.3 and G-CSF (CSF3) +8.3
    - adhesion molecules: E-selectin +11.2, VCAM-1 +8.7, ICAM-1 +6.0
    - IL-6 +5.8, plus IL-1β and TNF
    - a procoagulant shift: tissue factor (F3) +5.6, PAI-1 +1.7, thrombomodulin −1.0
- **AX-1177 neutralises the response.** At 10 µg/mL, added at the same time as IL-33, it reverses:
  - about **95% at 6 h**: per-gene median 97–100%; correlation with the IL-33 effect r = −0.94 across 3,393 expressed IL-33-responsive genes;
  - about **80–85% at 24 h**: per-gene median 91–93%.

  Both figures are measured against the isotype-matched arm, using wells independent of those that defined the IL-33 response.
- **Microvascular endothelium.** In glomerular microvascular endothelium (HGMEC), AX-1177 suppresses the same core programme at 6 h: the 82-gene core signature falls by a mean of −2.05 log2, against −3.03 in HUVEC. The NF-κB core is included (NFKBIA, TNFAIP3, TRAF1, RELB, CXCL2/3).
- **No effect on its own.** AX-1177 without IL-33 does nothing transcriptionally in HUVEC, HGMEC, A549 or MCF7 at 6 or 24 h:
  - the core IL-33 signature moves by at most ±0.11 log2;
  - the 14–73 nominally significant genes per contrast are low-count lncRNAs/pseudogenes or changes below 0.2 log2, with no pathway coherence;
  - only 0–9 genes per contrast have |log2FC|>1 and are expressed.

## 2.2 The IL-33 pathway sits near the top of the patient severity proteome (mmc2; Fig 2, Table 1)

- **The cohort.** 100 patients hospitalised with COVID-19; 44 reached the 30-day composite of ICU admission, invasive ventilation or death. Models are adjusted for age, sex and NEWS2 at enrolment.
- **sST2, the IL-33 decoy receptor, ranks #2 of 1,094 assays:** OR 3.02 per log unit (95% CI 1.83–5.01), p=1.7×10⁻⁵, adjusted p=0.0075. That is about 2.4 per SD.
- **Ten proteins are both IL-33-inducible / AX-1177-reversible in endothelium and prognostic at FDR<0.05:**
  - sST2
  - PTX3
  - IL-6 (significant on all 4 panels that carry it)
  - OPG (on both panels that carry it)
  - IL-18R1
  - MCP-3
  - CCL20
  - IL-8
  - CSF-1
  - IL-1β

  Each has an approximate OR of 1.7–2.4 per SD.

## 2.3 The target is present where the mechanism would act (mmc3; Fig 3)

- **Present in every donor.** IL-33 is expressed in endothelium and bronchial/bronchiolar basal epithelium in all 31 donor lungs.
- **Lower in COVID-19 endothelium.** Donor-level means:
  - endothelium 4.8 vs 5.25 (p=0.052);
  - vascular smooth muscle 2.5 vs 3.2 (p=0.068).
- **Lowest where neutrophils are highest:** ρ = −0.43, p = 0.016; age-adjusted p = 0.035.
- **How to read this.** Losing nuclear IL-33 is what you expect when an alarmin is released or when endothelium is activated. In our own cells, IL-33 lowered endothelial *IL33* mRNA at 24 h (−0.89 log2, nominal p = 0.055), and AX-1177 prevented this. This is consistent with IL-33 activity in COVID-19 lungs; it does not prove it.

## 2.4 The open questions are cheap to close

Everything needed for the go/no-go decision is already in-house:

- the 100 retained sera;
- FFPE blocks from 31 donors;
- lung tissue RNA (IDs recorded for 22 donors, and probably all 31);
- the archived RNA-seq count matrices;
- the full Olink output (1,194 assays analysed, of which 100, including IL-33, were not delivered).

# 3. What the data do not support (why we should not advance as-is)

1. **There is no patient evidence on IL-33 itself.**
   - IL-33 is on the Olink Inflammation panel, but its result is not in the delivery. The 15 missing Inflammation assays are the usual low-detectability set: IL-33, TSLP, IL-4, IL-5, IL-13, IL-1α, LIF and others.
   - The reported adjusted p-values can only be reproduced with a 1,194-test family. So 100 analysed assays are missing, and rank reconstruction shows at least 4 of them were at FDR<0.05.
2. **The AX-1177-sensitive programme does not specifically track outcome.**
   - 17 of 98 IL-33-induced, AX-1177-reversed proteins are prognostic (17%), against 141 of 792 non-regulated proteins (18%). Fisher OR 1.03, p = 1.0.
   - This holds across 5 alternative definitions (OR 0.67–1.45, all p>0.1). The rank correlation between in vitro induction and serum association is only ρ = 0.15.
   - Severity shows up as a global shift: 82% of proteins have OR>1, and 35% have nominal p<0.05. The strongest signals are HGF, HDGF, neutrophil/myeloid activation markers (PRTN3, CTSC, FCAR, IL-1R2, CLEC5A) and intracellular proteins that leak into serum (NPM1, PXN, CALR, PRDX1/6).
   - Several of the strongest IL-33 targets in vitro have no association with outcome at all: CXCL6 (OR 1.02), CXCL5 (1.17), G-CSF (1.25), VCAM-1 (1.28), 4-1BB (1.09).
3. **Tissue IL-33 is constitutive and not increased in COVID-19.**
   - Basal epithelium: COVID+ 4.4 vs COVID− 4.5, p = 0.76.
   - The IHC has almost no dynamic range: 53% of endothelial blocks are scored at the top of the scale ("5+").
4. **The pharmacology package is thin.**
   - Only one concentration was tested, at about 41-fold molar excess (≈68 nM IgG vs ≈1.7 nM IL-33).
   - The antibody was always added at the same time as IL-33, never afterwards. The clinical setting is the reverse: patients present after IL-33 has been released.
   - Only reduced IL-33 was tested, despite the claim that AX-1177 binds both forms.
   - There is one donor per endothelial type, and no lung endothelium.
   - No epithelial cell was ever challenged with IL-33. The A549/MCF7 arms only test antibody alone, and MCF7 is a breast line.
5. **The patient data are narrow.** They come from one pre-vaccination, single-centre SARS-CoV-2 cohort, sampled once at enrolment. There are no data on RSV, influenza or other viral LRTD.

# 4. Anticipated challenges and our answers

| Challenge | Answer grounded in our data |
|---|---|
| "You have no human evidence that IL-33 matters." | Correct for IL-33 itself, and that result exists but was not delivered; Stage 0 retrieves it. The indirect evidence points the right way: sST2 is #2 of 1,094, and ten IL-33-inducible, AX-1177-reversible endothelial proteins are prognostic. The decisive test (Stage 1b) runs on the same 100 sera. |
| "sST2 is a generic stress marker." | Agreed. That is why we use it only to enrich patients, not as proof of mechanism. The proof comes from measuring IL-33 itself and from the serum-transfer bioassay. |
| "The IL-33 signature isn't enriched in the severity proteome." | True, and we report it. With n=100 and a global proteome shift, enrichment is a weak test: it would miss a real contribution that is masked by generic inflammation. It does rule out IL-33 as the *dominant* driver of that proteome, which is why we do not recommend advancing. |
| "Tissue IL-33 isn't up in COVID-19." | IL-33 is a stored nuclear alarmin. The relevant question is release, not expression. The direction we see (lower in endothelium, tracking neutrophils) fits release or activation. It is not proof. |
| "Canonical markers (E-selectin, VCAM-1, IL-8) aren't significant in your RNA-seq." | That is a statistical artefact of the delivered model: their standard errors are impossible (SE 4–1,155 log2 units). Their effects are large and replicate in independent wells: for example, E-selectin is +11.2 with IL-33 and −11.0 with AX-1177 vs isotype in HUVEC, and −8.7 in HGMEC. |
| "Why keep something this unproven?" | Holding it costs little, the experiments that would settle it are defined, and the kill criteria are agreed in advance. |

# 5. If the committee drops AX-1177: what we are dropping and why

> *"We are dropping a well-behaved IL-33 neutraliser whose only demonstrated activity is blocking IL-33-driven endothelial activation in vitro. Its efficacy programme rested on an untested hypothesis that this activation drives severe viral pneumonia. We are not dropping a validated viral-LRTD asset. Our patient data never measured the target. The programme the drug blocks does not stand out in the patients' severity proteome. IL-33 in tissue is not disease-specific. And we have no data in lung cells, in epithelium, with oxidised IL-33, with treatment after exposure, or in any viral LRTD other than pre-vaccination COVID-19. The option we give up is an endothelial-activation (sST2-high) endotype of hospitalised pneumonia."*

# 6. Forward view: which indication do our data point at?

**Answer: an endothelial-activation endotype of severe, hospitalised viral pneumonia.** This is *not* a new organ or disease, and *not* viral LRTD as currently defined by pathogen.

- **What AX-1177 demonstrably blocks is vascular, not airway biology.** It is an IL-33-driven endothelial programme in two endothelial beds: neutrophil chemokines, GM-/G-CSF, adhesion molecules and a procoagulant shift.
- **The patient correlates that connect to it are systemic endothelial and inflammatory proteins.** sST2, OPG, CCL20, IL-6 and PTX3, measured at hospital enrolment, are prognostic in severe COVID-19.
- **The tissue fits the same picture.** Endothelial IL-33 is lost in COVID-19 lungs in step with neutrophil infiltration. Thromboemboli appear in 4 of 16 COVID-19 donors and 0 of 15 controls (p=0.10, descriptive only).
- **Best-supported target population:** hospitalised patients with viral pneumonia and systemic endothelial activation at admission (sST2-high, with OPG/CCL20 as supporting markers), treated early in the hospital course.
  - COVID-19 is the only aetiology with patient data.
  - Influenza/RSV pneumonia, and all-cause pneumonia/ARDS, are hypotheses for the next cohort, not conclusions. The mechanism does not depend on the pathogen, and IL-33 staining is the same in COVID-negative pneumonia.
- **Timing matters.** In vitro, the IL-33 programme is front-loaded: 24 h effects are about 30% the size of 6 h effects. AX-1177 was only ever tested when present at the moment of exposure. The clinical window is therefore probably early, and giving the drug after exposure is the most important untested condition.

**Alternative indications we examined and did not find support for** (details in Section 9): COPD/asthma (type-2 or epithelial), kidney/AKI, cardiovascular disease, mild or outpatient LRTD, and thrombo-inflammation as a stand-alone indication.

# 7. What the next studies must establish (decision package)

**Stage 0: data provenance (weeks)**

- Retrieve the full 1,194-assay Olink output, including IL-33, with LOD/QC flags.
  - Confirm whether NPX (already log2) was log-transformed a second time.
  - Re-analyse per unique protein with standardised ORs.
  - Add adjustment for renal function, leukocyte counts, steroid use and time from symptom onset.
- Re-fit the RNA-seq per cell line from the archived counts.
  - Check library identity.
  - Confirm SELE, VCAM1, CXCL8, PTX3 and IL1RL1 statistically.
- Re-adjudicate the IHC disease categories against the autopsy diagnoses. Add a blinded second reader and analyse at donor level.

**Stage 1: does IL-33 act in patients? (0–4 months, existing samples)**

- **1a. Target presence.** Measure IL-33 in the 100 retained sera with a validated high-sensitivity assay. It should distinguish free IL-33 from IL-33/sST2 complex, and reduced from oxidised IL-33 if possible.
- **1b. Serum-transfer bioassay (the decisive experiment).**
  - Expose human lung microvascular endothelial cells (≥3 donors) to each patient serum, with AX-1177 or isotype.
  - Read out at 6 h:
    - transcripts: CSF2, CCL20, CXCL6, CSF3, SELE, VCAM1, TNFRSF11B, IL6, NFKBIA, TNFAIP3;
    - secreted proteins: OPG, CCL20, IL-6, GM-CSF.
  - The question: what share of serum-induced endothelial activation is AX-1177-sensitive, and is that share larger in sera from patients with events or high sST2?
- **1c. Tissue.**
  - Score the IL-33 endothelial signature in the lung tissue RNA.
  - Stain E-selectin, VCAM-1 and ST2 by IHC on the same blocks.

**Stage 2: pharmacology gaps (2–6 months, in parallel)**

- Concentration–response against IL-33red and IL-33ox, to get IC50/IC90.
- Therapeutic-mode addition: AX-1177 added 1, 3 and 6 h after IL-33.
- Lung microvascular endothelium and primary bronchial epithelium (air–liquid interface) challenged with IL-33red/ox. This would be our first epithelial efficacy data.
- At least 3 donors per cell type, with per-cell-line statistics.

**Proposed decision criteria (thresholds to be agreed by the committee)**

- **GO** to a prospective biomarker cohort and Ph2a design only if all three hold:
  - (i) IL-33, or the IL-33/sST2 complex, is quantifiable and associated with outcome or with the endothelial PD panel;
  - (ii) AX-1177 removes a meaningful share (e.g. ≥30%) of serum-induced endothelial activation in high-risk sera;
  - (iii) activity is retained in lung microvascular endothelium and with delayed addition, at achievable concentrations.
- **KILL** if (i) and (ii) both fail, or if (iii) fails.
- **Stage 3 (only after GO):**
  - A contemporary, multi-pathogen, vaccinated-era cohort of hospitalised viral pneumonia: COVID-19, influenza and RSV.
  - Serial sampling at enrolment (pre-dose), 24 h, 72 h and day 7, to replicate sST2 and the PD panel and define kinetics.
  - Then a Ph2a with sST2 enrichment and a CCL20/OPG PD readout.

# 8. Biomarkers, sampling timepoint and roles in patients

**Sampling timepoints**

- **Mechanistic and ex vivo work: 6 h.** This is the peak of the IL-33 response (4,031 vs 1,836 genes), where neutralisation is most complete (~95% vs ~80–85%) and the isotype control is inert. At 24 h the isotype alone blunts the IL-33 response by 13–20%.
- **Patients, for enrichment: at enrolment, before dosing.** All of our prognostic evidence comes from this single timepoint.
- **Patients, for PD:**
  - 24 h after the dose is the primary timepoint, with 72 h as secondary.
  - Day ≥7 alone is unlikely to capture an IL-33-blocking effect, given how front-loaded the in vitro kinetics are.
  - In vivo kinetics are unknown and must be defined in the Stage 3 cohort.

**Table 1. Candidate biomarkers**

"Approx. OR/SD" is the approximate per-SD odds ratio. "Spread" is the between-patient SD in log units: a larger spread makes a marker easier to use as PD. "In vitro" gives IL-33 vs vehicle and then AX-1177 vs isotype, both in HUVEC at 6 h.

| Marker | Serum OR / log unit (95% CI); adj p | Approx. OR/SD; spread | In vitro (log2FC) | Can go into patients? Role |
|---|---|---|---|---|
| **sST2** | 3.02 (1.83–5.01); 0.0075 | 2.4; 0.78 | +1.6 / −1.7 (p-value unusable) | **Yes. Enrichment/stratifier at enrolment.** Not PD, not target engagement. High sST2 may also mean IL-33 is already sequestered, so read it together with free IL-33 |
| **CCL20** | 1.83 (1.28–2.61); 0.020 | 2.0; **1.11** | +9.2 / −9.8 (24 h +5.6 / −5.3; HGMEC −5.6) | **Yes. Lead PD marker:** largest dynamic range in vitro and in serum |
| **OPG** | 6.77 (2.47–18.6); 0.014 (second panel 0.020) | 2.1; 0.39 | +4.8 / −5.0 (24 h +2.4 / −2.1; HGMEC −1.9) | **Yes. Endothelial-origin PD companion.** Narrow serum range, so it needs larger n |
| MCP-3, IL-18R1 | 1.72; 0.020 / 6.07; 0.018 | ~2.0; 1.25 / 0.39 | +2.2 / −5.0 and +3.6 / −3.5 | Yes. PD panel members (MCP-3 induced early only) |
| IL-6, IL-8, IL-1β | 2.14 / 2.23 / 2.45; ≤0.046 | 1.7–2.2 | +5.8 / −6.0, +8.2 / −8.4, +3.6 / −4.0 | Yes, but **supportive only.** Not IL-33-specific, and IL-6 is directly altered by standard of care (dexamethasone, tocilizumab) |
| CSF-1, PTX3 | 90 / 11.6 (narrow ranges); ≤0.037 | 1.8 / 2.2; 0.13 / 0.32 | +2.9 / −3.0, +2.2 / −2.3 | Exploratory only: CSF-1 range is too narrow; PTX3 in vitro p-values are unusable |
| HGF (top hit), HDGF, ANGPT2, vWF | 4.99 / 2.74 / 2.21 / 3.86 | 1.7–2.6 | not IL-33-regulated | **Prognostic covariates only. Do not use as AX-1177 PD** |
| GM-CSF, G-CSF, CXCL6, E-selectin, VCAM-1 (mRNA/protein) | not prognostic / not measured (E-selectin adj p 0.09) | – | +8 to +11 / fully reversed | **Not for patients yet.** Ex vivo bioassay readouts at 6 h |
| **IL-33 (free / total / sST2-complexed)** | not delivered | – | – | **Must be developed.** Target presence, target engagement and patient selection |
| IL-33 IHC | – | – | – | No: constitutive, at the scale ceiling, needs tissue |

Full numbers are in `tables/T1_biomarker_candidates.csv`. All 1,094 assays are annotated with the in vitro data in `tables/T3_serum_proteome_x_invitro_bridge.csv`.

# 9. What was considered and ruled out

**Portfolio options**

| Option | Verdict | Why |
|---|---|---|
| Advance in all-comer viral LRTD | Ruled out | IL-33 was never measured in patients. The AX-1177-sensitive programme is not enriched among outcome proteins. The cohort is pre-vaccination and COVID-only. There is no lung or epithelial pharmacology |
| Drop now | Ruled out for now | Pharmacology is clean. There is a pathway-proximal prognostic signal. The decisive experiments are cheap, and the key result already exists |
| Repurpose to COPD/asthma (type-2/epithelial) | Not supported | No epithelial IL-33 challenge and no IL-33ox data. Tissue IL-33 is unrelated to eosinophil, basophil or mast-cell scores (ρ −0.17 to +0.08) and to COPD/asthma history (p 0.21–0.88). Type-2 serum markers are flat (IL-5 OR 1.00, CCL11 1.08/0.98, CCL24 0.92, CCL17 0.85) and IL-4/5/13/TSLP are not detectable/delivered |
| Repurpose to kidney/AKI | Not supported | The HGMEC response is about 2/3 of HUVEC's at 6 h and minimal at 24 h. There is no HGMEC vehicle arm, so the IL-33 response there is unmeasured. KIM-1 adj p 0.11, and there are no renal outcomes |
| Cardiovascular (sST2 is a heart-failure marker) | Not supported | A prognostic decoy receptor is not evidence that blocking IL-33 helps. IL-33/ST2L signalling is generally considered cardioprotective (general knowledge, not our data), so this is a potential liability |
| Thrombo-inflammation as a stand-alone indication | Folded into the main hypothesis | The in vitro procoagulant shift is reversed by AX-1177, but serum coagulation markers are weak (PAI-1 p=0.048, adj 0.15; vWF adj 0.05 and not IL-33-regulated) and the pathology is descriptive |
| Mild/outpatient LRTD or prophylaxis | No data | All patient and tissue data come from hospitalised or fatal disease |

**Analytical choices and traps avoided**

| Choice / trap | Why we rejected it |
|---|---|
| Using delivered gene-level p-values for endothelial activation genes | 135 genes have impossible SEs because of the single model pooled across four cell types. We used effect sizes replicated in independent wells instead |
| Using AveExpr to judge expression | It is averaged over all 114 libraries. CSF2 has AveExpr −3.2 but rises +10.3 log2 with IL-33 |
| Treating the "6h"/"24h" sheets of mmc5 as timepoints | Both sheets contain all 24 contrasts, with identical values |
| Reading the A549/MCF7 antibody-alone "DEGs" as off-target effects | They are low-count noise and tiny fold changes with inflated t values |
| Using "AX-1177+IL-33 vs IL-33" as the neutralisation measure | The isotype itself blunts the response at 24 h, so we used the isotype-matched contrast |
| Counting 178 significant assays | Duplicates across panels inflate this; the true figure is 169 unique proteins |
| Ranking serum proteins by OR | ORs are per log unit and depend on each protein's spread (CSF-1 OR 90 is a narrow range, not a huge effect). We ranked by z/p |
| Block-level IHC statistics | This is pseudo-replication: endothelial IL-33 p=0.017 at block level becomes 0.052 at donor level |
| Taking IHC disease categories at face value | 7 of 15 COVID-negative donors are mislabelled relative to their own autopsy diagnoses |
| HGF as a PD marker | It is the top prognostic protein, but it is not IL-33-regulated in vitro |
| sST2 as target-engagement or PD evidence | It is a decoy receptor made by many cell types. We use it for enrichment only |

# 10. Data-integrity findings the committee should know

The full log is in `tables/T2_data_integrity_audit_log.csv`. Headline items:

1. **mmc2 omits 100 analysed assays, including the drug's own target (IL-33).** The adjusted p-values imply a 1,194-test family, not the 1,094 delivered. At least 4 missing assays were FDR<0.05. The annex's statement that BH was applied "across all assays in the delivery" is therefore inaccurate.
2. **mmc4/mmc5 come from one limma model across HUVEC, HGMEC, A549 and MCF7.**
   - 135 genes have implausible SEs, up to 16,536 log2 units. These are cell-identity genes plus canonical IL-33 targets, so their p-values cannot be used.
   - Tiny fold changes carry absurd t values, e.g. AKR1C2 0.11 log2 with t=169.
   - AveExpr and the low-expression filter span all 114 libraries.
   - Our conclusions rely on effect sizes replicated in independent wells. The count matrices need per-cell-line re-fits.
3. **mmc5's "6h" and "24h" sheets are duplicates of each other.** Each contains both timepoints, and the "6h" sheet is padded to Excel's row limit.
4. **The experimental design has gaps.**
   - No vehicle arm in HGMEC.
   - No IL-33 arm in the epithelial lines.
   - One donor per primary cell type.
   - One antibody concentration, added only concurrently.
   - The isotype is not inert at 24 h.
   - Some ubiquitous genes are absent from the delivered gene set (e.g. LTBR, THOP1, OAS1).
5. **mmc2 has several further problems.**
   - 27 proteins are duplicated across panels: 1,094 assays = 1,063 proteins.
   - ORs per log unit cannot be compared across proteins.
   - The log transform of NPX is ambiguous.
   - The columns `composite_endpoint_0/1` are undocumented. They appear to be below-LOD fractions for 56 non-events and 44 events.
   - The whole proteome shifts with severity, consistent with confounding (renal clearance, cell lysis during serum clotting) that was not adjusted for.
6. **mmc3 has several further problems.**
   - 3 donors supply 32% of blocks.
   - Disease categories contradict the autopsy text for 9 donors.
   - "5+" is coded 5.5, above the 0–5 scale.
   - Scores come from a single reader.
   - One donor is missing SARS-CoV-2 status.
   - Tissue-RNA IDs are missing for 9 donors.

# Appendix: how this analysis was done

**Transcriptomics**

- The 26 delivered contrasts were taken from mmc4 and mmc5. Duplicated sheets were collapsed by `Comparison`.
- Standard errors were derived as |logFC/t|.
- IL-33-responsive genes were defined in HUVEC (IL-33red vs vehicle, FDR<0.05).
- Neutralisation = (IL-33+isotype − IL-33+AX-1177) / (IL-33+isotype − vehicle). The isotype-arm response was derived additively from the single-model contrasts.
- Hallmark enrichment used Fisher tests (msigdbr).

**Serum**

- Olink assay names were mapped to gene symbols, and proteins measured on more than one panel were de-duplicated (keeping the best p per protein).
- Approximate per-SD ORs were calculated as exp(z/√(n·p·(1−p))) with n=100 and p=0.44.
- The BH family size was reconstructed from reported p/adjusted-p ratios.
- The in vitro–serum bridge used Fisher and Mann–Whitney tests plus Spearman correlation, over 5 alternative definitions of "IL-33-regulated".

**IHC**

- Scores were aggregated to donor means. COVID+ vs COVID− comparisons used Mann–Whitney tests, plus an age-adjusted OLS (also run on ranks).
- Disease categories were cross-checked manually against each donor's autopsy diagnosis list.

**Deliverables**

- Code: `code/`.
- Figures: `figures/Fig1`–`Fig4`.
- Tables: `tables/T1`–`T5`.
