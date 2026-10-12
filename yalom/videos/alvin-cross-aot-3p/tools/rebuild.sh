#!/bin/sh
# rebuild.sh <script> visuals          fit the voices to shared slots → build → check → render the silent picture once (QUALITY defaults to draft)
# rebuild.sh <script> mux <voice|all>  mix each voice's VO + ducked music + SFX onto that picture → renders/preview-aot-3p.<script>.<voice>.mp4
cd "$(dirname "$0")/.."
N=~/.nvm/versions/node/v24.18.0/bin; HF="$N/node $N/npx --yes hyperframes@0.8.143"
S="${1:?script}"; PIC="renders/preview-aot-3p.$S.picture.mp4"
case "$2" in
visuals)
  python3 narration/fit.py "$S" && python3 tools/build.py "$S" || exit 1
  PATH=$N:/usr/bin:/bin $HF check >/dev/null || { echo "check failed: $S"; exit 1; }
  PATH=$N:/usr/bin:/bin $HF render -q "${QUALITY:-draft}" -o "$PIC" >"${PIC%.mp4}.log" 2>&1 || { echo "render failed: ${PIC%.mp4}.log"; exit 1; }
  echo "$PIC $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$PIC")s" ;;
mux)
  [ "${3:?voice|all}" = all ] && VOICES=$(python3 -c "import json;print(*json.load(open('narration/scripts/$S/slots.json'))['voices'])") || VOICES="$3"
  for v in $VOICES; do python3 tools/mux.py "$S" "$v" "$PIC" "renders/preview-aot-3p.$S.$v.mp4" || exit 1; done ;;
*) echo "usage: rebuild.sh <script> visuals | rebuild.sh <script> mux <voice|all>"; exit 1 ;;
esac
