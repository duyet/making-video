"""Write the molly-v2 script data (lines, shots, script cards, ref-index) for both projects from one shared shot plan.
The 3p and 1p sheets have the same beats, so each line has one shot list; only the cue phrases differ per text.
usage: molly_v2.py   -> alvin-cross-aot-3p/narration/scripts/molly-v2/ and alvin-cross-aot/narration/scripts/molly-v2/"""
import json,os
V=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P3,P1=os.path.join(V,'alvin-cross-aot-3p'),os.path.join(V,'alvin-cross-aot')

# id: (3p text, 1p text)
LINES={
 'a01':('Một buổi chiều đầy nắng, nhà trị liệu Irvin Yalom đến dự tang lễ của bà Molly.',
        'Tôi đến dự tang lễ của Molly vào một buổi chiều đầy nắng.'),
 'a02':('Suốt hàng chục năm, bà lo liệu mọi việc cho ông: tận tụy, quyết đoán, và đôi khi… khiến ông phát điên.',
        'Suốt hàng chục năm, bà lo liệu mọi việc cho tôi. Đôi khi bà khiến tôi phát điên, nhưng tôi không thể thiếu bà.'),
 'a03':('Lúc Yalom chuẩn bị ra về, một người đàn ông đội mũ Panama cùng vợ tiến đến.',
        'Khi tôi sắp ra về, một người đàn ông đội mũ Panama tiến lại.'),
 'a04':('Ông là Alvin Cross, một bệnh nhân cũ của Yalom. Người vợ nói rằng bà nợ Yalom cuộc hôn nhân của họ, và cả hai đứa con tuyệt vời.',
        'Anh giới thiệu mình là Alvin Cross, bệnh nhân cũ của tôi. Vợ anh nói rằng bà nợ tôi cuộc hôn nhân của họ, và cả hai đứa con tuyệt vời.'),
 'a05':('Nhưng Yalom hoàn toàn không nhớ Alvin là ai.',
        'Tôi mỉm cười, nhưng không sao nhớ nổi anh là ai.'),
 'a06':('Tối hôm đó, ông lục lại hồ sơ năm 1982. Một ca trị liệu mà ông từng tin rằng mình đã bỏ dở.',
        'Tối ấy, tôi tìm lại hồ sơ của Alvin, năm 1982. Một ca trị liệu mà tôi từng nghĩ mình đã bỏ dở.'),
 'b01':('Alvin là bác sĩ chẩn đoán hình ảnh tại Stanford.',
        'Alvin là bác sĩ chẩn đoán hình ảnh tại Stanford.'),
 'b02':('Một bài nói chuyện của Yalom khiến anh bắt đầu nghĩ đến những con người phía sau các tấm phim X-quang.',
        'Sau một buổi nói chuyện của tôi, anh bắt đầu nhìn thấy con người phía sau những tấm phim.'),
 'b03':('Nhưng còn một nguyên nhân sâu xa hơn: Jason, em trai anh, vừa qua đời.',
        'Rồi anh kể: em trai anh, Jason, vừa qua đời.'),
 'b04':('Hai anh em đã không liên lạc hơn mười lăm năm, từ khi Jason đính hôn trái ý gia đình và bỏ nhà đi cùng cô gái ấy.',
        'Hai anh em xa cách hơn mười lăm năm, từ khi Jason đính hôn trái ý gia đình và bỏ nhà đi cùng cô gái ấy.'),
 'b05':('Khi Jason mắc ung thư phổi, cậu gọi nhờ anh xem phim X-quang. Alvin bay đến, cố giúp đỡ và hàn gắn.',
        'Khi Jason mắc ung thư phổi, cậu gọi nhờ anh xem phim X-quang. Alvin bay đến thăm, cố nối lại tình thân.'),
 'b06':('Nhưng khoảng cách giữa họ vẫn còn đó. Không lâu sau, Jason qua đời.',
        'Nhưng họ vẫn không thể thực sự gần nhau. Không lâu sau, Jason qua đời.'),
 'b07':('Từ đó, những tấm phim X-quang trở thành nỗi ám ảnh của Alvin.',
        'Từ đó, mỗi tấm phim X-quang đều nhắc Alvin nhớ đến Jason.'),
 'b08':('Anh nhiều lần mơ thấy một con chim đen đuổi theo mình.',
        'Anh còn gặp ác mộng: một con chim đen đuổi theo anh trong bóng tối.'),
 'b09':('Qua trị liệu, Yalom nhận ra: nỗi đau vì những điều còn dang dở với Jason, cùng nỗi sợ cái chết, đang bủa vây anh.',
        'Tôi nhận ra nỗi đau ấy gắn với những điều còn dang dở, và cả nỗi sợ cái chết của chính anh.'),
 'b09a':('Mười năm trước, khi cha mẹ mất trong một tai nạn giao thông, Alvin mất ngủ suốt nhiều tuần, rồi dần hình thành thói quen thủ dâm để tìm giấc ngủ.',
        'Mười năm trước, khi cha mẹ mất trong một tai nạn giao thông, Alvin mất ngủ suốt nhiều tuần, rồi dần hình thành thói quen thủ dâm để dỗ giấc ngủ.'),
 'b10':('Sau nhiều buổi trị liệu, Alvin dần hồi phục. Ác mộng biến mất, anh lại có thể làm việc bình thường.',
        'Qua những buổi trị liệu, nỗi sợ dần dịu đi. Ác mộng biến mất, Alvin trở lại công việc bình thường.'),
 'b11':('Nhưng Yalom phát hiện một điều kỳ lạ: người đàn ông thành đạt ấy gần như sống hoàn toàn cô độc, không có lấy một mối quan hệ thân thiết.',
        'Nhưng tôi vẫn băn khoăn: một người tự tin, giỏi giang như anh, vì sao lại sống gần như hoàn toàn cô độc?'),
 'b12':('Khi Yalom hỏi sâu hơn, Alvin cuối cùng cũng thú nhận: những phụ nữ anh hẹn hò đều không quay lại sau khi đến nhà anh.',
        'Tôi tiếp tục hỏi về những mối quan hệ luôn kết thúc sớm. Cuối cùng, Alvin thú nhận: những phụ nữ anh hẹn hò đều rời đi sau khi đến nhà anh.'),
 'b13':('Yalom đề nghị buổi trị liệu tới diễn ra ngay tại nhà Alvin.',
        'Tôi đề nghị buổi trị liệu tới diễn ra ngay tại đó.'),
 'b13a':('Bảy giờ sáng hôm sau, Alvin gọi điện xin dừng trị liệu. Nhưng Yalom kiên nhẫn thuyết phục, và hẹn đến nhà anh ngay tối hôm đó.',
        'Bảy giờ sáng hôm sau, Alvin gọi điện xin dừng trị liệu. Nhưng tôi kiên nhẫn thuyết phục, và hẹn đến nhà anh ngay tối hôm đó.'),
 'b14':('Bước vào căn nhà, Yalom sững sờ. Danh bạ điện thoại cũ, báo ố vàng, sách vở, cả phim X-quang chất kín mọi nơi, chỉ còn những lối đi nhỏ.',
        'Tôi bước vào và sững sờ. Danh bạ điện thoại cũ, báo ố vàng, sách vở, cả phim X-quang chất kín nhà, chỉ còn những lối đi hẹp.'),
 'b15':('Alvin ngồi quay lưng, im lặng. Yalom cố tiếp cận, nhưng anh chỉ muốn dừng lại.',
        'Alvin ngồi quay lưng, im lặng. Tôi cố tiếp cận, nhưng anh chỉ muốn dừng lại.'),
 'c01':('Sáng hôm sau, Alvin gọi điện, xin kết thúc trị liệu. Anh nói sẽ tự sắp xếp lại ngôi nhà.',
        'Sáng hôm sau, Alvin gọi điện để kết thúc trị liệu. Anh nói sẽ tự sắp xếp lại ngôi nhà.'),
 'c02':('Yalom tự trách mình đã thúc ép anh quá mức. Suốt nhiều năm, ông vẫn xem đó là một ca trị liệu dang dở.',
        'Có phải tôi đã thúc ép anh quá mức? Nhiều năm sau, tôi vẫn xem đó là một ca trị liệu dang dở.'),
 'c03':('Hơn ba mươi năm sau, trong một quán cà phê, Yalom cuối cùng cũng tìm được lời giải.',
        'Giờ đây, ngồi cùng Alvin ở quán cà phê, tôi hỏi làm sao anh quen Molly.'),
 'c04':('Hóa ra, ngay sau buổi gặp cuối, chính ông đã giới thiệu Molly cho Alvin.',
        'Anh nhắc tôi: chính tôi đã giới thiệu bà, ngay sau buổi gặp cuối cùng.'),
 'c05':('Bà giúp anh dọn dẹp căn nhà, rồi suốt hơn ba mươi năm, mỗi tuần một lần, không hề sai hẹn, bà đến chăm lo cuộc sống của anh. Vậy mà Yalom đã hoàn toàn quên mất.',
        'Molly đến thu xếp lại căn nhà, rồi suốt hơn ba mươi năm, mỗi tuần một lần, không hề sai hẹn, bà chăm lo mọi việc cho anh. Vậy mà tôi đã quên mất.'),
 'c06':('Giờ đây, Alvin đang sống hạnh phúc bên vợ con.',
        'Giờ đây, anh đang sống hạnh phúc bên vợ con.'),
 'c08':('Cảm ơn bà, Molly.','Cảm ơn bà, Molly.'),
}

