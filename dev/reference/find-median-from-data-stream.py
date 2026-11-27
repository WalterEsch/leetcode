class MedianFinder:
    def __init__(self):
        self.a = []

    def addNum(self, num):
        bisect.insort(self.a, num)

    def findMedian(self):
        a, n = self.a, len(self.a)
        return float(a[n // 2]) if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
