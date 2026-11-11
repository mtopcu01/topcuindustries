# Topcu Industries website

Static site, no build dependencies.

- Edit content in `tools/build.py`, then run `python3 tools/build.py` to regenerate the HTML.
- Styles: `assets/css/style.css`. Behaviour (nav, terminal animation, contact form): `assets/js/main.js`.
- Contact form posts to Formspree: set `FORMSPREE_ID` in `tools/build.py` and rebuild.
- When moving to a custom domain, set `SITE_BASE = "/"` in `tools/build.py`, rebuild, and add a `CNAME` file.

Preview locally: `python3 -m http.server 8765` then open http://localhost:8765
