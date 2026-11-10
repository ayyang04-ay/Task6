# v3 FA — error-mode ledger

Job `bbc47ecc` · problem version `304e3f8f` · 8 trajectories. Graded mode available; **used as context only** — no mode below rests on a grader rationale or a score, and runs are not ranked by score.

## Reading coverage

| Trajectory | Coverage | Why selected |
|---|---|---|
| `64b88f15` | deliverable in full + thinking channel | widest candidate spread in the pre-registered screen |
| `22c61ae3` | deliverable in full + thinking channel | longest; carried the IL1RL1 and sST2-as-PD candidates |
| `ab6a5f0f` | deliverable §1–3.2 in full, remainder searched, + thinking channel | largest deliverable; both pre-registered candidates live |
| `3b347103` | §2.1, §3, §4 in full, remainder searched, + thinking channel | surfaced during screening as a confirmed carrier |
| `f3a1dc25`, `e8e62174`, `6f0519bd`, `e7787296` | searched for each named mode; `6f0519bd` thinking channel read | prevalence confirmation |

Selection was by candidate-mode spread and deliverable surface area. Coverage screen: all 8 trajectories read **and** cited all five room files (`mmc2`, `mmc3`, `mmc4`, `mmc5`, annex) — no non-use mode.

## M1 — The run derives an SE-validity filter, then does not apply it to its own gene lists and marker-role assignments

**Class.** Encountered-then-unapplied / raised-then-abandoned (reporting-consistency failure, not a knowledge gap).

**Not checked / measured / corrected for.** Whether every gene carried into a programme list or a biomarker-role row passes the implied-SE validity filter the run itself derived and stated. No run re-applied its own filter to its own downstream lists.

**Requirement basis (prompt, verbatim).** *"All recommendations and/or conclusions should be grounded in our data, as this is what the committee will want to see."* and *"Propose biomarkers, a sampling timepoint and a plan for next steps, and say which of those markers could go into patients and in what role."* The marker-role assignment is a prompt-required deliverable; the basis each run gives for it is contradicted by that run's own SE table.

**[computed] The governing values** (`mmc4.xlsx`, `IL33_vs_Vehicle_HUVEC_6_hrs`, implied SE = |logFC/t|):

| Gene | logFC | adj.P.Val | implied SE | Readable? |
|---|---|---|---|---|
| CXCL2 | +6.768 | 1.67e-28 | 0.367 | yes |
| CXCL3 | +8.279 | 7.80e-33 | 0.390 | yes |
| CXCL5 | +5.301 | 8.02e-21 | 0.388 | yes |
| CXCL6 | +9.406 | 3.41e-15 | 0.871 | yes |
| ICAM1 | +5.966 | 0.00981 | 1.748 | yes (borderline) |
| **CXCL8** | +8.186 | **0.193** | **4.061** | **no** |
| **VCAM1** | +8.739 | **0.511** | **7.064** | **no** |
| **SELE** | +11.209 | **0.498** | **8.866** | **no** |
| **IL1RL1** | +1.602 | **0.980** | **8.324** | **no** |
| **CXCL1** | +8.166 | **0.999** | **1154.884** | **no** |

**Trajectory IDs and evidence.** Site A = programme-content list; Site B = biomarker-role table. Line numbers are approximate for `f3a1dc25`, `6f0519bd` and `ab6a5f0f` (see `phase0_manifest.md`).

