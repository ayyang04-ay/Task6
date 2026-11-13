# v5 FA — error-mode ledger

Version 2 (2026-11-13). Change note: M2 replaced. The base-rate retention mode
is retired to "Excluded candidates" because the golden absolves it; the
interferon-arm omission takes its place. M1 and M3 unchanged.

Version 1 (2026-11-13). First v5 ledger.

Problem version `dd8c2378`. Two jobs, one version: Opus `7abd9695`
(`claude-opus-5-5`) and Fable `bad3b5d0` (`claude-fable-5-2`). 16 runs, none
refused, none truncated, none blocked by Trust & Safety.

Graded mode available; **used as context only.** No mode below rests on a grader
rationale. Runs are not ranked or labelled by score, and no score appears in this
file. Three grader rationale claims were checked and **not** sustained; they are
recorded under "Excluded candidates" with the reason.

## Run map

| Label | Short | UUID | Label | Short | UUID |
|---|---|---|---|---|---|
| Opus O1 | `db52d5f1` | db52d5f1-e183-40c6-89a7-c81c7d695888 | Fable F1 | `0f940787` | 0f940787-d3e3-4602-b6ad-29b84653388c |
| Opus O2 | `b0a42cb1` | b0a42cb1-7891-4e12-9395-e88de1d193b8 | Fable F2 | `5abe6ebf` | 5abe6ebf-008f-4ba5-9f82-10a2446f3a3c |
| Opus O3 | `73a66c65` | 73a66c65-58dc-489c-9b8a-98ed905d050b | Fable F3 | `bb669dca` | bb669dca-3c82-440f-bbc0-fd08d59b74a2 |
| Opus O4 | `44d1e489` | 44d1e489-a186-42b7-9c02-95b5bb424f71 | Fable F4 | `e3a689b2` | e3a689b2-a71c-4236-96ff-88e2c01048eb |
| Opus O5 | `03756b16` | 03756b16-4051-4968-946b-ffec1c5b62ea | Fable F5 | `0ed1841e` | 0ed1841e-1251-4f5b-a4ed-8423fd8827b5 |
| Opus O6 | `708ce744` | 708ce744-d2d5-4d95-bb72-04f1fe701251 | Fable F6 | `7469f3ac` | 7469f3ac-4f8e-4a1b-a1bc-c68f46ad0e68 |
| Opus O7 | `93d1301d` | 93d1301d-acc9-4108-904f-122ac0260607 | Fable F7 | `feca40ba` | feca40ba-f12b-42a2-8378-657d374cc6ac |
| Opus O8 | `67b6a053` | 67b6a053-006f-4a90-a1f9-24c6c8384382 | Fable F8 | `d0b95a32` | d0b95a32-92ff-4c41-bbf9-67128a76689e |

Attempt numbers are the export's own (`attempt_NN_<short>`), not constructed.

## Reading coverage

| Item | State |
|---|---|
| Deliverables | All 16 located in `outputs/`; every run has a markdown primary. Line numbers in this file are from those files and are exact |
| Read in full | O8, F1, F3, F6 (selected on visible errors, two per model) |
| Screened per mode | All 16, every mode, deliverable text |
| Transcripts consulted | F3, F6 (base-rate computation), O1/O2 (base-rate figure), v4 `c402acd4` (thinking-channel provenance) |
| Thinking channel | **Summaries, not raw.** Every `Thinking` block carries `metadata.thinking_summary`; blocks with `status: ok` hold text and blocks with `failed/rejected` or `skipped/char_cap` are empty, with no exceptions across 2,462 blocks in v4 and v5. Raw thinking is in no export |
| Thinking coverage asymmetry | Fable has 369 `skipped/char_cap` blocks against Opus's 32. Fable's longest reasoning blocks are the ones with no record, so any trace-based mode will under-count in Fable for export reasons |
| Consequence | **No mode below makes a claim about what a run weighed internally.** The raised-then-abandoned shape is unavailable on this panel |

Correction to the v4 ledger: its line *"Thinking is raw, not summarised (628 of
641 blocks carry text)"* is wrong. The text rate is the summarisation success
rate. v4 M1 quoted `c402acd4` blocks 36 and 23 as the run's own words; those
strings are verbatim in the export at those positions, but they are the
summariser's rendering.

