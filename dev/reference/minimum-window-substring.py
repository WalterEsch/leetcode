class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        l = 0
        best = (float("inf"), 0, 0)
        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if r - l + 1 < best[0]:
                    best = (r - l + 1, l, r + 1)
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return s[best[1]:best[2]] if best[0] != float("inf") else ""
