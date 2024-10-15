# Hunch

> A place for the things you're still figuring out.

Hunch turns a folder of Markdown notes into a browsable static site. It lives
on your machine, reads plain text files, and gets out of your way.

*(If you've ever opened Notion to write a quick note and spent 40 minutes
reorganizing your workspace instead, Hunch might be for you.)*

## What it does

- Reads `.md` files from a `notes/` directory
- Renders them to HTML in an `output/` directory
- Generates an `index.html` listing all your notes

## Usage

```
python -m hunch.build
```

Open `output/index.html` in a browser to see your notes.

## Requirements

Python 3.11+. No external dependencies.
