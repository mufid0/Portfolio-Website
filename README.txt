MUFID PANHALKAR — AI/ML PORTFOLIO
==================================

Files included
--------------
  index.html            Self-contained portfolio (all CSS + JS inlined)
  images/jinwoo-hero.jpg     Hero portrait (Solo Leveling — Shadow Monarch)
  images/shadow-army.jpg     Contact section image (Shadow Army)
  serve.py              Optional one-line Python server


How to run on your local server
-------------------------------

OPTION 1 — Just double-click
  Most browsers will open `index.html` directly. Fonts and styles work,
  but some browsers block local images from `file://` for security.
  If images don't show, use Option 2 instead.

OPTION 2 — Python (recommended, no install needed if Python is present)
  Open a terminal in this folder and run:

      python3 serve.py

  Then open http://localhost:8000 in your browser.

  (Or directly:  python3 -m http.server 8000)

OPTION 3 — Node.js
  npx serve .
  Then open the URL it prints.

OPTION 4 — Any other static server
  Drop the entire folder into Apache / Nginx / Caddy / Vercel / Netlify /
  GitHub Pages — `index.html` is the entry point. No build step required.


Editing
-------
Everything lives in a single HTML file (`index.html`).
  - Content (text, links, projects)  →  edit the <body>
  - Styling (colors, layout)          →  edit the <style> block (top)
  - Behavior (cursor, animations)     →  edit the <script> block (bottom)

Color theme variables are defined under `:root { ... }` near the top
of the <style> block — change `--accent`, `--accent2`, `--accent3` to
re-skin the whole site.

— Built with precision · Targeting FAANG
