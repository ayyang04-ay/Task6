# AX-1177 (anti-IL-33 IgG1; research code Compound_47) — portfolio-audit position

**For:** Respiratory portfolio audit committee  **Scope:** viral lower-respiratory-tract disease (LRTD) programme
**Evidence base:** only our four delivered datasets (mmc2–mmc5) and the Methods Annex, taken as ground truth. Every number below is regenerated from the raw files by `code/run_all.sh`; supporting tables are in `AX-1177_evidence_tables.xlsx`; figures are in `figures/`.

---

## 1. Recommendation

**Do not keep AX-1177 in the portfolio as a viral-LRTD asset. Stop LRTD-directed development spend now.**

**What happens to the molecule:** by default it is terminated after a close-out review of up to 12 weeks. That review runs no new experiments. It only retrieves and re-analyses data we already hold:
- the 100 serum assays analysed but left out of the delivery, which may include IL-33 itself;
- the archived RNA-seq count matrices;
- the 22 post-mortem lung RNA samples.

Termination is reversed only if the pre-set criteria in §6.6 are met.

**Why, in one sentence:** our data show clearly that AX-1177 neutralises IL-33 in cultured endothelium. They do not show that IL-33 is active in, or drives, viral LRTD:
- the target was never quantified in patients;
- IL-33 in lung tissue is the same in COVID-19 as in controls;
- the IL-33-driven programme the antibody blocks is not what predicts poor outcome.

| What an LRTD programme needs to be true | Our data | Key numbers |
|---|---|---|
| **1.** AX-1177 neutralises IL-33 signalling | **Supported (strong)** | IL-33red changes 4,031 HUVEC genes at 6 h. AX-1177 reverses 2,884 of them against the isotype arm (r = −0.80), leaving a median ~4% of the response. The same programme is blocked in glomerular microvascular cells. No reproducible effect of the antibody alone in 4 cell types. |
| **2.** IL-33 is released and active in the patients | **Not shown** | IL-33 is absent from the serum delivery, although it is on the Olink Inflammation panel; 100 analysed assays were omitted. Lung IL-33 staining does not differ between COVID-19 and non-COVID pneumonia (donor-level p = 0.92 / 0.16 / 0.15 for epithelium / endothelium / smooth muscle). |
| **3.** IL-33-driven biology tracks clinical outcome | **Not shown** | Proteins of the IL-33/AX-1177 programme predict ICU/ventilation/death no more often than other proteins (20.5% vs 16.9%; p = 0.43). The most endothelium-specific ones (VCAM-1, ICAM-1, E-selectin) do not predict at all. Intracellular "leakage" proteins do (28.6% vs 13.6%; p = 1.5×10⁻⁵). |
| Scope: "viral LRTD" | **Only COVID-19** | All human data are from SARS-CoV-2: 100 patients, pre-vaccination, single centre. There are no influenza, RSV or other viral data. |

**The best pro-asset fact, kept on the record:** soluble ST2 (sST2, the IL-33 decoy receptor) is the **#2 predictor of poor outcome out of 1,063 proteins**. Odds ratio (OR) 3.02 per log unit, 95% CI 1.83–5.01, FDR 0.0075; it is one of only two proteins surviving Bonferroni correction. This is why I recommend a short close-out rather than immediate termination. But sST2 is not IL-33-specific, and it cannot carry a programme on its own.

---

## 2. What each dataset shows

### 2.1 In vitro transcriptomics (mmc4/mmc5): the pharmacology is clean

![Fig 1](figures/Fig1_reversal_scatter.png)

**IL-33red triggers a strong endothelial activation programme in HUVEC** (IL-33red = reduced IL-33, 30 ng/mL):
- 4,031 genes change at 6 h and 1,836 at 24 h (FDR < 0.05).
- Enriched pathways (Hallmark normalised enrichment scores): TNFα/NF-κB 3.17, IFN-γ 2.84, inflammatory response 2.74, IFN-α 2.73, IL-6/JAK/STAT3 2.64, complement 2.26, coagulation 1.60.
- Adhesion molecules: E-selectin (SELE) +11.2 log2FC, VCAM-1 +8.7, ICAM-1 +6.0.
- Chemokines and cytokines: CCL20 +9.2, CXCL8 +8.2, CSF2 +10.3, TNF +7.9, IL6 +5.8.
- Pro-coagulant shift: tissue factor (F3) +5.6, PAI-1 +1.7, thrombomodulin −1.0.

