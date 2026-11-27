class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        def exists(w):
            def dfs(r, c, i):
                if i == len(w):
                    return True
                if not (0 <= r < m and 0 <= c < n) or board[r][c] != w[i]:
                    return False
                ch, board[r][c] = board[r][c], "#"
                ok = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                board[r][c] = ch
                return ok
            return any(dfs(r, c, 0) for r in range(m) for c in range(n))
        return [w for w in words if exists(w)]
