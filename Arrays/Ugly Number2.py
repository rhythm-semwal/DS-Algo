class Solution1:
    """
    We will use a dynamic programming approach to solve this problem. We will start with the first ugly number, which is 1, and then generate all the other ugly numbers. We will use three pointers to keep track of the next multiple of 2, 3, and 5 respectively. We will generate the next ugly number by selecting the minimum of the three next multiples, adding it to the list of ugly numbers, and updating the corresponding pointer. We will repeat this process until we have generated the nth ugly number.

    The time complexity of this algorithm is O(n), and the space complexity is O(n) as we need to store the list of n ugly numbers.
    """
    def nthUglyNumber(self, n: int) -> int:
        ugly_number = [1]
        i2, i3, i5 = 0,0,0

        while len(ugly_number) < n:
            next = min(ugly_number[i2]*2, ugly_number[i3]*3, ugly_number[i5]*5)
            ugly_number.append(next)

            if next == ugly_number[i2]*2:
                i2 += 1
            if next == ugly_number[i3]*3:
                i3 += 1
            if next == ugly_number[i5]*5:
                i5 += 1

        return ugly_number[-1]



class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        result = []

        i = 0
        num = 1

        while i < n:
            temp_num = num
            for prime_factor in [2, 3, 5]:
                while temp_num > 1 and temp_num % prime_factor == 0:
                    temp_num //= prime_factor

            if temp_num == 1:
                result.append(num)
                i = len(result)
            num += 1

        return result[n-1]


n = 10
print(Solution().nthUglyNumber(n))