**AX-1177 reverses the programme** (10 µg/mL, a ~41-fold molar excess, added at the same time as IL-33):
- The clean comparison is AX-1177 + IL-33 vs isotype + IL-33, because these arms share nothing with the IL-33-vs-vehicle contrast.
- At 6 h: r = −0.80; 2,884 of 4,031 genes significantly reversed, 12 moved the same way; residual IL-33 response about 4% (median).
- At 24 h: r = −0.65; 694 of 1,836 reversed; residual about 9%.
- The delivered "AX-1177 + IL-33 vs IL-33" contrast shares the IL-33 arm and inflates apparent reversal (r = −0.93). At 24 h the isotype arm itself shows only 77% of the IL-33 response, so only isotype-controlled contrasts should be quoted.

**Glomerular microvascular endothelium (HGMEC):** at 6 h, 942 of 964 shared genes are reversed (r = −0.66). There is no HGMEC vehicle arm and no HGMEC IL-33-vs-control contrast was delivered, so the HGMEC IL-33 response is *inferred*, not measured.

**Timing:** the response is early and transient (Fig. 2).
- HUVEC: 4,031 → 1,836 genes from 6 h to 24 h.
- HGMEC, antibody-reversible genes: 1,460 → 269.

**Specificity of the antibody alone:** 16 contrasts (vs isotype, PBS and DMSO) in 4 cell types give 14–73 "significant" genes each. Of these, 82–100% are statistical artefacts, either:
- trivial shifts in highly expressed genes (e.g., AKR1C2 log2FC 0.11 at FDR 10⁻⁹⁴), or
- noisy changes in barely expressed transcripts.

None replicates across timepoint or cell line (r ≈ 0), none correlates with the IL-33 programme (|r| ≤ 0.09), and the NF-κB sentinels (NFKBIA, TNFAIP3) are flat. So there is no sign of agonism or endotoxin-like contamination. Pathway-level proliferation and metabolism shifts flip sign depending on which control arm is used, which points to culture-state noise. A modest, consistent shift in HGMEC should be rechecked in multi-donor work.

**Not addressed by these experiments:**
- epithelium (A549 and MCF7 never received IL-33);
- oxidised IL-33;
- potency (one concentration only);
- adding the antibody *after* IL-33;
- donor variation (one donor per primary cell type, at different passages).

### 2.2 Clinical serum proteomics (mmc2): a severity signal, not an IL-33 signal

![Fig 3](figures/Fig3_serum_landscape.png)

**Cohort:** 100 patients hospitalised with COVID-19; 44 met the composite endpoint (ICU, invasive ventilation or death within 30 days). Models are adjusted for age, sex and NEWS2.

**The outcome signal is broad:**
- 893 of 1,094 ORs are above 1; 169 unique proteins are significant at FDR < 0.05.
- Top hits: HGF, sST2, HDGF, SEMA4C, PTX3, ANXA1, CLEC5A, NPM1, IL-6 (OR 2.1–2.3 on all four panels that measure it).

**The IL-33 endothelial programme is not enriched among outcome proteins:**
- Overall: OR 1.26, p = 0.43. Restricted to extracellular/membrane proteins: OR 1.54, p = 0.17.
- Of the 20 products most strongly induced by IL-33 and reversed by AX-1177 (≥16-fold), **4 are prognostic** (IL-6, OPG, CCL20, IL-8).
- **16 are not**, including VCAM-1 (FDR 0.61), ICAM-1 (0.25), E-selectin (0.09), G-CSF (0.40) and CXCL10 (0.42).

**Intracellular-only proteins are 2.5× enriched** among outcome hits (e.g., CALR, GSTP1, PRDX1/6, NPM1, CASP8). That is consistent with cell injury and/or ex-vivo release into clotted serum.

