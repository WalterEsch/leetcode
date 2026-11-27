# NeetCode 150, offline

Practice all of the NeetCode 150 in Python on your own computer, with no internet needed.
It's built for flights: a browser app with a problem list, an editor, a **Run tests** button and hints.

## Requirements

- Python 3.9 or newer, from [python.org](https://www.python.org/downloads/) or the Microsoft Store.
- Any modern browser.

Nothing else needs to be installed. The app only uses the Python standard library.

## Start it

- **Windows:** double-click `start.bat`.
- **Any OS:** run `python app.py` in this folder.

Your browser opens at `http://127.0.0.1:8150/`. Leave the console window open while you practice,
and close it (or press Ctrl+C) when you're done.

## Using it

- Pick a problem on the left. Write your solution in the editor on the right.
- Press **Run tests** (or Ctrl+Enter) to run it against all the test cases. Failing tests show the input,
  the expected answer, your answer, any error and anything you printed.
- Click **Show a hint** when you're stuck. Hints go from a small nudge to the key idea.
- Your code saves automatically to `solutions/<problem>.py`. You can also open that file in VS Code.
  The app reloads it when you switch back to the browser.
- **Reset** brings back the starter code.

Editor keys: Tab and Shift+Tab indent and dedent, Enter keeps your indentation (and adds a level after `:`),
Ctrl+S saves, Ctrl+Enter runs the tests.

As on LeetCode, `List`, `Optional`, `ListNode`, `TreeNode`, `collections`, `heapq` and `math` are
already available in your solution. A run is stopped after 10 seconds, in case of an infinite loop.

## Problems

All 150 problems are included, grouped in the NeetCode roadmap order: Arrays & Hashing, Two Pointers,
Sliding Window, Stack, Binary Search, Linked List, Trees, Tries, Heap / Priority Queue, Backtracking, Graphs,
Advanced Graphs, 1-D and 2-D Dynamic Programming, Greedy, Intervals, Math & Geometry and Bit Manipulation.

Each one has a description written in our own words (not copied from LeetCode), starter code, 4 to 10 tests
including edge cases, and 3 hints that go from a gentle nudge to the key idea.

A few kinds of problems work slightly differently:

- **Design problems** (Min Stack, LRU Cache, Trie, ...) have you write a class. Each test is a list of
  `operations` with matching `arguments`, like on LeetCode, and checks what every call returns.
- **In-place problems** (Rotate Image, Reorder List, ...) return nothing. The tests check the argument you changed.
- **Problems with several right answers** (Course Schedule II, Alien Dictionary, Longest Palindromic Substring, ...)
  accept any valid answer. The "Expected" value shown is one of them.

## Project layout

```
app.py          local web server (standard library only)
runner.py       runs a solution against a problem's tests in a separate process
start.bat       Windows launcher
static/         the browser app (HTML, CSS, JS)
problems/       one JSON file per problem (generated from dev/src/)
solutions/      your code (created as you work)
dev/src/        problem sources: descriptions, tests, hints and reference solutions
dev/reference/  reference solutions (generated), used only to verify the tests
```

The reference solutions exist to prove the tests are right. Many are deliberately simple brute-force
versions, not model answers, so they won't spoil much. Still, don't open that folder if you'd rather not see them.

## Adding or editing a problem

Problem sources live in `dev/src/<category>.py`. After editing them, rebuild and check:

```
python dev/build_problems.py    # writes problems/*.json and dev/reference/*.py
python dev/check_problems.py    # checks every problem's tests against its reference solution
```

The build computes each test's expected answer by running the reference solution, and compares it with any
hand-written answers in `expect`. The fields of a source entry are:

| Field | Meaning |
| --- | --- |
| `id`, `title`, `difficulty` | Shown in the problem list. The category and order come from the file and position |
| `desc` | Text with simple Markdown (`code`, **bold**, `- ` lists, fenced code blocks) |
| `sig` | The method signature, for example `def twoSum(self, nums: List[int], target: int) -> List[int]:` |
| `starter_prefix` | Optional text above `class Solution:` (for example the `ListNode` definition as a comment) |
| `tests` | List of inputs, each a dict of argument name to value |
| `examples` | How many of the first tests to show under the description (default 2) |
| `expect` | Optional `{test_index: answer}` written by hand, to double check the reference |
| `hints` | List of hints, from gentlest to most direct |
| `ref` | Reference solution source code |
| `compare` | Optional: `exact` (default, floats compared approximately), `unordered`, `unordered_nested` or `custom` |
| `checker` | For `custom`: code defining `check(input, actual, expected) -> bool` |
| `arg_types`, `return_type` | Optional: `linked_list`, `linked_list_list` or `tree`, to convert lists to `ListNode`/`TreeNode` and back. Trees use LeetCode's level order with `None` for gaps |
| `output_from_arg` | For in-place problems: the argument whose final value is the answer |
| `kind`, `class`, `starter` | `kind: "design"` with the class name, and a hand-written starter |
| `prelude` | Code run before the solution, such as a custom `Node` class |
| `harness` | Code defining `call(problem, namespace, input)`, for problems that need custom setup (cycles, random pointers, round trips) |
