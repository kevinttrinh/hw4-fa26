# Changelog

All notable changes to Hunch are documented here.

Versions follow `MAJOR.MINOR.PATCH`. While Hunch is pre-1.0, a **minor** bump
(0.x.0) can include changes that require you to update your notes or
workflow; these are marked **Breaking** with what to do. Patch releases add
small features or fixes.

---

## v0.5.0 — 2026-11-16

### Deprecated
- **`category:` is deprecated in favor of `tags:`.** Since v0.3.1 Hunch has
  read `category:` silently as a stand-in for `tags:`, so there was no way to
  learn your notes used the old format. Now:
  - `hunch build` still builds every note, then lists each note that uses
    `category:` with the exact line to change.
  - `hunch check` reports each one as a `DEPRECATED` issue.
  - If a note has both fields, you're told that `category:` is being ignored.

  Nothing fails and your site output is unchanged. A future version may stop
  reading `category:`. **To migrate**, see "Migrating from `category:` to
  `tags:`" in `docs/USAGE.md` (usually a one-line edit per note).

### Documentation
- `docs/USAGE.md` and `docs/CONTRIBUTING.md` brought up to date: `site/` (not
  `output/`), `tags:` and `author:`, the `hunch` command, `--clean`, and what
  `hunch check` really reports. Added a Known issues section (`draft: true` is
  not yet honored).
- New `HISTORY.md` explains how the project evolved, for new contributors.
- Sample notes and the `parser.py` doctest now use `tags:`.

---

## v0.4.1 — 2025-02-10

### Added
- `hunch build --drafts` flag, meant to include notes marked `draft: true`.
  **Known issue:** the `draft` field isn't read yet, so drafts are always
  published, with or without the flag. See "Known issues" in
  `docs/USAGE.md`.
- New sample note, `notes/linux-tools.md`.
- The parser module now documents the frontmatter format, with a runnable
  example (doctest).

---

## v0.4.0 — 2025-01-20

### Added
- The `hunch` command, which replaces `python -m hunch.build`:
  - `hunch build`: build the site
  - `hunch check`: report notes missing a `date` or `tags`, without building
  - `hunch index`: regenerate only `site/search.json`
- `hunch build --clean` to delete `site/` before building.
- `author` frontmatter field (stored; not yet shown on pages).
- User guide (`docs/USAGE.md`) and contributor guide (`docs/CONTRIBUTING.md`).

### Changed
- **Breaking: output now goes to `site/` instead of `output/`** (changed
  2024-12-18, first released here). Update any bookmarks, scripts, or servers
  that point at `output/`, and delete your old `output/` folder. `site/` is
  git-ignored.
- **Breaking: `python -m hunch.build` no longer builds anything.** It exits
  silently. Use `hunch build`.
- The build no longer deletes the output folder first. Pages for deleted or
  renamed notes stay in `site/` until you run `hunch build --clean`.

---

## v0.3.1 — 2024-12-05

### Added
- Search index generation: running the build now also writes `output/search.json`
  (`site/search.json` from v0.4.0)
- `search.json` contains title, date, tags, and a short excerpt for each note

### Changed
- **Breaking (format): `tags:` replaces `category:`** (changed 2024-11-22,
  first released here). A note can now have several labels:
  `tags: [python, tools]`. Notes that still say `category: python` keep
  working, but you should rename the field to `tags:`. Pages and the index
  now show each tag as a label.

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
