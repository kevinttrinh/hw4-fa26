"""Generate a lightweight JSON search index from parsed notes."""
from __future__ import annotations

import json
from pathlib import Path

from hunch.parser import Note


def build_index(notes: list[Note]) -> list[dict]:
    """Return a list of index entries suitable for client-side search."""
    entries = []
    for note in notes:
        entries.append({
            "slug": note.slug,
            "title": note.metadata.title,
            "date": note.metadata.date,
            "tags": note.metadata.tags,
            "excerpt": note.body[:200].replace("\n", " "),
        })
    return entries


def write_index(notes: list[Note], output_dir: Path) -> None:
    """Write search.json into output_dir."""
    entries = build_index(notes)
    out = output_dir / "search.json"
    out.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
