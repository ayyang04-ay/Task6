You are grading a portfolio-audit recommendation on an anti-IL-33 antibody in preclinical development for severe lower respiratory viral infection. The solver has in vitro transcriptomic contrasts across four cell lines and two timepoints, a serum proteomic association dataset from 100 hospitalised patients, post-mortem lung immunohistochemistry from an unrelated cohort, and a methods annex. The recommendation turns on what the data shows about the programme the antibody blocks, and on what it cannot show.

A) MUST BE PRESENT AND CORRECT

The following are the key requirements of a correct answer. Use your judgment to identify any additional required content not listed here.

A recommendation on keeping the asset, argued from the delivered data rather than asserted.

An answer on indication that rests on what the data shows IL-33 actually drives, read off genes whose statistics are usable. In the HUVEC stimulation contrast the implied standard error is |logFC / t| against a file median of 0.339. Readable and significant: the interferon genes (IFIT1-3, MX1, OAS3, OASL, IRF1, ISG20, RSAD2, CXCL10), the chemokines CXCL2, CXCL3, CXCL5 and CXCL6, CSF2, CSF3, TNF, IL6 and IL1B, and a procoagulant shift with tissue factor and SERPINE1 up and thrombomodulin down. A proposal that names an indication without engaging what the blocked programme consists of has not answered the question.

Three cautions on individual genes. CXCL1 and CXCL8 are neutrophil chemokines but their standard errors are 1154.9 and 4.1, so an answer is right to exclude them and should not be marked down for doing so. GATA3 and IL1RL1 carry standard errors of 22.9 and 8.3 and cannot be read in either direction, so an answer that omits them is correct and one that rests a conclusion on them is not. IL5, IL13, CCL11, CCL24 and IL25 are absent from the gene universe rather than unchanged, so no conclusion follows from their absence.

The stimulation data cannot test type 2 biology, and an answer that says so is correct. The only IL-33 arms are HUVEC and HGMEC endothelial monocultures; A549 and MCF7 never received IL-33. Those cultures contain none of the cells through which IL-33 drives a type 2 response, and IL4 and TSLP sit at AveExpr -4.16 and -4.00 against a file median of 0.50, in the bottom tenth of the expression range, so their flat logFCs are uninformative rather than negative. Credit either of two readings: that type 2 was not tested in vitro, or that these nulls carry no information. Where type 2 is excluded, the support for that is the human data, where nine type 2 and effector-cell markers are null against the endpoint (IL5 OR 1.001, eotaxin-1 on two panels, eotaxin-2, CCL17, tryptase, IL-5Ra, KIT, CD63) and the tissue eosinophil, basophil and mast cell scores do not separate COVID-positive from COVID-negative pneumonia.

A sampling timepoint, with a reason drawn from the data. Over the 1124 genes attributable at 6 h in HUVEC, 315 reproduce in HGMEC on the same sign plus adj.P.Val below 0.05, against 23 of the 417 attributable at 24 h. A proposal sampling at 6 h, or sampling both and treating 24 h as exploratory, is supported. Other timepoints are acceptable where the reason given is grounded.

Recognition that the package does not establish causality: no file contains a virus, an animal or a dose, and the serum dataset has no treatment arm.

Where cross-line reproducibility is assessed, the 6 h result and the 24 h result distinguished, with the figures that separate them.

Biomarker proposals with the role each would play distinguished: pharmacodynamic, target engagement, or patient selection.

Quantitative results cited with the file they came from and how they were reduced.

A set-aside section naming what was considered and rejected, with the reason that closed each.

B) PENALIZE FOR

The following are common errors observed on this task. This list is not exhaustive. Apply your judgment to any other issues you identify.

Building a type 2 case, or naming a type 2 indication, without reference to the human data. The serum type 2 axis is null and the tissue granulocyte scores do not separate COVID-positive from COVID-negative pneumonia. Do not penalise an answer for declining to read the IL4, TSLP and CCL26 nulls as type 2 evidence; that reading is correct.

Resting a conclusion in either direction on GATA3 or IL1RL1, whose standard errors of 22.9 and 8.3 against a median of 0.339 make them unreadable, or on the absence of IL5, IL13, CCL11, CCL24 and IL25, which were filtered as unexpressed.

