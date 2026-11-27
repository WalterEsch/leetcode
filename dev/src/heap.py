from .stack import DESIGN_NOTE

PROBLEMS = [
    {
        "id": "kth-largest-element-in-a-stream", "title": "Kth Largest Element in a Stream", "difficulty": "Easy",
        "kind": "design", "class": "KthLargest",
        "desc": f"""
Design a class that keeps track of the `k`th largest number in a stream of numbers.

- `KthLargest(k, nums)` starts with integer `k` and an initial list of numbers `nums`.
- `add(val)` adds `val` to the stream and returns the `k`th largest number seen so far (counting duplicates).

There are always at least `k` numbers when `add` returns.

{DESIGN_NOTE}
""",
        "starter": """
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass
""",
        "tests": [
            {"operations": ["KthLargest", "add", "add", "add", "add", "add"],
             "arguments": [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]},
            {"operations": ["KthLargest", "add", "add", "add", "add"],
             "arguments": [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]},
            {"operations": ["KthLargest", "add", "add", "add"], "arguments": [[1, []], [-3], [-2], [-4]]},
            {"operations": ["KthLargest", "add", "add", "add", "add"], "arguments": [[2, [0]], [-1], [1], [-2], [3]]},
        ],
        "hints": [
            "You only ever care about the `k` largest numbers. Everything smaller can be thrown away.",
            "Keep the `k` largest numbers in a structure that gives you the smallest of them quickly.",
            "Use a min-heap of size `k` (`heapq`). On `add`, push the value, pop if the heap has more than `k` items, and return `heap[0]`.",
        ],
        "ref": """
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums, reverse=True)[self.k - 1]
""",
    },
    {
        "id": "last-stone-weight", "title": "Last Stone Weight", "difficulty": "Easy",
        "desc": """
You have a list of stone weights, `stones`. Each turn, take the two heaviest stones, `x <= y`, and smash them together. If `x == y`, both are destroyed. Otherwise `x` is destroyed and `y` becomes `y - x`.

Repeat until at most one stone is left. Return its weight, or `0` if none are left.

**Constraints**

- `1 <= len(stones) <= 30`
- `1 <= stones[i] <= 1000`
""",
        "sig": "def lastStoneWeight(self, stones: List[int]) -> int:",
        "tests": [{"stones": [2, 7, 4, 1, 8, 1]}, {"stones": [1]}, {"stones": [2, 2]}, {"stones": [3, 7, 2]},
                  {"stones": [10, 4, 2, 10]}, {"stones": [1, 1, 1]}],
        "expect": {0: 1, 1: 1, 2: 0},
        "hints": [
            "Each turn you need the two largest values, and then you may add a new value back.",
            "A max-heap does exactly that. Python's `heapq` is a min-heap, so store negative weights.",
            "Push `-w` for every stone. While the heap has 2 or more items, pop two, and if they differ push back the negative of their difference. Return `-heap[0]` if anything is left, else `0`.",
        ],
        "ref": """
class Solution:
    def lastStoneWeight(self, stones):
        s = sorted(stones)
        while len(s) > 1:
            y, x = s.pop(), s.pop()
            if y != x:
                s.append(y - x)
                s.sort()
        return s[0] if s else 0
""",
    },
    {
        "id": "k-closest-points-to-origin", "title": "K Closest Points to Origin", "difficulty": "Medium",
        "desc": """
You are given a list of `points` on a plane, where `points[i] = [x, y]`, and an integer `k`. Return the `k` points closest to the origin `(0, 0)`, using ordinary straight-line distance. The answer can be in any order.

The tests guarantee the answer is unique.

**Constraints**

- `1 <= k <= len(points) <= 10^4`
""",
        "sig": "def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:",
        "compare": "unordered",
        "tests": [
            {"points": [[1, 3], [-2, 2]], "k": 1}, {"points": [[3, 3], [5, -1], [-2, 4]], "k": 2},
            {"points": [[0, 1], [1, 0]], "k": 2}, {"points": [[1, 1]], "k": 1},
            {"points": [[2, 2], [-1, 0], [0, -3], [5, 5], [1, 1]], "k": 3},
        ],
        "expect": {0: [[-2, 2]], 1: [[3, 3], [-2, 4]]},
        "hints": [
            "You don't need the square root. Comparing `x*x + y*y` gives the same order.",
            "Sorting all points by distance is O(n log n). A heap of size `k` makes it O(n log k).",
            "Keep a max-heap of the `k` closest points so far (push `(-dist, x, y)`), popping the farthest whenever it grows past `k`. Or simply use `heapq.nsmallest(k, points, key=...)`.",
        ],
        "ref": """
class Solution:
    def kClosest(self, points, k):
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
""",
    },
    {
        "id": "kth-largest-element-in-an-array", "title": "Kth Largest Element in an Array", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums` and an integer `k`. Return the `k`th largest element in sorted order (counting duplicates, so it is not the `k`th distinct value).

Can you do it without fully sorting the list?

**Constraints**

- `1 <= k <= len(nums) <= 10^5`
""",
        "sig": "def findKthLargest(self, nums: List[int], k: int) -> int:",
        "tests": [{"nums": [3, 2, 1, 5, 6, 4], "k": 2}, {"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4},
                  {"nums": [1], "k": 1}, {"nums": [2, 1], "k": 2}, {"nums": [-1, -1], "k": 1},
                  {"nums": [7, 6, 5, 4, 3, 2, 1], "k": 5}],
        "expect": {0: 5, 1: 4},
        "hints": [
            "Sorting gives O(n log n). Can you avoid ordering everything?",
            "A min-heap holding the `k` largest elements seen so far has the answer at its top.",
            "Push each number into a min-heap and pop whenever its size exceeds `k`; the answer is `heap[0]`. For O(n) on average, look up Quickselect.",
        ],
        "ref": """
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]
""",
    },
    {
        "id": "task-scheduler", "title": "Task Scheduler", "difficulty": "Medium",
        "desc": """
You are given a list of CPU `tasks`, each an uppercase letter, and a cooldown `n`. Each time unit, the CPU either runs one task or stays idle. Two runs of the **same** task must be separated by at least `n` time units.

Tasks can run in any order. Return the minimum number of time units needed to finish all tasks.

**Constraints**

- `1 <= len(tasks) <= 10^4`
- `0 <= n <= 100`
""",
        "sig": "def leastInterval(self, tasks: List[str], n: int) -> int:",
        "tests": [
            {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2}, {"tasks": ["A", "C", "A", "B", "D", "B"], "n": 1},
            {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 3}, {"tasks": ["A"], "n": 5},
            {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 0},
            {"tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], "n": 2},
            {"tasks": ["A", "B", "C", "D", "A", "B", "C", "D"], "n": 2},
        ],
        "expect": {0: 8, 1: 6, 2: 10},
        "hints": [
            "The most frequent task sets the pace: its runs must be at least `n` apart.",
            "Simulate greedily: at each step run the available task with the most remaining copies, using a max-heap, and a queue for tasks waiting out their cooldown.",
            "There is also a formula. With `f` the highest count and `c` the number of tasks with that count, the answer is `max(len(tasks), (f - 1) * (n + 1) + c)`.",
        ],
        "ref": """
class Solution:
    def leastInterval(self, tasks, n):
        cnt = collections.Counter(tasks)
        f = max(cnt.values())
        c = sum(1 for v in cnt.values() if v == f)
        return max(len(tasks), (f - 1) * (n + 1) + c)
""",
    },
    {
        "id": "design-twitter", "title": "Design Twitter", "difficulty": "Medium", "kind": "design", "class": "Twitter",
        "desc": f"""
Design a simplified Twitter.

- `Twitter()` creates the service.
- `postTweet(userId, tweetId)` posts a new tweet with a unique `tweetId` by `userId`.
- `getNewsFeed(userId)` returns the IDs of the 10 most recent tweets posted by the user or by anyone they follow, from most recent to least recent.
- `follow(followerId, followeeId)` makes `followerId` follow `followeeId`.
- `unfollow(followerId, followeeId)` stops that.

Following someone you already follow, unfollowing someone you don't follow, and following yourself should not cause errors.

{DESIGN_NOTE}
""",
        "starter": """
class Twitter:
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
""",
        "tests": [
            {"operations": ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
             "arguments": [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]},
            {"operations": ["Twitter", "getNewsFeed", "follow", "follow", "unfollow", "getNewsFeed"],
             "arguments": [[], [7], [1, 1], [1, 2], [1, 3], [1]]},
            {"operations": ["Twitter"] + ["postTweet"] * 12 + ["getNewsFeed"],
             "arguments": [[]] + [[1, i] for i in range(100, 112)] + [[1]]},
            {"operations": ["Twitter", "postTweet", "postTweet", "postTweet", "follow", "follow", "getNewsFeed",
                            "unfollow", "getNewsFeed", "getNewsFeed"],
             "arguments": [[], [1, 11], [2, 22], [3, 33], [1, 2], [1, 3], [1], [1, 3], [1], [3]]},
        ],
        "hints": [
            "Keep a global counter so you know the order in which tweets were posted, and store each user's tweets in a list.",
            "A user's feed draws from their own tweets plus the tweets of everyone they follow. You only need the 10 most recent overall.",
            "For `getNewsFeed`, put the newest tweet of each relevant user into a max-heap keyed by time. Pop the newest, then push that user's next-newest tweet, until you have 10 or the heap is empty.",
        ],
        "ref": """
class Twitter:
    def __init__(self):
        self.t = 0
        self.tweets = []
        self.follows = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.t += 1
        self.tweets.append((self.t, userId, tweetId))

    def getNewsFeed(self, userId):
        who = self.follows[userId] | {userId}
        return [tid for _, u, tid in sorted(self.tweets, reverse=True) if u in who][:10]

    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.follows[followerId].discard(followeeId)
""",
    },
    {
        "id": "find-median-from-data-stream", "title": "Find Median from Data Stream", "difficulty": "Hard",
        "kind": "design", "class": "MedianFinder",
        "desc": f"""
Design a structure that receives numbers one at a time and can report the median of all numbers so far. The median of an even count of numbers is the average of the two middle values.

- `MedianFinder()` creates an empty structure.
- `addNum(num)` adds `num`.
- `findMedian()` returns the current median as a float. It is only called when at least one number has been added.

Answers within `10^-5` of the expected value are accepted.

{DESIGN_NOTE}
""",
        "starter": """
class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass
""",
        "tests": [
            {"operations": ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
             "arguments": [[], [1], [2], [], [3], []]},
            {"operations": ["MedianFinder", "addNum", "findMedian"], "arguments": [[], [-7], []]},
            {"operations": ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
             "arguments": [[], [5], [15], [1], [3], [], [8], []]},
            {"operations": ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
                            "addNum", "findMedian"],
             "arguments": [[], [6], [], [10], [], [2], [], [6], []]},
        ],
        "hints": [
            "Keeping a sorted list makes `addNum` O(n). Can you keep just enough order to find the middle?",
            "Split the numbers into a lower half and an upper half. You only ever need the largest of the lower half and the smallest of the upper half.",
            "Use a max-heap for the lower half (store negatives) and a min-heap for the upper half, and keep their sizes within 1 of each other. The median is the top of the bigger heap, or the average of both tops.",
        ],
        "ref": """
class MedianFinder:
    def __init__(self):
        self.a = []

    def addNum(self, num):
        bisect.insort(self.a, num)

    def findMedian(self):
        a, n = self.a, len(self.a)
        return float(a[n // 2]) if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
""",
    },
]