**Other axes are null:**
- Type-2/eosinophil: IL-5 OR 1.00 (p = 0.997), eotaxin p = 0.84, CCL17 p = 0.39.
- Kidney and cardiac markers: KIM-1 (FDR 0.11) and NT-proBNP (FDR 0.15) are not significant.

### 2.3 Post-mortem lung immunohistochemistry (mmc3): IL-33 is everywhere and not different in COVID-19

![Fig 5](figures/Fig5_postmortem_donor_level.png)

**Material:** 31 donors (16 COVID+, 10 COVID− "pneumonia", 5 COVID− "non-pneumonia"); 74 blocks; ages 64–98; one reader. The donor is the unit of analysis.

**IL-33 is high in all groups.** The endothelial score sits at the ceiling (5.5) in 39 of 74 blocks.

**No COVID-specific difference.** Comparing COVID+ with COVID− pneumonia:
- basal epithelium p = 0.92, endothelium p = 0.16, vascular smooth muscle p = 0.15 (COVID+ trends lower);
- no effect after adjusting for age.

**Age confounds the scores.** Endothelial and smooth-muscle IL-33 rise with age (ρ ≈ +0.55, p = 0.001).

**Inflammatory cells mark pneumonia, not COVID-19.** Neutrophil elastase, IL-5Rα⁺ cells and eosinophil granule proteins separate pneumonia from non-pneumonia (p = 0.005–0.009), with no difference between COVID+ and COVID− pneumonia (p ≥ 0.44).

**One hypothesis-only observation:** endothelial IL-33 is lower where the autopsy documents lung inflammation (4.88 vs 5.50; p = 0.008; n = 24 vs 7). This fits IL-33 being released during injury, but it is confounded by age, the score ceiling and mislabelled controls.

---

## 3. Audit findings on the data package

These limit how far any claim can go, whichever way the committee decides.

| # | Finding | Evidence | Consequence / fix |
|---|---|---|---|
| 1 | **The serum FDR was computed over 1,194 tests, but only 1,094 assays were delivered.** The annex says "all assays in the delivery". | The back-calculated BH denominator is exactly 1,194 at the top ranks. At least one omitted assay ranked in the top ~20 associations (p ≈ 2–3×10⁻⁴), and ~4 omitted assays would pass FDR 0.05. **IL-33 is absent** from the delivery. | The target's own clinical data are missing, and the delivered FDRs cannot be reproduced (recomputing gives 206 vs 178 hits). **Retrieve the full output with QC/LOD flags.** |
| 2 | **Post-mortem group labels contradict the autopsy diagnoses.** | 4 of 10 "COVID− pneumonia" donors have no pneumonia (1905, 1961, 1968, 1970). 3 of 5 "non-pneumonia" donors have acute/organising pneumonia, pneumonitis or pulmonary coccidioidomycosis (1976, 1956, 1944). Donor 1905 has no SARS-CoV-2 result. | The comparator groups are unreliable. **Re-adjudicate from the autopsy reports.** |
| 3 | **The IL-33 scores are hidden and not fit for purpose.** | IL-33 columns X–Z are hidden. Scores are undocumented composites; one cell is a live formula `=(2+4.5)/2`. Values reach 5.5 on a stated 0–5 scale; 53% of endothelial scores are at the ceiling; one reader. | The stain cannot discriminate. **Blinded re-read by two readers plus quantitative image analysis; score nuclear vs extranuclear IL-33.** |
| 4 | **One pooled model was fitted across four cell types.** | Key endothelial genes have implied standard errors in the top 0.5%: E-selectin 8.9, CXCL1 1,155, vs a median of 0.34. They are reported "non-significant" despite ±8–11 log2FC mirrored in independent arms. Meanwhile trivial changes reach FDR 10⁻⁹⁴. | Gene-level p-values are unreliable, and key genes (SELE, VCAM1, CXCL8, CCL2, PTX3, IL1RL1) are false negatives. **Refit per cell line from the archived counts.** |
| 5 | **Design gaps in the in vitro work.** | No HGMEC vehicle arm or IL-33 contrast. Epithelial lines never received IL-33. One donor per primary cell type (HUVEC P2, HGMEC P5). One antibody concentration, added concurrently only. DMSO is not the antibody's vehicle. | Claims about potency, timing, epithelium or generalisability cannot be made. **See Stage 1 (§6.6).** |
| 6 | **Pseudo-replication in the post-mortem data.** | Three donors supply 24 of the 49 COVID+ blocks. Block-level testing produces false positives: IL-5Rα COVID+ vs COVID− pneumonia p = 0.025 by block vs 0.49 by donor. | **Analyse per donor** (done here). |
| 7 | **Cross-panel duplicates are counted as separate tests and hits.** | 27 proteins are measured on 2–4 panels (IL-6 ×4). The two hidden rows are duplicates (HGF, IL-6). | Apparent breadth is inflated. **Deduplicate** (done here: 1,063 unique proteins). |
| 8 | **Gene annotation is wrong for many genes.** | 1,129 named genes carry clone-ID placeholders (e.g., OAS1, LTBR, MCAM). 1,713 symbols disagree with org.Hs.eg.db; 8,550 genes lack Entrez IDs. | Symbol-based lookups silently drop genes. **Key on Ensembl ID** (done here). |
| 9 | **AveExpr is averaged over all 114 libraries.** | CSF2 −3.2, SELE −1.7, VCAM1 −1.7. | Filtering on AveExpr would delete the core IL-33 genes. **Do not filter on it.** |
| 10 | **The OR scale is ambiguous.** | ORs are "per log unit" after log-transforming Olink output, which is already on a log2 scale. | ORs cannot be compared across assays (e.g., CSF-1 OR 90, CI 4–1,933). **Re-express per SD.** |
| 11 | **Pre-analytical risk in clotted serum.** | Processing time is not documented; intracellular proteins are 2.5× enriched among outcome hits. | **Use EDTA plasma with a fixed processing SOP in future.** |
| 12 | **Minor file hygiene.** | mmc5's "6h" and "24h" sheets each contain all 24 contrasts (one padded with blank rows to Excel's row limit, one partly re-sorted; the values reconcile exactly). mmc4 says "Nontreated" where the annex says "Vehicle". Two undocumented per-group fraction columns in mmc2. Donor notes for 2040/2045 sit on non-first rows, against the annex rule. | Cosmetic, but **record it in the audit file.** |

