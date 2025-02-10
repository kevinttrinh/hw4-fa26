"""hunch CLI — build your notes into a static site.

Commands
--------
hunch build   — render notes/ to site/
hunch index   — regenerate site/search.json only
hunch check   — validate frontmatter in all notes
"""
from __future__ import annotations

import shutil
from pathlib import Path

import click

from hunch.parser import parse_all
from hunch.render import render_index, render_page
from hunch.search import write_index

NOTES_DIR = Path("notes")
SITE_DIR = Path("site")


@click.group()
def cli() -> None:
    """Hunch — publish your hunches, one note at a time."""


@cli.command()
@click.option("--clean", is_flag=True, default=False, help="Remove site/ before building.")  # noqa: E501
@click.option("--drafts", is_flag=True, default=False, help="Include notes marked draft: true.")  # noqa: E501
def build(clean: bool, drafts: bool) -> None:
    """Build all notes into a static site."""
    if clean and SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)

    notes_out = SITE_DIR / "notes"
    notes_out.mkdir(parents=True, exist_ok=True)

    notes = parse_all(NOTES_DIR)
    if not drafts:
        notes = [n for n in notes if not getattr(n.metadata, "draft", False)]

    for note in notes:
        html = render_page(note)
        (notes_out / f"{note.slug}.html").write_text(html, encoding="utf-8")

    index_html = render_index(notes)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

    write_index(notes, SITE_DIR)

    click.echo(f"Built {len(notes)} note(s) → {SITE_DIR}/")


@cli.command()
def index() -> None:
    """Regenerate the search index without rebuilding HTML."""
    notes = parse_all(NOTES_DIR)
    SITE_DIR.mkdir(exist_ok=True)
    write_index(notes, SITE_DIR)
    click.echo(f"Search index written to {SITE_DIR / 'search.json'}")


@cli.command()
def check() -> None:
    """Check all notes for missing or malformed frontmatter."""
    notes = parse_all(NOTES_DIR)
    issues = 0
    for note in notes:
        if not note.metadata.title:
            click.echo(f"  WARN  {note.slug}: missing title")
            issues += 1
        if not note.metadata.date:
            click.echo(f"  WARN  {note.slug}: missing date")
            issues += 1
        if not note.metadata.tags:
            click.echo(f"  WARN  {note.slug}: no tags")
            issues += 1
    if issues == 0:
        click.echo(f"All {len(notes)} note(s) look good.")
    else:
        click.echo(f"{issues} issue(s) found.")
