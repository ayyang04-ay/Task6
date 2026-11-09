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

Six runs. Confirmed by reading the matched text in three; the other three rest
on the grader rationale and should be confirmed before they are counted.

**Directly confirmed:**

| Run | Says the statistics are unusable | Then uses the gene anyway |
|---|---|---|
| `74fbe7af` | line 347: "73 large endothelial effects have implausible standard errors: E-selectin log2FC 11.2 but t = 1.26; CXCL1 standard error ≈ 1,150 log2 units" | line 230: PD panel = "CCL20, OPG, IL-8, **sE-selectin**, G-CSF, **CXCL1**, CXCL5, CXCL6, fractalkine, sVCAM-1, sICAM-1" |
| `9ff88a09` | line 123: "Key endothelial genes have implied standard errors in the top 0.5%: E-selectin 8.9, CXCL1 1,155, vs a median of 0.34" | line 208: "**sE-selectin** … +11.2 with IL-33, −11.0 with AX-1177 (HUVEC), −8.7 in HGMEC … **PD** of endothelial IL-33 blockade" |
| `8284fdf0` | flags the inflated errors, then reads them as "false negatives" | line 117: "**Tissue factor, sE-selectin** — Early endothelial PD (exploratory)"; line 61 puts IL-8 in the PD panel |

**From the grader rationale, not yet confirmed in text:** `b61bb2b9`
("CXCL1/8 and PAI-1 still appear in the description of the programme after
being flagged as SE-artefact genes"), `70ed96fe` ("ICAM1 appears among the
'most robust effects' although its standard error is flagged elsewhere"),
`29df470b` ("IL1RL1 (SE 8.3) is counted as induced and reversed, although its
p-value is flagged as unusable").

**Why it is not defensible.** The contradiction is inside one document. A run
that states E-selectin's standard error is 8.9 against a median of 0.34, and
that the delivered non-significance is therefore an artefact, cannot then
nominate sE-selectin as a pharmacodynamic readout on the strength of "+11.2
with IL-33, −11.0 with AX-1177" — those are the same numbers whose variance it
has just declared unusable. Either the estimate can be read or it cannot.

**What the data supports instead.** The four genes are SELE 8.866, VCAM1 7.064,
CXCL8 4.061 and CXCL1 1154.884, against a file median of 0.339. Twenty-three
genes carry standard errors under three times the median and are available for
exactly this purpose: the interferon set, CXCL2/3/5/6, CSF2, CSF3, TNF, IL6,
IL1B, and F3, SERPINE1, THBD and C3.

---

## B. Runs the base-rate test, gets a null, then relies on the overlap anyway

Three runs, from the grader rationales; not yet confirmed in text.

- `204e2bf4`: "the 'bridging proteins' are still used as support for the working
  hypothesis even though enrichment was null"
- `74fbe7af`: "CCL20 and OPG are put forward as 'mechanism-linked' markers
  because they sit in both lists, even though the enrichment test was null"
- `29df470b`: "the 17-protein overlap is called 'indirect evidence' in the case
  for keeping the asset and in the rebuttal table, despite the report's own
  null enrichment test"

Same shape as A: the run performs the correct check, records the answer, and
then argues from the thing the check failed to support.

Note on the reference figures: on the tight 315-gene core the enrichment is
real — 13 of 38 against 129 of 729, Fisher OR 2.419, p 0.0169 — but it is null
on looser signatures. So a run whose own test returned null was not wrong about
its own signature. The error is relying on the overlap after that result, not
the result itself.

---

## C. Quantifies the between-line difference, then recommends a model without it

Six runs, from the grader rationales.

`204e2bf4`, `74fbe7af`, `8284fdf0`, `70ed96fe`, `29df470b`, `9ff88a09` all
recommend primary lung microvascular endothelium and none ties it to the size
of the gap between the two delivered lines. Several also report the gap only at
6 h, or compute it over genes significant in both lines, which is selection-
biased — `74fbe7af` reports "~80% of the HUVEC magnitude" on that basis where
the HUVEC-responsive set gives about 2.7-fold at 6 h and 4.4-fold at 24 h.

Weaker than A and B: this is an omission rather than a self-contradiction, and
the prompt asks for a grounded recommendation rather than for this specific
ratio. It clears the two-run floor comfortably but it is the one a reviewer
would push on.

---

## Not candidates

| | |
|---|---|
| **GATA3 omitted** — 7 of 8 | They were right to omit it. Implied SE 22.891 against a median of 0.339 makes it unreadable, and the v2 grader wrongly required it. Corrected in `b515bba`. |
| The verdict | Runs split between gated-keep and drop; the grader makes the verdict neutral by design and both are argued from the data. |
| Tooling gaps | No pandoc, LaTeX, poppler or PyMuPDF in the image. Every run worked around them and no analytical result was affected. Difficulty may not live here. |
