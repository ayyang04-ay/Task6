# Is this panel FA material?

Short answer: **partly, and not as it stands.** The largest single driver of
the score spread is a task defect rather than a model failure, and three of the
six pre-registered modes need work before any of them can be counted.

## The fairness problem is real and it is structural

The grading guidance item A1 reads: *"A one-line recommendation at the top that
distinguishes the 6 h result from the 24 h result."* The prompt says only:
*"Build me the proposal, opening with your recommendation in one line at the
top."*

The env linter graded a controlled pair: identical bodies, saved analysis and
forward plan, differing only in the top line. The one naming the timepoint
result scored 0.85; the one opening "CONDITIONAL GO" scored 0.60. All 8 real
runs were marked A1 not met, including the highest at 0.55, whose top line is
"Recommendation: NOT YET ... fund a 12-month, three-gate de-risking plan".

This is not only unfair by the expert-understanding test. It breaks two rules
in the current guidance:

- **Standing authoring rule 4**: "A go/no-go verdict is an acceptable
  deliverable shape. **What gets graded is the pillars and the justification
  supporting the choice, not the verdict itself.**" A1 grades the wording of the
  verdict line.
- **Stage 4 grader derivation**: section A comes from the route-necessary legs.
  Placement of a sentence is not a leg, so A1 is malformed by construction
  rather than merely strict.

Consequence for the FA: every run lost the same fixed share of score for
something that is not a method failure. A run that separates the timepoints in
the body and opens with a decision line has made no error a careful expert
would recognise, so it fails the defensibility bar. That share of the spread
carries no FA signal.

## Two more places the prompt does not ask for what is scored

**The forward plan has no criterion and conflicts with the grounding line.**
The prompt asks what to measure, in which model, when, and what goes into the
clinic. The package holds no in vivo, PK, tox or clinical-design data. The
prompt also says all figures, findings and conclusions must be grounded in the
mounted files. The deliverable is therefore unanswerable as specified, and the
QA records that every rollout invented a labelling scheme to reconcile the two.
No A item covers the forward plan at all.

This was predicted. When the grounding sentence was tightened and "Domain
knowledge is welcome in interpretation" was dropped, the risk flagged was that
the stricter line forbids the external knowledge the forward plan needs. The
QA found it independently. The fix is to restore a clause permitting labelled
domain knowledge.

**The circulating-marker shortlist** appears in section C as a neutral
variation but is required by no A item and asked for by no prompt sentence
until "what goes into the clinic", which does not name analytes.

## Three of the six modes need work

| Mode | Status |
|---|---|
| `threshold-intersection` | **unknown prevalence.** The QA reports rollouts converging on the same recommendation, and one QA rollout reporting 951 concordant genes at r 0.57. 951 is the sign-plus-adjusted-p cell at the adj.P-only base in the criterion grid, so that rollout took a correct route. Whether any run intersected thresholded sets has to be read, not assumed |
| `both-windows-rejection` | **unknown prevalence**, and partly protected: the prompt's earlier wording presupposed a timepoint carries. That wording was removed before this run, so the mode is live, but it needs counting |
| `assay-as-analyte` | **refuting fact is wrong.** See below |
| `prognostic-as-pharmacodynamic` | plausible; needs counting. The QA notes graders may penalise sST2 offered for stratification, which would be unfair — only the pharmacodynamic claim is the error |
| `magnitude-ranked-response` | **dead.** See below |
| mmc5 sheet duplication | **stronger than recorded**, and needs counting. See below |

### `assay-as-analyte`: the reference number is wrong

A data-derived suffix rule over `mmc2.xlsx` gives 28 analyte groups. One,
`TR-AP` / `TR`, is spurious — TR-AP is tartrate-resistant acid phosphatase, not
`TR` with a panel suffix. That leaves **27 groups, 58 assays, 31 extras, 1063
unique analytes**, which is what the env linter computed and what two graders
reached independently.

The figure 1064 came from a hand-built suffix list that omitted `NEUI`, so
`GDNF-INFI` / `GDNF-NEUI` was never merged. 1064 is in the grader document as a
stated fact and in the golden. Both need correcting to 1063. Significant
analytes remain 169 under either rule.

### `magnitude-ranked-response`: the mode penalises better analysis than the golden

The mode rests on SELE, VCAM1 and CXCL8 being non-attributable at adj.P 0.4950,
0.4965 and 0.1772. Implied standard errors, `|logFC / t|` in
`Compound_47_IL33_vs_IL33_NIP228_HUVEC_6hrs`:

