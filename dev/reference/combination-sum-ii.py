class Solution:
    def combinationSum2(self, candidates, target):
        found = set()
        c = sorted(candidates)
        def go(i, rem, path):
            if rem == 0:
                found.add(tuple(path))
                return
            if rem < 0 or i == len(c):
                return
            go(i + 1, rem - c[i], path + [c[i]])
            go(i + 1, rem, path)
        go(0, target, [])
        return [list(t) for t in found]
