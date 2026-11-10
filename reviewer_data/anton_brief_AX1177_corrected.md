# Anton Task Brief — AX-1177 anti-IL-33 mechanistic package

RLS short ID: fpfj2b81
RLS URL ID: task_c95a3b4fb7e14881853c61756d8086e3
Campaign: camp_0589d1e96758477586df0e43dd8eeec1
URL: https://studio.mercor.com/annotator/tasks/task_c95a3b4fb7e14881853c61756d8086e3/?campaignId=camp_0589d1e96758477586df0e43dd8eeec1

> Create the task in RLS **first** and record both IDs here. They are needed in
> different places and hunting for them later is a recurring tax.

---

## 1. THE PROMPT

### Scene

A preclinical anti-IL-33 antibody programme in viral lower respiratory tract
disease. The solver is asked for a committee recommendation on whether the
mechanistic package supports carrying the asset forward.

### Deliverables + output paths

| Deliverable | Path |
|---|---|
| proposal, opening with a one-line recommendation | `/tmp/outputs/answer.md` |
| any supporting analysis, including the full signature membership table | `/tmp/outputs/` |

### As-of date

November 2026.

### Out-of-scope constraint

Interpretation of the data package only. No bench procedure, no synthesis, no
wet-lab protocol. The existing constraint line ("Keep this at the level of
interpretation of the data package") already covers this and does not forbid
any step the prompt requires.

### Prompt draft

> We have an anti-IL-33 antibody, AX-1177, in preclinical development for viral
> lower respiratory tract disease.
>
> The in vitro package and the supporting clinical datasets are mounted in
> /tmp/world/filesystem. Treat the mounted package as the complete and
> authoritative record for this programme. Domain knowledge is welcome in
> interpretation; figures, findings and conclusions must come from the mounted
> files.
>
> I need to take a recommendation to the programme committee on whether the
> mechanistic package supports carrying this forward. Build me the proposal,
> opening with your recommendation in one line at the top
> (/tmp/outputs/answer.md).
>
> It has to be highly defensible. Claims and recommendations need explicit
> reasoning, cited numbers and values, and sound methodology. Save any analysis
> you run under /tmp/outputs.
>
> Keep this at the level of interpretation of the data package. I need the
> response signature and timepoint we would carry forward, what the model data
> supports, and which circulating markers are worth taking into the clinic.

**Edits applied vs the version discussed:** "the measurement window it holds
over" replaced with "and timepoint", removing a presupposition that partially
foreclosed the `both-windows-rejection` mode.

**Writer to hand-edit.** Flagged as reading slightly over-instructive.

---

## 2. THE DATA ROOM

### Manifest

| File | Contents | States the world how |
|---|---|---|
| `AX-1177_serum_proteomics.xlsx` | Olink serum associations: 1094 assays × OR, 95% CI, p, adj.p vs composite endpoint; 13 panels | the clinical prognostic layer |
| `AX-1177_postmortem_lung.xlsx` | 78 histology blocks from 31 donors: demographics, pathology text, SARS-CoV-2 status, IHC scores | tissue context; unrelated cohort |
| `AX-1177_rnaseq_huvec_il33.xlsx` | HUVEC IL-33red vs vehicle, 6 h and 24 h, 26,210 genes | the stimulation reference |
| `AX-1177_rnaseq_contrasts.xlsx` | 24 contrasts across HUVEC, HGMEC, A549, MCF7 × control arm × timepoint, 26,210 genes each (26,113 distinct symbols) | **the decisive file** |
| `AX-1177_methods_annex.md` | authored methods and annotation; no results, no interpretation | the editable layer |

`mmc6` (ISARIC investigator list) is **dropped**: real names, institutional
emails and ORCIDs, no analytical value.

### Build steps, mandatory

1. **Strip workbook metadata.** All four carry `dc:creator` of `Scott, Ian
   Christopher` or `Van Zuydam, Natalie` and `cp:lastModifiedBy` of
   `Oxford PharmaGenesis`. Two source-paper authors and AstraZeneca's medical
   writing agency. Rewrite `docProps/core.xml` and `docProps/app.xml` inside the
   zip, copy every other part byte-for-byte. Verified lossless: all non-docProps
   parts hash-identical, row contents equal.
2. Ship the four workbooks under the names above, unedited beyond step 1.
3. Place the annex alongside them.
4. Do **not** convert to CSV. `pd.read_excel` on the largest sheet is 40 s and
   838 MB peak, which is unremarkable. Conversion buys nothing and costs
   verification.
5. Leave the `Vehicle` / `Nontreated` inconsistency in `AX-1177_rnaseq_huvec_il33` in place. It is a
   real artifact and the two arms are the same thing.

### Anchor table

| Value | File | Legible? | Steps from a cell |
|---|---|---|---|
| SELE adj.P 0.495; VCAM1 0.497; CXCL8 0.177 | AX-1177_rnaseq_contrasts | yes | 0, direct read |
| ST2 rank 2, OR 3.02 | AX-1177_serum_proteomics | yes | 0 |
| standalone arms 31 / 36 (HUVEC), 62 / 67 (HGMEC) | AX-1177_rnaseq_contrasts | yes | 1 |
| receptor-null floor 27 / 17 (A549), 20 / 26 (MCF7) | AX-1177_rnaseq_contrasts | yes | 1 |
| HUVEC 6 h / 24 h inhibition 1126 / 417 | AX-1177_rnaseq_contrasts | yes | 1 |
| HGMEC 6 h / 24 h inhibition 487 / 135 | AX-1177_rnaseq_contrasts | yes | 1 |
| HUVEC stimulation 1068 / 512 | AX-1177_rnaseq_huvec_il33 | yes | 1 |
| *IL1RL1* significant in 0 of 24 contrasts | AX-1177_rnaseq_contrasts | yes | 1, scan |
| **median \|logFC\| 2.0140 vs 0.7367 (6 h), 2.2349 vs 0.5136 (24 h)** | AX-1177_rnaseq_contrasts | yes | 2 |
| r 0.6216 (6 h) / 0.3032 (24 h) | AX-1177_rnaseq_contrasts | yes | 2 |
| sign agreement 76.82% / 64.27% | AX-1177_rnaseq_contrasts | yes | 2 |
| direction+nominal replication 28.0% / 5.5%; mirror replication 19.45% / 4.56%; Jaccard 0.1571 / 0.0356 | AX-1177_rnaseq_contrasts | yes | 2 |
| attribution overlap 6 / 1126 | AX-1177_rnaseq_contrasts | yes | 2 |
| 1094 assays → 1064 analytes; 178 hits → 169 | AX-1177_serum_proteomics | yes | 2 |
| df.total 85.128 uniform across all 24 contrasts | AX-1177_rnaseq_contrasts | yes | 2, invert t against P |

Every anchor is a computation over mounted numeric cells. No handbook values, no
transformed or synthetic quantities, nothing resting on literature. No thin
anchors identified.

### Absence anchors — the annex must not say

- that effect magnitudes differ between cell lines, or that any line is attenuated
- that the 24 h result does or does not reproduce
- that AveExpr is unsuitable for cross-line comparison (it states only how it was computed)
- that sST2 does or does not respond to the test article
- any distinction between assay count and analyte count
- which model or timepoint is preferred
- any consequence of the replicate numbers for statistical power
- any relationship, in either direction, between the serum cohort and the tissue donors

Assert these mechanically against the shipped annex, not by eye.

### Required tooling

| Tool | Confirmed |
|---|---|
| pandas + openpyxl | yes, 40 s / 838 MB on the largest sheet |
| scipy (correlation, distributions) | yes |
| no network access needed | — |

---

## 3. THE GOLDEN RESPONSE

### Spec

Six parts, mirroring the prompt, nothing more:

1. **Recommendation** — one line, carrying the timepoint distinction
2. **Response signature** — criterion stated as a predicate, resulting count,
   module composition, the ~15 genes carrying the clinical argument
3. **Timepoint** — both compared, both statistics, the conclusion
4. **What the model data supports** — attribution, cross-model behaviour, what
   the second line does and does not establish
5. **Circulating markers** — shortlist as distinct analytes, with exclusions
6. **Considered and not carried** — minimum three entries, each tracing to a value

Full membership table to `/tmp/outputs/`, not the body.

### Forcing chain

| Leg | Claim established | Mounted evidence | Route-necessary |
|---|---|---|---|
| 1 | the antibody effect is ligand-dependent, not artifact | the standalone sets are disjoint from the attributable set: overlap 6/1126 (HUVEC 6 h) and 1/487 (HGMEC 6 h), and removing every standalone-significant gene leaves the HGMEC median at 0.7367 unchanged | yes |
| 2 | the HUVEC 6 h attributable set is 1126 under the package criterion | AX-1177_rnaseq_contrasts, HUVEC 6 h isotype-controlled, adj.P<0.05 and \|logFC\|>1 | yes |
| 3 | **HGMEC effects are systematically attenuated** | median \|logFC\| 2.0140 vs 0.7367 (2.734×); 2.2349 vs 0.5136 (4.351×) | **yes — everything turns on it** |
| 4 | the lines agree at 6 h and not at 24 h | r 0.6216 vs 0.3032; sign 76.82% vs 64.27%; direction+nominal replication 28.0% vs 5.5% | yes |
| 5 | a fixed fold-change cut understates agreement given leg 3 | 219 vs 315 off the same base; the 107 recovered genes begin at magnitude rank 79 (ACKR3, \|logFC\| 3.710) | yes |
| 6 | the reproducible core is coherent suppressed inflammatory biology | interferon, NF-κB (incl. NFKB2 −2.86, RELB −3.27), CSF and cytokine, and chemokine modules all present; F3 −5.47, C3 −4.62; every member of the named modules is negative | yes, for the justification |
| 7 | sST2 has no pharmacodynamic response | *IL1RL1* in 0 of 24 contrasts, absent from the core | serum product only |
| 8 | the Olink delivery is 1094 assays over 1064 analytes | 26 analytes on more than one panel, IL6 on four | serum product only |

### Derivation notes

**The signature count is base-filter dependent and must not be stated as *the*
answer.** Criterion grid, HUVEC 6 h:

| base filter | mirror | sign+adjP<.05 | sign+adjP<.10 | sign+rawP<.05 | sign+\|lFC\|>0.5 | sign only |
|---|---|---|---|---|---|---|
| adj.P<.05 only (4239) | 241 | 951 | 1147 | 1720 | 776 | 3525 |
| adj.P<.05, \|lFC\|>0.585 (1825) | 239 | 556 | 623 | 846 | 732 | 1496 |
| adj.P<.05, \|lFC\|>1 (1126) | 219 | 315 | 348 | 458 | 579 | 865 |

Defensible corrected answers span 315 to 1720. **The mirror column is nearly
invariant at 241 / 239 / 219** because the second line's fold-change cut is the
binding constraint regardless of base. A reported count of 215–245 alongside a
reproducibility-failure claim is therefore diagnostic of the mirror rule.

Fisher and Stouffer both return 865, identical to sign-only, because the HUVEC
p-value dominates the combination.

**Translational shortlist: the join rule must be stated, and the golden
reconciles.** Olink reports protein assay names, not gene symbols. Off the
219-gene mirror core:

| Join rule | n | Members |
|---|---|---|
| exact symbol string | 5 | B4GALT1, CCL20, CTSS, IL1B, IL6 |
| **legacy names reconciled** | **9** | adds CSF-1 → CSF1, IL-18R1 → IL18R1, MCP-3 → CCL7, OPG → TNFRSF11B |

Off the 315-gene direction-plus-nominal core: 9 exact, **13** reconciled
(B4GALT1, BIRC2, CCL20, CSF-1, CTSS, FSTL3, IL-18R1, IL1B, IL6, MCP-3, OPG,
TANK, TRIM21).

**The golden reconciles: 9 and 13.** The four aliases are standard protein-to-
gene mappings with one correct answer each, and the prompt welcomes domain
knowledge in interpretation. The alias set is closed: of the 169 significant
analytes, every name maps to a symbol, so the reconciliation is determinate
rather than open-ended.

Note that an exact-string join gives 5, not 6. The figure of 6 is exact
matching plus the OPG alias alone, which no stated rule produces.

**Both joins are acceptable** where the rule is stated. A solver who reports 5
or 6 under a declared exact-matching rule has been internally consistent; the
error to penalise is an unstated rule or a count that does not follow from it.

**The module predicate must be stated, not the counts.** Interferon and
chemokine membership reproduces exactly at 14 and 9, but NF-κB is 9 or 10
depending on whether BIRC3 counts, and CSF and cytokine is 7 under a narrow
reading (CSF1-3, IL1A, IL1B, IL6, TNF) or 15 under a broad one that admits
IL15RA, IL18R1, IL32, IL4I1, IL9RP3 and TNFSF15. The golden states the
predicate it used and does not quote a bare module count.

**The core is not uniformly negative.** 184 of 219 genes are negative and 35
positive. No positive belongs to any named module: they are SLC14A1, FSTL4,
NDP, GAP43, CNFN, ABCC11, GATM, MLXIPL, ZNF177, SYTL1, C2orf72, a set of
antisense and lincRNA transcripts, two pseudogenes and RF00003. The claim is
therefore about the named modules, not the core, and the golden says so. The
positives are not characterised; they sit near the magnitude threshold and
look like transcriptional noise, but that has not been tested.

**Leg 1 does not rest on the null-floor comparison.** HUVEC standalone counts
of 31 and 36 sit inside the receptor-null range of 13–40, but HGMEC's 62 and
67 sit roughly double it, so the floor comparison does not carry
ligand-dependence for that line. What carries it is disjointness: the
standalone sets barely intersect the attributable sets (6 of 1126 in HUVEC
6 h, 1 of 487 in HGMEC 6 h) and removing every standalone-significant gene
leaves the HGMEC median over the HUVEC core at 0.7367, unchanged to four
decimals. The golden rests the claim there.

**Provenance form**, to be used for every number:

> Median |logFC| across the 1126 HUVEC-significant genes is 2.0140 in HUVEC and
> 0.7367 for the same genes in HGMEC (`AX-1177_rnaseq_contrasts.xlsx`,
> `Compound_47_IL33_vs_IL33_NIP228_HUVEC_6hrs` and `..._HGMEC_6hrs`, median of
> absolute `logFC` over the HUVEC-significant subset).

**The golden must not:** state a signature count as the answer; cite affinity,
potency or exposure figures for AX-1177, which are not in the room; draw on the
tissue dataset for the in vitro conclusion, since the cohorts are unrelated;
include pathway commentary bearing on nothing asked.

---

## 4. PRE-REGISTERED FAILURE MODES

Carry this table into the FA session. Checking predicted modes against
transcripts is the fastest route to the required one to five.

### False-optimum map

| Short name | Fails to check / measure / correct for | Why it attracts | Refuting fact | Counterfactual |
|---|---|---|---|---|
| `threshold-intersection` | whether between-line effect-size difference invalidates a fixed fold-change cut as a reproducibility test | intersecting significant sets is the standard move, and both arrive pre-thresholded by the package's own criterion | median \|logFC\| 2.0140 vs 0.7367 over the same genes | direction plus nominal significance gives 315 and r 0.6216; the intersection gives 219 and reads as failure |
| `both-windows-rejection` | that the correction separates the two timepoints | Jaccard 0.1571 and 0.0356 both read as low; one uniform conclusion is tidier | r 0.6216 vs 0.3032; direction+nominal replication 28.0% vs 5.5% | 6 h carries, 24 h does not |
| `assay-as-analyte` | reconciliation of assay identifiers across panels | one row per assay, 1094 rows, the obvious count | 26 analytes appear on more than one panel | 1064 analytes, 169 significant |
| `prognostic-as-pharmacodynamic` | whether the top-ranked marker responds to the intervention | sST2 ranks second of 1094 at OR 3.02 and is the pathway's own receptor | *IL1RL1* not significant in any of 24 contrasts | shortlist of 5-9 (219 core) or 9-13 (315 core) by declared criterion, sST2 excluded |
| `unverified-attribution` | the ligand-independent antibody term | the isotype appears in the contrast name, which looks like it handles it | the contrast is (Ab+IL-33) vs (isotype+IL-33); the antibody-alone term sits in the numerator only. 16 of the 24 contrasts contain no IL-33, so the data for the check is two thirds of the file | the standalone sets are disjoint from the attributable set, overlap 6/1126 and 1/487; attribution holds. **Low consequence** — removing every standalone-significant gene leaves the 6 h ratio at 2.734× |
| `magnitude-ranked-response` | the significance filter when naming the strongest effects | SELE, VCAM1 and CXCL8 are the textbook endothelial readouts and carry three of the ten largest fold changes | adj.P 0.495, 0.497, 0.177 | none is attributable; ICAM1 at adj.P 0.0101 is |

Six predicted so that one to five survive contact. The first two carry the
verdict; the rest fail independently of it.

**The last two are weakly forced by the prompt** and may simply not appear.

### Escape / foreclosure

| Escape | Local appeal | Foreclosing fact | Where mounted |
|---|---|---|---|
| "different tissues, so divergence is expected and HUVEC is the relevant line" | cell-type differences are real | the same two lines agree at 6 h, r 0.6216 and 76.82%; tissue identity would apply at both timepoints | both timepoints, AX-1177_rnaseq_contrasts |
| "HGMEC simply isn't IL-33 responsive" | no HGMEC vehicle arm exists | 487 genes are antibody-reversed in HGMEC at 6 h; you cannot reverse what was not driven | AX-1177_rnaseq_contrasts, HGMEC 6 h |
| "check receptor expression per line via AveExpr" | the column is right there | one fit across 114 libraries; AveExpr is per-gene identical at full precision across all 24 contrasts, for all 26,210 genes | annex §5, and AX-1177_rnaseq_contrasts |
| "report the top hits, they are the biology" | top hits are the mechanism | top 50 by magnitude is identical under both criteria | criterion grid |
| "sST2 ranks second, nominate it" | it is the pathway's own receptor | *IL1RL1* in 0 of 24 contrasts | AX-1177_rnaseq_contrasts |
| "pool the timepoints for power" | more samples | the question asks which timepoint carries; pooling cannot answer it | contract |

---

## 5. SUPPORTING

### Hidden basin

The second endothelial line's effects are systematically 2.734-fold smaller, so a
fixed fold-change threshold rejects reproducibility by construction at the
timepoint where the response is in fact reproducible.

### Answer contract

**One mandated structural element:** the recommendation, one line, at the top of
`answer.md`. Everything else is elicited by the prompt's component sentence.

| Graded | How |
|---|---|
| the criterion | stated as a predicate; does it account for between-line effect size |
| internal consistency | does the reported count follow from the solver's own declared base filter and rule |
| the diagnostic | a count of 215–245 alongside a reproducibility-failure claim indicates the mirror rule (measured mirror values are 219, 239, 241) |
| the conclusion | 6 h carries, 24 h does not |
| analyte handling | 1064 and 169, not 1094 and 178 |
| sST2 | excluded with a stated reason |

No absolute count band. The count is a legitimate degree of freedom; the
predicate and the conclusion are not.

**Near-miss forms of the verdict:**

| Form | Call |
|---|---|
| go, 6 h signature only, 24 h excluded | pass |
| go, with the 24 h arm to be repeated in a second model | pass |
| conditional go pending further models | pass if the timepoint distinction is made |
| bare go, no timepoint qualification | fail |
| no-go on reproducibility grounds | fail — this is the false optimum |
| go at both timepoints | fail |

Acceptable and not penalized: noting that HGMEC's IL-33 responsiveness is never
directly measured, since no vehicle arm exists for that line. That is a true
observation about the package.

### Grader guidelines

```
You are grading a preclinical committee proposal on whether an in vitro
mechanistic package supports advancing an anti-IL-33 antibody. The solver has
transcriptomic contrasts across four cell lines and two timepoints, plus a serum
proteomic association dataset. The answer turns on which part of the response
reproduces across cell lines and at which timepoint.

A) MUST BE PRESENT AND CORRECT
The following are the key requirements of a correct answer. Use your judgment
to identify any additional required content not listed here.
- A one-line recommendation at the top that distinguishes the 6 h result from
  the 24 h result.
- An explicitly stated criterion for which genes constitute the reproducible
  signature, with a count that follows from that criterion.
- Evidence that between-line effect size was considered when assessing
  reproducibility.
- Quantitative results cited with the file and contrast they came from.

B) PENALIZE FOR
The following are common errors observed on this task. This list is not
exhaustive — apply your judgment to any other issues you identify.
- Concluding that the response does not reproduce across cell lines, on the
  basis of intersecting threshold-filtered gene sets.
- Reporting 1094 proteins, or 178 significant proteins, where those figures
  count assays rather than analytes. The reconciled figures are 1064 and 169.
- Nominating soluble ST2 as a pharmacodynamic readout.
- Reporting adhesion molecules, in particular SELE or VCAM1, as part of the
  antibody-attributable response.
- Stating affinity, potency or exposure values for AX-1177, which are not in the
  delivered package.

C) NEUTRAL
The following are examples of acceptable variations that should not affect the
score. Other variations may also be neutral — use your judgment.
- The particular reproducibility criterion chosen, and the resulting gene count,
  provided the criterion is stated and the count follows from it.
- How Olink assay identifiers are matched to genes for the circulating-marker
  shortlist. Exact symbol matching and reconciliation of legacy assay names
  (OPG, CSF-1, IL-18R1, MCP-3) are both defensible and give different
  shortlists. Either is acceptable where the rule is stated and the members
  follow from it.
- Whether supporting analysis is presented as tables, prose or figures.
- Length, section ordering and file layout beyond the one-line recommendation.
- Noting that one cell line has no unstimulated baseline arm.
```

### Panel geometry

16 independent samples. Not subagent fanout: fanout arms share latent parent
context and give sixteen versions of one trajectory, which thins FA coverage.

### Known risks / open questions

| Risk | Severity | Status |
|---|---|---|
| workbook metadata names source-paper authors and AZ's writing agency | **high** | mandatory build step, method proven lossless |
| `mmc` filenames are an Elsevier supplementary fingerprint | medium | **fixed after v3**: 8 of 8 v3 runs pattern-matched the room, four naming the convention; files renamed |
| `Compound_47` and `NIP228` are inside the data and cannot be renamed without editing files; NIP228 is a documented AZ control reagent | medium | accepted, unfixable |
| a methods annex listing `mmc2.xlsx` reads as repurposed | low | **fixed**: mounted files renamed off the `mmc*` convention |
| `unverified-attribution` and `magnitude-ranked-response` weakly forced by the prompt | low | may not appear; FA needs only one to five of six |
| prompt reads over-instructive | low | writer hand-editing |

**Validate before submitting.** Two things worth proving: the **ceiling**, that a
strong attempt working only from the data room reaches the 6 h conclusion; and
the **floor**, that the obvious first pass intersects thresholded sets and
rejects both timepoints. The floor is what generates FA material.

### Next steps

Data room is built locally. Task runs on Taiga via RLS. QA runs after every run
finishes. After reviewer approval the **failure analysis is the main
deliverable** — the runs exist to produce transcripts.

Carry section 4's table into the FA session. Naming a mode is the writer's call,
not Claude's; Claude may compare, cluster, locate and count only.
