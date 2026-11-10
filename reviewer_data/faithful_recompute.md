# Faithful recompute

Predicate: every row as delivered in `AX-1177_rnaseq_contrasts.xlsx`. No gene-class filter, no
symbol deduplication, no annotation requirement. Contrast
`Compound_47_IL33_vs_IL33_NIP228_<line>_<tp>` throughout, read from the `24h`
sheet, which carries all 24 contrasts without the row padding in the `6h`
sheet.

## HUVEC 6 h criterion grid

| base filter | n | mirror | sign+adj<.05 | sign+adj<.10 | sign+rawP<.05 | sign+\|lFC\|>0.5 | sign only |
|---|---|---|---|---|---|---|---|
| adj.P<.05 only | **4239** | **241** | 951 | 1147 | 1720 | 776 | **3525** |
| adj.P<.05, \|lFC\|>0.585 | **1825** | **239** | 556 | 623 | 846 | 732 | **1496** |
| adj.P<.05, \|lFC\|>1 | **1126** | **219** | 315 | 348 | 458 | 579 | **865** |

HUVEC 24 h at adj.P<.05, |lFC|>1: n 417, mirror 19, sign+adj<.05 23,
sign only 268.

Bold cells differ from the brief; the rest are identical to it. The mirror
column stays nearly invariant at 241 / 239 / 219, so the diagnostic the brief
describes holds: a reported count in the 215-245 range alongside a
reproducibility-failure claim indicates the mirror rule.

### The brief dropped two genes

Every cell resting on HGMEC's own statistics matches the brief exactly. Every
cell counting the HUVEC base is +2 and every mirror cell +1, at all three
base thresholds. So the brief excluded exactly two genes from the HUVEC base,
one of which fell in the mirror set.

Two is not Rfam exclusion (removes 4), not symbol deduplication (removes 1),
and not any of the ~20 rules in `gene_universe_audit.md`. The two genes are
unidentified. This changes no conclusion and is left open.

## Translational shortlist

Serum analytes with adj.p < 0.05 in `AX-1177_serum_proteomics.xlsx` whose gene appears in the
HUVEC 6 h core:

| Core | n | Analytes |
|---|---|---|
| mirror, 219 | **9** | B4GALT1, CCL20, CSF-1, CTSS, IL-18R1, IL1B, IL6, MCP-3, OPG |
| direction + nominal, 315 | **13** | adds BIRC2, FSTL3, TANK, TRIM21 |

The brief gives 6 and 10. Its six are all present here; the three additions
are CSF-1, IL-18R1 and MCP-3, which carry Olink's legacy assay names rather
than current gene symbols:

| Olink assay | Gene |
|---|---|
| CSF-1 | CSF1 |
| IL-18R1 | IL18R1 |
| MCP-3 | CCL7 |
| OPG | TNFRSF11B |

A join on exact symbol string misses the first three and would miss OPG too.
This is the same class of error as the analyte count: Olink assay identifiers
are not gene symbols.

**Caveat.** The mapping above is hand-built, so 9 and 13 are not settled
either. A defensible shortlist needs the Olink panel definitions mapped to
UniProt or Entrez systematically rather than by name matching. Until that is
done, treat 9 and 13 as a lower bound on what a symbol-only join misses, not
as the answer.

`IL1RL1` is absent from both cores, so the sST2 exclusion holds on the
faithful predicate.

## AX-1177_serum_proteomics, faithful

1094 assays, 1064 analytes, 178 significant rows, 169 significant analytes.
26 analytes on more than one panel; IL6 on four, SCF and FGF-21 on three.

## The two inhibition contrast families give the same verdict

Both families exist for both endothelial lines and both timepoints. Running
the full basin on each:

| Family | tp | n | med HUVEC | med HGMEC | ratio | r | sign | dir+nom |
|---|---|---|---|---|---|---|---|---|
| isotype-controlled | 6 h | 1126 | 2.0140 | 0.7367 | 2.734x | 0.6216 | 76.82% | 28.0% |
| isotype-controlled | 24 h | 417 | 2.2349 | 0.5136 | 4.351x | 0.3032 | 64.27% | 5.5% |
| IL-33 alone | 6 h | 1075 | 2.0058 | 0.7145 | 2.807x | 0.6481 | 78.60% | 29.7% |
| IL-33 alone | 24 h | 547 | 2.1878 | 0.4434 | 4.934x | 0.2321 | 58.50% | 6.6% |

