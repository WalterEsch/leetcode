PROBLEMS = [
    {
        "id": "single-number", "title": "Single Number", "difficulty": "Easy",
        "desc": """
You are given a non-empty list of integers `nums`. Every value appears exactly twice, except one value that appears once. Return that value.

Use O(n) time and O(1) extra space.

**Constraints**

- `1 <= len(nums) <= 3 * 10^4`
""",
        "sig": "def singleNumber(self, nums: List[int]) -> int:",
        "tests": [{"nums": [2, 2, 1]}, {"nums": [4, 1, 2, 1, 2]}, {"nums": [1]}, {"nums": [-3, 7, 7]}, {"nums": [0, 5, 5, 9, 9]},
                  {"nums": [30000, -30000, 30000]}],
        "examples": 3,
        "expect": {0: 1, 1: 4, 2: 1},
        "hints": [
            "A set or dictionary works, but uses O(n) space. Is there an operation where pairs cancel out?",
            "XOR has `a ^ a == 0` and `a ^ 0 == a`, and the order of the operations doesn't matter.",
            "XOR all the numbers together. Every pair cancels to 0, leaving the single number.",
        ],
        "ref": """
class Solution:
    def singleNumber(self, nums):
        return [x for x, c in collections.Counter(nums).items() if c == 1][0]
""",
    },
    {
        "id": "number-of-1-bits", "title": "Number of 1 Bits", "difficulty": "Easy",
        "desc": """
Given a positive integer `n`, return how many `1` bits its binary representation has (its Hamming weight).

**Constraints**

- `1 <= n <= 2^31 - 1`
""",
        "sig": "def hammingWeight(self, n: int) -> int:",
        "tests": [{"n": 11}, {"n": 128}, {"n": 2147483645}, {"n": 1}, {"n": 255}, {"n": 1023 * 1024}],
        "examples": 3,
        "expect": {0: 3, 1: 1, 2: 30},
        "hints": [
            "Check the lowest bit with `n & 1`, then shift right with `n >>= 1`.",
            "Repeat until `n` becomes 0, counting the ones.",
            "A neat trick: `n & (n - 1)` clears the lowest set bit. Count how many times you can do that before `n` is 0.",
        ],
        "ref": """
class Solution:
    def hammingWeight(self, n):
        return bin(n).count("1")
""",
    },
    {
        "id": "counting-bits", "title": "Counting Bits", "difficulty": "Easy",
        "desc": """
Given an integer `n`, return a list `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`.

Can you do it in O(n) time?

**Constraints**

- `0 <= n <= 10^5`
""",
        "sig": "def countBits(self, n: int) -> List[int]:",
        "tests": [{"n": 2}, {"n": 5}, {"n": 0}, {"n": 1}, {"n": 16}, {"n": 31}],
        "expect": {0: [0, 1, 1], 1: [0, 1, 1, 2, 1, 2]},
        "hints": [
            "Counting bits separately for every number is O(n log n). Can you reuse the answers for smaller numbers?",
            "`i >> 1` is `i` with its lowest bit removed, and it's smaller than `i`, so its answer is already known.",
            "`ans[i] = ans[i >> 1] + (i & 1)`.",
        ],
        "ref": """
class Solution:
    def countBits(self, n):
        return [bin(i).count("1") for i in range(n + 1)]
""",
    },
    {
        "id": "reverse-bits", "title": "Reverse Bits", "difficulty": "Easy",
        "desc": """
You are given a 32-bit unsigned integer `n`. Reverse the order of its 32 bits (so bit 0 swaps with bit 31, bit 1 with bit 30, and so on) and return the result as an unsigned integer.

**Constraints**

- `0 <= n < 2^32`
""",
        "sig": "def reverseBits(self, n: int) -> int:",
        "tests": [{"n": 43261596}, {"n": 4294967293}, {"n": 0}, {"n": 1}, {"n": 2147483648}, {"n": 4294967295}],
        "expect": {0: 964176192, 1: 3221225471},
        "hints": [
            "Build the answer one bit at a time, taking bits from the low end of `n`.",
            "Each step, shift the result left by one and add `n & 1`, then shift `n` right by one.",
            "Do that exactly 32 times, even if `n` becomes 0 early, so the bits end up in the right positions.",
        ],
        "ref": """
class Solution:
    def reverseBits(self, n):
        return int(format(n, "032b")[::-1], 2)
""",
    },
    {
        "id": "missing-number", "title": "Missing Number", "difficulty": "Easy",
        "desc": """
You are given a list `nums` of `n` distinct numbers taken from the range `0` to `n`. Exactly one number from that range is missing. Return it.

Use O(1) extra space.

**Constraints**

- `1 <= n <= 10^4`
""",
        "sig": "def missingNumber(self, nums: List[int]) -> int:",
        "tests": [{"nums": [3, 0, 1]}, {"nums": [0, 1]}, {"nums": [9, 6, 4, 2, 3, 5, 7, 0, 1]}, {"nums": [0]}, {"nums": [1]},
                  {"nums": [1, 2, 3, 4]}],
        "examples": 3,
        "expect": {0: 2, 1: 2, 2: 8},
        "hints": [
            "You know exactly which numbers should be there: `0` to `n`.",
            "The sum of `0..n` is `n * (n + 1) // 2`. Subtract the actual sum.",
            "Or with XOR: XOR all indices `0..n` together with all values. Everything cancels except the missing number.",
        ],
        "ref": """
class Solution:
    def missingNumber(self, nums):
        return (set(range(len(nums) + 1)) - set(nums)).pop()
""",
    },
    {
        "id": "sum-of-two-integers", "title": "Sum of Two Integers", "difficulty": "Medium",
        "desc": """
Given two integers `a` and `b`, return their sum **without** using the `+` or `-` operators.

Python integers don't overflow, so to handle negative numbers you will need to simulate 32-bit integers with a mask.

**Constraints**

- `-1000 <= a, b <= 1000`
""",
        "sig": "def getSum(self, a: int, b: int) -> int:",
        "tests": [{"a": 1, "b": 2}, {"a": 2, "b": 3}, {"a": -1, "b": 1}, {"a": -5, "b": -7}, {"a": 0, "b": 0}, {"a": 1000, "b": -999},
                  {"a": -1000, "b": 1}],
        "examples": 3,
        "expect": {0: 3, 1: 5, 2: 0},
        "hints": [
            "In binary, `a ^ b` adds the bits without carrying, and `(a & b) << 1` gives the carries.",
            "Repeat: set `a` to the sum without carries and `b` to the carries, until there are no carries left.",
            "In Python, keep values to 32 bits with `& 0xFFFFFFFF` at each step. At the end, if the result is above `0x7FFFFFFF`, convert it back to a negative number with `~(a ^ 0xFFFFFFFF)`.",
        ],
        "ref": """
class Solution:
    def getSum(self, a, b):
        return sum([a, b])
""",
    },
    {
        "id": "reverse-integer", "title": "Reverse Integer", "difficulty": "Medium",
        "desc": """
Given a signed 32-bit integer `x`, return it with its digits reversed, keeping the sign. If the reversed number is outside the signed 32-bit range `[-2^31, 2^31 - 1]`, return `0`.

Pretend you can't store numbers outside that 32-bit range (so check for overflow before it happens).

**Constraints**

- `-2^31 <= x <= 2^31 - 1`
""",
        "sig": "def reverse(self, x: int) -> int:",
        "tests": [{"x": 123}, {"x": -123}, {"x": 120}, {"x": 0}, {"x": 1534236469}, {"x": -2147483412}, {"x": 1463847412},
                  {"x": -2147483648}],
        "examples": 3,
        "expect": {0: 321, 1: -321, 2: 21, 4: 0},
        "hints": [
            "Pop the last digit with `% 10` and push it onto the result with `result * 10 + digit`.",
            "Python's `%` and `//` behave differently for negatives. It's simpler to work with `abs(x)` and put the sign back at the end.",
            "Before pushing a digit, check that `result * 10 + digit` won't exceed `2^31 - 1` (or `2^31` for negative numbers). If it would, return 0.",
        ],
        "ref": """
class Solution:
    def reverse(self, x):
        r = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return r if -2 ** 31 <= r <= 2 ** 31 - 1 else 0
""",
    },
]
