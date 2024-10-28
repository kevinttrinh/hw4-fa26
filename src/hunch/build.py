"""hunch — build your notes into a static site.

Usage:
    python -m hunch.build
"""
import pathlib
import shutil

from hunch.parser import parse_all

NOTES_DIR = pathlib.Path("notes")
OUTPUT_DIR = pathlib.Path("output")


def build() -> None:
    """Render all notes in NOTES_DIR to HTML in OUTPUT_DIR."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    notes = parse_all(NOTES_DIR)
    if not notes:
        print("No notes found in notes/")
        return

    pages = []
    for note in notes:
        html = _render_page(note.metadata.title, note.metadata.category, note.body)
        out = OUTPUT_DIR / (note.slug + ".html")
        out.write_text(html, encoding="utf-8")
        pages.append((note.slug, note.metadata.title))

    index_html = _render_index(pages)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"Built {len(notes)} notes → {OUTPUT_DIR}/")


def _render_page(title: str, category: str, body: str) -> str:
    cat_html = f"<p><em>Category: {category}</em></p>" if category else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title} — Hunch</title>
  <style>body {{ font-family: sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }}</style>
</head>
<body>
  <nav><a href="index.html">← All notes</a></nav>
  <h1>{title}</h1>
  {cat_html}
  <pre style="white-space: pre-wrap">{body}</pre>
</body>
</html>
"""


def _render_index(pages: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'  <li><a href="{slug}.html">{title}</a></li>' for slug, title in pages
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>My Notes — Hunch</title>
  <style>body {{ font-family: sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }}</style>
</head>
<body>
  <h1>My Notes</h1>
  <ul>
{items}
  </ul>
</body>
</html>
"""


if __name__ == "__main__":
    build()
