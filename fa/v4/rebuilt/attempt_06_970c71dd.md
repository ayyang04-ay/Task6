---
title: "AX-1177 (anti-IL-33 IgG1) — portfolio audit position"
subtitle: "Recommendation, defence, forward view, and what was ruled out"
---

**Basis.** This memo uses only the five delivered AX-1177 files: the methods annex, the HUVEC IL-33 RNA-seq, the remaining RNA-seq contrasts, the clinical serum proteomics, and the post-mortem lung IHC. Every number below comes from re-analysing them. I re-analysed rather than reading the delivered statistics at face value because each file has integrity problems (Section 7). Points that rest on anything outside our data are marked *(outside our data — verify)*. Supporting tables are in `AX-1177_supporting_tables.xlsx` and figures are in `figures/`.

# 1. Recommendation

**Keep AX-1177, but stop developing it for "severe lower respiratory viral infection" as currently framed.** Re-scope it to the one hypothesis our data support: IL-33-driven endothelial inflammation in hospitalised severe pneumonia. Patients would be identified by a high serum sST2 at admission, whatever the pathogen. Fund only a short, low-cost, decisive gate that uses samples and data we already hold. Commit in advance to dropping the asset if that gate fails.

The position rests on three findings from our own data:

1. **The molecule works and is clean.**
   - In human endothelial cells, AX-1177 abolishes the reduced-IL-33 (IL-33red) programme.
   - For the 133-gene core signature at 6 h, the reversal slope is −1.03, median inhibition is 100%, and 98% of genes are significantly reversed. At 24 h the figures are 82% inhibition and 91% of genes reversed.
   - These estimates use a contrast that shares no wells with the IL-33 reference, so they are not a shared-group artefact.
   - On its own, with no IL-33, AX-1177 has no detectable transcriptional activity in four cell types.
2. **Our human data do not support the current disease thesis.**
   - COVID-19 lungs do not contain more IL-33 than other lungs. Vascular IL-33 is, if anything, lower: endothelium 4.81 vs 5.50 (p = 0.052) and smooth muscle 2.38 vs 3.25 (p = 0.068), analysed by donor.
   - Circulating IL-33 was never evaluable, because it is absent from the delivered serum data.
   - Type-2 biology plays no part in the severity signal.
3. **There is still a real, testable translational handle.**
   - sST2, the IL-33 decoy receptor, ranks 2nd of 1,063 serum proteins for ICU admission, invasive ventilation or death. This holds after adjusting for age, sex and NEWS2 (OR 3.02, 95% CI 1.83–5.01 per log unit).
   - Four other outcome-associated serum proteins (IL-6, OPG, CCL20, IL-1β) are driven by IL-33 in endothelium. AX-1177 fully reverses them at 6 h and reverses 84–96% of the effect at 24 h.
   - Together that is an enrichment marker plus a pharmacodynamic (PD) panel, which most assets at this stage lack.

**The ask: Gate 1, about 3–6 months**, using banked sera and tissue plus re-analysis of archived data.

- **Kill** if sera from sST2-high severe patients contain no IL-33 activity that AX-1177 can neutralise, *and* no measurable IL-33 (free or total).
- **If the committee applies a hard bar** of "human evidence that the target drives the disease", AX-1177 does not meet it today. The gate is designed to answer exactly that question.

# 2. Evidence scorecard

| Question | What our data show | Strength |
|---|---|---|
| Does AX-1177 neutralise IL-33 in human cells? | Yes, for IL-33red in HUVEC (complete at 6 h, ~80–90% at 24 h). HGMEC: concordant reversal at 6 h (r = −0.63 vs the HUVEC response), weaker at 24 h (r = −0.31). | **Strong**, but in vitro only: single donor per cell type, one concentration, about 41:1 IgG:IL-33 molar |
| Is it specific? | AX-1177 vs isotype with no IL-33 gives 13–67 "DE" genes per contrast, all noise-level. Correlation with the IL-33 signature \|ρ\| ≤ 0.10. NF-κB gene-set mean log2FC ≈ 0. Isotype does not alter the IL-33 response (median 0.4% at 6 h). | **Strong** at transcript level |
| Is the target present where the disease is? | IL-33 is present in lung endothelium, basal epithelium and vascular smooth muscle in every donor. Endothelium sits at the scoring ceiling in 39 of 74 blocks. | **Strong** for presence |
| Is the target increased or activated in the disease? | No. IL-33 is not higher in COVID-19 or pneumonia, and the vascular trend is lower. IHC measures stored nuclear IL-33 and cannot show release. | **Absent / contrary** |
| Is IL-33 pathway activity linked to outcome? | sST2 ranks 2nd of 1,063. But IL-33 itself was not measured, and the set of endothelial genes IL-33 induces is not enriched among outcome proteins (Fisher OR 1.13, p = 0.75) against a global upward shift. | **Moderate, indirect** |
| Is there a type-2 / eosinophil story? | No. IL-5 ranks 1,060 of 1,063 and tryptase 994. Tissue eosinophils track pneumonia, not IL-33. | None |
| In vivo efficacy, PK, toxicology, potency (IC50), oxidised IL-33 | Not in the files; the annex says the biologics file is held separately. | **Missing** |

