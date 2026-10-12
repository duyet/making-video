---
name: google-flow-video
description: >-
  Drive Google Flow (labs.google/fx/tools/flow, Google's Veo-powered AI filmmaking tool) through the
  Chrome browser to generate AI video — b-roll clips, multi-scene shorts, cover/thumbnail stills, and
  consistent characters via "ingredients" — and download the results to a folder. Use this skill
  WHENEVER the user wants to generate or download AI video/clips/scenes/b-roll from Google Flow, "make
  a video with Flow / Veo", build video material or thumbnails from Flow, create short vertical (9:16)
  clips for TikTok/Shorts, animate a prompt or reference image in Flow, or asks to control/automate the
  Flow web app — even if they don't name the tool explicitly but mention Google's AI video tool, Veo,
  Flow, or "labs.google". This is a BROWSER-AUTOMATION skill: it runs Flow's real web UI via the
  claude-in-chrome tools, it does not call an API.
compatibility: Requires the claude-in-chrome MCP tools and a Chrome where the user is signed in to a Google account with Flow access (Google AI Pro/Ultra).
---

# Google Flow — AI video generation via Chrome

Google **Flow** (`labs.google/fx/tools/flow`) is Google's AI filmmaking tool, powered by **Veo** (video, with
audio) and **Imagen** (stills). There is no public API, so the only way to drive it is its web UI. This skill
automates that UI through the `claude-in-chrome` tools to produce **standalone downloads** the user can then use
as material: b-roll clips, multi-scene shorts, cover/thumbnail stills, and consistent characters.

Flow's UI is an evolving AI product — exact button labels and layout WILL drift over time. So this skill teaches
the *workflow and intent*, and relies on you to **look at the page** (screenshots + `read_page`) and adapt, rather
than hard-coding selectors. Treat the steps below as the shape of the task, not a rigid script.

For **stills** (Nano Banana via the Agent chat, consistent characters, 1K/2K/4K downloads), prompt design, and
the hard-won chat-automation rules (single-line messages, idle gate, localhost receiver), use the sibling skill
`google-flow-images` — its `references/automation.md` and `references/prompt-design.md` apply to Veo work too.

## Before you start

