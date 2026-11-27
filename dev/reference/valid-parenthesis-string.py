class Solution:
    def checkValidString(self, s):
        possible = {0}
        for ch in s:
            nxt = set()
            for k in possible:
                if ch in "(*":
                    nxt.add(k + 1)
                if ch in ")*" and k > 0:
                    nxt.add(k - 1)
                if ch == "*":
                    nxt.add(k)
            possible = nxt
        return 0 in possible
