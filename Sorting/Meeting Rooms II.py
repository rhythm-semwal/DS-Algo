# https://neetcode.io/problems/meeting-schedule-ii/question

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)

        heap = []

        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if heap and heap[0] <= start:
                heappop(heap)

            heappush(heap, end)

        return len(heap)
      

# Approach 2 using the difference array technique. So we make the start as +1 and end as -1 meaning start +1 is a room is occupied and -1 means room is free.
# Then we sort the array and keep a count of current_rooms available and max_room
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        changes = []

        for each in intervals:
            start = each.start
            end = each.end

            changes.append((start, 1))
            changes.append((end, -1))
        
        changes.sort(key = lambda x:(x[0], x[1]))

        max_rooms, current_rooms = 0, 0

        for time, change in changes:
            current_rooms += change
            max_rooms = max(max_rooms, current_rooms)
        
        return max_rooms