## Verdict map (1a2)

| Run | Keep / drop | Indication | Gating marker | Divergence point |
|---|---|---|---|---|
| O1 | Keep, re-scoped, gated | endothelial IL-33 activation, sST2-high | sST2 | — |
| O2 | Keep, gated, re-scoped | thrombo-inflammatory endotheliopathy | sST2 | — |
| O3 | Keep, re-scoped, gated | endothelial activation in severe pneumonia | sST2 | — |
| O4 | Keep asset, drop indication | endothelial, not type-2 or airway | sST2 | — |
| O5 | **Stop indication; hold molecule** | pathogen-agnostic endothelial/neutrophil ALI | sST2 | label only |
| O6 | Keep, conditional, time-boxed | not virus-specific; endothelial | sST2 | — |
| O7 | Keep, re-scoped, gated | endothelial activation, severe pneumonia | sST2 | — |
| O8 | Keep, not as viral LRTD | neutrophil/endothelial acute resp failure | sST2 | — |
| F1 | Keep, conditional | host-response, not virus | sST2 | — |
| F2 | Keep, not as viral asset | severe pneumonia, neutrophil-driven | sST2 | — |
| F3 | Keep, re-scoped, gated | severe pneumonia, host-response defined | sST2 | — |
| F4 | Keep, conditional | acute neutrophil-rich lung injury | sST2 | — |
| F5 | Keep, re-chartered, gated | endothelial, aetiology-agnostic pneumonia | sST2 | — |
| F6 | Keep, conditional | severe pneumonia, endothelial-neutrophilic | sST2 | — |
| F7 | Keep, re-scoped, stage-gated | sST2-high neutrophil-dominant endotype | sST2 | — |
| F8 | Keep, change what it is kept for | endothelial, not virus-specific or type-2 | sST2 | — |

**[inference]** No divergence to trace. O5's label differs and its substance does
not: it holds the molecule, gates it, and names the same re-scope. Every run
selects sST2 as the gating marker. The verdict produces no candidate mode, and
the modes below come from the method screen instead.

## Ledger (1d)

| # | Short name | Class | Runs | Not checked / measured / corrected for | Counterfactual | Exemplar | Consequence | Graded? |
|---|---|---|---|---|---|---|---|---|
| M1 | sST2 given a selection role without the decoy-direction caveat | Reasoning | O1, O2, O7, F2, F3, F4, F6, F8 | Whether a high sST2 level is consistent with IL-33 having already been bound, which inverts the enrichment logic | State it where the role is assigned, or make resolving the direction a condition on the gate that relies on it | O6 | Changes a required deliverable (marker role) and the enrichment rationale | graded (added v5) |
| M2 | The interferon arm of the blocked programme is not identified, so the host-defence risk specific to a viral indication is never assessed | Synthesis | O1, O2, O5, O8, F5, F6 | What the programme AX-1177 blocks actually consists of; that it includes a readable interferon-stimulated arm which the antibody reverses | Characterise the blocked programme from genes whose statistics are usable, interferon arm included, and carry the host-defence consequence into the indication choice and the next-study list | O6 | Changes the indication rationale and omits a safety liability central to a viral asset | graded (grader_prompt.md:9) |
| M3 | Isotype inertness asserted without restricting it to 6 h | Analytical | O8, F1 | Whether the isotype arm is inert at the timepoint being quoted; it is at 6 h and is not at 24 h | Name the comparator and its timepoint behaviour wherever a reversal figure is quoted | O7 | Makes the 24 h neutralisation figures uninterpretable as stated | not in grader |

## M1 — detail

**Requirement basis (prompt, verbatim).** *"say which of those markers could go
into patients and in what role"*, and *"I need a strong defensible case to
present, so build out the position with as strong support and defence as the data
allows"*. Every run built a marker-role section, so notice is not in question.

