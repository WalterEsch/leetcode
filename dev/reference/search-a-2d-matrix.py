class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [x for row in matrix for x in row]
        i = bisect.bisect_left(flat, target)
        return i < len(flat) and flat[i] == target
