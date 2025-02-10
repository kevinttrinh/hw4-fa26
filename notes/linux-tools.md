---
title: Useful Linux Command-Line Tools
date: 2024-12-10
tags: [linux, tools, shell]
author: Alex
---

A running list of CLI tools I keep forgetting about and rediscovering.

## File and text

- `fd` — a friendlier `find`. `fd '.md'` just works.
- `ripgrep` (`rg`) — faster grep, respects .gitignore by default.
- `bat` — `cat` with syntax highlighting. Alias it over `cat`.
- `jq` — indispensable for wrangling JSON from APIs.

## System

- `htop` / `btop` — interactive process viewer. `btop` is prettier.
- `ncdu` — disk usage explorer. Find where your space went.
- `lsof -i :8080` — what process is using this port?

## Networking

- `httpie` (`http`) — more readable than curl for testing APIs.
- `mtr` — combines ping and traceroute. Good for diagnosing flaky connections.

## Things I should probably use more

- `tmux` — I keep starting, then forgetting. Maybe this time.
- `awk` — I always reach for Python instead but sometimes awk is just right.

## Open question

Is there a good TUI for browsing local Markdown files? Something like a
terminal-native Hunch. Would be a fun project.
