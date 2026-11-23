"""逐頁檢查簡報原稿 src/slides.src.html。
A 出處：data-wiki 列出的頁面皆存在於 Wiki
B 術語順序：術語首次出現的頁碼不得早於定義頁，除非該頁寫明「第 N 頁」指向定義頁
C 獨立可讀：每頁有完整句子的導言 (lead)，且正文字數足夠
D 符號說明：公式中的每個符號都列在同頁的符號說明
E 數字：頁面上的數字可在對應的 Wiki 頁面中找到
F 風格：不使用第一人稱、破折號與誇大用語
G 基礎名詞：簡報出現的基礎名詞，須在同頁或前面的頁面連到對應的 Wiki 基礎知識頁
用法：python tools/check_slides.py
"""
import html, os, re, sys

WIKI = os.path.join(os.path.dirname(__file__), '..', '..', 'finance-wiki')
SRC = os.path.join(os.path.dirname(__file__), '..', 'src', 'slides.src.html')
src = open(SRC, encoding='utf-8').read()
slides = re.findall(r'<section data-id="([^"]+)" data-wiki="([^"]*)" data-defines="([^"]*)"[^>]*>(.*?)</section>', src, re.S)

def wiki_text(slug):
    for sub in ('concepts', 'sources', 'projects', 'people'):
        p = os.path.join(WIKI, sub, slug + '.md')
        if os.path.exists(p):
            return open(p, encoding='utf-8').read()
    p = os.path.join(WIKI, slug + '.md')
    return open(p, encoding='utf-8').read() if os.path.exists(p) else None

def plain(body, keep_math=False):
    b = re.sub(r'<dl class="sym">.*?</dl>', ' ', body, flags=re.S)
    if not keep_math:
        b = re.sub(r'<(span|div) class="m[d]?">.*?</\1>', ' ', b, flags=re.S)
    b = re.sub(r'<[^>]+>', ' ', b)
    return html.unescape(b)

def math_tokens(tex):
    tex = re.sub(r'\\text\{[^}]*\}', ' ', tex)
    tex = re.sub(r'\\(frac|sqrt|left|right|max|ln|Pr|cdot|times|qquad|quad|partial|int|infty|pi|,|;|!|%)', ' ', tex)
    toks = set()
    for m in re.finditer(r'\\(sigma|mu|Delta|tau|beta)|\b(d[Stzwxyf])(?![A-Za-z])|([A-Za-z])(_\{[^}]+\}|_[A-Za-z0-9]|\^\{?[A-Z]\}?)?', tex):
        if m.group(1): toks.add('\\' + m.group(1))
        elif m.group(2): toks.add(m.group(2))
        else:
            t = m.group(3) + (m.group(4) or '')
            toks.add(t.replace('{', '').replace('}', ''))
    return toks

order = [s[0] for s in slides]
main = [s for s in slides if s[0].isdigit()]
define_at = {}
for sid, _, defines, _ in main:
    for t in [x for x in defines.split(',') if x]:
        define_at[t] = int(sid)

BASICS = {
    '機率': 'probability-expected-value', '期望值': 'probability-expected-value', '標準差': 'probability-expected-value',
    '變異數': 'probability-expected-value', '測度': 'probability-expected-value',
    '常態分配': 'normal-distribution', '累積機率': 'normal-distribution',
    '折現': 'discounting-continuous-compounding', '現值': 'discounting-continuous-compounding', '連續複利': 'discounting-continuous-compounding',
    '套利': 'no-arbitrage', '偏微分': 'calculus-basics', '積分': 'calculus-basics', '微分': 'calculus-basics',
    '自然對數': 'logarithm-exponential', '報酬': 'return-rate', '年化': 'return-rate',
}
cited_upto = {}
seen = set()
for sid, wiki, _, _ in slides:
    seen |= set(w for w in wiki.split(',') if w)
    cited_upto[sid] = set(seen)

results = {}
for sid, wiki, defines, body in slides:
    fails = []
    # A
    refs = [w for w in wiki.split(',') if w]
    texts = []
    for w in refs:
        t = wiki_text(w)
        if t is None: fails.append(f'A 出處：Wiki 沒有 {w} 這一頁')
        else: texts.append(t)
    if not refs: fails.append('A 出處：沒有標註 Wiki 頁面')
    wtext = re.sub(r'(?<=\d),(?=\d{3})', '', '\n'.join(texts))
    text = plain(body)
    # B
    if sid.isdigit() and sid != '1':  # 封面為全篇預告，不檢查術語順序
        n = int(sid)
        for term, at in define_at.items():
            if at > n and term in text and f'第 {at} 頁' not in text:
                fails.append(f'B 術語：「{term}」在第 {n} 頁出現，但第 {at} 頁才定義')
    # C
    lead = re.search(r'<p class="lead">(.*?)</p>', body, re.S)
    if not lead or not plain(lead.group(1)).strip().endswith('。'):
        fails.append('C 可讀：缺少完整句子的導言')
    if sid not in ('1',) and len(re.findall(r'[\u4e00-\u9fff]', text)) < 60:
        fails.append('C 可讀：正文太少，沒有講解可能看不懂')
    # D
    syms = set()
    for dt in re.findall(r'<dt>(.*?)</dt>', body, re.S):
        for m in re.findall(r'<span class="m">(.*?)</span>', dt, re.S):
            syms |= math_tokens(html.unescape(m))
    used = set()
    body_wo_dl = re.sub(r'<dl class="sym">.*?</dl>', ' ', body, flags=re.S)
    for m in re.findall(r'<(?:span|div) class="m[d]?">(.*?)</(?:span|div)>', body_wo_dl, re.S):
        used |= math_tokens(html.unescape(m))
    missing = sorted(used - syms)
    if missing:
        fails.append('D 符號：同頁沒有說明 ' + '、'.join(missing))
    # E
    nums_text = re.sub(r'第 \d+ (?:至 \d+ )?頁|第 \d+、\d+ 頁|附錄 [A-D]', ' ', plain(body, keep_math=True))
    nums_text = re.sub(r'(?<=\d),(?=\d{3})', '', nums_text)
    for num in sorted(set(re.findall(r'\d+(?:\.\d+)?', nums_text))):
        if re.fullmatch(r'\d', num): continue
        if num not in wtext:
            fails.append(f'E 數字：{num} 在對應的 Wiki 頁面中找不到')
    # F
    for pat, why in [(r'我', '第一人稱'), (r'——|—', '破折號'), (r'本研究|本報告|本文', '「本研究」類用語'),
                     (r'非常|超級|賦能|打造|深度|全方位|關鍵在於', '誇大用語'), (r'不是[^。]{0,20}而是', '「不是……而是」')]:
        if re.search(pat, text): fails.append(f'F 風格：{why}')
    # G（封面為全篇預告，不檢查）
    text_g = plain(body) + ' ' + ' '.join(re.findall(r'<dd>(.*?)</dd>', body, re.S))
    for term, page in BASICS.items():
        if sid != '1' and term in text_g and page not in cited_upto[sid]:
            fails.append(f'G 基礎名詞：「{term}」出現在此頁，但此頁與前面的頁面都沒有連到 {page}')
    results[sid] = fails

bad = 0
for sid in order:
    f = results[sid]
    label = f'第 {sid} 頁' if sid.isdigit() else f'附錄 {sid}'
    print(f'{label}：' + ('通過' if not f else '未通過'))
    for x in f: print('   - ' + x)
    bad += bool(f)
print(f'\n合計 {len(order)} 頁，未通過 {bad} 頁')
sys.exit(1 if bad else 0)
