"""Cost snapshot for the video work: Claude tokens per model (all session transcripts of this project) and ElevenLabs characters.
usage: cost.py [--log]   (--log also appends a one-line summary to TODO-molly-v2.md)"""
import collections, glob, json, os, sys, time, urllib.request
os.environ.setdefault('SSL_CERT_FILE', '/etc/ssl/cert.pem')
V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.expanduser('~/.claude/projects/-Users-duet-project-make-video-yalom')

agg = collections.defaultdict(lambda: [0, 0, 0, 0])  # calls, output, cache read, cache write
seen = set()
for f in glob.glob(os.path.join(T, '**', '*.jsonl'), recursive=True):
  for ln in open(f, errors='ignore'):
    try: m = json.loads(ln).get('message') or {}
    except ValueError: continue
    u, mid = m.get('usage'), m.get('id')
    if not u or not mid or mid in seen: continue
    seen.add(mid); a = agg[m.get('model', '?')]
    a[0] += 1; a[1] += u.get('output_tokens', 0); a[2] += u.get('cache_read_input_tokens', 0); a[3] += u.get('cache_creation_input_tokens', 0)

req = urllib.request.Request('https://api.elevenlabs.io/v1/user/subscription', headers={'xi-api-key': os.environ['ELEVENLABS_API_KEY']})
sub = json.load(urllib.request.urlopen(req))
used, limit = sub['character_count'], sub['character_limit']

rows = [(m, *a) for m, a in sorted(agg.items(), key=lambda x: -x[1][2]) if m != '<synthetic>']
for m, n, o, cr, cw in rows:
  print(f'{m:22} calls {n:6}  out {o/1e6:5.2f}M  cache read {cr/1e6:8.1f}M  cache write {cw/1e6:5.1f}M')
print(f'elevenlabs             {used:,} / {limit:,} chars used, {limit-used:,} left')
if '--log' in sys.argv:
  short = ', '.join(f'{m.replace("claude-", "")} {n} calls/{cr/1e6:.0f}M read' for m, n, o, cr, cw in rows)
  with open(os.path.join(V, 'TODO-molly-v2.md'), 'a') as fh:
    fh.write(f'- {time.strftime("%H:%M")} COST: {short}; ElevenLabs {used:,}/{limit:,} chars\n')
