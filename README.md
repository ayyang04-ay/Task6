# AX-1177 — anti-IL-33 mechanistic package (Anton task)

Source: *IL-33 is associated with alveolar dysfunction in patients with viral
lower respiratory tract disease*, Mucosal Immunology, 10.1016/j.mucimm.2024.12.001
(PMC11982439). Supplementary files mmc1-mmc6.

## Layout

| Path | What it is | Model-facing? |
|---|---|---|
| `data_room/` | the evidence world | **yes**, when built |
| `reviewer_data/` | brief, annex, spine, verification | no |
| `scratch/source_untrusted/` | the original supplementary files, unmodified | no |
| `scratch/analysis/` | verification scripts and their output | no |

`scratch/` is gitignored. mmc5.xlsx is 133 MB and needs Git LFS to be committed.

## Source files on disk

| File | Supp. table | Contents |
|---|---|---|
| `mmc1.pdf` | — | supplementary methods. **Not mounted** |
| `mmc2.xlsx` | ST7 | Olink serum associations, 1094 assays |
| `mmc3.xlsx` | ST8 + ST9 | 78 histology blocks, 31 donors |
| `mmc4.xlsx` | ST10a | HUVEC IL-33red vs vehicle, 6 h and 24 h |
| `mmc5.xlsx` | ST10b | 24 contrasts, four cell lines, both timepoints |
| mmc6 | ST12 | ISARIC4C investigator list. **Dropped** |

## State

Scoping. No prompt, no golden, no grader, no mounted data room.

### Verified against the brief

The hidden basin reproduces: median |logFC| over the HUVEC 6 h attributable
set is 2.0140 in HUVEC and 0.7367 in HGMEC (2.734x); at 24 h, 2.2349 and
0.5136 (4.351x). r 0.6216 / 0.3032. Sign agreement 76.82% / 64.27%.
Attribution overlap 6. IL1RL1 significant in 0 of 24 contrasts. SELE,
VCAM1, CXCL8 at adj.P 0.4950, 0.4965, 0.1772; ICAM1 at 0.0101. AveExpr
identical across all 24 contrasts, confirming the single-model fit.

### Open before anything is written

1. Gene universe. The brief's counts assume 26,113 genes per contrast;
   mmc5 carries 26,210. This shifts several counts by 1-2 and is why the
   brief reads 1124 where the file gives 1126.
2. mmc2 reconciliation. The brief says 1077 analytes and 173 significant;
   the file gives 1064 and 169, with 26 analytes on more than one panel and
   IL6 on four. All three figures in the brief are wrong.
3. A549 24 h null floor. Brief says 15, file gives 17.
4. mmc5 holds the same 24 contrasts twice, in sheets named `6h` and `24h`,
   values identical. The `6h` sheet is padded to 1,048,576 rows with
   419,535 empty ones. Reading sheet 0 by default picks up the padding.
5. Two inhibition contrast families exist. `..._IL33_vs_IL33_NIP228_*` is
   isotype-controlled; `..._IL33_vs_IL33_*` is against IL-33 alone. The
   brief uses only the first.
6. `df.total` and the module composition of the 219-gene core are unchecked.