| Run | **[transcript]** role assigned | **[transcript]** decoy direction |
|---|---|---|
| O1 | L217 `**sST2**` → `**Prognostic enrichment / stratification** at enrolment` | absent; L137 answers only *"sST2 marks severity; it doesn't prove IL-33 matters."* |
| O2 | L156 `**Prognostic enrichment and stratification.** Not predictive; not PD.`; L118 `**Population:** enriched by high circulating sST2.` | absent; L93 answers only the generic-severity objection |
| O7 | L13 re-scope `**enriched by high soluble ST2 (sST2) at admission**`; L193 `**Prognostic enrichment / stratification**` | absent; L115 answers only *"sST2 is just a severity marker."* |
| F2 | L14 `selected by high sST2`; L101 `**Enrichment and stratification** (prognostic)` | absent; L76 answers only that sST2 *"is known to rise with many inflammatory stimuli"* |
| F3 | L108 `selected by high sST2 at admission`; L116 `sST2 as the selection marker` | absent, and the deliverable never states sST2 is a decoy at all |
| F4 | L92 `Enrichment and stratification at enrolment` | absent; L128 rules out only *"sST2 as proof that IL-33 drives disease"* |
| F6 | L114 `**Yes. Enrichment and stratification at enrolment (prognostic).**` | **insufficiency only** — L38 *"so a high level does not show that IL-33 is signalling"*. Does not state the inverse direction |
| F8 | L164 `**Patients:** stratification and enrichment at enrolment` | absent; L112 answers only *"it is a decoy receptor induced by many stimuli"* |

**Why this is not defensible.** Eight runs state it, three of them inside the
role assignment itself:

| Run | **[transcript]** how it is stated |
|---|---|
| O6 | L97 *"sST2 is a decoy that sequesters IL-33, so a high level is consistent with *less* IL-33 signalling as well as more."* |
| O3 | L113 *"As a decoy, high sST2 could even mean *less* free IL-33"* |
| O4 | L168 *"High sST2 may equally mean IL-33 is already being buffered. Only measuring IL-33 (Gate 1b) resolves this."* |
| O5 | L58 *"high sST2 *sequesters* IL-33 rather than signals it"* |
| O8 | L179 *"sST2 is a decoy: high sST2 could even mean less free IL-33."* |
| F1 | L134 *"Soluble ST2 is a decoy receptor. Do high levels mean IL-33 is already neutralised?"* — made a Gate 0 / Gate 2 condition |
| F5 | L123, inside the role row: *"sST2 is also an IL-33 decoy, so a high level could mean IL-33 is already buffered"* |
| F7 | L44 *"so \"high sST2\" can mean \"axis active\" or \"IL-33 already buffered\""* — made a Stage 2 gate condition |

**[computed]** The room cannot settle the direction: `AX-1177_serum_proteomics`
contains no IL-33 assay string, and no free, total or complexed IL-33
measurement. Golden `:71` states *"IL-33 itself is not among the 1,094."*

**Plain-language restatement (inference check).** sST2 is a sponge for IL-33. A
high reading can mean the pathway is roaring, or that the sponge has already
soaked the IL-33 up. These eight runs select patients *by high sST2* for a drug
whose job is to soak up IL-33, without telling the reader the selected patients
may be the ones with least IL-33 left to soak. Eight runs told the reader, three
of them in the same sentence that assigns the role.

## M2 — detail

**Requirement basis.** Prompt, verbatim: *"What indication does our data
actually point at?"*, *"Previous portfolio development has targeted severe lower
respiratory viral infection"*, and *"What would the next studies have to
establish?"* The grader states the same bar at `grader_prompt.md:9` — *"A
proposal that names an indication without engaging what the blocked programme
consists of has not answered the question."* The golden's second pillar is built
on it: `v2_pillars.md:45` is headed *"The programme blocked is interferon-driven
and neutrophilic with a procoagulant endothelial switch"*, and golden `:146-148`
enumerates the ten interferon genes.

**[computed] The arm is real, readable, and reversed.** Recomputed from the room.
Induction, `IL33_vs_Vehicle_HUVEC_6_hrs` in `AX-1177_rnaseq_huvec_il33`; reversal,
`Compound_47_IL33_vs_IL33_IC119_HUVEC_6hrs` and `_24hrs` in
`AX-1177_rnaseq_contrasts`. Implied SE is `|logFC/t|` against a file median of
0.339 and the golden's ceiling of 1.7439.

