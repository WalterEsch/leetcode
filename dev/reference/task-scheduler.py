class Solution:
    def leastInterval(self, tasks, n):
        cnt = collections.Counter(tasks)
        f = max(cnt.values())
        c = sum(1 for v in cnt.values() if v == f)
        return max(len(tasks), (f - 1) * (n + 1) + c)
