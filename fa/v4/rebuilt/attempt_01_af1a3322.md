---
title: "AX-1177 (anti-IL-33 mAb): Portfolio Audit Brief"
subtitle: "Recommendation, defence, forward view and biomarker plan, based only on programme data"
---

**Evidence base.** This brief uses only the five delivered programme files: the methods annex, the HUVEC IL-33 RNA-seq file, the RNA-seq contrasts file, the serum proteomics file and the post-mortem lung file. No external literature or competitor data is used as evidence. Every number below was re-derived from those files, and the supporting tables are in `AX-1177_audit_supporting_tables.xlsx`. Compound_47 = AX-1177; IC119 = isotype control.

# 1. Recommendation

**KEEP AX-1177, but re-scoped and gated. Do not continue the programme as currently framed.**

| | Decision |
|---|---|
| **The molecule** | **Keep.** In human endothelial cells it neutralises reduced IL-33 signalling essentially completely and specifically. It has no transcriptional activity of its own in four cell types. |
| **The current thesis** ("severe lower respiratory viral infection") | **Stop as framed.** Our human data cover SARS-CoV-2 only. They show the IL-33 axis *tracks* severity, but not that IL-33 *drives* it. The most IL-33-specific outputs we block in vitro do not track severity in patients. |
| **Where the data point** | Hospitalised viral pneumonia, *before* critical illness, in patients with high IL-33-axis activity (sST2-high). Mechanistic hypothesis: **IL-33-driven endothelial thrombo-inflammation.** This is narrower than the current framing, and vascular rather than epithelial/type-2. |
| **Spend** | **Freeze IND-enabling spend.** Fund a time-boxed (about 6–9 months), mostly archive-based translational gate with pre-specified kill criteria (Section 6). **If the gate fails, terminate.** |

**Why not drop today.** The weakness is *absence* of evidence, not evidence of failure. The molecule works, and the pathway marker is among the strongest prognostic signals in our cohort. The decisive experiments mostly use material we already own: archived RNA-seq counts, 22 archived post-mortem lung RNAs, and the 100-patient serum cohort.

**Why not continue as-is.** Our data do not support the breadth of the current claim:

* SARS-CoV-2 only.
* The epithelial/oxidised-IL-33 mechanism was never tested.
* There is no efficacy model.
* Potency data are not in the delivered dataset.

# 2. What our data do and do not show

