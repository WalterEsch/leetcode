from ._common import existing

DESIGN_NOTE = ("Each test is a list of `operations` with matching `arguments`. The first operation creates the "
               "object, and the expected output lists what each call returns (`None` for calls that return nothing).")

PROBLEMS = [
    existing("valid-parentheses"),
    {
        "id": "min-stack", "title": "Min Stack", "difficulty": "Medium", "kind": "design", "class": "MinStack",
        "desc": f"""
Design a stack that also reports its smallest element. Every method must run in O(1) time.

- `MinStack()` creates an empty stack.
- `push(val)` puts `val` on top.
- `pop()` removes the top element.
- `top()` returns the top element.
- `getMin()` returns the smallest element in the stack.

`pop`, `top` and `getMin` are only called on a non-empty stack.

{DESIGN_NOTE}
""",
        "starter": """
class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass
""",
        "tests": [
            {"operations": ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
             "arguments": [[], [-2], [0], [-3], [], [], [], []]},
            {"operations": ["MinStack", "push", "getMin", "top"], "arguments": [[], [5], [], []]},
            {"operations": ["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
             "arguments": [[], [2], [2], [1], [], [], [], [], []]},
            {"operations": ["MinStack", "push", "push", "getMin", "pop", "getMin", "push", "getMin", "top"],
             "arguments": [[], [3], [5], [], [], [], [-1], [], []]},
            {"operations": ["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin", "top"],
             "arguments": [[], [0], [1], [0], [-5], [], [], [], [], [], []]},
        ],
        "hints": [
            "Keeping just one `min` variable fails after a `pop()` removes the minimum. What else do you need to remember?",
            "Store, with every element, the minimum of the stack at the moment it was pushed.",
            "Keep a second stack (or push pairs `(val, current_min)`). `getMin()` reads the top pair's min, and popping restores the previous min automatically.",
        ],
        "ref": """
class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append((val, min(val, self.s[-1][1]) if self.s else val))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
""",
    },
    {
        "id": "evaluate-reverse-polish-notation", "title": "Evaluate Reverse Polish Notation", "difficulty": "Medium",
        "desc": """
You are given `tokens`, an arithmetic expression in Reverse Polish Notation, where each operator comes after its two operands. Tokens are integers or one of `+`, `-`, `*`, `/`. Return the value of the expression.

Division between two integers **truncates toward zero** (so `-7 / 2` is `-3`). The expression is always valid and never divides by zero.

**Constraints**

- `1 <= len(tokens) <= 10^4`
""",
        "sig": "def evalRPN(self, tokens: List[str]) -> int:",
        "tests": [
            {"tokens": ["2", "1", "+", "3", "*"]}, {"tokens": ["4", "13", "5", "/", "+"]},
            {"tokens": ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]},
            {"tokens": ["42"]}, {"tokens": ["-7", "2", "/"]}, {"tokens": ["3", "-4", "-"]}, {"tokens": ["1", "2", "-", "3", "*"]},
        ],
        "expect": {0: 9, 1: 6, 2: 22, 4: -3},
        "hints": [
            "When you read an operator, which two numbers does it apply to?",
            "It applies to the two most recently seen values that haven't been used yet. A stack keeps exactly those.",
            "Push numbers. On an operator, pop `b` then `a`, push `a op b`. For division use `int(a / b)` to truncate toward zero, since `//` rounds down in Python.",
        ],
        "ref": """
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in "+-*/":
                b, a = st.pop(), st.pop()
                st.append(a + b if t == "+" else a - b if t == "-" else a * b if t == "*" else int(a / b))
            else:
                st.append(int(t))
        return st[0]
""",
    },
    {
        "id": "generate-parentheses", "title": "Generate Parentheses", "difficulty": "Medium",
        "desc": """
Given an integer `n`, return every string made of `n` pairs of parentheses that is well formed (every `(` is closed by a later `)`). The strings can be in any order.

**Constraints**

- `1 <= n <= 8`
""",
        "sig": "def generateParenthesis(self, n: int) -> List[str]:",
        "compare": "unordered",
        "tests": [{"n": 3}, {"n": 1}, {"n": 2}, {"n": 4}, {"n": 5}],
        "expect": {0: ["((()))", "(()())", "(())()", "()(())", "()()()"], 1: ["()"]},
        "hints": [
            "Build each string one character at a time. When is it allowed to add `(`? When is it allowed to add `)`?",
            "You can add `(` while fewer than `n` have been used. You can add `)` only while there are more `(` than `)` so far.",
            "Write a recursive (backtracking) function that tracks the counts of open and closed parentheses, and records the string when its length reaches `2 * n`.",
        ],
        "ref": """
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def go(s, o, c):
            if len(s) == 2 * n:
                res.append(s)
                return
            if o < n:
                go(s + "(", o + 1, c)
            if c < o:
                go(s + ")", o, c + 1)
        go("", 0, 0)
        return res
""",
    },
    {
        "id": "daily-temperatures", "title": "Daily Temperatures", "difficulty": "Medium",
        "desc": """
You are given a list `temperatures` of daily temperatures. Return a list `answer` where `answer[i]` is how many days you have to wait after day `i` to get a strictly warmer temperature. If no warmer day comes, `answer[i]` is `0`.

**Constraints**

- `1 <= len(temperatures) <= 10^5`
- `30 <= temperatures[i] <= 100`
""",
        "sig": "def dailyTemperatures(self, temperatures: List[int]) -> List[int]:",
        "tests": [
            {"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]}, {"temperatures": [30, 40, 50, 60]},
            {"temperatures": [30, 60, 90]}, {"temperatures": [90, 80, 70]}, {"temperatures": [50]},
            {"temperatures": [70, 70, 71]}, {"temperatures": [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]},
        ],
        "expect": {0: [1, 1, 4, 2, 1, 1, 0, 0]},
        "hints": [
            "Checking every later day for each day is O(n^2). Which days are still waiting for a warmer day?",
            "Keep the waiting days on a stack. Their temperatures are in decreasing order from bottom to top.",
            "For each new day, pop every waiting day with a lower temperature and set its answer to the difference in indices. Then push the new day.",
        ],
        "ref": """
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res
""",
    },
    {
        "id": "car-fleet", "title": "Car Fleet", "difficulty": "Medium",
        "desc": """
`n` cars drive toward a destination at mile `target` on a one-lane road. Car `i` starts at mile `position[i]` and drives at `speed[i]` miles per hour. All positions are different.

A car can't pass the car in front of it. When it catches up, it slows down and they drive together as one **fleet** at the slower speed. A car that catches up exactly at `target` still joins that fleet.

Return the number of fleets that arrive at the destination.

**Constraints**

- `1 <= n <= 10^5`
- `0 <= position[i] < target <= 10^6`
- `0 < speed[i] <= 10^6`
""",
        "sig": "def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:",
        "tests": [
            {"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]},
            {"target": 10, "position": [3], "speed": [3]},
            {"target": 100, "position": [0, 2, 4], "speed": [4, 2, 1]},
            {"target": 10, "position": [6, 8], "speed": [3, 2]},
            {"target": 10, "position": [0, 4, 2], "speed": [2, 1, 3]},
            {"target": 20, "position": [6, 2, 17], "speed": [3, 9, 2]},
        ],
        "expect": {0: 3, 1: 1, 2: 1},
        "hints": [
            "Work out when each car would reach the target if nothing were in its way: `(target - position) / speed`.",
            "Process cars from the closest to the target to the farthest. A car behind can only join the fleet directly ahead of it.",
            "Sort by position descending and keep a stack of fleet arrival times. If a car would arrive later than the fleet ahead, it starts a new fleet; otherwise it merges.",
        ],
        "ref": """
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets, slowest = 0, 0.0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if t > slowest:
                fleets += 1
                slowest = t
        return fleets
""",
    },
    {
        "id": "largest-rectangle-in-histogram", "title": "Largest Rectangle in Histogram", "difficulty": "Hard",
        "desc": """
You are given a list `heights` describing a histogram where every bar is 1 unit wide. Return the area of the largest rectangle that fits entirely inside the histogram.

**Constraints**

- `1 <= len(heights) <= 10^5`
- `0 <= heights[i] <= 10^4`
""",
        "sig": "def largestRectangleArea(self, heights: List[int]) -> int:",
        "tests": [
            {"heights": [2, 1, 5, 6, 2, 3]}, {"heights": [2, 4]}, {"heights": [1]}, {"heights": [0]},
            {"heights": [2, 1, 2]}, {"heights": [1, 2, 3, 4, 5]}, {"heights": [6, 2, 5, 4, 5, 1, 6]},
            {"heights": [3, 3, 3, 3]},
        ],
        "expect": {0: 10, 1: 4},
        "hints": [
            "For each bar, the biggest rectangle using that bar's full height stretches left and right until it hits a shorter bar.",
            "A stack of bars with increasing heights tells you, when a shorter bar arrives, exactly where each taller bar's rectangle has to stop.",
            "Keep a stack of `(start_index, height)`. When a shorter bar comes, pop taller bars, compute `height * (i - start)` for each, and push the new bar with the start index of the last bar popped. Empty the stack at the end.",
        ],
        "ref": """
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best, st = 0, []
        for i, h in enumerate(heights + [0]):
            start = i
            while st and st[-1][1] > h:
                s, sh = st.pop()
                best = max(best, sh * (i - s))
                start = s
            st.append((start, h))
        return best
""",
    },
]
