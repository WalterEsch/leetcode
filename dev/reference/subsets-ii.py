class Solution:
    def subsetsWithDup(self, nums):
        res = {()}
        for x in sorted(nums):
            res |= {s + (x,) for s in res}
        return [list(s) for s in res]
