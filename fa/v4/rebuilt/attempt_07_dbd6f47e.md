# AX-1177 (anti-IL-33 mAb): portfolio audit — recommendation, defence and forward view

**Basis:** only the AX-1177 data package (methods annex, HUVEC IL-33 RNA-seq, 24-contrast RNA-seq workbook, serum proteomics, post-mortem lung IHC). Every number below was re-derived from those files; code, figures and tables accompany this report. Interpretation uses standard IL-33 biology (e.g., sST2 is the soluble decoy receptor for IL-33); any further outside context is labelled *[external]*.

---

## 1. Recommendation

**Keep AX-1177, but re-scoped and gated. Do not keep it as a "severe lower respiratory viral infection" programme.**

- **Stop** the COVID/viral-LRTI framing and any IND-enabling spend.
- **Re-scope** to the hypothesis our data actually support: *IL-33-driven endothelial inflammation in early severe pneumonia, in patients selected by high serum sST2, whatever the pathogen.*
- **Fund one time-boxed gate (about 2 quarters).** It relies mostly on material we already hold (stored enrolment sera, archived tissue RNA, archived count matrices), plus a focused pharmacology package.
- **Kill criteria are pre-agreed.** We drop the asset if either:
  - IL-33 itself (not just its decoy receptor) fails to track outcome, or
  - AX-1177 cannot block IL-33 when it is added after IL-33 exposure.

**Why this position is defensible.**

- **The molecule works.** AX-1177 completely neutralises the endothelial programme driven by reduced IL-33 at 6 h (median 100% reversal of strongly induced genes). It does essentially nothing on its own.
- **The pathway matters clinically.** The IL-33 pathway's endogenous decoy receptor, sST2, is the #2 of 1,063 serum proteins for predicting ICU/ventilation/death in hospitalised patients. This holds after adjusting for NEWS2.
- **The gap.** Our data do not show that IL-33 is *specifically* active in viral or COVID pneumonia:
  - tissue IL-33 is indistinguishable between COVID+ and COVID− pneumonia;
  - the IL-33-inducible programme is not over-represented among outcome-linked serum proteins.
- **Why not kill or continue as-is.** That gap can be closed quickly and cheaply. Killing now would throw away a mechanistically validated asset to save little. Continuing as-is would spend money on an indication claim the data do not support.

**Evidence at a glance**

| Dataset | What it supports | What it does not support / limits |
|---|---|---|
| In-vitro RNA-seq (HUVEC, HGMEC, A549, MCF7; 114 libraries) | AX-1177 neutralises the reduced-IL-33 endothelial programme: 100% at 6 h, 84% at 24 h. The same blockade is seen in glomerular microvascular cells. AX-1177 is inert on its own in 4 cell types. | One donor per primary cell; a single dose of antibody and IL-33; no lung cells; no oxidised IL-33; no vehicle arm in HGMEC. The pooled fit makes p-values unusable for 154 genes (their effects are real). |
| Serum proteomics (100 hospitalised COVID-19 patients, 44 events) | sST2 is #2/1,063 proteins (OR 3.02, FDR 0.0075, NEWS2-adjusted). Ten IL-33-inducible, AX-1177-reversible proteins are outcome-linked, giving a PD panel. Type-2 markers are null. | The in-vitro IL-33 programme is not enriched among outcome-linked proteins (p = 0.74). No IL-33 assay. Pre-vaccination, single centre, summary statistics only. |
| Post-mortem lung IHC (31 donors / 74 blocks) | IL-33 is abundant in endothelium and basal epithelium of elderly lungs. Granulocyte infiltrates mark pneumonia in general. | No COVID-specific IL-33 difference at donor level. Underpowered, with a ceiling effect, a single reader and confounding by age. |

---

## 2. The case for keeping: what our data establish

**2.1 AX-1177 fully neutralises reduced IL-33 in endothelium, early (Fig. 1).**

