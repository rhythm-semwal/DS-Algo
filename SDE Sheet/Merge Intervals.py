# https://leetcode.com/problems/merge-intervals/
# check with interviewer if the interval is sorted or not
# advantage of sorting is that all the overlappingintervals will be consecutilvely and hence is easy to check
from typing import List


class Solution:
    def letter_cmp(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] == b[0]:
            if a[1] > b[1]:
                return 1
            else:
                return -1
        else:
            return 1

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from functools import cmp_to_key
        letter_cmp_key = cmp_to_key(self.letter_cmp)
        intervals.sort(key=letter_cmp_key)
        print(intervals)
        result = []
        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                result.append(current_interval)
                current_interval = intervals[i]

        result.append(current_interval)
        print(result)


# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[2,3]]
Solution().merge(intervals)

