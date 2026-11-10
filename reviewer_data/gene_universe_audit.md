# Gene universe audit

Question: the brief states 26,113 genes per contrast and a HUVEC 6 h
attributable set of 1124, where the shipped file gives 26,210 rows and 1126.

## 26,113 is correct, and it is not a row count

| Quantity | Value |
|---|---|
| rows per contrast | 26,210 |
| distinct Ensembl IDs | 26,210 (no duplicates) |
| distinct gene symbols | **26,113** |

97 extra rows come from 20 symbols that sit on more than one locus. The
large ones are Rfam non-coding RNA families:

| Symbol | Loci | What it is |
|---|---|---|
| RF00019 | 62 | Y RNA |
| RF00017 | 15 | Metazoa_SRP |
| RF00012 | 4 | U3 snoRNA |
| RF02271, RF00072 | 3 each | |
| RF00026 | 2 | U6 snRNA |
| RF00003 | 2 | U1 snRNA |
| ATXN7 | 2 | protein-coding |

So 26,113 counts genes by symbol and 26,210 counts them by locus. Both are
defensible; they are different quantities. The brief's figure is right and my
earlier note calling it unconfirmed was wrong.

## AX-1177_rnaseq_huvec_il33 and AX-1177_rnaseq_contrasts share one universe

Identical 26,210 Ensembl sets, identical symbol mapping, 26,113 distinct
symbols in each, zero symbol mismatches on shared IDs. The stimulation-to-
inhibition join is safe.

This follows from the methods: both come from the same pipeline. The paper
runs two unrelated RNA-seq pipelines and only one produced these files.

| | post-mortem lung bulk | endothelial (AX-1177_rnaseq_huvec_il33, AX-1177_rnaseq_contrasts) |
|---|---|---|
| reference | GRCh38 ensembl v100 | HG38 + ENSEMBL94 GTF |
| quantification | NGmerge, Salmon | STAR 2.6.1d, featureCounts |
| differential expression | DESeq2, apeglm | voom, limma |

The v100 reference belongs to the lung tissue work, which is not delivered as
a workbook. Nothing in AX-1177_rnaseq_huvec_il33 or AX-1177_rnaseq_contrasts was built against it. The annex's
"aligned to GRCh38" is consistent; HG38 and GRCh38 are the same assembly. The
mounted annex states only that low-expression genes were removed and that
counts were normalised and transformed with voom; it names neither TMM nor a
<10-count threshold. An unmounted draft of the annex source did, which is where
an earlier version of this note came from.

## The rule behind the counts: Rfam exclusion

Excluding symbols matching `^RF\d+$` reproduces most of the brief.

| Contrast | Brief | All rows | Rfam excluded |
|---|---|---|---|
| HGMEC inhibition 6 h | 485 | 487 | **485** |
| HGMEC inhibition 24 h | 134 | 135 | **134** |
| A549 isotype 24 h | 15 | 17 | **15** |
| HUVEC standalone 6 h | 31 | 31 | **31** |
| HGMEC standalone 6 h | 62 | 62 | **62** |
| mirror column, 6 h | 218 | 219 | **218** |
| direction + nominal, 6 h | 315 | 315 | **315** |
| median \|logFC\| ratio, 6 h | 2.73x | 2.734x | **2.728x** |
| HUVEC inhibition 24 h | 417 | **417** | 415 |
| HUVEC inhibition 6 h | 1124 | 1126 | 1122 |

Rfam exclusion is the better methodological choice independently of what the
brief did. RF00019 on 62 loci is multi-mapping across a repeated small-RNA
family, not 62 regulated genes, and leaving it in inflates every count with
duplicated symbols.

## What does not reconcile

Two figures follow neither rule:

- **HUVEC inhibition 6 h: 1124.** All rows give 1126, Rfam exclusion 1122,
  symbol-level deduplication 1125. No tested rule gives 1124. This is the
  brief's headline count and the base of its criterion grid.
- **HUVEC inhibition 24 h: 417.** Matches all rows exactly, where the same
  contrast's partners match only under Rfam exclusion.

Rules tested and rejected: symbol-level deduplication; entrez or gene_name
non-null; AveExpr > 0; symbol not ENSG-like; symbol != ensembl; `>=` instead
of `>` on either threshold; `<=` on adj.P; adj.P rounded to 3 dp; logFC
rounded to 1 or 2 dp; adj.P < 0.049; up-regulated only; and each annotation
filter crossed with symbol deduplication. Both sheets give identical results
under every variant.

The conclusion is that the brief's counts were not produced by one consistent
rule. 1124 is most likely a transcription slip for 1122 or 1126.

## Consequence

None of this touches the basin or the verdict. Under both rules the effect is
the same size and the timepoint split is the same:

| | 6 h | 24 h |
|---|---|---|
| median \|logFC\| HUVEC vs HGMEC, all rows | 2.0140 / 0.7367 (2.734x) | 2.2349 / 0.5136 (4.351x) |
| median \|logFC\|, Rfam excluded | 2.0109 / 0.7371 (2.728x) | 2.2252 / 0.5136 (4.332x) |
| Pearson r, all rows | 0.6216 | 0.3032 |
| Pearson r, Rfam excluded | 0.6259 | 0.3074 |
| sign agreement, Rfam excluded | 77.01% | 64.58% |

The brief's r of 0.625 sits between the two; Rfam exclusion is the closer
match, as it is for the median ratio and the mirror count.

## Recommendation

1. Adopt Rfam exclusion and state it in the criterion predicate, not as a
   footnote. It changes the headline count.
2. Recompute every count in the criterion grid and the golden from the
   shipped data room after the metadata strip, per the brief's own build
   constraint. Do not carry 1124 forward.
3. Decide whether "gene" means symbol or locus and use one throughout. The
   brief currently uses symbol for the universe and locus for at least one
   count.
