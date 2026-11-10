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

`scratch/` is gitignored. The largest workbook is ~123 MB as committed (the untouched original in `scratch/source_untrusted/mmc5.xlsx` is ~139 MB) and needs Git LFS.

## Source files on disk

Mounted files were renamed from the publisher's `mmc*` convention, which is an
Elsevier supplementary-material tell: 8 of 8 v3 runs pattern-matched the room to
a published study, four of them naming the convention itself. The reagent string
`NIP228` was separately replaced with `IC119`.

The rename alone changed no bytes: the serum, post-mortem and HUVEC workbooks
keep their LFS object ids (`ecb1903f2c`, `efc6428491`, `b089bd1cbe`). The
contrasts workbook has a new object id because the `NIP228` substitution touches
14 bytes of it — 12 in `xl/sharedStrings.xml` and one AutoFilter criterion per
worksheet. Its three changed parts are byte-identical to the originals after the
same substitution and its other six parts are untouched, so no numeric cell
moved. `data_room/` is reproduced from the pristine sources by
`scratch/analysis/strip_meta.py`, which verifies exactly that.

| Mounted as | Source file | Supp. table | Contents |
|---|---|---|---|
| — | `mmc1.pdf` | — | supplementary methods. **Not mounted** |
| `AX-1177_serum_proteomics.xlsx` | `mmc2.xlsx` | ST7 | Olink serum associations, 1094 assays |
| `AX-1177_postmortem_lung.xlsx` | `mmc3.xlsx` | ST8 + ST9 | 74 histology blocks, 31 donors |
| `AX-1177_rnaseq_huvec_il33.xlsx` | `mmc4.xlsx` | ST10a | HUVEC IL-33red vs vehicle, 6 h and 24 h |
| `AX-1177_rnaseq_contrasts.xlsx` | `mmc5.xlsx` | ST10b | 24 contrasts, four cell lines, both timepoints |
| — | mmc6 | ST12 | ISARIC4C investigator list. **Dropped** |

The post-mortem sheet has 78 rows below its header but only **74** carry a
Histology Block ID: rows 17, 18, 68 and 69 are fully blank spacers, and row 80
is a trailing blank. `len(pd.read_excel(...))` returns 78 and is not a block
count. The donor count of 31 is unaffected.

Licence: the source article is **CC BY 4.0** (PMC states "This is an open access
article under the CC BY license", Elsevier Sponsored Documents; © 2025
AstraZeneca UK LTD). PubMed's API reports "All rights reserved" for this PMID —
that is the publisher copyright line, not the licence, and it is wrong here.

## State

v3 shipped and re-run; v4 pending after the de-identification changes. Prompt,
golden, grader and mounted data room all present.

### Verified against the brief

The hidden basin reproduces: median |logFC| over the HUVEC 6 h attributable
set is 2.0140 in HUVEC and 0.7367 in HGMEC (2.734x); at 24 h, 2.2349 and
0.5136 (4.351x). r 0.6216 / 0.3032. Sign agreement 76.82% / 64.27%.
Attribution overlap 6. IL1RL1 significant in 0 of 24 contrasts. SELE,
VCAM1, CXCL8 at adj.P 0.4950, 0.4965, 0.1772; ICAM1 at 0.0101. AveExpr
identical across all 24 contrasts, confirming the single-model fit.

### Open before anything is written

1. Gene universe. The brief's counts assume 26,113 genes per contrast;
   `AX-1177_rnaseq_contrasts.xlsx` carries 26,210. This shifts several counts by 1-2 and is why the
   brief reads 1124 where the file gives 1126.
2. `AX-1177_serum_proteomics.xlsx` reconciliation. The brief says 1077 analytes and 173 significant;
   the file gives 1063 and 169, with 27 analytes on more than one panel and
   IL6 on four. All three figures in the brief are wrong.
3. A549 24 h null floor. Brief says 15, file gives 17.
4. `AX-1177_rnaseq_contrasts.xlsx` holds the same 24 contrasts twice, in sheets named `6h` and `24h`,
   values identical. The `6h` sheet is padded to 1,048,576 rows with
   419,535 empty ones. Reading sheet 0 by default picks up the padding.
5. Two inhibition contrast families exist. `..._IL33_vs_IL33_IC119_*` is
   isotype-controlled; `..._IL33_vs_IL33_*` is against IL-33 alone. The
   brief uses only the first.
6. `df.total` and the module composition of the 219-gene core are unchecked.
