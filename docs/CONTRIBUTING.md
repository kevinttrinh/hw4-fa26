# Contributing to Hunch

This guide is for people changing Hunch itself. For using Hunch, see
[USAGE.md](USAGE.md). For how the project got here, and which old docs not to
trust, see [HISTORY.md](../HISTORY.md).

## Development setup

**Recommended: the dev container.** Open the repository in VS Code and choose
"Reopen in Container" (see `DOCKER.md`). Python, uv, ruff, and all of Hunch's
dependencies are preinstalled, and the `hunch` command runs the code in your
checkout's `src/`, so your edits take effect immediately.

**Without the container:** install Python 3.11+ and
[uv](https://docs.astral.sh/uv/), then from the repository root:

```
uv sync
```

This creates `.venv/` with the runtime dependencies (click, jinja2, markdown,
pyyaml), the dev tools (ruff, taskipy), and Hunch itself in editable mode.
Prefix commands with `uv run` (e.g. `uv run hunch build`), or activate `.venv`.

Check that everything works:

```
hunch build
```

You should see `Built 4 note(s) → site/` and a new `site/` directory.

## Project layout

```
src/hunch/
  build.py      CLI entry point: the `hunch` command group (build, check, index)
  parser.py     reads frontmatter and body; defines Note and NoteMetadata
  render.py     Jinja2 HTML rendering (page and index)
  search.py     writes site/search.json
templates/      Jinja2 templates: page.html, index.html
notes/          sample notes (used for manual testing)
docs/           USAGE.md (users), CONTRIBUTING.md (you are here)
site/           build output; git-ignored, never commit it
```

All paths (`notes/`, `templates/`, `site/`) are relative to the current
directory, so run every command from the repository root.

## Checking your changes

| Task | Command | taskipy shortcut |
|---|---|---|
| Build the site | `hunch build` | `uv run task build` |
| Validate note frontmatter | `hunch check` | `uv run task check` |
| Lint | `ruff check src/` | `uv run task lint` |
| Run the doctest in `parser.py` | `python -m doctest src/hunch/parser.py` | `uv run task doctest` |

The doctest reads `notes/python-decorators.md` by relative path, so it only
works from the repository root. It prints nothing when it passes; add `-v` to
see each example run.

### Testing manually

1. Edit a file in `src/hunch/` or `templates/`.
2. Run `hunch build --clean` (the `--clean` removes pages from old runs).
3. Serve the result with `python -m http.server 8000 --directory site` and open
   <http://localhost:8000>.

## Frontmatter schema

The current frontmatter fields are `title`, `date`, `tags`, and `author`
(`category` is read only as a legacy fallback for `tags`). See USAGE.md for
what each one does.

If you add, rename, or remove a field, update **in the same commit**:

- `NoteMetadata` and `parse_note()` in `parser.py`
- the field list and example in the `parser.py` module docstring (and its doctest)
- the frontmatter table in `docs/USAGE.md`
- the sample notes in `notes/`, if they should show the field
- `CHANGELOG.md`

Most of the drift in [HISTORY.md](../HISTORY.md) comes from commits that
updated the code but skipped one of these.

## Templates

Templates live in `templates/` and use Jinja2 syntax with autoescaping on.
Variables available:

- In `page.html`: `note` (a `Note`: `note.slug`, `note.body`,
  `note.metadata.title`, `.date`, `.tags`, `.author`) and `body_html` (the
  rendered Markdown; output it with `| safe`)
- In `index.html`: `notes` (list of `Note` objects, newest first)

## Changelog and versions

`CHANGELOG.md` is written for users. Describe what changed and what they need
to do, not which files you touched. When you cut a release, bump `version` in
`pyproject.toml` to match the new changelog heading.
