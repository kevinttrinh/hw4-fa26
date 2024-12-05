# Changelog

All notable changes to Hunch are documented here.

---

## v0.3.1 — 2024-12-05

### Added
- Search index generation: running the build now also writes `output/search.json`
- `search.json` contains title, date, tags, and a short excerpt for each note

---

## v0.3.0 — 2024-11-08

### Added
- Jinja2 HTML templates (`templates/page.html`, `templates/index.html`)
- Rendered note pages now include title, date, and category metadata
- Index page lists all notes with links

### Changed
- `build.py` now uses `render.py` for all HTML generation

---

## v0.2.0 — 2024-10-28

### Added
- YAML frontmatter support: `title`, `date`, `category`
- `parser.py` module for reading frontmatter
- Notes without frontmatter still build (fields default gracefully)

---

## v0.1.0 — 2024-10-15

### Added
- Initial build script: reads `.md` files from `notes/`, writes HTML to `output/`
- Three sample notes
- Basic README
