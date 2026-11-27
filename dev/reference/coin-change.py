class Solution:
    def coinChange(self, coins, amount):
        dist = {0: 0}
        q = collections.deque([0])
        while q:
            a = q.popleft()
            if a == amount:
                return dist[a]
            for c in coins:
                b = a + c
                if b <= amount and b not in dist:
                    dist[b] = dist[a] + 1
                    q.append(b)
        return -1