- **IL-33 drives a large endothelial programme.** IL-33red (30 ng/mL) in HUVEC gives:
  - 4,031 DE genes at 6 h (645 up ≥2-fold) and 1,836 at 24 h;
  - Hallmark TNFα/NF-κB NES +3.14 (padj 3×10⁻⁶⁰), plus IFN-γ/α, IL-6/JAK/STAT3, complement and coagulation;
  - Reactome IL-1-family/MyD88 signalling, consistent with ST2 signalling. Because AX-1177 abolishes the response and the isotype does not, the response is IL-33-dependent; this also excludes a contaminant (e.g., endotoxin) in the IL-33 preparation as the driver.
- **The induced genes look pathogenic:**
  - neutrophil chemokines (CXCL1/2/3/5/6/8);
  - GM-CSF (+10.3 log2), G-CSF (+8.3), IL-6 (+5.8), TNF (+7.9);
  - E-selectin (+11.2), VCAM-1 (+8.7), ICAM-1 (+6.0);
  - a pro-coagulant switch: tissue factor F3 +5.6, PAI-1 up, thrombomodulin down;
  - complement C3/CFB.
- **AX-1177 blocks it.** Dosed at 10 µg/mL (about 41-fold molar excess), added concurrently, and compared with isotype:
  - at 6 h, strongly induced genes are reversed by a median 100% (IQR 93–104%, n = 136);
  - at 24 h, by 84% (IQR 71–93%, n = 35);
  - Hallmark NF-κB NES goes to −3.05.
- **The blockade is not specific to one vascular bed.** In glomerular microvascular endothelium (HGMEC) the same programme is blocked: 1,460 DE genes at 6 h, NF-κB NES −3.66, concordance with HUVEC ρ = 0.62.

**2.2 AX-1177 is inert without IL-33 in four cell types.**

- Antibody-alone vs isotype gives 22–73 DE genes per contrast, against more than 4,000 for IL-33. Most are low-count noise.
- IL-33-responsive genes are unchanged (median log2FC −0.006 to +0.08).
- There is no NF-κB induction in HUVEC, so no sign of agonism or endotoxin-like activity. In HGMEC there is a small coordinated shift in NF-κB genes (median +4.6%, no single gene significant).
- There is no potentiation of IL-33: only 8/645 (6 h) and 4/314 (24 h) IL-33-induced genes are pushed further up, mostly non-coding.
- In IL-33-stimulated cells, 446 (6 h) and 206 (24 h) non-IL-33-responsive genes change with AX-1177 vs isotype. This is comparator noise, not off-target activity:
  - 81% of them are below-average expression;
  - they are uncorrelated with antibody-alone effects (r ≈ 0);
  - the shift comes from the isotype+IL-33 wells (r = −0.83).

**2.3 The IL-33 axis is among the most outcome-linked pathways in hospitalised patients (Fig. 2).**

- sST2: OR 3.02 (1.83–5.01) per log unit, FDR 0.0075. It ranks #2 of 1,063 unique proteins (after HGF).
- The model is adjusted for age, sex and NEWS2, so sST2 adds information beyond the clinical score.
- Other IL-1-family receptors follow: IL-18R1 ranks #22 and IL-1R2 #24.

**2.4 We already have a patient-measurable PD panel.**

- **Ten serum proteins meet all three tests:** IL-33-inducible in endothelium, reversed by AX-1177 (significantly in HUVEC; in HGMEC by effect size, since some HGMEC SEs are inflated), and associated with outcome.
  - IL-6, OPG, IL-18R1, CCL20, MCP-3 (CCL7) and IL-1β: FDR 0.012–0.046.
  - IL-8 and PTX3: FDR 0.023 and 0.012.
  - MCP-1 and E-selectin: FDR 0.051 and 0.091.
- **IL-33 also up-regulates its own receptor gene.** IL1RL1 rises +1.6 log2 in HUVEC and AX-1177 reverses it (−1.7). This is a plausible route by which sST2 partly reports IL-33 activity; it still needs protein-level confirmation.

**2.5 The target reservoir is in the right compartments of the at-risk population (Fig. 3).**

