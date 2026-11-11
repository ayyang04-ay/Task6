# v4 FA — error-mode ledger

Job `8d1e3bae` · problem version `b8acb01f` · 8 trajectories, none refused.
Graded mode available; **used as context only.** No mode below rests on a grader
rationale, and runs are not ranked or labelled by score. Three grader defects
were confirmed in the v4 QA and are recorded at the foot of this file: they are
the reason the highest-prevalence apparent pattern is **not** a mode.

## Reading coverage

All eight deliverables read **end to end**. Thinking channel read in full for
`c402acd4` and `bd4f9a92`, and searched by pattern for the rest.

| Trajectory | Deliverable rebuilt | Lines | Words |
|---|---|---|---|
| `af1a3322` | `AX-1177_portfolio_audit_brief.md` | 318 | 4,315 |
| `cc5a3c81` | `AX-1177_portfolio_audit_memo.md` | 421 | 6,115 |
| `920dbc63` | `AX-1177_portfolio_audit_memo.md` | 302 | 4,341 |
| `c402acd4` | `AX-1177_portfolio_audit_brief.md` | 349 | 4,578 |
| `92f09677` | `AX-1177_portfolio_audit_report.md` | 373 | 5,287 |
| `970c71dd` | `AX-1177_portfolio_audit_memo.md` | 322 | 4,510 |
| `dbd6f47e` | `AX-1177_portfolio_audit_report.md` | 274 | 3,935 |
| `bd4f9a92` | `AX-1177_portfolio_audit_memo.md` | 357 | 5,344 |

`outputs/` was excluded from the export for the fourth consecutive time, so all
eight were rebuilt by replaying transcript file operations. **Line numbers are
approximate**; cite section headings. Thinking is raw, not summarised (628 of 641
blocks carry text), so claims about what a run weighed internally are supportable.

---

## M1 — sST2's decoy direction is raised in reasoning and dropped from the deliverable

**Class.** Raised-then-abandoned (verdict-chain gap, not a knowledge gap — both
runs derived the objection).

**Not checked / measured / corrected for.** Whether sST2's elevation is
consistent with IL-33 already being **sequestered** by it. sST2 is the soluble
decoy receptor; a high level is as compatible with IL-33 being mopped up as with
the pathway being active. If it is sequestration, sST2-high patients carry *low*
free IL-33 — the opposite of what enriching on sST2 for an anti-IL-33 antibody
assumes, and a reason the antibody could be redundant in exactly the patients it
would select. This is distinct from the non-specificity objection (sST2 rises
under many stimuli), which both runs do state.

**Requirement basis (prompt, verbatim).** *"I need a strong defensible case to
present, so build out the position with as strong support and defence as the data
allows"* and *"say which of those markers could go into patients and in what
role."* The marker-role assignment is a required deliverable, and sST2 is the
load-bearing human evidence in both runs.

**Trajectory IDs and evidence.**

| | `c402acd4` | `bd4f9a92` |
|---|---|---|
| **[transcript]** raised in thinking | block 36: *"sST2 (OR 3.02, top 2 of 1094) is tempting as an enrichment marker, but since it's a decoy that sequesters IL-33, sST2-high patients may actually have low free IL-33."* Also block 23: *"as a decoy receptor high levels would actually neutralize IL-33 rather than signal more activity"* | block 58: *"First, that IL-33 is actually released and bioactive in these patients, not just that its decoy receptor is up."* Also block 21: *"free serum IL-33 is rapidly oxidized and sequestered by sST2"* |
| **[transcript]** in the deliverable | **absent.** Zero matches for sequester / buffered / mopped / already-neutralised / redundant / equally-consistent. §1 says only that sST2 *"is IL-33's decoy receptor, and stressed tissue releases it under many stimuli"* — the non-specificity framing | **absent.** Zero matches on the same terms |
| **[transcript]** yet recommends | §6.3 biomarker table: sST2 → *"**Yes, first in line: prognostic enrichment / stratification at enrolment.**"* | §3.2 is titled *"The IL-33/ST2 axis is engaged in our target patients and marks those who deteriorate"*; §7 assigns sST2 *"Baseline prognostic enrichment / stratification at enrolment"* |
| **[transcript]** the aggravating detail | — | §3.2 carries a passage headed *"Alternative explanations for sST2 are weak in our own data"* which tests the **cardiac** alternative (NT-proBNP OR 1.20–1.24, troponin I 1.18) and the **renal** one (cystatin C OR 1.39) with data, and omits the decoy-direction one it had raised. Its §4 challenge table answers *"sST2 is a generic severity marker"* the same way. §7 rejects sST2 as a PD marker on a different ground entirely — *"the in-vitro response is small and absent in HGMEC"* |

