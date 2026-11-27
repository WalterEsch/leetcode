class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        def dfs(r, c, i, seen):
            if i == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or (r, c) in seen or board[r][c] != word[i]:
                return False
            seen.add((r, c))
            ok = any(dfs(r + a, c + b, i + 1, seen) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            seen.discard((r, c))
            return ok
        return any(dfs(r, c, 0, set()) for r in range(m) for c in range(n))
