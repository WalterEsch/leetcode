class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, l, best = {}, 0, 0
        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                l = last[ch] + 1
            last[ch] = r
            best = max(best, r - l + 1)
        return best
