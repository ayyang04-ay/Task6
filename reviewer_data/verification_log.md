# Verification log

Every figure below was recomputed from `scratch/source_untrusted/` by
`scratch/analysis/probe5.py` and `scratch/analysis/basin.py`. Counts use the
`24h` sheet of the source `mmc5.xlsx`, which carries all 24 contrasts without the row padding
present in the `6h` sheet.

## Confirmed

| Anchor | Brief | Measured |
|---|---|---|
| median \|logFC\| 6 h, HUVEC vs HGMEC | 2.01 / 0.74 | 2.0140 / 0.7367, 2.734x |
| median \|logFC\| 24 h | 2.23 / 0.51 | 2.2349 / 0.5136, 4.351x |
| Pearson r | 0.625 / 0.303 | 0.6216 / 0.3032 |
| sign agreement | 76.9% / 64.3% | 76.82% / 64.27% |
| mirror column | 218 | 219 |
| direction + nominal | 315 | 315 |
| attribution overlap | 6 | 6 |
| standalone HUVEC | 31 / 36 | 31 / 36 |
| standalone HGMEC | 62 / 67 | 62 / 67 |
| null floor MCF7 | 20 / 26 | 20 / 26 |
| IL1RL1 significant | 0 of 24 | 0 of 24, min adj.P 0.9614 |
| SELE / VCAM1 / CXCL8 adj.P | 0.495 / 0.497 / 0.177 | 0.4950 / 0.4965 / 0.1772 |
| ICAM1 adj.P | 0.0101 | 0.0101 |
| AveExpr constant across lines | asserted | 1.0989 in all 24 contrasts |
| AX-1177_serum_proteomics assays | 1094 | 1094 |
| AX-1177_serum_proteomics significant rows | 178 | 178 |
| ST2 rank, OR | 2, 3.02 | 2, 3.0243 |
| AX-1177_rnaseq_huvec_il33 HUVEC stimulation | 1068 / 512 | 1068 / 512 |
| AX-1177_postmortem_lung donors | 31 | 31 |

The brief's "replication 28.0% / 5.5%" is the direction-plus-nominal measure,
not the mirror rule: 315/1124 and 23/417. Both reproduce. The mirror rule
gives 219/1126 and 19/417, i.e. 19.45% and 4.56%. The anchor table and the
criterion grid label these differently and should be reconciled.

## Not confirmed

Superseded for the transcriptomic counts by `gene_universe_audit.md`. In
summary: 26,113 is the distinct-symbol count and is correct; 26,210 is the
locus count. Excluding Rfam symbols reproduces 485, 134, 15, 218 and the
2.73x ratio. Only two figures follow no tested rule:

| Anchor | Brief | All rows | Rfam excluded |
|---|---|---|---|
| HUVEC inhibition 6 h | 1124 | 1126 | 1122 |
| HUVEC inhibition 24 h | 417 | 417 | 415 |

1124 is the brief's headline count and is most likely a slip.

The AX-1177_serum_proteomics figures are a separate error that still stands:

| Anchor | Brief | Measured |
|---|---|---|
| AX-1177_serum_proteomics analytes | 1077 | 1063 |
| AX-1177_serum_proteomics significant analytes | 173 | 169 |
| analytes on more than one panel | 15, IL6 on three | 27, IL6 on four |

The AX-1177_serum_proteomics figures are a separate, independent error. Panel
suffixes are -ONCII, -ONCIII, -INFI, -CVDII, -CVDIII, -CRE, -IMO, -MET, -NEX,
-ODA, -NEUI. Stripping them leaves 1063 analytes. Omitting -NEUI yields 1064 and
is the origin of that figure: `GDNF-INFI` and `GDNF-NEUI` are one analyte on two
panels. `-CAM` is not a panel suffix here -- stripping it would mangle the
genuine analytes `Ep-CAM` and `Nr-CAM`. SCF and FGF-21 are on three panels,
IL6 on four.

## Not yet checked

- `df.total` 85.13, uniform across contrasts
- module composition of the 219-gene core (14 IFN, 9 NF-kB, 7 CSF/cytokine,
  9 chemokine, F3, C3)
- whether every absence anchor holds against the shipped annex

## Observations not in the brief

1. the source `mmc5.xlsx`'s two sheets carry the same 24 contrasts with identical values; 22
   are byte-identical and 2 differ only in row order. The `6h` sheet is
   dimensioned to Excel's 1,048,576-row ceiling, holding 629,040 data rows
   and 419,535 empty ones. `pd.read_excel` with default arguments reads that
   sheet and returns the padding; concatenating both sheets doubles every
   contrast. Either silently corrupts a count.
2. Two inhibition contrast families exist for both lines and both
   timepoints. `Compound_47_IL33_vs_IL33_NIP228_HUVEC_6hrs` is
   isotype-controlled (4239 / 1126); `Compound_47_IL33_vs_IL33_HUVEC_6hrs`
   is against IL-33 alone (4049 / 1075). A solver choosing the second gets a
   differently-controlled set that still looks defensible.
3. The source `mmc5.xlsx` carries the same `dc:creator` / `cp:lastModifiedBy` metadata as the
   other workbooks. The strip step applies to it too.

## df.total — confirmed, and it corroborates the design

Inverting `t` against `P.Value` for 400 genes per contrast gives
**df.total = 85.128**, identical in all 24 contrasts (min = max = median).
The brief's 85.13 is exact.

This independently supports the annex's experimental design:

| | |
|---|---|
| annex: 38 arm x timepoint groups, 114 libraries | 114 - 38 = 76 residual df |
| limma `df.total` = `df.residual` + `df.prior` | implied df.prior = 9.128 |
| annex: n = 3 biological replicates per arm | 38 x 3 = 114 |

A df.prior near 9 is ordinary for empirical Bayes moderation on a fit this
size. The design is internally consistent and the data agrees with it.

Taken with the constant AveExpr (1.0989 in all 24 contrasts), this confirms a
single linear model fitted across the whole dataset, as the annex states.

## What the pub does and does not settle

The paper's endothelial methods describe **only** the HUVEC experiment:
HUVEC passage 2, rRNA depletion, NovaSeq 2 x 100, 25 M reads. The delivered
data covers four cell lines and 24 contrasts, so the paper under-describes its
own deposit. Its library-prep figures therefore describe the HUVEC arm it
documented, not necessarily the whole 114-library fit.

Consequence: the mounted annex matches the paper on library prep (rRNA
depletion, 2 x 100 bp, 25 M read pairs) and on HUVEC passage (P2), so there is
no annex-versus-paper divergence to settle. An earlier draft of
`source_brief/AX-1177_methods_annex.md` carried poly(A), 2 x 150 / 30 M, P4 and
a TMM / <10-count filter; that draft was never mounted in any version. The
design claims the data does settle — four lines, 114 libraries, 38 groups,
single fit, n = 3 — all hold.
