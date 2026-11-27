class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best, st = 0, []
        for i, h in enumerate(heights + [0]):
            start = i
            while st and st[-1][1] > h:
                s, sh = st.pop()
                best = max(best, sh * (i - s))
                start = s
            st.append((start, h))
        return best