# id: [(ref, cue 3p, cue 1p, fallback, xf)]; the first shot of a line has no cue. M## are the new Flow images, S## the storyboard
# additions, R## redraws. xf = transition into the shot: 'cut', 'dissolve' or seconds (default: the 1.0 s crossfade).
S=lambda r,c3=None,c1=None,fb=None,xf=None:(r,c3,c1 if c1 is not None else c3,fb,xf)
AGED={'R06':'N16','R07':'N17','R08':'N18','R09':'B03','R10':'F22','R11':'N03','R12':'X10','R13':'R04',  # present-day redraws at ~80/~70/~60;
      'R14':'F20','R15':'X03','R16':'N04','R17':'N21'}  # same composition as the ref they replace, which stands in until drawn
A=lambda r,c3=None,c1=None,xf=None:S(r,c3,c1,AGED[r],xf)
SHOTS={
 'a01':[A('R17'),S('B02','tang lễ')],
 'a02':[S('X13'),S('N02','quyết đoán','Đôi khi')],  # N02 (Molly directing the tree crew, Yalom exasperated) holds through 'phát điên'
 'a03':[A('R11')],  # R10 (cemetery path) dropped 2026-10-11: no graves in the book's backyard memorial; re-add a backyard R10 when it passes
 'a04':[A('R12'),A('R13','Người vợ','Vợ anh nói')],  # R13 = backyard three-shot at the gate (9.0)
 'a05':[A('R14'),S('S19','Alvin là ai')],  # Yalom left puzzled, then the card insert on 'Alvin là ai' (storyboard score)
 'a06':[A('R15'),A('R16','hồ sơ'),S('N05','Một ca trị liệu'),S('S01','bỏ dở',xf=0.4)],
 'b01':[S('X01'),S('F10','bác sĩ chẩn đoán')],
 'b02':[S('B14'),S('X02','bắt đầu'),S('B15','phía sau')],
 'b03':[S('S15',fb='N06'),S('F19','Jason',xf='dissolve')],
 'b04':[S('M01',fb='B16'),S('S17','bỏ nhà đi')],
 'b05':[S('M02',fb='B18'),S('F34','xem phim X-quang'),S('N07','Alvin bay đến'),S('X07','cố giúp đỡ','nối lại')],
 'b06':[S('N08'),S('S20','Không lâu sau'),S('N09','Jason qua đời')],
 'b07':[S('R05',fb='F11'),S('X02','nỗi ám ảnh','nhắc Alvin')],
 'b08':[S('F27'),S('F28','đuổi theo')],
 'b09':[S('F14'),S('X04','nỗi sợ cái chết')],
 'b09a':[S('F26'),S('S13','mất ngủ')],
 'b10':[S('M04',fb='X05'),S('M03','Ác mộng biến mất'),S('F10','anh lại có thể','Alvin trở lại')],
 'b11':[S('N10'),S('N11','gần như sống','giỏi giang'),S('N12','không có lấy','vì sao')],
 'b12':[S('N06',xf=0.4),S('N13','những phụ nữ')],
 'b13':[S('R01',fb='F14')],
 'b13a':[S('S14',fb='M02'),S('S10','Nhưng Yalom','Nhưng tôi',fb='N15')],
 'b14':[S('F17',xf='cut'),S('R02','sững sờ',fb='B23'),S('R03','chỉ còn',fb='F25')],
 'b15':[S('N14'),S('S18','Yalom cố tiếp cận','Tôi cố tiếp cận',fb='R80')],  # R56 (back at the window, book) opens on 'ngồi quay lưng'
 'c01':[S('N15')],
 'c02':[S('S02'),S('M05','Suốt nhiều năm','Nhiều năm sau',xf=0.4)],
 'c03':[A('R06'),S('S07','cuối cùng','làm sao')],
 'c04':[A('R07'),S('S22','chính ông','chính tôi',fb='N15'),S('M06','Molly cho Alvin','ngay sau buổi gặp',fb='B22')],  # Yalom phones Alvin with Molly's name
 'c05':[S('S16'),S('M07','chăm lo'),A('R08','Vậy mà',xf='dissolve')],  # R08 (Yalom at the café window) instead of a repeat of R06 (art review 2026-10-11)
 'c06':[S('N19'),S('S11','bên vợ con',fb='R08',xf='dissolve')],
 'c08':[S('N01',xf='dissolve')],
}
SHOTS_1P={  # 1p lines whose sheet beats differ from 3p (replace the line's whole list, 1p cues only)
 'a05':[S('S08'),A('R14','không sao nhớ'),S('S19','anh là ai')],
 'b10':[S('F10'),S('M03','Ác mộng'),S('M04','Alvin trở lại',fb='X05')],
 'b11':[S('N10'),S('N11','giỏi giang'),S('S05','vì sao',fb='N12')],
}
NEW_CAM={  # scale0, scale1, x0, x1, y0, y1, ease (xPercent/yPercent, |x|,|y| <= (scale-1)*50)
 'M01':[1.10,1.16,0,0,2,-2,'sine.inOut'],'M02':[1.16,1.10,3,-3,0,0,'sine.inOut'],'M03':[1.08,1.16,0,0,-3,3,'sine.inOut'],
 'M04':[1.10,1.16,-3,3,0,0,'sine.inOut'],'M05':[1.16,1.08,0,0,3,-3,'sine.inOut'],'M06':[1.08,1.16,4,-3,0,0,'sine.inOut'],
 'M07':[1.16,1.10,-3,3,0,0,'sine.inOut'],'M08':[1.10,1.16,4,-4,0,0,'sine.inOut'],
 'N21':[1.08,1.16,3,-3,0,0,'sine.inOut'],
 'R01':[1.10,1.16,0,0,2,-2,'sine.inOut'],'R02':[1.08,1.16,0,0,-2,2,'sine.inOut'],'R03':[1.06,1.18,0,0,0,0,'sine.inOut'],
 'R04':[1.10,1.16,3,-3,0,0,'sine.inOut'],'R05':[1.10,1.16,0,0,-2,2,'sine.inOut'],'F01':[1.10,1.16,0,0,-3,3,'sine.inOut'],
 'S01':[1.06,1.14,0,0,2,-2,'sine.inOut'],'S05':[1.08,1.16,3,-3,0,0,'sine.inOut'],'S07':[1.06,1.16,2,-2,0,0,'sine.inOut'],
 'S08':[1.06,1.16,2,-2,0,0,'sine.inOut'],'S10':[1.10,1.16,0,0,2,-2,'sine.inOut'],
 'S11':[1.03,1.08,-1,1,0,0,'sine.inOut'],'S17':[1.06,1.14,2,-2,0,0,'sine.inOut'],'S13':[1.16,1.08,0,0,-3,3,'sine.inOut'],
 'S14':[1.08,1.16,3,-3,0,0,'sine.inOut'],'S15':[1.08,1.16,2,-2,0,0,'sine.inOut'],
 'S16':[1.04,1.12,0,0,0,0,'sine.inOut'],'S18':[1.06,1.14,-2,2,0,0,'sine.inOut'],'S19':[1.04,1.12,0,0,0,0,'sine.inOut'],'S22':[1.04,1.12,0,0,0,0,'sine.inOut'],'S23':[1.04,1.12,0,0,0,0,'sine.inOut'],
 'S20':[1.04,1.12,0,0,0,0,'sine.inOut'],
}
CROP={'F26':[0.27,0.06,0.81,0.60]}  # l,t,r,b of the image: F26's newspapers carry a near-legible masthead; keep the photo + blinds
SFX={'wind':[['a01',-0.8,1.0],['c08',-0.5,1.0]],'paper':[['a06',0,1.0]],'hum':[['b07',-0.5,1.0]],'raven':[['b08',0.8,1.0]],'clock':[['c01',0,1.0]]}
# hold_after: b04 a beat on Jason and his fiancée leaving (S17); b15 silence before the black; c06 silent hold on S11 (the realization is left to the live talk); c08 Molly under the end title
MOTION_F=os.path.join(P1,'script-src','molly-v2','MOTION.json')  # per-ref camera moves from the motion director
SCRIPT={'acts':[{'scene':'a01','label':'I · Cuộc hội ngộ bất ngờ'},{'scene':'b01','label':'II · Ca trị liệu dang dở'},{'scene':'c01','label':'III · Thank you, Molly'}],
 'file':{'scene':'a06','kicker':'Hồ sơ bệnh án · 1982','name':'Bác sĩ Alvin Cross'},
 'end':{'title':'THANK YOU, MOLLY','subtitle':'Theo lời kể của bác sĩ Irvin D. Yalom'},
 'hold_after':{'b04':1.2,'b15':1.5,'c06':5.0,'c08':6.0},'black_after':{'b15':1.0},
 'xf':0.6,'dissolve':1.2,'even_vo':True,'calm':1.0 if os.path.exists(MOTION_F) else 0.4}  # short crossfades; gentle camera (MOTION.json moves are already calm)

