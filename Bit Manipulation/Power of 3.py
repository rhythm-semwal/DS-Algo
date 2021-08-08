import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # TC = O(1)
        if n <= 0:
            return False

        max_int = 2 ** 31 - 1

        max_power = int(math.log(max_int, 3))

        return 3 ** max_power % n == 0

    def isPowerOfThree1(self, n: int) -> bool:
        # TC = O(log3N)
        if n < 1:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1