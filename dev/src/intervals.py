PROBLEMS = [
    {
        "id": "insert-interval", "title": "Insert Interval", "difficulty": "Medium",
        "desc": """
You are given a list of non-overlapping `intervals`, each `[start, end]`, sorted by start. Insert `newInterval`, merging any intervals that overlap with it, and return the resulting sorted list of non-overlapping intervals.

Intervals that touch (one ends where the next starts) count as overlapping.

**Constraints**

- `0 <= len(intervals) <= 10^4`
""",
        "sig": "def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:",
        "tests": [{"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]},
                  {"intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], "newInterval": [4, 8]},
                  {"intervals": [], "newInterval": [5, 7]}, {"intervals": [[1, 5]], "newInterval": [6, 8]},
                  {"intervals": [[3, 5]], "newInterval": [1, 2]}, {"intervals": [[1, 5]], "newInterval": [0, 0]},
                  {"intervals": [[1, 2], [5, 6]], "newInterval": [2, 5]}],
        "examples": 3,
        "expect": {0: [[1, 5], [6, 9]], 1: [[1, 2], [3, 10], [12, 16]], 2: [[5, 7]]},
        "hints": [
            "The intervals fall into three groups: completely before `newInterval`, overlapping it, and completely after it.",
            "Every overlapping interval gets absorbed. The merged interval runs from the smallest start to the largest end among them.",
            "Add the intervals that end before `newInterval` starts, then merge all intervals that overlap into `newInterval` and add it, then add the rest.",
        ],
        "ref": """
class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for s, e in sorted(intervals + [newInterval]):
            if res and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res
""",
    },
    {
        "id": "merge-intervals", "title": "Merge Intervals", "difficulty": "Medium",
        "desc": """
You are given a list of `intervals`, each `[start, end]`. Merge all overlapping intervals and return the non-overlapping intervals that cover the same ranges, in any order.

Intervals that touch (`[1, 4]` and `[4, 5]`) count as overlapping.

**Constraints**

- `1 <= len(intervals) <= 10^4`
""",
        "sig": "def merge(self, intervals: List[List[int]]) -> List[List[int]]:",
        "compare": "unordered",
        "tests": [{"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}, {"intervals": [[1, 4], [4, 5]]}, {"intervals": [[4, 7], [1, 4]]},
                  {"intervals": [[1, 4], [2, 3]]}, {"intervals": [[5, 5]]}, {"intervals": [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]},
                  {"intervals": [[1, 4], [0, 0]]}],
        "examples": 3,
        "expect": {0: [[1, 6], [8, 10], [15, 18]], 1: [[1, 5]], 2: [[1, 7]]},
        "hints": [
            "Sort the intervals by start. After that, which intervals can overlap?",
            "After sorting, an interval can only overlap the merged interval just before it.",
            "Walk the sorted list. If the interval starts at or before the end of the last merged interval, extend that end with `max`. Otherwise start a new merged interval.",
        ],
        "ref": """
class Solution:
    def merge(self, intervals):
        res = []
        for s, e in sorted(intervals):
            if res and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res
""",
    },
    {
        "id": "non-overlapping-intervals", "title": "Non-overlapping Intervals", "difficulty": "Medium",
        "desc": """
You are given a list of `intervals`. Return the minimum number of intervals to remove so that the remaining intervals don't overlap.

Intervals that only touch (`[1, 2]` and `[2, 3]`) do **not** count as overlapping here.

**Constraints**

- `1 <= len(intervals) <= 10^5`
""",
        "sig": "def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:",
        "tests": [{"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]]}, {"intervals": [[1, 2], [1, 2], [1, 2]]},
                  {"intervals": [[1, 2], [2, 3]]}, {"intervals": [[1, 100], [11, 22], [1, 11], [2, 12]]},
                  {"intervals": [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]}, {"intervals": [[5, 6]]}],
        "examples": 3,
        "expect": {0: 1, 1: 2, 2: 0},
        "hints": [
            "Turn it around: keep as many non-overlapping intervals as possible, then remove the rest.",
            "To fit the most intervals, always keep the one that finishes earliest, since it leaves the most room for the rest.",
            "Sort by end. Keep a `prev_end`; if an interval starts at or after `prev_end`, keep it and update `prev_end`; otherwise count it as removed.",
        ],
        "ref": """
class Solution:
    def eraseOverlapIntervals(self, intervals):
        iv = sorted(intervals)
        @functools.lru_cache(None)
        def keep(i, prev_end):
            if i == len(iv):
                return 0
            best = keep(i + 1, prev_end)
            if iv[i][0] >= prev_end:
                best = max(best, 1 + keep(i + 1, iv[i][1]))
            return best
        return len(iv) - keep(0, -10**9)
""",
    },
    {
        "id": "meeting-rooms", "title": "Meeting Rooms", "difficulty": "Easy",
        "desc": """
You are given a list of meeting time `intervals`, each `[start, end]`. Return `True` if one person could attend all of them, meaning no two meetings overlap. A meeting ending at time `t` and another starting at `t` do not overlap.

**Constraints**

- `0 <= len(intervals) <= 500`
""",
        "sig": "def canAttendMeetings(self, intervals: List[List[int]]) -> bool:",
        "tests": [{"intervals": [[0, 30], [5, 10], [15, 20]]}, {"intervals": [[7, 10], [2, 4]]}, {"intervals": []},
                  {"intervals": [[1, 5], [5, 8]]}, {"intervals": [[1, 5], [4, 8]]}, {"intervals": [[9, 10], [4, 9], [4, 17]]}],
        "examples": 3,
        "expect": {0: False, 1: True, 2: True, 3: True},
        "hints": [
            "When do two meetings conflict?",
            "After sorting by start time, only neighbors need to be compared.",
            "Sort the meetings and return `False` if any meeting starts before the previous one ends.",
        ],
        "ref": """
class Solution:
    def canAttendMeetings(self, intervals):
        return all(not (a[0] < b[1] and b[0] < a[1]) for i, a in enumerate(intervals) for b in intervals[i + 1:])
""",
    },
    {
        "id": "meeting-rooms-ii", "title": "Meeting Rooms II", "difficulty": "Medium",
        "desc": """
You are given a list of meeting time `intervals`, each `[start, end]`. Return the minimum number of conference rooms needed so that every meeting has a room. A room freed at time `t` can be used by a meeting starting at `t`.

**Constraints**

- `1 <= len(intervals) <= 10^4`
""",
        "sig": "def minMeetingRooms(self, intervals: List[List[int]]) -> int:",
        "tests": [{"intervals": [[0, 30], [5, 10], [15, 20]]}, {"intervals": [[7, 10], [2, 4]]}, {"intervals": [[1, 5]]},
                  {"intervals": [[1, 5], [5, 10], [10, 15]]}, {"intervals": [[1, 10], [2, 9], [3, 8], [4, 7]]},
                  {"intervals": [[9, 10], [4, 9], [4, 17]]}, {"intervals": [[2, 11], [6, 16], [11, 16]]}],
        "expect": {0: 2, 1: 1},
        "hints": [
            "The answer is the largest number of meetings happening at the same moment.",
            "Sort all the start times and all the end times separately, and sweep through time.",
            "Walk through the sorted starts. For each start, if the earliest unfinished end is `<=` that start, a room frees up (advance the end pointer); otherwise you need one more room. A min-heap of end times also works.",
        ],
        "ref": """
class Solution:
    def minMeetingRooms(self, intervals):
        times = sorted(set(t for iv in intervals for t in iv))
        return max(sum(1 for s, e in intervals if s <= t < e) for t in times)
""",
    },
    {
        "id": "minimum-interval-to-include-each-query", "title": "Minimum Interval to Include Each Query",
        "difficulty": "Hard",
        "desc": """
You are given a list of `intervals`, where `[left, right]` includes every integer from `left` to `right`, so its size is `right - left + 1`. You are also given a list of integer `queries`.

For each query `q`, find the size of the smallest interval that contains `q`, or `-1` if no interval contains it. Return the answers in the same order as `queries`.

**Constraints**

- `1 <= len(intervals), len(queries) <= 10^5`
""",
        "sig": "def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:",
        "tests": [{"intervals": [[1, 4], [2, 4], [3, 6], [4, 4]], "queries": [2, 3, 4, 5]},
                  {"intervals": [[2, 3], [2, 5], [1, 8], [20, 25]], "queries": [2, 19, 5, 22]},
                  {"intervals": [[1, 1]], "queries": [1, 2]}, {"intervals": [[5, 10], [1, 20]], "queries": [7, 7, 0, 20]},
                  {"intervals": [[4, 5], [5, 8], [1, 9], [8, 10], [1, 6]], "queries": [7, 9, 3, 9, 3]}],
        "expect": {0: [3, 3, 1, 4], 1: [2, -1, 4, 6]},
        "hints": [
            "Checking every interval for every query is O(n * q). Can you answer the queries in sorted order and reuse work?",
            "Sort the queries (keeping their original positions) and the intervals by start. As queries increase, more intervals start, and some end.",
            "Sweep queries in increasing order. Push every interval with `left <= q` into a min-heap keyed by size, as `(size, right)`. Pop from the top while `right < q`. The top's size is the answer, or `-1` if the heap is empty.",
        ],
        "ref": """
class Solution:
    def minInterval(self, intervals, queries):
        return [min((r - l + 1 for l, r in intervals if l <= q <= r), default=-1) for q in queries]
""",
    },
]