---

## 4. Defence: likely challenges and answers

**"AX-1177 abolishes IL-33-driven endothelial activation — isn't that enough?"**
It proves the drug hits its target, and we accept that fully. It does not show that the target matters in disease; any competent neutralising antibody would produce Fig. 1. An LRTD programme needs links 2 and 3 as well, and our data do not supply them.

**"sST2 is the #2 outcome predictor — doesn't that prove the IL-33 pathway is active?"**
It is our best signal, and it is robust: Bonferroni-significant and ranked #2 however duplicates are handled. But:
- sST2 is released under many inflammatory stresses, and it is itself an endogenous IL-33 blocker, so high sST2 can equally mean IL-33 is already neutralised;
- without IL-33 data, which are absent from the delivery, activation cannot be told apart from non-specific stress.

That is exactly what the close-out review checks.

**"IL-6, CCL20, OPG, PTX3 and IL-8 are all IL-33-inducible in our cells, and they all predict outcome."**
Those five are a selective pick:
- across all 78 measured IL-33-programme proteins, the hit rate is no higher than chance (p = 0.43);
- the most endothelium-specific readouts of IL-33 activity (VCAM-1, ICAM-1, E-selectin) do not predict outcome;
- those five are generic NF-κB products.

**"IL-33 is an alarmin — tissue staining can't show its activity."**
Agreed, which is why the tissue cannot support the case either. At donor level there is no COVID-specific difference. The one trend (lower endothelial staining with inflammation) is confounded by age, the score ceiling and mislabelled controls.

**"Our plan targeted viral LRTD, and these are viral LRTD patients."**
They are COVID-19 only: pre-vaccination, one centre, n = 100. There are no influenza, RSV or other viral data, and the "COVID-negative pneumonia" tissue is mostly bronchopneumonia of unrecorded cause. Extrapolating to viral LRTD is not supported.

