# D7 — pre-registered failure modes

RLS short ID fpfj2b81. Task `task_c95a3b4fb7e14881853c61756d8086e3`.

Six modes. Each entry below is set out the same way:

- **If a solver falls in** — what they actually do and conclude
- **What we would claim** — the method failure, stated as what was not
  checked, measured or corrected for
- **Case for** — why it clears the FA bar
- **Case against** — why it might not

The FA bar: method-based, confirmable by a second annotator from the
transcript, and not defensible by a careful expert. Naming a mode is the
writer's call. Nothing here decides it.

All figures recomputed from the mounted room and asserted by
`scratch/analysis/verify_room.py` and `verify_golden.py`.

---

## 1. `threshold-intersection`

**If a solver falls in.** They take the HUVEC 6 h attributable set (1126
genes at `adj.P.Val < 0.05`, `|logFC| > 1`), apply the same two thresholds to
HGMEC, intersect, get 219, read 219 of 1126 as poor overlap, and conclude the
response does not reproduce across cell lines. Verdict comes out no-go.

**What we would claim.** They did not check whether the two lines are on the
same effect-size scale before applying the same threshold to both.

**Case for.**

- Median `|logFC|` over those same 1126 genes is 2.0140 in HUVEC and 0.7367
  in HGMEC, a factor of 2.7337. A cut at 1.0 sits near the centre of the
  HGMEC distribution, so it removes genes for being small rather than for
  disagreeing.
- The rule admits 11 genes with **opposite signs** in the two lines —
  RF00003 is +2.5564 in HUVEC and −2.7988 in HGMEC, both significant. A rule
  that counts those as reproducing is not measuring agreement, which is
  visible without any knowledge of effect-size scaling.
- Correcting it reverses the verdict: direction plus nominal significance
  gives 315 of 1126 and r 0.6216.
- Confirmable from a transcript — you can see whether the solver compared
  effect-size distributions before thresholding.

**Case against.** None I can see. Intersecting pre-thresholded sets is the
standard move, which is what makes it attractive, but the data to catch it is
in the same two columns the solver is already reading.

**Diagnostic for the transcripts.** A reported count of 215–245 alongside a
reproducibility-failure claim indicates the mirror rule. Measured mirror
values are 219, 239 and 241 across the three base filters, so that column is
nearly invariant to the base.

---

## 2. `both-windows-rejection`

**If a solver falls in.** They assess both timepoints, see low overlap at
each, and give one uniform conclusion covering both — either no-go overall,
or go without distinguishing the windows.

**What we would claim.** They did not check whether the two timepoints behave
differently once the effect-size correction is applied.

**Case for.**

- The statistics separate cleanly: r 0.6216 against 0.3032, sign agreement
  76.82% against 64.27%, signature 315 against 23.
- The absolute figures do look uniformly low before correction — Jaccard
  0.1571 and 0.0356 — so the error is a real attractor rather than
  carelessness.
- It changes the recommendation, which is the highest-consequence outcome
  available.

**Case against.** Partly protected by the prompt as currently worded. "the
response signature and timepoint we would carry forward" tells the solver a
timepoint carries, so a solver who rejects both is contradicting the brief
rather than falling into a basin. **Fix the prompt and this concern goes
away.**

---

## 3. `assay-as-analyte`

**If a solver falls in.** They report the serum layer as 1094 proteins with
178 significant, taking one row per assay.

**What we would claim.** They did not reconcile assay identifiers across
panels before counting.

**Case for.**

- 26 analytes appear on more than one panel; IL6 on four, SCF and FGF-21 on
  three. The reconciled figures are 1064 and 169.
- The panel column is right there in the file, and the suffixes (-INFI,
  -CVDII, -ONCII and so on) are visible in the assay names themselves.
- The annex states that assay identifiers are panel-specific and reported
  without reconciliation, so the room says the work is needed.
- Trivially confirmable: the number is either 1094 or 1064.

**Case against.** Low consequence. It changes a reported count, not the
recommendation. A solver could also argue the per-assay figure is what the
vendor delivered and therefore what to report — though the annex's wording
undercuts that.

---

## 4. `prognostic-as-pharmacodynamic`

**If a solver falls in.** They nominate soluble ST2 as a biomarker to carry
into the clinic, on its serum ranking.

**What we would claim.** They did not check whether the marker they nominated
responds to the intervention.

**Case for.**

- ST2 ranks second of 1094 at OR 3.0243 and is the pathway's own receptor, so
  it is strongly attractive.
- `IL1RL1` is not significant in any of the 24 contrasts, minimum
  `adj.P.Val` 0.9614, and is absent from the signature. The check is a
  one-line lookup in a file the solver has already opened.
- The consequence is concrete: a pharmacodynamic readout that cannot move
  would report target engagement where none is measurable.