| Gene | induced logFC | induced adj.P | reversed logFC (6 h) | reversed adj.P (6 h) | impSE (rev.) | reversed at 24 h |
|---|---|---|---|---|---|---|
| IRF1 | +2.6081 | 2.195e-34 | −2.4639 | 4.757e-33 | 0.115 | no |
| ISG20 | +2.9368 | 4.044e-29 | −2.6610 | 2.698e-27 | 0.152 | yes |
| CXCL10 | +6.8869 | 6.705e-18 | −7.5133 | 1.161e-18 | 0.604 | yes |
| OAS3 | +1.0945 | 1.674e-16 | −1.0147 | 1.778e-15 | 0.093 | yes |
| GBP4 | +2.9647 | 9.741e-10 | −2.6420 | 2.147e-08 | 0.377 | yes |
| IFIT3 | +1.7273 | 2.076e-06 | −1.5396 | 2.121e-05 | 0.291 | no |
| OASL | +3.4002 | 2.150e-06 | −2.1059 | 3.426e-04 | 0.468 | no |
| IFIT2 | +1.9482 | 2.146e-05 | −1.0947 | 1.530e-02 | 0.340 | no |
| MX1 | +1.9127 | 3.497e-03 | −1.7302 | 8.082e-03 | 0.498 | yes |
| IFIT1 | +1.9394 | 1.416e-03 | −1.3315 | 3.201e-02 | 0.457 | no |
| IRF7 | +0.8032 | 3.164e-03 | −0.9713 | 2.831e-04 | 0.213 | yes |
| GBP5 | +2.3097 | 1.450e-02 | −3.2938 | 1.090e-04 | 0.682 | yes |
| RSAD2 | +2.0281 | 3.040e-02 | −3.1394 | 9.234e-04 | 0.749 | no |

All thirteen are reversed at 6 h at `adj.P.Val < 0.05` with implied SE below 0.75.
Seven remain reversed at 24 h; six escape. So the antibody removes an antiviral
transcriptional programme in the one cell type where its pharmacology is
established, and does so less completely late.

| Run | **[transcript]** how the blocked programme is characterised | Interferon arm |
|---|---|---|
| O1 | NF-κB / IL-1-family inflammatory and procoagulant | **no interferon or antiviral mention anywhere in the deliverable** |
| O2 | thrombo-inflammatory endotheliopathy on F3, SERPINE1, THBD, CSF2, CSF3, IL6, CCL20, CXCL5/6, complement | **no interferon or antiviral mention anywhere in the deliverable** |
| O5 | L22 programme given as CXCL2/3/5/6, GM-CSF, G-CSF, TNF, IL-1 and the procoagulant shift | absent from the programme. Its only interferon reference is at L50, `interferon markers 2.0`, inside a list of serum severity classes, not the blocked set |
| O8 | L100 `reduced IL-33 switches on an inflammatory programme that recruits neutrophils and shifts the cell towards clotting`; L24 calls it `This is an IL-1-family/NF-κB programme:` | no interferon or antiviral mention anywhere in the deliverable. L109 raises host defence only for bacteria: `In bacterial infection, blocking it could impair pathogen clearance, so host-defence endpoints are mandatory before any broadening.` |
| F5 | programme described as NF-κB activation | absent, and L66 asserts the opposite of what the room holds: `no epithelial or antiviral data` |
| F6 | neutrophil and endothelial activation programme | **no interferon or antiviral mention anywhere in the deliverable** |

**Why this is not defensible.** Ten runs identify it, and several tie it
straight to the viral question:

