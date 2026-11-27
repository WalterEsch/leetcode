class Solution:
    def mergeTriplets(self, triplets, target):
        best = [0, 0, 0]
        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                best = [max(best[i], t[i]) for i in range(3)]
        return best == target
