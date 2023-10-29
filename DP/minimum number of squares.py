class Solution:
    # @param A : integer
    # @return an integer

    # brute force using recursion
    # def countMinSquares(self, A):
    #     if A <= 3:
    #         return A
    #
    #     ans = A
    #
    #     for i in range(1, A+1):
    #         ans = min(ans, 1+self.countMinSquares(A-i*i))
    #     return ans

    def countMinSquares(self, A):
        import math
        if A <= 3:
            return A

        dp = list()
        # for n = 0
        dp.append(0)
        # for n = 1
        dp.append(1)
        for i in range(2, A+1):
            # in worst case for any number n the max number of squares needed will be = n if we do 1^2 n times
            dp.append(i)
            # iterate from 1 to sqrt(A)+1 and check for all the possible numbers
            for x in range(1, int(math.ceil(math.sqrt(i)))+1):
                dp[i] = min(dp[i], dp[i-(x*x)]+1)

        print(dp)

A = 41
Solution().countMinSquares(A)
