"""Generate terminal-demo frames for the README GIFs — one set per language."""
import pathlib, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent

FRAMES = {
    "en": [
        ("Set up SEO for this site", "seo-geo-setup", "5 search engines + GEO (AI-search citations) + local SEO"),
        ("Make me a carousel", "carousel-generator", "research → branded design → PNG carousel"),
        ("Give me 4 thumbnails", "thumbnail-maker", "4 A/B variants · generated via Higgsfield"),
        ("Edit my webinar recording and publish it", "longform-to-content", "full edit + 4–8 Shorts + thumbnails + scheduling"),
        ("Boost this post", "paid-ads", "7 platforms · budget-approval gates · A/B creatives"),
        ("Marketing is so hard", "dans-advice", "diagnose → real prescriptions → one action for today"),
    ],
    "zh": [
        ("帮这个网站做 SEO", "seo-geo-setup", "5 大搜索引擎 + GEO（AI 搜索引用）+ 本地 SEO"),
        ("做一组轮播图", "carousel-generator", "调研 → 品牌化设计 → PNG 轮播"),
        ("出 4 张缩略图", "thumbnail-maker", "4 个 A/B 变体 · 经 Higgsfield 生成"),
        ("把研讨会录像剪辑后发布", "longform-to-content", "完整剪辑 + 4–8 条 Shorts + 缩略图 + 定时发布"),
        ("给这条帖子加热", "paid-ads", "7 大平台 · 预算审批门 · A/B 素材"),
        ("营销太难了", "dans-advice", "诊断 → 务实处方 → 今天就做的一件事"),
    ],
    "es": [
        ("Configura el SEO de este sitio", "seo-geo-setup", "5 buscadores + GEO (citas en búsqueda IA) + SEO local"),
        ("Hazme un carrusel", "carousel-generator", "investigación → diseño de marca → carrusel PNG"),
        ("Dame 4 miniaturas", "thumbnail-maker", "4 variantes A/B · vía Higgsfield"),
        ("Edita mi webinar y publícalo", "longform-to-content", "edición completa + 4–8 Shorts + programación"),
        ("Impulsa este post", "paid-ads", "7 plataformas · aprobación de presupuesto · creatividades A/B"),
        ("El marketing es muy difícil", "dans-advice", "diagnóstico → recetas reales → una acción para hoy"),
    ],
    "pt": [
        ("Configure o SEO deste site", "seo-geo-setup", "5 buscadores + GEO (citações em busca IA) + SEO local"),
        ("Faça um carrossel", "carousel-generator", "pesquisa → design de marca → carrossel PNG"),
        ("Me dê 4 thumbnails", "thumbnail-maker", "4 variações A/B · via Higgsfield"),
        ("Edite meu webinar e publique", "longform-to-content", "edição completa + 4–8 Shorts + agendamento"),
        ("Impulsione este post", "paid-ads", "7 plataformas · aprovação de orçamento · criativos A/B"),
        ("Marketing é muito difícil", "dans-advice", "diagnóstico → receitas reais → uma ação para hoje"),
    ],
    "ja": [
        ("このサイトのSEOをセットアップして", "seo-geo-setup", "検索エンジン5種 + GEO（AI検索の引用）+ ローカルSEO"),
        ("カルーセルを作って", "carousel-generator", "リサーチ → ブランドデザイン → PNGカルーセル"),
        ("サムネイルを4枚出して", "thumbnail-maker", "A/Bバリアント4種 · Higgsfield 生成"),
        ("ウェビナー録画を編集して公開して", "longform-to-content", "フル編集 + Shorts 4–8本 + 予約公開"),
        ("この投稿をブーストして", "paid-ads", "7プラットフォーム · 予算承認ゲート · A/Bクリエイティブ"),
        ("マーケティングが難しすぎる", "dans-advice", "診断 → 現実的な処方 → 今日やること1つ"),
    ],
    "ko": [
        ("이 사이트 SEO 세팅해줘", "seo-geo-setup", "검색엔진 5종 등록 + GEO (AI 검색 인용) + 로컬 SEO"),
        ("카드뉴스 만들어줘", "carousel-generator", "리서치 → 브랜드 디자인 → PNG 캐러셀"),
        ("썸네일 4개 뽑아줘", "thumbnail-maker", "A/B 변형 4종 · 힉스필드 생성"),
        ("웨비나 녹화 편집해서 올려줘", "longform-to-content", "풀편집 + 쇼츠 4–8개 + 썸네일 + 예약 발행"),
        ("이 포스트 부스트해줘", "paid-ads", "7개 플랫폼 · 예산 승인 게이트 · A/B creative"),
        ("마케팅 너무 어려워", "dans-advice", "진단 → 현실 처방 → 오늘 할 일 딱 하나"),
    ],
}

TPL = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable-dynamic-subset.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:800px;height:420px;overflow:hidden}}
body{{background:#FBF8F1;font-family:"Pretendard Variable",Pretendard,"Noto Sans","Noto Sans CJK SC","Noto Sans CJK JP",sans-serif;
     display:flex;align-items:center;justify-content:center}}
.term{{width:720px;height:340px;background:#14212B;border-radius:16px;
      box-shadow:0 18px 50px rgba(20,33,43,.18);padding:26px 30px;color:#F6F1E7}}
.bar{{display:flex;gap:8px;margin-bottom:24px}}
.bar i{{width:12px;height:12px;border-radius:50%;background:#2A3B49;display:block}}
.bar i:first-child{{background:#E8756A}}
.line{{font-size:21px;font-weight:600;letter-spacing:-0.01em}}
.prompt{{color:#E8756A;font-weight:800;margin-right:10px}}
.skill{{margin-top:26px;font-size:19px;color:#9FB2BE}}
.skill b{{color:#F6F1E7;font-weight:800}}
.check{{color:#7BC49A;font-weight:800;margin-right:8px}}
.desc{{margin-top:10px;font-size:16px;color:#8296A3}}
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
  <div class="count">AI + MARKETING KIT &middot; BY SUNDAYABLE</div>
  <div class="dots">{dots}</div>
</div>
</body></html>"""

total = 0
for lang, frames in FRAMES.items():
    for i, (prompt, skill, desc) in enumerate(frames):
        dots = "".join(f'<i class="{"on" if j == i else ""}"></i>' for j in range(len(frames)))
        (HERE / f"frame_{lang}_{i}.html").write_text(
            TPL.format(prompt=prompt, skill=skill, desc=desc, dots=dots), encoding="utf-8")
        total += 1
print(f"{total} frames written")
