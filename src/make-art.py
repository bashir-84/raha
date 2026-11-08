from pathlib import Path
import math
out=Path('public/assets');out.mkdir(parents=True,exist_ok=True)
def save(name,body,bg='#f6f2e9'):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="840" viewBox="0 0 1440 840"><defs><filter id="shadow" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="18" stdDeviation="20" flood-opacity=".16"/></filter><pattern id="grain" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="1" cy="2" r=".6" fill="#000" opacity=".08"/></pattern></defs><rect width="1440" height="840" fill="{bg}"/>{body}<rect width="1440" height="840" fill="url(#grain)" opacity=".3"/></svg>'
 (out/name).write_text(s)
def text(x,y,s,size=30,color='#282822',extra=''):
 return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" fill="{color}" {extra}>{s}</text>'
def sun(x,y,r,c,center=None):
 b=''
 for i in range(12):
  a=i*math.pi/6;cx=x+math.cos(a)*r*.67;cy=y+math.sin(a)*r*.67
  b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{r*.23}" ry="{r*.6}" fill="{c}" transform="rotate({i*30-90} {cx} {cy})"/>'
 b+=f'<circle cx="{x}" cy="{y}" r="{r*.47}" fill="{c}"/>'
 if center:b+=f'<circle cx="{x}" cy="{y}" r="{r*.24}" fill="{center}"/>'
 return b
# Sol: a deliberately art-directed campaign with poster, vinyl and ticket.
for n in range(1,4):
 if n==1:
  b='<path d="M0 675L1440 575V840H0Z" fill="#d8493c"/>'
  b+='<g transform="translate(150 65) rotate(-8 240 320)" filter="url(#shadow)"><rect width="490" height="690" fill="#ffc7d8"/>'
  b+=text(35,57,'A FESTIVAL FOR FEELING GOOD.',14,'#7c2633', 'letter-spacing="3"')+text(25,245,'sol',235,'#df4a35','font-weight="900" letter-spacing="-24"')
  b+=sun(248,440,158,'#ef5a35','#ffdc52')+text(35,644,'SOUND. SUN. TOGETHER.',20,'#7c2633')+text(35,671,'21—23 JUNE  /  CONCEPT EDITION',12,'#7c2633')+'</g>'
  b+='<g transform="translate(750 260) rotate(8 220 220)" filter="url(#shadow)"><rect x="-20" y="-20" width="480" height="480" fill="#ffe255"/><circle cx="220" cy="220" r="220" fill="#2c2927"/>'
  for r in range(100,215,10):b+=f'<circle cx="220" cy="220" r="{r}" stroke="#46423d" fill="none"/>'
  b+='<circle cx="220" cy="220" r="87" fill="#ef5a35"/>'+text(167,245,'sol',70,'#ffe255','font-weight="900" letter-spacing="-6"')+'<circle cx="220" cy="220" r="7" fill="#ffe255"/></g>'
  b+='<g transform="translate(925 70) rotate(10)"><rect width="320" height="145" rx="8" fill="#f7edb8"/>'+text(20,35,'YOUR GOOD-ENERGY PASS',12)+text(20,100,'sol / 01',55,'#d8493c','font-weight="700"')+'<path d="M265 5v135" stroke="#d8493c" stroke-dasharray="4 5"/></g>'
  save('sol-1.svg',b,'#f3694e')
 elif n==2:
  b=''
  for i,(c,ink) in enumerate([('#ffe255','#d64735'),('#a8c6ed','#3a48a4'),('#ffc7d8','#dc4938')]):
   x=70+i*440;b+=f'<g transform="translate({x} 65) rotate({[-4,2,-3][i]} 190 345)"><rect width="410" height="700" fill="{c}"/>'+text(25,80,'COME',66,ink,'font-weight="900"')+text(25,150,'AS YOU',66,ink,'font-weight="900"')+text(25,220,'ARE.',66,ink,'font-weight="900"')+sun(200,420,140,ink,c)+text(25,660,'sol / MUSIC &amp; CULTURE',17,ink)+'</g>'
  save('sol-2.svg',b,'#df5942')
 else:
  b=text(65,90,'THE GOOD-ENERGY TOOLKIT',20,'#7b2634','letter-spacing="5"')+text(50,340,'sol',290,'#e34b36','font-weight="900" letter-spacing="-25"')
  b+=sun(1050,270,180,'#e34b36','#ffdc52')
  for i,c in enumerate(['#e34b36','#ffdc52','#ffc7d8','#a8c6ed','#7b2634']):b+=f'<rect x="{65+i*265}" y="490" width="245" height="205" rx="15" fill="{c}"/>'
  b+=text(65,765,'LOUD TYPE. WARM COLOURS. OPEN ARMS.',24,'#7b2634')
  save('sol-3.svg',b,'#f4b5c8')
