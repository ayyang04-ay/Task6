You are grading a portfolio-audit recommendation on an anti-IL-33 antibody in
preclinical development for viral lower respiratory tract disease. The solver
has in vitro transcriptomic contrasts across four cell lines and two
timepoints, a serum proteomic association dataset from 100 hospitalised
patients, post-mortem lung immunohistochemistry from an unrelated cohort, and
a methods annex. The recommendation turns on what the data shows about the
programme the antibody blocks, and on what it cannot show.

A) MUST BE PRESENT AND CORRECT
The following are the key requirements of a correct answer. Use your judgment
to identify any additional required content not listed here.
- A recommendation on keeping the asset, argued from the delivered data rather
  than asserted.
- An answer on indication that rests on what the data shows IL-33 actually
  drives, read off genes whose statistics are usable. In the HUVEC stimulation
  contrast the implied standard error is `|logFC / t|` against a file median of
  0.339. Readable and significant: the interferon genes (IFIT1-3, MX1, OAS3,
  OASL, IRF1, ISG20, RSAD2, CXCL10), the chemokines CXCL2, CXCL3, CXCL5 and
  CXCL6, CSF2, CSF3, TNF, IL6 and IL1B, and a procoagulant shift with tissue
  factor and SERPINE1 up and thrombomodulin down. Readable and null: IL4, TSLP
  and CCL26, which is the type 2 evidence the stimulation data actually
  supports.
  Three cautions. CXCL1 and CXCL8 are neutrophil chemokines but their standard
  errors are 1154.9 and 4.1, so an answer is right to exclude them and should
  not be marked down for doing so. GATA3 and IL1RL1 carry standard errors of
  22.9 and 8.3 and cannot be read in either direction, so an answer that omits
  them is correct and one that rests a type 2 conclusion on them is not. IL5,
  IL13, CCL11, CCL24 and IL25 are absent from the gene universe rather than
  unchanged, so no conclusion follows from their absence.
  A proposal that names an indication without engaging what the blocked
  programme consists of has not answered the question.
- A sampling timepoint, with a reason drawn from the data. 6 h is where the
  response reproduces across both endothelial lines and 24 h is where it does
  not, so a proposal sampling at 6 h, or sampling both and treating 24 h as
  exploratory, is supported. Other timepoints are acceptable where the reason
  given is grounded.
- Recognition that the package does not establish causality: no file contains
  a virus, an animal or a dose, and the serum dataset has no treatment arm.
- Where cross-line reproducibility is assessed, the 6 h result and the 24 h
  result distinguished, with the figures that separate them.
- Biomarker proposals with the role each would play distinguished —
  pharmacodynamic, target engagement, or patient selection.
- Quantitative results cited with the file they came from and how they were
  reduced.
- A set-aside section naming what was considered and rejected, with the reason
  that closed each.

B) PENALIZE FOR
The following are common errors observed on this task. This list is not
exhaustive — apply your judgment to any other issues you identify.
- Carrying a type 2 inflammatory framing, or naming a type 2 indication,
  without reference to what the stimulation data shows. IL4, TSLP and CCL26 are
  measured with usable standard errors and none moves, while the interferon
  genes, CXCL2/3/5/6, CSF2, CSF3, TNF, IL6 and IL1B are significant and tissue
  factor and SERPINE1 rise as thrombomodulin falls.
- Resting a conclusion in either direction on GATA3 or IL1RL1, whose standard
  errors of 22.9 and 8.3 against a median of 0.339 make them unreadable, or on
  the absence of IL5, IL13, CCL11, CCL24 and IL25, which were filtered as
  unexpressed.
- Treating an overlap between the in vitro signature and the prognostic serum
  analytes as evidence without testing it against the base rate. In this panel
  893 of 1094 odds ratios exceed 1 and 176 of the 178 significant rows point
  the same way, so being prognostic is close to universal and an intersection
  establishes nothing until it is shown to exceed chance.
- Using the between-cell-line effect-size difference only to adjust a
  threshold, and then recommending a model system or a confirmatory study
  without reference to it. The same effect differs by roughly 2.7-fold at 6 h
  and 4.4-fold at 24 h between two cell lines, neither of which is pulmonary,
  which bears directly on what the next experiment has to be run in.
- Treating the odds ratios for CSF-1, CTSS or BIRC2 as estimated magnitudes
  when their confidence intervals span orders of magnitude.
- Concluding that the response does not reproduce across cell lines on the
  basis of intersecting two threshold-filtered gene sets, where effect sizes
  in the second line are roughly 2.7-fold smaller over the same genes.
- Reporting 1094 proteins, or 178 significant proteins, where those figures
  count assays rather than analytes. The reconciled figures are 1063 and 169.
- Nominating soluble ST2 as a pharmacodynamic or target-engagement readout.
  It is the decoy receptor for the drug's own target, so its serum level tracks
  pathway activity and disease severity at once and a post-dose fall cannot be
  attributed to engagement rather than recovery. Markers downstream of the
  receptor do not carry that confound, so this applies to sST2 specifically and
  not to the other candidates. Offering it for stratification or enrichment is
  correct and should not be penalised.
- Citing SELE, VCAM1, CXCL8 or CXCL1 as part of the blocked response without
  addressing their standard errors of 8.9, 7.1, 4.1 and 1154.9 against a median
  of 0.339. An answer that names them and explains why it is not relying on
  them has handled this correctly.
- Stating affinity, potency or exposure values, which are not in the delivered
  package.

C) NEUTRAL
The following are examples of acceptable variations that should not affect the
score. Other variations may also be neutral — use your judgment.
- Whether the recommendation is to keep the asset or to drop it. Either is
  acceptable where the case is built from the data; the reasoning and the
  pillars supporting it are what is being graded, not the verdict.
- Which indication is named, provided it follows from what the data shows the
  antibody blocks.
- The reproducibility criterion chosen and the resulting gene count, provided
  the criterion is stated and the count follows from it.
- How Olink assay identifiers are matched to genes. Exact symbol matching and
  reconciliation of legacy assay names such as OPG, CSF-1, IL-18R1 and MCP-3
  are both defensible and give different shortlists.
- Length, ordering, section structure, and where in the answer any particular
  point appears, including the recommendation.
- Whether supporting analysis is presented as tables, prose or figures.
- Noting that one endothelial line has no unstimulated baseline arm, that the
  serum multiplicity correction implies more tests than were delivered, or that
  the two sheets of the largest workbook hold the same contrasts.