**"Why not terminate today?"**
Because the deciding data already sit in our archive (the omitted assays including IL-33, the count matrices, the 22 lung RNAs). The close-out costs analyst time, not experiments, and defaults to termination. If the committee wants zero further spend, immediate termination is defensible on the current evidence.

**"Is there a safety reason behind this?"**
No. AX-1177 showed no reproducible off-target transcriptional activity; the decision is about the efficacy rationale. One point for any viral indication: IL-33 induces interferon-stimulated genes in endothelium (Hallmark IFN-α +2.73) and AX-1177 blocks this, so viral clearance would need monitoring.

---

## 5. What we are dropping, and why

We are dropping a well-behaved IL-33 neutraliser from a programme whose central premise is unsupported by our own data. The premise is that IL-33 drives progression of viral LRTD. Against it:
- the target was never measured in patients;
- IL-33 in diseased lung is indistinguishable from controls;
- what predicts poor outcome in hospitalised COVID-19 is broad injury and inflammation, not the IL-33 endothelial programme the antibody blocks;
- the human evidence is COVID-only.

We are **not** dropping it for safety or developability reasons. Its in vitro selectivity is clean, and that package should be archived intact for any future IL-33 programme or partnering discussion.

---

## 6. Forward view

### 6.1 What indication our data actually point at

Our data point at **a mechanism and a patient state, not a pathogen**:
- **Mechanism:** IL-33-driven activation of vascular endothelium (large-vessel and microvascular): adhesion molecules, chemokines, and a pro-coagulant shift. This is the only biology AX-1177 has been shown to block.
- **Patient state:** hospitalised patients with severe pneumonia at risk of progression to ICU, ventilation or death. This is the only clinical population with data, and high sST2 identifies those at greatest risk.
- **Pathogen:** nothing in the tissue is COVID-specific. Whatever IL-33 biology exists is shared with non-COVID pneumonia.

So the best-supported hypothesis is **sST2-high, severe, hospitalised pneumonia with endothelial involvement, whatever the pathogen**. That is narrower than "viral LRTD", is defined by the host response rather than the virus, and is **untested**. It should not be funded until links 2 and 3 are shown.

The data do **not** point to COPD/asthma, kidney or cardiovascular disease (§7).

### 6.2 What the next studies have to establish, in order

1. **The target is present.** IL-33 is released and free in target patients' blood at the time we would treat, shown by measurable free IL-33 or an IL-33-specific activity readout.
2. **The mechanism is active in patients.** IL-33-dependent endothelial activation is present in patient blood or lung, separable from generic NF-κB activation, and tracks outcome independently of NEWS2 and IL-6.
3. **The signal generalises.** sST2's prognostic value replicates in a contemporary (vaccinated, current standard of care), multi-pathogen cohort, using plasma and an absolute assay. If it does not, the indication narrows to where it holds.
4. **The drug works therapeutically.** AX-1177 reverses *established* activation (dosed after IL-33), across donors, in lung microvascular endothelium and primary airway epithelium, and blocks oxidised IL-33, at a potency compatible with achievable exposure.
5. **A PD readout exists.** A pharmacodynamic marker set moves with IL-33 blockade and can be measured in plasma.

### 6.3 Biomarkers, and which can go into patients

![Fig 4](figures/Fig4_candidate_markers_forest.png)

