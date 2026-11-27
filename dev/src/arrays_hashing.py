from ._common import existing

SUDOKU_VALID = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def _sudoku_with(changes):
    b = [row[:] for row in SUDOKU_VALID]
    for r, c, v in changes:
        b[r][c] = v
    return b


EMPTY = [["."] * 9 for _ in range(9)]

PROBLEMS = [
    existing("contains-duplicate"),
    {
        "id": "valid-anagram", "title": "Valid Anagram", "difficulty": "Easy",
        "desc": """
You are given two strings `s` and `t`. Return `True` if `t` is an anagram of `s`, meaning it uses exactly the same letters the same number of times (possibly in a different order). Otherwise return `False`.

**Constraints**

- `1 <= len(s), len(t) <= 5 * 10^4`
- Both strings contain only lowercase English letters.
""",
        "sig": "def isAnagram(self, s: str, t: str) -> bool:",
        "tests": [
            {"s": "anagram", "t": "nagaram"}, {"s": "rat", "t": "car"},
            {"s": "a", "t": "ab"}, {"s": "ab", "t": "ba"}, {"s": "aacc", "t": "ccac"},
            {"s": "listen", "t": "silent"}, {"s": "x", "t": "x"}, {"s": "abcd", "t": "abce"},
        ],
        "expect": {0: True, 1: False, 4: False},
        "hints": [
            "If the strings have different lengths, can they be anagrams?",
            "Count how many times each letter appears in each string and compare the counts.",
            "A dictionary (or `collections.Counter`) of letter counts works in O(n). Sorting both strings and comparing also works in O(n log n).",
        ],
        "ref": """
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
""",
    },
    existing("two-sum"),
    existing("group-anagrams"),
    {
        "id": "top-k-frequent-elements", "title": "Top K Frequent Elements", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums` and an integer `k`. Return the `k` values that appear most often in `nums`. The answer can be in any order.

The tests guarantee that the answer is unique.

**Constraints**

- `1 <= len(nums) <= 10^5`
- `1 <= k <=` number of distinct values in `nums`
- Try for better than O(n log n).
""",
        "sig": "def topKFrequent(self, nums: List[int], k: int) -> List[int]:",
        "compare": "unordered",
        "tests": [
            {"nums": [1, 1, 1, 2, 2, 3], "k": 2}, {"nums": [7], "k": 1},
            {"nums": [4, 4, 4, 5, 5, 6, 6, 6, 6], "k": 1}, {"nums": [-1, -1, 2, 2, 2, 3], "k": 2},
            {"nums": [1, 2, 3], "k": 3}, {"nums": [5, 3, 5, 3, 5, 9, 9, 9, 9, 1], "k": 3},
        ],
        "expect": {0: [1, 2], 1: [7]},
        "hints": [
            "Start by counting how often each value appears.",
            "Sorting the counts works but is O(n log n). A heap of size `k` gets you O(n log k).",
            "Bucket sort gives O(n): make a list of buckets where bucket `i` holds the values that appear exactly `i` times, then read buckets from the highest count down until you have `k` values.",
        ],
        "ref": """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in collections.Counter(nums).most_common(k)]
""",
    },
    {
        "id": "encode-and-decode-strings", "title": "Encode and Decode Strings", "difficulty": "Medium",
        "desc": """
Design two methods. `encode` turns a list of strings into a single string, and `decode` turns that single string back into the original list.

The strings can contain **any** characters, including commas, digits, `#` and other characters you might be tempted to use as a separator.

Each test calls `encode(strs)`, passes the result to `decode`, and checks that you get `strs` back.

**Constraints**

- `0 <= len(strs) <= 200`
- `0 <= len(strs[i]) <= 200`
""",
        "starter": """
class Solution:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass
""",
        "function": "encode", "params": ["strs"],
        "harness": """
def call(problem, ns, inp):
    encoded = ns["Solution"]().encode(inp["strs"])
    if not isinstance(encoded, str):
        raise TypeError(f"encode() must return a str, but it returned {type(encoded).__name__}")
    return ns["Solution"]().decode(encoded)
""",
        "tests": [
            {"strs": ["neet", "code", "love", "you"]}, {"strs": ["we", "say", ":", "yes"]},
            {"strs": []}, {"strs": [""]}, {"strs": ["", "", ""]},
            {"strs": ["4#abc", "#", "12#", "a,b,c"]}, {"strs": ["hello world", "  ", "\\n", "tab\tchar"]},
            {"strs": ["x" * 150, "y"]},
        ],
        "hints": [
            "Joining with a separator like `,` breaks if a string contains that separator. How can `decode` know where each string ends without relying on its content?",
            "Write each string's length in front of it, so the decoder knows exactly how many characters to read.",
            "Encode each string as `str(len(s)) + '#' + s`. To decode, read digits up to the `#`, then take that many characters, and repeat.",
        ],
        "ref": """
class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.index("#", i)
            n = int(s[i:j])
            res.append(s[j + 1:j + 1 + n])
            i = j + 1 + n
        return res
""",
    },
    {
        "id": "product-of-array-except-self", "title": "Product of Array Except Self", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums`. Return a list `answer` where `answer[i]` is the product of every element of `nums` **except** `nums[i]`.

Do it in O(n) time **without using division**.

**Constraints**

- `2 <= len(nums) <= 10^5`
- `-30 <= nums[i] <= 30`
""",
        "sig": "def productExceptSelf(self, nums: List[int]) -> List[int]:",
        "tests": [
            {"nums": [1, 2, 3, 4]}, {"nums": [-1, 1, 0, -3, 3]}, {"nums": [2, 3]},
            {"nums": [0, 0, 2]}, {"nums": [5, 0, 2, 3]}, {"nums": [-2, -3, 4, 1, 2]}, {"nums": [1, 1, 1, 1]},
        ],
        "expect": {0: [24, 12, 8, 6], 1: [0, 0, 9, 0, 0]},
        "hints": [
            "The product of everything except `nums[i]` equals (product of everything to its left) times (product of everything to its right).",
            "Make one pass from the left computing prefix products, and one pass from the right computing suffix products.",
            "You can store prefix products in the answer list, then sweep from the right with a running suffix product and multiply it in. That uses O(1) extra space.",
        ],
        "ref": """
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
""",
    },
    {
        "id": "valid-sudoku", "title": "Valid Sudoku", "difficulty": "Medium",
        "desc": """
You are given a partly filled 9 x 9 Sudoku `board`. Each cell holds a digit `"1"` to `"9"` or `"."` for empty. Return `True` if the filled cells follow the rules:

- no digit repeats in any row,
- no digit repeats in any column, and
- no digit repeats in any of the nine 3 x 3 boxes.

You only need to check the filled cells. The board does not need to be solvable.
""",
        "sig": "def isValidSudoku(self, board: List[List[str]]) -> bool:",
        "tests": [
            {"board": SUDOKU_VALID}, {"board": _sudoku_with([(0, 0, "8"), (3, 0, "8")])},
            {"board": EMPTY}, {"board": _sudoku_with([(0, 2, "5")])},
            {"board": _sudoku_with([(1, 1, "9")])}, {"board": _sudoku_with([(8, 0, "1")])},
            {"board": _sudoku_with([(2, 0, "1"), (2, 3, "3")])},
        ],
        "expect": {0: True, 1: False, 2: True},
        "hints": [
            "Check rows, columns and boxes separately, using a set to spot repeats.",
            "The 3 x 3 box for cell `(r, c)` can be identified by `(r // 3, c // 3)`.",
            "In a single pass, keep a set per row, per column and per box. If a digit is already in any of the three sets for its cell, return `False`.",
        ],
        "ref": """
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                keys = [("r", r, v), ("c", c, v), ("b", r // 3, c // 3, v)]
                if any(k in seen for k in keys):
                    return False
                seen.update(keys)
        return True
""",
    },
    {
        "id": "longest-consecutive-sequence", "title": "Longest Consecutive Sequence", "difficulty": "Medium",
        "desc": """
You are given an unsorted list of integers `nums`. Return the length of the longest run of consecutive integers (like `4, 5, 6, 7`) that can be formed from values in `nums`. The values do not need to be next to each other in the list.

Aim for O(n) time.

**Constraints**

- `0 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
""",
        "sig": "def longestConsecutive(self, nums: List[int]) -> int:",
        "tests": [
            {"nums": [100, 4, 200, 1, 3, 2]}, {"nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]}, {"nums": []},
            {"nums": [1]}, {"nums": [1, 2, 0, 1]}, {"nums": [9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]},
            {"nums": [10, 30, 20]}, {"nums": list(range(50000, 0, -1))},
        ],
        "expect": {0: 4, 1: 9, 2: 0},
        "hints": [
            "Sorting solves it in O(n log n). To get O(n), what fast lookup structure could help?",
            "Put every number in a set. A number `x` starts a run only if `x - 1` is not in the set.",
            "For each start of a run, count upward (`x + 1`, `x + 2`, ...) while the numbers are in the set. Each number is visited a constant number of times overall.",
        ],
        "ref": """
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                y = x
                while y + 1 in s:
                    y += 1
                best = max(best, y - x + 1)
        return best
""",
    },
]
