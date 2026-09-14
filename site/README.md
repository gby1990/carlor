# Carlor ESTech GmbH – company website

Static site, no build tooling required for hosting: upload everything in this folder
(except `_src/`) to the web root of carlorestech.com.

## Editing
- Page content lives in `_src/pages/*.html` (body only; first line holds title + meta description).
- Shared header/footer: `_src/header.html`, `_src/footer.html`.
- Regenerate the top-level `*.html` files with `python3 _src/build.py`.
- Styles: `assets/style.css`, nav script: `assets/main.js`.

## Open items before go-live
- `impressum.html`: fill in the USt-IdNr. (currently `[TODO]`).
- `contact.html`: the form uses a `mailto:` action; replace with a form backend (Formspree, own PHP, etc.) if you want server-side handling.
- Replace the Unsplash stock photos (see below) with your own product / lab photos when available.
- Optional: add a German language version.

## Photos
All photos in `assets/*.jpg` are from Unsplash (Unsplash License – free for commercial use, no attribution required):
- hero-pcb.jpg – unsplash.com/photos/vE6WEdZA6Vg
- p-/pl-ambient.jpg – unsplash.com/photos/SvY5byRf-Iw
- p-/pl-roof.jpg – unsplash.com/photos/Lgiha3FBAr0 (placeholder: dashboard vents, replace with a real roof-lighting photo)
- p-/pl-grille.jpg – unsplash.com/photos/2z-CjTFqgr4 (headlight; replace with grille/logo lamp photo if available)
- p-/pl-cockpit.jpg – unsplash.com/photos/QtcKGnOOqiA
- cap-board.jpg – unsplash.com/photos/AEboEnOlpLc
