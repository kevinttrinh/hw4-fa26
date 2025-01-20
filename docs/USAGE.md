# Hunch

> A place for the things you're still figuring out.

Hunch turns a folder of Markdown notes into a browsable static site. It lives
on your machine, reads plain text files, and gets out of your way.

*(If you've ever opened Notion to write a quick note and spent 40 minutes
reorganizing your workspace instead, Hunch might be for you.)*

## Installation

Requires Python 3.11+. Install dependencies with:

```
uv sync
```

## Building your notes

```
hunch build
```

Reads all `.md` files from `notes/` and writes HTML to `output/`.

To also regenerate the search index:

```
hunch build
hunch index
```

## Checking your notes

```
hunch check
```

Scans all notes for missing or malformed frontmatter. Reports warnings for
notes that are missing `title`, `date`, or `category`.

## Note frontmatter

Frontmatter is a YAML block at the top of a note, delimited by `---`:

```markdown
---
title: My Note Title
date: 2024-11-01
category: python
---

Your note content here.
```

### Supported fields

| Field      | Type   | Description                                      |
|------------|--------|--------------------------------------------------|
| `title`    | string | Display title. Defaults to the filename if omitted. |
| `date`     | string | ISO 8601 date (`YYYY-MM-DD`). Used to sort the index. |
| `category` | string | A single category label shown in the rendered page. |

Fields are all optional. A bare Markdown file with no frontmatter will build fine.

## Output structure

After running `hunch build`, the `output/` directory contains:

```
output/
  index.html          — note listing
  notes/
    <slug>.html       — one page per note
  search.json         — search index (if hunch index was run)
```

## Project layout

```
notes/        your Markdown files
templates/    Jinja2 HTML templates
output/       generated site (do not edit by hand)
src/hunch/    the hunch source code
```

## Flags

`hunch build` accepts the following options:

| Flag       | Description                              |
|------------|------------------------------------------|
| `--clean`  | Delete `output/` before building         |
