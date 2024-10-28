"""Parse Markdown notes with optional YAML frontmatter."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class NoteMetadata:
    title: str
    date: str = ""
    category: str = ""


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
    metadata = NoteMetadata(
        title=fm.get("title") or path.stem.replace("-", " ").replace("_", " ").title(),
        date=str(fm.get("date", "")),
        category=fm.get("category", ""),
    )
    return Note(metadata=metadata, body=body.strip(), slug=path.stem)


def parse_all(notes_dir: Path) -> list[Note]:
    """Parse all .md files in notes_dir, sorted by date descending."""
    notes = [parse_note(p) for p in sorted(notes_dir.glob("*.md"))]
    notes.sort(key=lambda n: n.metadata.date, reverse=True)
    return notes
