# Phase 1 — what the runs did

Deliverables rebuilt from transcript file operations (no `outputs/` in the
export) and validated against the range-reads each run made of its own file.
Rebuilds are approximate where late patch edits did not match: run
85c06969 had 12 unmatched edits, 5ee4d9d8 and 3fa01b44 one each, c3051d03 two.
Every count below was confirmed by reading the matched text, not from a
pattern hit.

Thinking blocks in all 8 transcripts carry `thinking_summary: {status: ok}`,
so they are summaries. No claim about what a run weighed internally is
supportable.

## Verdicts: all 8 recommend against advancing

| Run | Recommendation line, opening |
|---|---|
| c3051d03 | "do not move AX-1177 into IND-enabling studies or the clinic on this package" |
| 5ee4d9d8 | "NOT YET. Do not start IND-enabling work or clinical dosing" |
| d96741c2 | "CONDITIONAL GO, limited to a gated, time-boxed (~12-month) de-risking phase" |
| 026318d8 | "NOT YET. Do not move AX-1177 into IND-enabling or clinical work" |
| 3fa01b44 | "NOT YET. Do not start clinical development" |
| 85c06969 | "CONDITIONAL GO. Move AX-1177 into a gated de-risking phase... do not fund a clinical efficacy study" |
| 356f2f79 | "Do not take AX-1177 into IND-enabling or clinical work on this package" |
| d684fc0a | "No. This package does not support carrying AX-1177 into IND-enabling or clinical development" |

**No recommendation line in any run names a timepoint.** A1 fails uniformly,
confirmed from the rebuilt deliverables rather than from the grader.

**The stated reason is package scope, not reproducibility.** Every run cites
the absence of in vivo, infection-model, potency or safety data. None rejects
on cross-line reproducibility grounds.

## The pre-registered modes, against the transcripts

| Mode | Appears? | Evidence |
|---|---|---|
| `threshold-intersection` | **no** | every run used rank correlation, slope or sign agreement rather than set intersection. c3051d03: "Spearman is 0.56 and 0.25, and 83% / 68% move in the same direction". 356f2f79: "97.3% move in the same direction". d684fc0a: "r = −0.79, slope −0.58, 94% opposite sign" at 6 h |
| `both-windows-rejection` | **no — inverted** | runs reached the timepoint split correctly. d684fc0a: "mirrors the HUVEC programme at 6 h (r = −0.79 ...) but only weakly at 24 h (r = −0.30, slope −0.07)". 026318d8: "Neutralisation is weaker at 24 h". 356f2f79: "At 24 h the effect is weaker (269 genes)". d96741c2: "24 h: weaker, −0.31" |
| `assay-as-analyte` | **no** | 7 of 8 reconciled explicitly. c3051d03: "27 proteins are measured on more than one panel (58 assays). The 178 FDR-significant assays correspond to 169 unique proteins." d96741c2: "1,094 assays, or 1,063 unique proteins once the 27 proteins measured on 2–4 panels are collapsed". 3fa01b44 and 356f2f79 also give 1,063. d684fc0a's uses of 1,094 and 178 are correctly labelled as assay counts |
| `prognostic-as-pharmacodynamic` | **marginal** | 85c06969 writes "sST2 (used for stratification)" and 356f2f79 "a plausible enrichment and patient-selection biomarker" — both correct handling. d96741c2 places sST2 in a target-engagement panel. d684fc0a lists sST2 among proteins "induced by IL-33 and reversed by Compound_47 in HUVEC (both >2-fold)", which the contrasts do not support. At most 1–2 runs, against a floor of 2 |
| `magnitude-ranked-response` | **not assessable as a mode** | the delivered q-values for SELE and VCAM1 rest on implied SEs of 8.779 and 7.019 against a signature ceiling of 1.7439. A run relying on fold change after showing this has not erred |
| mmc5 sheet duplication | **mostly found** | 5ee4d9d8 states it exactly: "sheets '6h' and '24h' hold the *same* 24 contrasts (both timepoints), with identical values. Sheet '6h' is padded with 419,535 blank rows up to Excel's 1,048,576-row limit." Also flagged by 026318d8, 3fa01b44, 356f2f79, d684fc0a. Not mentioned by c3051d03, d96741c2, 85c06969 — non-mention is not yet confirmed as non-handling |

## Things the runs found that the golden did not

Recorded because they bear on whether the room holds material the design did
not anticipate.

- **The BH denominator implies ~100 withheld assays.** Six runs independently
  reverse-engineered it. c3051d03: "the delivered multiple-testing adjustment
  (Benjamini–Hochberg, BH) only reproduces if **1,194 tests** were run. Only
  1,094 are delivered, and ≥4 of the 100 missing tests were FDR-significant."
  d684fc0a derives the same 1,194 from integer implied counts rising
  monotonically 0→99. Also in 5ee4d9d8, d96741c2, 026318d8, 3fa01b44.
- **The two inhibition contrast families share an arm.** 5ee4d9d8: "Using the
  IL-33-alone arm as reference gives 82% reversal of IL-33-repressed genes;
  the isotype comparator gives 41%. The gap comes from noise in the shared
  IL-33-alone libraries." This identifies the mechanism, which the derivation
  notes did not.
- **The isotype is not inert at 24 h.** d96741c2: "NIP228 attenuated the IL-33
  response by 13.6% (95% CI 9.2–17.7%) in expressed genes at 24 h, but not at
  6 h (−3.0%, CI −8.5 to 2.1)."
- **The SE pathology.** d96741c2 lists "resolve the SE inflation" as a
  workstream.
- 3fa01b44 re-applied BH across the 1,063 unique proteins and reports a
  different significant count as a result.

## Reading coverage

All 8 deliverables rebuilt and searched. None read end to end as prose; the
verdict lines, the timepoint and cross-line passages, the serum-count
passages and the sST2 passages were read in full. Transcripts were parsed for
tool calls and thinking blocks but not read end to end.