# 3. The case: keep, re-scoped and gated

## 3.1 What AX-1177 does (RNA-seq, Fig. 1)

**Design.** HUVEC (macrovascular) and HGMEC (glomerular microvascular) were treated with IL-33red at 30 ng/mL, with AX-1177 or isotype IC119 at 10 µg/mL (about 41-fold molar excess). The antibody was added concurrently, with no pre-incubation. Samples were taken at 6 h and 24 h, n = 3.

**What IL-33red does in HUVEC.**
- It changes 4,031 genes at q < 0.05 at 6 h (1,057 with \|log2FC\| > 1 and reliable statistics) and 1,836 at 24 h.
- The response is a canonical NF-κB programme: TNFα/NF-κB NES 3.1, plus IFN-γ/α, inflammatory-response and IL-6/JAK/STAT3 sets.
- It is neutrophil-mobilising and endothelium-activating. Examples (log2FC at 6 h): GM-CSF/CSF2 +10.3, CXCL6 +9.4, CCL20 +9.2, CX3CL1 +8.4, G-CSF/CSF3 +8.3, TNF +7.9, IL6 +5.8, tissue factor/F3 +5.6, OPG/TNFRSF11B +4.8.

**What AX-1177 does to that response.**
- At 6 h the core 133-gene signature is reversed with slope −1.03 and 100% median inhibition; 98% of genes are significantly reversed.
- At 24 h the 33-gene core is reversed with slope −1.02, 82% inhibition and 91% of genes reversed.
- Across all 1,057 responsive genes the independent estimate is lower (77% at 6 h, 47% at 24 h). Weak responders are noisy, and inhibition may be partial by 24 h.

**Specificity.**
- On its own, AX-1177 changes no inflammatory pathway in HUVEC, HGMEC, A549 or MCF7.
- Its nominal "hits" are sporadically detected lncRNAs and pseudogenes, plus housekeeping genes with \|log2FC\| < 0.2 that carry inflated t-statistics.

**Limits.**
- The reduced form of IL-33 signals through ST2. Only that form was tested, although the annex says AX-1177 binds both forms.
- The oxidised form signals through RAGE/EGFR. That arm is untested, and no epithelial cells were given IL-33.
- No IC50, no lung-derived cells, and the IL-33 concentration is supraphysiological.
- The 24 h "proliferation" component (E2F/G2M/MYC) cannot be credited to IL-33. AX-1177 alone shifts the same gene sets by a similar amount (NES −2.4 to −3.0), which looks like well-to-well culture variation. I claim only the inflammatory programme as IL-33-specific.

## 3.2 What the patient serum says (Fig. 2)

**Cohort.** 100 patients hospitalised with SARS-CoV-2 before vaccination was available, at a single centre, sampled at enrolment. 44 reached the composite endpoint; this is inferred from the below-LOD columns.

**Internal reproducibility is good.**
- The 1,094 assays collapse to 1,063 unique proteins.
- Proteins run on several panels agree closely: IL-6 OR 2.07–2.31 across four panels, HGF 4.99/4.84, OPG 6.77/4.40.

**Severity lifts almost the whole serum proteome.**
- 82% of proteins have OR > 1. 362 are nominally up and 8 down, against about 27 each expected by chance.
- Many top hits are intracellular proteins (NPM1, PXN, PRDX1/6, CALR), pointing to tissue damage and/or release from blood cells during clotting.
- So any single association has to be read against that background.

