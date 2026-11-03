import sys; sys.path.insert(0,'.')
import s5, s6
from base import *
from css import CSS
import s1,s2,s3,s4
cards=[s1.e01(),s5.e01b(),s1.e02(),s5.e03(),s2.e04(),s6.e21(),s3.e06(),s3.e07(),s3.e09(),s6.e22(),s3.e10(),s4.e11(),s5.e12(),s5.e13(),s4.e14(),s4.e15(),s5.e20(),s4.e16(),s4.e17(),s4.e18(),s4.e19()]
html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1920">
<title>HeyDoc Film Element Board</title>
<!--
  HeyDoc AI · explainer film (1:55) · element board
  Static components only. Board chrome = .eb-*  ·  reusable components = .hd-*
  Each component's markup is self-contained (icons inlined, no sprite) so it can be copied into a scene.
  All design values live in :root below. Fake data throughout. Placeholders (.hd-slot) mark logos/screens to supply.
-->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Open+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}{s5.FILMCSS}{s6.CSS6}</style>
</head>
<body>
<header class="eb-top">
  <div><div class="k">HeyDoc AI · Explainer film · 1:55</div><h1>Film element board: <em>every building block, static</em></h1></div>
  <div class="meta"><span>18 element groups</span><span>Updated to match the film</span><span>1920 · 12-col grid</span><span>Open Sans · HeyDoc tokens</span><span>Fake data only</span></div>
</header>
<main class="eb-grid">
{"".join(cards)}
</main>
</body>
</html>'''
open('/mnt/user-data/outputs/heydoc-film-element-board.html','w').write(html) if False else None
open('../board.html','w').write(html)
print(len(html))