**Why this is not defensible.** Six trajectories state the objection in the
deliverable, and four convert it into gate design or a kill criterion:

| Trajectory | **[transcript]** where it is addressed |
|---|---|
| `920dbc63` | §3.2: *"High sST2 may itself neutralise IL-33 (it is a decoy), which could make an antibody redundant."* §3.3 makes the bioassay testing it a kill criterion |
| `92f09677` | §2.2: *"sST2 is an endogenous IL-33 decoy. A high value is equally consistent with IL-33 being mopped up."* |
| `dbd6f47e` | §7 ruled-out table: *"High levels are equally consistent with IL-33 being sequestered, so direction must be tested first."* |
| `970c71dd` | §5.2 design note: *"serum sST2 itself sequesters IL-33, so the bioassay must be read together with total IL-33. High total IL-33 with low bioactivity would mean sequestration, which is not a kill by itself"* — protects its own kill criterion |
| `cc5a3c81` | §3.2: *"Because sST2 is a decoy, high sST2 could even mean IL-33 is already buffered. This is exactly why the gate measures free IL-33 and the IL-33:sST2 complex."* |
| `af1a3322` | Gate 1a feasibility caveat: *"reduced IL-33 oxidises (and loses ST2 activity) within hours ex vivo, and sST2 in the sample will buffer it"* |

So the objection is neither obscure nor contested in this panel: it is the
standard reading, and in `bd4f9a92` the omission sits inside a section built to
enumerate alternative explanations.

**Counterfactual.** State, where sST2 is assigned its role, that its elevation is
equally consistent with IL-33 being sequestered, and that this bears on the
enrichment logic specifically: a marker selected for high sST2 may select
patients with least free ligand. Then either test the direction before relying on
it (`920dbc63`, `dbd6f47e`), make it a gate design constraint (`970c71dd`,
`cc5a3c81`), or carry it as a stated caveat on the role assignment.

**Consequence.** Changes a required deliverable in both — the marker-role
assignment — and in `bd4f9a92` also props up the second pillar of the keep case.
Neither run's verdict is wrong on its face; the defect is a missing step in the
chain that reaches it.

**Plain-language restatement (inference check).** sST2 is a sponge for IL-33. If
a patient's sST2 is high, that could mean the IL-33 pathway is roaring, or it
could mean the sponge has already soaked the IL-33 up. These two runs worked that
out while thinking, then recommended selecting patients *by high sST2* for a drug
whose whole job is to soak up IL-33 — without telling the reader that the
selected patients might be the ones with least IL-33 left to soak. Six other runs
told the reader.

**Graded?** `not in grader`. No grading item covers it, so nothing was mis-scored.

### M1b — the same gap at a second site (writer's call whether to merge)

