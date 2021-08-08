"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        current_end_time = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < current_end_time:
                return False

        return True

    def canAttendMeetings1(self, intervals):
        # Write your code here
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)

        end = intervals[0].end

        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                return False
            end = intervals[i].end

        return True

x = [(0,30),(15,20),(5,10)]
# x = [(5,8),(9,15)]
print(Solution().canAttendMeetings(x))