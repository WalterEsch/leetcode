import re

class Solution:
    def isMatch(self, s, p):
        return re.fullmatch(p, s) is not None
