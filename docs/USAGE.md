# Hunch

> A place for the things you're still figuring out.

Hunch turns a folder of Markdown notes into a browsable static site. It lives
on your machine, reads plain text files, and gets out of your way.

*(If you've ever opened Notion to write a quick note and spent 40 minutes
reorganizing your workspace instead, Hunch might be for you.)*

## Installation

Requires Python 3.11+. From the project root, install Hunch and its
dependencies with:

```
uv sync
```

This installs the `hunch` command into the project's virtual environment
(run it with `uv run hunch …`, or activate `.venv` first). In the course dev
container, `hunch` is already on your `PATH`.

Run every `hunch` command **from the project root**: Hunch looks for
`notes/` and `templates/` in the current directory and writes `site/` there.

## Commands at a glance

| Command | What it does |
|---|---|
| `hunch build` | Renders every note in `notes/` to HTML in `site/`, writes the index page and `site/search.json` |
| `hunch check` | Checks every note's frontmatter and reports problems without building anything |
| `hunch index` | Regenerates only `site/search.json`, without re-rendering HTML |
| `hunch --help`, `hunch <command> --help` | Shows built-in help |

## Building your notes

```
hunch build
```

Reads all `.md` files from `notes/` and writes the site to `site/`. When it
finishes it prints a summary such as:

```
Built 4 note(s) → site/
```

`hunch build` always writes the search index too, so you don't need to run
`hunch index` afterwards. Use `hunch index` only when you want to refresh
`site/search.json` on its own.

### Build options

| Flag | Description |
|---|---|
| `--clean` | Delete `site/` before building. Use this after renaming or deleting a note, so its old page doesn't linger. |
| `--drafts` | Intended to include notes marked `draft: true`. **Currently has no effect; see [Known issues](#known-issues).** |

Without `--clean`, pages for notes you've deleted stay in `site/notes/`.

### Viewing the site

The site is plain HTML. Open `site/index.html` in a browser, or serve it
locally:

```
python -m http.server 8000 --directory site
```

and visit <http://localhost:8000>.

## Checking your notes

```
hunch check
```

Scans every note and prints a `WARN` line for each one that has:

- no `date`
- no `tags`

When everything is fine it prints `All N note(s) look good.`; otherwise it
prints the warnings and a count, e.g. `2 issue(s) found.` (A missing `title`
is never reported, because Hunch always falls back to the filename.)

`hunch check` doesn't change any files and always exits successfully. It's a
report, not a gate.

## Note frontmatter

Frontmatter is an optional YAML block at the very top of a note, between two
`---` lines:

```markdown
---
title: My Note Title
date: 2024-11-01
tags: [python, tools]
author: Alex
---

Your note content here.
```

### Supported fields

| Field | Type | Description |
|---|---|---|
| `title` | string | Display title. If omitted, built from the filename: `python-decorators.md` → "Python Decorators". |
| `date` | date (`YYYY-MM-DD`) | Used to sort the index, newest first. Notes without a date are listed last. |
| `tags` | list of strings | Labels shown on the note page, the index, and in `search.json`. A single string (`tags: python`) is treated as a one-item list. |
| `author` | string | Who wrote the note. Read and stored, but not yet shown on rendered pages. |

All fields are optional. A bare Markdown file with no frontmatter still
builds, though `hunch check` will warn that it has no date and no tags.

> **Older notes:** before v0.3.1 Hunch used a single `category:` field instead of
> `tags:`. It's still read for compatibility, but new notes should use `tags:`.

## Output structure

After `hunch build`, `site/` contains:

```
site/
  index.html          — list of all notes, newest first
  notes/
    <slug>.html       — one page per note (slug = filename without .md)
  search.json         — search index: slug, title, date, tags, and a
                        200-character excerpt for each note
```

`site/` is generated and git-ignored. Don't edit it by hand or commit it;
rebuild it instead.

## Project layout

```
notes/        your Markdown files
templates/    Jinja2 HTML templates (page.html, index.html)
site/         generated site (do not edit by hand)
src/hunch/    the Hunch source code
docs/         this guide and the contributor guide
```

## Known issues

- **`draft: true` is ignored.** The `--drafts` flag exists, but Hunch doesn't
  read the `draft` field yet, so **every note is published, including notes
  marked `draft: true`**. Until this is fixed, keep notes you don't want
  published outside `notes/`.
- **`author` isn't displayed.** It's parsed but no template shows it yet.