- IL-33 protein is high in endothelium in every group (donor medians 4.8–5.5 on a delivered scale that tops out at 5.5).
- It is also high in basal airway epithelium of elderly lungs (64–98 y).

---

## 3. The case against the current indication, and our answers

| Committee challenge | What our data say | Our answer |
|---|---|---|
| "Is IL-33 actually active in viral/COVID pneumonia?" | At donor level, tissue IL-33 does not differ across COVID+ pneumonia, COVID− pneumonia and non-pneumonia. Kruskal–Wallis p = 0.65 (epithelium), 0.11 (endothelium), 0.16 (VSM); age-adjusted GEE p = 0.15–0.49. Age is the main driver of endothelial/VSM IL-33 (ρ = 0.55, p = 0.001). | Inconclusive, not negative. IHC sees stored nuclear IL-33, not released IL-33. For endothelial IL-33, 52% of donors sit at the scale ceiling; power is only 22–45% for moderate effects. The direction fits release: endothelial IL-33 is lower in COVID+ (d = −0.6) and lower where neutrophils are dense (partial ρ = −0.43, nominal). That is a hypothesis only. **We stop claiming COVID specificity.** |
| "Isn't sST2 just a severity marker?" | sST2 is prognostic, not causal. 169 of 1,063 proteins associate with outcome, so the severity proteome is broad (IL-6, HGF, neutrophil and cell-injury proteins). | Agreed. Gate 1 measures IL-33 itself in the same stored sera. |
| "Does the in-vitro IL-33 programme show up in patients?" | Not preferentially. 19% of IL-33-inducible, AX-1177-reversible proteins are outcome-linked, against 17% of all others (Fisher OR 1.1, p = 0.74). The strongest IL-33 outputs (G-CSF, CXCL5/6, CXCL10, VCAM-1) are null. | This is the strongest argument against a broad claim, and we do not make it. The overlap is generic NF-κB biology, so the PD panel can only be read against placebo. |
| "Could blocking IL-33 do harm?" | sST2 is a decoy, so high sST2 could mean IL-33 is already being sequestered, i.e. protective IL-33 signalling is lost. Amphiregulin is also higher in severe patients (OR 2.0–2.2, FDR 0.03–0.045); *[external]* it is a tissue-repair factor downstream of IL-33. | This is a real, unresolved directional risk. The in-vivo gate must include viral-clearance and repair endpoints before any patient is exposed. |
| "Is there a treatment window in hospitalised patients?" | Neutralisation is 100% at 6 h but 84% at 24 h. ISGs (CXCL10, IFIT1) and complement (C3, C1S) partly escape. TNF is induced +7.9 log2 at 6 h, so secondary loops start early. | Front-load treatment: the indication is defined as *early* (at admission), and Gate 2 tests delayed addition. If AX-1177 fails when given ≥2 h after IL-33, the acute indication is not viable. |
| "How strong is the pharmacology?" | One donor per primary cell type; one antibody and one IL-33 concentration; no pre-incubation. No lung microvascular cells, no airway-epithelial IL-33 stimulation, no oxidised IL-33, and no vehicle arm in HGMEC. | Enough for proof of mechanism, not for potency or translatability. Gate 2 addresses this. |
| "Is the cohort relevant today?" | 100 patients, single centre, pre-vaccination COVID-19. | Replicate in a multi-centre, post-vaccination pneumonia cohort (all pathogens) before fixing a Phase 2 design. |

---

## 4. Forward view: which indication our data point at

**What the data point at:**

- **Cell type: the endothelium.**
  - Every piece of functional IL-33 biology we hold is endothelial (macro- and microvascular).
  - The patient signals are sST2 plus endothelial and neutrophil injury proteins.
