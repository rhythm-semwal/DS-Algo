class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x : x[0])
        print(intervals)
        count = 0
        current_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if current_end > intervals[i][0]:
                count += 1
                current_end = min(current_end, intervals[i][1])
            else:
                current_end = intervals[i][1]

        return count

# intervals = [[1,2],[2,3],[3,4],[1,3]]
# intervals = [[1,2],[1,2],[1,2]]
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(Solution().eraseOverlapIntervals(intervals))