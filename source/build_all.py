# -*- coding: utf-8 -*-
"""Bản HTML gộp: bộ QT tuần tự LGEC + các lưu đồ khác của Tập đoàn Long Giang (dạng artifact, không doctype)."""
import sys, os, json, base64, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lg_data, lgec_data
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "index.html")
LOGO_DIR = os.path.join(HERE, "assets")

# ---------- dữ liệu ----------
cat, f_other_all = lg_data.build()
_, f_lgec = lgec_data.build()
others = [f for f in f_other_all if not (f["code"].startswith("QLDA-LGEC") or f["code"].startswith("CUNGUNG"))]
flows = []
for f in f_lgec:
    flows.append(dict(f, group="lgec"))
_cnt = {}
for f in flows:
    pi = int(f["field"].split(".")[0])
    _cnt[pi] = _cnt.get(pi, 0) + 1
    f["no"] = "%s%d" % (chr(64 + pi), _cnt[pi])
    f["field"] = chr(64 + pi) + f["field"][f["field"].index("."):]
for f in flows:
    f.pop("wave", None) if f["group"] == "other" else None
    f["src"] = f.get("src") or ""
for f in f_lgec:
    pass
# nguồn của QT LGEC (Có trong danh mục / Đề xuất bổ sung) nằm trong trường wave cũ
by_code = {f["code"]: f for f in flows}
for f in f_lgec:
    by_code[f["code"]]["src"] = f["wave"]

CATMAP = {"QLDA-LGEC-01": "LGEC-09", "QLDA-LGEC-02": "LGEC-10", "QLDA-LGEC-03": "LGEC-11", "QLDA-LGEC-04": "LGEC-12",
          "QLDA-LGEC-05": "LGEC-15", "QLDA-LGEC-06": "LGEC-16", "QLDA-LGEC-07": "LGEC-06",
          "CUNGUNG-01": "LGEC-07", "CUNGUNG-02": "LGEC-08", "CUNGUNG-03": "LGEC-13"}
catalog = []
for c in cat:
    code = CATMAP.get(c["code"], c["code"])
    catalog.append(dict(stt=c["stt"], field=c["field"], code=c["code"], name=c["name"], flow=code if code in by_code else ""))


