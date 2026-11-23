"""Wiki 一致性檢查：死連結、孤立頁、未進索引、缺必要區塊、空區塊。
用法：python tools/lint_wiki.py ../finance-wiki
"""
import glob, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else '../finance-wiki'
os.chdir(root)
files = [p for p in glob.glob('*/*.md') if not p.startswith('raw')]
pages = {os.path.basename(p)[:-3] for p in files}
index = open('index.md', encoding='utf-8').read()
required = {
    'sources': ['## 核心問題', '## 方法', '## 主要發現', '## 關聯概念', '## 關聯文獻'],
    'concepts': ['## 定義', '## 在知識庫中的出現', '## 關聯概念'],
}
problems = []
inbound = {n: 0 for n in pages}
for f in files + ['index.md', 'log.md']:
    text = open(f, encoding='utf-8').read()
    for link in set(x.split('|')[0].replace('\\', '') for x in re.findall(r'\[\[([^\]]+)\]\]', text)):
        if link not in pages:
            problems.append(f'死連結：{f} → {link}')
        elif not f.endswith('/' + link + '.md') and f not in ('index.md', 'log.md'):
            inbound[link] += 1
    folder = f.split('/')[0]
    for head in required.get(folder, []):
        if head not in text and not (folder == 'sources' and not os.path.basename(f).startswith('fe-')):
            problems.append(f'缺區塊：{f} 缺 {head}')
    for m in re.finditer(r'(## [^\n]+)\n(.*?)(?=\n## |\Z)', text, re.S):
        if not m.group(2).strip().strip('-').strip():
            problems.append(f'空區塊：{f} 的 {m.group(1)}')
problems += [f'孤立頁：{n}' for n, c in inbound.items() if c == 0]
problems += [f'未進索引：{n}' for n in pages if f'[[{n}]]' not in index and f'[[{n}|' not in index]
print('\n'.join(problems) if problems else '通過：死連結、孤立頁、未進索引、缺區塊、空區塊皆為 0')
print(f'頁數：{len(files)}')
