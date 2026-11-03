# Homework 4: Written Reflection

Answer the following questions thoughtfully. There are no "right" answers. The
goal is genuine reflection on your experience and engagement with course ideas.

This written component is designed to reward honest engagement and
theory-building, even if your artifact is incomplete. A complete artifact
without understanding and an incomplete artifact with deep understanding are
not the same thing, and both can be discussed thoughtfully here.

---

## Part 0: Self-Assessment

Complete this section before writing your reflection. Be honest. This is
not penalized and helps us calibrate grading.

### Artifact Completion

For each task, mark your status: Done, Partial, or Not Done. Add brief notes
if helpful.

| Task | Status | Notes (optional) |
|------|--------|------------------|
| Task 1: HISTORY.md written | | |
| Task 2: USAGE.md and CONTRIBUTING.md repaired | | |
| Task 3: Example notes updated; doctest examined and updated | | |
| Task 4: CHANGELOG completed | | |
| Task 5: Deprecation strategy implemented | | |
| Task 5: Migration section added to USAGE.md | | |
| Task 5: CHANGELOG entry added | | |
| At least 5 new meaningful commits | | |

### Understanding Self-Check

Answer briefly (1-3 sentences each):

1. What do you feel you genuinely understand about this assignment? (Not just
   "made it correct," but could explain to someone else or extend on your own.)

2. What did you make correct without fully understanding? Be honest. This is
   useful self-knowledge.

3. Where did you get stuck? What did you try before moving on or seeking help?

---

## Part 1: Short Response (1-2 paragraphs each)

**1. Your Path Through the Assignment**

How did you approach the assignment (reading the git history yourself, reading
the current files and noticing discrepancies, working mainly or entirely through
LLM tools, or some combination), and how did your approach change as you went? Which task was hardest, and why?

**2. Finding Drift**

Pick two specific documentation mismatches you found and repaired. For each:
describe what was wrong and where you found it, explain why you think the
drift happened (not just "it wasn't updated"; think about the circumstances
that let it persist), and describe who would have been confused or misled by it.

**3. The Deprecation Design**

In Task 5, you made design decisions about how to handle the deprecation of
`category:`: where the warning surfaces, what it says, who it is written for,
and how loud it is. Describe the choices you made and why.

The original code made a different choice: silent backward compatibility, no
warning. Hyrum's Law (from Chapter 1 of *Software Engineering at Google*) says
that with enough users, every observable behavior of a system will be depended
on by somebody, whether or not anyone promised it. Was the silence a reasonable
decision at the time? Answer in light of both Hyrum's Law and what you think
motivated the choice.

**4. Executable Documentation**

In Task 3, you encountered a doctest: a test embedded in a documentation
string. After working with it, do you think executable documentation (tests,
doctests, runnable examples) is more or less trustworthy than prose
documentation, and why? What did the state of the doctest in this repo tell you
about how it was being maintained?

---

## Part 2: Self-Documentation in Your Own Life

Answer B1 and B2.

**B1: Your personal documentation system**

Describe the tools and habits you use to document yourself across time: your
obligations, intentions, work, and memory. This might include calendars, to-do
apps, note-taking systems, journals, reminders, sticky notes, email flags,
time-trackers, voice memos, or anything else.

Be specific and concrete. Don't describe the ideal system; describe the one you
actually use, including the parts that don't work very well or that you've
abandoned.

**B2: Automation, drift, and responsibility**

Describe which parts of your personal documentation system are automated and
what that automation does for you, and a time you experienced something like
documentation drift, where your records, reminders, or notes no longer
accurately reflected reality. Has automation ever given you false confidence
that something was handled when it wasn't, or made it easier to avoid thinking
carefully about something you should have thought about?

Try to connect at least one observation here to something you encountered in the
Hunch repository.

---

## Part 3 Essay: Documentation, Memory, and Responsibility (500-700 words)

This is the most important question. Take your time.

Knuth argues that a program's documentation should be its primary artifact:
that software written for humans to read is fundamentally more maintainable
than software written to satisfy a compiler. Bush imagines a machine that
extends human memory perfectly, preserving every note, every association, every
trail of thought indefinitely.

Both visions share an assumption: that documentation is a commitment. Knuth's
literate programmer commits to maintaining the web; Bush's memex user commits to
feeding it faithfully. Both assume an author who cares about the future reader,
including their own future self.

Hunch replicates a story that plays out constantly in real software projects.
The documentation was written, and then it wasn't maintained. The code moved
on; the docs didn't. The project still works, but the written record is no
longer trustworthy.

Earlier this semester we read "Consequences of Cognitive Offloading: Boosting
Performance but Diminishing Memory" (linked on Moodle), which found that handing information to an
external store helps people perform and weakens their memory of what they handed
over. Documentation is offloading too: a project writes things down so that nobody
has to keep them in their head, and then readers rely on the record.

Write an essay that takes a position on the distance between these visions and
what happened to Hunch's record, grounded in your experience with this
assignment. Your essay should engage with both Knuth and Bush and use specific
examples from the Hunch repository and from your own work repairing it.

Possible directions (develop 2-3; you do not need all of them):

- What conditions would a real project need, in terms of tooling, culture,
  team discipline, or incentives, to sustain the correspondence between code
  and documentation that Knuth describes? Where did Hunch's development depart
  from those conditions, and why?

- Bush worries that human memory fades and offers a record that doesn't. The
  offloading article suggests a cost he doesn't weigh: the more we rely on a
  record, the less we hold ourselves, and so the less able we may be to notice
  when it goes wrong. Using a specific case from Hunch, argue whether the memex
  solves forgetting or moves the problem somewhere harder to see.

- In what ways does Hunch succeed at being a memex-like tool, and in what ways
  does it fall short? What would a truly reliable personal knowledge base require
  that Hunch does not currently provide? To test this, you could write one note
  you actually want to keep, run `hunch build`, and view the site (the README
  shows how). You do not need to commit this note.

- In at least one place in the Hunch repository, a document exists and is wrong:
  not missing, but actively misleading. Is that worse than if the document had
  never been written? Defend your position with reference to the specific case
  you found.

A thoughtful defense of any position is acceptable, including skepticism about
whether the standards Knuth and Bush set are achievable or even desirable,
provided it is honest and grounded in your experience.

---

## Submission

The written reflection is submitted separately from your artifact:

1. Write your responses in this document (or a copy of it, in any editor you like).
2. Upload the completed `WRITTEN.md` to the **HW4 Written** assignment on Gradescope.

### Formatting Guidelines

- Part 1: ~1-2 paragraphs each
- Part 2 (B1, B2): ~1-2 paragraphs each
- Part 3 (essay): ~500-700 words (slightly over is fine)
