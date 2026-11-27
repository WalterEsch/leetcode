# NeetCode 150, offline

Practice the NeetCode 150 in Python on your own computer, with no internet needed.
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

## Project layout

```
app.py          local web server (standard library only)
runner.py       runs a solution against a problem's tests in a separate process
start.bat       Windows launcher
static/         the browser app (HTML, CSS, JS)
problems/       one JSON file per problem: description, starter code, tests, hints
solutions/      your code (created as you work)
dev/            tools for checking problem files, plus reference solutions used to verify the tests
```

## Adding or editing a problem

Each problem is a JSON file in `problems/`, named after its `id`:

| Field | Meaning |
| --- | --- |
| `id`, `order`, `title`, `category`, `difficulty` | Shown in the problem list, sorted by `order` |
| `description` | Text with simple Markdown (`code`, **bold**, `- ` lists, fenced code blocks) |
| `function`, `params` | Method name on `class Solution` and its argument names |
| `starter` | Starter code shown in the editor |
| `tests` | List of `{"input": {param: value}, "expected": value}`. Add `"example": true` to show a test under the description |
| `hints` | List of hints, from gentlest to most direct |
| `compare` | Optional: `exact` (default), `unordered`, `unordered_nested` or `float` |
| `arg_types`, `return_type` | Optional: `linked_list` or `tree`, to convert lists to `ListNode`/`TreeNode` and back. Trees use LeetCode's level order with `null` for gaps |

To check every problem file, run `python dev/check_problems.py`. It also runs the reference solution in
`dev/reference/<id>.py`, if one exists, to make sure the tests themselves are correct.

Problem descriptions are written in our own words, not copied from LeetCode.
