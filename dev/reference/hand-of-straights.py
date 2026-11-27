class Solution:
    def isNStraightHand(self, hand, groupSize):
        cards = sorted(hand)
        while cards:
            start = cards[0]
            for v in range(start, start + groupSize):
                if v not in cards:
                    return False
                cards.remove(v)
        return True
