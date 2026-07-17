"""Generate terminal-demo frames for the README GIF."""
import pathlib, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent

FRAMES = [
    ("이 사이트 SEO 세팅해줘", "seo-geo-setup", "검색엔진 5종 등록 + GEO (AI 검색 인용) + 로컬 SEO"),
    ("카드뉴스 만들어줘", "card-news-generator", "리서치 → 브랜드 디자인 → PNG 캐러셀"),
    ("썸네일 4개 뽑아줘", "thumbnail-maker", "A/B 변형 4종 · gpt-image-2 / Nano Banana"),
    ("웨비나 녹화 편집해서 올려줘", "longform-to-content", "풀편집 + 쇼츠 4–8개 + 썸네일 + 예약 발행"),
    ("이 포스트 부스트해줘", "zernio-ads", "7개 플랫폼 · 예산 승인 게이트 · A/B creative"),
    ("마케팅 너무 어려워", "dans-advice", "진단 → 현실 처방 → 오늘 할 일 딱 하나"),
]

TPL = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable-dynamic-subset.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:800px;height:420px;overflow:hidden}}
body{{background:#FBF8F1;font-family:"Pretendard Variable",Pretendard,sans-serif;
     display:flex;align-items:center;justify-content:center}}
.term{{width:720px;height:340px;background:#14212B;border-radius:16px;
      box-shadow:0 18px 50px rgba(20,33,43,.18);padding:26px 30px;color:#F6F1E7}}
.bar{{display:flex;gap:8px;margin-bottom:24px}}
.bar i{{width:12px;height:12px;border-radius:50%;background:#2A3B49;display:block}}
.bar i:first-child{{background:#E8756A}}
.line{{font-size:22px;font-weight:600;letter-spacing:-0.01em}}
.prompt{{color:#E8756A;font-weight:800;margin-right:10px}}
.skill{{margin-top:26px;font-size:19px;color:#9FB2BE}}
.skill b{{color:#F6F1E7;font-weight:800}}
.check{{color:#7BC49A;font-weight:800;margin-right:8px}}
.desc{{margin-top:10px;font-size:17px;color:#8296A3}}
.count{{margin-top:34px;font-size:14px;letter-spacing:.22em;color:#5A6E7C;font-weight:700}}
.dots{{display:flex;gap:7px;margin-top:12px}}
.dots i{{width:8px;height:8px;border-radius:50%;background:#2A3B49;display:block}}
.dots i.on{{background:#E8756A}}
</style></head><body>
<div class="term">
  <div class="bar"><i></i><i></i><i></i></div>
  <div class="line"><span class="prompt">&gt;</span>"{prompt}"</div>
  <div class="skill"><span class="check">&#10003;</span><b>{skill}</b> activated</div>
  <div class="desc">{desc}</div>
  <div class="count">AI + MARKETING KIT &middot; 24 SKILLS</div>
  <div class="dots">{dots}</div>
</div>
</body></html>"""

for i, (prompt, skill, desc) in enumerate(FRAMES):
    dots = "".join(f'<i class="{"on" if j == i else ""}"></i>' for j in range(len(FRAMES)))
    (HERE / f"frame_{i}.html").write_text(
        TPL.format(prompt=prompt, skill=skill, desc=desc, dots=dots), encoding="utf-8")
print(f"{len(FRAMES)} frames written")
