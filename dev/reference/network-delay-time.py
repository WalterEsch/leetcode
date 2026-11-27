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
