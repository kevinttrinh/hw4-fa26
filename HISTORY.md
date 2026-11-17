# Hunch: Project History

*For new contributors. Read this before trusting any other document in the repo.*

Hunch has changed a lot in four months, and the written record didn't always
keep up. This file explains how the project got to where it is, points out
where the docs and the code went separate ways (so you don't get caught by the
same gaps), and sums up the conventions the code actually follows today.

When a document and the code disagree, **the code wins**. Every claim below
was checked against `git show` output and against the current source.

---

## How the project evolved

**1. A one-file prototype (Oct 15, 2024, `5f42bc6`).**
Hunch started as a single script, `python -m hunch.build`. It read
`notes/*.md`, turned them into bare HTML in `output/`, and had no
dependencies. The README described it accurately at the time.

**2. Metadata and real templates (Oct 28 to Nov 22, 2024: `963bf23`, `a2948e2`, `fefcc50`).**
Notes got YAML frontmatter (`title`, `date`, `category`), and rendering moved
to Jinja2 templates in `templates/`. Two weeks later the single `category:`
string was replaced by a `tags:` list, so a note could have more than one
label. The parser kept reading `category:` quietly as a fallback, so old notes
still built. This is the first point where the docs fell behind.

**3. Features and renames (Dec 2024 to Jan 2025: `bee8f96`, `33d6854`, `3a8d0e6`, `4dbf258`).**
A search index (`search.json`) was added, and `CHANGELOG.md` was created in
the same commit. Two weeks later the output directory was renamed from
`output/` to `site/`. A copy of the generated site was then committed "as a
quick visual reference" and removed the next day, because generated output
doesn't belong in version control.

**4. A real CLI, with documentation written afterwards (Jan to Feb 2025: `7daac0b`, `019471e`).**
`python -m hunch.build` became the `hunch` command with three subcommands
(`build`, `check`, `index`). This commit also added an `author` field and wrote
`docs/USAGE.md` and `docs/CONTRIBUTING.md` for the first time, after most of
the features above already existed. The last commit added a `--drafts` flag
and a module docstring with a doctest in `parser.py`.

---

## Where the docs and the code drifted apart

These are the specific moments to know about. Each one explains a piece of
stale text you may still run into in older copies or forks.

### 1. `category:` became `tags:`, and not everything followed (`fefcc50`)
The commit updated the parser, both templates, and two of the three sample
notes. It missed `notes/python-decorators.md`, which kept `category: python`.
It also left the README's "Supported fields: `title`, `date`, `category`"
unchanged. The silent fallback in `parser.py`
(`fm.get("tags") or fm.get("category")`) meant nothing broke, so nobody
noticed. Two months later, `USAGE.md` and `CONTRIBUTING.md` were written with
`category` as the current field, which shows they were written from memory of
the old design and not from the code.

**Why it persisted:** backward compatibility hid the mistake. A rename that
breaks nothing produces no error, and so nobody goes back to check.

### 2. `output/` became `site/`, but the docs written later still say `output/` (`33d6854` → `7daac0b`)
The rename touched only `build.py` and `search.py`. A month later `USAGE.md`
and `CONTRIBUTING.md` were written, and both describe `output/`: the build
target, the `--clean` flag, the output tree, and "open `output/index.html`".
So these docs were already stale on the day they were created. The changelog's
v0.3.1 entry correctly says `output/search.json` (true at the time), but the
rename itself was never recorded, so a reader has no way to learn that it
moved.

Related detail: `.gitignore` has ignored `site/` since the very first commit,
while the build wrote to `output/` for two months. The snapshot in `3a8d0e6`
must have been force-added (`git add -f`) past that rule. The removal in
`4dbf258` restored the original intent.

### 3. `docs/USAGE.md` describes a `check` command that doesn't exist (`7daac0b`)
USAGE.md says `hunch check` warns about missing `title`, `date`, or
`category`. The code checks `title`, `date`, and **`tags`**. The `title` check
can't actually fire, because the parser always fills in a title from the
filename. CONTRIBUTING.md still says to build with `python -m hunch.build`, but the CLI
commit removed that entry point's `if __name__ == "__main__"` block. The
command now **exits silently and builds nothing**, so a contributor following
the guide would see no error and no output. It also says to update "the
frontmatter table in `README.md`", which no longer exists.

The same commit quietly changed one behavior: earlier builds always deleted
the output folder first, but `hunch build` only does that with `--clean`.
Nothing documented the change.

### 4. A docstring that teaches the old convention and passes its own test (`019471e`)
The new module docstring in `parser.py` lists `category : str` as a field and
shows an example note with `category: python`. Right below it, the doctest
asserts `note.metadata.tags == ['python']`. The doctest **passes**, because
the `category` fallback converts the field. So the one "executable" piece of
documentation confirms the outdated example instead of catching it. A test
only checks what it asserts.

### 5. `--drafts` has a help string but no working feature (`019471e`)
`hunch build --help` says `--drafts` includes "notes marked `draft: true`".
But the parser never reads a `draft` field, so
`getattr(n.metadata, "draft", False)` is always `False`. In practice **every
note is published, including ones marked `draft: true`, with or without the
flag.** (Tested: a `draft: true` note appeared in `site/notes/` after a plain
`hunch build`.) The help text is the only documentation for this feature, and
it is wrong.

### 6. The changelog stopped at v0.3.1 (`bee8f96` onward)
`CHANGELOG.md` was created on Dec 5, 2024, and never updated again. The
`tags:` switch (before it), the `site/` rename, the CLI, `author`, and
`--drafts` (after it) were all missing. Meanwhile `pyproject.toml` moved to
`0.4.0`.

---

## Conventions today (what the code actually does)

| Topic | Current convention |
|---|---|
| Running Hunch | `hunch build`, `hunch check`, `hunch index` (not `python -m hunch.build`) |
| Output directory | `site/` (git-ignored; never commit it) |
| Labels | `tags:` as a YAML list, e.g. `tags: [python, tools]`. A single string also works. |
| `category:` | Deprecated (v0.5.0). Still read as `tags:`, but `hunch build` and `hunch check` now warn and show the fix; see the migration section in `docs/USAGE.md` |
| Other fields | `title` (defaults to the filename), `date` (`YYYY-MM-DD`, sorts the index), `author` (stored but not yet shown on pages) |
| Drafts | `draft: true` is **not** honored yet; see drift item 5 |
| Search | `hunch build` always writes `site/search.json`; `hunch index` only regenerates it |
| Sample notes | All use `title`, `date`, `tags`, `author` |

When you change a field, a path, or a command, update `docs/USAGE.md`,
`docs/CONTRIBUTING.md`, the `parser.py` docstring, and `CHANGELOG.md` in the
same commit. Almost every drift item above comes from a commit that skipped
one of these.
