(()=>{
const field=document.querySelector('.physics-field');if(!field||!window.Matter)return;
const config={gravity:1,restitution:.25,friction:.35,frictionAir:.025,spawnInterval:120,coreDesktop:60,coreMobile:42};
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
const {Engine,Bodies,Body,Composite,Constraint,Sleeping}=Matter;
const engine=Engine.create({enableSleeping:true});engine.gravity.y=config.gravity;engine.positionIterations=8;
let width=field.clientWidth,height=field.clientHeight,walls=[],items=[],frame=0,last=0,acc=0,visible=true,drag=null,timers=[];
function boundaries(){Composite.remove(engine.world,walls);walls=[Bodies.rectangle(width/2,height+45,width+200,100,{isStatic:true}),Bodies.rectangle(-50,height/2,100,height+800,{isStatic:true}),Bodies.rectangle(width+50,height/2,100,height+800,{isStatic:true}),Bodies.rectangle(width/2,-350,width+200,100,{isStatic:true})];Composite.add(engine.world,walls);}
function measure(){width=field.clientWidth;height=field.clientHeight;boundaries();for(const item of items){item.w=item.el.offsetWidth;item.h=item.el.offsetHeight;const next=Math.min(width<700?config.coreMobile:config.coreDesktop,item.h*.85);const factor=next/item.core;Body.scale(item.body,factor,factor);item.core=next;Body.setPosition(item.body,{x:Math.max(item.w/2,Math.min(width-item.w/2,item.body.position.x)),y:Math.min(height-item.h/2,item.body.position.y)});}}
boundaries();
function render(){for(const item of items){const {x,y}=item.body.position;item.el.style.transform=`translate3d(${x-item.w/2}px,${y-item.h/2}px,0) rotate(${item.body.angle}rad)`;}}
function release(){if(!drag)return;Composite.remove(engine.world,drag.joint);const b=drag.item.body;Body.setVelocity(b,{x:Math.max(-18,Math.min(18,drag.vx)),y:Math.max(-22,Math.min(22,drag.vy))});Sleeping.set(b,false);drag.item.el.classList.remove('dragging');drag=null;}
[...field.children].forEach((el,i)=>{el.style.visibility='hidden';timers.push(setTimeout(()=>{const w=el.offsetWidth,h=el.offsetHeight,core=Math.min(width<700?config.coreMobile:config.coreDesktop,h*.85);const body=Bodies.rectangle(Math.max(w/2,Math.min(width-w/2,width*(.15+Math.random()*.7))),-70,core,core,{chamfer:{radius:5},density:.002,friction:config.friction,frictionStatic:.5,frictionAir:config.frictionAir,restitution:config.restitution,sleepThreshold:80});Body.setAngle(body,(Math.random()-.5)*1.4);const item={el,body,w,h,core};items.push(item);Composite.add(engine.world,body);el.style.visibility='';
el.addEventListener('pointerdown',e=>{if(e.pointerType==='mouse'&&e.button!==0)return;e.preventDefault();release();const r=field.getBoundingClientRect(),p={x:e.clientX-r.left,y:e.clientY-r.top};Sleeping.set(body,false);const joint=Constraint.create({bodyA:body,pointA:{x:p.x-body.position.x,y:p.y-body.position.y},pointB:p,length:0,stiffness:.18,damping:.18});Composite.add(engine.world,joint);drag={item,joint,x:p.x,y:p.y,t:performance.now(),vx:0,vy:0};el.classList.add('dragging');el.setPointerCapture(e.pointerId);});
el.addEventListener('pointermove',e=>{if(!drag||drag.item!==item)return;const r=field.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top,t=performance.now(),dt=Math.max(8,t-drag.t);drag.vx=(x-drag.x)/dt*16.667;drag.vy=(y-drag.y)/dt*16.667;drag.x=x;drag.y=y;drag.t=t;drag.joint.pointB={x,y};Sleeping.set(body,false);});
for(const event of ['pointerup','pointercancel','lostpointercapture'])el.addEventListener(event,()=>{if(drag?.item===item){if(performance.now()-drag.t>100)drag.vx=drag.vy=0;release();}});
el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();Sleeping.set(body,false);Body.setVelocity(body,{x:(Math.random()-.5)*5,y:-10});}});
},i*config.spawnInterval));});
function tick(t){if(visible){acc+=Math.min(50,last?t-last:16.667);while(acc>=16.667){Engine.update(engine,16.667);acc-=16.667;}render();}last=t;frame=requestAnimationFrame(tick);}frame=requestAnimationFrame(tick);
const resize=new ResizeObserver(measure);resize.observe(field);
const observer=new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;last=0;acc=0;});observer.observe(field);
addEventListener('pagehide',()=>{cancelAnimationFrame(frame);timers.forEach(clearTimeout);release();resize.disconnect();observer.disconnect();Composite.clear(engine.world,false);Engine.clear(engine);},{once:true});
})();
