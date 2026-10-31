#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Brewing 页面生成器：md → html（沿用 issue-001..003 的内联样式）。

用法：
    python3 build_page.py source.md out.html --title "…" [--kicker "…"]

支持的最小 Markdown 子集（够用即止，不引依赖）：
    # H1 / ## H2 / > 引言 / --- 分隔 / **粗体** / [文字](链接) /
    有序条目（`1. [标题](链接)` 下一行缩进即点评）/ 普通段落

自检：`python3 build_page.py --selftest`
"""

import sys
import re
import html as htmllib

STYLE = """<style>
:root{--ink:#1a1a1a;--dim:#6b6b6b;--rule:#e2ddd5;--paper:#fdfcf7;--accent:#8c3a2e;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font:16px/1.85 -apple-system,BlinkMacSystemFont,"PingFang SC","Songti SC","Microsoft YaHei",serif;
  background:var(--paper);color:var(--ink);max-width:680px;margin:0 auto;padding:64px 24px 96px;-webkit-font-smoothing:antialiased;}
h1{font-size:1.7rem;font-weight:600;line-height:1.4;letter-spacing:.01em;}
h2{font-size:1.05rem;font-weight:600;margin:38px 0 14px;padding-bottom:8px;border-bottom:1px solid var(--rule);}
p{margin:12px 0;}
p.lead{color:var(--accent);letter-spacing:.08em;font-size:.95rem;margin-top:14px;}
p.item a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--accent);}
p.item a:hover{color:var(--accent);}
hr{border:none;border-top:1px solid var(--rule);margin:36px 0;}
a{color:var(--accent);}
.back{display:inline-block;margin-top:40px;font-size:.85rem;color:var(--dim);text-decoration:none;}
.note{color:var(--dim);font-size:.85rem;}
small{display:block;margin:4px 0;font-size:.8rem;color:var(--dim);line-height:1.7;}
</style>"""

INLINE = [
    (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), r'<a href="\2" target="_blank">\1</a>'),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"\*([^*]+)\*"), r"<em>\1</em>"),
]


def inline(text):
    """行内标记转 HTML。先转义再替换，避免链接里的 & 二次转义。"""
    out = htmllib.escape(text, quote=False)
    for pat, rep in INLINE:
        out = pat.sub(rep, out)
    return out


def convert(md, kicker=None):
    """md 文本 → 正文 HTML 片段（不含 <html> 外壳）。"""
    lines = md.replace("\r\n", "\n").split("\n")
    out, buf, i = [], [], 0

    def flush():
        if buf:
            out.append("<p>%s</p>" % inline(" ".join(buf).strip()))
            buf.clear()

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if not s:
            flush()
            i += 1
            continue
        if s.startswith("# "):
            flush()
            out.append("<h1>%s</h1>" % inline(s[2:].strip()))
        elif s.startswith("## "):
            flush()
            out.append("<h2>%s</h2>" % inline(s[3:].strip()))
        elif s.startswith(">"):
            flush()
            out.append('<p class="lead">%s</p>' % inline(s.lstrip("> ").strip()))
        elif s == "---" or s == "***":
            flush()
            out.append("<hr>")
        elif re.match(r"^\d+\.\s", s):
            flush()
            body = re.sub(r"^\d+\.\s+", "", s)
            out.append('<p class="item">%s</p>' % inline(body))
            # 紧跟的缩进行是点评
            j = i + 1
            desc = []
            while j < len(lines) and lines[j].startswith("    ") and lines[j].strip():
                desc.append(lines[j].strip())
                j += 1
            if desc:
                out.append("<p>%s</p>" % inline(" ".join(desc)))
            i = j
            continue
        elif re.match(r"^[*\-]\s", s):
            flush()
            out.append('<p class="item">· %s</p>' % inline(re.sub(r"^[*\-]\s+", "", s)))
        elif s.startswith("<small>") and s.endswith("</small>"):
            flush()
            inner = s[len("<small>"):-len("</small>")]
            out.append('<small>%s</small>' % inline(inner))
        elif s.startswith("*") and s.endswith("*") and len(s) > 2:
            flush()
            out.append('<p class="note">%s</p>' % inline(s.strip("*")))
        else:
            buf.append(s)
        i += 1
    flush()

    body = "\n".join(out)
    if kicker:
        body = '<p class="lead">%s</p>\n' % inline(kicker) + body
    return body


def page(title, body, back="./../index.html"):
    return (
        "<!DOCTYPE html>\n<html lang=\"zh-Hans\">\n<head>\n"
        "<meta charset=\"UTF-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        "<title>%s</title>\n%s\n</head>\n<body>\n%s\n"
        '<a class="back" href="%s">← 返回目录</a>\n'
        "</body>\n</html>\n"
    ) % (htmllib.escape(title), STYLE, body, back)


def selftest():
    md = "# 标题\n\n> 副题\n\n第一段**粗**。\n\n## 小节\n\n1. [链接](https://a.b/c)\n   点评文字\n\n---\n\n*注：说明*\n"
    got = convert(md, kicker="一夕运粮")
    assert "<h1>标题</h1>" in got, got
    assert '<p class="lead">一夕运粮</p>' in got, got
    assert '<p class="lead">副题</p>' in got, got
    assert "<strong>粗</strong>" in got, got
    assert "<h2>小节</h2>" in got, got
    assert '<a href="https://a.b/c" target="_blank">链接</a>' in got, got
    assert "<p>点评文字</p>" in got, got
    assert "<hr>" in got, got
    assert '<p class="note">注：说明</p>' in got, got
    # 转义：原文的 < > 不应变成标签
    assert "&lt;script&gt;" in convert("a <script> b"), "未转义"
    print("selftest ok")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    src, dst = args[0], args[1]
    title = ""
    kicker = "一夕运粮，一期酝酿。"
    if "--title" in args:
        title = args[args.index("--title") + 1]
    if "--kicker" in args:
        kicker = args[args.index("--kicker") + 1]
    if "--no-kicker" in args:
        kicker = None
    md = open(src, encoding="utf-8").read()
    body = convert(md, kicker=kicker)
    open(dst, "w", encoding="utf-8").write(page(title or src, body))
    print("wrote %s (%d bytes)" % (dst, len(body)))


if __name__ == "__main__":
    main()
