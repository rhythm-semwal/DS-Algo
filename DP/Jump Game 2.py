# giving TLE - O(N^2)
class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        # base case = if n = 1 return 0
        dp = [0] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i:
                    if dp[i] == 0:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