| Trajectory | Site | Unflagged at point of claim | The run's own contradicting statement | Thinking-channel trace |
|---|---|---|---|---|
| `64b88f15` | A, line 58 | `CXCL1` inside "CXCL1/2/3/5/6/8" — **and CXCL1 is flagged nowhere in the document**; it is absent from the run's own §6.1 hold-list and §8 affected-gene list | §8 names "standard errors of 2 to 16,536 log2 units" affecting "E-selectin, VCAM-1, IL-8, MCP-1 and PTX3" — CXCL1 omitted | block 11 names the trap itself: *"For a naive analyst, CXCL1 at logFC 8.17 looks like strong IL-33 induction but has t ≈ 0."* block 24 lists CXCL1 as unreliable. block 48 then builds the hold-list **without** CXCL1 |
| `f3a1dc25` | A, line 83 | `CXCL1`, `CXCL8` in "CXCL1/2/3/5/6/8" | line 307 names the 121 high-SE genes including CXCL1 | not read |
| `6f0519bd` | A, line 21 | `CXCL1`, `CXCL8`, `E-selectin`, `VCAM-1` listed as "up" with no caveat | lines 77 and 188: *"implausible standard errors for 130 genes, including SELE, VCAM1, CXCL8, CXCL1, CCL2 and IL1RL1"* | block 42 confirms the 130-gene set. block 45 gives an **explicit reasoned override** for E-selectin only: *"E-selectin also makes the panel despite unreliable in vitro SEs, since its LFC is huge and concordant"* |
| `3b347103` | B, line 192 | `VCAM-1`, `CXCL1` placed in a row whose stated basis is "Strongly IL-33-induced and reversed in vitro", role "In-vitro PD" — while line 191 holds `E-selectin` (SE 8.87) in a separate "in-vitro statistics broken" row | line 48 states "E-selectin and VCAM-1 (+11.2 and +8.7 log2, **statistics broken**)" | block 22 identifies the SE-broken set as "SELE, VCAM1, CXCL1, CXCL8, IL1RL1, PTX3, ESM1, with ICAM1 borderline". block 55 records the intention: *"E-selectin and VCAM-1 have broken statistics, so I'll add a parenthetical flagging that"* — carried into §2.1, not into the marker table |
| `ab6a5f0f` | B, line 298 | `VCAM-1` in "Exploratory PD only", basis "Strongly induced and reversed in vitro" — while line 297 holds `E-selectin` as "contingent on re-analysis ... in vitro statistics unusable (T-1)" | T-1, line 214, computes it: "130 genes exceed 2 log2 units. They include SELE (9.0), **VCAM1 (7.1)**, CCL2 (6.3), CXCL8 (4.1), PTX3 (10.9), IL1RL1 (8.3) and CXCL1 (1,166)" | block 40: *"E-selectin and VCAM-1 are out too because their statistics are unreliable."* block 47: *"...with E-selectin/VCAM-1 pending re-analysis"* — the pair it decided to treat together is split in the final table |

**Why this is not defensible.** Three of the eight — `e8e62174` (line 69), `3b347103` (line 47) and `e7787296` (line 56) — wrote the chemokine list as **"CXCL2/3/5/6"**, excluding both unreadable members. `e7787296` **edited its own draft to make that correction mid-run** (bash call 76: `"CXCL1/2/3/5/6" → "CXCL2/3/5/6"`). So the distinction is one careful readers in this panel drew explicitly. In the Site-B cases the inconsistency is internal to a single table: `VCAM1` (SE 7.064) and `SELE` (SE 8.866) are assigned different readability classes in adjacent rows, and the discriminator the runs use — serum outcome-association — is orthogonal to statistical readability.

`6f0519bd` is the partial exception worth recording: for `E-selectin` it states a reasoned override in block 45. A reasoned override is defensible; what is not is that the override is never surfaced in the deliverable at the point of claim, and is not extended to `CXCL1`/`CXCL8` either way.

**Counterfactual.** Apply the derived SE filter to every gene list and every marker-role row, so that `CXCL1`, `CXCL8`, `SELE`, `VCAM1`, `CCL2`, `PTX3` and `IL1RL1` are handled consistently: either all carried as effect-size-only pending re-analysis (as `e8e62174` and `e7787296` do), or all carried with the caveat attached where the claim is made and the override stated — not split across adjacent rows of one table.

**Consequence.** Changes a prompt-required deliverable in `3b347103` and `ab6a5f0f`: `VCAM-1` (and `CXCL1`) receive an in-vitro PD role on a basis the run's own data contradicts, while the identically-affected `E-selectin` is correctly withheld. In the three Site-A cases the recommendation is unchanged — **benign but real**.

**Graded?** Overlaps grader item A on the chemokine caveat, but the ledger entry rests only on the deliverable text, the room values and the thinking channel.

---

## Pre-registered candidates that did NOT survive

Recorded so they are not re-proposed.