**Case against.** A solver who nominates sST2 explicitly as a **patient-
selection** marker rather than a pharmacodynamic one has made no error. The
mode only holds where they offer it as a readout of drug effect, so the
transcript has to show which claim was made.

---

## 5. `magnitude-ranked-response`

**If a solver falls in.** They name SELE, VCAM1 and CXCL8 as the antibody's
main effects, or as evidence the antibody suppresses endothelial activation.

**What we would claim.** They ranked by effect size without applying the
significance filter.

**Case for.**

- Those three carry three of the ten largest fold changes, at −10.9852,
  −8.7623 and −8.4467, and they are the textbook endothelial activation
  readouts, so both the data and prior expectation point at them.
- None is attributable: `adj.P.Val` 0.4950, 0.4965 and 0.1772. ICAM1 at
  −5.9116 and 0.0101 is.
- Not defensible — the adjusted p value is in the adjacent column.

**Case against.** The brief flags it as weakly forced: nothing in the prompt
asks for the largest effects, so a solver may simply never go looking. It may
not appear at all.

---

## 6. AX-1177_rnaseq_contrasts sheet duplication

**If a solver falls in.** They call `pd.read_excel('AX-1177_rnaseq_contrasts.xlsx')` with
defaults, or concatenate both sheets, or filter on sheet name for timepoint,
and compute over a corrupted frame without noticing.

**What we would claim.** They did not check the shape of the file before
computing over it.

**What is actually there.** Two sheets named `6h` and `24h`, each holding the
same 24 contrasts with identical values. 22 are byte-identical and 2 differ
only in row order. The names are not a timepoint split; both timepoints sit
inside each sheet and are selected by the `Comparison` column. The `6h` sheet
is dimensioned to Excel's 1,048,576-row ceiling, holding 629,040 data rows
and 419,535 empty ones. The `24h` sheet holds 629,040 rows and no padding.

| Action | Result |
|---|---|
| `pd.read_excel` with defaults | reads sheet 0, returns 419,535 NaN rows alongside the data |
| concatenating both sheets | every contrast duplicated; any recomputed statistic is wrong |
| filtering on sheet name for timepoint | returns all 24 contrasts, both timepoints |

**Case for.** Unambiguous and not defensible — nobody reads 419,535 empty
rows as data. Checking rows per contrast equals 26,210 is a one-line
sanity check. Cheap to confirm from a transcript.

**Case against.** It is a data-handling failure rather than a preclinical-
reasoning one. If you want the FA to be about scientific method, this reads
as a pandas slip and is weaker material even though it is clean.

**Counterfactual.** Select on `Comparison`, verify 26,210 rows per contrast,
read the `24h` sheet.

---

## Considered and not pre-registered

| Candidate | Why not |
|---|---|
| **`unverified-attribution`** — not checking the ligand-independent antibody term | **Cut.** The check changes no number: dropping every gene significant in either standalone arm leaves 1114 of 1126 and moves the attenuation from 2.7337x to 2.7341x. The solver reaches the same answer whether or not they run it. Against that, the data is highly discoverable (16 of the 24 contrasts contain no IL-33), so skipping it is hard to defend — but a mode that cannot change an answer is weak FA material. Record the figures if a transcript shows the check was skipped; do not pre-register it. |
| **contrast-family choice** — using `Compound_47_IL33_vs_IL33_<line>` instead of the isotype-controlled family | Same verdict, and three features come out larger: attenuation 2.807× and 4.934×, r 0.6481 to 0.2321, sign 78.60% to 58.50%. A careful expert could defend either family, so it fails the defensibility bar. Belongs in the derivation notes. The 24 h set does inflate from 417 to 547, carrying a ligand-independent term, which is worth credit if a solver names it. |
| **Olink join rule** | Both exact matching and legacy-name reconciliation are defensible and the grader accepts either. The mode-shaped version is an **unstated** join — reconciling some aliases and not others — which is what the brief's own figure of 6 was: exact matching plus the `OPG` alias alone, a count no stated rule produces. Worth watching for; too narrow to pre-register. |
| **AX-1177_postmortem_lung `Tissue RNA`** | 22 of 78 blocks carry `Zr4940_<n>` identifiers, matching the paper's 9 + 9 + 4 lung RNA-seq cohort, pointing at data in no mmc file. But AX-1177_serum_proteomics holds assay-level summary statistics with no patient identifiers, so a serum-to-tissue join is **impossible**, not merely unwise. A solver can err in prose but cannot produce a wrong number. Kept as foreclosure so the absence anchor has something to foreclose. |
| **shortlist precision** | Three of the thirteen shortlist analytes have upper 95% bounds above 20 — CSF-1 at 1932.572, CTSS at 200.019, BIRC2 at 64.215. Nominating them on point estimates is a real error, but it was not predicted before the odds ratios were read, so it is an observation to check the transcripts for rather than a pre-registration. |
