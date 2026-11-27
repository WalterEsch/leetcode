class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        q = collections.deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for v in words:
                if v not in seen and sum(a != b for a, b in zip(v, w)) == 1:
                    seen.add(v)
                    q.append((v, d + 1))
        return 0
