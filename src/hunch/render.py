"""Render Note objects to HTML using Jinja2 templates."""
from __future__ import annotations

from pathlib import Path

import markdown as md
from jinja2 import Environment, FileSystemLoader

from hunch.parser import Note

_TEMPLATES_DIR = Path("templates")


def _env() -> Environment:
    return Environment(loader=FileSystemLoader(str(_TEMPLATES_DIR)), autoescape=True)


def render_page(note: Note) -> str:
    """Render a single note to an HTML string."""
    env = _env()
    template = env.get_template("page.html")
    body_html = md.markdown(note.body, extensions=["fenced_code", "tables"])
    return template.render(note=note, body_html=body_html)


def render_index(notes: list[Note]) -> str:
    """Render the index page listing all notes."""
    env = _env()
    template = env.get_template("index.html")
    return template.render(notes=notes)
