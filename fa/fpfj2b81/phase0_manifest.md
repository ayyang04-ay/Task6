# Phase 0 — input manifest, task fpfj2b81

Problem `task_c95a3b4fb7e14881853c61756d8086e3`, version `9dbf422a`.
Job `d1def40a-1524-45d8-b77e-6476ae209d12`, 8 attempts, model claude-opus-5-5,
completed 2026-11-06 19:26 UTC.

| Row | Status | Detail |
|---|---|---|
| Run export located | **pass** | 8 attempts, transcripts 1.5-2.7 MB each |
| Export complete | **FAIL** | `export_selection` includes transcripts + grading only. `outputs`, `task_files`, `grader_files` all excluded by the exporter |
| Clusters present | partial | no `_ERROR.txt`; the three missing clusters were deselected, not failed downloads |
| Trajectory IDs | **open** | short ids `c3051d03` ... `d684fc0a` and full UUIDs are in `all_runs.json`. The label form the Hub displays must come from the user, not be constructed |
| Run count and status | **pass** | 8 of 8 completed, 0 refused, no truncation flagged |
| Data room | **workaround** | not in export. Local `data_room/` verified byte-identical to the original Elsevier files on every worksheet property checked. Pushed before the run; problem version matches |
| Grading document | **pass** | writer-authored ABC guidance present in `grading_config.json`. Graded mode available as context only |
| Stats availability | pass | scipy present in this container |
| Thinking channel | **FAIL for one shape** | every thinking block in all 8 transcripts is summary-flagged. 57-83 blocks per run carry text, so there is content, but they are summaries. **No claim about what a run weighed internally is supportable**, which rules out the raised-then-abandoned shape before Phase 1 |
| Deliverable present | **FAIL** | no `outputs/`. `output_files_manifest.json` carries gs:// pointers with `file_count: 0`. Deliverables must be re-exported or rebuilt by replaying each transcript's file operations. Without this there are no citable line numbers |

## Blockers, in order

1. Re-export with `outputs` selected. Everything in Phase 1 that needs a line
   number depends on it.
2. Confirm the trajectory label form as the Hub shows it.
3. Decide whether the panel is FA material at all — see `suitability.md`.

## Not a blocker but worth recording

The job's own `submit_gate` reads: *"ships only if the model does NOT solve it —
mean score must be at or below max_avg_score"*, `max_avg_score: 0.55`, mean
0.415, `clears_gate: true`. The current scoping guidance states the 55% gate
"has been removed from all task-writing worlds". The harness still enforces it.
Which is authoritative is unresolved and matters before relying on either.
