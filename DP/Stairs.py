class Solution:
    # @param A : integer
    # @return an integer

    # approach 1 => top down approach
    def climbStairs(self, A):
        dp = dict()
        dp[1] = 1
        dp[2] = 2
        if A == 1:
            return 1
        if A == 2:
            return 2

        dp[1] = 1
        dp[2] = 2

        for i in range(3, A + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp[A])

    # approach 2 => bottom up approach
    def calculate_answer(self, n, hash_map):
        if n == 1:
            return hash_map[n]
        elif n == 2:
            return hash_map[n]

        else:
            hash_map[n] = self.calculate_answer(n-1, hash_map) + self.calculate_answer(n-2, hash_map)
            return hash_map[n]

    def climbStairs(self, A):
        dp = dict()
        dp[1] = 1
        dp[2] = 2
        if A == 1:
            return 1
        if A == 2:
            return 2

        dp[1] = 1
        dp[2] = 2

        return self.calculate_answer(A, dp)


A = 3
print(Solution().climbStairs(A))
