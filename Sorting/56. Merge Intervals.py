# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals):

        # sorting based on the start time
        intervals.sort(key=lambda x: x[0])

        current_interval = intervals[0]
        result = []

        for i in range(1, len(intervals)):
            # end time > start time
            if current_interval[1] >= intervals[i][0]:
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                result.append(current_interval)
                current_interval = intervals[i]

        result.append(current_interval)
        return result


interval = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
print(Solution().merge(interval))