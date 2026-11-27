class Solution:
    def minMeetingRooms(self, intervals):
        times = sorted(set(t for iv in intervals for t in iv))
        return max(sum(1 for s, e in intervals if s <= t < e) for t in times)
