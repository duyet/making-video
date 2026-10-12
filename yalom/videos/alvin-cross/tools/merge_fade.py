"""After carve.mjs: add a fade-in/out volume lane into the music bed's carve automation."""
import re,json,html,os,sys
p=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'index.html')
s=open(p).read()
m=re.search(r'<audio id="music-bed"[^>]*>',s); tag=m.group(0)
d=float(re.search(r'data-duration="([\d.]+)"',tag).group(1))
am=re.search(r'data-automation="([^"]*)"',tag)
a=json.loads(html.unescape(am.group(1)))
a['lanes']=[l for l in a['lanes'] if l['target']!='volume']+[{'target':'volume','points':[{'t':0,'v':0},{'t':3,'v':1},{'t':round(d-5,3),'v':1},{'t':round(d,3),'v':0}]}]
new=tag.replace(am.group(0),'data-automation="'+html.escape(json.dumps(a,separators=(',',':')),quote=True)+'"')
open(p,'w').write(s.replace(tag,new)); print('merged volume lane; lanes:',[l['target'] for l in a['lanes']])
