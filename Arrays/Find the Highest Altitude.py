from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0

        running_sum = 0

        for i in gain:
            running_sum += i
            max_altitude = max(max_altitude, running_sum)

        return max_altitude
