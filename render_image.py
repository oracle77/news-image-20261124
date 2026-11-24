#!/usr/bin/env python3
"""Render the 24 November 2026 world-news front page (1024x1024 PNG).

All text is drawn with PIL from verified facts (see NEWS.md in this folder),
so no glyph is ever garbled by an image model. Layout is a newspaper front
page: masthead with the date, one hero story, four panels, one ALSO strip.
Pattern reused from news-image-20261123; only the date and content changed.
Market figures are verified session closes (see NEWS.md).
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 32, 46)
NAVY = (18, 38, 63)
NAVY2 = (24, 52, 84)
RED = (179, 38, 30)
BLUE = (29, 78, 137)
TEAL = (15, 118, 110)
GOLD = (201, 162, 39)
ORANGE = (242, 140, 40)
GRAY = (90, 100, 112)
LIGHT = (233, 228, 218)
WHITE = (255, 255, 255)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, color, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


def kicker(draw, x, y, label, color):
    draw.text((x, y), label, font=font(BOLD, 22), fill=color)
    return y + 30


# ---------- icons (flat, drawn) ----------
def icon_tower(d, x, y, s):
    # a tall skyscraper: tapered body, lit window grid, impact burst
    # body
    d.polygon([(x + 30, y + 200), (x + 45, y + 10), (x + 155, y + 10),
               (x + 170, y + 200)], fill=(29, 78, 137),
              outline=(120, 170, 210))
    d.polygon([(x + 45, y + 10), (x + 155, y + 10), (x + 155, y + 26),
               (x + 45, y + 26)], fill=(120, 170, 210))
    # windows
    for r in range(6):
        wy = y + 44 + r * 24
        for c in range(4):
            wx = x + 58 + c * 24
            d.rectangle([wx, wy, wx + 13, wy + 13], fill=(205, 216, 228))
    # impact burst halfway up the facade
    bx, by = x + 168, y + 96
    pts = []
    for i in range(12):
        ang = -math.pi / 2 + i * math.pi / 6
        rr = 26 if i % 2 == 0 else 12
        pts.append((bx + rr * math.cos(ang), by + rr * math.sin(ang)))
    d.polygon(pts, fill=(242, 140, 40), outline=(255, 200, 120))
    d.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=(255, 255, 255))


def icon_star(d, x, y, s):
    cx, cy, r = x + 24, y + 24, 22
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=(201, 162, 39))


# ---------- page ----------
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 28  # margin

# Masthead
d.text((M, 18), "WORLD NEWS", font=font(BOLD, 92), fill=INK)
d.text((M, 118), "TUESDAY  ·  24 NOVEMBER 2026", font=font(BOLD, 36), fill=RED)
d.rectangle([M, 168, W - M, 172], fill=INK)
d.rectangle([M, 176, W - M, 178], fill=INK)

# Hero panel: Houthi drone hits Riyadh tower
hy0, hy1 = 192, 474
d.rounded_rectangle([M, hy0, W - M, hy1], radius=10, fill=NAVY)
d.text((M + 24, hy0 + 20), "MIDDLE EAST  ·  RIYADH", font=font(BOLD, 23), fill=(242, 140, 40))
y = text_block(d, M + 24, hy0 + 56, "HOUTHI DRONE HITS RIYADH TOWER",
               font(BOLD, 40), WHITE, 660, 48)
d.text((M + 24, y + 10), "11 injured in strike on PIF skyscraper;",
       font=font(REG, 25), fill=(205, 216, 228))
d.text((M + 24, y + 44), "2nd hit in under a week.",
       font=font(REG, 25), fill=(205, 216, 228))
icon_tower(d, 748, hy0 + 76, 1)


def panel(x0, y0, x1, y1, kicker_text, kicker_color, headline, deck):
    d.rounded_rectangle([x0, y0, x1, y1], radius=8, fill=WHITE, outline=(200, 192, 178), width=2)
    d.rectangle([x0 + 8, y0, x1 - 8, y0 + 6], fill=kicker_color)
    tx = x0 + 20
    kicker(d, tx, y0 + 18, kicker_text, kicker_color)
    y = text_block(d, tx, y0 + 52, headline, font(BOLD, 31), INK, (x1 - x0) - 40, 38)
    text_block(d, tx, y + 6, deck, font(REG, 21), (60, 70, 84), (x1 - x0) - 40, 28)


# Row 2
panel(M, 488, 502, 692, "WAR  ·  GAZA", BLUE,
      "ISRAELI STRIKES KILL 7 IN GAZA",
      "Hamas security chief among dead despite ceasefire.")
panel(522, 488, W - M, 692, "WAR  ·  UKRAINE", RED,
      "RUSSIAN STRIKE KILLS 2 IN ZAPORIZHZHIA",
      "44 wounded, incl. 4 children, in apartment hit.")

# Row 3
panel(M, 706, 502, 910, "MARKETS", RED,
      "DOW TOPS 50,000 FOR FIRST TIME",
      "Dow +0.9% to 50,018.70; Nasdaq -1.5%, S&P -0.5%.")
panel(522, 706, W - M, 910, "ASIA  ·  DISASTER", TEAL,
      "HANOI GAS BLAST KILLS 6",
      "Hot-pot eatery explosion; 10+ injured in Dong Da.")

# Bottom strip
d.rectangle([M, 924, W - M, 984], fill=INK)
d.text((M + 20, 940), "ALSO:", font=font(BOLD, 26), fill=(242, 140, 40))
d.text((M + 118, 940), "Iran says 4 tankers hit mines in Hormuz; rial plunges",
       font=font(BOLD, 26), fill=WHITE)

img.save(OUT, optimize=True)
print("saved", img.size)
print("bytes:", os.path.getsize(OUT))
