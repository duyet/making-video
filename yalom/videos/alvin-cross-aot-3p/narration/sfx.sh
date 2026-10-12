cd "$(dirname "$0")/../assets"
gen(){ curl -s --fail-with-body -o sfx/$1.mp3 -X POST https://api.elevenlabs.io/v1/sound-generation -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" -d "{\"text\":\"$2\",\"duration_seconds\":$3,\"prompt_influence\":0.5}" && echo "sfx $1 ok" || echo "sfx $1 FAIL $(head -c 200 sfx/$1.mp3)"; }
gen wind "Soft gentle wind through grass and willow trees in a quiet foggy cemetery, distant faint church bell, calm ambience, no voices" 22 &
gen clock "Slow old mechanical clock ticking in a quiet room, close, steady" 12 &
gen hum "Low electrical hum of a fluorescent x-ray lightbox in a quiet hospital room" 12 &
gen paper "Rustling old newspapers being stacked and bundled, paper crinkling" 8 &
gen raven "Large raven wings flapping heavily then a single dark caw, reverberant" 5 &
curl -s --fail-with-body -o music/bed.mp3 -X POST "https://api.elevenlabs.io/v1/music" -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" -d '{"prompt":"Slow, sparse, melancholic solo acoustic piano with a low mournful cello entering in fragments. Documentary film score, contemplative, intimate, lots of space and silence between phrases, 60 bpm, no drums, no vocals. Gradually warms toward a gentle hopeful resolution at the end.","music_length_ms":180000}' && echo "music ok" || echo "music FAIL $(head -c 300 music/bed.mp3)"
wait
