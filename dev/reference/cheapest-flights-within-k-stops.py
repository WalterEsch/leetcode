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