**sST2 stands out against that background.** It ranks 2nd (q = 0.009), about 2 robust SD above the shift. NT-proBNP is only weakly associated (OR 1.20), so sST2 is not simply a heart-failure signal. HGF ranks 1st.

**The outcome biology is innate inflammation plus endothelial activation/injury.**
- Ranks: PTX3 5, IL-6 10, OPG 14, OSM 16, IL-18R1 21, MCP-3 40, CCL20 41, VEGF-A 86, vWF 169, tissue factor 183, ANGPT2 187, sFlt-1 191.
- Structural endothelial markers are null: PECAM-1, VE-cadherin, VEGFR-2.
- Type-2 markers are null: IL-5 rank 1,060, eotaxin-1 991, tryptase 994, eotaxin-2 844, TARC 742.

**The bridge is partial, not a fingerprint.**
- Several outcome proteins are IL-33-dependent and AX-1177-reversible in endothelium: IL-6, OPG, CCL20, IL-1β, IL-18R1, MCP-3, tissue factor.
- But the strongest IL-33-specific outputs (G-CSF, CXCL5, CXCL6, CXCL10) rank 620–1,035. As a set, IL-33-inducible genes are not over-represented among outcome proteins (p = 0.75).
- The ligand itself was not delivered: IL-33, TSLP, IL-4, IL-13 and the Inflammation-panel IL-5 are all missing. The most likely reason is a detectability filter.

## 3.3 What the lung tissue says (Fig. 3)

**Unit of analysis.** The file holds 31 donors and 74 blocks, analysed by donor. Blocks are highly correlated within a donor (ICC 0.40–0.82), and three COVID+ donors contribute 24 of the 49 COVID+ blocks.

**COVID+ vs all COVID− donors.**

| Compartment | COVID+ | COVID− | p |
|---|---|---|---|
| Basal epithelium | 4.25 | 4.75 | 0.76 |
| Endothelium | 4.81 | 5.50 | 0.052 |
| Vascular smooth muscle | 2.38 | 3.25 | 0.068 |

- A mixed model at block level gives endothelium −0.43 (p = 0.049) and smooth muscle −0.72 (p = 0.042).
- Adjusting for age and sex by donor gives p ≈ 0.07–0.08.
- The direction is consistently *lower*, never higher.

**Other determinants.**
- Vascular IL-33 rises with age (ρ = 0.55, p = 0.001).
- IL-33 shows no significant association with COPD, asthma or emphysema.
- It is, if anything, lower where there is acute lung pathology: endothelium 4.88 vs 5.50, p = 0.028 unadjusted, p = 0.11 after age/sex adjustment.
- It is also lower with diffuse alveolar damage: smooth muscle 1.78 vs 3.25, p = 0.055.
- Eosinophil granule proteins do not correlate with IL-33 (ρ −0.20 to +0.08).
- IL-5Rα and neutrophil elastase correlate *inversely* with endothelial IL-33 (ρ ≈ −0.4, exploratory). That fits IL-33 depletion where inflammation is greatest.
- Eosinophil, basophil and IL-5Rα scores separate pneumonia from non-pneumonia by label, but not COVID+ from COVID−.

**Reading.** The target is present but not induced. Lower vascular IL-33 in severe or COVID lungs is what release would look like, or endothelial loss. Static IHC cannot tell the two apart.

## 3.4 Why the data lead to "re-scope and gate"

- **Continuing as is** would contradict our own human data. Nothing links IL-33 to viral infection specifically. The serum evidence is COVID-only and from before vaccination.
- **Dropping now** would throw away a de-risked, specific molecule and a prognostic enrichment marker with a linked PD panel. It would do so when the missing link (is bioactive IL-33 present in these patients?) can be tested in months, using samples we hold.
- **Re-scoping and gating** spends little, asks the one question that decides value, and has explicit kill criteria (Section 5.2).

## 3.5 Anticipated challenges and answers

- **"sST2 ranks 2nd of 1,063 — doesn't that validate IL-33?"**
  - No. sST2 is a decoy receptor that endothelium and epithelium release in response to many stimuli. It shows who is at risk, which is what enrichment needs. It does not show that IL-33 drives the outcome.
  - In our own cells IL-33 induces IL1RL1 only modestly (+1.6 log2 at 6 h, and the statistics for this gene are unreliable).
