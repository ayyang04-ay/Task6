# v2 panel — shared errors, located

Job `f8f80815`, 8 runs, 2026-11-09. Deliverables rebuilt from transcript file
operations because `outputs/` was excluded from the export again; line numbers
are into `fa/v2/rebuilt/<run>_deliverable.md`.

Thinking blocks in all 8 transcripts are summaries, so no claim about internal
reasoning is supportable.

**Naming a failure mode is the writer's call. Below is what the runs did, where,
and how many share it.**

---

## A. Declares a gene's statistics uninterpretable, then relies on that gene

**Three runs, all confirmed by reading the matched text.** An earlier version of
this file claimed six, on the strength of grader rationales. That was wrong and
three of those six do not hold — see "Checked and does not hold" below.

| Run | Says the statistics are unusable | Then uses the gene anyway |
|---|---|---|
| `74fbe7af` | line 347: "73 large endothelial effects have implausible standard errors: E-selectin log2FC 11.2 but t = 1.26; CXCL1 standard error ≈ 1,150 log2 units" | line 230: PD panel = "CCL20, OPG, IL-8, **sE-selectin**, G-CSF, **CXCL1**, CXCL5, CXCL6, fractalkine, sVCAM-1, sICAM-1" |
| `9ff88a09` | line 123: "Key endothelial genes have implied standard errors in the top 0.5%: E-selectin 8.9, CXCL1 1,155, vs a median of 0.34" | line 208: "**sE-selectin** … +11.2 with IL-33, −11.0 with AX-1177 (HUVEC), −8.7 in HGMEC … **PD** of endothelial IL-33 blockade" |
| `8284fdf0` | flags the inflated errors and reads them as "false negatives" | line 117: "**Tissue factor, sE-selectin** — Early endothelial PD (exploratory)"; line 61 puts IL-8 in the PD panel |

A fourth, `b61bb2b9`, names CXCL1 and CXCL8 in a parenthetical chemokine list
at line 66 while listing both as SE-affected at line 240. Weaker in form than
the three above — a gene list rather than a nominated readout — so it is
recorded and not counted.

**Why it is not defensible.** The contradiction is inside one document. A run
that states E-selectin's standard error is 8.9 against a median of 0.34, and
that the delivered non-significance is therefore an artefact, cannot then
nominate sE-selectin as a pharmacodynamic readout on the strength of "+11.2
with IL-33, −11.0 with AX-1177" — those are the same numbers whose variance it
has just declared unusable.

**What was available instead.** SELE 8.866, VCAM1 7.064, CXCL8 4.061 and CXCL1
1154.884 against a file median of 0.339. Twenty-three genes carry standard
errors under three times the median: the interferon set, CXCL2/3/5/6, CSF2,
CSF3, TNF, IL6, IL1B, and F3, SERPINE1, THBD and C3.

---

## B. Runs the base-rate test, records a null, then argues from the overlap

**Three runs, all confirmed in text.**

| Run | Records the null | Then relies on the overlap |
|---|---|---|
| `74fbe7af` | line 110: "All 99 endothelial IL-33-response proteins measured \| 17% \| vs 17% background; **Fisher OR 0.99, p = 1.0**"; line 325 rules out reading the serum signature as an IL-33 signature on it | line 231: "CCL20, OPG \| **Mechanism-linked** prognostic and PD candidates … The only markers that are both clean IL-33 responders in vitro and prognostic" |
| `29df470b` | line 98: "17 of 98 IL-33-induced, AX-1177-reversed proteins are prognostic (17%), against 141 of 792 non-regulated proteins (18%). **Fisher OR 1.03, p = 1.0**" | line 117, answering "You have no human evidence that IL-33 matters": "The **indirect evidence points the right way**" |
| `204e2bf4` | grader records Fisher p 0.75 and 0.11 and the report stating "not an enrichment" | line 72 "**Bridging proteins.** Eight IL-33-inducible, AX-1177-reversible endothelial genes have serum proteins that are also prognostic"; line 207 retains the indication hypothesis on "sST2 and bridging proteins prognostic" |

**Why it is not defensible.** A null on that test says co-membership of the two
lists carries no information about outcome. `74fbe7af` then qualifies CCL20 and
OPG as "mechanism-linked" precisely because they sit in both lists. The
measurement and the inference contradict each other in the same document.

**Reference figures.** On the tight 315-gene core the enrichment is real — 13
of 38 against 129 of 729, Fisher OR 2.419, p 0.0169 — and null on looser
signatures. So these runs were not wrong about their own signatures. The error
is arguing from the overlap after recording the null, not the null itself.

---

## C. Quantifies the between-line difference, then recommends a model without it

Six runs, from the grader rationales, not confirmed in text. `204e2bf4`,
`74fbe7af`, `8284fdf0`, `70ed96fe`, `29df470b` and `9ff88a09` all recommend
primary lung microvascular endothelium and none ties it to the size of the gap.
`74fbe7af` reports "~80% of the HUVEC magnitude" computed over genes
significant in both lines, which is selection-biased; the HUVEC-responsive set
gives about 2.7-fold at 6 h and 4.4-fold at 24 h.

Weakest of the three: an omission rather than a self-contradiction, and the QA
flagged requiring this specific ratio as a detail the open-ended prompt does
not request.

---

## Checked and does not hold

Three runs the grader rationales put under A are not instances of it.

| Run | Why not |
|---|---|
| `70ed96fe` | Handled it correctly. Line 194 assigns E-selectin, VCAM-1, ICAM-1, IL-8 and MCP-1 "Large in vitro point estimates, but uninterpretable statistics" and a role of "**None until the counts are re-analysed**", with "No" under taking them into patients. Its only slip is listing ICAM1 (6.0) in a summary table, and ICAM1's SE of 1.748 is 5.2x the median — borderline rather than unreadable. |
| `29df470b` | Handled it correctly. Line 204 gives sST2 "+1.6 / −1.7 (**p-value unusable**)" and the role "Enrichment/stratifier at enrolment. **Not PD, not target engagement.**" Line 152 schedules statistical confirmation of SELE, VCAM1, CXCL8, PTX3 and IL1RL1. |
| `b61bb2b9` | Over-flagged rather than under-flagged. Its stated plausibility window is 0.01–3 log2 units (line 456), applied across contrasts, which catches SERPINE1 at line 240 although SERPINE1's SE at 6 h is 0.112 — 0.3x the median and among the best-measured genes in the file. |

## Not candidates

| | |
|---|---|
| **GATA3 omitted** — 7 of 8 | They were right to omit it. Implied SE 22.891 against a median of 0.339 makes it unreadable, and the v2 grader wrongly required it. Corrected in `b515bba`. |
| The verdict | Runs split between gated-keep and drop; the grader makes the verdict neutral by design and both are argued from the data. |
| Tooling gaps | No pandoc, LaTeX, poppler or PyMuPDF in the image. Every run worked around them and no analytical result was affected. Difficulty may not live here. |
