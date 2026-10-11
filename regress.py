"""Test regresyjny Mini-trans: python3 regress.py [plik.html]
Uruchamia 3 tryby gry, scenariusz Test (hasło w grze; tu startTest() bezpośrednio) i zapisy save_*.txt z tego katalogu.
Wymaga: pip install playwright (Chromium)."""
import sys,glob,os,time
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__))
V="file://"+os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(D,"index.html"))
def page(b):
    pg=b.new_page(viewport={'width':1000,'height':800});errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto(V);pg.wait_for_timeout(1500);return pg,errs
bad=0
with sync_playwright() as p:
    b=p.chromium.launch()
    for mode in ["operator","manager","classic"]:
        pg,errs=page(b);pg.evaluate(f"()=>{{GAME.pname='Test';startMode('{mode}')}}");t=time.time()
        for d in range(4):pg.evaluate("()=>{for(let i=0;i<1440*2;i++)simTick(0.5);if(typeof jobsFlush==='function')jobsFlush();EV.queue&&(EV.queue.length=0);}")
        print(mode,round(time.time()-t,1),"s",errs[:4]);bad+=len(errs);pg.close()
    pg,errs=page(b);pg.evaluate("()=>{startTest();EV.queue.length=0;}")
    for m in range(2):pg.evaluate("()=>{EV.queue.length=0;for(let i=0;i<1440*2;i++)simTick(0.5);}")
    print("test",errs[:3]);bad+=len(errs);pg.close()
    for f in sorted(glob.glob(os.path.join(D,"save_*.txt"))):
        pg,errs=page(b);s=open(f).read()
        r=pg.evaluate("async (s)=>{const d=await parseSave(s);loadSaveData(d.data||d);for(let i=0;i<1440*2;i++)simTick(0.5);return {lines:lines.length,stuck:trains.filter(t=>!t.inDepot&&(t.stuck||0)>60).length}}",s)
        print(os.path.basename(f),r,errs[:3]);bad+=len(errs);pg.close()
    b.close()
print("BŁĘDY:",bad);sys.exit(1 if bad else 0)
