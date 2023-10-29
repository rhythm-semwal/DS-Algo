# @type of k: integer
# @type of n: integer
# @return type: integer
class Solution:
    def calculatePower(self, k: int, n: int) -> int:
        # write your awesome code here
        if n == 0:
            return 1

        temp = self.calculatePower(k, n // 2)

        if n % 2 == 0:
            return temp * temp

        else:
            if n > 0:
                return temp * temp * k
            else:
                return (temp * temp) // k


print(Solution().calculatePower(2,3))