def logo(name, width):
    im = Image.open(name if name.endswith(".png") else os.path.join(LOGO_DIR, name + ".png")).convert("RGBA")
    im = im.crop(im.getbbox())
    h = round(im.height * width / im.width)
    im = im.resize((width, h), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


shutil_base = os.path.join(LOGO_DIR, "base.png")
logos = dict(base=logo(shutil_base, 360), lgg=logo("lgg", 360), lgec=logo("lgec", 300), lgl=logo("lgl", 300), ri=logo("ri", 300), rh=logo("rh", 300))
n_by = dict(LGEC=sum(1 for f in flows if f["unit"] == "LGEC"), LGL=sum(1 for f in flows if f["unit"] == "LGL"),
            RI=sum(1 for f in flows if f["unit"] == "RI"), LGG=sum(1 for f in flows if f["unit"] == "LGG"))
data = dict(flows=flows, catalog=catalog, logos=logos, nby=n_by,
            phases=[chr(65 + i) + p[1][p[1].index("."):] for i, p in enumerate(lgec_data.PHASES)])

TEMPLATE = r'''<title>Danh mục và lưu đồ QT Long Giang</title>
<style>
:root{
  --ink:#16233b; --muted:#566377; --line:#d7dde8; --bg:#f3f5f9; --card:#ffffff;
  --accent:#1f3d7a; --accent-soft:#e8edf7; --gold:#b58a3c; --gold-soft:#f6efe0;
  --amber:#7a4b00; --amber-soft:#fff4dc; --amber-line:#e3b45f; --back:#b4531a;
  --lane-a:#ffffff; --lane-b:#f7f9fc;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg)}
body{font-family:-apple-system,"Segoe UI","Helvetica Neue",Arial,sans-serif;color:var(--ink);font-size:14px;line-height:1.55}
button{font:inherit;cursor:pointer;color:inherit}
.app{display:grid;grid-template-columns:292px 1fr;min-height:100vh}
aside{background:#fff;border-right:1px solid var(--line);padding:18px 14px 28px;position:sticky;top:0;height:100vh;overflow:auto}
.brand{margin:0 6px 14px;padding-bottom:14px;border-bottom:1px solid var(--line)}
.brand{text-align:center}
.brand .pair{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:10px}
.brand .pair img{height:34px;width:auto}
.brand .pair img.bl{height:22px}
.brand .pair i{width:1px;height:28px;background:var(--line);flex:none}
.brand b{display:block;font-size:14px;line-height:1.3;color:var(--accent)}
.hero .pair{display:flex;align-items:center;gap:18px}
.hero .pair i{width:1px;height:44px;background:var(--line)}
.hero .pair img{height:52px;width:auto}
.hero .pair img.bl{height:34px}
.others{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-top:12px}
.orow{display:grid;grid-template-columns:210px 1fr;border-top:1px solid var(--line)}
.orow:first-child{border-top:0}
.orow .lab{background:var(--accent-soft);padding:12px 14px;display:flex;flex-direction:column;gap:6px;justify-content:center}
.orow .lab b{font-size:13px;color:var(--accent);line-height:1.3}
.orow .lab img{height:22px;width:auto;max-width:110px;object-fit:contain;object-position:left}
.orow .items{padding:10px;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;align-items:stretch}
.orow .items .qt{margin:0;height:100%}
@media(max-width:700px){.orow{grid-template-columns:1fr}}
.nav-home{display:block;width:100%;text-align:left;border:1px solid var(--line);background:#fff;border-radius:8px;padding:9px 12px;margin-bottom:12px;font-weight:700}
.nav-home.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.g1{background:var(--accent);color:#fff;font-weight:800;font-size:12px;letter-spacing:.03em;text-transform:uppercase;padding:8px 10px;border-radius:7px;margin:16px 0 6px;display:flex;justify-content:space-between;gap:8px}
.button.g1,button.g1{width:100%;border:0;text-align:left;font-family:inherit;cursor:pointer}
.g1.on{background:#142a57;box-shadow:inset 4px 0 0 var(--gold)}
.g1 small{font-weight:600;opacity:.8;text-transform:none;letter-spacing:0}
.g2{font-size:12.5px;font-weight:800;color:var(--accent);margin:12px 6px 3px;padding-left:9px;border-left:3px solid var(--gold);line-height:1.3}
.nav-item{display:flex;gap:8px;width:100%;text-align:left;border:0;background:none;padding:6px 8px;border-radius:7px;align-items:flex-start}
.nav-item:hover{background:var(--bg)}
.nav-item.on{background:var(--accent-soft);color:var(--accent);font-weight:700}
.nav-item .no{flex:none;min-width:32px;padding:0 4px;height:22px;border-radius:11px;background:var(--bg);font-size:11px;font-weight:700;display:grid;place-items:center;color:var(--muted);margin-top:1px}
.nav-item.on .no{background:var(--accent);color:#fff}
.nav-item span.t{font-size:13px;line-height:1.35}
main{padding:30px 36px 70px;min-width:0}
.crumb{font-size:12px;color:var(--muted);margin-bottom:6px;font-weight:600}
h2{font-size:28px;margin:0 0 6px;line-height:1.2;color:var(--accent);font-weight:800;letter-spacing:-.01em}
h3.sec{font-size:19px;font-weight:800;color:var(--accent);margin:0 0 6px;padding-left:12px;border-left:5px solid var(--gold);line-height:1.25}
h4.sub{font-size:13px;font-weight:800;color:var(--accent);margin:18px 0 8px;text-transform:uppercase;letter-spacing:.04em}
.top{display:flex;gap:14px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 0}
.chip{font-size:12px;padding:2px 10px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-weight:700}
.chip.gray{background:#eceff3;color:var(--muted)}
.chip.gold{background:var(--gold-soft);color:#7a5a1a}
.btns{display:flex;gap:8px;flex-wrap:wrap}
.btn{border:1px solid var(--line);background:#fff;border-radius:8px;padding:7px 12px;font-size:13px;font-weight:600}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 24px;margin-top:18px}
.p{color:var(--muted);margin:4px 0 8px;font-size:13.5px}
.small{font-size:12px;color:var(--muted);line-height:1.6}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px 26px}
.facts h4{margin:0 0 3px;font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--accent);font-weight:800}
.facts p{margin:0;font-size:13.5px}
.facts a{color:var(--accent);text-decoration:none;font-weight:600}
.facts a:hover{text-decoration:underline}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--muted);align-items:center;margin:16px 0 8px}
.legend i{display:inline-block;vertical-align:middle;margin-right:5px}
.lg-start{width:26px;height:14px;border-radius:999px;background:var(--ink)}
.lg-task{width:22px;height:14px;border:1.5px solid #9aa6b2;background:#fff;border-radius:4px}
.lg-dec{width:22px;height:14px;border:1.5px solid var(--amber-line);background:var(--amber-soft);border-radius:4px}
.lg-back{width:24px;border-top:2px dashed var(--back);height:0}
.flow-wrap{overflow:auto;border:1px solid var(--line);border-radius:12px;background:#fff}
.canvas{position:relative}
.lane{position:absolute;left:0;right:0;border-bottom:1px solid var(--line)}
.lane .lab{position:absolute;left:0;top:0;bottom:0;width:150px;padding:10px 12px;font-size:12.5px;font-weight:700;color:var(--accent);background:rgba(232,237,247,.8);border-right:1px solid var(--line);display:flex;align-items:center}
.lane .lab span{outline:none;display:block;width:100%}
svg.edges{position:absolute;left:0;top:0;pointer-events:none;z-index:1}
.node{position:absolute;z-index:2;width:156px;height:72px;display:flex;align-items:center;justify-content:center;text-align:center;padding:6px 10px;font-size:12px;line-height:1.3;border-radius:8px;background:#fff;border:1.5px solid #9aa6b2}
.node .tx{outline:none;max-height:100%;overflow:hidden;width:100%}
.node:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
.node.S,.node.E{background:var(--ink);color:#fff;border-color:var(--ink);border-radius:999px}
.node.D{background:var(--amber-soft);border-color:var(--amber-line);color:#4a2d00;font-weight:600}
.node .id{position:absolute;left:-9px;top:-9px;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#fff;font-size:10.5px;font-weight:700;display:grid;place-items:center;border:2px solid #fff}
.node.D .id{background:#b9770a}
.hint{font-size:12px;color:var(--muted);margin:8px 2px 0}
table{border-collapse:collapse;width:100%;font-size:13px}
th{background:var(--accent-soft);text-align:left;font-size:11.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--accent);font-weight:800;padding:9px 10px;border-bottom:1px solid var(--line);position:sticky;top:0}
td{padding:8px 10px;border-bottom:1px solid #edf0f4;vertical-align:top}
tr.fl{cursor:pointer}
tr.fl:hover td{background:#f6f8fc}
.tbl-wrap{overflow:auto;max-height:620px;border:1px solid var(--line);border-radius:10px;margin-top:10px}
/* tổ chức */
.hero{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-bottom:4px}
.hero img{height:64px;width:auto}
.org2{margin-top:16px}
.lggbox{display:flex;align-items:center;gap:20px;border:1px solid var(--line);border-radius:14px;padding:16px 22px;background:linear-gradient(180deg,#fff,#f5f7fc);max-width:760px;margin:0 auto}
.lggbox img{height:74px;width:auto;flex:none}
.lggbox b{display:block;font-size:16px;color:var(--accent)}
.lggbox p{margin:2px 0 0;font-size:12.5px;color:var(--muted)}
.members{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;position:relative;margin-top:30px;padding-top:0}
.members::before{content:"";position:absolute;top:-16px;left:12.5%;right:12.5%;border-top:2px solid var(--line)}
.lggbox::after{content:"";position:absolute}
.mem{position:relative;border:1px solid var(--line);border-radius:14px;background:#fff;padding:16px 14px 14px;text-align:center}
.mem::before{content:"";position:absolute;top:-16px;left:50%;height:16px;border-left:2px solid var(--line)}
.mem .lg{height:58px;display:flex;align-items:center;justify-content:center;margin-bottom:8px}
.mem .lg img{max-height:58px;max-width:78%;width:auto;height:auto}
.mem b{display:block;font-size:14px;color:var(--ink)}
.mem .role{display:block;font-size:12.5px;color:var(--muted);margin:3px 0 8px}
.mem .deps{font-size:11.5px;color:var(--muted);border-top:1px dashed var(--line);padding-top:8px;line-height:1.5}
.mem .cnt{display:inline-block;margin-top:9px;font-size:11.5px;font-weight:800;color:var(--accent);background:var(--accent-soft);padding:2px 10px;border-radius:999px}
.vchain{display:flex;flex-wrap:wrap;gap:0;margin-top:18px;border-radius:10px;overflow:hidden;border:1px solid var(--line)}
.vchain div{flex:1 1 150px;padding:9px 12px 9px 22px;font-size:12px;font-weight:700;color:var(--accent);background:var(--accent-soft);position:relative;line-height:1.35}
.vchain div small{display:block;font-weight:500;color:var(--muted)}
.vchain div:nth-child(even){background:#f1f4fa}
/* phase / chain */
.phases{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;margin-top:12px}
.ph{background:var(--bg);border-radius:10px;padding:10px}
.ph h4{margin:0 0 8px;font-size:12px;font-weight:800;color:var(--accent);line-height:1.3}
.qt{display:flex;gap:8px;align-items:flex-start;width:100%;text-align:left;border:1px solid var(--line);background:#fff;border-radius:8px;padding:7px 9px;margin-bottom:6px;font-size:12px;line-height:1.35}
.qt b{flex:none;font-size:11px;min-width:30px;padding:0 5px;height:20px;border-radius:10px;display:grid;place-items:center;background:var(--accent-soft);color:var(--accent)}
.qt.add b{background:var(--gold-soft);color:#7a5a1a}
.qt:hover{border-color:var(--accent)}
.chain{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:22px;margin-top:14px;counter-reset:st}
.chain .qt{position:relative;flex-direction:column;align-items:center;text-align:center;gap:8px;margin:0;padding:14px 8px 12px;height:100%;border-color:#cfd8ea;background:linear-gradient(180deg,#fff,#f5f7fc);font-size:12.5px;font-weight:600;color:var(--ink)}
.chain .qt b{min-width:40px;height:28px;border-radius:14px;font-size:13px;background:var(--accent);color:#fff}
.chain .qt:not(:last-child)::after{content:"";position:absolute;top:50%;right:-17px;width:12px;height:12px;border-top:2px solid var(--gold);border-right:2px solid var(--gold);transform:translateY(-50%) rotate(45deg)}
@media(max-width:1250px){.chain{grid-template-columns:repeat(4,minmax(0,1fr))}.chain .qt:nth-child(4)::after{display:none}}
@media(max-width:700px){.chain{grid-template-columns:repeat(2,minmax(0,1fr))}.chain .qt::after{display:none}}
.minis{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:8px;margin-top:8px}
.minis .qt{margin:0}
.minis .qt b{background:var(--accent-soft)}
.notice{border-left:4px solid var(--gold);background:var(--gold-soft);padding:10px 14px;border-radius:0 8px 8px 0;font-size:13px;color:#4a3a14;margin-top:14px}
.menu-btn{display:none}
@media (max-width:1100px){.members{grid-template-columns:1fr 1fr}.members::before,.mem::before{display:none}.phases{grid-template-columns:1fr 1fr}}
@media (max-width:900px){
  .app{grid-template-columns:1fr}
  aside{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);display:none}
  aside.open{display:block}
  .menu-btn{display:inline-block;margin:12px 16px 0}
  main{padding:18px 16px 50px}
  .phases,.members{grid-template-columns:1fr}
  .lggbox{flex-direction:column;text-align:center}
  h2{font-size:23px}
}
</style>
<button class="btn menu-btn" id="menuBtn">☰ Danh sách quy trình</button>
<div class="app">
  <aside id="side"></aside>
  <main id="main"></main>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('data').textContent);
const NODE_W=156, NODE_H=72, GAP=46, LAB_W=150, PAD_T=26, PAD_B=26, SUBGAP=18, LEFT=LAB_W+30;
const TYPE_NAME={S:'Bắt đầu',T:'Công việc',D:'Quyết định',E:'Kết thúc'};
const $=(s,r=document)=>r.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);
const flowOf={}; D.flows.forEach(f=>flowOf[f.code]=f);
const sname=f=>cap(f.name.replace(/^Quy trình /,''));
const nameOf=c=>flowOf[c]?sname(flowOf[c]):c;
const links=a=>a&&a.length?a.map(c=>`<a href="#${c}"><b>QT ${flowOf[c].no}</b> ${esc(nameOf(c))}</a>`).join('<br>'):'—';
let fitMode=false;
function applyFit(){
  const wrap=$('.flow-wrap'), cv=$('.canvas'); if(!wrap||!cv)return;
  let z=1; if(fitMode) z=Math.max(0.4,Math.min(1,(wrap.clientWidth-2)/cv.offsetWidth));
  cv.style.zoom=z; const b=$('#fitBtn'); if(b) b.textContent=fitMode?'Xem 100%':'Thu vừa khung';
}
window.addEventListener('resize',applyFit);
function fitText(el){let fs=12;el.style.fontSize=fs+'px';while(el.scrollHeight>el.clientHeight+1&&fs>9){fs-=0.5;el.style.fontSize=fs+'px';}}
function fitAll(){document.querySelectorAll('.node .tx').forEach(fitText);}

/* ---------- menu trái ---------- */
function renderSide(cur){
  let h=`<div class="brand"><div class="pair"><img src="${D.logos.lgg}" alt="Long Giang Group"><i></i><img src="${D.logos.base}" alt="Base.vn" class="bl"></div><b>Danh mục & lưu đồ QT số hóa</b></div>`;
  const item=f=>`<button class="nav-item ${cur===f.code?'on':''}" data-go="${f.code}"><span class="no">${f.no}</span><span class="t">${esc(sname(f))}</span></button>`;
  const lg=D.flows.filter(f=>f.group==='lgec');
  h+=`<button class="g1 ${cur==='home'?'on':''}" data-go="home"><span>Mảng thi công xây lắp</span><small>LGEC · ${lg.length} QT</small></button>`;
  D.phases.forEach(ph=>{h+=`<div class="g2">${esc(ph)}</div>`+lg.filter(f=>f.field===ph).map(item).join('');});
  $('#side').innerHTML=h;
  $('#side').querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>{go(b.dataset.go);$('#side').classList.remove('open')});
}
$('#menuBtn').onclick=()=>$('#side').classList.toggle('open');
function go(code){location.hash=code==='home'?'':code;}
window.addEventListener('hashchange',route);
function route(){
  const code=decodeURIComponent(location.hash.slice(1));
  window.scrollTo(0,0);
  if(code && flowOf[code]){renderSide(code);renderFlow(flowOf[code]);}
  else{renderSide('home');renderHome();}
}

/* ---------- tổng quan ---------- */
function renderHome(){
  const L=D.logos, nb=D.nby;
  const lg=D.flows.filter(f=>f.group==='lgec');
  const phases=D.phases.map(ph=>({name:ph,items:lg.filter(f=>f.field===ph)}));
  const cols=phases.map(p=>`<div class="ph"><h4>${esc(p.name)}</h4>${p.items.map(f=>`<button class="qt ${f.src==='Có trong danh mục'?'':'add'}" data-go="${f.code}"><b>${f.no}</b><span>${esc(sname(f))}</span></button>`).join('')}</div>`).join('');
  const spine=[['LGEC-04','Lập tiến độ gốc (baseline)'],['LGEC-07','Đặt hàng theo tiến độ'],['LGEC-08','Cấp vật tư kịp thời'],['LGEC-09','Theo dõi tuần, bù tiến độ'],['LGEC-10','Nghiệm thu hạng mục'],['LGEC-14','Phát sinh đổi baseline'],['LGEC-15','Thanh toán theo khối lượng đạt']];
  const chain=spine.map(([c,t])=>`<button class="qt" data-go="${c}"><b>${flowOf[c].no}</b><span>${t}</span></button>`).join('');
  $('#main').innerHTML=`
  <div class="hero"><div class="pair"><img src="${L.lgg}" alt="Long Giang Group"><i></i><img class="bl" src="${L.base}" alt="Base.vn"></div><div>
    <h2>Danh mục quy trình và lưu đồ đề xuất số hóa</h2></div></div>
  <p class="p">Bản này vẽ lưu đồ trọn bộ ${D.flows.length} quy trình tuần tự của mảng thi công xây lắp (Long Giang E&C) để hình dung cách vận hành.</p>
  <div class="notice"><b>Bản tham khảo để trao đổi.</b> Các bước, vai trò và hạn mức phê duyệt là đề xuất ban đầu, cần Long Giang xác nhận. Việc quy trình nào số hóa trước sẽ cùng trao đổi và chốt với khách hàng. Bấm vào chữ trong khung ở từng lưu đồ để sửa thử; bản lưu chính thức nằm trong file Google Sheet.</div>

  <div class="card">
    <h3 class="sec">Mảng thi công xây lắp: bộ quy trình tuần tự (Long Giang E&C)</h3>
    <p class="p">${lg.length} quy trình sắp theo vòng đời một công trình, từ nhận thầu đến bảo hành. Quản lý tiến độ là trục chính xuyên suốt.</p>
    <h4 class="sub">Tiến độ nối các quy trình với nhau như thế nào</h4>
    <p class="p">Tiến độ gốc được duyệt ở QT ${flowOf['LGEC-04'].no}, sau đó các quy trình bên dưới đều bám theo mốc này. Mỗi trang quy trình có mục "Liên hệ tiến độ".</p>
    <div class="chain">${chain}</div>
    <h4 class="sub">Trình tự theo vòng đời công trình</h4>
    <div class="phases">${cols}</div>
    <p class="small" style="margin-top:8px">Giai đoạn C chạy lặp hằng ngày, hằng tuần trong suốt thời gian thi công; các giai đoạn còn lại chạy một lần cho mỗi công trình hoặc hợp đồng. Khung màu vàng đồng là quy trình đề xuất bổ sung, chưa có trong danh mục Basework.</p>
  </div>

  <p class="small" style="margin-top:18px"><b>Ghi chú.</b> Bộ quy trình mảng thi công ghép từ 10 quy trình LGEC đã có trong danh mục, vòng đời tiêu chuẩn của một công trình và danh mục đơn vị của Long Giang; không có danh mục chuẩn công khai cho tổng thầu D&B. Các căn cứ pháp luật về chất lượng, nghiệm thu, bảo hành, thầu phụ chưa đưa vào lưu đồ và cần đối chiếu văn bản hiện hành cùng hợp đồng thi công trước khi chốt thời hạn, ngưỡng phê duyệt.</p>`;
  $('#main').querySelectorAll('[data-go]').forEach(r=>r.onclick=()=>go(r.dataset.go));
}

/* ---------- lưu đồ ---------- */
function layout(f){
  const steps=f.steps, by={}; steps.forEach(s=>by[s.id]=s);
  const state={}, back=new Set();
  (function(){
    function dfs(id){state[id]=1;by[id].next.forEach(e=>{const k=id+'>'+e.to; if(!by[e.to])return; if(state[e.to]===1)back.add(k); else if(!state[e.to])dfs(e.to);});state[id]=2;}
    dfs(steps[0].id); steps.forEach(s=>{if(!state[s.id])dfs(s.id)});
  })();
  const col={}; steps.forEach(s=>col[s.id]=0);
  for(let i=0;i<steps.length+3;i++) steps.forEach(s=>s.next.forEach(e=>{
    if(by[e.to] && !back.has(s.id+'>'+e.to)) col[e.to]=Math.max(col[e.to],col[s.id]+1);
  }));
  const cell={}, sub={};
  steps.forEach(s=>{const k=s.lane+'|'+col[s.id]; cell[k]=(cell[k]||0); sub[s.id]=cell[k]++;});
  const rows=f.lanes.map(()=>1);
  steps.forEach(s=>{rows[s.lane]=Math.max(rows[s.lane],sub[s.id]+1)});
  const laneTop=[], laneH=[]; let y=0;
  f.lanes.forEach((_,i)=>{const h=PAD_T+PAD_B+rows[i]*NODE_H+(rows[i]-1)*SUBGAP; laneTop[i]=y; laneH[i]=h; y+=h;});
  const maxCol=Math.max(...steps.map(s=>col[s.id]));
  const W=LEFT+(maxCol+1)*(NODE_W+GAP)+10, H=y;
  const pos={};
  steps.forEach(s=>{pos[s.id]={x:LEFT+col[s.id]*(NODE_W+GAP), y:laneTop[s.lane]+PAD_T+sub[s.id]*(NODE_H+SUBGAP), lane:s.lane};});
  return {by,back,col,pos,laneTop,laneH,W,H};
}
function edgesSvg(f,L){
  const {by,back,pos,W,H}=L; let out=`<defs>
  <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#6b7785"/></marker>
  <marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#b4531a"/></marker></defs>`;
  let bk=0; const labels=[];
  f.steps.forEach(s=>s.next.forEach(e=>{
    const t=by[e.to]; if(!t)return;
    const a=pos[s.id], b=pos[t.id]; const isBack=back.has(s.id+'>'+e.to);
    let d, lx, ly, anchor='middle';
    if(!isBack){
      const x1=a.x+NODE_W, y1=a.y+NODE_H/2, x2=b.x, y2=b.y+NODE_H/2;
      if(Math.abs(y1-y2)<1){d=`M${x1} ${y1}H${x2-1}`; lx=(x1+x2)/2; ly=y1-6;}
      else{const xm=x2-18; d=`M${x1} ${y1}H${xm}V${y2}H${x2-1}`; lx=xm-4; ly=(y1+y2)/2+3; anchor='end';}
      out+=`<path d="${d}" fill="none" stroke="#6b7785" stroke-width="1.4" marker-end="url(#ar)"/>`;
    }else{
      const k=bk++, off=(k%3)*7;
      let x1=a.x+NODE_W/2+off-7, x2=b.x+NODE_W/2+off-7, y1,y2,rail;
      if(b.lane<a.lane){y1=a.y; rail=y1-12-(k%3)*4; y2=b.y+NODE_H;}
      else if(b.lane>a.lane){y1=a.y+NODE_H; rail=y1+12+(k%3)*4; y2=b.y;}
      else{y1=a.y+NODE_H; rail=y1+12+(k%3)*4; y2=b.y+NODE_H;}
      d=`M${x1} ${y1}V${rail}H${x2}V${y2}`;
      out+=`<path d="${d}" fill="none" stroke="#b4531a" stroke-width="1.4" stroke-dasharray="5 4" marker-end="url(#arb)"/>`;
      lx=Math.min(x1,x2)+6; ly=rail-4; anchor='start';
      if(!e.label){e={...e,label:'quay lại'};}
    }
    if(e.label) labels.push([lx,ly,e.label,anchor,isBack]);
  }));
  labels.forEach(([x,y,t,an,bkk])=>{
    const w=t.length*5.8+8;
    const rx=an==='middle'?x-w/2:an==='end'?x-w:x;
    out+=`<rect x="${rx}" y="${y-10}" width="${w}" height="14" rx="3" fill="#fff" opacity=".92"/><text x="${x+(an==='middle'?0:an==='end'?-4:4)}" y="${y}" text-anchor="${an}" font-size="10.5" font-weight="600" fill="${bkk?'#b4531a':'#4a5666'}">${esc(t)}</text>`;
  });
  return `<svg class="edges" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${out}</svg>`;
}
function renderFlow(f){
  const L=layout(f);
  let lanes='';
  f.lanes.forEach((n,i)=>{lanes+=`<div class="lane" style="top:${L.laneTop[i]}px;height:${L.laneH[i]}px;background:${i%2?'var(--lane-b)':'var(--lane-a)'}"><div class="lab"><span contenteditable="true" spellcheck="false" data-lane="${i}">${esc(n)}</span></div></div>`;});
  let nodes='';
  f.steps.forEach(s=>{const p=L.pos[s.id];
    nodes+=`<div class="node ${s.type}" style="left:${p.x}px;top:${p.y}px" title="${TYPE_NAME[s.type]}"><span class="id">${s.id}</span><div class="tx" contenteditable="true" spellcheck="false" data-step="${s.id}">${esc(s.text)}</div></div>`;});
  const isL=f.group==='lgec';
  const unitLogo=({LGL:'lgl',LGEC:'lgec',RI:'ri',LGG:'lgg'})[f.unit];
  const extra=isL?`
    <div><h4>Liên hệ tiến độ</h4><p>${esc(f.prog)}</p></div>
    <div><h4>Nhận đầu vào từ</h4><p>${links(f.frm)}</p></div>
    <div><h4>Chuyển kết quả sang</h4><p>${links(f.to)}</p></div>`:'';
  $('#main').innerHTML=`
  <div class="top"><div>
    <div class="crumb">${esc(f.field)}</div>
    <h2>${esc(f.name)}</h2>
    <div class="chips"><span class="chip gray">QT ${f.no}</span>${isL?`<span class="chip ${f.src==='Có trong danh mục'?'gray':'gold'}">${esc(f.src)}</span>`:''}<span class="chip gray">${f.steps.length} bước · ${f.lanes.length} vai trò</span></div>
  </div>
  <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">${unitLogo?`<img src="${D.logos[unitLogo]}" alt="" style="height:40px;width:auto">`:''}<div class="btns"><button class="btn" id="prev">← Trước</button><button class="btn" id="next">Sau →</button><button class="btn" id="fitBtn">Thu vừa khung</button></div></div></div>
  <div class="card"><div class="facts">
    <div><h4>Mục tiêu</h4><p>${esc(f.goal)}</p></div>
    <div><h4>Đầu vào</h4><p>${esc(f.inp)}</p></div>
    <div><h4>Đầu ra</h4><p>${esc(f.out)}</p></div>${extra}
    <div><h4>Ứng dụng Base gợi ý</h4><p>${esc(f.app)}</p></div>
  </div></div>
  <div class="legend"><span><i class="lg-start"></i>Bắt đầu / kết thúc</span><span><i class="lg-task"></i>Công việc</span><span><i class="lg-dec"></i>Quyết định (rẽ nhánh)</span><span><i class="lg-back"></i>Quay lại bước trước</span></div>
  <div class="flow-wrap"><div class="canvas" style="width:${L.W}px;height:${L.H}px">${lanes}${edgesSvg(f,L)}${nodes}</div></div>
  <p class="hint">Bấm vào chữ trong khung hoặc tên làn để sửa thử. Chỉnh sửa trên trang chỉ giữ trong phiên xem này; muốn lưu lại, thêm hoặc bớt bước, đổi luồng thì sửa trong file Google Sheet đi kèm.</p>
  <div class="card"><h3 class="sec">Diễn giải từng bước</h3><div class="tbl-wrap" style="max-height:none"><table id="stepTbl"></table></div></div>`;
  fillTable(f); fitAll();
  $('#main').querySelectorAll('[data-step]').forEach(el=>{
    el.addEventListener('input',()=>fitText(el));
    el.addEventListener('blur',()=>{f.steps.find(s=>s.id===el.dataset.step).text=el.textContent.trim();fillTable(f);});
    el.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();el.blur();}});
  });
  $('#main').querySelectorAll('[data-lane]').forEach(el=>{
    el.addEventListener('blur',()=>{f.lanes[+el.dataset.lane]=el.textContent.trim();fillTable(f);});
    el.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();el.blur();}});
  });
  const idx=D.flows.indexOf(f);
  $('#prev').onclick=()=>go(D.flows[(idx+D.flows.length-1)%D.flows.length].code);
  $('#next').onclick=()=>go(D.flows[(idx+1)%D.flows.length].code);
  $('#fitBtn').onclick=()=>{fitMode=!fitMode;applyFit();};
  applyFit();
}
function fillTable(f){
  const nxt=s=>s.next.length?s.next.map(n=>`<b>${n.to}</b>${n.label?` <span style="color:var(--muted)">(${esc(n.label)})</span>`:''}`).join(' · '):'—';
  $('#stepTbl').innerHTML='<thead><tr><th>Bước</th><th>Người thực hiện</th><th>Loại</th><th>Nội dung</th><th>Tiếp theo</th><th>Thời hạn</th><th>Biểu mẫu / ghi chú</th></tr></thead><tbody>'+
   f.steps.map(s=>`<tr><td><b>${s.id}</b></td><td>${esc(f.lanes[s.lane])}</td><td>${TYPE_NAME[s.type]}</td><td>${esc(s.text)}</td><td>${nxt(s)}</td><td>${esc(s.sla||'')}</td><td>${esc(s.note||'')}</td></tr>`).join('')+'</tbody>';
}
route();
</script>
'''

html = TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
# bọc thêm doctype/charset/viewport để mở trực tiếp trên trình duyệt hoặc đưa lên GitHub Pages
html = '<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n' + html + '\n</html>\n'
open(OUT, "w", encoding="utf-8").write(html)
print("OK", os.path.normpath(OUT), len(html) // 1024, "KB", len(flows), "flows")
