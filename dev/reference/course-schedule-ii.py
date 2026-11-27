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
