# Homework 4: Grading Rubric

This assignment is evaluated using **two independent letter grades**, as
described in the syllabus:

* **Artifact Grade**: evaluates the quality of your documentation work and
  deprecation strategy
* **Written Reflection Grade**: evaluates your theory-building, honest
  self-assessment, and engagement with course ideas

These two grades measure *different learning outcomes*. They are not averaged
mechanically, and strong performance in one does not automatically imply strong
performance in the other.

---

## Part A: Artifact Grade

This grade evaluates how you engaged with the documentation ecosystem: reading
the history, identifying drift, repairing it thoughtfully, and extending the
project with documentation from the start.

You are **not** graded solely on whether everything is technically correct. You
*are* graded on whether your work shows genuine understanding of *why* the drift
happened, *who* each piece of documentation is written for, and *what* a new
reader would actually need.

### Artifact Grade: A+ / A / A-

You will receive an A-range artifact grade if **most** of the following are
true:

- `HISTORY.md` is clearly written for a new contributor and identifies specific
  drift moments with accurate detail, not just a list of commit messages
- `docs/USAGE.md` and `docs/CONTRIBUTING.md` are accurate and consistent with
  the current codebase, with no stale paths, field names, commands, or flags
- Example notes use current conventions throughout
- The doctest in `parser.py` is updated and reflects current best practice
- `CHANGELOG.md` covers the changes in the git history with user-facing entries
- The deprecation strategy reflects genuine design thinking: the warning
  surfaces in a logical place, the message text is clear and actionable for
  its intended audience, and the USAGE.md migration section would actually
  help a confused user update their notes
- Commit messages are specific and informative; at least 5 new commits that
  correspond to logical phases of work

This grade reflects **strong engagement across the full documentation
ecosystem**, even if minor details remain.

---

### Artifact Grade: B+ / B / B-

You will receive a B-range artifact grade if:

- Most drift is identified and repaired, but one or two items are missed or
  addressed only partially
- `HISTORY.md` is present and accurate but reads more like a summary than
  something written *for* a reader
- The deprecation strategy works, but documentation updates are incomplete,
  e.g., CHANGELOG updated but USAGE.md migration section missing, or vice versa
- The deprecation warning fires correctly but the message is generic or the
  migration section is thin: technically present but not written for a reader
- Commit messages are present but some are vague

This grade reflects **substantial progress**, but with room for more depth or
completeness.

---

### Artifact Grade: C+ / C

You will receive a C-range artifact grade if:

- Some drift is repaired but significant stale content remains in one or more
  documents
- `HISTORY.md` exists but is superficial, mostly restates commit messages
  without synthesis or audience awareness
- The deprecation strategy is attempted but documentation is largely absent
- Commit history is sparse or messages are uniformly uninformative

This grade reflects **a good-faith attempt** that did not fully succeed.

---

### Artifact Grade: D / E

You will receive a D or E if:

- There is little evidence of engagement with the documentation work
- Documentation remains substantially unchanged from the starter state
- The submission does not reflect a serious attempt to complete the assignment

---

## Written Reflection Grade

This grade evaluates the quality of your reflection, theory-building, and
engagement with the readings and course ideas.

The written component is not a summary or a justification. It is an
opportunity to demonstrate *how you understand what you worked on*, including
confusion, partial understanding, or disagreement.

### Reflection Grade: A+ / A / A-

You will receive an A-range reflection grade if:

- The Part 3 essay engages substantively with both Knuth and Bush, takes a
  clear position, and grounds it in specific experiences from the assignment
- Part 1 responses are honest, specific, and grounded in your actual experience
  (not what you think you should have done)
- Part 2 on self-documentation is honest and specific about the system you
  actually use, however simple it is
- The self-assessment table is completed accurately; the understanding
  self-check is honest

This grade reflects strong theory-building or a well-defended critique of
the ideas raised.

---

### Reflection Grade: B+ / B / B-

You will receive a B-range reflection grade if:

- The Part 3 essay is present and addresses the prompt but stays at a surface
  level: describes the readings rather than arguing from them
- Part 2 is present but generic, with little about the system you actually use

This grade reflects solid understanding, with room to go deeper.

---

### Reflection Grade: C+ / C

You will receive a C-range reflection grade if:

- Part 3 is brief or only partially addresses the question
- Readings are mentioned in passing but not substantively engaged
- Some sections are missing or very thin
- Part 2 is absent

This grade reflects partial theory-building and awareness of learning gaps.

---

### Reflection Grade: D / E

You will receive a D or E if:

- The reflection is generic, boilerplate, or disconnected from the assignment
- There is little evidence of genuine engagement with the readings or the
  specific work done
- AI use (if any) is undocumented or uncritically presented

---

## How to Interpret the Two Grades

You will receive **two separate letter grades** for HW4: one for the artifact
and one for the written reflection.

Examples:

* **Artifact: C+, Reflection: A** → strong understanding of documentation
  despite incomplete execution
* **Artifact: A-, Reflection: C** → thorough repairs but shallow engagement
  with what they mean
* **Artifact: B, Reflection: B+** → solid work across both dimensions

Both grades matter. A strong written reflection can partially offset incomplete
technical execution, but both dimensions are expected to show meaningful effort.

---

## Final Note

The goal of this assignment is not just to make Hunch's documentation correct,
but to understand **what documentation is for**: who reads it, what they trust,
what happens when it misleads them, and what it would take to keep it honest
over time.
