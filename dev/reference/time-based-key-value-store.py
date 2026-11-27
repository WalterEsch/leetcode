class TimeMap:
    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        best = ""
        for t, v in self.d.get(key, []):
            if t <= timestamp:
                best = v
        return best
