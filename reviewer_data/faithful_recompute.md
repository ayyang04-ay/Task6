# Faithful recompute

Predicate: every row as delivered in `mmc5.xlsx`. No gene-class filter, no
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

Serum analytes with adj.p < 0.05 in `mmc2.xlsx` whose gene appears in the
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

## mmc2, faithful

1094 assays, 1064 analytes, 178 significant rows, 169 significant analytes.
26 analytes on more than one panel; IL6 on four, SCF and FGF-21 on three.
