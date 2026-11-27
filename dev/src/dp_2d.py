PROBLEMS = [
    {
        "id": "unique-paths", "title": "Unique Paths", "difficulty": "Medium",
        "desc": """
A robot starts in the top-left corner of an `m x n` grid and wants to reach the bottom-right corner. It can only move right or down. Return the number of different paths.

**Constraints**

- `1 <= m, n <= 100`, and the answer is at most `2 * 10^9`.
""",
        "sig": "def uniquePaths(self, m: int, n: int) -> int:",
        "tests": [{"m": 3, "n": 7}, {"m": 3, "n": 2}, {"m": 1, "n": 1}, {"m": 1, "n": 10}, {"m": 7, "n": 3}, {"m": 10, "n": 10}],
        "expect": {0: 28, 1: 3},
        "hints": [
            "The robot reaches a cell either from the cell above or from the cell to the left.",
            "So `paths[r][c] = paths[r - 1][c] + paths[r][c - 1]`, with every cell in the first row and first column equal to 1.",
            "Fill the table row by row. You only need one row at a time. (Or use combinatorics: choose which `m - 1` of the `m + n - 2` moves go down.)",
        ],
        "ref": """
class Solution:
    def uniquePaths(self, m, n):
        return math.comb(m + n - 2, m - 1)
""",
    },
    {
        "id": "longest-common-subsequence", "title": "Longest Common Subsequence", "difficulty": "Medium",
        "desc": """
You are given two strings `text1` and `text2`. Return the length of their longest common subsequence: the longest string that can be formed from both by deleting some characters without changing the order of the rest. Return `0` if they share nothing.

**Constraints**

- `1 <= len(text1), len(text2) <= 1000`, lowercase letters only.
""",
        "sig": "def longestCommonSubsequence(self, text1: str, text2: str) -> int:",
        "tests": [{"text1": "abcde", "text2": "ace"}, {"text1": "abc", "text2": "abc"}, {"text1": "abc", "text2": "def"},
                  {"text1": "a", "text2": "a"}, {"text1": "bsbininm", "text2": "jmjkbkjkv"}, {"text1": "ezupkr", "text2": "ubmrapg"},
                  {"text1": "oxcpqrsvwf", "text2": "shmtulqrypy"}],
        "examples": 3,
        "expect": {0: 3, 1: 3, 2: 0},
        "hints": [
            "Compare the strings from the end (or the start). If the last characters match, they can be part of the subsequence.",
            "Let `dp[i][j]` be the answer for `text1[i:]` and `text2[j:]`. If `text1[i] == text2[j]`, `dp[i][j] = 1 + dp[i + 1][j + 1]`; otherwise it is `max(dp[i + 1][j], dp[i][j + 1])`.",
            "Fill a `(len1 + 1) x (len2 + 1)` table from the bottom-right, with zeros along the last row and column. Return `dp[0][0]`.",
        ],
        "ref": """
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @functools.lru_cache(None)
        def go(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + go(i + 1, j + 1)
            return max(go(i + 1, j), go(i, j + 1))
        return go(0, 0)
""",
    },
    {
        "id": "best-time-to-buy-and-sell-stock-with-cooldown", "title": "Best Time to Buy and Sell Stock with Cooldown",
        "difficulty": "Medium",
        "desc": """
You are given a list `prices` where `prices[i]` is a stock's price on day `i`. You may make as many trades as you like, with two rules:

- you can hold at most one share at a time (sell before you buy again), and
- after you sell, you can't buy on the next day (a one-day cooldown).

Return the maximum profit.

**Constraints**

- `1 <= len(prices) <= 5000`
""",
        "sig": "def maxProfit(self, prices: List[int]) -> int:",
        "tests": [{"prices": [1, 2, 3, 0, 2]}, {"prices": [1]}, {"prices": [1, 2, 4]}, {"prices": [5, 4, 3, 2]},
                  {"prices": [6, 1, 3, 2, 4, 7]}, {"prices": [1, 4, 2, 7, 1, 9]}, {"prices": [2, 1, 4, 5, 2, 9, 7]}],
        "expect": {0: 3, 1: 0},
        "hints": [
            "Each day you are in one of three states: holding a share, just sold (cooling down), or free to buy.",
            "Write how each state's best profit for today depends on yesterday's states.",
            "`hold = max(hold, free - price)`, `sold = hold_yesterday + price`, `free = max(free, sold_yesterday)`. Start with `hold = -inf`, `sold = free = 0`, and return `max(sold, free)`.",
        ],
        "ref": """
class Solution:
    def maxProfit(self, prices):
        @functools.lru_cache(None)
        def go(i, holding):
            if i >= len(prices):
                return 0
            skip = go(i + 1, holding)
            if holding:
                return max(skip, prices[i] + go(i + 2, False))
            return max(skip, -prices[i] + go(i + 1, True))
        return go(0, False)
""",
    },
    {
        "id": "coin-change-ii", "title": "Coin Change II", "difficulty": "Medium",
        "desc": """
You are given an `amount` and coin denominations `coins`, with an unlimited number of each coin. Return the number of different **combinations** of coins that add up to `amount`. Different orders of the same coins count as one combination.

**Constraints**

- `0 <= amount <= 5000`
- `1 <= len(coins) <= 300`, all distinct.
""",
        "sig": "def change(self, amount: int, coins: List[int]) -> int:",
        "tests": [{"amount": 5, "coins": [1, 2, 5]}, {"amount": 3, "coins": [2]}, {"amount": 10, "coins": [10]},
                  {"amount": 0, "coins": [7]}, {"amount": 100, "coins": [1, 5, 10, 25, 50]}, {"amount": 7, "coins": [2, 4]}],
        "examples": 3,
        "expect": {0: 4, 1: 0, 2: 1, 3: 1},
        "hints": [
            "Counting `1 + 2` and `2 + 1` separately is the classic mistake. How can you make each combination be counted once?",
            "Process the coins one at a time. With each new coin, count the ways that use it zero or more times on top of the earlier coins.",
            "Use `dp[a]` = number of ways to make `a`, with `dp[0] = 1`. With the coin loop on the **outside**: for each coin `c`, for `a` from `c` to `amount`, add `dp[a - c]` to `dp[a]`.",
        ],
        "ref": """
class Solution:
    def change(self, amount, coins):
        @functools.lru_cache(None)
        def go(i, a):
            if a == 0:
                return 1
            if i == len(coins) or a < 0:
                return 0
            return go(i, a - coins[i]) + go(i + 1, a)
        return go(0, amount)
""",
    },
    {
        "id": "target-sum", "title": "Target Sum", "difficulty": "Medium",
        "desc": """
You are given a list of non-negative integers `nums` and an integer `target`. Put a `+` or `-` in front of every number, and add them all up. Return the number of different sign choices that give exactly `target`.

**Constraints**

- `1 <= len(nums) <= 20`
- `0 <= nums[i] <= 1000`, `sum(nums) <= 1000`
""",
        "sig": "def findTargetSumWays(self, nums: List[int], target: int) -> int:",
        "tests": [{"nums": [1, 1, 1, 1, 1], "target": 3}, {"nums": [1], "target": 1}, {"nums": [1], "target": 2},
                  {"nums": [0, 0, 1], "target": 1}, {"nums": [2, 3, 5], "target": 0}, {"nums": [7, 9, 3, 8, 0, 2, 4, 8, 3, 9], "target": 0}],
        "examples": 3,
        "expect": {0: 5, 1: 1, 2: 0, 3: 4},
        "hints": [
            "Trying all `2^n` sign choices works for small `n`. Many partial choices reach the same running total, though.",
            "Track how many ways each running total can be reached after the first `i` numbers.",
            "Keep a dictionary `{sum: ways}` starting at `{0: 1}`. For each number `x`, build a new dictionary where every `s` contributes its ways to both `s + x` and `s - x`. Return the ways for `target`.",
        ],
        "ref": """
class Solution:
    def findTargetSumWays(self, nums, target):
        return sum(1 for signs in itertools.product((1, -1), repeat=len(nums))
                   if sum(s * x for s, x in zip(signs, nums)) == target)
""",
    },
    {
        "id": "interleaving-string", "title": "Interleaving String", "difficulty": "Medium",
        "desc": """
You are given three strings `s1`, `s2` and `s3`. Return `True` if `s3` can be formed by interleaving `s1` and `s2`: taking all characters of both strings, keeping each string's characters in their original order, and merging them into one string.

**Constraints**

- `0 <= len(s1), len(s2) <= 100`, `0 <= len(s3) <= 200`
""",
        "sig": "def isInterleave(self, s1: str, s2: str, s3: str) -> bool:",
        "tests": [{"s1": "aabcc", "s2": "dbbca", "s3": "aadbbcbcac"}, {"s1": "aabcc", "s2": "dbbca", "s3": "aadbbbaccc"},
                  {"s1": "", "s2": "", "s3": ""}, {"s1": "a", "s2": "", "s3": "c"}, {"s1": "ab", "s2": "cd", "s3": "acbd"},
                  {"s1": "abc", "s2": "def", "s3": "abcdefg"}, {"s1": "aa", "s2": "ab", "s3": "aaba"}],
        "examples": 3,
        "expect": {0: True, 1: False, 2: True},
        "hints": [
            "If the lengths don't add up, the answer is `False`. Otherwise, each character of `s3` comes from either `s1` or `s2`.",
            "The state is how many characters you have used from each string: `(i, j)`. Then the next character of `s3` is `s3[i + j]`.",
            "`dp(i, j)` is `True` if `s1[i] == s3[i + j]` and `dp(i + 1, j)`, or `s2[j] == s3[i + j]` and `dp(i, j + 1)`. Memoize it, or fill a 2-D table.",
        ],
        "ref": """
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        @functools.lru_cache(None)
        def go(i, j):
            if i + j == len(s3):
                return True
            return (i < len(s1) and s1[i] == s3[i + j] and go(i + 1, j)) or \\
                   (j < len(s2) and s2[j] == s3[i + j] and go(i, j + 1))
        return go(0, 0)
""",
    },
    {
        "id": "longest-increasing-path-in-a-matrix", "title": "Longest Increasing Path in a Matrix", "difficulty": "Hard",
        "desc": """
You are given an `m x n` integer `matrix`. From any cell you can move up, down, left or right. Return the length of the longest path along which the values are **strictly increasing**.

**Constraints**

- `1 <= m, n <= 200`
""",
        "sig": "def longestIncreasingPath(self, matrix: List[List[int]]) -> int:",
        "tests": [{"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}, {"matrix": [[3, 4, 5], [3, 2, 6], [2, 2, 1]]}, {"matrix": [[1]]},
                  {"matrix": [[7, 7], [7, 7]]}, {"matrix": [[1, 2, 3], [6, 5, 4], [7, 8, 9]]}, {"matrix": [[1, 2], [4, 3]]}],
        "examples": 3,
        "expect": {0: 4, 1: 4, 2: 1},
        "hints": [
            "Because values must strictly increase, a path can never loop back to a cell. So the longest path starting at a cell is fixed.",
            "Compute `longest(r, c)`, the longest increasing path that starts at `(r, c)`, and remember the results.",
            "`longest(r, c) = 1 + max(longest(neighbor))` over neighbors with a larger value (or 1 if there are none). Memoize it with a dictionary or `functools.lru_cache`, and return the max over all cells.",
        ],
        "ref": """
class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        cells = sorted((matrix[r][c], r, c) for r in range(m) for c in range(n))
        best = {}
        for v, r, c in reversed(cells):
            best[(r, c)] = 1 + max([best[(x, y)] for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > v] or [0])
        return max(best.values())
""",
    },
    {
        "id": "distinct-subsequences", "title": "Distinct Subsequences", "difficulty": "Hard",
        "desc": """
You are given two strings `s` and `t`. Return how many different subsequences of `s` are equal to `t`. Two subsequences are different if they use different positions of `s`.

**Constraints**

- `1 <= len(s), len(t) <= 1000`, letters only. The answer fits in a 32-bit integer.
""",
        "sig": "def numDistinct(self, s: str, t: str) -> int:",
        "tests": [{"s": "rabbbit", "t": "rabbit"}, {"s": "babgbag", "t": "bag"}, {"s": "a", "t": "b"}, {"s": "aaa", "t": "a"},
                  {"s": "abc", "t": "abcd"}, {"s": "aaaaa", "t": "aa"}, {"s": "ddd", "t": "dd"}],
        "examples": 3,
        "expect": {0: 3, 1: 5, 2: 0},
        "hints": [
            "Walk through both strings. At `s[i]`, you can always skip it. If it equals `t[j]`, you can also use it to match `t[j]`.",
            "Let `dp(i, j)` be the number of ways to form `t[j:]` from `s[i:]`. If `j == len(t)` there is exactly 1 way; if `i == len(s)` there are 0.",
            "`dp(i, j) = dp(i + 1, j) + (dp(i + 1, j + 1) if s[i] == t[j] else 0)`. Memoize it, or fill a table from the end.",
        ],
        "ref": """
class Solution:
    def numDistinct(self, s, t):
        @functools.lru_cache(None)
        def go(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            return go(i + 1, j) + (go(i + 1, j + 1) if s[i] == t[j] else 0)
        return go(0, 0)
""",
    },
    {
        "id": "edit-distance", "title": "Edit Distance", "difficulty": "Medium",
        "desc": """
You are given two strings `word1` and `word2`. Return the minimum number of operations to turn `word1` into `word2`, where each operation is one of:

- insert a character,
- delete a character, or
- replace a character.

**Constraints**

- `0 <= len(word1), len(word2) <= 500`
""",
        "sig": "def minDistance(self, word1: str, word2: str) -> int:",
        "tests": [{"word1": "horse", "word2": "ros"}, {"word1": "intention", "word2": "execution"}, {"word1": "", "word2": "abc"},
                  {"word1": "same", "word2": "same"}, {"word1": "abc", "word2": ""}, {"word1": "kitten", "word2": "sitting"},
                  {"word1": "a", "word2": "b"}],
        "expect": {0: 3, 1: 5},
        "hints": [
            "Compare the strings character by character. If `word1[i] == word2[j]`, no operation is needed for that pair.",
            "Otherwise you try all three operations, and each one moves to a smaller subproblem: insert `(i, j + 1)`, delete `(i + 1, j)`, replace `(i + 1, j + 1)`.",
            "`dp(i, j)` is the cost for `word1[i:]` and `word2[j:]`. Base cases: if one string is used up, the cost is the length of what's left of the other. Memoize, or fill a table.",
        ],
        "ref": """
class Solution:
    def minDistance(self, word1, word2):
        @functools.lru_cache(None)
        def go(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return go(i + 1, j + 1)
            return 1 + min(go(i + 1, j), go(i, j + 1), go(i + 1, j + 1))
        return go(0, 0)
""",
    },
    {
        "id": "burst-balloons", "title": "Burst Balloons", "difficulty": "Hard",
        "desc": """
You have `n` balloons in a row, and balloon `i` has the number `nums[i]`. Bursting balloon `i` earns `nums[left] * nums[i] * nums[right]` coins, where `left` and `right` are its current neighbors. A missing neighbor (past either end) counts as `1`. After a burst, its neighbors become adjacent.

Burst all the balloons and return the most coins you can collect.

**Constraints**

- `1 <= n <= 300`
- `0 <= nums[i] <= 100`
""",
        "sig": "def maxCoins(self, nums: List[int]) -> int:",
        "tests": [{"nums": [3, 1, 5, 8]}, {"nums": [1, 5]}, {"nums": [7]}, {"nums": [0, 0]}, {"nums": [2, 3, 4]},
                  {"nums": [9, 76, 64, 21]}],
        "expect": {0: 167, 1: 10},
        "hints": [
            "Choosing which balloon to burst **first** is hard, because the neighbors keep changing. What about choosing which balloon to burst **last**?",
            "If balloon `k` is the last one burst between boundaries `l` and `r`, its neighbors at that moment are exactly `l` and `r`. The two sides are then independent subproblems.",
            "Pad `nums` with a `1` at each end. `dp(l, r) = max over l < k < r of nums[l] * nums[k] * nums[r] + dp(l, k) + dp(k, r)`. The answer is `dp(0, n + 1)`.",
        ],
        "ref": """
class Solution:
    def maxCoins(self, nums):
        a = [1] + nums + [1]
        @functools.lru_cache(None)
        def go(l, r):
            return max((a[l] * a[k] * a[r] + go(l, k) + go(k, r) for k in range(l + 1, r)), default=0)
        return go(0, len(a) - 1)
""",
    },
    {
        "id": "regular-expression-matching", "title": "Regular Expression Matching", "difficulty": "Hard",
        "desc": """
Implement pattern matching with two special characters:

- `.` matches any single character.
- `*` matches zero or more of the character just before it.

Given a string `s` and a pattern `p`, return `True` if the pattern matches the **whole** string.

**Constraints**

- `1 <= len(s) <= 20`, `1 <= len(p) <= 20`
- `s` has lowercase letters; `p` has lowercase letters, `.` and `*`. Every `*` follows a valid character.
""",
        "sig": "def isMatch(self, s: str, p: str) -> bool:",
        "tests": [{"s": "aa", "p": "a"}, {"s": "aa", "p": "a*"}, {"s": "ab", "p": ".*"}, {"s": "aab", "p": "c*a*b"},
                  {"s": "mississippi", "p": "mis*is*p*."}, {"s": "ab", "p": ".*c"}, {"s": "aaa", "p": "a*a"},
                  {"s": "a", "p": "ab*"}, {"s": "abcd", "p": "d*"}],
        "examples": 3,
        "expect": {0: False, 1: True, 2: True, 3: True, 4: False},
        "hints": [
            "Match from the left. Check whether the first characters match (`p[j] == s[i]` or `p[j] == '.'`), and look ahead to see whether `p[j + 1]` is `*`.",
            "If the next pattern character is `*`, there are two options: use the `x*` zero times (skip 2 pattern characters), or, if the first characters match, use it once more (advance in `s` only).",
            "Write `dp(i, j)` for whether `s[i:]` matches `p[j:]`, using the two cases above, and memoize it. The base case: `j == len(p)` matches only if `i == len(s)`.",
        ],
        "ref": """
import re

class Solution:
    def isMatch(self, s, p):
        return re.fullmatch(p, s) is not None
""",
    },
]
