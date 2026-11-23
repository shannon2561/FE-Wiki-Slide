"""將 src/slides.src.html 組裝為 index.html（單頁瀏覽、鍵盤換頁、KaTeX 公式、Wiki 出處連結）。"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WIKI_URL = 'https://github.com/shannon2561/FE-Wiki-Slide/blob/main/finance-wiki/'
WIKI_DIR = os.path.join(ROOT, '..', 'finance-wiki')

def wiki_link(slug):
    for sub in ('concepts', 'sources'):
        p = os.path.join(WIKI_DIR, sub, slug + '.md')
        if os.path.exists(p):
            title = open(p, encoding='utf-8').readline().lstrip('# ').strip()
            title = re.sub(r'（.*$|：.*$', '', title) if sub == 'concepts' else re.sub(r'^.*講義 (\d+)：.*$', r'講義 \1', title)
            return f'<a href="{WIKI_URL}{sub}/{slug}.md" target="_blank" rel="noopener">{title}</a>'
    return f'<a href="{WIKI_URL}index.md" target="_blank" rel="noopener">Wiki 總索引</a>'

C = '#2F5D50'; A = '#C8742B'; G = '#8A948F'
FIG = {
'payoff': f'''<svg viewBox="0 0 420 210" role="img" aria-label="買進買權的到期淨損益圖">
<line x1="40" y1="150" x2="405" y2="150" stroke="{G}"/><line x1="60" y1="15" x2="60" y2="185" stroke="{G}"/>
<text x="404" y="143" text-anchor="end" font-size="13" fill="{G}">到期股價（元）</text><text x="66" y="24" font-size="13" fill="{G}">每股淨損益（元）</text>
<polyline points="60,165 230,165 390,45" fill="none" stroke="{C}" stroke-width="3"/>
<line x1="230" y1="150" x2="230" y2="170" stroke="{G}" stroke-dasharray="3"/><text x="230" y="186" text-anchor="middle" font-size="13">100</text>
<text x="350" y="186" text-anchor="middle" font-size="13">115</text><line x1="350" y1="150" x2="350" y2="75" stroke="{A}" stroke-dasharray="3"/>
<circle cx="350" cy="75" r="4" fill="{A}"/><text x="342" y="66" text-anchor="end" font-size="13" fill="{A}">股價 115：100 股淨賺 1,000</text>
<text x="66" y="182" font-size="13" fill="{C}">最多損失權利金 5</text></svg>''',
'tree1': f'''<svg viewBox="0 0 420 170" role="img" aria-label="一期二元樹">
<line x1="90" y1="85" x2="300" y2="35" stroke="{G}" stroke-width="2"/><line x1="90" y1="85" x2="300" y2="135" stroke="{G}" stroke-width="2"/>
<circle cx="90" cy="85" r="30" fill="{C}"/><text x="90" y="81" text-anchor="middle" fill="#fff" font-size="13">股價 20</text><text x="90" y="98" text-anchor="middle" fill="#fff" font-size="12">買權 ?</text>
<circle cx="300" cy="35" r="30" fill="#fff" stroke="{C}" stroke-width="2"/><text x="300" y="31" text-anchor="middle" font-size="13">22</text><text x="300" y="48" text-anchor="middle" font-size="12" fill="{A}">買權 1</text>
<circle cx="300" cy="135" r="30" fill="#fff" stroke="{C}" stroke-width="2"/><text x="300" y="131" text-anchor="middle" font-size="13">18</text><text x="300" y="148" text-anchor="middle" font-size="12" fill="{A}">買權 0</text>
<text x="200" y="165" text-anchor="middle" font-size="12" fill="{G}">今天 → 3 個月後</text></svg>''',
'tree2': f'''<svg viewBox="0 0 460 215" role="img" aria-label="二期二元樹">
<g stroke="{G}" stroke-width="2"><line x1="70" y1="95" x2="220" y2="50"/><line x1="70" y1="95" x2="220" y2="140"/><line x1="220" y1="50" x2="380" y2="20"/><line x1="220" y1="50" x2="380" y2="95"/><line x1="220" y1="140" x2="380" y2="95"/><line x1="220" y1="140" x2="380" y2="170"/></g>
<g font-size="14" text-anchor="middle">
<rect x="28" y="70" width="84" height="50" rx="8" fill="{C}"/><text x="70" y="91" fill="#fff">20</text><text x="70" y="110" fill="#fff">1.2823</text>
<rect x="178" y="25" width="84" height="50" rx="8" fill="#fff" stroke="{C}"/><text x="220" y="46">22</text><text x="220" y="65" fill="{A}">2.0257</text>
<rect x="178" y="115" width="84" height="50" rx="8" fill="#fff" stroke="{C}"/><text x="220" y="136">18</text><text x="220" y="155" fill="{A}">0</text>
<rect x="342" y="0" width="76" height="42" rx="8" fill="#fff" stroke="{G}"/><text x="380" y="17">24.2</text><text x="380" y="35" fill="{A}">3.2</text>
<rect x="342" y="74" width="76" height="42" rx="8" fill="#fff" stroke="{G}"/><text x="380" y="91">19.8</text><text x="380" y="109" fill="{A}">0</text>
<rect x="342" y="149" width="76" height="42" rx="8" fill="#fff" stroke="{G}"/><text x="380" y="166">16.2</text><text x="380" y="184" fill="{A}">0</text></g>
<text x="230" y="210" text-anchor="middle" font-size="13" fill="{G}">每格上方為股價，下方（橘色）為買權價值；今天 → 3 個月 → 6 個月</text></svg>''',
}
# 常態分配曲線（d2 = 0.15 附近陰影）
import math
pts = [(x/10, math.exp(-(x/10)**2/2)) for x in range(-35, 36)]
path = ' '.join(f'{210+px*50:.1f},{150-py*120:.1f}' for px, py in pts)
shade = ' '.join(f'{210+px*50:.1f},{150-py*120:.1f}' for px, py in pts if px <= 0.15)
FIG['normal'] = f'''<svg viewBox="0 0 420 180" role="img" aria-label="標準常態分配與累積機率"><text x="330" y="60" font-size="12" fill="#66706C">鐘形曲線＝標準常態分配</text>
<polygon points="35,150 {shade} 217.5,150" fill="{A}" opacity="0.35"/>
<polyline points="{path}" fill="none" stroke="{C}" stroke-width="2.5"/><line x1="20" y1="150" x2="400" y2="150" stroke="{G}"/>
<line x1="217.5" y1="150" x2="217.5" y2="20" stroke="{A}" stroke-dasharray="3"/><text x="224" y="18" font-size="13" fill="{A}">d₂ = 0.15</text>
<text x="120" y="135" font-size="13" fill="#5a3a12">面積 = N(d₂) = 0.5596</text><text x="210" y="168" text-anchor="middle" font-size="12" fill="{G}">0</text></svg>'''

src = open(os.path.join(ROOT, 'src', 'slides.src.html'), encoding='utf-8').read()
sections = re.findall(r'<section data-id="([^"]+)" data-wiki="([^"]*)" data-defines="[^"]*"([^>]*)>(.*?)</section>', src, re.S)
out = []
for sid, wiki, attrs, body in sections:
    body = re.sub(r'<figure data-fig="(\w+)"></figure>', lambda m: f'<figure class="fig">{FIG[m.group(1)]}</figure>', body)
    links = '、'.join(wiki_link(w) for w in wiki.split(',') if w)
    cls = 'slide appendix' if 'appendix' in attrs else ('slide cover' if sid == '1' else 'slide')
    out.append(f'<section class="{cls}" id="s{sid}" data-id="{sid}">\n<div class="content">{body}</div>\n<footer class="src">Wiki：{links}</footer>\n</section>')
html = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read().replace('<!--SLIDES-->', '\n'.join(out))
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html 完成，共', len(out), '頁')