- **"AX-1177 blocks everything IL-33 does to endothelium."**
  - In vitro, yes. But TNF, IL-1 and viral sensing drive the same NF-κB programme. Blocking IL-33 matters only if it is a dominant input in patients, and that is what we have not shown.
  - The IL-33-specific outputs (G-CSF, CXCL5, CXCL6) are absent from the outcome signal.
- **"IL-33 is everywhere in lung."**
  - Presence is not activity. It is not increased in disease, it is at the scoring ceiling, and it is driven by age.
- **"Why not pivot to COPD like others?"**
  - We have no COPD patients and no COPD-related IL-33 difference among our donors (epithelium 4.75 vs 4.25, p = 0.21).
  - We have no test of the epithelial / oxidised-IL-33 arm.
  - That pivot would be a bet made on competitors' evidence, not ours.
- **"Can we trust these files?"**
  - Not at face value (Section 7). Every conclusion here uses only statistics that pass checks: donor-level tissue analysis, de-duplicated serum multiplicity, independent-contrast inhibition, and exclusion of genes with unreliable standard errors.
  - None of the fixes is likely to reverse a conclusion. Several could strengthen the PD package: E-selectin, VCAM-1, ICAM-1, IL-8 and PTX3 are currently unusable statistically.
- **"Is 30 ng/mL IL-33 relevant?"**
  - It is supraphysiological. It shows capacity at about 41-fold excess, not potency. IC50 data against both IL-33 forms must come before dose selection.
- **"Is it safe to block IL-33 during infection?"**
  - Not addressed by our data. IL-33 has repair and host-defence roles *(outside our data — verify)*, so this needs in vivo evaluation.

# 4. If we drop it: what we are dropping and why

**What we would be dropping:**
- A specific anti-IL-33 IgG1 with clean in vitro pharmacology. It completely neutralises IL-33red in two human endothelial beds and has no transcriptional off-target activity in four cell types.
- A biomarker package: sST2 for enrichment, plus a four-protein IL-33-dependent PD panel (IL-6, OPG, CCL20, IL-1β) on the same platform.
- A disease hypothesis that has not been validated.

**Why we would be dropping it:**
1. There is no human evidence in our data that IL-33 is increased, released or active in severe viral pneumonia.
2. The prognostic signals are non-specific, and the IL-33 fingerprint is absent from them.
3. There is no in vivo, PK, toxicology or potency package in the files.
4. The indication as framed rests on a single-centre, pre-vaccination COVID-19 cohort.

**Salvage.** Partner or out-license the in vitro and biomarker package, after the data fixes in Section 7.

*Outside our data — verify before the meeting:* other anti-IL-33 and anti-ST2 antibodies have been or are being tested in hospitalised viral lung infection and in COPD. A competitor readout would validate or undercut the class regardless of our data.

# 5. Forward view

## 5.1 Which indication our data point at

**The data point at the vascular endothelium, not the airway, and at acute severe inflammation, not chronic type-2 disease.** Concretely: hospitalised severe pneumonia at high risk of ICU, invasive ventilation or death, identified by high sST2 at admission, whatever the pathogen.

- **Endothelium.** It is where lung IL-33 is highest and where AX-1177's activity is demonstrated.
- **Mechanism.** AX-1177 blocks an endothelial programme whose secreted products (IL-6, OPG, CCL20, IL-1β, IL-18R1, MCP-3, tissue factor) are outcome-associated in patients.
- **Enrichment.** sST2 is the most outcome-selective protein beyond clinical severity.
- **Pathogen-agnostic.** Tissue IL-33 does not separate COVID from non-COVID pneumonia. But the serum evidence is COVID-only, so generalisation must be shown.
- **Early window.** The serum signal was measured at admission. Vascular IL-33 appears depleted at death, so any therapeutic window is likely early.

This is a **redefinition of the population**, not a move to a new organ or therapeutic area. Severe pneumonia and ARDS are high-attrition fields *(outside our data)*, which is one more reason for a gate. The data do **not** point at COVID-specific use, type-2 or eosinophilic disease, COPD or asthma, or kidney disease.

## 5.2 What the next studies have to establish, with go/kill gates

