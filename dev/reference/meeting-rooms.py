class Solution:
    def canAttendMeetings(self, intervals):
        return all(not (a[0] < b[1] and b[0] < a[1]) for i, a in enumerate(intervals) for b in intervals[i + 1:])