# Forma: abstract botanical product packaging with shadows and leaf forms.
for n in range(1,4):
 b=''
 if n==1:
  b+='<ellipse cx="725" cy="745" rx="560" ry="48" fill="#4f663f" opacity=".13"/>'
  for i,(x,y,w,h,c,label) in enumerate([(215,160,275,540,'#f1eacd','01 / DAILY WASH'),(610,290,245,410,'#a9bf7a','02 / HAND BALM'),(955,125,245,570,'#eff0d0','03 / BODY OIL')]):
   b+=f'<g transform="rotate({[-6,5,8][i]} {x+w/2} {y+h/2})" filter="url(#shadow)"><rect x="{x+30}" y="{y-55}" width="{w-60}" height="90" rx="13" fill="#344c35"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="35" fill="{c}"/>'
   b+=text(x+24,y+105,'forma',65,'#344c35','font-weight="700" letter-spacing="-5"')
   b+=f'<path d="M{x+w/2} {y+165}c-150-80-140 180 0 200c130-60 130-260 0-200Z" fill="#57734c"/><path d="M{x+w/2} {y+190}v190" stroke="{c}" stroke-width="3"/>'
   b+=text(x+25,y+h-55,label,13,'#344c35')+text(x+25,y+h-30,'BOTANICAL ESSENTIALS / 250 ML',10,'#344c35')+'</g>'
  save('forma-1.svg',b,'#c6d1a2')
 elif n==2:
  b+='<rect x="130" y="100" width="500" height="640" fill="#f1eacd" transform="rotate(-7 380 420)" filter="url(#shadow)"/>'+text(175,260,'forma',110,'#344c35','font-weight="700" letter-spacing="-8"')+text(180,660,'GOOD BY NATURE.',25,'#344c35')
  b+='<path d="M390 340C120 260 140 580 390 610C630 470 600 250 390 340Z" fill="#57734c"/>'
  b+='<g transform="translate(780 240) rotate(7)"><rect width="430" height="330" fill="#344c35" filter="url(#shadow)"/>'+text(30,90,'a little',48,'#dbe88b')+text(30,150,'closer to',48,'#dbe88b')+text(30,210,'nature.',48,'#dbe88b')+'</g>'
  save('forma-2.svg',b,'#dce2bf')
 else:
  b+=text(80,160,'Less, but',110,'#344c35','font-weight="700" letter-spacing="-7"')+text(80,280,'lovelier.',110,'#344c35','font-weight="700" letter-spacing="-7"')
  for i,c in enumerate(['#344c35','#57734c','#a9bf7a','#f1eacd']):b+=f'<circle cx="{175+i*275}" cy="590" r="100" fill="{c}"/>'
  b+='<path d="M1130 60c-400 20-240 350 0 340c240-120 180-370 0-340Z" fill="#57734c"/>'
  save('forma-3.svg',b,'#dbe88b')