- **Biology: neutrophil-recruiting, pro-coagulant, complement-activating vascular inflammation, not type-2.**
  - Serum type-2 markers are null: IL-5 OR 1.00, eotaxin-1 1.08/0.98, eotaxin-2 0.92, TARC 0.85, tryptase 1.07.
  - In tissue, eosinophil infiltrates (EDN, MBP) track pneumonia as such. They are equal in COVID+ and COVID− pneumonia; pneumonia vs non-pneumonia p = 0.0045 (EDN) and 0.0058 (MBP), and neutrophil elastase behaves the same way (p = 0.0067).
  - Mast-cell tryptase does not differ (p = 0.48).
- **Pathogen: none in particular.** COVID+ and COVID− pneumonia look alike in tissue for every IL-33 and granulocyte readout (all p ≥ 0.15).
- **Timing: early.** Both the IL-33 programme and its blockade are front-loaded (6 h ≫ 24 h).

**Proposed re-scoped indication:** *early severe pneumonia (any pathogen) in hospitalised adults with an sST2-high endothelial-inflammatory phenotype.*

- The goal is to prevent progression to ICU admission, invasive ventilation or death (an ARDS-prevention setting).
- This replaces "severe lower respiratory viral infection". It is broader on pathogen and narrower on biology, because it is biomarker-defined.
- The HGMEC data suggest the same blockade applies in extrapulmonary microvasculature. That fits a systemic-endotheliopathy framing but is not a separate indication.

**What we would be dropping if the gates fail, and why.**

- *What:* a clean, functionally validated neutraliser of reduced IL-33. It has demonstrated blockade of IL-33-driven endothelial inflammation and is linked to a top-ranked prognostic human biomarker of its own pathway.
- *Why:* we could not show that IL-33 itself is active in the patients we would treat, at the time we could treat them.

---

## 5. Biomarkers, sampling timepoint, and what can go into patients

**Sampling timepoint: enrolment / hospital admission, before dosing, as close to admission as possible and before escalation of care.**

- Serum is handled as in the discovery cohort (clotted, centrifuged, −80 °C), with a standardised clotting time.
- **Why this timepoint:**
  1. The only patient evidence we hold comes from enrolment serum, and it predicts 30-day outcome independently of NEWS2.
  2. In vitro, both the IL-33 programme and its neutralisation peak early: 4,031 vs 1,836 DE genes at 6 h vs 24 h, and 100% vs 84% reversal. The biology and the drug's leverage are both front-loaded.
  3. Post-mortem tissue is end-stage and cannot inform timing.
- **Secondary draws:** PD samples at about 24 h and day 3 on treatment.
- **Also record:** days since symptom onset, and concomitant immunomodulators (dexamethasone, IL-6R/JAK inhibitors). These move IL-6-pathway markers independently of AX-1177.

| Marker | Evidence in our data | Role in patients | Can it go into patients? |
|---|---|---|---|
| **sST2** (serum) | #2/1,063; OR 3.02 (1.83–5.01), FDR 0.0075, NEWS2-adjusted. IL1RL1 mRNA up with IL-33 and reversed by AX-1177 (SE inflated, needs confirmation). | **Prognostic enrichment / stratification** at enrolment; exploratory PD. | **Yes, as an enrichment marker** once an absolute immunoassay cut-off is set in an independent cohort (*[external]* sST2 immunoassays are already in clinical use in cardiology). **Not** as a predictive/companion marker: we have no treatment-response data. |
| **IL-33 endothelial PD panel:** IL-6, OPG, IL-18R1, CCL20, MCP-3, IL-1β, IL-8, PTX3, MCP-1, E-selectin | Induced by IL-33 in endothelium, reversed by AX-1177 in HUVEC and HGMEC, and outcome-linked (FDR 0.012–0.091). E-selectin is the only endothelium-restricted member. | **Pharmacodynamic / proof of mechanism:** change from baseline vs placebo. | **Yes, exploratory.** They are not IL-33-specific (NF-κB), so read only in a randomised comparison. IL-6 is confounded by IL-6R blockade and steroids. |
| **Free IL-33, oxidised IL-33, total IL-33; IL-33:sST2 and IL-33:AX-1177 complexes** | Not measured: there is no IL-33 assay in the Olink delivery. | **Target engagement**; candidate *predictive* enrichment. | **Not yet.** Assays must be built and qualified first (Gate 1). |
| Neutrophil/injury proteins (CLEC5A, PRTN3, CD177, LCN2, OSM, HGF, vWF, ANGPT2) | Prognostic (FDR 0.004–0.052); not IL-33-specific. | Covariates / stratification. | Research use only; not an IL-33 readout. |
| Type-2 markers (IL-5, eotaxins, TARC, tryptase, IL-5Rα; blood eosinophils) | Null in serum; tissue eosinophilia is pneumonia-generic. | None. | **No.** Do not use for selection in this indication. |
| Tissue IHC (IL-33 by compartment; granulocyte panels) | No disease discrimination at donor level; ceiling effect; block ICC 0.44–0.60; single reader; post-mortem only. | None. | **No.** Translational research only. |

