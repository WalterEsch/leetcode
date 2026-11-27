PROBLEMS = [
    {
        "id": "network-delay-time", "title": "Network Delay Time", "difficulty": "Medium",
        "desc": """
A network has `n` nodes labeled `1` to `n`. Each entry `times[i] = [u, v, w]` is a directed edge: a signal sent from `u` reaches `v` after `w` time units.

A signal is sent from node `k`. Return how long it takes until every node has received it, or `-1` if some node never does.

**Constraints**

- `1 <= k <= n <= 100`
- `1 <= len(times) <= 6000`, `0 <= w <= 100`
""",
        "sig": "def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:",
        "tests": [
            {"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}, {"times": [[1, 2, 1]], "n": 2, "k": 1},
            {"times": [[1, 2, 1]], "n": 2, "k": 2}, {"times": [[1, 2, 1], [2, 3, 2], [1, 3, 4]], "n": 3, "k": 1},
            {"times": [[2, 1, 5]], "n": 2, "k": 2}, {"times": [[1, 2, 0], [2, 3, 0]], "n": 3, "k": 1},
        ],
        "examples": 3,
        "expect": {0: 2, 1: 1, 2: -1, 3: 3},
        "hints": [
            "The time for a node is its shortest-path distance from `k`. The answer is the largest of those distances.",
            "Edge weights are non-negative, so Dijkstra's algorithm works.",
            "Use a min-heap of `(time, node)` starting with `(0, k)`. Pop the closest node; if it's new, record its time and push its neighbors with `time + w`. If fewer than `n` nodes are reached, return `-1`.",
        ],
        "ref": """
class Solution:
    def networkDelayTime(self, times, n, k):
        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        for _ in range(n):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        best = max(dist.values())
        return best if best < float("inf") else -1
""",
    },
    {
        "id": "reconstruct-itinerary", "title": "Reconstruct Itinerary", "difficulty": "Hard",
        "desc": """
You are given a list of airline `tickets`, where `tickets[i] = [from, to]`. All of them belong to someone who started at `"JFK"`. Rebuild their itinerary: a list of airports, starting with `"JFK"`, that uses **every ticket exactly once**.

If several itineraries work, return the one that comes first in lexical (dictionary) order when compared as a list of strings. At least one valid itinerary exists.

**Constraints**

- `1 <= len(tickets) <= 300`
""",
        "sig": "def findItinerary(self, tickets: List[List[str]]) -> List[str]:",
        "tests": [
            {"tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]},
            {"tickets": [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]},
            {"tickets": [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]},
            {"tickets": [["JFK", "AAA"]]},
            {"tickets": [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "BOS"], ["BOS", "JFK"]]},
        ],
        "expect": {0: ["JFK", "MUC", "LHR", "SFO", "SJC"], 1: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
                   2: ["JFK", "NRT", "JFK", "KUL"]},
        "hints": [
            "Always taking the alphabetically smallest destination can lead to a dead end with tickets unused (see example 3).",
            "You need a path that uses every edge exactly once: an Eulerian path. Hierholzer's algorithm builds one.",
            "Sort each airport's destinations. DFS: while the airport has unused tickets, take the smallest and recurse. After an airport has no tickets left, append it to the result. Reverse the result at the end.",
        ],
        "ref": """
class Solution:
    def findItinerary(self, tickets):
        g = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            g[a].append(b)
        route = []
        def visit(a):
            while g[a]:
                visit(g[a].pop())
            route.append(a)
        visit("JFK")
        return route[::-1]
""",
    },
    {
        "id": "min-cost-to-connect-all-points", "title": "Min Cost to Connect All Points", "difficulty": "Medium",
        "desc": """
You are given a list of `points`, where `points[i] = [x, y]`. Connecting two points costs their Manhattan distance, `|x1 - x2| + |y1 - y2|`.

Return the minimum total cost to connect all the points, so that there is exactly one path between any two points.

**Constraints**

- `1 <= len(points) <= 1000`, all points distinct.
""",
        "sig": "def minCostConnectPoints(self, points: List[List[int]]) -> int:",
        "tests": [{"points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]}, {"points": [[3, 12], [-2, 5], [-4, 1]]},
                  {"points": [[0, 0]]}, {"points": [[0, 0], [1, 1], [1, 0], [-1, 1]]}, {"points": [[-1000000, -1000000], [1000000, 1000000]]}],
        "expect": {0: 20, 1: 18, 2: 0},
        "hints": [
            "You want a minimum spanning tree of a complete graph whose edge weights are Manhattan distances.",
            "Prim's algorithm grows the tree one point at a time, always adding the cheapest edge from the tree to a point outside it.",
            "Since the graph is dense, a simple O(n^2) Prim works well: keep `dist[i]`, the cheapest edge from the tree to point `i`. Repeatedly pick the unvisited point with the smallest `dist`, add its cost, and update the others.",
        ],
        "ref": """
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        dist = [float("inf")] * n
        dist[0] = 0
        used = [False] * n
        total = 0
        for _ in range(n):
            i = min((d, j) for j, d in enumerate(dist) if not used[j])[1]
            used[i] = True
            total += dist[i]
            for j in range(n):
                if not used[j]:
                    d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    dist[j] = min(dist[j], d)
        return total
""",
    },
    {
        "id": "swim-in-rising-water", "title": "Swim in Rising Water", "difficulty": "Hard",
        "desc": """
You are given an `n x n` grid where `grid[r][c]` is the elevation of that cell. All values are distinct and range from `0` to `n*n - 1`.

Rain starts falling, and at time `t` the water everywhere is at depth `t`. You can swim from a cell to a neighboring cell (up, down, left, right) only if **both** cells have elevation at most `t`. Swimming takes no time.

Starting at the top-left cell, return the earliest time at which you can reach the bottom-right cell.

**Constraints**

- `1 <= n <= 50`
""",
        "sig": "def swimInWater(self, grid: List[List[int]]) -> int:",
        "tests": [{"grid": [[0, 2], [1, 3]]},
                  {"grid": [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]},
                  {"grid": [[0]]}, {"grid": [[3, 2], [0, 1]]}, {"grid": [[0, 8, 7], [1, 6, 5], [2, 3, 4]]}],
        "examples": 3,
        "expect": {0: 3, 1: 16, 2: 0},
        "hints": [
            "The time a path needs is the highest elevation along it. You want the path whose highest point is as low as possible.",
            "A Dijkstra-style search works, where the cost of a path is its maximum elevation instead of a sum.",
            "Use a min-heap of `(max_height_so_far, r, c)` starting from `(grid[0][0], 0, 0)`. Pop the lowest, and push neighbors with `max(current, grid[nr][nc])`. The first time you pop the bottom-right cell, return its value. (Binary search on `t` with a flood fill also works.)",
        ],
        "ref": """
class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        def ok(t):
            if grid[0][0] > t:
                return False
            seen, stack = {(0, 0)}, [(0, 0)]
            while stack:
                r, c = stack.pop()
                if (r, c) == (n - 1, n - 1):
                    return True
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and grid[x][y] <= t:
                        seen.add((x, y))
                        stack.append((x, y))
            return False
        t = 0
        while not ok(t):
            t += 1
        return t
""",
    },
    {
        "id": "alien-dictionary", "title": "Alien Dictionary", "difficulty": "Hard",
        "desc": """
An alien language uses the lowercase English letters, but in an unknown order. You are given a list of `words` from its dictionary, sorted in the alien order.

Return a string with every letter that appears in `words`, each exactly once, in an order consistent with the dictionary. If several orders are possible, any of them is accepted. If no order is possible (the input contradicts itself), return `""`.

Note that a word must come after any of its own prefixes: `["abc", "ab"]` is invalid.

**Constraints**

- `1 <= len(words) <= 100`, `1 <= len(words[i]) <= 100`
""",
        "sig": "def alienOrder(self, words: List[str]) -> str:",
        "compare": "custom",
        "checker": """
def check(inp, actual, expected):
    if expected == "":
        return actual == ""
    if not isinstance(actual, str):
        return False
    letters = set("".join(inp["words"]))
    if len(actual) != len(letters) or set(actual) != letters:
        return False
    pos = {ch: i for i, ch in enumerate(actual)}
    words = inp["words"]
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if pos[x] > pos[y]:
                    return False
                break
    return True
""",
        "tests": [{"words": ["wrt", "wrf", "er", "ett", "rftt"]}, {"words": ["z", "x"]}, {"words": ["z", "x", "z"]},
                  {"words": ["abc", "ab"]}, {"words": ["z", "z"]}, {"words": ["ab", "adc"]},
                  {"words": ["baa", "abcd", "abca", "cab", "cad"]}, {"words": ["a", "b", "ca", "cc"]}],
        "examples": 3,
        "expect": {0: "wertf", 1: "zx", 2: ""},
        "hints": [
            "Comparing two neighboring words tells you about at most one pair of letters: the first position where they differ.",
            "Collect those \"letter `a` comes before letter `b`\" rules as directed edges, then find an order that respects all of them.",
            "Build the graph (and return `\"\"` right away if a word is followed by its own proper prefix). Then topologically sort all letters with Kahn's algorithm. If not every letter makes it into the order, there's a cycle, so return `\"\"`.",
        ],
        "ref": """
class Solution:
    def alienOrder(self, words):
        letters = sorted(set("".join(words)))
        g = {c: set() for c in letters}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    g[x].add(y)
                    break
            else:
                if len(a) > len(b):
                    return ""
        indeg = {c: 0 for c in letters}
        for x in g:
            for y in g[x]:
                indeg[y] += 1
        q = [c for c in letters if indeg[c] == 0]
        out = []
        while q:
            x = q.pop(0)
            out.append(x)
            for y in sorted(g[x]):
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        return "".join(out) if len(out) == len(letters) else ""
""",
    },
    {
        "id": "cheapest-flights-within-k-stops", "title": "Cheapest Flights Within K Stops", "difficulty": "Medium",
        "desc": """
There are `n` cities labeled `0` to `n - 1`. Each `flights[i] = [from, to, price]` is a one-way flight. Return the cheapest price to get from `src` to `dst` with **at most `k` stops** in between, or `-1` if there is no such route.

**Constraints**

- `1 <= n <= 100`, `0 <= k < n`, `src != dst`
""",
        "sig": "def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:",
        "tests": [
            {"n": 4, "flights": [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], "src": 0, "dst": 3, "k": 1},
            {"n": 3, "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]], "src": 0, "dst": 2, "k": 1},
            {"n": 3, "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]], "src": 0, "dst": 2, "k": 0},
            {"n": 3, "flights": [[0, 1, 2], [1, 2, 1]], "src": 2, "dst": 0, "k": 2},
            {"n": 5, "flights": [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], "src": 0, "dst": 2, "k": 2},
            {"n": 4, "flights": [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], "src": 0, "dst": 3, "k": 1},
        ],
        "examples": 3,
        "expect": {0: 700, 1: 200, 2: 500, 3: -1},
        "hints": [
            "Plain Dijkstra ignores the limit on stops. A cheaper path might use too many stops.",
            "At most `k` stops means at most `k + 1` flights. Bellman-Ford relaxes paths one edge at a time, so `k + 1` rounds is exactly right.",
            "Run `k + 1` rounds of Bellman-Ford. In each round, update from a **copy** of the previous round's prices, so one round can't chain several flights together.",
        ],
        "ref": """
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        best = None
        q = [(0, src, 0)]
        while q:
            cost, city, used = q.pop()
            if city == dst:
                best = cost if best is None else min(best, cost)
                continue
            if used == k + 1:
                continue
            for a, b, p in flights:
                if a == city:
                    q.append((cost + p, b, used + 1))
        return -1 if best is None else best
""",
    },
]
