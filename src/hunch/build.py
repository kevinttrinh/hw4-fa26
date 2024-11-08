"""hunch — build your notes into a static site.

Usage:
    python -m hunch.build
"""
import pathlib
import shutil

from hunch.parser import parse_all
from hunch.render import render_index, render_page

NOTES_DIR = pathlib.Path("notes")
OUTPUT_DIR = pathlib.Path("output")


def build() -> None:
    """Render all notes in NOTES_DIR to HTML in OUTPUT_DIR."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    notes_out = OUTPUT_DIR / "notes"
    notes_out.mkdir(parents=True)

    notes = parse_all(NOTES_DIR)
    if not notes:
        print("No notes found in notes/")
        return

    for note in notes:
        html = render_page(note)
        (notes_out / f"{note.slug}.html").write_text(html, encoding="utf-8")

    index_html = render_index(notes)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"Built {len(notes)} notes → {OUTPUT_DIR}/")


if __name__ == "__main__":
    build()
