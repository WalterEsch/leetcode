class DetectSquares:
    def __init__(self):
        self.pts = []

    def add(self, point):
        self.pts.append(tuple(point))

    def count(self, point):
        x, y = point
        total = 0
        cnt = collections.Counter(self.pts)
        for (px, py), k in cnt.items():
            if px != x and abs(px - x) == abs(py - y):
                total += k * cnt[(x, py)] * cnt[(px, y)]
        return total
