# making-video

Narrated, image-driven videos with Vietnamese voice-over. Pictures are HTML compositions rendered by [HyperFrames](https://hyperframes.heygen.com), stills come from Google Flow (Nano Banana), and the voice comes from ElevenLabs.

Current project: **Thank You, Molly** (`yalom/`), script id `molly-v2`, built in three variants (original, first-person AOT, third-person AOT).

## Pipeline

```
SHEET.md → lines.json (VO text) → shots.json → Flow images → storyboard score
        → tts.py → fit.py → build.py → hyperframes render → mux.py → renders/*.mp4
```

Run the steps from a project folder such as `yalom/videos/alvin-cross-aot-3p`:

```bash
npm install
npm run check                                            # must be clean before rendering
python3 narration/tts.py molly-v2 thanh                  # spends ElevenLabs credits
python3 narration/fit.py molly-v2
QUALITY=standard sh tools/rebuild.sh molly-v2 visuals    # picture render
sh tools/rebuild.sh molly-v2 mux all                     # mux each voice into renders/
```

`ELEVENLABS_API_KEY` must be set in your environment. Never commit it.

## Layout

| Path | What |
|---|---|
| `yalom/videos/<project>/` | One standalone HyperFrames project each |
| `yalom/videos/tools/cost.py` | Claude-token and ElevenLabs credit snapshot |
| `yalom/videos/TODO-molly-v2.md` | Running log: decisions, blockers, resume commands |
| `.claude/skills/` | Project skills: HyperFrames family, Google Flow, `vo-narration`, `make-good-video` |
| `AGENTS.md` | Rules for coding agents (`CLAUDE.md` imports it) |

## Not in git

Images, audio, video, `renders/` and `node_modules/` are gitignored (about 9 GB). They live only on the author's machine, so a fresh clone has the source and scripts but cannot render until assets are regenerated or restored.

## Working with agents

Read `AGENTS.md` first. It lists which skill to load for which task, the credit and quota rules, and the quality bar (storyboard and image score of 9.0 or above).
