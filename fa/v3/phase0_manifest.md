# v3 FA — Phase 0 parse manifest

Job `bbc47ecc` (exported 2026-11-09) · problem version `304e3f8f-1753-4f82-898a-abd28d7654cd` · model `claude-opus-5-5` · 8 attempts, 0 refused.

| Row | Status | Detail |
|---|---|---|
| Run export located | pass | single archive, `Anton_c95a3b4fb7e14881853c61756d8086e3_job_bbc47ecc_2026-11-09` |
| Export complete | pass | one `export_selection`; clusters `transcripts, grading` |
| Clusters present | pass | no `task_files/_ERROR.txt` |
| Trajectory IDs | pass | taken verbatim from the export run index |
| Run count / status | pass | 8/8 completed; none truncated, errored or T&S-blocked |
| Data room | pass | exported `task_prompt.md` byte-identical to repo `task_prompt.txt`; room = v3 room at `58442ab` |
| Grading document | present (writer-authored) | graded mode available; used as **context only** — no mode may rest on it, runs not ranked by score |
| Stats availability | pass | scipy 1.18.1 |
| Thinking channel | pass — raw, not summarised | 622 / 638 blocks carry text (97%). Raised-then-abandoned IS in scope |
| Deliverable present | **fail, remedied** | `outputs/` excluded by the exporter's selection (`file_count: 0` for all 8). Rebuilt by replaying transcript file operations |

## Trajectory index

| Attempt | Trajectory ID | Deliverable written | Rebuilt lines | Rebuilt words |
|---|---|---|---|---|
| 1 | `64b88f15` | `AX-1177_portfolio_audit_memo.md` | 310 | 4,473 |
| 2 | `22c61ae3` | `AX-1177_portfolio_audit_memo.md` | 299 | 5,131 |
| 3 | `f3a1dc25` | `AX-1177_portfolio_position.md` | 357 | 4,932 |
| 4 | `e8e62174` | `AX-1177_portfolio_audit_recommendation.md` | 329 | 5,085 |
| 5 | `3b347103` | `AX-1177_portfolio_audit_report.md` | 334 | 3,957 |
| 6 | `6f0519bd` | `AX-1177_portfolio_audit_memo.md` | 224 | 4,241 |
| 7 | `e7787296` | `AX-1177_portfolio_audit_memo.md` | 278 | 3,091 |
| 8 | `ab6a5f0f` | `AX-1177_portfolio_audit_report.md` | 403 | 5,444 |

All 8 wrote a Markdown deliverable unprompted; the v3 prompt neither asks for nor forbids a format. 2 of 8 also rendered a PDF (`22c61ae3`, `e8e62174`), 2 an HTML (`f3a1dc25`, `ab6a5f0f`).

## Rebuild method and validation

`scratch/analysis/replay_v3.py` replays, in order: editor `create` / `str_replace` / `insert`, `sed -i` substitutions, `>>` heredoc appends, and the in-transcript Python find-replace blocks. The Python blocks required four corrections before the rebuilds validated:

| Replay bug | Effect if uncorrected |
|---|---|
| `rep` given as a **dict** (`{old: new}`), not a list of tuples | `f3a1dc25` lost 15 edits |
| `b = a + """…"""` — replacement built by **concatenation**, an AST BinOp not a Constant | `22c61ae3` short by 264 words (its whole evidence scorecard) |
| `s.replace(old, new, 1)` passing **variable names**, not literals | `64b88f15` short by 57 words |
| A block guarded by `assert` that **raised wrote nothing**, but a traceback from a *later* command in the same bash call does not undo an unguarded write | `ab6a5f0f` double-applied one edit set (+242 words); `e7787296` and `6f0519bd` lost a block each |

Validation, `scratch/analysis/validate_v3.py`, against two independent in-transcript observations:

| Trajectory | `wc -w` the run itself printed | Rebuilt | Line-number observations matched |
|---|---|---|---|
| `64b88f15` | 4,464 (final) | 4,473 (+0.2%) | 1 obs, from a figure script not the memo |
| `22c61ae3` | 5,102 (final) | 5,131 (+0.6%) | 15 / 15 |
| `f3a1dc25` | — | — | 12 / 16 |
| `e8e62174` | — | — | whitespace-only diff on the 1 obs |
| `3b347103` | — | — | no mismatches |
| `6f0519bd` | — | — | 6 / 9 |
| `e7787296` | — | — | 5 / 5 |
| `ab6a5f0f` | 5,088 at call 99, **10 further edits followed** | 5,444 (+356, expected) | 11 / 15 |

Every unmatched observation resolves to one of: an observation of a *pre-edit* version of a line the run later changed; an en-dash mangled by `grep` under a non-UTF-8 locale; a whitespace-only difference; or an observation of a different file.

**Carry-forward limitation.** Text is accurate at final state for all 8. **Line numbers are reliable for `64b88f15`, `22c61ae3`, `3b347103`, `e7787296`, and approximate (±a few lines) for `f3a1dc25`, `e8e62174`, `6f0519bd`, `ab6a5f0f`**, which applied late whole-file reformatting or table restructuring. Where a mode is traced in those four, cite the section heading, not the line.