**Gate 0 — data remediation (weeks; near-zero cost).**
- Refit the RNA-seq separately per cell line from the archived counts.
- Deliver the missing contrasts: HGMEC IL-33 vs isotype; isotype+IL-33 vs IL-33; isotype vs vehicle.
- Re-analyse serum NPX: document the LOD filter and log base, adjust for global protein level, derive an sST2 cut-off with an optimism correction, and examine sST2 against NT-proBNP.
- Re-score post-mortem IL-33 with two blinded readers plus digital image analysis on the documented 0–5 scale, and re-adjudicate the disease labels.

**Gate 1 — is bioactive IL-33 present in the patients we would treat? (3–6 months; banked material). This is the decisive gate.**
- **E1.** In the 100 banked enrolment sera, measure free and total IL-33 with a high-sensitivity, drug-tolerant assay, plus IL-33:sST2 complexes.
- Run a **patient-serum HUVEC bioassay** with and without AX-1177 vs isotype: 6 h readout of CSF2, CCL20, CXCL6 and IL6 mRNA, or GM-CSF/CCL20 protein.
- **Go:** sera from sST2-high severe patients show IL-33 activity that AX-1177 reverses, above sST2-low patients.
- **Design note:** serum sST2 itself sequesters IL-33, so the bioassay must be read together with total IL-33. High total IL-33 with low bioactivity would mean sequestration, which is not a kill by itself.
- **E2.** On the same tissue blocks, stain nuclear vs extracellular IL-33, endothelial density (CD31/ERG) and ST2, to separate release from endothelial loss.
- **E3.** Archived tissue RNA exists for 22 donors (9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia; IDs Zr4940_x). Score the 133-gene core signature there, to test whether the IL-33-dependent endothelial programme is active in diseased lung.

**Gate 2 — complete the pharmacology, in parallel.**
- **In vitro:**
  - IC50 against IL-33red and IL-33ox, in at least 3 donors.
  - Lung microvascular endothelium.
  - Primary airway epithelium at air–liquid interface, to test the IL-33ox → RAGE/EGFR arm.
  - Pre-incubation vs concurrent addition, and physiological sST2.
  - Functional readouts: endothelial barrier and neutrophil adhesion under flow.
- **In vivo:** a viral pneumonia model with endothelial endpoints. This needs species cross-reactivity or a surrogate antibody.

**Gate 3 — clinical validation before Phase 1b.**
- An external multi-pathogen cohort of severe pneumonia (influenza, RSV, post-vaccination COVID, bacterial), with EDTA plasma at admission. It must confirm the sST2 enrichment and the Tier-1 PD panel.
- Then a Phase 1b/2a in sST2-high hospitalised severe pneumonia: PD at 24 h, target engagement, and safety.

**Kill criteria.**
- **K1 (Gate 1, decisive):** E1 is negative on both readouts. There is no AX-1177-neutralisable bioactivity, *and* free and total IL-33 are not higher in sST2-high than sST2-low severe patients.
- **K2 (Gates 0 and 3):** the sST2 association disappears after global-shift adjustment, or fails external replication. That removes the enrichment strategy.
- **K3 (Gate 2):** the required exposure is infeasible given the IC50, or AX-1177 has no IL-33ox activity in a setting where that arm matters.
- **K4 (Gate 2):** no benefit on endothelial endpoints in vivo.
- **E2 and E3 (tissue) are weight of evidence, not stand-alone kills.** A positive tissue signature would strengthen the case. Absence of release *and* absence of the signature, alongside a weak E1, should end the programme.

## 5.3 Biomarkers: role, and whether they can go into patients

