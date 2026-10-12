"""Record library-redraw winners from a round json into winners.json (replace any entry with the same shot).
usage: libv2_winner.py <round.json> <round_n> <file-suffix e.g. R42/r1-1.png> [...]"""
import json, sys, os
R = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'script-src/molly-v2/ratings')
rnd = json.load(open(sys.argv[1])); n = int(sys.argv[2])
W = json.load(open(os.path.join(R, 'winners.json')))
for suf in sys.argv[3:]:
    x = next(c for c in rnd if c['file'].endswith(suf))
    e = {"shot": x['shot'], "replaces": x['replaces'], "file": x['file'], "round_rated": n, "total": x['total'],
         "scores": x['scores'], "minor": x.get('minor', []) + x.get('defects', [])}
    W = [w for w in W if w.get('shot') != x['shot']] + [e]
    print(e['shot'], e['replaces'], e['total'])
json.dump(W, open(os.path.join(R, 'winners.json'), 'w'), indent=1, ensure_ascii=False)
