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
