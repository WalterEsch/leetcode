PROBLEMS = [
    {
        "id": "climbing-stairs", "title": "Climbing Stairs", "difficulty": "Easy",
        "desc": """
You are climbing a staircase with `n` steps. Each move, you climb either 1 or 2 steps. Return the number of distinct ways to reach the top.

**Constraints**

- `1 <= n <= 45`
""",
        "sig": "def climbStairs(self, n: int) -> int:",
        "tests": [{"n": 2}, {"n": 3}, {"n": 1}, {"n": 5}, {"n": 10}, {"n": 45}],
        "expect": {0: 2, 1: 3},
        "hints": [
            "To land on step `n`, your last move came from step `n - 1` or from step `n - 2`.",
            "So `ways(n) = ways(n - 1) + ways(n - 2)`. Plain recursion repeats the same work many times. Remember results.",
            "Iterate from the bottom with two variables, like computing Fibonacci numbers: `a, b = b, a + b`.",
        ],
        "ref": """
class Solution:
    def climbStairs(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a
""",
    },
    {
        "id": "min-cost-climbing-stairs", "title": "Min Cost Climbing Stairs", "difficulty": "Easy",
        "desc": """
You are given a list `cost` where `cost[i]` is the price of stepping on stair `i`. After paying for a stair you can climb 1 or 2 stairs. You can start on stair `0` or stair `1`.

Return the minimum cost to get past the last stair (the "top" is just beyond the end of the list).

**Constraints**

- `2 <= len(cost) <= 1000`
- `0 <= cost[i] <= 999`
""",
        "sig": "def minCostClimbingStairs(self, cost: List[int]) -> int:",
        "tests": [{"cost": [10, 15, 20]}, {"cost": [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]}, {"cost": [0, 0]},
                  {"cost": [5, 1]}, {"cost": [1, 2, 3, 4, 5]}, {"cost": [0, 2, 2, 1]}],
        "expect": {0: 15, 1: 6},
        "hints": [
            "Let `best[i]` be the cheapest cost to stand on stair `i` (before paying for it).",
            "`best[i] = min(best[i - 1] + cost[i - 1], best[i - 2] + cost[i - 2])`, with `best[0] = best[1] = 0`.",
            "The answer is `best[len(cost)]`. You only ever need the previous two values, so two variables are enough.",
        ],
        "ref": """
class Solution:
    def minCostClimbingStairs(self, cost):
        a = b = 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b
""",
    },
    {
        "id": "house-robber", "title": "House Robber", "difficulty": "Medium",
        "desc": """
Houses along a street hold `nums[i]` money each. You can't rob two **adjacent** houses (the alarm would go off). Return the most money you can rob.

**Constraints**

- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 400`
""",
        "sig": "def rob(self, nums: List[int]) -> int:",
        "tests": [{"nums": [1, 2, 3, 1]}, {"nums": [2, 7, 9, 3, 1]}, {"nums": [5]}, {"nums": [2, 1, 1, 2]},
                  {"nums": [0, 0, 0]}, {"nums": [10, 1, 1, 10, 1, 1, 10]}],
        "expect": {0: 4, 1: 12},
        "hints": [
            "At each house you either rob it (and skip the previous one) or skip it.",
            "`best(i) = max(best(i - 1), best(i - 2) + nums[i])`.",
            "Iterate keeping two values, `prev2` and `prev1`: for each `x`, the new best is `max(prev1, prev2 + x)`.",
        ],
        "ref": """
class Solution:
    def rob(self, nums):
        a = b = 0
        for x in nums:
            a, b = b, max(b, a + x)
        return b
""",
    },
    {
        "id": "house-robber-ii", "title": "House Robber II", "difficulty": "Medium",
        "desc": """
This is House Robber, but the houses are arranged in a **circle**: the first and last houses are neighbors. You still can't rob two adjacent houses. Return the most money you can rob.

**Constraints**

- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 1000`
""",
        "sig": "def rob(self, nums: List[int]) -> int:",
        "tests": [{"nums": [2, 3, 2]}, {"nums": [1, 2, 3, 1]}, {"nums": [1, 2, 3]}, {"nums": [7]}, {"nums": [4, 1]},
                  {"nums": [200, 3, 140, 20, 10]}, {"nums": [1, 3, 1, 3, 100]}],
        "examples": 3,
        "expect": {0: 3, 1: 4, 2: 3},
        "hints": [
            "Because of the circle, you can't rob both the first and the last house.",
            "So the answer is the better of two straight-line problems: one without the last house, and one without the first.",
            "Reuse your House Robber solution: `max(rob_line(nums[1:]), rob_line(nums[:-1]))`, with a special case for a single house.",
        ],
        "ref": """
class Solution:
    def rob(self, nums):
        def line(arr):
            a = b = 0
            for x in arr:
                a, b = b, max(b, a + x)
            return b
        return nums[0] if len(nums) == 1 else max(line(nums[1:]), line(nums[:-1]))
""",
    },
    {
        "id": "longest-palindromic-substring", "title": "Longest Palindromic Substring", "difficulty": "Medium",
        "desc": """
You are given a string `s`. Return its longest substring that reads the same forwards and backwards. If there are several of the same maximum length, any of them is accepted.

**Constraints**

- `1 <= len(s) <= 1000`, letters and digits only.
""",
        "sig": "def longestPalindrome(self, s: str) -> str:",
        "compare": "custom",
        "checker": """
def check(inp, actual, expected):
    return (isinstance(actual, str) and len(actual) == len(expected)
            and actual == actual[::-1] and actual in inp["s"])
""",
        "tests": [{"s": "babad"}, {"s": "cbbd"}, {"s": "a"}, {"s": "ac"}, {"s": "forgeeksskeegfor"},
                  {"s": "abacdfgdcaba"}, {"s": "aaaa"}, {"s": "racecar"}],
        "hints": [
            "Every palindrome mirrors around its center. A center is either a single character (odd length) or the gap between two characters (even length).",
            "There are `2n - 1` possible centers. From each, expand outward while the characters on both sides match.",
            "For each `i`, expand from `(i, i)` and from `(i, i + 1)`, and keep the longest palindrome found. This is O(n^2) time and O(1) space.",
        ],
        "ref": """
class Solution:
    def longestPalindrome(self, s):
        best = ""
        for i in range(len(s)):
            for j in range(i + len(best) + 1, len(s) + 1):
                t = s[i:j]
                if t == t[::-1]:
                    best = t
        return best
""",
    },
    {
        "id": "palindromic-substrings", "title": "Palindromic Substrings", "difficulty": "Medium",
        "desc": """
You are given a string `s`. Return how many of its substrings are palindromes. Substrings at different positions count separately, even if they contain the same letters.

**Constraints**

- `1 <= len(s) <= 1000`, lowercase letters only.
""",
        "sig": "def countSubstrings(self, s: str) -> int:",
        "tests": [{"s": "abc"}, {"s": "aaa"}, {"s": "a"}, {"s": "abba"}, {"s": "racecar"}, {"s": "aabaa"}],
        "expect": {0: 3, 1: 6},
        "hints": [
            "Every single character is a palindrome. How do longer ones grow from shorter ones?",
            "Expand around each of the `2n - 1` centers, as in Longest Palindromic Substring.",
            "Each successful expansion step from a center is one more palindrome, so add 1 to the count every time the two sides match.",
        ],
        "ref": """
class Solution:
    def countSubstrings(self, s):
        return sum(s[i:j] == s[i:j][::-1] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
""",
    },
    {
        "id": "decode-ways", "title": "Decode Ways", "difficulty": "Medium",
        "desc": """
Letters are encoded as numbers: `"A" -> "1"`, `"B" -> "2"`, ..., `"Z" -> "26"`. You are given a string `s` of digits. Return how many ways it can be decoded back into letters.

A piece can't have a leading zero (`"06"` is not valid, but `"6"` is). If `s` can't be decoded at all, return `0`.

**Constraints**

- `1 <= len(s) <= 100`
""",
        "sig": "def numDecodings(self, s: str) -> int:",
        "tests": [{"s": "12"}, {"s": "226"}, {"s": "06"}, {"s": "10"}, {"s": "27"}, {"s": "11106"}, {"s": "100"},
                  {"s": "2611055971756562"}],
        "examples": 3,
        "expect": {0: 2, 1: 3, 2: 0, 3: 1},
        "hints": [
            "The last piece is either the last single digit, or the last two digits.",
            "Let `dp[i]` be the number of ways to decode `s[:i]`. A single digit adds `dp[i - 1]` if it isn't `'0'`; a two-digit piece adds `dp[i - 2]` if it's between `10` and `26`.",
            "Start with `dp[0] = 1`, fill the table left to right, and return `dp[len(s)]`. You only need the previous two values.",
        ],
        "ref": """
class Solution:
    def numDecodings(self, s):
        @functools.lru_cache(None)
        def ways(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            total = ways(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                total += ways(i + 2)
            return total
        return ways(0)
""",
    },
    {
        "id": "coin-change", "title": "Coin Change", "difficulty": "Medium",
        "desc": """
You are given coin denominations `coins` and a total `amount`. You have an unlimited number of each coin. Return the fewest coins needed to make exactly `amount`, or `-1` if it can't be done.

**Constraints**

- `1 <= len(coins) <= 12`
- `0 <= amount <= 10^4`
""",
        "sig": "def coinChange(self, coins: List[int], amount: int) -> int:",
        "tests": [{"coins": [1, 2, 5], "amount": 11}, {"coins": [2], "amount": 3}, {"coins": [1], "amount": 0},
                  {"coins": [186, 419, 83, 408], "amount": 6249}, {"coins": [2, 5, 10, 1], "amount": 27},
                  {"coins": [3, 7], "amount": 5}, {"coins": [1, 3, 4], "amount": 6}],
        "examples": 3,
        "expect": {0: 3, 1: -1, 2: 0, 6: 2},
        "hints": [
            "Always picking the biggest coin doesn't always work (try `coins = [1, 3, 4]`, `amount = 6`).",
            "Let `dp[a]` be the fewest coins for amount `a`. The last coin used could be any coin `c <= a`.",
            "`dp[0] = 0`, and `dp[a] = 1 + min(dp[a - c])` over coins `c <= a`. Fill it from 1 up to `amount`, using infinity for amounts that can't be made.",
        ],
        "ref": """
class Solution:
    def coinChange(self, coins, amount):
        dist = {0: 0}
        q = collections.deque([0])
        while q:
            a = q.popleft()
            if a == amount:
                return dist[a]
            for c in coins:
                b = a + c
                if b <= amount and b not in dist:
                    dist[b] = dist[a] + 1
                    q.append(b)
        return -1
""",
    },
    {
        "id": "maximum-product-subarray", "title": "Maximum Product Subarray", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums`. Return the largest product of any non-empty contiguous subarray.

**Constraints**

- `1 <= len(nums) <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
""",
        "sig": "def maxProduct(self, nums: List[int]) -> int:",
        "tests": [{"nums": [2, 3, -2, 4]}, {"nums": [-2, 0, -1]}, {"nums": [-2]}, {"nums": [-2, 3, -4]},
                  {"nums": [0, 2]}, {"nums": [-1, -2, -3, 0]}, {"nums": [2, -5, -2, -4, 3]}],
        "examples": 3,
        "expect": {0: 6, 1: 0, 2: -2, 3: 24},
        "hints": [
            "Unlike sums, a very negative product can become the largest one after multiplying by another negative.",
            "So at each position, track both the largest and the smallest product of a subarray ending there.",
            "For each `x`, the new max is `max(x, x * cur_max, x * cur_min)` and the new min is `min(x, x * cur_max, x * cur_min)` (compute both from the old values). Keep the best max seen.",
        ],
        "ref": """
class Solution:
    def maxProduct(self, nums):
        best = nums[0]
        for i in range(len(nums)):
            p = 1
            for j in range(i, len(nums)):
                p *= nums[j]
                best = max(best, p)
        return best
""",
    },
    {
        "id": "word-break", "title": "Word Break", "difficulty": "Medium",
        "desc": """
You are given a string `s` and a list of words `wordDict`. Return `True` if `s` can be split into a sequence of one or more dictionary words. Words can be reused.

**Constraints**

- `1 <= len(s) <= 300`
- `1 <= len(wordDict) <= 1000`, all words distinct.
""",
        "sig": "def wordBreak(self, s: str, wordDict: List[str]) -> bool:",
        "tests": [{"s": "leetcode", "wordDict": ["leet", "code"]}, {"s": "applepenapple", "wordDict": ["apple", "pen"]},
                  {"s": "catsandog", "wordDict": ["cats", "dog", "sand", "and", "cat"]},
                  {"s": "a", "wordDict": ["b"]}, {"s": "aaaaaaa", "wordDict": ["aaaa", "aaa"]},
                  {"s": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", "wordDict": ["a", "aa", "aaa", "aaaa", "aaaaa"]},
                  {"s": "cars", "wordDict": ["car", "ca", "rs"]}],
        "examples": 3,
        "expect": {0: True, 1: True, 2: False},
        "hints": [
            "Trying every way to split the string with plain recursion can be exponential (see the long `aaa...b` test).",
            "Let `dp[i]` be `True` if `s[:i]` can be split into words. Then `dp[i]` is `True` if some word ends exactly at `i` and `dp[start of that word]` is `True`.",
            "Set `dp[0] = True`. For each `i` from 1 to `len(s)`, check every word `w` with `s[i - len(w):i] == w` and `dp[i - len(w)]`. Return `dp[len(s)]`.",
        ],
        "ref": """
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        ok = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            ok[i] = any(ok[j] and s[j:i] in words for j in range(i))
        return ok[-1]
""",
    },
    {
        "id": "longest-increasing-subsequence", "title": "Longest Increasing Subsequence", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums`. Return the length of the longest **strictly increasing** subsequence. A subsequence keeps the original order but may skip elements.

**Constraints**

- `1 <= len(nums) <= 2500`
""",
        "sig": "def lengthOfLIS(self, nums: List[int]) -> int:",
        "tests": [{"nums": [10, 9, 2, 5, 3, 7, 101, 18]}, {"nums": [0, 1, 0, 3, 2, 3]}, {"nums": [7, 7, 7, 7, 7, 7, 7]},
                  {"nums": [1]}, {"nums": [4, 10, 4, 3, 8, 9]}, {"nums": [5, 4, 3, 2, 1]}, {"nums": [1, 3, 6, 7, 9, 4, 10, 5, 6]}],
        "examples": 3,
        "expect": {0: 4, 1: 4, 2: 1},
        "hints": [
            "Let `dp[i]` be the length of the longest increasing subsequence that **ends** at index `i`.",
            "`dp[i] = 1 + max(dp[j])` over all `j < i` with `nums[j] < nums[i]` (or just 1). The answer is the max of `dp`. That's O(n^2).",
            "For O(n log n), keep a list `tails` where `tails[k]` is the smallest possible tail of an increasing subsequence of length `k + 1`. For each number, replace the first tail `>=` it using `bisect_left`, or append it.",
        ],
        "ref": """
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
""",
    },
    {
        "id": "partition-equal-subset-sum", "title": "Partition Equal Subset Sum", "difficulty": "Medium",
        "desc": """
You are given a list of positive integers `nums`. Return `True` if it can be split into two groups with equal sums.

**Constraints**

- `1 <= len(nums) <= 200`
- `1 <= nums[i] <= 100`
""",
        "sig": "def canPartition(self, nums: List[int]) -> bool:",
        "tests": [{"nums": [1, 5, 11, 5]}, {"nums": [1, 2, 3, 5]}, {"nums": [1]}, {"nums": [2, 2]},
                  {"nums": [1, 2, 5]}, {"nums": [3, 3, 3, 4, 5]}, {"nums": [100] * 30 + [99, 1]}],
        "expect": {0: True, 1: False},
        "hints": [
            "If the total is odd, the answer is `False`. Otherwise you need a subset that adds up to `total / 2`.",
            "Track every sum that can be made from the numbers seen so far.",
            "Start with the set `{0}`. For each number `x`, add `s + x` for every reachable sum `s`. Return whether `total // 2` becomes reachable. (A boolean array works the same way.)",
        ],
        "ref": """
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        sums = {0}
        for x in nums:
            sums |= {s + x for s in sums}
        return total // 2 in sums
""",
    },
]
