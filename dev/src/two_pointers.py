PROBLEMS = [
    {
        "id": "valid-palindrome", "title": "Valid Palindrome", "difficulty": "Easy",
        "desc": """
You are given a string `s`. Ignore every character that is not a letter or digit, and treat uppercase and lowercase letters as the same. Return `True` if what is left reads the same forwards and backwards.

An empty result counts as a palindrome.

**Constraints**

- `1 <= len(s) <= 2 * 10^5`
- `s` contains printable ASCII characters.
""",
        "sig": "def isPalindrome(self, s: str) -> bool:",
        "tests": [
            {"s": "A man, a plan, a canal: Panama"}, {"s": "race a car"}, {"s": " "},
            {"s": "0P"}, {"s": "Was it a car or a cat I saw?"}, {"s": "ab_a"}, {"s": "a."}, {"s": "12321"},
        ],
        "expect": {0: True, 1: False, 2: True, 3: False},
        "hints": [
            "Building a cleaned-up copy of the string and comparing it with its reverse works, but uses extra space.",
            "Use two pointers, one at each end, and move them toward each other.",
            "Skip characters where `ch.isalnum()` is `False`. Compare `s[l].lower()` with `s[r].lower()` and return `False` on the first mismatch.",
        ],
        "ref": """
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [c.lower() for c in s if c.isalnum()]
        return t == t[::-1]
""",
    },
    {
        "id": "two-sum-ii-input-array-is-sorted", "title": "Two Sum II - Input Array Is Sorted", "difficulty": "Medium",
        "desc": """
You are given a list of integers `numbers` sorted in non-decreasing order, and an integer `target`. Find the two numbers that add up to `target` and return their positions as `[index1, index2]`, **counting from 1**, with `index1 < index2`.

There is exactly one answer, and you may not use the same element twice. Use only O(1) extra space.

**Constraints**

- `2 <= len(numbers) <= 3 * 10^4`
- `-1000 <= numbers[i], target <= 1000`
""",
        "sig": "def twoSum(self, numbers: List[int], target: int) -> List[int]:",
        "tests": [
            {"numbers": [2, 7, 11, 15], "target": 9}, {"numbers": [2, 3, 4], "target": 6},
            {"numbers": [-1, 0], "target": -1}, {"numbers": [1, 2, 3, 4, 4, 9, 56, 90], "target": 8},
            {"numbers": [5, 25, 75], "target": 100}, {"numbers": [-5, -3, 0, 2, 9], "target": 6},
            {"numbers": [1, 1], "target": 2},
        ],
        "expect": {0: [1, 2], 1: [1, 3], 2: [1, 2]},
        "hints": [
            "The list is sorted. How can you use that instead of a dictionary?",
            "Start with one pointer at each end. If their sum is too small, what should move? If it is too big?",
            "While `l < r`: if `numbers[l] + numbers[r]` is less than `target`, move `l` right; if greater, move `r` left; otherwise return `[l + 1, r + 1]`.",
        ],
        "ref": """
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
""",
    },
    {
        "id": "3sum", "title": "3Sum", "difficulty": "Medium",
        "desc": """
You are given a list of integers `nums`. Return every **distinct** triplet `[a, b, c]` of values taken from three different positions such that `a + b + c == 0`.

The answer must not contain the same triplet twice. The triplets, and the numbers inside each triplet, can be in any order.

**Constraints**

- `3 <= len(nums) <= 3000`
- `-10^5 <= nums[i] <= 10^5`
""",
        "sig": "def threeSum(self, nums: List[int]) -> List[List[int]]:",
        "compare": "unordered_nested",
        "tests": [
            {"nums": [-1, 0, 1, 2, -1, -4]}, {"nums": [0, 1, 1]}, {"nums": [0, 0, 0]},
            {"nums": [0, 0, 0, 0]}, {"nums": [-2, 0, 1, 1, 2]}, {"nums": [3, -2, 1, 0]},
            {"nums": [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]},
        ],
        "expect": {0: [[-1, -1, 2], [-1, 0, 1]], 1: [], 2: [[0, 0, 0]]},
        "hints": [
            "Sort the list first. That makes skipping duplicates and searching easier.",
            "Fix the first number `nums[i]`, then the problem becomes Two Sum II on the rest of the sorted list with target `-nums[i]`.",
            "Use two pointers for the inner search. Skip `i` when `nums[i] == nums[i - 1]`, and after finding a triplet, move `l` past repeated values to avoid duplicates.",
        ],
        "ref": """
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
""",
    },
    {
        "id": "container-with-most-water", "title": "Container With Most Water", "difficulty": "Medium",
        "desc": """
You are given a list `height` where `height[i]` is the height of a vertical line drawn at position `i`. Pick two lines. Together with the x-axis they form a container whose water level is limited by the shorter line.

Return the largest amount of water such a container can hold. That is `min(height[i], height[j]) * (j - i)` for the best pair.

**Constraints**

- `2 <= len(height) <= 10^5`
- `0 <= height[i] <= 10^4`
""",
        "sig": "def maxArea(self, height: List[int]) -> int:",
        "tests": [
            {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, {"height": [1, 1]}, {"height": [4, 3, 2, 1, 4]},
            {"height": [1, 2, 1]}, {"height": [0, 0]}, {"height": [2, 3, 10, 5, 7, 8, 9]},
            {"height": [1, 2, 4, 3]},
        ],
        "expect": {0: 49, 1: 1, 2: 16},
        "hints": [
            "Trying every pair is O(n^2). Start with the widest container: the first and last lines.",
            "When you move a pointer inward, the width shrinks. Moving the taller line can never help, because the shorter line still limits the height.",
            "Keep `l` and `r` at the ends. Record the area, then move whichever pointer has the shorter line. Repeat until they meet.",
        ],
        "ref": """
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, best = 0, len(height) - 1, 0
        while l < r:
            best = max(best, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
""",
    },
    {
        "id": "trapping-rain-water", "title": "Trapping Rain Water", "difficulty": "Hard",
        "desc": """
You are given a list `height` of non-negative integers describing an elevation map where each bar is 1 unit wide. Return how many units of rain water are trapped between the bars after it rains.

**Constraints**

- `1 <= len(height) <= 2 * 10^4`
- `0 <= height[i] <= 10^5`
""",
        "sig": "def trap(self, height: List[int]) -> int:",
        "tests": [
            {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}, {"height": [4, 2, 0, 3, 2, 5]},
            {"height": [1]}, {"height": [3, 2, 1]}, {"height": [2, 0, 2]}, {"height": [5, 4, 1, 2]},
            {"height": [0, 7, 1, 4, 6]},
        ],
        "expect": {0: 6, 1: 9, 2: 0},
        "hints": [
            "The water above bar `i` is `min(tallest bar on its left, tallest bar on its right) - height[i]`, if that is positive.",
            "You could precompute the max to the left and max to the right of every position with two passes. Can you do it with O(1) space?",
            "Use two pointers with `left_max` and `right_max`. Move the side with the smaller max inward: the water at that position is decided by its own max, because the other side is at least as tall.",
        ],
        "ref": """
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm = rm = total = 0
        while l < r:
            if height[l] < height[r]:
                lm = max(lm, height[l])
                total += lm - height[l]
                l += 1
            else:
                rm = max(rm, height[r])
                total += rm - height[r]
                r -= 1
        return total
""",
    },
]