Treating an overlap between the in vitro signature and the prognostic serum analytes as evidence without testing it against the base rate. In this panel 893 of 1094 odds ratios exceed 1 and 176 of the 178 significant rows point the same way, so being prognostic is close to universal and an intersection establishes nothing until it is shown to exceed chance.

Letting a claim stand that the answer's own base-rate test removes the support for. An answer that reports the set-level test as null and then asserts that the blocked programme is the programme tracking outcome has contradicted itself.

Using the between-cell-line effect-size difference only to adjust a threshold, and then recommending a model system or a confirmatory study without reference to it. Over the genes attributable at each timepoint in HUVEC, the median absolute logFC is 2.01 in HUVEC against 0.74 in HGMEC at 6 h, a ratio of 2.7, and 2.23 against 0.51 at 24 h, a ratio of 4.4. Neither line is pulmonary, which bears directly on what the next experiment has to be run in.

Concluding that the response does not reproduce across cell lines on the basis of intersecting two threshold-filtered gene sets, where effect sizes in the second line are smaller over the same genes by the ratios above.

Treating the odds ratios for CSF-1, CTSS or BIRC2 as estimated magnitudes when their confidence intervals span orders of magnitude.

Reporting 1094 proteins, or 178 significant proteins, where those figures count assays rather than analytes. The reconciled figures are 1063 and 169.

Nominating soluble ST2 as a pharmacodynamic or target-engagement readout. It is a soluble decoy that competes with the drug for the same ligand, so it does not report signalling through the membrane receptor. Offering it for stratification or enrichment is correct and should not be penalised. Downstream serum markers such as IL6, CXCL10 and CSF3 also track severity and viral clearance in this population, so any pharmacodynamic role for them needs a placebo or concurrent comparator, and an answer that says so is correct.

Assigning soluble ST2 a selection or enrichment role without addressing that its elevation is equally consistent with the ligand already being bound. It is the decoy receptor, so a high level is as compatible with IL-33 having been sequestered as with the pathway being active, and under that reading the patients selected carry the least free ligand. An answer that states this where it assigns the role, or makes it a condition on the proposed gate, has handled it. An answer that enumerates other explanations for the marker and omits this one has not.

Quoting a neutralisation or reversal figure without naming which comparator produced it, or asserting that the isotype arm is inert without restricting that to 6 h. Over the IL-33-induced genes the isotype arm retains 0.99 of the response at 6 h and 0.87 at 24 h, so a 24 h figure measured against the isotype and one measured against IL-33 alone differ, and the direction of the difference is known. Genome-wide the two arms agree at both timepoints, so an answer that validates against a genome-wide null is correct.

Citing SELE, VCAM1, CXCL8 or CXCL1 as part of the blocked response without addressing their standard errors of 8.9, 7.1, 4.1 and 1154.9 against a median of 0.339. An answer that names them and explains why it is not relying on them has handled this correctly, and so has one that retains them on a stated replication argument across independent sample groups.

Stating affinity, potency or exposure values, which are not in the delivered package.

C) NEUTRAL

The following are examples of acceptable variations that should not affect the score. Other variations may also be neutral. Use your judgment.

Whether the recommendation is to keep the asset or to drop it. Either is acceptable where the case is built from the data; the reasoning and the pillars supporting it are what is being graded, not the verdict. A gated hold labelled either way is the same recommendation and should be read on its substance.

Which indication is named, provided it follows from what the data shows the antibody blocks.

The reproducibility criterion chosen and the resulting gene count, provided the criterion is stated and the count follows from it.

How Olink assay identifiers are matched to genes. Exact symbol matching and reconciliation of legacy assay names such as OPG, CSF-1, IL-18R1 and MCP-3 are both defensible and give different shortlists.

Length, ordering, section structure, and where in the answer any particular point appears, including the recommendation.

Whether supporting analysis is presented as tables, prose or figures.

Noting that one endothelial line has no unstimulated baseline arm, that the serum multiplicity correction implies more tests than were delivered, or that the two sheets of the largest workbook hold the same contrasts.
