from .stack import DESIGN_NOTE

PROBLEMS = [
    {
        "id": "binary-search", "title": "Binary Search", "difficulty": "Easy",
        "desc": """
You are given a list of distinct integers `nums` sorted in increasing order, and an integer `target`. Return the index of `target` in `nums`, or `-1` if it is not there.

Your solution must run in O(log n) time.

**Constraints**

- `1 <= len(nums) <= 10^4`
""",
        "sig": "def search(self, nums: List[int], target: int) -> int:",
        "tests": [
            {"nums": [-1, 0, 3, 5, 9, 12], "target": 9}, {"nums": [-1, 0, 3, 5, 9, 12], "target": 2},
            {"nums": [5], "target": 5}, {"nums": [5], "target": -5}, {"nums": [1, 2, 3, 4, 5, 6, 7, 8], "target": 1},
            {"nums": [1, 2, 3, 4, 5, 6, 7, 8], "target": 8}, {"nums": [2, 5], "target": 5}, {"nums": [-9, -4, 0], "target": 1},
        ],
        "expect": {0: 4, 1: -1},
        "hints": [
            "Compare the target with the middle element. Which half can you rule out?",
            "Keep two bounds `l` and `r`. If `nums[mid] < target`, the answer must be right of `mid`.",
            "Loop while `l <= r` with `mid = (l + r) // 2`, moving `l = mid + 1` or `r = mid - 1`. Return `-1` when the loop ends.",
        ],
        "ref": """
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        return i if i < len(nums) and nums[i] == target else -1
""",
    },
    {
        "id": "search-a-2d-matrix", "title": "Search a 2D Matrix", "difficulty": "Medium",
        "desc": """
You are given an `m x n` integer `matrix` where each row is sorted in increasing order, and the first number of each row is larger than the last number of the row before it. Return `True` if `target` is in the matrix.

Your solution must run in O(log(m * n)) time.

**Constraints**

- `1 <= m, n <= 100`
""",
        "sig": "def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:",
        "tests": [
            {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 3},
            {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 13},
            {"matrix": [[1]], "target": 1}, {"matrix": [[1]], "target": 2},
            {"matrix": [[1, 3]], "target": 3}, {"matrix": [[1], [3]], "target": 3},
            {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 60},
            {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 0},
        ],
        "expect": {0: True, 1: False},
        "hints": [
            "Because of how the rows are ordered, reading the matrix row by row gives one fully sorted list.",
            "You could binary search for the right row first, then binary search inside that row.",
            "Or treat it as one list of length `m * n`: index `i` maps to `matrix[i // n][i % n]`, then run a normal binary search.",
        ],
        "ref": """
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [x for row in matrix for x in row]
        i = bisect.bisect_left(flat, target)
        return i < len(flat) and flat[i] == target
""",
    },
    {
        "id": "koko-eating-bananas", "title": "Koko Eating Bananas", "difficulty": "Medium",
        "desc": """
There are `n` piles of bananas, where `piles[i]` is the size of pile `i`. Koko has `h` hours. Each hour she picks one pile and eats `k` bananas from it. If the pile has fewer than `k`, she eats the whole pile and waits out the rest of that hour.

Return the smallest whole number `k` that lets her finish every pile within `h` hours.

**Constraints**

- `1 <= len(piles) <= h <= 10^9`
- `1 <= piles[i] <= 10^9`
""",
        "sig": "def minEatingSpeed(self, piles: List[int], h: int) -> int:",
        "tests": [
            {"piles": [3, 6, 7, 11], "h": 8}, {"piles": [30, 11, 23, 4, 20], "h": 5},
            {"piles": [30, 11, 23, 4, 20], "h": 6}, {"piles": [1], "h": 1}, {"piles": [1000000000], "h": 2},
            {"piles": [312884470], "h": 312884469}, {"piles": [2, 2], "h": 4}, {"piles": [5, 5, 5], "h": 1000},
        ],
        "expect": {0: 4, 1: 30, 2: 23},
        "hints": [
            "If speed `k` works, does every faster speed also work? That means you can binary search on `k`.",
            "The answer lies between `1` and `max(piles)`. For a candidate `k`, total hours is the sum of `ceil(pile / k)`.",
            "Binary search for the smallest `k` whose total hours is `<= h`. Compute `ceil(p / k)` with integers as `(p + k - 1) // k`.",
        ],
        "ref": """
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if sum((p + k - 1) // k for p in piles) <= h:
                hi = k
            else:
                lo = k + 1
        return lo
""",
    },
    {
        "id": "find-minimum-in-rotated-sorted-array", "title": "Find Minimum in Rotated Sorted Array",
        "difficulty": "Medium",
        "desc": """
A list of distinct integers was sorted in increasing order and then rotated some number of times. For example `[0, 1, 2, 4, 5, 6, 7]` rotated 4 times is `[4, 5, 6, 7, 0, 1, 2]`. Given the rotated list `nums`, return its smallest element.

Your solution must run in O(log n) time.

**Constraints**

- `1 <= len(nums) <= 5000`
""",
        "sig": "def findMin(self, nums: List[int]) -> int:",
        "tests": [
            {"nums": [3, 4, 5, 1, 2]}, {"nums": [4, 5, 6, 7, 0, 1, 2]}, {"nums": [11, 13, 15, 17]},
            {"nums": [1]}, {"nums": [2, 1]}, {"nums": [5, 1, 2, 3, 4]}, {"nums": [2, 3, 4, 5, 1]},
        ],
        "expect": {0: 1, 1: 0, 2: 11},
        "hints": [
            "Compare the middle element with the last element. What does that tell you about where the minimum is?",
            "If `nums[mid] > nums[r]`, the rotation point (and the minimum) is to the right of `mid`. Otherwise it is at `mid` or to its left.",
            "Loop while `l < r`: set `l = mid + 1` when `nums[mid] > nums[r]`, else `r = mid`. Return `nums[l]`.",
        ],
        "ref": """
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
""",
    },
    {
        "id": "search-in-rotated-sorted-array", "title": "Search in Rotated Sorted Array", "difficulty": "Medium",
        "desc": """
A list of distinct integers was sorted in increasing order and then rotated at some unknown point (for example `[4, 5, 6, 7, 0, 1, 2]`). Given the rotated list `nums` and a `target`, return the index of `target`, or `-1` if it is not there.

Your solution must run in O(log n) time.

**Constraints**

- `1 <= len(nums) <= 5000`
""",
        "sig": "def search(self, nums: List[int], target: int) -> int:",
        "tests": [
            {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}, {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3},
            {"nums": [1], "target": 0}, {"nums": [1], "target": 1}, {"nums": [3, 1], "target": 1},
            {"nums": [5, 1, 3], "target": 5}, {"nums": [6, 7, 1, 2, 3, 4, 5], "target": 6},
            {"nums": [1, 2, 3, 4, 5], "target": 4},
        ],
        "expect": {0: 4, 1: -1},
        "hints": [
            "After picking `mid`, at least one of the halves `[l, mid]` or `[mid, r]` is sorted normally.",
            "Find out which half is sorted by comparing `nums[l]` with `nums[mid]`. Then check whether `target` lies within that sorted half's range.",
            "If the target is in the sorted half's range, search there; otherwise search the other half. Continue until you find it or the range is empty.",
        ],
        "ref": """
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
""",
    },
    {
        "id": "time-based-key-value-store", "title": "Time Based Key-Value Store", "difficulty": "Medium",
        "kind": "design", "class": "TimeMap",
        "desc": f"""
Design a key-value store that keeps every value a key has had, along with when it was set.

- `TimeMap()` creates the store.
- `set(key, value, timestamp)` stores `value` for `key` at time `timestamp`.
- `get(key, timestamp)` returns the value that was set for `key` at the largest time `<= timestamp`. If there is none, return `""`.

Timestamps passed to `set` are strictly increasing.

{DESIGN_NOTE}
""",
        "starter": """
class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass
""",
        "tests": [
            {"operations": ["TimeMap", "set", "get", "get", "set", "get", "get"],
             "arguments": [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]},
            {"operations": ["TimeMap", "get"], "arguments": [[], ["x", 10]]},
            {"operations": ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
             "arguments": [[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 15],
                           ["love", 20], ["love", 25]]},
            {"operations": ["TimeMap", "set", "set", "get", "get", "get"],
             "arguments": [[], ["a", "1", 1], ["b", "2", 2], ["a", 2], ["b", 1], ["c", 3]]},
        ],
        "hints": [
            "Store, for each key, a list of `(timestamp, value)` pairs. Because timestamps only increase, the list stays sorted.",
            "`get` needs the last pair with timestamp `<= t`. You can find that with binary search.",
            "Binary search the key's list (by hand, or with `bisect.bisect_right` on the timestamps) and return the value just before the insertion point, or `\"\"` if there is none.",
        ],
        "ref": """
class TimeMap:
    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        best = ""
        for t, v in self.d.get(key, []):
            if t <= timestamp:
                best = v
        return best
""",
    },
    {
        "id": "median-of-two-sorted-arrays", "title": "Median of Two Sorted Arrays", "difficulty": "Hard",
        "desc": """
You are given two sorted lists `nums1` and `nums2`. Return the median of all the numbers in both lists combined, as a float.

Aim for O(log(m + n)) time.

**Constraints**

- `0 <= len(nums1), len(nums2) <= 1000`
- `1 <= len(nums1) + len(nums2)`
""",
        "sig": "def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:",
        "tests": [
            {"nums1": [1, 3], "nums2": [2]}, {"nums1": [1, 2], "nums2": [3, 4]}, {"nums1": [], "nums2": [1]},
            {"nums1": [2], "nums2": []}, {"nums1": [0, 0], "nums2": [0, 0]}, {"nums1": [1, 2, 3, 4, 5], "nums2": [6, 7]},
            {"nums1": [-5, 3, 6, 12, 15], "nums2": [-12, -10, -6, -3, 4, 10]}, {"nums1": [1, 3, 8], "nums2": [7, 9, 10, 11]},
        ],
        "expect": {0: 2.0, 1: 2.5},
        "hints": [
            "Merging both lists is O(m + n). For O(log), think about partitioning both lists so that the left halves together hold half of the numbers.",
            "Binary search on how many elements to take from the shorter list. The rest of the left half comes from the other list.",
            "A partition is right when the largest value on the left side of each list is `<=` the smallest value on the right side of the other list. Then the median comes from those four boundary values.",
        ],
        "ref": """
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        n = len(a)
        return float(a[n // 2]) if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
""",
    },
]
