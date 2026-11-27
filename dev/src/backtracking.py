PROBLEMS = [
    {
        "id": "subsets", "title": "Subsets", "difficulty": "Medium",
        "desc": """
You are given a list `nums` of distinct integers. Return every possible subset (the power set), including the empty subset. The subsets, and the numbers within each subset, can be in any order, but the same subset must not appear twice.

**Constraints**

- `1 <= len(nums) <= 10`
""",
        "sig": "def subsets(self, nums: List[int]) -> List[List[int]]:",
        "compare": "unordered_nested",
        "tests": [{"nums": [1, 2, 3]}, {"nums": [0]}, {"nums": [5, -1]}, {"nums": [1, 2, 3, 4]}, {"nums": [9, 8, 7, 6, 5]}],
        "expect": {0: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], 1: [[], [0]]},
        "hints": [
            "For each number there are two choices: put it in the subset or leave it out.",
            "Make those choices one number at a time with a recursive function `dfs(i, current)`.",
            "At `i == len(nums)`, record a copy of `current`. Otherwise append `nums[i]`, recurse, pop it, and recurse again without it. (You can also start from `[[]]` and, for each number, add it to a copy of every subset so far.)",
        ],
        "ref": """
class Solution:
    def subsets(self, nums):
        res = [[]]
        for x in nums:
            res += [s + [x] for s in res]
        return res
""",
    },
    {
        "id": "combination-sum", "title": "Combination Sum", "difficulty": "Medium",
        "desc": """
You are given a list of distinct positive integers `candidates` and a positive integer `target`. Return every distinct combination of candidates that adds up to `target`. The **same number can be used any number of times**.

Two combinations are the same if they use each number the same number of times. The combinations, and the numbers inside them, can be in any order.

**Constraints**

- `1 <= len(candidates) <= 30`, `2 <= candidates[i] <= 40`
- `1 <= target <= 40`
""",
        "sig": "def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:",
        "compare": "unordered_nested",
        "tests": [{"candidates": [2, 3, 6, 7], "target": 7}, {"candidates": [2, 3, 5], "target": 8},
                  {"candidates": [2], "target": 1}, {"candidates": [7, 3, 2], "target": 18}, {"candidates": [8, 7, 4, 3], "target": 11}],
        "examples": 3,
        "expect": {0: [[2, 2, 3], [7]], 1: [[2, 2, 2, 2], [2, 3, 3], [3, 5]], 2: []},
        "hints": [
            "Build combinations with backtracking, subtracting from the remaining target as you go.",
            "To avoid producing `[2, 3]` and `[3, 2]` separately, only allow choosing candidates at or after the index of the last one you chose.",
            "`dfs(i, remaining, path)`: if `remaining == 0`, record `path`; if it is negative or `i` is past the end, stop. Otherwise either use `candidates[i]` again (stay at `i`) or move on to `i + 1`.",
        ],
        "ref": """
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def go(i, rem, path):
            if rem == 0:
                res.append(path)
                return
            if rem < 0 or i == len(candidates):
                return
            go(i, rem - candidates[i], path + [candidates[i]])
            go(i + 1, rem, path)
        go(0, target, [])
        return res
""",
    },
    {
        "id": "combination-sum-ii", "title": "Combination Sum II", "difficulty": "Medium",
        "desc": """
You are given a list of positive integers `candidates` (which may contain duplicates) and a `target`. Return every distinct combination of candidates that adds up to `target`, where **each position in `candidates` can be used at most once**.

The answer must not contain the same combination twice. The combinations, and the numbers inside them, can be in any order.

**Constraints**

- `1 <= len(candidates) <= 100`, `1 <= candidates[i] <= 50`
- `1 <= target <= 30`
""",
        "sig": "def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:",
        "compare": "unordered_nested",
        "tests": [{"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8}, {"candidates": [2, 5, 2, 1, 2], "target": 5},
                  {"candidates": [3], "target": 2}, {"candidates": [1, 1, 1, 1, 1], "target": 3},
                  {"candidates": [4, 4, 2, 1, 4, 2, 2, 1, 3], "target": 6}],
        "expect": {0: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], 1: [[1, 2, 2], [5]]},
        "hints": [
            "Sort the candidates first so that equal values sit next to each other.",
            "Backtrack as in Combination Sum, but move to `i + 1` after using a candidate, since each can be used once.",
            "To skip duplicate combinations: when looping over choices at one level of the recursion, skip `candidates[j]` if `j > start` and `candidates[j] == candidates[j - 1]`.",
        ],
        "ref": """
class Solution:
    def combinationSum2(self, candidates, target):
        found = set()
        c = sorted(candidates)
        def go(i, rem, path):
            if rem == 0:
                found.add(tuple(path))
                return
            if rem < 0 or i == len(c):
                return
            go(i + 1, rem - c[i], path + [c[i]])
            go(i + 1, rem, path)
        go(0, target, [])
        return [list(t) for t in found]
""",
    },
    {
        "id": "permutations", "title": "Permutations", "difficulty": "Medium",
        "desc": """
You are given a list `nums` of distinct integers. Return every possible ordering (permutation) of them. The permutations can be listed in any order.

**Constraints**

- `1 <= len(nums) <= 6`
""",
        "sig": "def permute(self, nums: List[int]) -> List[List[int]]:",
        "compare": "unordered",
        "tests": [{"nums": [1, 2, 3]}, {"nums": [0, 1]}, {"nums": [1]}, {"nums": [4, -2, 9, 0]}, {"nums": [1, 2, 3, 4, 5]}],
        "examples": 3,
        "expect": {0: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], 1: [[0, 1], [1, 0]], 2: [[1]]},
        "hints": [
            "Build each permutation one position at a time, choosing any number that has not been used yet.",
            "Track which numbers are used (a set or a boolean list) as you recurse.",
            "`dfs(path)`: if `len(path) == len(nums)`, record a copy. Otherwise, for each unused number, mark it used, append it, recurse, then undo both.",
        ],
        "ref": """
class Solution:
    def permute(self, nums):
        return [list(p) for p in itertools.permutations(nums)]
""",
    },
    {
        "id": "subsets-ii", "title": "Subsets II", "difficulty": "Medium",
        "desc": """
You are given a list `nums` that may contain duplicates. Return every possible subset, without returning the same subset twice. (Subsets that contain the same values the same number of times count as the same.) Order doesn't matter.

**Constraints**

- `1 <= len(nums) <= 10`
""",
        "sig": "def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:",
        "compare": "unordered_nested",
        "tests": [{"nums": [1, 2, 2]}, {"nums": [0]}, {"nums": [4, 4, 4, 1, 4]}, {"nums": [1, 1]}, {"nums": [3, 1, 2, 1]}],
        "expect": {0: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], 1: [[], [0]]},
        "hints": [
            "Sort `nums` so duplicates are next to each other.",
            "When you decide to skip a value, skip **all** copies of it. Otherwise the same subset gets built in two different ways.",
            "In `dfs(i, path)`: include `nums[i]` and recurse on `i + 1`; then, to exclude it, advance `i` past every element equal to `nums[i]` before recursing.",
        ],
        "ref": """
class Solution:
    def subsetsWithDup(self, nums):
        res = {()}
        for x in sorted(nums):
            res |= {s + (x,) for s in res}
        return [list(s) for s in res]
""",
    },
    {
        "id": "word-search", "title": "Word Search", "difficulty": "Medium",
        "desc": """
You are given an `m x n` grid of characters `board` and a string `word`. Return `True` if `word` can be spelled by moving between horizontally or vertically adjacent cells, using each cell at most once.

**Constraints**

- `1 <= m, n <= 6`
- `1 <= len(word) <= 15`
""",
        "sig": "def exist(self, board: List[List[str]], word: str) -> bool:",
        "tests": [
            {"board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "word": "ABCCED"},
            {"board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "word": "SEE"},
            {"board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "word": "ABCB"},
            {"board": [["a"]], "word": "a"}, {"board": [["a", "b"]], "word": "ba"}, {"board": [["a", "a"]], "word": "aaa"},
            {"board": [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "word": "AAB"},
        ],
        "examples": 3,
        "expect": {0: True, 1: True, 2: False},
        "hints": [
            "Try starting the word from every cell.",
            "From a cell, explore the four neighbors recursively, but don't reuse a cell that's already in the current path.",
            "`dfs(r, c, i)` returns `True` once `i == len(word)`. Otherwise, check the bounds and that `board[r][c] == word[i]`, temporarily mark the cell (for example set it to `'#'`), recurse into the neighbors with `i + 1`, then restore the cell.",
        ],
        "ref": """
class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        def dfs(r, c, i, seen):
            if i == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or (r, c) in seen or board[r][c] != word[i]:
                return False
            seen.add((r, c))
            ok = any(dfs(r + a, c + b, i + 1, seen) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            seen.discard((r, c))
            return ok
        return any(dfs(r, c, 0, set()) for r in range(m) for c in range(n))
""",
    },
    {
        "id": "palindrome-partitioning", "title": "Palindrome Partitioning", "difficulty": "Medium",
        "desc": """
You are given a string `s`. Split it into pieces so that every piece is a palindrome. Return every possible way of doing this. Each way is a list of pieces in order. The ways themselves can be in any order.

**Constraints**

- `1 <= len(s) <= 16`, lowercase letters only.
""",
        "sig": "def partition(self, s: str) -> List[List[str]]:",
        "compare": "unordered",
        "tests": [{"s": "aab"}, {"s": "a"}, {"s": "racecar"}, {"s": "abba"}, {"s": "aaaa"}, {"s": "abc"}],
        "expect": {0: [["a", "a", "b"], ["aa", "b"]], 1: [["a"]]},
        "hints": [
            "Choose the first piece, then partition whatever is left. That is a smaller version of the same problem.",
            "The first piece must be a palindrome, so try every prefix `s[i:j]` that is one.",
            "`dfs(i, path)`: if `i == len(s)`, record `path`. Otherwise, for every `j > i` where `s[i:j]` is a palindrome, append it, call `dfs(j)`, then pop it.",
        ],
        "ref": """
class Solution:
    def partition(self, s):
        if not s:
            return [[]]
        res = []
        for j in range(1, len(s) + 1):
            if s[:j] == s[:j][::-1]:
                res += [[s[:j]] + rest for rest in self.partition(s[j:])]
        return res
""",
    },
    {
        "id": "letter-combinations-of-a-phone-number", "title": "Letter Combinations of a Phone Number",
        "difficulty": "Medium",
        "desc": """
You are given a string `digits` made of the digits `2` to `9`. On a phone keypad each digit maps to letters: 2 = abc, 3 = def, 4 = ghi, 5 = jkl, 6 = mno, 7 = pqrs, 8 = tuv, 9 = wxyz.

Return every letter string the digits could spell, in any order. If `digits` is empty, return an empty list.

**Constraints**

- `0 <= len(digits) <= 4`
""",
        "sig": "def letterCombinations(self, digits: str) -> List[str]:",
        "compare": "unordered",
        "tests": [{"digits": "23"}, {"digits": ""}, {"digits": "2"}, {"digits": "79"}, {"digits": "234"}, {"digits": "9999"}],
        "examples": 3,
        "expect": {0: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], 1: [], 2: ["a", "b", "c"]},
        "hints": [
            "Each digit adds one letter choice. How many strings are there in total?",
            "Build the strings one digit at a time, either recursively or by extending a list of partial strings.",
            "Start with `[\"\"]` and, for each digit, replace the list with every partial string plus every letter for that digit. Remember the empty-input case.",
        ],
        "ref": """
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        keys = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return ["".join(p) for p in itertools.product(*(keys[d] for d in digits))]
""",
    },
    {
        "id": "n-queens", "title": "N-Queens", "difficulty": "Hard",
        "desc": """
Place `n` chess queens on an `n x n` board so that no two queens attack each other (no two share a row, column or diagonal). Return every distinct solution, in any order.

Each solution is a list of `n` strings, one per row, where `"Q"` is a queen and `"."` is an empty square.

**Constraints**

- `1 <= n <= 9`
""",
        "sig": "def solveNQueens(self, n: int) -> List[List[str]]:",
        "compare": "unordered",
        "tests": [{"n": 4}, {"n": 1}, {"n": 2}, {"n": 3}, {"n": 5}, {"n": 6}],
        "expect": {0: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]], 1: [["Q"]]},
        "hints": [
            "Every row holds exactly one queen, so place them one row at a time.",
            "To check whether a square is attacked in O(1), track which columns and diagonals are taken. Squares on one diagonal share `r - c`; on the other diagonal they share `r + c`.",
            "Backtrack over rows: for each column that is free in all three sets, place the queen, recurse on the next row, then remove it. When all `n` rows are filled, build the board strings.",
        ],
        "ref": """
class Solution:
    def solveNQueens(self, n):
        res = []
        for perm in itertools.permutations(range(n)):
            if len({r - c for r, c in enumerate(perm)}) == n and len({r + c for r, c in enumerate(perm)}) == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in perm])
        return res
""",
    },
]
