# HW4: Hunch

Hunch is a small tool that publishes Markdown notes as a website. It works, but its documentation no longer describes it. You'll read the project's history to work out how that happened, repair the record, and then extend the project with its documentation done from the start. Writing things down is one way people and projects offload what they would otherwise have to remember, so this assignment also asks what that record owes its readers, and what happens when they stop checking it.

**ASSIGNMENT DUE DATE (all parts):** Monday, Nov 16th @ 11:59pm ET

## Learning Objectives

By completing this assignment, you will:

1. **Understand documentation drift**: how documentation falls out of sync with code as a project evolves, and why that matters (Tasks 2, 3, and 4)
2. **Read version history as documentation**, reconstructing a project's past and the decisions that aren't visible in its current files (Tasks 1 and 4)
3. **Write documentation for different audiences**, distinguishing user-facing, contributor-facing, and historical documents (Tasks 1, 2, 4, and 5)
4. **Work with executable documentation**, and see how it can go stale just as prose can (Task 3)
5. **Extend a project with documentation from the start**, treating a tool's messages as documentation too (Task 5)
6. **Weigh documentation as offloaded memory**: what a written record lets people stop holding in their heads, and what that costs them (WRITTEN)

## No CI for this assignment

Unlike earlier homeworks, HW4 has no CI workflow, and you don't need to add one. Everything you need to check your work (`hunch build`, `hunch check`, `ruff`, `doctest`) runs in seconds in your container, and this assignment is mainly about documentation rather than automated testing.

---

## Assignment Structure

This assignment has three parts:

| Part | Where | Description |
|------|-------|-------------|
| **Artifact** | [ARTIFACT.md](ARTIFACT.md) | Repair and extend the Hunch documentation ecosystem; submitted to **HW4 Artifact** on Gradescope |
| **Written Reflection** | [WRITTEN.md](WRITTEN.md) | Reflect on documentation, history, and self-documentation; submitted to **HW4 Written** on Gradescope |
| **AI Usage Report** | [HW4 AI usage reporting tool](https://genai.cs.brandeis.edu/prompt/9e91b3e8-709e-4d07-a9b0-319f22e5bbb6) | Required **even if you didn't use AI** |

**Complete the artifact first**, then do the required reading, then write your reflection.

AI usage reporting should come last. Full instructions for reporting AI usage can be found on Moodle.

---

## Required Reading

Read these **after completing the artifact tasks and before starting the written reflection**, so you can connect them to your own experience repairing Hunch. This order is intentional.

- **Donald Knuth, "Literate Programming"** (sections A and B), provided on Moodle
- **Vannevar Bush, "As We May Think"** (1945), provided on Moodle

We haven't covered these in class, and the written reflection depends on them.

---

## Prerequisites & Setup

### Getting your repository

**This works differently from earlier homeworks, so please read this section even if you've done the others.**

You still work in your own **private** copy, and the course dev container works the same way. What changes is how you make the copy.

**Why:** this project's commit history is part of the assignment. You'll read it for Task 1 and rely on it for Task 4, so your copy has to keep it.
- **Use this template**, which we used before, starts your copy with a single commit, so the history would be gone.
- **Forking** keeps the history, but a fork of a public repository is public, and GitHub doesn't let you make a fork private on its own. Other students could see your work. **Please don't fork this repository.**

So you'll make an empty private repository, clone the course repository, and push its full history to yours.

**How:**

1. On GitHub, [create a new repository](https://github.com/new). Set **Owner** to your own GitHub account, name it (for example `cosi106b-hw4`), and choose **Private**. Leave it empty: no README, no `.gitignore`, no license.
2. In a terminal on your computer, run these commands, using your new repository's URL from its GitHub page:

   ```bash
   git clone https://github.com/brandeis-cosi-106b/hw4-fa26.git cosi106b-hw4
   cd cosi106b-hw4
   git remote rename origin upstream
   git remote add origin <your-new-repository-url>
   git push -u origin main
   ```

   Cloning names the course repository `origin`. The third command renames it to `upstream`, the fourth makes your own repository `origin`, and the last sends everything to it. After this, a plain `git push` goes to your repository.
3. Check the result. `git remote -v` should show your repository as `origin` and the course repository as `upstream`. Your repository's page on GitHub should say **Private**, and its **Commits** page should list the project's earlier commits, not just one.

### Required updates

If bugs in the assignment are discovered after release, course staff may publish fixes. **Applying them is required.** They will be announced with one or more commit IDs. In your repository,

```bash
git fetch upstream
git cherry-pick <commit-id>          # as announced
git push
```

If Git reports a conflict, it's because you edited the same lines as the fix. Open the listed files, keep both your work and the fix, then run `git add <file>` and `git cherry-pick --continue`.

### Tools

As in earlier homeworks, all work happens inside a **Docker development container** with every tool preinstalled (Python, uv, ruff, and Hunch's dependencies).

**Follow [DOCKER.md](DOCKER.md) to get set up.** If you set up Docker Desktop and VS Code for an earlier homework, you already have everything: open your `cosi106b-hw4` folder in VS Code and reopen it in its container the same way.

Once your container is open, check in its terminal that everything is there:

```bash
hunch --help
ruff --version
git log --oneline
```

For full usage documentation, see [docs/USAGE.md](docs/USAGE.md), keeping in mind what this assignment is about. To view a built site, run `python -m http.server 8000 --directory site` in the container and open the address VS Code offers.

---

## Grading

This assignment is evaluated using **two independent letter grades**:

| Grade | Evaluates |
|-------|-----------|
| **Artifact Grade** | Documentation quality, historical engagement, deprecation strategy |
| **Reflection Grade** | Theory-building, honest self-assessment, engagement with course ideas |

These grades are **not mechanically averaged**. Strong performance in one area does not automatically make up for the other, though a strong written reflection can partially offset incomplete technical work.

**See [RUBRIC.md](RUBRIC.md) for detailed grading criteria.**

The goal is not just to make things technically correct, but to produce documentation that is useful: clear, accurate, and written for the right audience. For the reflection, we value honesty, specificity, and real engagement with the readings. A thoughtful reflection on partial success is more valuable than a superficial reflection on complete success.

### Gradescope Autograder

When you submit your artifact to Gradescope, the autograder runs a few basic checks. It can tell whether files exist, whether some stale text remains, whether Hunch reacts to a deprecated field, and whether `hw4.bundle` is current. It can't tell whether a document is accurate, or whether it serves its reader, and that's most of this assignment. Course staff read your work for that.

The autograder score is **not** your artifact grade, in either direction. Passing a check doesn't automatically earn credit: many checks are bare minimums, which show that something is there, not that it was done well. Failing a check doesn't automatically lose credit, because a script can miss good work. The score is one piece of evidence course staff use alongside [RUBRIC.md](RUBRIC.md).

---

## AI Tools Policy

You may use automation tools to help with this assignment, including both LLM-powered tools and "older" automations (e.g., those built into your IDE). You must document your usage in the AI usage report (see [Assignment Structure](#assignment-structure)).

LLM tools can produce plausible-sounding documentation that is subtly wrong or misses what an audience actually needs.

**Remember**: you need to understand what your submission says and does. You may be asked about it in an oral exam.

---

## Submission

Your final repository should contain:

| File | Description |
|------|-------------|
| **`HISTORY.md`** | New file: project evolution and documentation drift (Task 1) |
| **`docs/USAGE.md`**, **`docs/CONTRIBUTING.md`** | Repaired: accurate and written for their readers (Task 2) |
| **`notes/`**, **`src/hunch/parser.py`** | Example notes on current conventions, doctest examined and updated (Task 3) |
| **`CHANGELOG.md`** | Complete: covers every change in the git history (Task 4) |
| **Task 5 deprecation** | Code change, migration section in `docs/USAGE.md`, and `CHANGELOG.md` entry |
| **`hw4.bundle`** | Your commit history, including at least 5 meaningful new commits spread across the tasks |

### How to Submit

0. Review [RUBRIC.md](RUBRIC.md) to understand how you'll be evaluated
1. Complete the tasks in [ARTIFACT.md](ARTIFACT.md), committing as you go
2. As your last artifact step, commit all your work, then run this in your container's terminal:

```bash
bundle-history
```

Your commit history is part of what we grade, but the copy of your repository that Gradescope receives leaves it out. This command saves your history in one file, `hw4.bundle`, then commits and pushes that file so it reaches us with your submission. If you commit more work afterward, run it again before you resubmit.

3. Submit your **artifact** on Gradescope: open the **HW4 Artifact** assignment, choose **GitHub** as the submission method, and select your HW4 repository and the `main` branch. You can resubmit as many times as you like before the deadline.

4. Do the required reading, complete the written reflection in [WRITTEN.md](WRITTEN.md) (including the self-assessment), then upload your completed `WRITTEN.md` to the **HW4 Written** assignment on Gradescope.

5. Submit your AI usage report through the [HW4 AI usage reporting tool](https://genai.cs.brandeis.edu/prompt/9e91b3e8-709e-4d07-a9b0-319f22e5bbb6), **even if you didn't use AI**. Full instructions for reporting AI usage can be found on Moodle.

---

## Resources

- [Click documentation](https://click.palletsprojects.com/)
- [Jinja2 documentation](https://jinja.palletsprojects.com/)
- [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [Python doctest documentation](https://docs.python.org/3/library/doctest.html)
- [git cherry-pick](https://git-scm.com/docs/git-cherry-pick)