1. **Load the browser tools in ONE `ToolSearch` call** (they're usually deferred). Start with the core set plus
   the ones this task needs (downloads, scripting):
   `ToolSearch("select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__javascript_tool")`
2. Call `tabs_context_mcp` first to see existing tabs. **Create a new tab** for Flow rather than reusing one,
   unless the user points you at an open Flow tab.
3. Navigate to `https://labs.google/fx/tools/flow`. **Verify the user is signed in** (screenshot / `read_page`).
   If you hit a sign-in wall or "no access" / upgrade prompt, STOP and tell the user — they must sign in
   themselves (it's an interactive Google OAuth + a paid tier; you cannot and should not do it for them). Suggest
   they sign in in that Chrome window, then say "go".
4. Confirm the **output folder**. Chrome downloads land in the default download dir; ask the user where they want
   the material (e.g. `data/flow/<project>/`) and plan to move/organize downloads there after each batch.

## The core loop (applies to every output type)

Generation in Flow is **asynchronous** — you submit a prompt and clips render over seconds to minutes. So every
task is: **set up → submit → wait & verify → download → organize.**

- **Set up the project & format.** Open or create a project. Set the **aspect ratio** before generating — for
  TikTok/Shorts material choose **9:16 (vertical)**; for YouTube landscape use 16:9. Set the model (prefer the
  latest **Veo** with audio when available) and the number of outputs per prompt if exposed.
- **Submit** the prompt in the prompt box (`form_input` or click+type via `computer`). Use the prompting patterns
  below — Veo rewards cinematographic, specific prompts.
- **Wait & verify.** Do NOT assume it's done. Poll: screenshot / `read_page` every several seconds until the clip
  thumbnails finish (look for the play button / progress reaching 100% / the spinner disappearing). Generation can
  take a while; be patient and check rather than spamming clicks. If you must wait, use a short poll loop, not a
  single guess.
- **Download.** Use each clip's download/export control (often a ⋯ menu → Download, or a download icon on hover).
  After the browser reports the download, the file is in the Chrome download dir.
- **Organize.** Move/rename each download into the user's chosen folder with a meaningful name
  (`<project>_<shot>_<short-prompt-slug>.mp4`). Keep a small index (a `manifest.json` or a markdown list) mapping
  filename → prompt → settings so the material is reusable.

**Never trigger native browser dialogs** (alert/confirm) and avoid clicking things that open them — a modal dialog
freezes the extension. If the page shows an in-page modal (e.g. a delete confirm), handle it deliberately, and if
you get stuck, tell the user to dismiss it manually.

## Output A — B-roll clips (text → video)

The default and simplest mode. One prompt → one or more short clips, for use as scene backgrounds / b-roll.

- Use Flow's **Text to Video** input. Set 9:16, pick the Veo model, set outputs (e.g. 1–4) if available.
- Write one clip prompt per shot you need. Keep each clip a **single continuous moment** (one camera move, one
  action) — Veo clips are short (often ~8s); don't pack a whole scene into one prompt.
- Submit, wait, download each, organize. For a batch (e.g. 6 b-roll shots), loop the core loop per prompt and keep
  the tab on the same project so they group together.

## Output B — Multi-scene shorts (Scenebuilder + extend)

To assemble a full short rather than isolated clips:

- Generate an opening clip, then use **"Extend"** (a.k.a. "Jump to" / "Add to scene") to continue the action into
  the next clip so motion/identity carry over. Flow's **Scenebuilder** view shows the shot timeline — use it to
  add, reorder, and extend shots.
- Drive continuity with the prompt ("continue the same shot, the character now turns and walks left…") and with
  **start/end frames** ("Frames to Video") when you need a specific transition.
- When the sequence is complete, use Flow's **export/download the full scene** option to get the stitched video;
  otherwise download each shot and stitch externally (ffmpeg) — tell the user which you did.

## Output C — Cover / thumbnail stills

For a striking still to use as a video cover/thumbnail:

- Prefer generating a **frame/still** directly (Flow exposes image generation via Imagen / "Frames"), OR generate a
  short clip and **grab the hero frame** (download the clip, then `ffmpeg -ss <t> -frames:v 1` for the cover).
- Compose for the cover use-case: strong subject, negative space for an overlaid headline, high contrast. The
  *headline text itself* is usually added later by the thumbnail compositor — generate the **background image**,
  not text-baked-in (Veo/Imagen text rendering is unreliable).
- Download at the highest available resolution; 9:16 (1080×1920) for vertical covers.

## Output D — Ingredients (consistent character / persona)

Flow's **"Ingredients to Video"** lets you upload reference images so a subject/style stays consistent across clips
— ideal for a recurring persona (e.g. a channel's character).

- Upload the reference image(s) as **ingredients** (file picker → the `file_upload`/`upload_image` tool, or the
  page's upload control). Use a few clean, consistent references of the same subject.
- Reference the ingredient in prompts ("the woman from the reference, now coding at a desk, …"). Generate clips as
  in Output A but with the ingredient attached, so the character is recognizably the same across the set.
- Save the ingredient images alongside the project so the look is reproducible later.

## Prompting Veo (what actually improves output)

Veo rewards **specific, cinematographic** prompts. Structure each clip prompt as: **subject + action + setting +
camera + lighting/mood + lens/style.**

**Example 1**
Input intent: "a coder girl at night, techy vibe, vertical"
Prompt: "A young woman in a dim home office lit by monitor glow, typing fast on a laptop, neon code reflecting on
her glasses; slow push-in dolly, shallow depth of field, cinematic teal-and-magenta color grade, 9:16 vertical."

**Example 2**
Input intent: "abstract AI network b-roll"
Prompt: "Macro shot of glowing data nodes connected by pulsing light threads drifting through dark space, particles
floating, gentle parallax camera drift, volumetric light, hyper-detailed, 9:16 vertical."

Tips: one clear action per clip; name the **camera move** (push-in, orbit, handheld, static) and the **lighting**;
specify **9:16 vertical** in the prompt as well as the UI setting; avoid asking for on-screen text; if a result is
off, iterate the prompt rather than re-rolling identical text.

## Robustness & etiquette

- **Adapt to the live UI.** Labels change. Use `read_page`/screenshots to find the prompt box, format selector,
  generate button, and download control by their visible role/text, not memorized positions.
- **Respect rate/quota.** Flow tiers cap generations/credits. If you hit a quota or error banner, stop and report
  it — don't hammer generate.
- **Don't rabbit-hole.** If a control can't be found or a step fails after 2–3 honest attempts, screenshot, explain
  what you tried, and ask the user how to proceed (per the browser-automation guidance).
- **Record what you made.** Always leave the user a manifest (filename → prompt → settings → which output type) so
  the generated material is reusable, and tell them the folder it's in.
- **Optional: record a GIF** of a multi-step generation with `gif_creator` if the user wants to review the run.