The identical logic recurs in gate design: a banked-serum IL-33 measurement is
made the decisive kill criterion without protecting it against a false negative
from storage plus sequestration. `af1a3322` protects its gate explicitly
(*"confirm it in about 20 rapidly processed fresh plasma samples before invoking
the kill criterion"*); `92f09677` and `970c71dd` protect theirs on other grounds;
`920dbc63` and `dbd6f47e` use conjunctive kill criteria, which protects them
structurally. `c402acd4`'s Gate B terminates or out-licenses on an unprotected
banked-serum result.

**[inference]** This is the same root as M1 applied further down the chain. Report
it as one mode cited at two sites rather than two modes — a reviewer will see the
common root, and counting it twice would overstate prevalence.

---

## M4 — the isotype comparator's timepoint-dependence is not named

**Class.** Convention-not-declared (a named-convention omission, not a wrong
figure).

**Not checked / measured / corrected for.** Whether the isotype arm is inert at
the timepoint being quoted. It is at 6 h and is not at 24 h, so a blanket claim
of inertness is wrong for any 24 h number, and the choice of comparator
(isotype+IL-33 versus IL-33 alone) moves the reversal figure in a known
direction.

**[computed] The governing values** (HUVEC, derived from the delivered contrasts
as `(Compound_47_IL33_vs_IL33_<line>_<tp>) − (Compound_47_IL33_vs_IL33_IC119_<line>_<tp>)`,
over IL-33-induced genes with `adj.P.Val < 0.05`, `logFC > 1` and implied SE < 1.0):

| Selection | n | median difference | fraction of the IL-33 response the isotype retains |
|---|---|---|---|
| 6 h | 639 | −0.0173 log2 | **0.991** — inert |
| 24 h, selected on the 24 h contrast | 313 | −0.3129 log2 | 0.844 |
| 24 h, **selected at 6 h and measured at 24 h** (independent) | 205 | −0.2378 log2 | **0.874** |
| whole gene universe, either timepoint | 26,113 | −0.005 to +0.008 log2 | ~1.00 |

Two cautions that the numbers themselves impose, and that cost me two wrong
readings before I ran the third test:

- The 24 h effect is **partly** winner's curse. Selecting genes on the 24 h
  IL-33 contrast shares the IL-33-alone group with the quantity being measured,
  which inflates it from 0.874 to 0.844. About a quarter of the apparent
  dampening is selection artefact; the rest survives independent selection and
  is real.
- Genome-wide the difference is centred at zero at **both** timepoints, because
  most genes are not IL-33-responsive. A genome-wide null is therefore a valid
  calibration target — `92f09677` uses exactly that and its method is sound.
  The dampening is a property of the induced set, not of the whole file.

**Requirement basis (prompt, verbatim).** *"All recommendations and/or conclusions
should be grounded in our data"* — a reversal percentage is only interpretable
once the comparator and its timepoint behaviour are stated.

**Trajectory IDs and evidence.**

| Trajectory | **[transcript]** the claim | Why it fails |
|---|---|---|
| `af1a3322` | §4.1: *"Reversal is complete for robust genes at both timepoints, and the isotype is inert."* | Asserts inertness **at both timepoints** explicitly. False at 24 h for the induced set, which is the set its own reversal figures are computed on; §2 quotes a 24 h residual of 1% (−10 to +15%) that depends on it |
| `920dbc63` | §2.1: *"The IL-33 + isotype arm reproduced the full IL-33 response (median log2FC 4.12 vs 4.02), so the effect is specific to AX-1177."* | A 6 h figure — the ~2% gap matches the 6 h value — carried as a general claim with no timepoint named |

**Why this is not defensible.** Four trajectories state it, one of them in a
single sentence that is the model answer:

| Trajectory | **[transcript]** how it is handled |
|---|---|
| `c402acd4` | *"**The isotype control is not neutral at 24 h.** The IL-33 + isotype arm keeps 95% of the IL-33-alone response at 6 h but only 86% at 24 h. Any claim of AX-1177 efficacy 'vs IL-33 alone' therefore overstates it. All numbers in this brief use the isotype-matched arm."* — names the convention, quantifies both timepoints, states the direction of the error, declares which it uses |
| `cc5a3c81` | Tabulates both conventions at both timepoints: reversal 95%/98% at 6 h and 73%/84% at 24 h; *"Median IL-33 effect retained with isotype control: 99% / 84%"* |
| `dbd6f47e` | §7: *"Measuring neutralisation against 'IL-33 alone' … inflates reversal (slope −0.82 vs −0.62 against isotype at 6 h). We used isotype as comparator throughout."* Also flags the winner's-curse component separately |
| `bd4f9a92` | Restricts the inertness claim to its timepoint — *"For genes induced >4-fold at 6 h, the isotype has no effect (ratio ≈ 0)"* — and reports the 24 h attenuation (7–20%) separately |

**Counterfactual.** Name the comparator and its timepoint behaviour wherever a
reversal figure is quoted, in one sentence, as `c402acd4` does. Restricting an
inertness claim to 6 h is sufficient; asserting it at both timepoints is not.

**Consequence.** Benign for the verdict — both carriers reach defensible
positions — but it makes their 24 h neutralisation figures uninterpretable as
stated, and `af1a3322` builds a stated claim on a property the data contradicts.

**Plain-language restatement (inference check).** The control antibody really is
doing nothing at 6 hours, so measuring the drug against it is clean. By 24 hours
the control is itself knocking about 13% off the IL-33 response, so "the drug
removed X% compared with control" means something different then. Two runs said
the control does nothing, full stop — one of them explicitly "at both
timepoints" — and then quoted 24-hour numbers resting on it. Four runs said which
comparator they used and what it does at each timepoint.

**Graded?** `not in grader`.

---

## Candidates that cleared the floor but are weak

Recorded with their weakness stated, so the choice to ship or drop them is
deliberate.

| Candidate | Trajectories | Why it is weak |
|---|---|---|
| **Procoagulant switch not stated directionally.** `cc5a3c81` writes *"procoagulant genes: tissue factor (F3, +5.6) and PAI-1 (SERPINE1, +1.7)"* with no anticoagulant arm; `970c71dd` lists F3 +5.6 among inflammatory genes and never characterises the haemostatic module. **[computed]** THBD is −1.0005 at `adj.P.Val` 1.72e-10, implied SE 0.123 — among the best-measured genes in the file | `cc5a3c81`, `970c71dd` | `cc5a3c81`'s statement is true as far as it goes, and `970c71dd`'s is an omission rather than an error. Six trajectories state it directionally, so it does not discriminate. An expert defends both |
| **Assays reported as proteins.** `af1a3322` writes *"#2 of 1,094 proteins"* and *"176 of 178 significant proteins"* with no reconciliation anywhere; `bd4f9a92` writes *"Of 1,094 serum proteins"* and *"82% of all 1,094 proteins"* in its bottom line and scorecard while computing *"27 proteins appear on >1 panel (58 assays)"* in §9. **[computed]** 1,094 assays = 1,063 analytes; the single load-bearing suffix is `-NEUI`, since `GDNF-INFI` and `GDNF-NEUI` are one analyte | `af1a3322`, `bd4f9a92` | Benign: a 2.9% error in a denominator that changes no conclusion. `920dbc63` corrects it explicitly as a ruled-out item. An expert may read "1,094 proteins" as shorthand |

---

## Candidates that did NOT survive

Recorded so they are not re-proposed. The first is the most important entry in
this file.

| Candidate | Apparent reach | Why it fails |
|---|---|---|
| **Failed to cite the in vitro type-2 nulls (IL4, TSLP, CCL26)** | widest of any pattern | **Invalid — the runs were right and the golden was wrong.** **[computed]** IL4 sits at `AveExpr` −4.164 (4th percentile) and TSLP at −3.999 (5th) against a file median of 0.50; a null at that level cannot separate *not induced* from *not detectable*. More decisively, the only IL-33 arms are endothelial monocultures containing no ILC2s, Th2 cells, mast cells or basophils, and A549/MCF7 never received IL-33 — so the system cannot mount a type-2 response at all. The golden's P2 type-2 half has been withdrawn (`b87e643`). The grader penalised the correct reading, and v4 QA verified this by resubmitting one memo with the correct reasoning: it scored identically and was still flagged inconsistent |
| **Asserts an in vitro type-2 negative** (the inverse error, and the real one) | `cc5a3c81` only | Below the floor. `cc5a3c81` §2.1: *"There is no type-2 output. IL-5, IL-13 and eotaxin-1/-2 are not expressed in any arm (removed by the low-expression filter). IL-4, eotaxin-3 and TSLP are unchanged"* — it names the filter and still draws the negative, repeating it in its ruled-out table. Every other trajectory mentions IL-4/TSLP/IL-13 only as *missing serum assays* and places the exclusion on serum and tissue |
| **Reliance on SE-inflated genes** (v3's confirmed mode) | — | **Does not reproduce.** Runs now quantify the inflation and justify retention empirically: `c402acd4` r = −0.998 across disjoint sample groups, `dbd6f47e` r = 0.97, `bd4f9a92` ρ = −0.85, and `92f09677` validates against an empirical null (the isotype-vs-IL-33-alone difference, which should be zero). A disclosed, reasoned override is defensible, and v4 QA flagged the grader for deducting on it anyway |
| **Interferon arm missed from the blocked programme** | 4 on tight patterns | **Dies.** Varied spellings (gene names, set names, prose, Hallmark) show all eight mention it. The complaint is emphasis, not omission |
| **Cross-line effect size not quantified** | 7 on tight patterns | **Dies on requirement-basis.** The grader's own 2.7-fold and 4.4-fold figures name no gene set, contrast or statistic, so there is no stated requirement to breach. v4 QA raised the same point |
| **Divergent verdicts as such** | 2 drop, 6 keep | **Not a mode.** With no causality evidence anywhere in the package, "drop" is defensible; `92f09677` makes termination the default with a recovery gate rather than a flat drop. Divergence located M1 by pointing at the chains, but the endpoint difference is not itself an error |
| **Shared numeric errors** | 0 | **[computed]** Every gene-value claim shared by two or more trajectories matches the 6 h file. No shared wrong figure exists |

---

## Screens run that produced no mode

| Screen | Result |
|---|---|
| Renal clearance as the alternative explanation for sST2 | `c402acd4` and `bd4f9a92` both check it (cystatin C OR 1.39, p 0.18); `bd4f9a92` adds the cardiac check. This was absent in v3 and is now present |
| `AveExpr` misused as a per-cell-line expression filter | `970c71dd` explicitly rejects it — *"AveExpr is pooled across all 114 libraries"* — the foreclosed route, correctly closed |
| Hidden workbook state (AutoFilter, hidden columns, merged cells) | `920dbc63` found the AutoFilter hiding 23 of 24 contrasts plus the hidden serum CI and IHC columns; `bd4f9a92` found the 127 merged cells and the `J12:J13` merge spanning two donors |
| Block-level versus donor-level post-mortem analysis | all eight analyse at donor level and name the pseudo-replication |
| Coverage (files read vs cited) | all eight used all five room files |
| Prompt's seven asks | all eight address all seven |

---

## Grader defects confirmed in v4 QA

Recorded because they explain the apparent prevalence patterns above. **Not being
fixed** — grading is corrected in-house and the FA is what ships.

1. Section A calls the IL4/TSLP/CCL26 nulls *"the type 2 evidence the stimulation
   data actually supports."* Biologically wrong (see the failed-candidate table).
   Seven trajectories were docked for the correct reading.
2. The sentence exempting downstream markers from sST2's recovery confound is
   wrong: serum IL-6, CXCL10 and CSF3 track severity and viral clearance too.
   What is specific to sST2 is that it is a decoy competing with the drug — which
   is the subject of M1.
3. The cross-line figures and the *"24 h is where it does not reproduce"* claim
   carry no gene set, contrast or statistic.

Also: the grader penalises omitting a base-rate enrichment test that the prompt
gives no signal is required.

## Gate

**Cleared.** Four candidates reach the prevalence floor, but they do not all
reach the same standard and should not be presented as equivalent:

| | Mode | Trajectories | Clears the defensibility bar? |
|---|---|---|---|
| M1 | sST2's decoy direction raised then dropped | `c402acd4`, `bd4f9a92` | **Yes.** Six trajectories state the objection, four act on it; one carrier omits it from a section built to enumerate alternatives |
| M4 | Isotype comparator's timepoint-dependence not named | `af1a3322`, `920dbc63` | **Yes.** Computable ground truth; four trajectories state it, one in a single sentence |
| M2 | Procoagulant switch not directional | `cc5a3c81`, `970c71dd` | **Marginal.** `cc5a3c81`'s claim is true as far as it goes and `970c71dd`'s is an omission, not an error |
| M3 | Assays reported as proteins | `af1a3322`, `bd4f9a92` | **Marginal.** A 2.9% denominator error that changes no conclusion; "1,094 proteins" reads as shorthand |

M1 and M4 are the submission. M2 and M3 are available if more volume is wanted,
with the caveat that the defensibility bar is the strictest test in the guidance
and is applied before the prevalence floor.
