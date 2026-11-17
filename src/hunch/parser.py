"""Parse Markdown notes with YAML frontmatter.

Each note file is a Markdown file with an optional YAML frontmatter block.
Supported frontmatter fields:

  title  : str        — display title (defaults to the filename, title-cased)
  date   : str        — ISO date string, e.g. 2024-11-15; sorts the index
  tags   : list[str]  — labels for the note; a single string becomes [string]
  author : str        — note author

``category:`` (a single string) is the pre-0.3.1 name for ``tags:``. It is
still read as a fallback so old notes build, but new notes should not use it.

Example note file::

    ---
    title: My First Note
    date: 2024-10-15
    tags: [python, tools]
    author: Alex
    ---

    Note body goes here.

Typical usage (run from the repository root, since the path is relative)::

    >>> from pathlib import Path
    >>> note = parse_note(Path('notes/python-decorators.md'))
    >>> note.metadata.title
    'Python Decorators'
    >>> note.metadata.tags
    ['python']
    >>> note.metadata.author
    'Alex'
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class NoteMetadata:
    title: str
    date: str = ""
    tags: list[str] = field(default_factory=list)


@dataclass
class Note:
    metadata: NoteMetadata
    body: str
    slug: str


_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_note(path: Path) -> Note:
    """Parse a single Markdown note file, returning a Note object."""
    raw = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(raw)

    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        body = raw[m.end():]
    else:
        fm = {}
        body = raw

    tags_raw = fm.get("tags") or fm.get("category") or []
    if isinstance(tags_raw, str):
        tags_raw = [tags_raw]

    author = fm.get("author", "")

    metadata = NoteMetadata(
        title=fm.get("title") or path.stem.replace("-", " ").replace("_", " ").title(),
        date=str(fm.get("date", "")),
        tags=tags_raw,
    )
    metadata.author = author  # type: ignore[attr-defined]

    return Note(metadata=metadata, body=body.strip(), slug=path.stem)


def parse_all(notes_dir: Path) -> list[Note]:
    """Parse all .md files in notes_dir, sorted by date descending."""
    notes = [parse_note(p) for p in sorted(notes_dir.glob("*.md"))]
    notes.sort(key=lambda n: n.metadata.date, reverse=True)
    return notes