| Candidate | Status | Why it fails |
|---|---|---|
| **A — cites the unusable-statistic genes (E-selectin, VCAM-1, IL-8, CXCL1) without caveat** | **fails as framed** | Every run caveats these genes somewhere, most of them repeatedly. `64b88f15` caveats them at four separate points and holds them out of its biomarker panel. The surviving defect is not "uncaveated citation" but the *inconsistent application* of the run's own filter — M1. Framed as written, the mode would be contradicted by the runs' own text |
| **B — presents the in vitro/serum overlap as a pillar of the keep case while its own enrichment test is null** | **fails** | A null set-level enrichment does not refute individual, NEWS2-adjusted associations, and the prompt asks for biomarkers — for which the individual associations are the relevant evidence. Every carrier states the null enrichment in its own "what our data do not show" section (`64b88f15` §1 and §4; `ab6a5f0f` §1 and item 2; `3b347103` line 89). The grader rationales fault the *ordering* — overlap before the debunk — and ordering is neutral under the grading guidelines. **[computed]** The golden's own position is that the result is signature-dependent (like-for-like OR 2.419, p 0.0169; looser signatures null), so runs reporting p 0.31–0.80 are inside the defensible range |
| **C — proposes sST2 as a PD or target-engagement marker** | **fails** | No run does this. `64b88f15` line 232 explicitly rejects it; `f3a1dc25` line 40, `3b347103` line 189 and `ab6a5f0f` line 344 all assign sST2 to enrichment/stratification and put the endothelial outputs in the PD role |

## Screens run that produced no mode

| Screen | Result |
|---|---|
| Coverage (files read vs cited) | all 8 used all 5 files |
| Prompt's seven asks | all 8 address all seven |
| P2 procoagulant switch stated directionally (F3/SERPINE1 up **with THBD down**) | 5 of 8 have it (`22c61ae3`, `f3a1dc25`, `e8e62174`, `6f0519bd`, `ab6a5f0f`). `64b88f15` and `3b347103` give the up-arm only; `e7787296` omits coagulation. **[inference]** Reporting F3 +5.636 and not THBD −1.001 while summarising a 4,031-gene programme is ordinary prioritisation — an expert defends it, and both runs reached the endothelial-injury indication anyway. Not carried |
| Type-2 effectors absent from the 26,210-gene universe | no run claims in vitro evidence against a type-2 programme; all use serum type-2 markers, which is valid. `f3a1dc25` line 126 states the absence correctly. No error to name |
| Renal clearance as the alternative explanation for sST2 | 4 of 8 silent (`f3a1dc25`, `3b347103`, `6f0519bd`, `ab6a5f0f`). **[computed]** The check is performable: CST3 q 0.337, KIM1 q 0.109–0.241, REN q 0.178 (null — favourable to sST2), LCN2 q 0.0298. **[inference]** sST2 is well known to be less renally dependent than NT-proBNP, so omitting the check is defensible. Not carried |
| Bonferroni / family-wise view (only `ST2` and `HGF` survive) | 0 of 8 mention it. BH is the appropriate correction and is what the room delivers; an expert defends using it. Not carried |
| `df.total` implying one excluded library | only `f3a1dc25` and `ab6a5f0f` found it. Obscure, no consequence for the verdict. Not carried |
| Shared numeric error in load-bearing figures | none found. **[computed]** Spot-audited against the room: 4,031/1,836 DE genes ✓; sST2 OR 3.0243 (1.83–5.01), p 1.685e-5, q 0.00746, rank 2 behind HGF ✓; THBD −1.0005 q 1.72e-10 ✓; F3 +5.6357 t 16.899 ✓; TNF +7.885 → −0.088 ✓; all ten SE values in the M1 table ✓ |
| BH test count | **1,194 is exactly right.** Delivered q / BH-at-1,094 is a constant 0.916248 = 1094/1194 across all 1,094 rows, and the binding step-up ranks imply 1194.00 exactly. The claim in `64b88f15`, `22c61ae3`, `ab6a5f0f` and in the golden is confirmed |

## Gate

**Cleared.** The floor is 2 trajectories holding a single reasoning/reporting error. M1 is held by **five**: `64b88f15`, `f3a1dc25`, `6f0519bd`, `3b347103`, `ab6a5f0f` — four of them with a thinking-channel trace, two of them recording the intention to flag and then not doing it.
