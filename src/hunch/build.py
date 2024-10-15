"""hunch — build your notes into a static site.

Usage:
    python -m hunch.build
"""
import pathlib
import shutil

NOTES_DIR = pathlib.Path("notes")
OUTPUT_DIR = pathlib.Path("output")


def build() -> None:
    """Render all notes in NOTES_DIR to HTML in OUTPUT_DIR."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    note_paths = sorted(NOTES_DIR.glob("*.md"))
    if not note_paths:
        print("No notes found in notes/")
        return

    pages = []
    for path in note_paths:
        content = path.read_text(encoding="utf-8")
        title = path.stem.replace("-", " ").replace("_", " ").title()
        html = _render_page(title, content)
        out = OUTPUT_DIR / (path.stem + ".html")
        out.write_text(html, encoding="utf-8")
        pages.append((path.stem, title))

    index_html = _render_index(pages)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Built {len(note_paths)} notes → {OUTPUT_DIR}/")


def _render_page(title: str, body: str) -> str:
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
