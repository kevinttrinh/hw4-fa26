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

from hunch.parser import Note, parse_all
from hunch.render import render_index, render_page
from hunch.search import write_index

NOTES_DIR = Path("notes")
SITE_DIR = Path("site")

MIGRATION_DOC = 'docs/USAGE.md, section "Migrating from category: to tags:"'


def _yaml(value: object) -> str:
    """Show a frontmatter value the way the user wrote it, not as a Python repr."""
    if value is None:
        return ""
    if isinstance(value, list):
        return "[" + ", ".join(str(v) for v in value) + "]"
    return str(value)


def _as_tags_yaml(value: object) -> str:
    """Show a category value the way it should be written as tags."""
    if value is None or value == "":
        return "[]"
    return _yaml(value) if isinstance(value, list) else f"[{value}]"


def category_fix(note: Note) -> str | None:
    """Return a one-line fix for a note that uses `category:`, else None.

    The reader is someone whose notes predate `tags:` (v0.3.1). They did
    nothing wrong, so the line names the file, shows the exact old line, and
    shows the exact replacement, so it can be fixed without opening the docs.
    """
    fields = note.metadata.deprecated_fields
    path = NOTES_DIR / f"{note.slug}.md"
    if "category_ignored" in fields:
        # Both fields present: tags wins and category is silently dropped.
        value = fields["category_ignored"]
        return (
            f"{path}: `category: {_yaml(value)}` is ignored because the note "
            "also has `tags:`. Delete the `category:` line, or move its value "
            "into `tags:`."
        )
    if "category" not in fields:
        return None
    value = fields["category"]
    old, new = _yaml(value), _as_tags_yaml(value)
    return f"{path}: change `category: {old}` to `tags: {new}`"


def warn_deprecated_category(notes: list[Note]) -> None:
    """After a build, explain which notes still use `category:` and how to fix them."""
    fixes = [fix for note in notes if (fix := category_fix(note))]
    if not fixes:
        return
    one = len(fixes) == 1
    noun, these = ("note uses", "This note") if one else ("notes use", "These notes")
    click.echo("")
    click.echo(f"Heads up: {len(fixes)} {noun} `category:`, which is deprecated.")
    click.echo(
        f"Hunch replaced `category:` with `tags:` in v0.3.1. {these} still "
        "built normally,\nbut `category:` may stop working in a future version. "
        "To update:"
    )
    for fix in fixes:
        click.echo(f"  {fix}")
    click.echo(f"More details: {MIGRATION_DOC}")


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
    warn_deprecated_category(notes)


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
    deprecated = 0
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
        if fix := category_fix(note):
            click.echo(f"  DEPRECATED  {fix}")
            deprecated += 1
    issues += deprecated
    if issues == 0:
        click.echo(f"All {len(notes)} note(s) look good.")
    else:
        click.echo(f"{issues} issue(s) found.")
    if deprecated:
        click.echo(f"`category:` was replaced by `tags:`. See {MIGRATION_DOC}")
