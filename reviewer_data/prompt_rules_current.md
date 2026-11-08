# Prompt rules as of 2026-11-08

Writer-confirmed against revised project guidance, during the v2 rebuild.
Recorded here because the scoping skill still states the superseded versions
and will keep doing so — see the note at the bottom.

## Deprecated

| No longer required | What to do instead |
|---|---|
| Fix an as-of date, not in the future | State no as-of date |
| Name each deliverable and the path it goes to | Name no output file, path or deliverable object. This extends to `.md` files and to any named artifact — report, write-up, memo, deck. The reply is the deliverable, and the questions may be open-ended |
| Make the mounted-only constraint explicit, do not search the web | Add no no-web line. Saying the files are the record is a scene fact and is fine; forbidding search is not |
| Require analysis saved under an outputs path | Drop it, with the paths |

## Two consequences

**The grader loses the saved-artifact surface.** Nothing can be recomputed
from what the model filed, because it files nothing. Provenance per number is
now the only guard against a reply that invented its figures, so it carries
more weight than it did.

**The verdict is no longer deterministically parseable.** The prompt audit
wants both a parseable verdict and no printed answer set. With formats and
paths gone, those conflict. Resolve toward not printing the options: the
solver constructs the verdict in its own words.

## Still current, and applied in the v2 prompt

Terse brief, situation then ask. No personas, no numbered analysis steps, no
tool names, no cautions, no hints. Load-bearing sources unnamed and the room
described generically. Spoken by whoever owns the decision. Decision rule not
stated and the answer set not printed. Several products that fail
independently. Provenance per number. A set-aside section. Under 600 words.

## Why this file exists

The scoping skill is delivered as a plugin and synced into a per-session
cache that has no version control and no link to this repository. Editing that
cache in-session changes nothing durable — the next sync overwrites it. The
deprecations above were applied to the cached copy on 2026-11-08 and are
**container-only**; they are in neither the published skill nor this repo
beyond this note.

To make them stick, the edit has to be made wherever the plugin is published.
Until then every new session loads the superseded text and will re-assert all
four rules. The affected places in that text are the "A group leader briefing
a colleague DOES" list, the template's output-headings paragraph, the length
paragraph, the provenance note, six items of the prompt audit checklist, and
the handoff template's deliverables and as-of-date lines.
