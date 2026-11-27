class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def go(i, rem, path):
            if rem == 0:
                res.append(path)
                return
            if rem < 0 or i == len(candidates):
                return
            go(i, rem - candidates[i], path + [candidates[i]])
            go(i + 1, rem, path)
        go(0, target, [])
        return res