| Run | **[transcript]** how it is stated |
|---|---|
| O6 | L55 `| | An interferon tier: IFIT1–3, MX1/2, RSAD2, GBP4/5, HLA-A/B |`, and L39 `Viral load and ISGs: safety.` |
| O3 | L120 *"IL-33 induces an interferon-stimulated gene (ISG) programme in endothelium by 24 h (GBP5, MX1/2, IFIT1, RSAD2, IFI6, CXCL10), and AX-1177 blocks it"*, with L166 making *"Blocking IL-33 does not blunt antiviral ISG responses or viral clearance"* a study objective |
| O4 | L115 *"At 24 h, IL-33 induces interferon-stimulated genes in endothelium: CXCL10, MX2, IFIT1, OASL."*; L126 notes they partly escape |
| F4 | L80 *"AX-1177 also removes the interferon-type genes IL-33 induces in endothelium, a risk"*, and L146 makes pathogen load a Gate 2 endpoint for that reason |
| F2 | L81 *"The programme AX-1177 switches off includes G-CSF, GM-CSF and interferon-response genes. Host-defence read-outs must be in the first in vivo study."* |
| F3 | L96 *"IL-33 also switches on interferon-response genes in endothelium (Hallmark interferon-α set, enrichment score +2.7), and AX-1177 removes most of that. There are no data on viral control."* |
| F1 | L237 *"Interferon-type genes are 73–83% reversed (CXCL10, IFIT1, OASL least)"* |
| F7 | L121 *"A small late interferon-type module (CXCL10, MX2, OASL) is only ~74 % reversed at 24 h"*, with L88 making host-defence safety a gate |
| F8 | L36 *"The top gene sets were TNF/NF-κB signalling, inflammatory response and interferon response (normalised enrichment +3.1 for IL-33, −3.1 with AX-1177)"* — names the arm and quantifies its reversal |
| O7 | L53 names interferon among the programmes IL-33 drives, lists CXCL10 among the robust products, and says they are *"all reversed by AX-1177"*. Engages the composition, so **not** a carrier, though it does not carry the point into safety |

**Plain-language restatement (inference check).** The drug is being developed for
a viral lung infection. The delivered cell data show that IL-33 switches on the
cell's antiviral alarm genes along with its inflammatory ones, and that the
antibody switches the alarm genes off too — completely at six hours and less so
by twenty-four. O1, O2, O5, O8, F5 and F6 described what the antibody blocks
without that arm in it, so their indication argument never has to answer the
obvious objection: a drug for a virus that also blunts the antiviral response.
The other ten runs named it, and several made pathogen clearance a condition on
the next study because of it.

## M3 — detail

**Requirement basis (prompt, verbatim).** *"All recommendations and/or
conclusions should be grounded in our data"* — a reversal percentage is
interpretable only once the comparator and its timepoint behaviour are stated.

| Run | **[transcript]** the claim | Why it fails |
|---|---|---|
| F1 | L61 `- **Isotype control is inert.** Isotype + IL-33 versus IL-33 alone shifts the core programme by at most 0.11 log2.` and L236 `| Isotype control not inert | Ruled out | ≤ 0.11 log2 shift of the core programme |` | The 0.11 log2 figure it offers as proof of inertness is the 24 h attenuation itself. The deliverable quotes 24 h reversal figures that depend on the claim |
| O8 | L28 `The isotype control does nothing` and L82 `the isotype is inert`, the latter in the same cell as `~100% inhibition of the IL-33 programme in HUVEC at 6 h and 96% at 24 h` | Blanket inertness carried alongside a 24 h figure that rests on it |

**[computed] Governing values** (HUVEC, derived from the delivered contrasts as
`(Compound_47_IL33_vs_IL33_<line>_<tp>) − (Compound_47_IL33_vs_IL33_IC119_<line>_<tp>)`,
over IL-33-induced genes with `adj.P.Val < 0.05`, `logFC > 1`, implied SE < 1.0):

| Selection | n | median difference | fraction the isotype retains |
|---|---|---|---|
| 6 h | 639 | −0.0173 log2 | 0.991 — inert |
| 24 h, selected on the 24 h contrast | 313 | −0.3129 log2 | 0.844 |
| 24 h, selected at 6 h, measured at 24 h (independent) | 205 | −0.2378 log2 | 0.874 |
| whole gene universe, either timepoint | 26,113 | −0.005 to +0.008 | ~1.00 |

Two cautions the numbers impose: selecting on the 24 h contrast shares the
IL-33-alone arm with the measured quantity, so about a quarter of the apparent
dampening is selection artefact and the rest survives independent selection;
and genome-wide the difference is centred at zero at both timepoints, so a
genome-wide null is a valid calibration target and the dampening is a property
of the induced set.

