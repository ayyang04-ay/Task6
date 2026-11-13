# v5 QA triage

QA chain on problem version `dd8c2378`, completed 2026-11-13T07:59:39Z.
Nine items across six jobs. `env_linter` and `reward_hacking` both returned **no
issues**, so the biologically wrong grader instruction found at v4 is clear.

## Freshness and coverage

| Check | State |
|---|---|
| Chain status | completed |
| `runCount` / `completedRunCount` | 16 / 16 — the version's pool held both arms |
| Jobs starting after the last run was graded (2026-11-12T22:03:16Z) | `env_linter`, `reward_hacking`, `data_quality`, `claudescope`, and one `difficulty` |
| Jobs starting before the panel finished | `problem_linter` (2026-11-12T19:17:32Z) and one `difficulty` (20:56:05Z). Neither cites a run |
| **Model coverage** | **Opus only.** Of 16 run UUIDs, the seven run-citing items name O1, O2, O3, O4, O6, O7, O8 and no Fable run. 21 Opus citations, zero Fable |
| Timing explanation for that | **Ruled out.** ClaudeScope started 2026-11-13T04:19:16Z, after both arms were graded, so all 16 were available to it |
| `findingCount` against `itemCount` | `claudescope` reports 11 findings and 7 items. Four findings did not become items. Reported without explanation |

**[inference]** The export carries no model field, so coverage is read from the
run map. A chain that had all 16 and drew every exemplar from one job is more
consistent with clustering on a single job than with having read both. The Hub's
per-job QA view would settle it; the export cannot.

## Triage

| # | Finding | Runs | Type | Affects golden? | Action |
|---|---|---|---|---|---|
| 0 | `undisclosed_constraints`: the prompt never states a base-rate-test requirement for overlap claims | — | Ambiguity / undisclosed constraint | No | **Sustained, and it cost a mode.** The base-rate retention mode was retired from the ledger, on the golden's own text rather than on this item. No rerun; no prompt change |
| 1 | `minor_grader_penalizes_point_placement_despite_neutral_guidance` | O4 | Grader-only | No | No grader edit. Checked: the golden does not penalise placement. No action |
| 2 | `minor_no_pdf_rasterizer_or_render_engine` | O2, O3, O4, O6, O8 | Tooling | No | Ignore. Noted in the ledger's excluded table |
| 3 | `minor_base_env_missing_common_utilities` | O7 | Tooling | No | Ignore |
| 4 | `minor_data_only_grounding_conflicts_with_needed_external_knowledge` | O1, O2, O8 | Ambiguity | **Checked, no edit needed** | The golden does not rest the withheld-IL-33 finding on vendor panel knowledge. It derives the test count from the delivery itself at `:66-67` — the delivered adjusted p over the BH value at the delivered count is a constant 1094/1194 = 0.916248 across all rows, and the binding step-up ranks imply m = 1194 exactly. `:71` then states only *"IL-33 itself is not among the 1,094."* Derivable from the room as the runs saw it |
| 5 | `minor_committee_deliverable_cannot_be_verified_in_environment` | O4 | Tooling | No | Ignore |
| 6 | `minor_external_knowledge_substituted_for_delivered_data` | O2, O8 | Ambiguity | No | Same derivability check as item 4. The runs' own hedging ("very likely", "external reference") is the correct handling and the golden needs no change |
| 7 | `minor_retained_claims_undercut_by_own_analysis` | O4, O6 | Reasoning issue | No | **Partly not sustained.** O4 puts the null in its own bottom-line table at L15 and L63, so no retention was found there. The pattern is real in other runs, but the mode built on it was retired on the golden's text (item 0 and the golden quote in the ledger) |
| 8 | `AX-1177 anti-IL-33 audit: grader guidance contradicts itself on penalising soluble ST2 for enrichment` | — | Grader-only | **Yes — golden revised** | See below |

## Item 8 — the finding is wrong, the check it triggered was not

QA reads two adjacent `PENALIZE FOR` items as contradictory: one says offering
sST2 for stratification or enrichment is correct and should not be penalised, the
next penalises assigning it that role without addressing the sequestration
direction. **[inference]** These are consistent — the role is correct and must
carry the caveat — so the contradiction is an adjacency problem in the grader,
not a logical one, and no grader edit follows.

The check it prompted did find a real defect. The golden granted sST2 a selection
role and nowhere stated the decoy direction, so the reference solution committed
the omission the ledger's M1 penalises eight runs for.

### Golden edit, 2026-11-13

**Derivability check: passes.** The golden already asserts in the same row that
soluble ST2 is the decoy receptor for the drug's own target. The absence of a
ligand measurement is established in the room — `AX-1177_serum_proteomics`
contains no IL-33 assay string and no free, total or complexed measurement — and
the golden states it at `:71`. No fact outside the room is needed, so this is a
golden fix and not a room defect. No rerun.

**Edit A — `reviewer_data/golden_response_v2.md`, section 5 role line.**

| | |
|---|---|
| Original | `**sST2 is a stratification marker, not a pharmacodynamic one** — see section 6.` |
| Words changed | after `one**`, inserted `, and because it is the decoy receptor its elevation is as consistent with IL-33 having already been bound as with the pathway being active` |
| Why | The role is stated here, so the condition on it belongs here. M1's counterfactual requires the caveat where the role is assigned |

**Edit B — same file, section 6 ruled-out row.**

| | |
|---|---|
| Original | `Prognostic and for patient selection: yes, on the Bonferroni result. Target engagement or pharmacodynamics: not shown, and not resolvable here.` |
| Words changed | after `Bonferroni result`, inserted `, with the direction stated as a condition on that use`, then four sentences giving the decoy direction, the consequence for an enriched cohort, the absence of any IL-33 measurement, and the two acceptable handlings |
| Why | This row grants the selection role with reasoning and was the only place the decoy receptor was discussed. It discussed only the pharmacodynamic confound |

**Checked after the edit.** `scratch/analysis/verify_golden_v2.py` passes every
row. `reviewer_data/v2_pillars.md` grants sST2 no selection role — `:112` and
`:141` state only that it is prognostic — so it needs no matching change.

**Ledger items re-checked:** M1's counterfactual now has golden backing and is
final. M2 and M3 are untouched by this edit.