# Orbit: a rendered desktop interface and matching mobile device.
for n in range(1,4):
 b=''
 if n==1:
  b+='<g transform="translate(115 75) rotate(-3 540 320)" filter="url(#shadow)"><rect width="1080" height="660" rx="18" fill="#f7f5fc"/><rect width="1080" height="43" rx="18" fill="#edeaf4"/><circle cx="23" cy="22" r="5" fill="#c6b5f5"/><circle cx="42" cy="22" r="5" fill="#d2d8bb"/><circle cx="61" cy="22" r="5" fill="#e7c3d2"/>'+text(455,28,'orbit — your creative space',12,'#6a6379')+'<path d="M200 44v616" stroke="#ded9e8"/>'
  b+=text(25,100,'orbit',38,'#493a66','font-weight="700" letter-spacing="-2"')+text(25,175,'⌕  Search',16,'#746c82')+text(25,225,'◉  My space',16,'#493a66')+text(25,272,'▦  Collections',16,'#746c82')+text(25,320,'♡  Inspiration',16,'#746c82')+text(245,120,'A little space to think.',38,'#493a66','font-weight="700" letter-spacing="-2"')+text(245,152,'Catch an idea. See where it takes you.',14,'#746c82')
  for i,(x,y,w,h,c) in enumerate([(245,195,330,210,'#e6d983'),(595,195,410,210,'#d4c4ef'),(245,425,410,185,'#cadbd2'),(675,425,330,185,'#edd0d9')]):
   b+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{c}"/>'
   if i==0:b+=text(x+25,y+65,'Today’s',40,'#493a66','font-weight="700"')+text(x+25,y+110,'little idea.',40,'#493a66','font-weight="700"')
   elif i==1:b+=f'<ellipse cx="{x+205}" cy="{y+100}" rx="140" ry="55" fill="none" stroke="#7655ad" stroke-width="18" transform="rotate(-25 {x+205} {y+100})"/><circle cx="{x+205}" cy="{y+100}" r="55" fill="#b198dc"/>'
   else:b+=text(x+25,y+60,['','','Make room for','A fresh'][i],32,'#493a66','font-weight="700"')+text(x+25,y+105,['','','something new.','perspective.'][i],32,'#493a66','font-weight="700"')
  b+='</g><g transform="translate(1110 315) rotate(8)" filter="url(#shadow)"><rect width="230" height="440" rx="33" fill="#352d45"/><rect x="9" y="10" width="212" height="420" rx="27" fill="#f7f5fc"/><rect x="75" y="20" width="80" height="20" rx="10" fill="#352d45"/>'+text(28,95,'orbit',32,'#493a66','font-weight="700"')+'<rect x="24" y="125" width="182" height="165" rx="12" fill="#d4c4ef"/>'+text(40,185,'Your next',27,'#493a66','font-weight="700"')+text(40,222,'big thing.',27,'#493a66','font-weight="700"')+'<rect x="24" y="310" width="182" height="65" rx="12" fill="#e6d983"/>'+text(43,350,'Start somewhere ↗',16,'#493a66')+'</g>'
  save('orbit-1.svg',b,'#b29bdf')
 elif n==2:
  for i,(c,title) in enumerate([('#e6d983','Catch it.'),('#cadbd2','Collect it.'),('#d4c4ef','Create it.')]):
   x=190+i*375;b+=f'<g transform="translate({x} 90) rotate({[-5,0,5][i]})" filter="url(#shadow)"><rect width="300" height="640" rx="45" fill="#352d45"/><rect x="11" y="11" width="278" height="618" rx="36" fill="#f7f5fc"/><rect x="100" y="23" width="100" height="25" rx="12" fill="#352d45"/>'+text(30,110,'orbit',35,'#493a66','font-weight="700"')+f'<rect x="25" y="145" width="250" height="300" rx="18" fill="{c}"/>'+text(40,245,title,46,'#493a66','font-weight="700"')+text(30,510,'A little idea,',23,'#493a66')+text(30,545,'a whole new world.',23,'#493a66')+'</g>'
  save('orbit-2.svg',b,'#c6b5f5')
 else:
  b+=text(80,150,'Everything',115,'#493a66','font-weight="700" letter-spacing="-7"')+text(80,275,'in its orbit.',115,'#493a66','font-weight="700" letter-spacing="-7"')
  for i in range(3):b+=f'<ellipse cx="1050" cy="420" rx="270" ry="100" fill="none" stroke="{["#7655ad","#e6d983","#f7f5fc"][i]}" stroke-width="25" transform="rotate({i*60-30} 1050 420)"/>'
  b+='<circle cx="1050" cy="420" r="90" fill="#7655ad"/>'+text(80,710,'SAVE A THOUGHT. START A WORLD.',24,'#493a66','letter-spacing="3"')
  save('orbit-3.svg',b,'#c6b5f5')
