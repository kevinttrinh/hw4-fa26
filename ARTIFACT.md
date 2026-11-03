# Homework 4: Artifact Tasks

Hunch is a small Markdown-based notes publisher that has been in development
for a few months. The code works. The documentation has not kept up.

Your job is not to fix bugs. Your job is to understand what happened to this
project and bring its documentation ecosystem back into alignment, then extend
it with a new feature, documented from the start.

The git history for this assignment is part of the work. Read it carefully
before diving into the tasks, and commit your work as you go. A single large
commit at the end is not acceptable. See the commit requirements at the bottom
of this file before you start.

---

## Setup

In your container's terminal:

```
hunch build
python -m http.server 8000 --directory site
```

Open the address VS Code offers to see the current output. Press Ctrl+C to stop the server.

---

## Task 1: Read the history

Run `git log` and read every commit message. Then explore the changes in a few
key commits with `git show <hash>` or `git diff <hash>^ <hash>`. If you prefer
a visual interface, the commit history is also available on your GitHub repo
page under the "Commits" tab.

Write a file called `HISTORY.md` at the root of the repo. It should:

- Summarize the major phases of the project's evolution (3-5 bullet points or
  short paragraphs)
- Identify at least three specific moments where a change to the code or
  structure was not reflected in the documentation
- Note what you think the intended conventions are now, based on the current
  code

`HISTORY.md` is a documentation artifact. Write it for a new contributor who
needs to get up to speed quickly. You are writing to someone, not just listing
facts.

Commit this file with a message that reflects what it is.

---

## Task 2: Repair the usage documentation

`docs/USAGE.md` and `docs/CONTRIBUTING.md` were written after most of the
project's development and are already partially stale. Your reading in Task 1
should help you identify what changed and when.

`docs/USAGE.md` is the main reference for how to use Hunch. It should be
accurate and complete for current Hunch behavior. `docs/CONTRIBUTING.md` should
accurately describe how to set up, build, and extend the project today.

Commit your documentation fixes. You may use one commit or two.

---

## Task 3: Repair the example notes and the doctest

Audit the sample notes in `notes/` for consistency with current conventions.
Update any that are out of date.

Then open `src/hunch/parser.py` and read the module-level docstring carefully,
including the doctest example. Run the doctest:

```
python -m doctest src/hunch/parser.py
```

Read the result carefully, and ensure that the example in the docstring
accurately represents how notes should be written today. Fix it if it does not.

Commit your note and doctest fixes.

---

## Task 4: Update the changelog

`CHANGELOG.md` documents the project's release history, but it is incomplete.
Several changes that appear in the git log have no corresponding changelog
entry. Use the commit history directly, not just your memory of Tasks 1-3,
to find everything that's missing.

For each missing entry, decide what version number and date are appropriate
based on when the change was made. Use the existing entries as a model for the
version numbering scheme.

The changelog is a document written for users, not developers. Write entries
that explain what changed and why it matters, not just what files were touched.

Commit your changelog update.

---

## Task 5: Design a deprecation strategy for `category:`

When `tags:` replaced `category:` in an early commit, the parser was quietly
updated to accept both. A note that still says `category: python` will build
without complaint, but the user has no way of knowing their file uses an
outdated convention.

That silence is a design choice. Your task is to make a better one.

Design and implement a deprecation strategy for `category:`. There is no
single correct answer. You will need to make real decisions:

- Where should the warning surface? During `hunch build`? `hunch check`? Both?
- What should the message say, and who is the audience: a confused first-time
  user, or someone who has been using Hunch since before `tags:` existed?
- How loud should it be? Should the tool fail, warn and continue, or just note it?

At minimum, your implementation must produce output on at least one user-facing
command when a deprecated field is detected.

Your implementation must include:

1. Code changes that surface the deprecation in at least one user-facing command
2. An update to `docs/USAGE.md` with a migration section explaining what
   changed, what users should do, and what the warning looks like
3. An update to `CHANGELOG.md` noting when and why `category:` was deprecated
   and where to find migration guidance
4. Well-written warning message text: the message itself is a documentation
   artifact, and it will be read by someone who is confused

In your commit message(s), briefly describe the design choices you made and why.

---

## Commit requirements

Your git log should include at least 5 new commits beyond the inherited
history before you submit. Commit messages should be specific and informative.
A message like `"fix docs"` is not acceptable; `"fix USAGE.md: update output
dir and frontmatter field names"` is.

Do not leave all your commits to the end. Commit after each task as you go.

As your last step, run `bundle-history` to save your commit history for submission.
The README's Submission section explains it.

---

## Deliverables summary

| Artifact | What's expected |
|---|---|
| `HISTORY.md` | New file summarizing project evolution and drift |
| `docs/USAGE.md` | Repaired: accurate tool description, flags, fields, output structure |
| `docs/CONTRIBUTING.md` | Repaired: accurate setup and development instructions |
| `notes/` | Example notes updated to current conventions |
| `src/hunch/parser.py` | Doctest updated to reflect current best practice |
| `CHANGELOG.md` | Complete: covers every change in the git history |
| Task 5 deprecation | Code change + migration section in USAGE.md + CHANGELOG entry |
| `hw4.bundle` | Your commit history, with at least 5 meaningful new commits |