---

## 6. Next studies and decision gates

**Gate 1 — Is IL-33 itself active in the patients we would treat?** (0–6 months; existing material; low cost; this gate decides keep or drop.)

1. **IL-33 forms in stored sera.** In the 100 stored enrolment sera, measure free reduced IL-33, oxidised IL-33, total IL-33 and IL-33:sST2 complex. Also run sST2 on an absolute immunoassay, bridged to Olink.
2. **Incremental value of sST2.** Obtain patient-level NPX and test whether sST2 (and IL-33 forms) add prognostic value beyond NEWS2 + IL-6 + HGF (ΔAUC, NRI).
3. **IL-33 programme in tissue.** Score the AX-1177-reversible IL-33 endothelial signature in the archived tissue RNA: 22 blocks with Zr4940 IDs (9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia). Re-score IL-33 IHC with two blinded readers on the annex 0–5 scale.
4. **Re-fit the RNA-seq.** Refit per cell line from the archived count matrix, to settle significance for SELE, VCAM1, ICAM1, IL-8, MCP-1, PTX3 and IL1RL1 and to freeze the PD gene set.

- **Go:** free or complexed IL-33 is associated with outcome independently of NEWS2 (e.g., FDR < 0.05) and correlates with sST2 and with the PD panel, **or** the IL-33 signature is raised in pneumonia lungs.
- **Kill:** no IL-33 form tracks outcome **and** sST2 is unrelated to IL-33 forms. That would make the sST2 signal non-specific.

**Gate 2 — Can AX-1177 block IL-33 in the right cells, forms and time window?** (3–9 months; runs in parallel.)

1. **Concentration–response.** IC50/IC90 against reduced IL-33, full-length and protease-processed IL-33, and oxidised IL-33, with a functional readout suited to each. Use human lung microvascular endothelium and primary bronchial epithelium, ≥3 donors each, with vehicle arms in every line.
2. **Therapeutic-window design.** Antibody added at −1 h (pre-incubated), 0, +1, +3 and +6 h relative to IL-33. Read out at 6 h and 24 h; measure the PD panel and sST2 in supernatants.
3. **Explain the 24 h escape.** Add anti-TNF and anti-IFNAR controls to test whether the escape is IL-33-independent.

- **Go:** ≥80% suppression of the PD panel when AX-1177 is added ≥2 h after IL-33.
- **Kill:** <50% suppression when AX-1177 is added ≥2 h after IL-33, which would mean no plausible acute window.

**Gate 3 — Efficacy without harm, and a population that replicates.** (6–12 months; only if Gates 1 and 2 pass.)

1. **In-vivo viral pneumonia model** (influenza or SARS-CoV-2). Use a cross-reactive surrogate if AX-1177 does not bind rodent IL-33; confirm from the biologics file.
   - Efficacy endpoints: vascular leak, lung injury, survival, PD panel.
   - **Safety endpoints:** viral titre and repair markers (amphiregulin).
2. **Multi-centre, post-vaccination severe-pneumonia cohort** (COVID, influenza, RSV, bacterial CAP). Replicate sST2, fix a cut-off, record days since onset, and adjust for renal function and NT-proBNP.