`isotype-controlled` is `Compound_47_IL33_vs_IL33_NIP228_<line>_<tp>`;
`IL-33 alone` is `Compound_47_IL33_vs_IL33_<line>_<tp>`.

Every structural feature survives the substitution, and three of them are
larger on the non-isotype contrast: attenuation 2.81x and 4.93x against
2.73x and 4.35x, the r gap 0.648 to 0.232 against 0.622 to 0.303, and the
sign gap 78.6% to 58.5% against 76.8% to 64.3%.

**Consequence for the design.** A solver who picks the non-isotype contrast
reaches the same conclusion: HGMEC is attenuated at both timepoints, 6 h
carries and 24 h does not. A careful expert could defend either choice, so
this is not a failure mode by the FA bar. It belongs in the derivation notes
as a degree of freedom the verdict is robust to, not in the pre-registered
mode table.

The one measurable cost of the wrong choice: the 24 h attributable set
inflates from 417 to 547. Those extra 130 genes carry a ligand-independent
antibody term that the isotype arm removes. That is a real defect in the
derivation, and worth credit if a solver names it, but it does not move the
recommendation.

## Module composition of the mirror core

219 genes, 219 distinct symbols. Counts under a regex over gene symbols:

| Module | Brief | Measured | Members |
|---|---|---|---|
| interferon | 14 | **14** | EPSTI1, HELZ2, IFIH1, IFIT1, IFIT2, IFIT3, IRF1, ISG20, MX1, OAS3, OASL, RSAD2, SAMD9L, XAF1 |
| chemokine | 9 | **9** | CCL5, CCL7, CCL20, CX3CL1, CXCL2, CXCL3, CXCL5, CXCL6, CXCL10 |
| NF-kB | 9 | **10** | BIRC3, NFKB1, NFKB2, NFKBIA, NFKBIE, NFKBIZ, RELB, TNFAIP3, TNFAIP6, TRAF1 |
| CSF and cytokine | 7 | **15** | CSF1, CSF2, CSF3, IL1A, IL1B, IL6, IL15, IL15RA, IL18R1, IL32, IL4I1, IL9RP3, LIF, TNF, TNFSF15 |

Interferon and chemokine match exactly. NF-kB differs by BIRC3 alone, which
is an IAP and arguably outside the module. The CSF and cytokine count is
definition-dependent: a narrow reading of CSF1-3, IL1A, IL1B, IL6, TNF gives
7, the brief's figure. Neither is an error; the module predicate has to be
stated in the golden rather than the count quoted bare.

`NFKB2` at -2.8605 and `RELB` at -3.2667 are both present, as the brief says.
`F3` at -5.4739 and `C3` at -4.6241 likewise.

### "all negative" needs qualifying

The brief's leg 6 says the core is "all negative". **184 of 219 are negative
and 35 are positive.** But zero of the positives belong to any named module:
they are SLC14A1, FSTL4, NDP, GAP43, CNFN, ABCC11, GATM, MLXIPL, ZNF177,
SYTL1, C2orf72, plus antisense and lincRNA transcripts, two pseudogenes and
RF00003.

So the claim is true of the named inflammatory modules and false of the core
as a whole. The golden should say "every member of the named modules is
negative", not "all negative".

Full membership in `scratch/analysis/mirror_core_symbols.json`.

## AX-1177_postmortem_lung `Tissue RNA` column

22 of 78 blocks carry an identifier of the form `Zr4940_<n>`, 20 distinct
values. The count matches the paper's lung bulk RNA-seq cohort exactly:
n = 9 COVID, n = 9 non-COVID pneumonia, n = 4 non-pneumonia, total 22.

So the column is a join key into the lung RNA-seq dataset, which is not
delivered in any workbook. It points at data a solver cannot reach.

## Leg 5 and the Jaccard figures

| Claim | Brief | Measured |
|---|---|---|
| Jaccard of the two thresholded sets | 0.157 / 0.036 | **0.1571 / 0.0356** |
| recovered genes begin at magnitude rank | 61 | **79** |

