import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high

        while low < high:
            mid = (low+high)//2
            hours = 0

            for n in piles:
                hours += math.ceil(n/mid)

            if hours <= h:
                result = min(result, mid)
                high = mid-1
            else:
                low = mid+1

        return result


piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))
