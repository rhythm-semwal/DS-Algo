from typing import List


class Solution1:
    # https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/?envType=study-plan-v2&envId=leetcode-75
    """
    The idea here is to use the number of 1's in i >> 1 (i.e., i divided by 2)
    and the last bit in i to find the number of 1's in i.
    """
    def countBits(self, n: int) -> List[int]:
        result = [0]

        for i in range(1, n + 1):

            # i >> 1 ====> i divided by 2
            # i % 2 = i & 1
            # result.append(result[i >> 1] + i % 2)
            result.append(result[i >> 1] + (i & 1))

        return result


class Solution2:
    def countBits(self, n: int) -> List[int]:
        result = [0]

        for i in range(1, n+1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            result.append(count)

        return result

n = 5
print(Solution1().countBits(n))