| Marker | Our evidence | Role | Into patients? |
|---|---|---|---|
| **sST2** (soluble ST2) | #2 of 1,063 outcome proteins; OR 3.02 (1.83–5.01), FDR 0.0075. The IL1RL1 transcript is +1.6 with IL-33 and −1.7 with AX-1177 (an artefact-affected gene). | **Prognostic enrichment / stratification at baseline**; candidate PD marker | **Yes, now**, as an exploratory stratification or enrichment factor (not a selection claim), moving to an absolute assay in plasma |
| **Free and total (drug-bound) IL-33** | None: absent from the delivery | **Target engagement** (total rises, free falls after dosing); selection if detectable | **Not yet.** Retrieve the omitted data; qualify a sensitive, drug-tolerant assay |
| **sE-selectin** | Endothelium-specific. +11.2 with IL-33, −11.0 with AX-1177 (HUVEC), −8.7 in HGMEC. Serum p = 0.02 (FDR 0.09) | **PD** of endothelial IL-33 blockade | Exploratory PD, after the per-cell-line refit confirms it |
| **CCL20, OPG, IL-6** (+ IL-18R1, IL-8, CSF-1) | IL-33-induced and AX-reversed in HUVEC and HGMEC; prognostic (FDR 0.012–0.037) | **PD panel** ("IL-33 endothelial score"); IL-6 also a prognostic covariate | Exploratory PD. Not IL-33-specific (also induced by IL-1β/TNF) |
| **PTX3** | OR 11.6 per log unit, FDR 0.012. Transcript +2.2 / −2.3 (artefact-affected) | Prognostic; candidate PD | Exploratory |
| **HGF** | #1 outcome protein (Bonferroni-significant); not IL-33-regulated in endothelium | **Prognostic covariate only** | Yes as a covariate; never as PD |
| sVCAM-1, sICAM-1, CXCL10, G-CSF | Strongly IL-33-induced and AX-reversed; **not** prognostic | PD only | Exploratory PD; not for selection |
| Viral load / clearance | AX-1177 blocks IL-33-induced endothelial interferon-stimulated genes | **Safety** monitoring in any viral indication | Yes (standard) |
| *Ruled out:* intracellular serum proteins, tissue IL-33 IHC, IL-5/eotaxin/CCL17, NT-proBNP, KIM-1 | Leakage-type, non-discriminating, or null | Use intracellular proteins only as a sample-quality ("lysis") covariate | No |

No marker in our data predicts *response* to AX-1177, because no patient has been treated. Stratified randomisation by sST2-high vs sST2-low is how that would be tested.

### 6.4 Sampling timepoint

- **Primary: enrolment, before dosing (Day 0).** This is the only timepoint at which our serum associations exist. Record time from symptom onset and from admission; these are absent from our dataset.
- **PD: 24 h (±4 h) after dosing;** Day 3 secondary, Day 7 for durability; outcome at Day 30 (matching our composite).
- **Rationale:** in our cells, IL-33-driven activation peaks early (6 h) and fades by 24 h (HUVEC 4,031 → 1,836 genes; HGMEC 1,460 → 269). AX-1177 reversal is still clear at 24 h (r = −0.65). Secreted products need hours to accumulate, so 24 h is the earliest practical time to see suppression in blood. This is an extrapolation from transcripts to circulating proteins, to be confirmed in Stage 1/2.
- **In vitro follow-up:** 6 h primary (largest dynamic range; HGMEC is only informative at 6 h), 24 h secondary.
- **Specimen:** EDTA plasma with a fixed processing time, plus serum for bridging.

### 6.5 Plan and decision gates

**Stage 0: archive close-out (≤12 weeks; analyst and pathologist time; no new experiments). Default outcome: terminate.**
- a. Retrieve the complete 1,194-assay output, patient-level NPX and QC/LOD flags; locate IL-33.
- b. Patient-level re-analysis: does sST2 stay prognostic after adding IL-6, HGF and a lysis index to NEWS2? What is the discrimination gain?
- c. Refit the transcriptomics per cell line; add the HGMEC IL-33-vs-isotype contrast; confirm the artefact-affected genes.
- d. Score the IL-33 endothelial signature in the 22 existing lung RNA samples (9 COVID+, 9 COVID− pneumonia, 4 non-pneumonia); re-adjudicate group labels; blinded double re-read of IL-33 IHC.
- **Continue only if** sST2 stays independently prognostic (p < 0.01 after IL-6, HGF and lysis adjustment) **and** at least one of:
  - IL-33 is detectable in ≥50% of event patients, or associated with outcome;
  - the IL-33 endothelial signature is higher in inflamed than in non-inflamed lung (donor-level, age-adjusted).
- Otherwise terminate and archive.

**Stage 1: decisive in vitro package (~6 months).**
- AX-1177 added 1, 3 and 6 h *after* IL-33.
- IL-33 and antibody dose–response (IC50).
- Oxidised and full-length IL-33.
- Lung microvascular endothelium plus HUVEC/HGMEC from ≥3 donors; primary airway epithelium (air–liquid interface) stimulated with IL-33.
- IL-1β/TNF comparator arms, to define IL-33-specific secreted PD markers.
- Virus-infected epithelium–endothelium co-culture.
- **Go** if ≥50% inhibition is retained when AX-1177 is added ≥3 h after IL-33 at achievable concentrations, and an IL-33-specific PD set exists.

