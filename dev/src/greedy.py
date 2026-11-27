PROBLEMS = [
    {
        "id": "maximum-subarray", "title": "Maximum Subarray", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums`. Return the largest sum of any non-empty contiguous subarray.

**Constraints**

- `1 <= len(nums) <= 10^5`
""",
        "sig": "def maxSubArray(self, nums: List[int]) -> int:",
        "tests": [{"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, {"nums": [1]}, {"nums": [5, 4, -1, 7, 8]},
                  {"nums": [-3, -1, -2]}, {"nums": [-1, 2, -1, 2, -1]}, {"nums": [8, -19, 5, -4, 20]}],
        "examples": 3,
        "expect": {0: 6, 1: 1, 2: 23, 3: -1},
        "hints": [
            "Checking every subarray is O(n^2). As you scan left to right, when is a running sum no longer worth keeping?",
            "If the running sum becomes negative, it can only hurt whatever comes next. Start fresh instead.",
            "Kadane's algorithm: `cur = max(x, cur + x)` for each `x`, and keep the best `cur`. Start `best` at `nums[0]` so all-negative lists work.",
        ],
        "ref": """
class Solution:
    def maxSubArray(self, nums):
        best = nums[0]
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                best = max(best, s)
        return best
""",
    },
    {
        "id": "jump-game", "title": "Jump Game", "difficulty": "Medium",
        "desc": """
You start at index `0` of a list `nums`. From index `i` you can jump forward by **up to** `nums[i]` positions. Return `True` if you can reach the last index.

**Constraints**

- `1 <= len(nums) <= 10^4`
- `0 <= nums[i] <= 10^5`
""",
        "sig": "def canJump(self, nums: List[int]) -> bool:",
        "tests": [{"nums": [2, 3, 1, 1, 4]}, {"nums": [3, 2, 1, 0, 4]}, {"nums": [0]}, {"nums": [0, 1]},
                  {"nums": [2, 0, 0]}, {"nums": [1, 1, 0, 1]}, {"nums": [5, 0, 0, 0, 0, 0]}],
        "examples": 3,
        "expect": {0: True, 1: False, 2: True},
        "hints": [
            "Instead of trying every jump, keep track of how far you could possibly reach.",
            "Scan left to right with `reach` = the furthest index reachable so far. If you ever reach an index `i > reach`, you're stuck.",
            "For each `i` up to `reach`, update `reach = max(reach, i + nums[i])`. Return `True` once `reach >= len(nums) - 1`. (Working backward from the goal also works.)",
        ],
        "ref": """
class Solution:
    def canJump(self, nums):
        ok = [False] * len(nums)
        ok[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            ok[i] = any(ok[j] for j in range(i + 1, min(len(nums), i + nums[i] + 1)))
        return ok[0]
""",
    },
    {
        "id": "jump-game-ii", "title": "Jump Game II", "difficulty": "Medium",
        "desc": """
You start at index `0` of a list `nums`. From index `i` you can jump forward by up to `nums[i]` positions. Return the **minimum number of jumps** needed to reach the last index. The tests guarantee that it is reachable.

**Constraints**

- `1 <= len(nums) <= 10^4`
""",
        "sig": "def jump(self, nums: List[int]) -> int:",
        "tests": [{"nums": [2, 3, 1, 1, 4]}, {"nums": [2, 3, 0, 1, 4]}, {"nums": [0]}, {"nums": [1, 2]},
                  {"nums": [1, 1, 1, 1]}, {"nums": [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]}],
        "expect": {0: 2, 1: 2},
        "hints": [
            "Think of it as a breadth-first search: all indices reachable with `k` jumps form one level.",
            "Each level is a contiguous range of indices. The next level reaches up to the furthest `i + nums[i]` from the current range.",
            "Keep `end` (the end of the current level) and `far` (the furthest reach). Scan `i` from 0 to `n - 2`, updating `far`; when `i == end`, add a jump and set `end = far`.",
        ],
        "ref": """
class Solution:
    def jump(self, nums):
        n = len(nums)
        best = [0] + [float("inf")] * (n - 1)
        for i in range(n):
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                best[j] = min(best[j], best[i] + 1)
        return best[-1]
""",
    },
    {
        "id": "gas-station", "title": "Gas Station", "difficulty": "Medium",
        "desc": """
There are `n` gas stations in a circle. Station `i` has `gas[i]` units of gas, and driving from station `i` to station `i + 1` costs `cost[i]` units. You start with an empty tank at one station.

Return the index of the station where you can start and drive all the way around once, or `-1` if there is none. The tests guarantee the answer is unique when it exists.

**Constraints**

- `1 <= n <= 10^5`
""",
        "sig": "def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:",
        "tests": [{"gas": [1, 2, 3, 4, 5], "cost": [3, 4, 5, 1, 2]}, {"gas": [2, 3, 4], "cost": [3, 4, 3]},
                  {"gas": [5], "cost": [4]}, {"gas": [1], "cost": [2]}, {"gas": [3, 1, 1], "cost": [1, 2, 2]},
                  {"gas": [5, 1, 2, 3, 4], "cost": [4, 4, 1, 5, 1]}],
        "expect": {0: 3, 1: -1},
        "hints": [
            "If the total gas is less than the total cost, no start can work. Otherwise, a start always exists.",
            "If you start at `s` and run out of gas before reaching station `j`, then no station between `s` and `j` can be the start either.",
            "Scan once with a running tank. Whenever it goes negative, reset it to 0 and make the next station the candidate start. Return the candidate if `sum(gas) >= sum(cost)`, else `-1`.",
        ],
        "ref": """
class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        for s in range(n):
            tank = 0
            for k in range(n):
                i = (s + k) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    break
            else:
                return s
        return -1
""",
    },
    {
        "id": "hand-of-straights", "title": "Hand of Straights", "difficulty": "Medium",
        "desc": """
You are given a list `hand` of card values and an integer `groupSize`. Return `True` if the cards can be rearranged into groups of exactly `groupSize` cards, where each group is a run of consecutive values (like `3, 4, 5`).

**Constraints**

- `1 <= len(hand) <= 10^4`
- `1 <= groupSize <= len(hand)`
""",
        "sig": "def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:",
        "tests": [{"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "groupSize": 3}, {"hand": [1, 2, 3, 4, 5], "groupSize": 4},
                  {"hand": [5], "groupSize": 1}, {"hand": [1, 1, 2, 2, 3, 3], "groupSize": 3}, {"hand": [1, 2, 4, 5], "groupSize": 2},
                  {"hand": [1, 1, 2, 3], "groupSize": 2}, {"hand": [8, 10, 12], "groupSize": 3}],
        "expect": {0: True, 1: False},
        "hints": [
            "If `len(hand)` isn't divisible by `groupSize`, the answer is `False`.",
            "The smallest remaining card has to start a group. There's no other group it could belong to.",
            "Count the cards. Repeatedly take the smallest value with a non-zero count and try to remove one each of `x, x + 1, ..., x + groupSize - 1`; if any is missing, return `False`.",
        ],
        "ref": """
class Solution:
    def isNStraightHand(self, hand, groupSize):
        cards = sorted(hand)
        while cards:
            start = cards[0]
            for v in range(start, start + groupSize):
                if v not in cards:
                    return False
                cards.remove(v)
        return True
""",
    },
    {
        "id": "merge-triplets-to-form-target-triplet", "title": "Merge Triplets to Form Target Triplet",
        "difficulty": "Medium",
        "desc": """
You are given a list of `triplets` (each a list of 3 integers) and a `target` triplet. You may repeatedly pick two triplets `a` and `b` and replace `b` with `[max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])]`.

Return `True` if you can make some triplet equal to `target`.

**Constraints**

- `1 <= len(triplets) <= 10^5`
""",
        "sig": "def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:",
        "tests": [{"triplets": [[2, 5, 3], [1, 8, 4], [1, 7, 5]], "target": [2, 7, 5]},
                  {"triplets": [[3, 4, 5], [4, 5, 6]], "target": [3, 2, 5]},
                  {"triplets": [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], "target": [5, 5, 5]},
                  {"triplets": [[1, 1, 1]], "target": [1, 1, 1]}, {"triplets": [[1, 2, 3], [3, 2, 1]], "target": [3, 2, 3]},
                  {"triplets": [[1, 3, 1], [1, 1, 3]], "target": [2, 3, 3]}],
        "examples": 3,
        "expect": {0: True, 1: False, 2: True},
        "hints": [
            "Merging only ever increases values. Which triplets can you never use?",
            "Any triplet with a value bigger than the target in the same position would ruin that position. Ignore those.",
            "Among the safe triplets, check whether each of the three target values appears in its position in at least one of them.",
        ],
        "ref": """
class Solution:
    def mergeTriplets(self, triplets, target):
        best = [0, 0, 0]
        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                best = [max(best[i], t[i]) for i in range(3)]
        return best == target
""",
    },
    {
        "id": "partition-labels", "title": "Partition Labels", "difficulty": "Medium",
        "desc": """
You are given a string `s`. Split it into as many pieces as possible so that each letter appears in at most one piece. Return the sizes of the pieces, in order.

**Constraints**

- `1 <= len(s) <= 500`, lowercase letters only.
""",
        "sig": "def partitionLabels(self, s: str) -> List[int]:",
        "tests": [{"s": "ababcbacadefegdehijhklij"}, {"s": "eccbbbbdec"}, {"s": "a"}, {"s": "abc"}, {"s": "abca"},
                  {"s": "caedbdedda"}],
        "expect": {0: [9, 7, 8], 1: [10]},
        "hints": [
            "A piece containing some letter must stretch at least to that letter's last occurrence.",
            "First record the last index of every letter.",
            "Scan with a running `end = max(end, last[ch])`. When the index reaches `end`, the current piece is complete: record its size and start a new one.",
        ],
        "ref": """
class Solution:
    def partitionLabels(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            end = s.rindex(s[i])
            while j <= end:
                end = max(end, s.rindex(s[j]))
                j += 1
            res.append(j - i)
            i = j
        return res
""",
    },
    {
        "id": "valid-parenthesis-string", "title": "Valid Parenthesis String", "difficulty": "Medium",
        "desc": """
You are given a string `s` made of `(`, `)` and `*`. Each `*` can act as `(`, as `)`, or as nothing. Return `True` if some choice for the `*`s makes the string a balanced set of parentheses.

**Constraints**

- `1 <= len(s) <= 100`
""",
        "sig": "def checkValidString(self, s: str) -> bool:",
        "tests": [{"s": "()"}, {"s": "(*)"}, {"s": "(*))"}, {"s": "(("}, {"s": "*"}, {"s": ")*"}, {"s": "(*()"},
                  {"s": "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"}],
        "examples": 3,
        "expect": {0: True, 1: True, 2: True, 3: False},
        "hints": [
            "Without `*`, you would track the number of open parentheses. With `*`, that number could be one of several values.",
            "Track a range: `lo` is the fewest open parentheses possible so far, and `hi` is the most.",
            "For `(`: both go up. For `)`: both go down. For `*`: `lo` goes down and `hi` goes up. If `hi < 0`, return `False`; keep `lo` at least 0. At the end, return `lo == 0`.",
        ],
        "ref": """
class Solution:
    def checkValidString(self, s):
        possible = {0}
        for ch in s:
            nxt = set()
            for k in possible:
                if ch in "(*":
                    nxt.add(k + 1)
                if ch in ")*" and k > 0:
                    nxt.add(k - 1)
                if ch == "*":
                    nxt.add(k)
            possible = nxt
        return 0 in possible
""",
    },
]