| gene | logFC | t | implied SE | vs median |
|---|---|---|---|---|
| CSF2 | −12.2128 | −31.1112 | 0.393 | 1.2x |
| CCL20 | −9.8418 | −13.3856 | 0.735 | 2.2x |
| ICAM1 | −5.9116 | −3.3900 | 1.744 | 5.1x |
| CXCL8 | −8.4467 | −2.0554 | 4.110 | 12.1x |
| VCAM1 | −8.7623 | −1.2484 | 7.019 | **20.6x** |
| SELE | −10.9852 | −1.2513 | 8.779 | **25.8x** |

Median implied SE across all 26,210 genes is 0.3404. SELE's fold change is
comparable to CSF2's and its standard error is 22 times larger. The extreme tail
is worse: CD93 carries `t` of exactly 0 against a non-zero logFC, implying SE
16,535; CXCL1 logFC −8.0443 with `t` −0.0071 implies SE 1,137.

So SELE's adjusted p value is driven by a pathological variance estimate, not by
a small effect. A run that notices this, calibrates against null contrasts and
relies on the fold change has done **better** analysis than the golden, which
took adj.P 0.4950 at face value. Under the FA bar — if a careful expert could
defend the choice, it is not a failure mode — this cannot be a mode, and the
B item penalising it is penalising correct work.

The golden's claim "None is attributable" needs qualifying to the delivered
statistics rather than stated as fact.

### mmc5 sheets: the hazard is larger than recorded, and it is authentic

The mode was written around two duplicate sheets and 419,535 padding rows. The
files carry more than that:

| File | Property |
|---|---|
| `mmc5.xlsx` | active AutoFilter over `A1:K629041` with **602,830 hidden rows per sheet**. 629,040 − 602,830 = 26,210 visible, exactly one contrast of 24 |
| `mmc2.xlsx` | AutoFilter, 2 hidden rows, and columns 4-5 hidden — `l95` and `u95`, the confidence intervals |
| `mmc3.xlsx` | 12 hidden columns, 127 merged cells, one live formula cell `(2+4.5)/2` |

None of this was in the data-room inventory reported earlier. pandas and
openpyxl ignore AutoFilter and hidden state, which is why a dozen profiling
passes never surfaced it. The inventory was wrong and the correction is above.

**But it is authentic.** Every one of these properties is byte-identical between
the original Elsevier supplementary files and the mounted copies — mmc5's
original carries 1,205,660 hidden rows across its two sheets. Nothing was
planted.

## Where the QA is wrong

`minor_contrived_density_of_planted_data_traps` calls the task "a scavenger
hunt" and lists the hidden sheets, the AutoFilter, the stale row dimension, the
hidden columns, the merged cell and the formula cell as "planted integrity
defects that resemble puzzle construction more than real-world data
messiness."

Every artifact in that list is in the published source, unmodified. Standing
authoring rule 3 requires exactly this: *"Assume the source data is clean and
that the original researchers acted unbiased. Source inconsistencies are
reproduced verbatim and unremarked; parsing human error is a legitimate task
constraint."*

So the finding criticises compliance with a standing rule, on an inferred
authorship the files refute. It is the finding most likely to get the task
rejected on contrivance grounds and it rests on a false premise. The underlying
observation — that score may track which artifacts a run happened to find — is
worth taking seriously on its own terms, but it is a different argument and does
not need the planting claim.

Two other QA findings infer rather than check: `package_not_complete_despite
_authoritative_framing` treats an annex stating that count matrices are not part
of the delivery as a defect, where a real data package says exactly that; and
its claim that "about 100 analysed Olink assays were withheld" is not verified
here either way.

## What would make this panel usable

1. Fix A1, in the guidance not the prompt. The env linter's own wording works:
   judge the 6 h / 24 h distinction wherever it appears in the proposal.
2. Correct 1064 to 1063 in the guidance and the golden.
3. Cut the SELE/VCAM1 penalty, or narrow it to claims made without addressing
   the delivered standard errors. Qualify the golden's claim.
4. Narrow the adhesion penalty so it cannot catch ICAM1, whose HUVEC 6 h
   reversal is significant at adj.P 0.0102.
5. Restore a clause permitting labelled domain knowledge, so the forward-plan
   deliverable is answerable.
6. Add an A item for the forward plan, or drop the ask from the prompt.
7. Re-export with `outputs` selected.

Items 1 to 6 are a new problem version and a new run. The current 8 transcripts
would then be a pilot rather than the FA panel.
