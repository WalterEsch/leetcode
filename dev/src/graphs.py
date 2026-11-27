INF = 2147483647

GRID_ISLANDS = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

PROBLEMS = [
    {
        "id": "number-of-islands", "title": "Number of Islands", "difficulty": "Medium",
        "desc": """
You are given an `m x n` grid where `"1"` is land and `"0"` is water. An island is a group of land cells connected horizontally or vertically. Everything outside the grid is water. Return the number of islands.

**Constraints**

- `1 <= m, n <= 300`
""",
        "sig": "def numIslands(self, grid: List[List[str]]) -> int:",
        "tests": [
            {"grid": [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]},
            {"grid": GRID_ISLANDS}, {"grid": [["0"]]}, {"grid": [["1"]]},
            {"grid": [["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]},
            {"grid": [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]},
        ],
        "expect": {0: 1, 1: 3},
        "hints": [
            "When you find a land cell you haven't seen, you have found a new island. How do you avoid counting its other cells again?",
            "Explore the whole island from that cell (DFS or BFS) and mark every cell you visit.",
            "Loop over all cells. When a cell is `\"1\"`, add one to the count and flood-fill from it, changing connected land to `\"0\"` (or adding it to a visited set).",
        ],
        "ref": """
class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        seen = set()
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    stack = [(r, c)]
                    seen.add((r, c))
                    while stack:
                        a, b = stack.pop()
                        for x, y in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1" and (x, y) not in seen:
                                seen.add((x, y))
                                stack.append((x, y))
        return count
""",
    },
    {
        "id": "max-area-of-island", "title": "Max Area of Island", "difficulty": "Medium",
        "desc": """
You are given an `m x n` grid of `0`s (water) and `1`s (land). An island is a group of `1`s connected horizontally or vertically, and its area is the number of cells in it. Return the largest island area, or `0` if there is no land.

**Constraints**

- `1 <= m, n <= 50`
""",
        "sig": "def maxAreaOfIsland(self, grid: List[List[int]]) -> int:",
        "tests": [
            {"grid": [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]},
            {"grid": [[0, 0, 0, 0, 0, 0, 0, 0]]}, {"grid": [[1]]}, {"grid": [[1, 1], [1, 0]]},
            {"grid": [[1, 0, 1], [0, 1, 0], [1, 0, 1]]},
        ],
        "expect": {0: 6, 1: 0},
        "hints": [
            "This is Number of Islands, but you also need the size of each island.",
            "Make the flood fill return the number of cells it visited.",
            "`dfs(r, c)` returns 0 for water, out-of-bounds or visited cells; otherwise it marks the cell and returns `1 +` the sum of `dfs` on its four neighbors. Keep the maximum.",
        ],
        "ref": """
class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0 or (r, c) in seen:
                return 0
            seen.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        return max(dfs(r, c) for r in range(m) for c in range(n))
""",
    },
    {
        "id": "clone-graph", "title": "Clone Graph", "difficulty": "Medium",
        "desc": """
You are given a reference to a node in a connected, undirected graph. Return a **deep copy** of the graph: new nodes with the same values and the same connections. No node in the copy may be a node of the original graph.

The `Node` class is already defined:

```
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

Tests show the graph as an adjacency list: `adjList[i]` lists the neighbors of the node with value `i + 1`. You receive the node with value `1` (or `None` for an empty graph).

**Constraints**

- The graph has 0 to 100 nodes with values `1` to `n`, no repeated edges and no self-loops.
""",
        "prelude": """
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
""",
        "starter_prefix": """# Definition for a Node (already provided):
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

""",
        "sig": "def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:",
        "harness": """
def call(problem, ns, inp):
    Node = ns["Node"]
    adj = inp["adjList"]
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    original = {id(n) for n in nodes}
    start = ns["Solution"]().cloneGraph(nodes[0] if nodes else None)
    if start is None:
        return []
    seen = {}
    stack = [start]
    while stack:
        n = stack.pop()
        if id(n) in original:
            raise ValueError("Your copy contains a node from the original graph. Every node must be new.")
        if n.val in seen:
            if seen[n.val] is not n:
                raise ValueError(f"Your copy has two different nodes with value {n.val}")
            continue
        seen[n.val] = n
        stack.extend(n.neighbors)
    return [[m.val for m in seen[v].neighbors] for v in sorted(seen)]
""",
        "tests": [{"adjList": [[2, 4], [1, 3], [2, 4], [1, 3]]}, {"adjList": [[]]}, {"adjList": []},
                  {"adjList": [[2], [1]]}, {"adjList": [[2, 3], [1, 3], [1, 2]]},
                  {"adjList": [[2, 3, 4, 5], [1], [1], [1], [1]]}],
        "examples": 3,
        "hints": [
            "You need a copy of every node, and each copy's neighbors must be copies too. Watch out for cycles.",
            "Keep a dictionary from original node to its copy. It tells you whether a node has already been copied and lets you reuse that copy.",
            "DFS: if the node is in the dictionary, return its copy. Otherwise create the copy, store it in the dictionary **before** recursing, then set its neighbors to the clones of the original's neighbors.",
        ],
        "ref": """
class Solution:
    def cloneGraph(self, node):
        copies = {}
        def go(n):
            if n in copies:
                return copies[n]
            c = Node(n.val)
            copies[n] = c
            c.neighbors = [go(x) for x in n.neighbors]
            return c
        return go(node) if node else None
""",
    },
    {
        "id": "walls-and-gates", "title": "Walls and Gates", "difficulty": "Medium",
        "desc": f"""
You are given an `m x n` grid `rooms` with three kinds of cells:

- `-1` is a wall,
- `0` is a gate, and
- `{INF}` (`2^31 - 1`) is an empty room.

Fill every empty room, **in place**, with the number of steps to its nearest gate, moving up, down, left or right through non-wall cells. Leave a room at `{INF}` if no gate can be reached. Your function returns nothing. The tests check `rooms` afterwards.

**Constraints**

- `1 <= m, n <= 250`
""",
        "sig": "def wallsAndGates(self, rooms: List[List[int]]) -> None:",
        "output_from_arg": "rooms",
        "tests": [
            {"rooms": [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]},
            {"rooms": [[-1]]}, {"rooms": [[INF]]}, {"rooms": [[0, INF, INF, INF]]},
            {"rooms": [[0, -1, INF], [-1, INF, INF], [INF, INF, 0]]},
        ],
        "expect": {0: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]},
        "hints": [
            "Running a separate search from every room is slow. What if you searched outward from the gates instead?",
            "A breadth-first search from **all gates at once** reaches each room first along a shortest path.",
            "Put every gate in a queue. Pop a cell and, for each neighbor that is still `2147483647`, set it to the cell's distance plus 1 and add it to the queue.",
        ],
        "ref": """
class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms[0])
        q = collections.deque((r, c) for r in range(m) for c in range(n) if rooms[r][c] == 0)
        while q:
            r, c = q.popleft()
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                    rooms[x][y] = rooms[r][c] + 1
                    q.append((x, y))
""",
    },
    {
        "id": "rotting-oranges", "title": "Rotting Oranges", "difficulty": "Medium",
        "desc": """
You are given an `m x n` grid where `0` is an empty cell, `1` is a fresh orange and `2` is a rotten orange. Every minute, each fresh orange next to a rotten one (up, down, left or right) becomes rotten.

Return the number of minutes until no fresh orange is left, or `-1` if that never happens.

**Constraints**

- `1 <= m, n <= 10`
""",
        "sig": "def orangesRotting(self, grid: List[List[int]]) -> int:",
        "tests": [{"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}, {"grid": [[2, 1, 1], [0, 1, 1], [1, 0, 1]]}, {"grid": [[0, 2]]},
                  {"grid": [[0]]}, {"grid": [[1]]}, {"grid": [[2, 2], [1, 1], [0, 0], [2, 0]]}, {"grid": [[2, 1, 1, 1, 1, 1]]}],
        "examples": 3,
        "expect": {0: 4, 1: -1, 2: 0},
        "hints": [
            "Rot spreads outward from all rotten oranges at the same time, one step per minute.",
            "That is a breadth-first search that starts from every rotten orange at once. Each BFS level is one minute.",
            "Count the fresh oranges and queue all rotten ones. Process the queue level by level, rotting fresh neighbors and decreasing the count. At the end, return the minutes if the count is 0, else `-1`.",
        ],
        "ref": """
class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        rotten = {(r, c) for r in range(m) for c in range(n) if grid[r][c] == 2}
        fresh = {(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1}
        t = 0
        while fresh:
            new = {(x, y) for (x, y) in fresh if any(p in rotten for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))}
            if not new:
                return -1
            fresh -= new
            rotten |= new
            t += 1
        return t
""",
    },
    {
        "id": "pacific-atlantic-water-flow", "title": "Pacific Atlantic Water Flow", "difficulty": "Medium",
        "desc": """
You are given an `m x n` grid `heights` of an island. The Pacific Ocean touches the top and left edges, and the Atlantic Ocean touches the bottom and right edges.

Rain water flows from a cell to a neighboring cell (up, down, left, right) if the neighbor's height is **less than or equal** to the current cell's. Water flows from edge cells into the adjacent ocean.

Return the coordinates `[r, c]` of every cell from which water can reach **both** oceans, in any order.

**Constraints**

- `1 <= m, n <= 200`
""",
        "sig": "def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:",
        "compare": "unordered",
        "tests": [
            {"heights": [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]},
            {"heights": [[1]]}, {"heights": [[1, 1], [1, 1]]}, {"heights": [[3, 2, 1], [2, 1, 0], [1, 0, 0]]},
            {"heights": [[10, 10, 10], [10, 1, 10], [10, 10, 10]]},
        ],
        "expect": {0: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], 1: [[0, 0]]},
        "hints": [
            "Searching from every cell is expensive. Think in reverse: which cells can the ocean be reached from, starting at the ocean?",
            "From each ocean's edge cells, move uphill (to neighbors with height `>=` the current cell). Every cell you reach can drain into that ocean.",
            "Run one DFS or BFS from all Pacific edge cells and one from all Atlantic edge cells, collecting two visited sets. The answer is their intersection.",
        ],
        "ref": """
class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        def reach(starts):
            seen = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen and heights[x][y] >= heights[r][c]:
                        seen.add((x, y))
                        stack.append((x, y))
            return seen
        pac = reach([(0, c) for c in range(n)] + [(r, 0) for r in range(m)])
        atl = reach([(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)])
        return [[r, c] for r, c in sorted(pac & atl)]
""",
    },
    {
        "id": "surrounded-regions", "title": "Surrounded Regions", "difficulty": "Medium",
        "desc": """
You are given an `m x n` board of `"X"` and `"O"` characters. A region is a group of `"O"` cells connected horizontally or vertically. A region is **surrounded** if none of its cells is on the edge of the board.

Capture every surrounded region by changing its `"O"`s to `"X"`, **in place**. Your function returns nothing. The tests check `board` afterwards.

**Constraints**

- `1 <= m, n <= 200`
""",
        "sig": "def solve(self, board: List[List[str]]) -> None:",
        "output_from_arg": "board",
        "tests": [
            {"board": [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]},
            {"board": [["X"]]}, {"board": [["O", "O"], ["O", "O"]]},
            {"board": [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]]},
            {"board": [["X", "X", "X", "X", "X"], ["X", "O", "X", "O", "X"], ["X", "X", "O", "X", "X"], ["X", "O", "X", "O", "O"]]},
        ],
        "expect": {0: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]},
        "hints": [
            "Rather than finding the surrounded regions, find the ones that are **not** surrounded.",
            "A region escapes if it touches the edge. Every `\"O\"` connected to an edge `\"O\"` is safe.",
            "From every edge `\"O\"`, flood-fill and mark the safe cells (for example with `\"T\"`). Then flip every remaining `\"O\"` to `\"X\"` and turn every `\"T\"` back into `\"O\"`.",
        ],
        "ref": """
class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        safe = set()
        stack = [(r, c) for r in range(m) for c in range(n)
                 if (r in (0, m - 1) or c in (0, n - 1)) and board[r][c] == "O"]
        while stack:
            r, c = stack.pop()
            if (r, c) in safe:
                continue
            safe.add((r, c))
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    stack.append((x, y))
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
""",
    },
    {
        "id": "course-schedule", "title": "Course Schedule", "difficulty": "Medium",
        "desc": """
There are `numCourses` courses, labeled `0` to `numCourses - 1`. Each entry `[a, b]` in `prerequisites` means you must take course `b` before course `a`. Return `True` if it is possible to finish every course.

**Constraints**

- `1 <= numCourses <= 2000`
- `0 <= len(prerequisites) <= 5000`, and all pairs are distinct.
""",
        "sig": "def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:",
        "tests": [{"numCourses": 2, "prerequisites": [[1, 0]]}, {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]]},
                  {"numCourses": 1, "prerequisites": []}, {"numCourses": 3, "prerequisites": [[1, 0], [2, 1], [0, 2]]},
                  {"numCourses": 5, "prerequisites": [[1, 4], [2, 4], [3, 1], [3, 2]]},
                  {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [3, 2], [1, 3]]}],
        "expect": {0: True, 1: False},
        "hints": [
            "Think of courses as nodes and prerequisites as directed edges. When is it impossible to finish?",
            "It's impossible exactly when the graph has a cycle.",
            "Detect a cycle with DFS, tracking nodes on the current path (seeing one again means a cycle). Or use Kahn's algorithm: repeatedly take courses with no remaining prerequisites, and check that all courses get taken.",
        ],
        "ref": """
class Solution:
    def canFinish(self, numCourses, prerequisites):
        indeg = [0] * numCourses
        g = collections.defaultdict(list)
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        q = [i for i in range(numCourses) if indeg[i] == 0]
        done = 0
        while q:
            x = q.pop()
            done += 1
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        return done == numCourses
""",
    },
    {
        "id": "course-schedule-ii", "title": "Course Schedule II", "difficulty": "Medium",
        "desc": """
There are `numCourses` courses, labeled `0` to `numCourses - 1`. Each entry `[a, b]` in `prerequisites` means you must take course `b` before course `a`.

Return an order in which you can take every course. If several orders work, any of them is accepted. If it is impossible, return an empty list.

**Constraints**

- `1 <= numCourses <= 2000`
""",
        "sig": "def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:",
        "compare": "custom",
        "checker": """
def check(inp, actual, expected):
    if not expected:
        return actual == []
    n = inp["numCourses"]
    if sorted(actual) != list(range(n)):
        return False
    pos = {c: i for i, c in enumerate(actual)}
    return all(pos[b] < pos[a] for a, b in inp["prerequisites"])
""",
        "tests": [{"numCourses": 2, "prerequisites": [[1, 0]]},
                  {"numCourses": 4, "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]]},
                  {"numCourses": 1, "prerequisites": []}, {"numCourses": 2, "prerequisites": [[0, 1], [1, 0]]},
                  {"numCourses": 3, "prerequisites": []}, {"numCourses": 6, "prerequisites": [[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]},
                  {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [0, 2], [3, 0]]}],
        "examples": 3,
        "hints": [
            "This is Course Schedule, but you have to output the order as well (a topological sort).",
            "In Kahn's algorithm, the order in which courses become free to take is a valid order.",
            "Count each course's prerequisites (in-degree). Start a queue with the courses that have none. Pop a course, add it to the order, and decrease its dependents' counts, queueing any that hit 0. If the order has fewer than `numCourses` courses, return `[]`.",
        ],
        "ref": """
class Solution:
    def findOrder(self, numCourses, prerequisites):
        indeg = [0] * numCourses
        g = collections.defaultdict(list)
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        q = collections.deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while q:
            x = q.popleft()
            order.append(x)
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        return order if len(order) == numCourses else []
""",
    },
    {
        "id": "graph-valid-tree", "title": "Graph Valid Tree", "difficulty": "Medium",
        "desc": """
You have `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`. Return `True` if these edges form a valid tree: all nodes are connected and there are no cycles.

**Constraints**

- `1 <= n <= 2000`
- No duplicate edges and no self-loops.
""",
        "sig": "def validTree(self, n: int, edges: List[List[int]]) -> bool:",
        "tests": [{"n": 5, "edges": [[0, 1], [0, 2], [0, 3], [1, 4]]}, {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]},
                  {"n": 1, "edges": []}, {"n": 2, "edges": []}, {"n": 4, "edges": [[0, 1], [2, 3]]},
                  {"n": 3, "edges": [[0, 1], [1, 2], [2, 0]]}, {"n": 4, "edges": [[3, 2], [1, 0], [0, 3]]}],
        "examples": 3,
        "expect": {0: True, 1: False, 2: True, 3: False},
        "hints": [
            "A tree with `n` nodes has exactly `n - 1` edges. What else must be true?",
            "With exactly `n - 1` edges, the graph is a tree if and only if it is connected.",
            "Return `False` if `len(edges) != n - 1`. Otherwise check connectivity with a DFS/BFS from node 0, or with Union-Find (which also detects a cycle when an edge joins two nodes already connected).",
        ],
        "ref": """
class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        seen, stack = {0}, [0]
        while stack:
            for y in g[stack.pop()]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        return len(seen) == n
""",
    },
    {
        "id": "number-of-connected-components-in-an-undirected-graph",
        "title": "Number of Connected Components in an Undirected Graph", "difficulty": "Medium",
        "desc": """
You have `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`. Return the number of connected components.

**Constraints**

- `1 <= n <= 2000`
- No duplicate edges.
""",
        "sig": "def countComponents(self, n: int, edges: List[List[int]]) -> int:",
        "tests": [{"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]}, {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [3, 4]]},
                  {"n": 1, "edges": []}, {"n": 4, "edges": []}, {"n": 6, "edges": [[0, 1], [1, 2], [2, 0], [3, 4]]},
                  {"n": 3, "edges": [[2, 0]]}],
        "expect": {0: 2, 1: 1},
        "hints": [
            "Each time you find a node not yet visited, you have found a new component.",
            "Explore all of that component with DFS or BFS so its nodes are not counted again.",
            "Union-Find is a neat alternative: start with `n` components and subtract one every time an edge joins two different sets.",
        ],
        "ref": """
class Solution:
    def countComponents(self, n, edges):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        count = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                count -= 1
        return count
""",
    },
    {
        "id": "redundant-connection", "title": "Redundant Connection", "difficulty": "Medium",
        "desc": """
A tree with `n` nodes labeled `1` to `n` had one extra edge added, which created a cycle. You are given the resulting list of undirected `edges`.

Return an edge that can be removed so the rest is a tree with all `n` nodes. If there are several, return the one that appears **last** in `edges`.

**Constraints**

- `3 <= n == len(edges) <= 1000`
""",
        "sig": "def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:",
        "tests": [{"edges": [[1, 2], [1, 3], [2, 3]]}, {"edges": [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]},
                  {"edges": [[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]}, {"edges": [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]},
                  {"edges": [[2, 3], [1, 2], [3, 1]]}],
        "expect": {0: [2, 3], 1: [1, 4]},
        "hints": [
            "Add the edges one at a time. Which edge is the first one that creates a cycle?",
            "An edge creates a cycle if its two endpoints are already connected.",
            "Use Union-Find. For each edge, if both endpoints already have the same root, return that edge; otherwise union them. The first such edge is the last one in the input that you could remove.",
        ],
        "ref": """
class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]
            parent[ra] = rb
""",
    },
    {
        "id": "word-ladder", "title": "Word Ladder", "difficulty": "Hard",
        "desc": """
You are given two words, `beginWord` and `endWord`, and a list `wordList`. A transformation sequence goes from `beginWord` to `endWord` by changing one letter at a time, where every word after `beginWord` must be in `wordList`.

Return the number of words in the **shortest** such sequence (counting both ends), or `0` if there is none.

**Constraints**

- `1 <= len(beginWord) <= 10`, and all words have the same length.
- `1 <= len(wordList) <= 5000`, lowercase letters, all distinct.
""",
        "sig": "def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:",
        "tests": [
            {"beginWord": "hit", "endWord": "cog", "wordList": ["hot", "dot", "dog", "lot", "log", "cog"]},
            {"beginWord": "hit", "endWord": "cog", "wordList": ["hot", "dot", "dog", "lot", "log"]},
            {"beginWord": "a", "endWord": "c", "wordList": ["a", "b", "c"]},
            {"beginWord": "hot", "endWord": "dog", "wordList": ["hot", "dog"]},
            {"beginWord": "red", "endWord": "tax", "wordList": ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]},
            {"beginWord": "lost", "endWord": "cost", "wordList": ["most", "fist", "lost", "cost", "fish"]},
        ],
        "examples": 3,
        "expect": {0: 5, 1: 0, 2: 2},
        "hints": [
            "Treat each word as a node, connected to words that differ by one letter. You want the shortest path.",
            "Breadth-first search finds shortest paths in unweighted graphs.",
            "BFS from `beginWord`. To find neighbors quickly, try replacing each position with every letter `a` to `z` and check a set of remaining words (or group words by patterns like `h*t`). Remove words from the set once visited.",
        ],
        "ref": """
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        q = collections.deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for v in words:
                if v not in seen and sum(a != b for a, b in zip(v, w)) == 1:
                    seen.add(v)
                    q.append((v, d + 1))
        return 0
""",
    },
]
