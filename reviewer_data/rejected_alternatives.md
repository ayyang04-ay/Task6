# Rejected alternatives — reference for the FA

Moved out of the golden response. The prompt does not ask for a
considered-and-not-carried section, and under the Stage 7 rule that analysis
the prompt did not request is a defect rather than generosity, it does not
belong there. The content is kept because the FA counterfactuals draw on it.

Every figure recomputed from the shipped room; see `faithful_recompute.md` and
`scratch/analysis/verify_golden.py`.

## The alternatives and what closed each

| Option | Why not |
|---|---|
| **No-go on cross-line reproducibility grounds.** Intersecting the two threshold-filtered sets gives 219 of 1126 genes, a Jaccard of 0.1571, which reads as failure to reproduce. | The threshold is invalid on the second line. HGMEC effects are 2.7337× smaller over the same genes, so `\|logFC\| > 1` removes genes for magnitude, and the rule admits 11 sign-discordant genes. On direction and nominal significance the same data gives 315 of 1126 and r 0.6216. |
| **Carry both timepoints.** Both Jaccard values, 0.1571 and 0.0356, are low in absolute terms, which invites one uniform conclusion. | The statistics separate cleanly: r 0.6216 against 0.3032, sign agreement 76.82% against 64.27%, signature 315 against 23. The 6 h result reproduces and the 24 h result does not. |
| **Nominate soluble ST2 as the pharmacodynamic biomarker.** Second of 1094 analytes, OR 3.0243, and the pathway's own receptor. | `IL1RL1` is not significant in any of 24 contrasts, minimum `adj.P.Val` 0.9614. Prognostic, not pharmacodynamic. |
| **Report SELE and VCAM1 as the mechanism.** Among the largest fold changes and the expected endothelial biology. | `adj.P.Val` 0.4950 and 0.4965. Not attributable. |
| **Use the 1094-assay and 178-hit figures.** One row per assay is the obvious count. | 27 analytes sit on more than one panel. The reconciled figures are 1063 analytes and 169 significant. |
| **Discount HGMEC as the wrong vascular bed.** HUVEC is macrovascular venous, HGMEC glomerular microvascular; divergence is expected. | The same two lines agree at 6 h, r 0.6216 and 76.82% sign agreement. A bed-identity difference would apply at both timepoints. |
| **Pool the timepoints for power.** n = 3 per arm is small and pooling would increase it. | The question is which window to carry. Pooling cannot answer it, and the two windows differ in exactly the respect being tested. |
| **Draw on the lung tissue dataset.** `AX-1177_postmortem_lung.xlsx` carries IL-33 immunohistochemistry in endothelium across 78 blocks from 31 donors. | Unrelated cohort. `AX-1177_serum_proteomics.xlsx` reports assay-level summary statistics over 100 serum patients with no patient identifiers, so no link to the 31 tissue donors can be established or excluded. The tissue data cannot inform the in vitro conclusion. |

