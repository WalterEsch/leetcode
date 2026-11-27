from .stack import DESIGN_NOTE

PROBLEMS = [
    {
        "id": "rotate-image", "title": "Rotate Image", "difficulty": "Medium",
        "desc": """
You are given an `n x n` `matrix`. Rotate it 90 degrees clockwise **in place**, without making another matrix. Your function returns nothing. The tests check `matrix` afterwards.

**Constraints**

- `1 <= n <= 20`
""",
        "sig": "def rotate(self, matrix: List[List[int]]) -> None:",
        "output_from_arg": "matrix",
        "tests": [{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]},
                  {"matrix": [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]},
                  {"matrix": [[1]]}, {"matrix": [[1, 2], [3, 4]]},
                  {"matrix": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]}],
        "expect": {0: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
        "hints": [
            "Where does the element at `(r, c)` end up after a clockwise rotation?",
            "It moves to `(c, n - 1 - r)`. A rotation can also be done as two simpler steps that each work in place.",
            "Transpose the matrix (swap `matrix[r][c]` with `matrix[c][r]` for `c > r`), then reverse each row.",
        ],
        "ref": """
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        rotated = [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]
        for r in range(n):
            matrix[r][:] = rotated[r]
""",
    },
    {
        "id": "spiral-matrix", "title": "Spiral Matrix", "difficulty": "Medium",
        "desc": """
You are given an `m x n` `matrix`. Return all of its elements in spiral order: across the top row left to right, down the right column, back along the bottom row, up the left column, then continue inward.

**Constraints**

- `1 <= m, n <= 10`
""",
        "sig": "def spiralOrder(self, matrix: List[List[int]]) -> List[int]:",
        "tests": [{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, {"matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]},
                  {"matrix": [[7]]}, {"matrix": [[1, 2, 3]]}, {"matrix": [[1], [2], [3]]}, {"matrix": [[1, 2], [3, 4], [5, 6], [7, 8]]}],
        "expect": {0: [1, 2, 3, 6, 9, 8, 7, 4, 5], 1: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]},
        "hints": [
            "Keep four boundaries: `top`, `bottom`, `left` and `right`.",
            "Walk the top row, then move `top` down. Walk the right column, then move `right` left. And so on for the bottom row and left column.",
            "Before walking the bottom row or the left column, check that the boundaries haven't crossed. Otherwise single rows or columns get added twice.",
        ],
        "ref": """
class Solution:
    def spiralOrder(self, matrix):
        res = []
        m = [row[:] for row in matrix]
        while m:
            res += m.pop(0)
            m = [list(r) for r in zip(*m)][::-1]
        return res
""",
    },
    {
        "id": "set-matrix-zeroes", "title": "Set Matrix Zeroes", "difficulty": "Medium",
        "desc": """
You are given an `m x n` integer `matrix`. If a cell is `0`, set its entire row and column to `0`. Do it **in place**. Your function returns nothing. The tests check `matrix` afterwards.

Can you use only O(1) extra space?

**Constraints**

- `1 <= m, n <= 200`
""",
        "sig": "def setZeroes(self, matrix: List[List[int]]) -> None:",
        "output_from_arg": "matrix",
        "tests": [{"matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}, {"matrix": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]},
                  {"matrix": [[1]]}, {"matrix": [[0]]}, {"matrix": [[1, 0], [1, 1]]}, {"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 0]]}],
        "expect": {0: [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 1: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]},
        "hints": [
            "If you zero rows and columns while scanning, the new zeros cause more rows and columns to be zeroed. First find out which rows and columns to clear.",
            "Recording the zero rows and columns in two sets takes O(m + n) space.",
            "For O(1) space, use the first row and first column as the markers, with one extra flag for whether the first column itself needs clearing. Clear the inner cells first, then the first row and column.",
        ],
        "ref": """
class Solution:
    def setZeroes(self, matrix):
        rows = {r for r, row in enumerate(matrix) for v in row if v == 0}
        cols = {c for row in matrix for c, v in enumerate(row) if v == 0}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0
""",
    },
    {
        "id": "happy-number", "title": "Happy Number", "difficulty": "Easy",
        "desc": """
Start with a positive integer `n`. Replace it with the sum of the squares of its digits, and repeat. If this eventually reaches `1`, `n` is a **happy** number. Otherwise it loops forever without reaching `1`.

Return `True` if `n` is happy.

**Constraints**

- `1 <= n <= 2^31 - 1`
""",
        "sig": "def isHappy(self, n: int) -> bool:",
        "tests": [{"n": 19}, {"n": 2}, {"n": 1}, {"n": 7}, {"n": 4}, {"n": 100}, {"n": 2147483647}],
        "expect": {0: True, 1: False},
        "hints": [
            "If the process doesn't reach 1, it must eventually repeat a number. How can you detect a repeat?",
            "Keep a set of numbers you have already seen.",
            "Loop until `n == 1` (happy) or `n` is already in the set (not happy). Floyd's slow/fast pointers also work, with O(1) space.",
        ],
        "ref": """
class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
""",
    },
    {
        "id": "plus-one", "title": "Plus One", "difficulty": "Easy",
        "desc": """
A non-negative integer is given as a list of its digits, `digits`, most significant first, with no leading zeros (except for the number 0). Add one to the integer and return the resulting list of digits.

**Constraints**

- `1 <= len(digits) <= 100`
""",
        "sig": "def plusOne(self, digits: List[int]) -> List[int]:",
        "tests": [{"digits": [1, 2, 3]}, {"digits": [4, 3, 2, 1]}, {"digits": [9]}, {"digits": [0]}, {"digits": [9, 9, 9]},
                  {"digits": [1, 9, 9]}, {"digits": [8, 9]}],
        "examples": 3,
        "expect": {0: [1, 2, 4], 1: [4, 3, 2, 2], 2: [1, 0]},
        "hints": [
            "Work from the last digit, the way you'd add by hand.",
            "A `9` becomes `0` and carries 1 to the left. Any other digit just goes up by one, and you're done.",
            "If every digit was `9`, the answer is `[1]` followed by all zeros.",
        ],
        "ref": """
class Solution:
    def plusOne(self, digits):
        return [int(c) for c in str(int("".join(map(str, digits))) + 1)]
""",
    },
    {
        "id": "powx-n", "title": "Pow(x, n)", "difficulty": "Medium",
        "desc": """
Compute `x` raised to the power `n`, where `x` is a float and `n` is an integer that may be negative. Don't use `**` or `pow`. Aim for O(log n) multiplications.

Answers within `10^-5` (relative) of the expected value are accepted.

**Constraints**

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`, and `x` is not 0 when `n` is negative.
""",
        "sig": "def myPow(self, x: float, n: int) -> float:",
        "tests": [{"x": 2.0, "n": 10}, {"x": 2.1, "n": 3}, {"x": 2.0, "n": -2}, {"x": 1.0, "n": 2147483647}, {"x": 0.5, "n": 0},
                  {"x": -2.0, "n": 3}, {"x": 1.00001, "n": 123456}],
        "examples": 3,
        "expect": {0: 1024.0, 1: 9.261, 2: 0.25},
        "hints": [
            "Multiplying `x` by itself `n` times is too slow for `n` around 2 billion.",
            "`x^n = (x^(n/2))^2` when `n` is even, and `x * x^(n-1)` when it's odd. Each step halves the problem.",
            "Handle negative `n` with `1 / myPow(x, -n)`. Then use repeated squaring: while `n > 0`, multiply the result by `x` if `n` is odd, square `x`, and halve `n`.",
        ],
        "ref": """
class Solution:
    def myPow(self, x, n):
        return float(x ** n)
""",
    },
    {
        "id": "multiply-strings", "title": "Multiply Strings", "difficulty": "Medium",
        "desc": """
You are given two non-negative integers, `num1` and `num2`, as strings. Return their product, also as a string.

Don't convert the whole inputs to integers directly. Work with the digits, as you would on paper.

**Constraints**

- `1 <= len(num1), len(num2) <= 200`, no leading zeros except for `"0"`.
""",
        "sig": "def multiply(self, num1: str, num2: str) -> str:",
        "tests": [{"num1": "2", "num2": "3"}, {"num1": "123", "num2": "456"}, {"num1": "0", "num2": "52"}, {"num1": "9", "num2": "99"},
                  {"num1": "999", "num2": "999"}, {"num1": "123456789", "num2": "987654321"},
                  {"num1": "1" * 60, "num2": "9" * 60}],
        "examples": 3,
        "expect": {0: "6", 1: "56088", 2: "0"},
        "hints": [
            "In long multiplication, digit `i` of `num1` times digit `j` of `num2` lands in a predictable position of the answer.",
            "Counting positions from the right, the product of those digits belongs at position `i + j` (if `i` and `j` are also counted from the right).",
            "Make a list of `len(num1) + len(num2)` zeros, add every digit product into its position, then carry from right to left. Strip leading zeros, returning `\"0\"` if nothing is left.",
        ],
        "ref": """
class Solution:
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))
""",
    },
    {
        "id": "detect-squares", "title": "Detect Squares", "difficulty": "Medium", "kind": "design", "class": "DetectSquares",
        "desc": f"""
Design a structure for points on a plane.

- `DetectSquares()` creates an empty structure.
- `add(point)` adds `point = [x, y]`. The same point can be added more than once, and each copy counts separately.
- `count(point)` returns how many ways you can pick three stored points that, together with `point`, form a square with **positive area** whose sides are parallel to the axes.

{DESIGN_NOTE}
""",
        "starter": """
class DetectSquares:
    def __init__(self):
        pass

    def add(self, point: List[int]) -> None:
        pass

    def count(self, point: List[int]) -> int:
        pass
""",
        "tests": [
            {"operations": ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"],
             "arguments": [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]},
            {"operations": ["DetectSquares", "count"], "arguments": [[], [[0, 0]]]},
            {"operations": ["DetectSquares", "add", "add", "add", "add", "count", "count"],
             "arguments": [[], [[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]], [[0, 0]], [[1, 1]]]},
            {"operations": ["DetectSquares", "add", "add", "add", "add", "add", "count", "count"],
             "arguments": [[], [[5, 5]], [[5, 7]], [[7, 5]], [[3, 5]], [[3, 7]], [[5, 5]], [[5, 6]]]},
        ],
        "hints": [
            "Store how many times each point has been added, in a dictionary keyed by `(x, y)`.",
            "Given the query point, pick a candidate for the opposite (diagonal) corner. The other two corners are then fixed.",
            "Loop over the stored points `(px, py)` that form a diagonal with `(x, y)`: `abs(px - x) == abs(py - y)` and `px != x`. Add `count[(px, py)] * count[(x, py)] * count[(px, y)]`.",
        ],
        "ref": """
class DetectSquares:
    def __init__(self):
        self.pts = []

    def add(self, point):
        self.pts.append(tuple(point))

    def count(self, point):
        x, y = point
        total = 0
        cnt = collections.Counter(self.pts)
        for (px, py), k in cnt.items():
            if px != x and abs(px - x) == abs(py - y):
                total += k * cnt[(x, py)] * cnt[(px, y)]
        return total
""",
    },
]
