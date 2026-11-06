# Grader notes

Not part of the grading document. Reference for the writer and reviewer.

## Why the document is short

Leadership has said a sentence or two is acceptable and the 55% gate is gone,
so the grading document is not where effort belongs. The ABC template is kept
because it is still one of the task's parts. The value lands in the failure
analysis.

## Reference figures, for checking a solver's internal consistency

All recomputed from the shipped room by `scratch/analysis/verify_room.py` and
`verify_golden.py`.

| Quantity | Value |
|---|---|
| HUVEC 6 h attributable set, adj.P<.05 and \|logFC\|>1 | 1126 |
| same, 24 h | 417 |
| HGMEC 6 h / 24 h | 487 / 135 |
| signature, direction + nominal significance | 315 (6 h), 23 (24 h) |
| signature, two-sided threshold (mirror rule) | 219 (6 h), 19 (24 h) |
| median \|logFC\| HUVEC vs HGMEC, 6 h | 2.0140 / 0.7367, ratio 2.7337 |
| same, 24 h | 2.2349 / 0.5136, ratio 4.3512 |
| Pearson r | 0.6216 (6 h), 0.3032 (24 h) |
| sign agreement | 76.82% (6 h), 64.27% (24 h) |
| Jaccard of thresholded sets | 0.1571 (6 h), 0.0356 (24 h) |
| serum assays / analytes | 1094 / 1064 |
| serum significant rows / analytes | 178 / 169 |
| ST2 rank and OR | 2 of 1094, 3.0243 |
| IL1RL1 significant contrasts | 0 of 24, min adj.P 0.9614 |
| SELE / VCAM1 / CXCL8 adj.P | 0.4950 / 0.4965 / 0.1772 |
| ICAM1 adj.P | 0.0101 |
| shortlist, 219 core | 5 exact, 9 reconciled |
| shortlist, 315 core | 9 exact, 13 reconciled |

## The diagnostic

A reported count of 215–245 alongside a reproducibility-failure claim
indicates the mirror rule. Measured mirror values are 219, 239 and 241 across
the three base filters, so that column is nearly invariant to the base filter
the solver chose. A count in that band is therefore diagnostic of the rule,
not of the base.

Defensible counts span roughly 315 to 1720 depending on the declared
criterion. There is no count band to grade against. The predicate and the
timepoint conclusion are what matter.

## Near-miss forms of the verdict

| Form | Call |
|---|---|
| go, 6 h signature only, 24 h excluded | pass |
| go, with the 24 h arm to be repeated in a second model | pass |
| conditional go pending further models | pass if the timepoint distinction is made |
| bare go, no timepoint qualification | fail |
| no-go on reproducibility grounds | fail — this is the false optimum |
| go at both timepoints | fail |

## Deliberately not in the grading document

- Any absolute gene count as a target. The count is a legitimate degree of
  freedom.
- The mmc5 sheet-duplication hazard. It is a pre-registered failure mode and
  naming it in the grading document would flag the trap.
- The contrast-family choice. Both families give the same verdict, so it is
  not gradeable either way.
- The shortlist precision point. Three of the thirteen analytes have upper
  95% bounds above 20 — CSF-1 at 1932.572, CTSS at 200.019, BIRC2 at
  64.215 — so nominating them on point estimates is poor practice. It was not
  predicted before the odds ratios were read, so it is not graded; credit it
  under judgment if a solver raises it.
