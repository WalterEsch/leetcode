class Solution:
    def partitionLabels(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            end = s.rindex(s[i])
            while j <= end:
                end = max(end, s.rindex(s[j]))
                j += 1
            res.append(j - i)
            i = j
        return res
