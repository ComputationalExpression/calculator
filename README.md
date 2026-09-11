# Activity 2: The Calculation Report

|Item |       |
|:----|:------|
|Week |Week 3, Friday |
|Type |In-class activity |
|Due  |See the [course schedule](https://computationalexpression.com/schedule/) |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

Your program takes two whole numbers and prints a report of every arithmetic operation this
course has covered, formatted with lines that you build rather than type out. You decide how
the two numbers are entered, and your prompt has to say so.

Everything here comes from the last two weeks. If a step
confuses you, please ask about it while you are still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this activity you should be able to:

* read a line of input, split it into pieces, and convert those pieces to numbers
* choose your own input format and write a prompt that tells the user exactly how to use it
* use `+`, `-`, `*`, `/`, and `%` on integers, and say what each one gives back
* print the same text three ways: with commas, by joining strings, and with an f-string
* build a repeated line of characters instead of typing the characters out
* write comments that explain why a line exists
* write a markdown document, including a fenced code block, and preview it before pushing

## The problem

Your program reads a single line holding two whole numbers. You choose how the two numbers
are separated (a space, a comma, anything you like), and your prompt has to say so, so that
someone who has never seen your code still knows exactly what to type.

Two examples, to make the flexibility concrete. Separate with a space:

```text
Enter two whole numbers separated by a space: 17 5
```

or separate with a comma instead:

```text
Enter two whole numbers separated by a comma, like 17,5: 17,5
```

Whichever you pick, once `first` is `17` and `second` is `5`, your program prints exactly
this:

```text
==================================
CALCULATION REPORT: 17 and 5
==================================
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 % 5 = 2
==================================
```

Note that `17 / 5` gives `3.4` and not `3`. Division always hands back a float.

### Example run

Here is the whole interaction, prompt and output together, exactly as it would look if you
picked a comma as your separator:

```text
$ uv run python src/main.py
Enter two whole numbers separated by a comma, like 17,5: 17,5
==================================
CALCULATION REPORT: 17 and 5
==================================
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 % 5 = 2
==================================
```

Your own prompt and separator can look different. The report itself always looks like this.

### Three lines, three ways to print

The sum, difference, and product lines look identical once printed. Write each one a different
way, because having written all three at least once is the point:

|Line |How to print it |
|:----|:---------------|
|The sum |Commas inside a single `print()`, letting Python space the pieces for you |
|The difference |Joining strings with `+`, converting the numbers with `str()` |
|The product |An f-string |

The quotient and remainder lines are yours to write whichever way you prefer.

### The line you build instead of type

`banner` is 34 equals signs. Build it with string repetition, so that changing `34` to `50`
would change the whole report. Do not type out 34 characters.

## Getting started

Open `src/main.py` and work through the `TODO` markers in order. Run it as you go, rather than
writing the whole thing and running it once:

```text
uv run python src/main.py
```

Put your name on the `Author:` line at the top of the file, and delete each `TODO` marker as
you finish that step.

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade.

|Level |What it looks like |
|:-----|:------------------|
|**Complete** |The prompt says how to enter the numbers, the report prints correctly, and `docs/summary.md` is answered |
|**Partial** |The numbers are read and converted and some of the report prints, but the prompt does not say how to enter them or the formatting is unfinished |
|**Incomplete** |Little or no meaningful attempt |

Run the automated checks yourself, as many times as you like, from the top folder of this
repository rather than from inside `src`:

```text
uv run gatorgrade --config gatorgrade.yml
```

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

## Summary writing

Complete [`docs/summary.md`](docs/summary.md). Three questions, answered fully, with a minimum
word count of `100`. One of them asks you to paste your output inside a fenced code block, so
preview the file before you push and confirm it renders the way you expect.

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded.

**In the terminal:**

```text
git add src/main.py docs/summary.md
git commit -m "Complete the calculation report"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it, which is `git add`
2. Type a message in the box at the top, then click the checkmark, which is `git commit`
3. Click **Sync Changes** (or the up arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
