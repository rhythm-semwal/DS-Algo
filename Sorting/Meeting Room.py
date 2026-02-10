# https://neetcode.io/problems/meeting-schedule/question
class Solution:
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        
        intervals.sort(key= lambda x: x[0])

        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if current_interval[1] > intervals[i][0]:
                return False
            else:
                current_interval = intervals[i]

        return True


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    intervals = [(5, 8), (9, 15)]
    intervals = [(5, 8), (8, 15)]
    print(Solution().canAttendMeetings(intervals))