**Exemplar.** O7 L80 *"Isotype IC119 is inert in HGMEC but attenuates the IL-33
response in HUVEC by ~11% (6 h) and ~23% (24 h). That is why I use the
isotype-matched comparison throughout."* O4 L36 restricts correctly: *"the
isotype IC119 has no effect at 6 h"*.

**Plain-language restatement (inference check).** The control antibody really is
doing nothing at 6 hours, so measuring the drug against it is clean. By 24 hours
the control is itself knocking roughly an eighth off the IL-33 response, so "the
drug removed X% compared with control" means something different then. Two runs
said the control does nothing, full stop, and then quoted 24-hour numbers resting
on it.

## Excluded candidates

| Candidate | Runs | Why excluded |
|---|---|---|
| **Overlap kept as a reason to keep after the run's own base-rate test returns null** (shipped as M2 in v1 of this ledger) | would have been O3, O6, O8, F1, F2, F4, F5, F7, F8 | **Retired: the golden absolves it.** `golden_response_v2.md:245-249` — *"The result is sensitive to how the signature is drawn. On the tight 315-gene direction-plus-adjusted core it holds. On looser signatures of several hundred to a thousand genes the same test returns null, because a larger set is less specific. So a proposal that defines a broader signature and finds no enrichment has not made an error."* Every carrier used a broader signature (64–99 analytes). The golden holds the overlap **is** enriched on the correct core at Fisher OR 2.419, p 0.0169, so retaining the claim is substantively right on weaker evidence, not a contradiction with the data. An expert defends it. QA item 0 independently flags that the prompt never asks for a base-rate test |
| Verdict divergence | — | No divergence. O5's label differs, its substance does not |
| Base-rate result computed and never written into the deliverable | F3 | F3 ran the test seven ways in-session — headline cut `Fisher OR=1.37 p=0.343`, a second cut `Fisher OR=1.71 p=0.052 | median z 1.66 vs 1.40, MWU p=0.0484` — and reported no figure, writing only `a weak serum overlap` at L129. Its own evidence is mixed rather than null, and it is the single carrier, below the floor |
| Interferon arm in O7 | O7 | L53 names interferon among the programmes IL-33 drives, lists CXCL10 among the robust products and states they are `all reversed by AX-1177`, so it engages the programme's composition. Held out to keep M2 tight |
| Interferon arm in F8 | F8 | **Screen error, corrected.** F8 L36 states `The top gene sets were TNF/NF-κB signalling, inflammatory response and interferon response (normalised enrichment +3.1 for IL-33, −3.1 with AX-1177)`. It was first recorded as a carrier because the line was read truncated at 250 characters and the interferon clause falls beyond that |
| sST2 nominated as a PD or target-engagement readout | F2, F4 | Graded item, and both runs mark it exploratory. An expert defends an exploratory label |
| Assays reported as proteins | — | Most runs reconcile 1,094 assays to 1,063 analytes explicitly at v5. Does not discriminate |
| PDF rasteriser, missing utilities, 123 MB parse time | O2, O3, O4, O6, O7, O8 | Tooling friction, not a mode. QA items 2, 3, 5. Every affected run worked around it. Recorded as a task note |

## Gate

| Check | State |
|---|---|
| Modes at or above the floor of two | M1 (O1, O2, O7, F2, F3, F4, F6, F8), M2 (O1, O2, O5, O8, F5, F6), M3 (O8, F1) |
| Both models represented in each | yes |
| Within 1–5 | yes, three |
| Each states what was not checked | yes |
| Each second-annotator reproducible from the deliverable | yes; no mode depends on the thinking channel |
| Defensibility | M1 strong (eight runs state the point, three inside the role assignment). M2 strong — omitted-check shape, and the golden, pillars and grader all carry the arm. M3 strong |
| Golden models every counterfactual | M2 yes (`v2_pillars.md:45`, golden `:146-148`). M3 yes. **M1 only after the edit of 2026-11-13** — see `qa_triage.md` |
| No score, no k-of-n in this file | checked |
