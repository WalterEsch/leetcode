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