The Jaccard figures are exact: 219/1394 at 6 h and 19/533 at 24 h. The brief
never names them as Jaccard indices; the `both-windows-rejection` row carries
them bare, which is why they were hard to place.

Leg 5's magnitude rank is wrong. Ranking the 1126-gene HUVEC base by |logFC|
descending, the 107 genes recovered by the direction-plus-nominal rule but
missed by the mirror rule begin at **rank 79**, ACKR3 at |logFC| 3.710. The
next five are SERPINB2 (152), GCH1 (244), AL356534.1 (383), NOCT (408),
RBM47 (472). The argument is unaffected and arguably stronger: the recovered
genes are spread from rank 79 to the tail, not clustered low.

## Translational shortlist, settled

| Join rule | 219 core | 315 core |
|---|---|---|
| exact symbol string | 5 | 9 |
| legacy names reconciled | **9** | **13** |

Four aliases, each with one correct answer: CSF-1 -> CSF1, IL-18R1 -> IL18R1,
MCP-3 -> CCL7, OPG -> TNFRSF11B.

The reconciliation is determinate, not open-ended: of the 169 significant
analytes every name maps to a symbol, so the alias set is closed. Only 15 of
the 169 are not bare uppercase strings, and OPG shows that bare uppercase does
not imply identity.

The brief's figure of 6 is exact matching plus the OPG alias alone. No stated
rule produces it. The golden reconciles and reports 9 and 13.

## Attribution: how discoverable is the check, and what does it cost to skip

### Discoverability

Of the 24 contrasts in AX-1177_rnaseq_contrasts, **16 contain no IL-33 at all** — they are
antibody-against-control contrasts in all four lines, with DMSO and PBS arms
for the epithelial pair. Only 8 involve IL-33.

So two thirds of the file is antibody-without-ligand data, sitting in the same
`Comparison` column as the inhibition contrasts. Anyone who lists the
contrasts sees them. The check is one filter away, not buried.

### What the antibody alone does

| Line | arm | 6 h | 24 h |
|---|---|---|---|
| HUVEC | vs NIP228 | 31 | 36 |
| HGMEC | vs NIP228 | 62 | 67 |
| A549 | vs NIP228 | 27 | 17 |
| A549 | vs DMSO | 29 | 27 |
| A549 | vs PBS | 37 | 36 |
| MCF7 | vs NIP228 | 20 | 26 |
| MCF7 | vs DMSO | 30 | 30 |
| MCF7 | vs PBS | 40 | 13 |

The receptor-null floor runs 13 to 40. HUVEC at 31 and 36 sits inside it.
**HGMEC at 62 and 67 sits above it**, roughly double, which is the one result
in this table that is not obviously background.

### Does it contaminate the inhibition sets

| Line | tp | inhibition | standalone | overlap | % of inhibition |
|---|---|---|---|---|---|
| HUVEC | 6 h | 1126 | 31 | 6 | 0.53% |
| HUVEC | 24 h | 417 | 36 | 6 | 1.44% |
| HGMEC | 6 h | 487 | 62 | 1 | 0.21% |
| HGMEC | 24 h | 135 | 67 | 2 | 1.48% |

Negligible everywhere, and the shared genes are mostly unannotated
transcripts: AC008105.1, AC027088.5, DHRS2, EPHA7, FGF18, MMP3 at HUVEC 6 h;
AC091133.2 alone at HGMEC 6 h.

### Consequence of skipping

Removing every standalone-significant gene from the HUVEC base leaves the
basin unchanged:

| tp | set | n | median HUVEC / HGMEC | ratio |
|---|---|---|---|---|
| 6 h | all | 1126 | 2.0140 / 0.7367 | 2.734x |
| 6 h | standalone removed | 1114 | 2.0154 / 0.7371 | **2.734x** |
| 24 h | all | 417 | 2.2349 / 0.5136 | 4.351x |
| 24 h | standalone removed | 408 | 2.2373 / 0.5137 | **4.355x** |

So the check is cheap, highly discoverable, and confirms the result. Skipping
it leaves a premise unverified but costs nothing numerically.