| # | Claim | Key numbers (our data) | Strength |
|---|---|---|---|
| 1 | AX-1177 neutralises reduced IL-33 (IL-33red) signalling in human endothelium | HUVEC: IL-33red changes 4,031 genes at 6 h and 1,836 at 24 h. For well-measured IL-33-responsive genes, residual IL-33 effect with AX-1177 present is a median **0% (IQR −5 to +8%) at 6 h** and 1% (−10 to +15%) at 24 h. All 36 genes induced >32-fold are significantly reversed (median 101%). Isotype effect is negligible (median \|log2FC\| 0.05). | **Strong** (in vitro; one concentration, single donor) |
| 2 | AX-1177 is inert without IL-33 | AX-1177 vs isotype in HUVEC, HGMEC, A549 and MCF7 at 6 and 24 h gives 21–73 "hits" per contrast, versus 269–4,239 in IL-33 contrasts. Of the 328 hits, 84% are low-count genes, 10% are <15% shifts and 6% are isolated genes, with no pathway enrichment (best Hallmark q = 0.40). AX-1177 alone does not move IL-33-responsive genes (median log2FC ≈ 0), so there is no basal IL-33 tone to block. | **Strong** (in vitro) |
| 3 | IL-33 drives a pro-inflammatory **and procoagulant** endothelial programme | Hallmark TNFα/NF-κB: 88/197 genes (q ≈ 10⁻¹⁰⁵). Effects at 6 h: GM-CSF +10.3, CCL20 +9.2, CXCL6 +9.4, G-CSF +8.3, TNF +7.9, IL-6 +5.8 log2. Procoagulant switch: **tissue factor +5.6, PAI-1 +1.7, thrombomodulin −1.0**, all reversed by AX-1177. | **Strong** in vitro, but a generic MyD88/NF-κB programme (IL-1/TNF comparators not run) |
| 4 | The microvasculature responds too, but less | HGMEC (no vehicle arm): AX-1177 changes 1,460 genes in IL-33-treated cells at 6 h, but only 269 at 24 h. Only 29% of HUVEC IL-33 genes are reversed in HGMEC at 6 h, and 6% at 24 h. | Moderate |
| 5 | IL-33-axis activation predicts progression in hospitalised COVID-19 | **sST2** (soluble IL-33 decoy receptor) ranks #2 of 1,094 proteins. OR 3.02 per log-unit (95% CI 1.83–5.01), p = 1.7×10⁻⁵, BH adj.p 0.0075, adjusted for age, sex and NEWS2. | **Moderate** (n = 100, single centre, one timepoint, prognostic not causal) |
| 6 | The AX-1177-reversible programme is what is active in severe patients | 21% of reversible genes are prognostic in serum vs 18% background (Fisher p = 0.33). Strongest IL-33 outputs are null: CXCL6 OR 1.02 (p = 0.95), G-CSF 1.25 (p = 0.23), CXCL5 1.17 (p = 0.52), TNFRSF9 1.09 (p = 0.68). | **Not shown** |
| 7 | IL-33 protein is present in human lung | Abundant in bronchial/bronchiolar basal epithelium and endothelium in all 31 donors | Shown |
| 8 | Lung IL-33 is altered by COVID-19, COPD or lung injury | COVID+ vs COVID− pneumonia (age-adjusted): p = 0.75 basal epithelium, 0.23 endothelium, 0.21 vascular smooth muscle. No association with COPD/emphysema, DAD or thrombosis. | **Not shown** |
| 9 | Efficacy in a disease model; oxidised-IL-33 / epithelial pharmacology; potency (IC₅₀) | Not in the delivered data. Epithelial lines were never given IL-33; there was no oxidised IL-33 arm; affinity/potency are held in the biologics file. | **No data** |

# 3. Anticipated challenges and answers

**"Your best human evidence is one prognostic protein in 100 patients. Why is that enough to keep?"**
It is not enough to advance, and we are not asking to advance. It is enough to justify a cheap, decisive test. Three things support that:

* sST2 is #2 of 1,094 proteins after adjusting for NEWS2, so it adds information beyond clinical severity at admission.
* It is the IL-33 pathway's own receptor.
* The technical platform is reproducible: 27 proteins measured on 2–4 panels agree closely, e.g. IL-6 OR 2.07–2.31 on four panels.

**"sST2 rises in every sick patient. It's non-specific."**
Agreed, and we say so. 176 of 178 significant proteins go *up* with severity, and the top of the list is cell-leakage proteins (NPM1, PXN, CALR, GSTP1, PRDX1/6), neutrophil activation (PRTN3, CD177) and IL-6. The other IL-1-family decoy receptor, IL-1R2, is also prognostic (rank 27). That is exactly why sST2 is proposed only for *enrichment*, not as proof of mechanism. It is also why Gate 1 tests IL-33 *bioactivity* directly.

**"The in vitro data show massive E-selectin and VCAM-1 induction. Isn't that the endothelial story?"**
No. Those figures (SELE +11.2, VCAM1 +8.7, CXCL8 +8.2, CXCL1 +8.2 log2) sit at the top of the logFC-sorted HUVEC file, but they are **not statistically supported** (q = 0.19–1.0). Their per-gene standard errors in the delivered fit are 4 to >1,000 log2 units, an artefact of one pooled model across four unrelated cell types (Fig. S1). The same applies to ST2 (IL1RL1), PTX3 and vWF. Our mechanistic case rests only on genes with interpretable statistics.

