"""hunch — build your notes into a static site.

Usage:
    python -m hunch.build
"""
import pathlib
import shutil

from hunch.parser import parse_all
from hunch.render import render_index, render_page
from hunch.search import write_index

NOTES_DIR = pathlib.Path("notes")
SITE_DIR = pathlib.Path("site")


def build() -> None:
    """Render all notes in SITE_DIR to HTML."""
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)

    notes_out = SITE_DIR / "notes"
    notes_out.mkdir(parents=True)

    notes = parse_all(NOTES_DIR)
    if not notes:
        print("No notes found in notes/")
        return

    for note in notes:
        html = render_page(note)
        (notes_out / f"{note.slug}.html").write_text(html, encoding="utf-8")

    index_html = render_index(notes)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

    write_index(notes, SITE_DIR)
    print(f"Built {len(notes)} notes → {SITE_DIR}/")


if __name__ == "__main__":
    build()