**Stage 2: prospective observational cohort (~12–18 months).**
- Hospitalised adults with LRTD of any cause (SARS-CoV-2, influenza, RSV, hMPV, bacterial community-acquired pneumonia).
- EDTA plasma at Day 0, 24 h, Day 3 and Day 7; free/total IL-33, sST2 and the PD panel; composite outcome at Day 30.
- **Go** to an sST2-enriched Phase 2a (PD at 24 h, target engagement by IL-33, viral-load safety) only if sST2 and/or IL-33 is independently prognostic in ≥2 causes and a pre-specified cut-off raises the event rate ≥1.5×.

---

## 7. Considered and ruled out

**Decision options**
- *Keep in viral LRTD as is:* ruled out. Two of the three required links are missing, and the human data are COVID-only.
- *Pivot now to an sST2-enriched severe-pneumonia trial:* ruled out as premature. There is no target-engagement marker, no validated PD marker and no multi-pathogen replication.
- *Terminate immediately without the close-out:* defensible, but it gives up a near-zero-cost answer that already exists in our archive. Acceptable if the committee wants zero spend.

**Alternative indications**
- *COVID-19 specifically:* ruled out. The tissue shows nothing COVID-specific, and the cohort is pre-vaccination.
- *COPD / asthma / type-2 airway disease:* not supported by our data.
  - We have no epithelial IL-33 experiments.
  - IL-33 staining does not differ by COPD/asthma history (p = 0.13–0.18, 12 vs 19 donors).
  - Serum type-2 markers are null.
- *Kidney (diabetic kidney disease / acute kidney injury), prompted by the HGMEC data:* ruled out for now. The HGMEC IL-33 response is inferred, from a single donor, and KIM-1 and cystatin C show no association.
- *Cardiovascular / heart failure, prompted by sST2:* ruled out. sST2 here tracks inflammatory severity, NT-proBNP is not associated, and there are no cardiac data.
- *Sepsis / ARDS broadly:* not ruled in. It is consistent with the pathogen-agnostic hypothesis, but we have no non-pneumonia data.

**Candidate biomarkers**
- *HGF as PD:* not IL-33-regulated.
- *Intracellular serum proteins:* leakage or pre-analytical artefacts.
- *Very large per-log-unit ORs* (CSF-1 90, GSTP1 24.6, CTSS 23.2): reflect narrow assay ranges, not effect size.
- *Tissue IL-33 IHC:* ceiling effect, single reader, no discrimination.
- *IL-5 / eotaxin / CCL17:* null.
- *VCAM-1 / ICAM-1 / G-CSF / CXCL10 as enrichment markers:* null in serum (acceptable as PD only).

**Analytical shortcuts rejected**
- Block-level IHC statistics (pseudo-replication).
- The shared-arm "AX-1177 + IL-33 vs IL-33" contrast as proof of reversal.
- Filtering genes on AveExpr.
- Symbol-based gene mapping.
- Trusting the delivered FDRs.
- Counting cross-panel duplicates as independent hits.
- Reading antibody-alone "DEGs" as off-target biology.

---

## 8. Limitations of this review

- **No patient-level proteomics.** I could not adjust sST2 for IL-6, HGF or lysis, nor estimate discrimination; the OR scale is as delivered.
- **No count matrices.** The transcript conclusions rest on the delivered log fold-changes and on concordance between independent arms, not on a refit.
- **Data not in the package:** in vivo efficacy, PK, toxicology, affinity and potency (held in the biologics file).
- **My own classifications:**
  - "Intracellular-only" uses GO annotation, which is imperfect.
  - "Lung inflammation" in the autopsy text was keyword-based; I read the discordant cases in full.
  - The omitted-assay reconstruction gives their number and p-value positions, not their identities.
- **Enrichment tests** depend on the Olink-to-gene mapping (915 of 1,063 proteins map to expressed transcripts).