**"Isn't this just generic NF-κB inflammation that steroids and IL-6 blockade already cover?"**
Possibly. Our data cannot tell, for two reasons:

* No IL-1β or TNF comparator arm was run.
* The IL-33 endothelial programme (NF-κB, chemokines, TF/PAI-1/thrombomodulin) is the kind of output those cytokines can also produce.

So the decision question is not whether the downstream programme is unique to IL-33. It is whether IL-33 is a meaningful *upstream driver* of that programme in patients who deteriorate. Gate 1a measures exactly that, using patient samples with AX-1177 vs isotype. Gate 1c adds IL-1β/TNF comparators to find any IL-33-selective readouts.

**"IL-33 is a COPD target. Why not pivot there?"**
Because *our* data contain nothing supporting it:

* No epithelial cell was ever stimulated with IL-33.
* There was no oxidised-IL-33 arm.
* In the post-mortem cohort, IL-33 does not differ with COPD/emphysema (18 vs 13 donors; p = 0.14–0.89 across compartments).

A COPD pivot would be a new programme justified by external data, not by ours.

**"Then why not simply drop it?"**
The key uncertainty, whether IL-33 is *bioactive* on endothelium in patients who deteriorate, can be answered in months using samples we own. Dropping now would discard a validated, specific molecule on absence of evidence. The gate has explicit kill criteria, so this is not an open-ended commitment.

# 4. Evidence by dataset (summary)

**4.1 In vitro transcriptomics** (Fig. 1, Fig. 4)

*Design:* HUVEC (umbilical vein, single donor, P2) and HGMEC (glomerular microvascular, single donor, P5) were treated with IL-33red 30 ng/mL ± AX-1177 or isotype at 10 µg/mL. That is about a 41-fold molar excess of antibody, added at the same time as IL-33 with no pre-incubation. Readouts at 6 h and 24 h; n = 3.

*Findings:*

* Reversal is complete for robust genes at both timepoints, and the isotype is inert.
* The response peaks at 6 h:
  * **Transient** (back near baseline by 24 h): TNF, MCP-3, tissue factor.
  * **Persisting but declining:** IL-6, CX3CL1, TNFRSF9, OPG.
  * **Sustained:** GM-CSF, CXCL6, G-CSF, CCL20, CXCL5, KYNU, IL-1β.
* A secondary interferon/complement component rises at 24 h (C3, C1S, CFB, GBP5). A few low-expression interferon-stimulated genes (OASL, RSAD2, MX2) are only partly reversed at 24 h. That signal is noisy (blockade q = 0.19–0.82) but warrants a pre-incubation/endotoxin control.

*Design limits:*

* HUVEC is not lung endothelium, and each endothelial line comes from a single donor.
* One antibody concentration, so no potency estimate.
* Reduced IL-33 only.
* Epithelial lines (A549, MCF7) served only as specificity controls.
* The "vs PBS" and "vs DMSO" contrasts are not valid controls for an antibody.

**4.2 Serum proteomics** (Fig. 2)

*Cohort:* 100 hospitalised COVID-19 patients (single centre, pre-vaccination). Serum taken at enrolment. 44 reached ICU, invasive ventilation or death within 30 days (inferred from the per-group denominators 56/44).

*Association with outcome:*

