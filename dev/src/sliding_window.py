PROBLEMS = [
    {
        "id": "best-time-to-buy-and-sell-stock", "title": "Best Time to Buy and Sell Stock", "difficulty": "Easy",
        "desc": """
You are given a list `prices` where `prices[i]` is a stock's price on day `i`. You may buy once and sell once, on a later day. Return the largest profit you can make, or `0` if no profit is possible.

**Constraints**

- `1 <= len(prices) <= 10^5`
- `0 <= prices[i] <= 10^4`
""",
        "sig": "def maxProfit(self, prices: List[int]) -> int:",
        "tests": [
            {"prices": [7, 1, 5, 3, 6, 4]}, {"prices": [7, 6, 4, 3, 1]}, {"prices": [1]},
            {"prices": [2, 4, 1]}, {"prices": [3, 2, 6, 5, 0, 3]}, {"prices": [1, 2]}, {"prices": [2, 1, 2, 1, 0, 1, 2]},
        ],
        "expect": {0: 5, 1: 0},
        "hints": [
            "For each day you might sell on, what is the best day to have bought?",
            "The best buy day is simply the lowest price seen so far.",
            "Track the minimum price so far in one pass, and at each day update the best profit with `price - min_price`.",
        ],
        "ref": """
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, best = float("inf"), 0
        for p in prices:
            lo = min(lo, p)
            best = max(best, p - lo)
        return best
""",
    },
    {
        "id": "longest-substring-without-repeating-characters",
        "title": "Longest Substring Without Repeating Characters", "difficulty": "Medium",
        "desc": """
You are given a string `s`. Return the length of the longest substring (a contiguous run of characters) in which no character appears more than once.

**Constraints**

- `0 <= len(s) <= 5 * 10^4`
- `s` may contain letters, digits, symbols and spaces.
""",
        "sig": "def lengthOfLongestSubstring(self, s: str) -> int:",
        "tests": [
            {"s": "abcabcbb"}, {"s": "bbbbb"}, {"s": "pwwkew"}, {"s": ""}, {"s": " "},
            {"s": "dvdf"}, {"s": "abba"}, {"s": "tmmzuxt"}, {"s": "abcdefghijklmnopqrstuvwxyz0123456789"},
        ],
        "expect": {0: 3, 1: 1, 2: 3, 3: 0},
        "hints": [
            "Think of a window `s[l:r+1]` that never contains a repeat. Grow it to the right one character at a time.",
            "When the new character is already in the window, shrink the window from the left until it is not.",
            "Keep a dictionary of each character's last index. When you see a repeat at `r`, jump `l` to `max(l, last[ch] + 1)`.",
        ],
        "ref": """
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, l, best = {}, 0, 0
        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                l = last[ch] + 1
            last[ch] = r
            best = max(best, r - l + 1)
        return best
""",
    },
    {
        "id": "longest-repeating-character-replacement",
        "title": "Longest Repeating Character Replacement", "difficulty": "Medium",
        "desc": """
You are given a string `s` of uppercase English letters and an integer `k`. You may change up to `k` characters of `s` into any other uppercase letter.

Return the length of the longest substring that can be made of a single repeated letter after those changes.

**Constraints**

- `1 <= len(s) <= 10^5`
- `0 <= k <= len(s)`
""",
        "sig": "def characterReplacement(self, s: str, k: int) -> int:",
        "tests": [
            {"s": "ABAB", "k": 2}, {"s": "AABABBA", "k": 1}, {"s": "A", "k": 0}, {"s": "ABCDE", "k": 1},
            {"s": "AAAA", "k": 0}, {"s": "ABBB", "k": 2}, {"s": "BAAAB", "k": 2}, {"s": "ABCABCABC", "k": 2},
        ],
        "expect": {0: 4, 1: 4},
        "hints": [
            "A window can be made all one letter if `window length - (count of its most common letter) <= k`.",
            "Slide a window over `s`, keeping letter counts. Shrink from the left whenever the window needs more than `k` changes.",
            "You only need the largest most-common count seen so far (`maxf`). The window never needs to shrink below the best length found, so a slightly stale `maxf` still gives the right answer.",
        ],
        "ref": """
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, l, best = {}, 0, 0
        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
""",
    },
    {
        "id": "permutation-in-string", "title": "Permutation in String", "difficulty": "Medium",
        "desc": """
You are given two strings `s1` and `s2`. Return `True` if some rearrangement of `s1` appears as a contiguous substring of `s2`, and `False` otherwise.

**Constraints**

- `1 <= len(s1), len(s2) <= 10^4`
- Both contain only lowercase English letters.
""",
        "sig": "def checkInclusion(self, s1: str, s2: str) -> bool:",
        "tests": [
            {"s1": "ab", "s2": "eidbaooo"}, {"s1": "ab", "s2": "eidboaoo"}, {"s1": "abc", "s2": "ab"},
            {"s1": "a", "s2": "a"}, {"s1": "adc", "s2": "dcda"}, {"s1": "hello", "s2": "ooolleoooleh"},
            {"s1": "aab", "s2": "abab"}, {"s1": "xyz", "s2": "zzyx"},
        ],
        "expect": {0: True, 1: False},
        "hints": [
            "A rearrangement of `s1` is a substring of `s2` with exactly the same letter counts as `s1`.",
            "Look at every window of length `len(s1)` in `s2` and compare letter counts.",
            "Slide the window one step at a time: add the new letter's count and remove the old one, instead of recounting. Compare two 26-length count arrays (or track how many letters match).",
        ],
        "ref": """
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        target = collections.Counter(s1)
        for i in range(len(s2) - n + 1):
            if collections.Counter(s2[i:i + n]) == target:
                return True
        return False
""",
    },
    {
        "id": "minimum-window-substring", "title": "Minimum Window Substring", "difficulty": "Hard",
        "desc": """
You are given two strings `s` and `t`. Return the shortest substring of `s` that contains every character of `t`, including repeats (if `t` has two `"a"`s, the window needs at least two). If there is no such substring, return `""`.

The tests guarantee the shortest window is unique.

**Constraints**

- `1 <= len(s), len(t) <= 10^5`
- `s` and `t` contain uppercase and lowercase English letters.
""",
        "sig": "def minWindow(self, s: str, t: str) -> str:",
        "tests": [
            {"s": "ADOBECODEBANC", "t": "ABC"}, {"s": "a", "t": "a"}, {"s": "a", "t": "aa"},
            {"s": "ab", "t": "b"}, {"s": "aaflslflsldkalskaaa", "t": "aaa"}, {"s": "cabwefgewcwaefgcf", "t": "cae"},
            {"s": "abc", "t": "d"}, {"s": "bba", "t": "ab"},
        ],
        "expect": {0: "BANC", 1: "a", 2: ""},
        "hints": [
            "Use a window over `s`. Grow it on the right until it contains everything in `t`.",
            "Once the window is valid, shrink it from the left as much as possible while it stays valid, recording the smallest valid window.",
            "Keep counts of what `t` needs and a number `have` of characters whose required count is satisfied. The window is valid when `have` equals the number of distinct characters in `t`.",
        ],
        "ref": """
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        l = 0
        best = (float("inf"), 0, 0)
        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if r - l + 1 < best[0]:
                    best = (r - l + 1, l, r + 1)
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return s[best[1]:best[2]] if best[0] != float("inf") else ""
""",
    },
    {
        "id": "sliding-window-maximum", "title": "Sliding Window Maximum", "difficulty": "Hard",
        "desc": """
You are given a list of integers `nums` and a window size `k`. A window of size `k` slides from the left end of the list to the right end, one position at a time. Return a list with the maximum value in each window position.

**Constraints**

- `1 <= len(nums) <= 10^5`
- `1 <= k <= len(nums)`
""",
        "sig": "def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:",
        "tests": [
            {"nums": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3}, {"nums": [1], "k": 1}, {"nums": [1, -1], "k": 1},
            {"nums": [9, 11], "k": 2}, {"nums": [4, -2], "k": 2}, {"nums": [7, 2, 4], "k": 2},
            {"nums": [1, 3, 1, 2, 0, 5], "k": 3}, {"nums": [5, 4, 3, 2, 1], "k": 2},
        ],
        "expect": {0: [3, 3, 5, 5, 6, 7], 1: [1]},
        "hints": [
            "Taking `max()` of every window is O(n * k). Which elements in a window can never be the maximum of any later window?",
            "If a newer element is bigger than an older one, the older one can never be a maximum again. Throw it away.",
            "Keep a deque of indices whose values are decreasing. Pop from the back while the new value is bigger, pop from the front when the index leaves the window, and the front is always the current maximum.",
        ],
        "ref": """
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq, res = collections.deque(), []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
""",
    },
]
