class Solution:
    def alienOrder(self, words):
        letters = sorted(set("".join(words)))
        g = {c: set() for c in letters}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    g[x].add(y)
                    break
            else:
                if len(a) > len(b):
                    return ""
        indeg = {c: 0 for c in letters}
        for x in g:
            for y in g[x]:
                indeg[y] += 1
        q = [c for c in letters if indeg[c] == 0]
        out = []
        while q:
            x = q.pop(0)
            out.append(x)
            for y in sorted(g[x]):
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        return "".join(out) if len(out) == len(letters) else ""