* 178 of 1,094 assays pass BH 0.05, and 384 reach p < 0.05 against 55 expected by chance.
* The IL-33 axis is represented by sST2 (#2).
* **Serum IL-33 itself cannot be assessed.** It is one of 15 low-detectability Inflammation-panel assays absent from the delivery.
* Endotheliopathy and coagulation proteins are prognostic: PTX3 (adj.p 0.012), uPAR (0.025), vWF (0.050), ANGPT2 (p = 0.009), tissue factor (p = 0.009), PAI-1 (p = 0.048).
* Structural endothelial proteins are not: CDH5, PECAM-1, CD93, TIE1/2.
* Type-2 markers are null: IL-5 OR 1.00, eotaxins, CCL17, tryptase.

*Bridging panel* — proteins that are IL-33-induced, AX-1177-reversible *and* prognostic:

* **CCL20** (adj.p 0.020)
* **OPG/TNFRSF11B** (two panels; adj.p 0.014 / 0.020)
* **IL-6** (four panels; adj.p 0.012–0.019)
* **IL-18R1** (0.018)
* **MCP-3** (0.020)
* **IL-1β** (0.046)
* **CSF-1** (0.037)
* **tissue factor** (0.051)

**4.3 Post-mortem lung** (Fig. 3)

*Cohort:* 31 donors, 74 blocks; analysed at donor level because three COVID+ donors contribute 24 of 49 COVID+ blocks. The cohort is very elderly (mean 81–84 years).

*Findings:*

* IL-33 is abundant everywhere. Endothelial IL-33 sits at the top of the delivered scale in 16 of 31 donors.
* There is no COVID effect after age adjustment.
* Endothelial and vascular smooth muscle IL-33 rise with age (ρ = 0.55–0.56, p = 0.001).
* What *does* distinguish COVID-19 lungs is DAD (7/16 vs 0/15, p = 0.007) and thromboemboli (4/16 vs 0/15, p = 0.10). IL-33 IHC does not track either.
* Granulocyte markers separate pneumonia from non-pneumonia, not COVID+ from COVID−.
* Nuclear IL-33 IHC shows *stored* alarmin, not release or activity. It was scored by a single reader on an undocumented sub-graded scale.

# 5. What indication do our data point at?

Only one thread runs through all three datasets, and it is **vascular**:

1. **Mechanism we can show and block:** IL-33-driven endothelial inflammation with a procoagulant switch (TF↑, PAI-1↑, thrombomodulin↓).
2. **Patients:** at enrolment, the IL-33 decoy receptor sST2 and endotheliopathy/coagulation proteins predict progression, independent of NEWS2. PTX3 and uPAR pass BH < 0.05; vWF, ANGPT2 and TF are borderline (adj.p 0.050–0.052); PAI-1 is nominal (p = 0.048).
3. **Tissue:** diffuse alveolar damage and thromboemboli are what set COVID-19 lungs apart.

**Indication the data support:** *prevention of progression to critical illness (ICU/IMV/death) in hospitalised, not-yet-critical viral pneumonia patients with high IL-33-axis activity (sST2-high) and an endotheliopathic/thrombo-inflammatory phenotype.*

This has three consequences:

* **Patient population:** narrower than "severe LRTI", with biomarker-based enrichment and early treatment.
* **Mechanism:** vascular rather than epithelial/type-2.
* **Evidence gap:** human evidence exists only for SARS-CoV-2. Extending to influenza/RSV is an assumption that needs its own data.

This is a **hypothesis our data are consistent with, not one they prove.** The IL-33 → endothelium link has not yet been demonstrated in patients.

**Indications our data do not support:**

* **COPD / asthma:** no epithelial or oxidised-IL-33 pharmacology, no COPD association in tissue, no type-2 signal.
* **Renal microvascular disease:** HGMEC response is weaker and transient; no renal patient data.
* **Cardiovascular disease** (sST2 is a heart-failure marker): no cardiovascular patients in our data.

If the vascular thesis fails in viral pneumonia, any move to another thrombo-inflammatory disease would be a *new* hypothesis with no programme data behind it.

# 6. What the next studies must establish: gated plan

**Gate 0: desk and archive work (0–2 months, minimal cost)**

1. Put the **biologics file** (affinity, IL-33red/IL-33ox binding, potency) in front of the committee. The dual-redox-form claim cannot be verified from the delivery.
2. **Refit the RNA-seq per cell line** from the archived count matrices. Add sample-level QC, and settle E-selectin, VCAM-1, IL-8, CXCL1, ST2, PTX3 and vWF, which are currently uninterpretable.
3. **Re-analyse the serum cohort at patient level:**
   * sST2 cut-off, ROC, and added value over NEWS2.
   * Does sST2 co-vary with the AX-1177-reversible panel (CCL20, OPG, IL-6, IL-18R1, TF) more than with non-IL-33 inflammatory proteins? If the IL-33 axis drives endothelial activation in patients, it should.

**Gate 1: decisive translational tests (2–9 months, modest cost)**

| Test | What it must establish | Go | Kill |
|---|---|---|---|
| **1a. Ex vivo IL-33 bioactivity of patient samples** (the critical test). Serum/plasma from the 100-patient cohort applied to primary human *lung* microvascular EC (≥3 donors) ± AX-1177 ± isotype. 6 h readout of CSF2, CXCL6, CCL20, F3, NFKBIA, TNFAIP3. | That patients carry IL-33 activity that AX-1177 neutralises, and that it relates to outcome | AX-1177-neutralisable activity in a meaningful fraction of patients (pre-specify; e.g. ≥20%), enriched in progressors and/or sST2-high patients | No AX-1177-neutralisable activity, or no relation to outcome |
| **1b. Lung tissue signature.** RNA-seq of the 22 archived lung RNAs (9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia), scored for the AX-1177-reversible IL-33 endothelial signature. | That the programme we block is active in diseased lung | Score higher in COVID+ than COVID− pneumonia, and/or in DAD/thrombosis cases | No difference |
| **1c. Pharmacology** in lung microvascular EC: dose-response (IC₅₀/IC₉₀) with and without pre-incubation; IL-1β and TNF comparators; oxidised IL-33 in primary airway epithelium (ALI); endotoxin/heat-inactivated IL-33 control | Potency; IL-33-selective outputs; whether the dual-form claim holds | Competitive potency (against biologics-file target); IL-33-selective readouts identified | Poor potency *and* no oxidised-IL-33 activity (no differentiation) |
| **1d. Second blinded pathologist + image analysis** of IL-33 IHC; add ST2 staining of lung endothelium | Whether ST2-bearing endothelium co-localises with injury | Supportive only | — |

*Decision rule:* **1a is mandatory.** Advance only if 1a is positive and at least one of 1b/1c is positive. If 1a is negative, terminate.

*Feasibility caveat for 1a:* reduced IL-33 oxidises (and loses ST2 activity) within hours ex vivo, and sST2 in the sample will buffer it. Run 1a first on archived cohort serum, which is cheap. If that is negative, confirm it in about 20 rapidly processed fresh plasma samples (or airway samples) from hospitalised patients before invoking the kill criterion.

**Gate 2: in vivo and prospective biomarker work (9–24 months)**

* **Therapeutic-dosing viral pneumonia model(s):** influenza ± SARS-CoV-2, dosing after infection.
  * Efficacy endpoints: survival/weight, vascular leak, coagulation activation.
  * Safety endpoint: **no impairment of viral clearance or repair.**
* **Prospective multi-virus observational cohort** (SARS-CoV-2, influenza, RSV; vaccinated era):
  * EDTA/citrate **plasma** at admission, 24 h, 72 h, day 7 and day 14.
  * Record time from symptom onset and treatments (steroids, IL-6R/JAK inhibitors).
  * Outcomes: ICU/IMV/death and venous thromboembolism.
* **Total IL-33 assay:** develop a drug-tolerant, high-sensitivity assay for total (drug-bound) IL-33, covering both redox forms.

**Gate 3:** IND-enabling work, then an sST2-enriched Phase 1b/2a in hospitalised viral pneumonia with PD-driven dose selection.

# 7. Biomarkers, sampling timepoint, and roles in patients

**Sampling timepoint.**

* **In patients:** the primary sample is **pre-dose at enrolment**, i.e. hospitalised and not yet critical. This is the only timepoint at which our data show prognostic value (sST2), and it is the randomisation decision point.
* **For pharmacodynamics (PD):** add early on-treatment samples at **24 h and 72 h**, then day 7. This follows the in vitro kinetics: IL-33-driven endothelial outputs peak by 6 h, and several (TNF, MCP-3, tissue factor) are near baseline by 24 h. So:
  * Use the **sustained** outputs (CCL20, OPG, IL-6, IL-1β) as circulating PD markers.
  * Transient ones are only usable with dense early sampling.
* **Ex vivo / in vitro assays:** read out at **6 h**. At 6 h the response is maximal and fully reversible, and the microvascular (HGMEC) response is still present; 82% of it is gone by 24 h.
* **Sample matrix:** use **citrated/EDTA plasma, not serum.** Clotting releases tissue factor, PAI-1, VEGF and other platelet proteins ex vivo.

| Marker | Role in patients | Could go into patients now? | Basis in our data |
|---|---|---|---|
| **sST2** | **Prognostic enrichment / stratification** (baseline) | **Yes**, as an exploratory stratifier. It should not be an inclusion criterion until the cut-off is derived and externally validated. | #2 of 1,094 proteins, independent of NEWS2. Not a PD marker: not interpretable as IL-33-regulated in vitro, and it is a decoy receptor. |
| **Total (drug-bound) IL-33** | **Target engagement** | **No**: assay needed | Serum IL-33 not measurable in our cohort |
| **CCL20, OPG, IL-6, IL-18R1** (+ IL-1β) | **Exploratory PD**: placebo-controlled change from baseline; also prognostic covariates | **Yes** (exploratory) | IL-33-induced, AX-1177-reversed in both EC types (CCL20, OPG, IL-6, IL-1β sustained to 24 h), and prognostic in serum. Non-specific, and confounded by steroids/IL-6R blockade. |
| **Tissue factor, MCP-3** | Early exploratory PD (procoagulant arm) | Yes, if sampled ≤24 h, in citrated plasma | Transient in vitro; TF p = 0.009 in serum |
| **vWF, ANGPT2, PTX3, uPAR, HGF** | Prognostic / disease-activity covariates (**not PD**) | Yes | Prognostic. No interpretable IL-33 regulation in vitro. |
| **GM-CSF, CXCL6, G-CSF, CXCL5, KYNU, TNFRSF9** | **Ex vivo bioassay readouts** (6 h), potency and patient-sample bioactivity | Assay only | Largest, most sustained IL-33 outputs, but **not** prognostic in serum |
| IL-33 IHC; type-2 markers; E-selectin/VCAM-1/IL-8/CXCL1 as PD | **Not recommended** | No | See Section 9 |

# 8. If the committee drops AX-1177: what we are dropping and why

*For the minutes:*

**What we would be dropping:** an anti-IL-33 monoclonal antibody with clean in vitro pharmacology. It completely and specifically neutralises reduced IL-33-driven inflammatory and procoagulant activation of human endothelium, with no IL-33-independent transcriptional activity in four cell types. It comes with an untested hypothesis of benefit in sST2-high hospitalised viral pneumonia.

**Why:**

* There is no programme evidence that IL-33 is a dominant, druggable driver of progression in patients.
* The IL-33 programme we block overlaps the IL-1/TNF/NF-κB axis, and our data cannot separate the two. *Context, not programme data:* standard of care already targets downstream mediators such as IL-6.
* The most IL-33-specific outputs do not track severity.
* Lung IL-33 is not altered by COVID-19.
* The antibody's presumed differentiator (oxidised IL-33 / epithelial activity), its potency and in vivo efficacy are undocumented in the programme data.

**What would reverse that:** a positive Gate 1a, i.e. AX-1177-neutralisable IL-33 bioactivity in samples from patients who progress.

# 9. Considered and ruled out

| Option / claim considered | Why ruled out (our data) |
|---|---|
| Continue the broad "severe LRTI" programme unchanged | Human data are SARS-CoV-2 only. No causal or efficacy data. Key outputs don't track severity. Differentiator untested. |
| Drop outright now | Case rests on absence of evidence. Decisive tests are cheap and largely archive-based. |
| Pivot to COPD | No epithelial/oxidised-IL-33 data. Tissue IL-33 not associated with COPD/emphysema (p = 0.14–0.89) or clinical COPD (p = 0.21–0.59). |
| Pivot to asthma / eosinophilic (type-2) disease | Serum IL-5 (OR 1.00), eotaxins, CCL24, CCL17 and tryptase are null. Tissue eosinophil/mast-cell markers track pneumonia, not COVID, and don't relate to IL-33. |
| Renal / glomerular microvascular indication | HGMEC response is weaker and mostly gone by 24 h. No renal patient data (KIM-1 p = 0.03–0.07 only). |
| Cardiovascular indication via sST2 | No cardiovascular patients in our data. sST2 is a non-specific stress marker. |
| E-selectin, VCAM-1, IL-8, CXCL1, ST2, PTX3, vWF as in vitro-bridged PD markers | In vitro statistics unusable (SE 4 to >1,000). Serum VCAM-1 (p = 0.43) and CXCL1 (p = 0.28/0.46) are not prognostic in any case. |
| Serum IL-33 as a biomarker | Not measurable; assay absent from the delivery |
| Lung IL-33 IHC as a selection tool | Post-mortem only, at ceiling, age-driven, not disease-specific, single reader |
| "AX-1177 has off-target effects" (from AX-alone hits) | Of 328 hits, 84% are low-count genes, 10% are <15% shifts (e.g. AKR1C2 log2FC 0.06–0.17 with implausible t of 60–169) and 6% are isolated genes. No pathway enrichment (best Hallmark q = 0.40), and no effect on IL-33-responsive genes. |
| "AX-1177 effects" based on the vs-PBS / vs-DMSO contrasts | Wrong comparators for an antibody; the isotype contrasts are the valid ones |
| Block-level post-mortem statistics | Pseudo-replicated: 3 donors supply 24/49 COVID+ blocks. All inference here is donor-level. |
| Ranking serum proteins by OR | ORs are per log-unit, so not comparable across assays (e.g. CSF-1 OR 90, CI 4–1,933). Ranked by p-value instead. |
| "Lower endothelial/vascular-smooth-muscle IL-33 in COVID+ = alarmin release" | Attractive but not supported: explained by age (age-adjusted p = 0.21–0.23). Endothelial IL-33 vs neutrophil elastase (ρ = −0.43, p = 0.016) is one of many exploratory tests. |

# 10. Data-integrity issues the committee should know about

Full log with consequences and actions: workbook sheet S7. None of these issues overturns the core pharmacology. Several limit what can be claimed.

1. **RNA-seq sheets mislabelled.** The "6h" and "24h" sheets each contain *all* 24 contrasts for both timepoints, with identical values. The "6h" sheet runs to Excel's 1,048,576-row limit, but it is not truncated: all 629,040 rows are present.
2. **One pooled limma fit across four unrelated cell types.** 136 genes, including the canonical endothelial and IL-33-axis genes, have uninterpretable statistics. The HUVEC file is sorted by log2FC, so it headlines exactly those genes. *Action:* refit per cell line from the archived counts.
3. **Design gaps:**
   * No HGMEC vehicle arm.
   * No IL-33 in epithelial lines.
   * No oxidised IL-33 arm.
   * Single donors.
   * One antibody dose, no pre-incubation.
   * DMSO "vehicle" for an antibody.
4. **Serum proteomics reporting:**
   * Reported adj.p values correspond to about 1,194 tests, not the 1,094 delivered (slightly conservative).
   * IL-33 and 14 other low-detectability assays are absent.
   * The outcome-group columns are unlabelled; they were inferred as fraction below LOD/missing in groups of n = 56/44.
   * 27 proteins are duplicated across panels.
   * "Log-transformed" is applied to already-log2 Olink data, with an undocumented base.
   * Samples are serum, not plasma.
5. **Post-mortem:**
   * Donor fields are recorded only on the first block.
   * The numeric scores exceed the documented 0–5 scale (the "+0.5" encoding and an undocumented IL-33 sub-grade scale).
   * One donor has missing SARS-CoV-2 status.
   * Single reader.
6. **Potency and redox-form binding data are not in the delivery** (held in the biologics file).

# 11. Methods (brief) and files

* **RNA-seq.**
  * Consistency checks: identical AveExpr across all 26 contrasts; t↔p consistent with df ≈ 85; per-gene SE computed as log2FC/t.
  * Reversal analysis restricted to genes with SE < 1.5. Residual IL-33 effect under AX-1177 = (IL-33 vs vehicle) + (AX-1177+IL-33 vs IL-33) − (AX-1177 vs isotype), which assumes isotype ≈ vehicle.
  * Pathway enrichment: MSigDB Hallmark (msigdbr 7.5.1), one-sided Fisher test, BH correction.
* **Serum.**
  * Wald consistency of OR/CI/p verified.
  * Olink assay names mapped to genes manually (940/1,094 matched to RNA-seq genes).
  * Enrichment tested one row per gene, against genes not responsive to IL-33.
* **Post-mortem.**
  * Donor fields forward-filled; blocks averaged per donor.
  * Mann-Whitney/Kruskal-Wallis tests; rank-based OLS for age adjustment.
  * Pathology text flags for DAD, thrombosis and emphysema, manually checked for regex false positives.

*Files in `/tmp/outputs/`:*

* `AX-1177_portfolio_audit_brief.md` / `.docx` — this brief
* `AX-1177_audit_supporting_tables.xlsx` — sheets S1–S8: signature, biomarker candidates, annotated serum table, donor-level pathology, statistics, DE counts, QC log, unreliable genes
* `figures/Fig1_invitro_pharmacology.png`
* `figures/Fig2_serum_proteomics_bridge.png`
* `figures/Fig3_postmortem_IL33.png`
* `figures/Fig4_kinetics_specificity.png`
* `figures/FigS1_rnaseq_variance_artifact.png`

# Figures

![**Figure 1. AX-1177 pharmacology in endothelium.** Each dot is a gene. The x-axis is the IL-33red effect versus vehicle; the y-axis is the effect of AX-1177 relative to isotype, both in the presence of IL-33. Points on the red line are fully reversed. Red crosses mark canonical genes (SELE, VCAM1, CXCL8, CXCL1, IL1RL1, PTX3) whose statistics are not interpretable in the delivered fit.](figures/Fig1_invitro_pharmacology.png)

![**Figure 2. Serum proteomics and the translational bridge.** (A) Association with ICU/IMV/death, adjusted for age, sex and NEWS2. (B) The AX-1177-reversible endothelial signature is not over-represented among prognostic proteins.](figures/Fig2_serum_proteomics_bridge.png)

![**Figure 3. Post-mortem lung IL-33 at donor level.** No COVID effect in any compartment. Age drives endothelial and vascular smooth muscle IL-33. Block counts show the pseudo-replication problem.](figures/Fig3_postmortem_IL33.png)

![**Figure 4. Kinetics and specificity.** (A) Selected genes across contrasts (* = BH q < 0.05). (B) Size of each response; AX-1177 alone is inert.](figures/Fig4_kinetics_specificity.png)

![**Figure S1. RNA-seq variance artefact.** Implausible per-gene standard errors from a single pooled fit across four cell types. These make the canonical endothelial and IL-33-axis genes uninterpretable.](figures/FigS1_rnaseq_variance_artifact.png)
