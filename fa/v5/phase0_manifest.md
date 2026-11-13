# v5 FA — Phase 0 parse manifest (opus arm)

Job `7abd9695` (exported 2026-11-12) · problem version `dd8c2378` (v5) · model
`claude-opus-5-5` · 8 attempts, 0 refused. **Fable arm not yet received.**

| Row | Status | Detail |
|---|---|---|
| Run export located | pass | one archive, 8 transcripts, grading cluster present |
| Export complete | pass | single `export_selection`; clusters `transcripts, grading` |
| Clusters present | pass | no `task_files/_ERROR.txt` |
| Trajectory IDs | pass | taken verbatim from the export |
| Run count / status | pass | 8/8 completed, none truncated or T&S-blocked |
| Data room | pass | v5 room at `59dc65d` |
| Prompt as the runs saw it | pass, with a known drift | exported prompt differs from the repo in one word only — `defense` against `defence`. Editing is done in Studio; the repo should be aligned so this stops showing as drift |
| Grading document | **the v5 grader reached the run** | problem version `dd8c2378` matches the v5 QA archive. Both items added at `59dc65d` are firing: 7 of 8 rationales discuss the decoy direction or the comparator convention. Used as context only |
| Stats availability | pass | scipy 1.18.1 |
| Thinking channel | pass — raw, not summarised | 645 of 690 blocks carry text (93%). Raised-then-abandoned is in scope |
| Deliverable present | **fail, remedied** | `outputs/` excluded for the **fifth consecutive export** |

## Trajectory index

| Attempt | Trajectory | Deliverable | Rebuilt lines | Rebuilt words |
|---|---|---|---|---|
| 1 | `db52d5f1` | `AX-1177_portfolio_audit_memo.md` | 340 | 4,822 |
| 2 | `b0a42cb1` | `AX-1177_portfolio_audit_memo.md` | 270 | 4,252 |
| 3 | `73a66c65` | `AX-1177_portfolio_audit_memo.md` | 349 | 4,847 |
| 4 | `44d1e489` | `AX-1177_committee_memo.md` | 227 | 3,732 |
| 5 | `03756b16` | **script-generated** — see below | — | 3,140 (prose only) |
| 6 | `708ce744` | `AX-1177_portfolio_audit_memo.md` | 315 | 4,244 |
| 7 | `93d1301d` | `AX-1177_portfolio_audit_memo.md` | 316 | 4,300 |
| 8 | `67b6a053` | `AX-1177_committee_brief.md` | 402 | 6,655 |

## Rebuild method and its limits

Seven rebuilt by `scratch/analysis/replay_v3.py`, unchanged from v4 except that it
now reports and continues where a run writes no Markdown directly, instead of
raising. That crash had stopped the run before attempts 06–08 were reached.

**`03756b16` is a different case and carries a real limitation.** It wrote no `.md`
at all: the memo lives in `/tmp/outputs/code/memo_content.py` as Python string
constants, rendered to Markdown and PDF by `render_memo.py`.
`scratch/analysis/extract_generated.py` replays the edits to that script and emits
its string constants and f-string templates in source order, recovering **3,140
words of prose**.

What that does and does not support:

| | |
|---|---|
| Recoverable | the memo's prose, section order, and every reasoning claim — which is where the sST2 and comparator arguments live |
| **Not recoverable** | its numeric figures. They are injected at render time from pandas intermediates, so `0.339` and `3.02` appear nowhere in the script |
| Consequence | `03756b16`'s reasoning claims can be screened and quoted; **its figures cannot be cited from the rebuild**, and it has no line numbers at all |

Validation of the other seven against the runs' own `grep -n` output: `db52d5f1`
10 of 16 matched, `73a66c65` 6 of 7, `44d1e489` and `b0a42cb1` clean on the
observations available, none with a `wc -w` to check against. Line numbers are
approximate throughout — cite section headings.

## Not yet done

Phase 1 counting is **held until the fable arm arrives.** Prevalence has to be
reported per model as well as per panel: a mode in four fable runs and no opus
runs is a different finding from two of each, and that split is the point of the
16-run design. The floor stays at 2 and is an absolute count, so a mode can clear
it inside one arm.
