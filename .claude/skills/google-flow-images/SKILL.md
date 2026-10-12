---
name: google-flow-images
description: >-
  Drive Google Flow (labs.google/fx/tools/flow) through Chrome to generate and edit STILL IMAGES with
  Nano Banana via Flow's agent chat — storyboard shots, illustrations, reference sheets, consistent
  characters across 30+ shots, batch generation, collections, editor view, and 1K/2K/4K downloads —
  and to design detailed image/Veo prompts. Use this skill WHENEVER the user wants images or stills
  from Flow / Nano Banana / Imagen, a storyboard or shot list illustrated, a character kept consistent
  across many images, Flow images downloaded or upscaled, or help writing Nano Banana / Veo prompts.
  For video clips (Veo, extend, scenebuilder) also see google-flow-video. BROWSER-AUTOMATION skill:
  uses the claude-in-chrome tools; there is no public API.
compatibility: Requires claude-in-chrome MCP tools, a Chrome signed in to a Google account with Flow access (Google AI Plus/Pro/Ultra), python3 + Pillow for the helper scripts.
---

# Google Flow — images via the agent chat

Flow = Google's creative studio: **Nano Banana** (images), **Veo** (video), an **Agent** chat panel that can
generate, batch, edit, rename and file assets into **Collections**, plus an image **editor view**. No public API and
no WebMCP tools (see `references/automation.md`) — drive the real UI with claude-in-chrome. Labels drift; screenshot
and adapt.

Files:
- `references/automation.md` — UI map, agent chat protocol, downloads, WebMCP/API findings, failure modes.
- `references/prompt-design.md` — how to write prompts; character bible; 30+ shot consistency; worked examples.
- `references/project-lessons.md` — this repo's multi-worker loop, quality bar, and failure modes (2K upscale, Vimium, quota).
- `scripts/flow_recv.py` — localhost receiver (127.0.0.1:8765) for page-JS blob saves.
- `scripts/flow_match.py` — dHash matcher: map downloads (2K) back to reference images / shot ids.
- `scripts/flow_snippets.js` — idle detection, collect large images, post to receiver, scroll collections.

## Workflow

1. **Setup.** ToolSearch-load `tabs_context_mcp, navigate, computer, read_page, find, javascript_tool` in one call.
   Open the Flow project (sign-in / paywall → stop, ask user). Turn **Agent** on in the prompt box, expand the panel.
   In Agent settings set image defaults (16:9, model, outputs) and consider Confirmations = Never for long batches
   (ask the user first — it spends credits without pausing).
2. **Plan prompts offline** with `references/prompt-design.md`: write a character bible, then one self-contained
   prompt per shot (shot id, full identity anchors, negatives). Keep a `shots.json`/markdown manifest.
3. **Send one message per batch** (3–4 shots). For each send:
   - Run the idle snippet; send only when `busy:false`. A message sent while busy is **silently lost**.
   - Type a **single line** (no newlines — Enter sends, so newlines fragment the message), then press Return.
   - Poll idle every ~10–20 s. Read the chat tail: answer clarifying questions / "Approve N credits" /
     "Xác nhận…" confirmations; on "Too many generations are running" or "Something went wrong" wait and resend.
4. **Collect 1K** right away: on the project view (not `/edit/`), the last N large images in the latest chat
   message are the batch in prompt order → snippet 2 + 3 posts them to `flow_recv.py` as `<shot_id>.jpg`.
   Eyeball a contact sheet; regenerate or edit failures (edit requests: see prompt-design §Edits).
5. **Get 2K finals** with real user-gesture clicks (programmatic downloads get blocked after the first): tile ⋮ →
   Download ▸ 2K, or open tile → editor → download icon → 2K ("Upscaling…", saves `<Title>_2K_<ts>.jpg`,
   2752×1536 for 16:9, to ~/Downloads). 4K is Upgrade-locked on Plus.
6. **Map & file**: `python3 scripts/flow_match.py ~/Downloads/<batch> <dir_of_1K_shots> --rename` → copies matches
   as `<shot_id>.jpg`. Never map by grid position (lazy-load re-sorts it).
7. **Record**: manifest of shot id → prompt → file → Flow title. Report folder to the user.

## Non-negotiables

- One line per message; wait for idle; read the tail after every turn.
- Repeat full character anchors in every prompt — the agent does not reliably carry identity between turns.
- Ask for "no text, no captions, no watermark" every time.
- Verify period/anatomical accuracy visually before accepting a shot (e.g. iron lung: patient supine, face up).
- Stop and report on quota/paywall/sign-in; don't hammer generate. After 2–3 failed attempts at a UI step, ask.
