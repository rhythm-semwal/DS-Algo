# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
find all intervals strictly to the left and right of the new interval.
if any interval in between, they overlap with the new interval.

if any overlap is there than left <= right and then update the new interval
at the end return the left half + new interval + right half
"""

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        left, right = 0, len(intervals)-1

        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1

        while right >= 0 and intervals[right][0] > newInterval[1]:
            right -= 1

        if left <= right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right][1])

        return intervals[:left] + [newInterval] + intervals[right+1:]


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))