| Marker | Role | Evidence in our data | Into patients? |
|---|---|---|---|
| **Serum sST2** | **Prognostic enrichment** (select high-risk patients) | Rank 2/1,063; OR 3.02 (1.83–5.01) adjusted for NEWS2 | **Yes.** Clinical sST2 immunoassays exist *(outside our data)*; the cut-off must be derived and externally validated. Not predictive of treatment benefit; not IL-33-specific |
| **IL-6, OPG, CCL20, IL-1β** (± cathepsin S) | **PD / proof of mechanism** (Tier 1) | IL-33-induced at 6 h and 24 h and reversed by AX-1177; outcome-associated (ranks 10, 14, 41, 156); reliable statistics | **Yes.** Same Olink panels, or a clinical IL-6 assay. Read only as a placebo-controlled change, because they are not IL-33-specific |
| IL-18R1, MCP-3, tissue factor, CSF-1 | Early PD (secondary) | IL-33-dependent at 6 h only; outcome-associated | Yes, in a 6 h intensive-sampling subset only |
| G-CSF, CXCL5, CXCL6, CX3CL1, MMP-10 | Exploratory mechanism PD | Largest and most sustained IL-33-dependent, AX-1177-reversed transcripts; not outcome-associated | Yes (Olink), for mechanism only |
| Total IL-33; IL-33:drug and IL-33:sST2 complexes | **Target engagement** / dose selection | Not in our data | Needs a new drug-tolerant assay first |
| Patient-serum HUVEC bioassay | Gate experiment; functional target engagement | Built on our validated system | Research use (banked sera now; exploratory in Phase 1b) |
| sE-selectin, sVCAM-1, sICAM-1, IL-8, PTX3 | Exploratory only | Large in vitro effects, but RNA statistics unreliable | Hold until the per-cell-line refit |
| Tissue IL-33 IHC; type-2 markers; HGF; damage proteins | None, or covariates at most | Ceiling and age confounding; null; non-mechanistic | **No** |

## 5.4 Sampling timepoints (Fig. 4)

- **Enrichment: at enrolment, before dosing.** This is the only timepoint at which our prognostic data exist. The tissue data (vascular IL-33 lower at death) also argue for early sampling.
- **Primary PD: 24 h after the first dose, paired with the pre-dose sample.**
  - At 24 h in vitro, the Tier-1 markers are still IL-33-dependent and AX-1177-reversed (log2FC: IL-6 −2.4, OPG −2.1, CCL20 −5.3, IL-1β −3.0).
  - The transient markers (tissue factor, MCP-3, IL-18R1, adhesion molecules) have largely resolved by then.
  - So 24 h isolates the sustained IL-33-dependent component, and it is practical in hospitalised patients.
  - Optional extras: a 6 h sample in an intensive PK/PD cohort to catch transient markers, and day 3–5 for durability.
- **Ex vivo bioassay: read at 6 h.** That is where the dynamic range is greatest (1,057 vs 506 responsive genes; 98% vs 91% of the core signature significantly reversed).

# 6. What I considered and ruled out

| Option | Verdict | Reason, from our data |
|---|---|---|
| Continue in severe LRVI as framed | Ruled out | No disease-linked IL-33 increase; ligand unmeasured; COVID-only, pre-vaccination serum |
| COVID-19-specific positioning | Ruled out | Tissue IL-33 is the same in COVID+ and COVID− pneumonia; trend is lower in COVID+ |
| Type-2 / eosinophilic indications | Ruled out | Type-2 cytokines, chemokines and tryptase are null in serum (ranks 742–1,060); ECP and IL-5Rα are unremarkable against the global shift (ranks 208, 391); tissue eosinophils do not track IL-33; no type-2 cells tested |
| COPD / asthma pivot | Considered; not supported | No COPD/emphysema signal in epithelial IL-33; oxidised-IL-33 arm untested; A549/MCF7 are not suitable models |
| Kidney / glomerular indication | Considered; not supported | HGMEC responds less and transiently; no HGMEC IL-33-vs-control contrast; no renal patient data |
| Tissue IL-33 IHC for patient selection | Ruled out | Post-mortem only; ceiling; age/sex-confounded; single reader; scores outside the stated scale |
| Serum IL-33 as a biomarker | Not evaluable | Not in the delivery; needs a new assay (kept as a target-engagement development item) |
| HGF (top prognostic) as PD | Ruled out | Not IL-33-regulated in HUVEC; the HGMEC signal is inconsistent |
| Intracellular damage proteins | Ruled out | Non-specific; possible pre-analytical artefact |
| Adhesion molecules as primary PD | Deferred | RNA statistics unreliable; sVCAM-1/sICAM-1 not outcome-linked; transient |
| sST2 as a PD marker | Exploratory only | Weak, unreliable IL-33 induction in vitro; decoy-receptor biology |
| Off-target or safety signal from antibody-alone RNA-seq | Ruled out at transcript level | Noise-level DE; gene-set shifts flip direction between cell types; no inflammatory activation |
| Block-level post-mortem statistics | Rejected | Pseudo-replication (ICC 0.40–0.82) overstates significance; e.g. EDN p = 0.0004 naive vs 0.038 in a mixed model |
| Delivered adjusted p-values; ranking by OR | Replaced | Duplicates in the BH correction; OR scale is undefined ("per log unit") |
| The "24h" sheet as 24 h data | Rejected | It is a re-ordered duplicate of all contrasts at both timepoints |
| Filtering RNA-seq on AveExpr, or reading p-values for SE-flagged genes | Rejected | AveExpr is pooled across all 114 libraries; 382 genes have degenerate SEs |

