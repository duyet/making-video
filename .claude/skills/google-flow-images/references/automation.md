# Flow automation reference

Observed in a Plus-tier session (Oct 2026). Labels and layout drift — confirm with a screenshot.

## UI map

- **Project view** (`/fx/tools/flow/project/<id>`): asset grid (images + videos) on the left, prompt box at bottom.
  Click **Agent** in the prompt box to toggle the agent; expand icon opens it as a right-side panel (x ≈ 980+ in a
  ~1500px window). Chat header shows an agent/session name that may change per conversation; the **new chat** icon
  is top-right of the panel. Panel menu: sessions (open/create/rename/delete), Agent Instructions (project-wide
  guidelines + optional reference image), Settings (Confirmations, image defaults: ratio/outputs/model, video defaults).
- **Grid tile hover ⋮ menu**: Download ▸ 1K / 2K / 4K, Animate (→ Veo), Add to prompt, Reuse prompt, Rename,
  Set project cover, Move to trash.
- **Editor view** (`/edit/<id>`, opened by clicking a tile): large image, filmstrip of the project's assets,
  download icon top right → 1K original / 2K upscaled / 4K (Upgrade badge on Plus). 2K shows "Upscaling your image,
  download will start automatically" and saves `<Title>_2K_<timestamp>.jpg` (2752×1536 for 16:9) to ~/Downloads.
  Lasso/region edits live here too.
- **Collections**: the agent auto-files outputs into the project's collection; you can also ask it to group selected
  assets into a new Collection, rename, or delete. The collection page lazy-loads — scroll the **inner** scroller
  (snippet 4), not `window`.
- **Characters / ingredients**: upload or select reference images ("Add to prompt" from a tile, drag-in, or the
  ingredients control) so the model conditions on them. Nano Banana 2 claims consistency for up to ~5 characters and
  ~14 objects per workflow — still repeat textual anchors.

## Agent chat protocol

1. **Idle gate.** Busy ⇔ a button with aria-label/text "Stop" exists (snippet 1). Never send while busy — the message
   is dropped without error.
2. **Single line.** The prompt box sends on Enter. A prompt with newlines arrives as several fragmented messages,
   each of which may trigger its own generation. Join everything into one line (`;` / ` — ` separators), click the
   box, type, press Return.
3. **Batch phrasing.** "Generate 4 separate 16:9 images, one per shot, in this order: [S01] … [S02] … Keep each
   image a separate generation; no collage, no grid." 3–4 shots per message is reliable; larger batches trigger
   "Too many generations are running. Please wait and try again".
4. **Read the tail** (`get_page_text` or snippet 1's `tail`) after every turn. The agent may:
   - ask a clarifying question or propose a plan → answer in one line;
   - request credit approval ("Approve 15 credits", Vietnamese UI: "Xác nhận…") → click the approve button or reply
     "yes, approve"; or set Confirmations = Never (only with user consent);
   - report "Something went wrong" → wait 30–60 s, resend the same line.
5. **New session** when the chat gets long/slow or drifts in style: new-chat icon, then restate the style + character
   bible in the first message (or put them in Agent Instructions once per project — best option).

## Getting files out

| Need | Method | Why |
|---|---|---|
| 1K, many images | page JS `fetch(img.src)` → POST to `scripts/flow_recv.py` | anchor/`a.download` clicks get blocked after the first by Chrome's "multiple automatic downloads" protection |
| 2K / 4K | real clicks: tile ⋮ → Download ▸ 2K, or editor → download → 2K | upscale happens server-side on request; needs a user-gesture click via `computer` |
| Whole set | ask agent to file into a Collection, then open it and scroll to load | grouping only; downloads are still per image |

Start the receiver: `python3 ~/.claude/skills/google-flow-images/scripts/flow_recv.py <out_dir>` (run in background).
It sends CORS + `Access-Control-Allow-Private-Network: true` so the https page may POST to 127.0.0.1.

**Mapping.** Grid DOM order is unstable (lazy load, re-sort, new items prepend), so position-based mapping fails.
Reliable mappings: (a) chat panel — last N large images of the latest agent message = this batch in prompt order
(project view only; on `/edit/` the panel/filmstrip images interfere); (b) content — `flow_match.py` dHash between
2K downloads and the named 1K files (dist ≤ 5 same image; > 12 different); (c) rename assets via the agent
("rename the 4 images you just made to S01..S04") so the 2K filename carries the shot id.

## WebMCP / API findings (Oct 2026)

- **WebMCP**: no evidence Flow registers tools via `navigator.modelContext` / `document.modelContext` or declarative
  `<form toolname>` tools. WebMCP itself is an early-preview Chrome API (flag / origin trial) and Google has not
  announced Flow support. To re-check on a live page: `javascript_tool` →
  `({nm: !!navigator.modelContext, dm: !!document.modelContext, forms: document.querySelectorAll('[toolname]').length})`.
- **Public API**: none for Flow. Veo and Nano Banana (Gemini image) have official APIs via Gemini API / Vertex AI —
  use those if the user has keys and wants headless generation; outputs won't land in the Flow project.
- **Internal endpoints**: the web app calls private Google backends with the session's OAuth token. Unofficial
  tools (gflow-cli, Google-Flow_MCP, Chrome extensions) all drive the UI via CDP/extension rather than a documented
  API. Don't call private endpoints directly — undocumented, ToS-risky, credit-billing, and they change without notice.
- **Most reliable approach**: the official Agent chat panel driven by claude-in-chrome (type one line → idle-gate →
  read tail), page JS only for *reading* the DOM and exporting already-rendered images, real clicks for upscale downloads.

## Related notes

- Free HeyGen cannot generate images (avatar/prompt endpoint needs paid plan) → Flow is the image source.
- Veo animation of a still: tile ⋮ → Animate, or ask the agent; see google-flow-video for clip workflow.
