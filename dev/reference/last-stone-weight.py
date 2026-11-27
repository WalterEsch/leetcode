class Solution:
    def lastStoneWeight(self, stones):
        s = sorted(stones)
        while len(s) > 1:
            y, x = s.pop(), s.pop()
            if y != x:
                s.append(y - x)
                s.sort()
        return s[0] if s else 0