# 7. Data integrity: what must be fixed before anyone relies on these files

The full log is in the workbook (sheet `Data_integrity_log`, 21 items).

**RNA-seq.**
- The `6h` and `24h` sheets are identical copies containing both timepoints. The `6h` sheet is padded with blank rows to Excel's row limit, which looks like truncation but is not.
- The HGMEC IL-33-vs-control contrast and the isotype contrasts are missing.
- "Vehicle" and "Nontreated" labels conflict.
- The single pooled model across four very different cell types leaves 382 genes with degenerate standard errors. For example, CXCL1 has log2FC +8.2 but P = 0.994, and E-selectin +11.2 with P = 0.21.
- AveExpr is pooled across all 114 libraries.
- Design limits: single donors, a single concentration, reduced IL-33 only, and a DMSO arm that is meaningless for an antibody.

**Serum.**
- The `composite_endpoint_0/1` columns are undocumented. I infer they are per-group below-LOD fractions (56 non-events, 44 events).
- IL-33 and 14 other panel assays are absent.
- 27 proteins are duplicated inside the multiplicity correction.
- The OR scale is undefined.
- There is a global upward shift.
- Cohort scope is single-centre, n = 100, pre-vaccination and one timepoint.

**Post-mortem.**
- Pseudo-replication (74 blocks from 31 donors).
- Donor-level fields appear only on the first block, in merged cells.
- IL-33 scores of 5.5 exceed the stated 0–5 scale, and one score is a live spreadsheet formula.
- Columns U–W are derived copies of other columns.
- Disease labels contradict the pathology in 9 of 31 donors. Four "COVID-negative pneumonia" donors have no pneumonia recorded; three "non-pneumonia" donors have pneumonia or pulmonary infection; two COVID+ donors have no acute lung pathology.
- Age is a confounder.

# 8. How the analysis was done

**RNA-seq.**
- I audited both workbooks: inventory, duplication, and consistency of t with P. The implied total df is 85, which fits 76 residual df plus moderated prior df.
- I flagged genes whose standard error exceeds 3× the expression-matched trend.
- I estimated inhibition from the contrast vs isotype+IL-33, which shares no wells with IL-33 vs vehicle.
- I ran Hallmark GSEA (fgsea).

**Serum.**
- I mapped Olink names to genes and collapsed to unique proteins using a pre-specified panel priority, then recomputed BH.
- I quantified the global shift and tested enrichment with Fisher and Wilcoxon tests.

**Post-mortem.**
- I parsed merged cells and formulas and forward-filled donor fields.
- I aggregated to donor means and used rank tests, with age/sex-adjusted models and a block-level mixed model as sensitivity analyses.
- I curated acute lung pathology and DAD from the autopsy text.

Code is in `analysis_code/`.

**Figures.**
- Fig. 1: in vitro pharmacology.
- Fig. 2: serum proteomics.
- Fig. 3: post-mortem IL-33 by donor.
- Fig. 4: 6 h vs 24 h kinetics behind the PD sampling time.

![Fig. 1 — AX-1177 reverses the IL-33red endothelial programme; antibody alone is inert.](figures/Fig1_invitro_pharmacology.png)

![Fig. 2 — Serum: sST2 stands out against a global severity shift; the IL-33 endothelial set is not enriched; type-2 markers are null.](figures/Fig2_serum_proteomics.png)

![Fig. 3 — Lung IL-33 by donor: present everywhere, not increased in COVID-19 (vascular trend lower), tracks age.](figures/Fig3_postmortem_IL33.png)

![Fig. 4 — Kinetics behind the PD sampling time.](figures/Fig4_kinetics_sampling_time.png)
