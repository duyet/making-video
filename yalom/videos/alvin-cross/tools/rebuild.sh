#!/bin/sh
# build → carve the music bed under the VO → merge fades
cd "$(dirname "$0")/.."
N=~/.nvm/versions/node/v24.18.0/bin
REF_INDEX="${REF_INDEX:?}" python3 tools/build.py && $N/node ~/.claude/skills/hyperframes-audio/scripts/carve.mjs --comp index.html >/dev/null && python3 tools/merge_fade.py