# Slow Good: tactile editorial layouts and magazine covers.
for n in range(1,4):
 if n==1:
  b='<g transform="translate(190 80) rotate(-9 260 340)" filter="url(#shadow)"><rect width="510" height="685" fill="#f2eacb"/>'+text(27,95,'slow',105,'#1e5264','font-weight="900" letter-spacing="-8"')+text(27,185,'good',105,'#1e5264','font-weight="900" letter-spacing="-8"')+text(30,230,'AN EVERYDAY KIND OF WONDER',13,'#1e5264','letter-spacing="2"')+'<path d="M30 330Q255 190 480 330L480 610Q255 480 30 610Z" fill="#86c4df"/><circle cx="255" cy="405" r="100" fill="#e77553"/><path d="M30 490Q255 355 480 490V610Q255 480 30 610Z" fill="#1e5264"/>'+text(30,654,'ISSUE 01 / ORDINARY MAGIC',14,'#1e5264')+'</g>'
  b+='<g transform="translate(765 150) rotate(7 220 280)" filter="url(#shadow)"><rect width="450" height="570" fill="#1e5264"/>'+text(30,70,'TAKE',78,'#f2eacb','font-weight="700"')+text(30,150,'YOUR',78,'#f2eacb','font-weight="700"')+text(30,230,'TIME.',78,'#f2eacb','font-weight="700"')+sun(220,380,120,'#86c4df','#e77553')+text(30,535,'A SMALL REMINDER FROM SLOW GOOD',11,'#f2eacb')+'</g>'
  save('slow-good-1.svg',b,'#78b8d2')
 elif n==2:
  b='<g transform="translate(130 105) rotate(-3 590 315)" filter="url(#shadow)"><rect width="1180" height="630" fill="#f2eacb"/><path d="M590 0v630" stroke="#c7bea3" stroke-width="4"/>'+text(50,100,'The art of',70,'#1e5264','font-weight="700"')+text(50,180,'noticing.',70,'#1e5264','font-weight="700"')
  for y in range(260,530,23):b+=f'<rect x="55" y="{y}" width="{400 if y%2 else 430}" height="3" fill="#1e5264" opacity=".4"/>'
  b+='<rect x="640" y="50" width="490" height="500" fill="#86c4df"/><circle cx="885" cy="290" r="155" fill="#e77553"/><path d="M640 400Q885 240 1130 400v150H640Z" fill="#1e5264"/>'+text(55,595,'SLOW GOOD / 014',12,'#1e5264')+text(1020,595,'015',12,'#1e5264')+'</g>'
  save('slow-good-2.svg',b,'#9dc7d2')
 else:
  b=text(70,150,'Ordinary things.',110,'#1e5264','font-weight="700" letter-spacing="-7"')+text(70,280,'Extraordinary feeling.',100,'#1e5264','font-weight="700" letter-spacing="-6"')
  for i,c in enumerate(['#f2eacb','#e77553','#1e5264']):
   x=100+i*435;b+=f'<rect x="{x}" y="390" width="360" height="350" rx="180" fill="{c}"/>'
  b+=sun(280,565,110,'#86c4df')+sun(715,565,110,'#f2eacb')+sun(1150,565,110,'#86c4df')
  save('slow-good-3.svg',b,'#86c4df')
# Purposefully illustrated placeholder, not an invented person's photograph.
p='<rect width="1440" height="840" fill="#e5dba8"/><circle cx="720" cy="450" r="330" fill="#f2b59a"/><path d="M370 840Q370 590 720 590Q1070 590 1070 840" fill="#596b54"/><rect x="655" y="495" width="130" height="150" rx="55" fill="#b77954"/><ellipse cx="720" cy="390" rx="175" ry="205" fill="#c68b64"/><path d="M540 380Q490 150 710 145Q945 130 905 400L850 260Q710 330 570 265Z" fill="#35352d"/><circle cx="650" cy="380" r="12" fill="#35352d"/><circle cx="785" cy="380" r="12" fill="#35352d"/><path d="M655 472Q720 525 785 472" fill="none" stroke="#35352d" stroke-width="10" stroke-linecap="round"/>'+sun(1110,210,100,'#ef7357','#e5dba8')+text(140,730,'just a',45,'#35352d','transform="rotate(-10 140 730)"')+text(150,785,'placeholder :)',45,'#35352d','transform="rotate(-10 150 785)"')
save('portrait.svg',p)
(out/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#f27054"/><text x="25" y="77" fill="#282822" font-family="Arial" font-size="85" font-weight="bold">r</text></svg>')
print('Generated 12 project illustrations, placeholder portrait, and favicon.')
