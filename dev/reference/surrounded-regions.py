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