def merged(key):  # cam/fx from every earlier script in either project
  out={}
  for p in (P1,P3):
    d=os.path.join(p,'narration','scripts')
    for s in sorted(os.listdir(d)):
      f=os.path.join(d,s,'shots.json')
      if s!='molly-v2' and os.path.exists(f): out.update(json.load(open(f))[key])
  return out
CAM,FX=merged('cam'),merged('fx'); CAM.update(NEW_CAM); CAM['S02']=CAM['M05']  # S02 match-cuts into M05
NOFOG={'F22','F23','X10','B03','N03','F20','F15','R04','X12'}  # a01–a05 and the closing c08 are a sunny afternoon
FX={r:[e for e in v if not (r in NOFOG and e[0]=='fog')] for r,v in FX.items()}
for r,g in {'X12':'warm','F10':'cold','R05':'cold'}.items(): FX[r]=FX.get(r,[])+[[g]]  # grade: warm sunny close, cold Act 2 lightbox
FX.update({r:FX[o] for r,o in AGED.items() if o in FX})
CAM.update({r:CAM[o] for r,o in AGED.items()})
# library redraws that have landed (winners.json "replaces" + a PNG) swap in for the ref they replace, which becomes the fallback
WIN=json.load(open(os.path.join(P1,'script-src','molly-v2','ratings','winners.json')))
REPLACE={e['replaces']:e['shot'] for e in WIN if e.get('replaces') in CAM and any(os.path.exists(os.path.join(p,'assets','redraw',e['shot']+'.png')) for p in (P1,P3))}
CAM.update({n:CAM[o] for o,n in REPLACE.items() if n not in NEW_CAM}); FX.update({n:FX[o] for o,n in REPLACE.items() if o in FX})
FX={r:v for r,v in FX.items() if v}
# MOTION.json (the motion director's pick per ref) overrides the camera: one calm move from a small vocabulary per shot,
# aimed at a target point (fractions of the frame). Hero shots get a slightly larger move. |pan| stays <= (scale-1)*50.
def move(m):
  k=1.6 if m.get('hero') else 1.0; z=0.035*k; tx,ty=m.get('target') or [0.5,0.5]
  aim=lambda sc,t: max(-(sc-1)*50,min((sc-1)*50,(0.5-t)*100*(sc-1)))  # pan that brings point t toward the centre at scale sc
  e='sine.inOut'; mv=m['move']
  if mv=='still': return [1.02,1.02+0.008*k,0,0,0,0,e]
  if mv=='push': b=1+z+0.02; return [1.02,b,0,aim(b,tx),0,aim(b,ty),e]
  if mv=='pull': a=1+z+0.02; return [a,1.02,aim(a,tx),0,aim(a,ty),0,e]
  sc=1.03+0.01*k; p=(sc-1)*50*0.8
  if mv=='drift_left': return [sc,sc,p,-p,0,0,e]
  if mv=='drift_right': return [sc,sc,-p,p,0,0,e]
  if mv=='rise': return [sc,sc,0,0,p,-p,e]
  if mv=='fall': return [sc,sc,0,0,-p,p,e]
  raise SystemExit(f'unknown move {mv}')
