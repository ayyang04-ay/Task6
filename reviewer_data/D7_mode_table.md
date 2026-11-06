# D7 — pre-registered failure modes, for the FA session

RLS short ID fpfj2b81. Task `task_c95a3b4fb7e14881853c61756d8086e3`.

Carry this table into the FA session. Checking predicted modes against
transcripts is the fastest route to the one-to-five that are required.
Naming a mode is the writer's call; nothing here decides it.

All figures recomputed from the mounted room and asserted by
`scratch/analysis/verify_room.py` and `verify_golden.py`.

## The six, ranked by consequence

### 1. `threshold-intersection` — carries the verdict

**Fails to check:** whether a between-line effect-size difference invalidates
a fixed fold-change cut as a reproducibility test.

**Why it attracts:** intersecting significant sets is the standard move, and
both sets arrive pre-thresholded by the package's own criterion.

**Refuting facts:** median `|logFC|` over the 1126 HUVEC-significant genes is
2.0140 in HUVEC and 0.7367 in HGMEC, a factor of 2.7337. The cut at 1.0
therefore sits near the centre of the HGMEC distribution. Separately, the
intersection admits 11 sign-discordant genes — ABCC11, AC007336.3,
AC091133.2, AL353807.3, ATP2B1-AS1, CALR4P, CNFN, DNAH17-AS1, GATM, MLXIPL,
RF00003 — of which RF00003 is +2.5564 in HUVEC and −2.7988 in HGMEC.

**Counterfactual:** direction plus nominal significance gives 315 of 1126 and
r 0.6216. The intersection gives 219 and reads as failure.

**Diagnostic:** a reported count of 215–245 alongside a reproducibility-failure
claim indicates the mirror rule. Measured mirror values are 219, 239 and 241
across the three base filters, so the column is nearly invariant.

### 2. `both-windows-rejection` — carries the verdict

**Fails to check:** that the correction separates the two timepoints.

**Why it attracts:** Jaccard 0.1571 and 0.0356 both read as low, and one
uniform conclusion is tidier than a split one.

**Refuting facts:** r 0.6216 against 0.3032; sign agreement 76.82% against
64.27%; signature 315 against 23.

**Counterfactual:** 6 h carries, 24 h does not.

### 3. `assay-as-analyte`

**Fails to check:** reconciliation of assay identifiers across panels.

**Why it attracts:** one row per assay, 1094 rows, the obvious count.

**Refuting fact:** 26 analytes appear on more than one panel; IL6 on four,
SCF and FGF-21 on three.

**Counterfactual:** 1064 analytes and 169 significant, not 1094 and 178.

### 4. `prognostic-as-pharmacodynamic`

**Fails to check:** whether the top-ranked marker responds to the
intervention.

**Why it attracts:** ST2 ranks second of 1094 at OR 3.0243 and is the
pathway's own receptor.

**Refuting fact:** `IL1RL1` is not significant in any of the 24 contrasts,
minimum `adj.P.Val` 0.9614, and is absent from the signature.

**Counterfactual:** shortlist by declared criterion with sST2 excluded.

### 5. `magnitude-ranked-response`

**Fails to check:** the significance filter when naming the strongest
effects.

**Why it attracts:** SELE, VCAM1 and CXCL8 are the textbook endothelial
readouts and carry three of the ten largest fold changes, at −10.9852,
−8.7623 and −8.4467.

**Refuting fact:** `adj.P.Val` 0.4950, 0.4965 and 0.1772. None is
attributable. ICAM1 at −5.9116 and 0.0101 is.

### 6. `unverified-attribution` — low consequence

**Fails to check:** the ligand-independent antibody term.

**Why it attracts:** the isotype appears in the contrast name, which looks
like it handles it. The contrast is (Ab + IL-33) vs (isotype + IL-33), so the
antibody-alone term sits in the numerator only.

**Discoverability:** **16 of the 24 contrasts in mmc5 contain no IL-33.** The
antibody-alone data is two thirds of the file and sits in the same
`Comparison` column as the inhibition contrasts. The check is one filter
away, not buried. This is what makes skipping it hard to defend.

**Refuting facts:** the standalone sets are disjoint from the attributable
sets, overlap 6 of 1126 in HUVEC 6 h and 1 of 487 in HGMEC 6 h. Dropping
every gene significant in either standalone arm leaves 1114 of 1126 and
moves the attenuation from 2.7337x to 2.7341x.

**Counterfactual:** attribution holds. **Changes no number**, which is why
this ranks last. It is a method failure that costs nothing numerically.

**The case for cutting it:** if trusting a contrast name that says `NIP228`
is what a careful expert does, the mode fails the defensibility bar. The
counter is the discoverability figure above.

### 7. mmc5 sheet duplication — approved for addition

**Fails to check:** the shape of the file before computing over it.

**What is there:** two sheets named `6h` and `24h`, each holding the same 24
contrasts with identical values. 22 are byte-identical and 2 differ only in
row order. The names are not a timepoint split; both timepoints sit inside
each sheet, selected by the `Comparison` column. The `6h` sheet is
dimensioned to Excel's 1,048,576-row ceiling: 629,040 data rows and 419,535
empty ones. The `24h` sheet holds 629,040 rows and no padding.

**Three ways it bites:**

| Action | Result |
|---|---|
| `pd.read_excel('mmc5.xlsx')` with defaults | reads sheet 0 and returns 419,535 NaN rows alongside the data |
| concatenating both sheets | every contrast duplicated; any recomputed statistic is wrong |
| filtering on the sheet name for timepoint | returns all 24 contrasts, both timepoints |

**Counterfactual:** select on `Comparison`, check rows per contrast equals
26,210, and read the `24h` sheet.

**The case against pre-registering it:** this is a data-handling failure
rather than a preclinical-reasoning one, which is weaker FA material even
though it is unambiguous and non-defensible.

## Not modes

| Candidate | Why not |
|---|---|
| contrast-family choice | `Compound_47_IL33_vs_IL33_<line>` instead of the isotype-controlled family gives attenuation 2.807x and 4.934x, r 0.6481 to 0.2321, sign 78.60% to 58.50%. Same verdict, three features larger. A careful expert could defend either, so it fails the bar. Belongs in the derivation notes. The 24 h set does inflate from 417 to 547. |
| Olink join rule | both exact matching and legacy-name reconciliation are defensible and the grader accepts either. The mode-shaped version is an **unstated** join: reconciling some aliases and not others, as the brief's own figure of 6 did (exact matching plus the OPG alias alone, which no rule produces). |
| mmc3 `Tissue RNA` | 22 of 78 blocks carry `Zr4940_<n>` identifiers, matching the paper's 9 + 9 + 4 lung RNA-seq cohort, pointing at data in no mmc file. But mmc2 holds assay-level summary statistics with no patient identifiers, so a serum-to-tissue join is impossible rather than merely unwise. A solver can err in prose but cannot produce a wrong number. Kept as foreclosure, not pre-registered. |
| shortlist precision | three of the thirteen analytes have upper 95% bounds above 20 — CSF-1 at 1932.572, CTSS at 200.019, BIRC2 at 64.215. Nominating them on point estimates is a real error but it was not predicted before the data was read, so it is an observation to check for rather than a pre-registration. |
