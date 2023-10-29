class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x + 1

        while left < right:
            mid = (left + right) // 2

            if mid * mid > x:
                right = mid
            else:
                # we are doing mid+1 because as we already know that mid is
                # less than x so we are doing mid+1
                left = mid + 1

        return left - 1