MOTION=json.load(open(MOTION_F)) if os.path.exists(MOTION_F) else {}
CAM.update({r:move(m) for r,m in MOTION.items()})
refidx={}
for p in (P1,P3):
  for s in os.listdir(os.path.join(p,'narration','scripts')):
    f=os.path.join(p,'narration','scripts',s,'ref-index.txt')
    if os.path.exists(f): refidx.update(l.rstrip('\n').split(' ',1) for l in open(f) if l.strip())

for proj,k in ((P3,0),(P1,1)):
  sc=os.path.join(proj,'narration','scripts','molly-v2'); os.makedirs(sc,exist_ok=True)
  lines=[{'id':i,'text':t[k]} for i,t in LINES.items()]
  shots={}; used=set()
  for i in SHOTS:
    shots[i]=[]
    for j,(r,c3,c1,fb,xf) in enumerate(SHOTS_1P.get(i,SHOTS[i]) if k else SHOTS[i]):
      c=(c3,c1)[k]
      if r in REPLACE: r,fb=REPLACE[r],r
      elif fb in REPLACE: fb=REPLACE[fb]
      if j and c not in LINES[i][k]: raise SystemExit(f'{proj} {i}: cue "{c}" not in text')
      it={'ref':r}
      if j: it['cue']=c
      if fb: it['fallback']=fb; used.add(fb)
      if xf is not None: it['xf']=xf
      if r in CROP: it['crop']=CROP[r]
      shots[i].append(it); used.add(r)
  miss=[r for r in used if r not in CAM]
  if miss: raise SystemExit(f'no camera move for {miss}')
  json.dump(lines,open(os.path.join(sc,'lines.json'),'w'),ensure_ascii=False,indent=1)
  json.dump({'cam':{r:CAM[r] for r in sorted(used)},'fx':{r:FX[r] for r in sorted(used) if r in FX},'shots':shots,'sfx':SFX},
            open(os.path.join(sc,'shots.json'),'w'),ensure_ascii=False,indent=1)
  json.dump(SCRIPT,open(os.path.join(sc,'script.json'),'w'),ensure_ascii=False,indent=1)
  open(os.path.join(sc,'ref-index.txt'),'w').write(''.join(f'{r} {refidx[r]}\n' for r in sorted(used) if r in refidx))
  print(proj.split('/')[-1],'molly-v2:',len(lines),'lines,',sum(len(t[k].split()) for t in LINES.values()),'words,',len(used),'refs')