- **Go to IND-enabling:** efficacy without impaired viral clearance, plus sST2 replication.

**End-state, only if all gates pass:** an sST2-enriched, randomised, placebo-controlled Phase 2a in early hospitalised severe pneumonia.

- Sample at enrolment (pre-dose), ~24 h and day 3.
- Co-primary readouts: the PD panel and safety (viral clearance).
- Clinical secondary: 30-day ICU/IMV/death, matching our discovery endpoint.

---

## 7. What we considered and ruled out

| Considered | Ruled out because (our data) |
|---|---|
| Continue as-is in severe viral LRTI / COVID-19 | Tissue IL-33 is not COVID-specific. The IL-33 programme is not enriched in the severity proteome. The cohort is pre-vaccination and single-centre. sST2 is non-specific on its own. |
| Type-2 airway indications (asthma, COPD, viral-triggered exacerbations) | No epithelial IL-33 experiment exists (A549/MCF7 got antibody only). Serum type-2 markers are null. Tissue IL-33 is unrelated to COPD/asthma history (p = 0.21/0.34). Eosinophils track pneumonia, not airway disease. We would be entering on others' data. |
| Eosinophil/mast-cell-driven COVID pathology | Tryptase is null in tissue (p = 0.48) and serum (OR 1.07). EDN/MBP are equal in COVID+ and COVID− pneumonia. |
| Renal/glomerular endothelial indication (from HGMEC) | AX-1177 does block a concordant programme in HGMEC, but there is no vehicle arm, the effect is largely gone by 24 h (8% of genes), and we have no renal patient data (KIM-1 only nominal: OR 1.66, FDR 0.11). |
| Tissue IL-33 IHC as a selection biomarker | Post-mortem only; ceiling effect; ICC 0.44–0.60; single reader; confounded by age. |
| Ranking serum biomarkers by OR size (CSF-1 90, GSTP1 24.6, CTSS 23.2, SEMA4C 20.9, CALR 19.7) | Per-log-unit ORs depend on assay scale. Many of these are intracellular proteins (lysis or ex-vivo release into serum). We ranked by z instead. |
| Counting cross-panel duplicates as independent hits | 178 "significant" assays are 169 unique proteins. Duplicates agree (IL-6 OR 2.07–2.31 on 4 panels). |
| Measuring neutralisation against "IL-33 alone" | That contrast shares the IL-33 group with the signature contrast, so it inflates reversal (slope −0.82 vs −0.62 against isotype at 6 h). We used isotype as comparator throughout. |
| Treating IL-33-repressed genes as "resistant to AX-1177" | Winner's-curse artefact: the apparent isotype effect of +0.5 to +1.0 log2 disappears (+0.04 to +0.05) in independent wells. |
| AX-1177 agonism / off-target activity | Only 22–73 DE genes, mostly low-count; IL-33-responsive genes unchanged. Hallmark-level shifts are small (≤7.5% median; 0–1 significant genes per set) and inconsistent in direction across lines. We flag this for vehicle arms and cell counts; we do not treat it as pharmacology. |
| "Compound_47 vs DMSO" as a vehicle control | DMSO is not the antibody's vehicle; PBS and isotype are the relevant controls. |
| Lost RNA-seq data (6h sheet at Excel's row limit) | Checked: the extra rows are blank padding. The "6h" and "24h" sheets are identical and each holds both timepoints. |
| Block-level post-mortem statistics | Pseudo-replication: 3 donors contribute 24/74 blocks. It fabricates significance (endothelial IL-33 p = 0.028 block-level vs 0.114 donor-level). |
| High sST2 as proof that IL-33 drives disease | sST2 is a decoy receptor. High levels are equally consistent with IL-33 being sequestered, so direction must be tested first. |

---

## 8. Data-package issues the committee should know

1. **RNA-seq: pooled single fit.** One voom/limma fit across four cell types gives 154 genes implausibly large standard errors (implied SE up to 16,535 log2 units, against a median of 0.34). Most are cell-type-restricted markers or strongly induced IL-33 targets, and they include the canonical endothelial IL-33 targets and IL1RL1.
   - Their fold-changes replicate in independent wells (r = 0.97, slope 0.96), so the effects are real and only the p-values are unusable.
   - The delivered p-values therefore *understate* the evidence for E-selectin, VCAM-1, ICAM-1, IL-8, MCP-1 and PTX3.
   - Fix: request the count matrix and refit per cell line.
2. **RNA-seq: design limits.**
   - HGMEC has no vehicle arm.
   - One donor per primary cell type.
   - A single antibody and IL-33 concentration, with no pre-incubation.
   - Epithelial lines never received IL-33.
   - The "6h"/"24h" sheet names are misleading (both sheets hold both timepoints).
   - Contrast labels say "Nontreated" where the annex says "Vehicle".
3. **Serum proteomics: statistics as delivered.**
   - Summary statistics only, with no IL-33 assay.
   - 27 proteins are duplicated across panels, and BH was applied across duplicates.
   - ORs per log unit cannot be compared between assays (log base not stated).
   - `composite_endpoint_0/1` are per-group missing/<LOD fractions (denominators 56/44).
4. **Serum proteomics: cohort.** Pre-vaccination, single-centre; no information on steroid/IL-6R use or time from symptom onset.
5. **Post-mortem: scoring and parsing.**
   - Scores run to 5.5 with quarter values, outside the annex's 0–5 scale (an undocumented transform). The numeric EPX/NE/tryptase columns equal the "+" score plus 0.5.
   - Donor-level fields sometimes sit on non-first blocks.
   - Donor 1905 lacks SARS-CoV-2 status.
   - Blocks are unevenly sampled (1–8 per donor).
   - Single reader.

---

## Appendix A — How the analyses were done

- **RNA-seq.**
  - Re-validated the delivered statistics: p vs t at df ≈ 85 (76 residual + prior), and BH exact within contrast.
  - Implied SE = |logFC/t|.
  - IL-33 signature: HUVEC IL-33 vs vehicle, adj.P < 0.05 and |log2FC| > 1.
  - Neutralisation: −(AX-1177+IL-33 vs isotype+IL-33) / (IL-33 vs vehicle); these use four independent well sets. "Strong" genes: adj.P < 10⁻⁶ and log2FC > 2.
  - Selection-bias check: genes selected at one timepoint, evaluated at the other.
  - GSEA: fgsea on the moderated t, MSigDB Hallmark and Reactome.
- **Proteomics.**
  - De-duplicated 1,094 assays to 1,063 proteins (best assay per protein).
  - z = ln(OR)/SE, with SE from the 95% CI; reproduces the delivered p (median |Δlog10p| = 2×10⁻⁵).
  - Olink names mapped to HGNC symbols to link with RNA-seq.
  - Enrichment by Fisher's exact test.
- **Post-mortem.**
  - Donor-level fields forward-filled and aggregated across blocks; IHC "+" scores parsed; ND treated as missing; donor means.
  - Kruskal–Wallis and Mann–Whitney tests.
  - Rank-based and GEE (exchangeable, donor-clustered) models with age.
  - ICC(1) for block agreement; power by simulation.

## Appendix B — Deliverables

- `AX-1177_portfolio_audit_report.md` / `.pdf` — this report.
- `figures/fig1_invitro_neutralisation.png`, `fig2_serum_proteomics.png`, `fig3_postmortem.png`, `fig4_integrity_checks.png`.
- `tables/AX-1177_supporting_tables.xlsx`:
  - DE summary;
  - per-gene neutralisation;
  - GSEA;
  - ranked serum proteins with in-vitro mapping;
  - biomarker shortlist;
  - donor-level post-mortem table and tests;
  - integrity log.
- `tables/key_statistics_audit_trail.txt` — every number cited in this report, recomputed by script.
- `code/` — scripts that regenerate figures and tables from the source files; a from-scratch re-run reproduced all outputs.
