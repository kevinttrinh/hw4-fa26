# Contributing to Hunch

## Development setup

Clone the repo and install dependencies:

```
git clone <repo-url>
cd hunch
uv sync
```

Run the build to verify everything works:

```
python -m hunch.build
```

You should see `output/` created with HTML files.

## Project layout

```
src/hunch/
  build.py      entry point and CLI
  parser.py     frontmatter parsing
  render.py     Jinja2 HTML rendering
notes/          sample notes (used for manual testing)
templates/      HTML templates
```

## Running the linter

```
uv run ruff check src/
```

## Testing your changes manually

The fastest way to verify a change:

1. Edit a file in `src/hunch/`
2. Run `python -m hunch.build`
3. Open `output/index.html` in a browser

## Frontmatter schema

The current frontmatter fields are: `title`, `date`, `category`.

If you add a new field, update:
- `NoteMetadata` in `parser.py`
- The frontmatter table in `README.md`
- The frontmatter table in `docs/USAGE.md`
- `CHANGELOG.md`

## Templates

Templates live in `templates/` and use Jinja2 syntax. Variables available:

- In `page.html`: `note` (a `Note` object), `body_html` (rendered markdown)
- In `index.html`: `notes` (list of `Note` objects)
