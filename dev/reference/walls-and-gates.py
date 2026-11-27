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
