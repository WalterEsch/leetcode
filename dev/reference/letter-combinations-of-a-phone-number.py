class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        keys = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return ["".join(p) for p in itertools.product(*(keys[d] for d in digits))]
