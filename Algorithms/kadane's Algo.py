class Solution:
    def maxSubArraySum(self, a, size):
        ans = a[0]
        max_so_far = a[0]
        for i in range(1, size):
            max_so_far = max(a[i], max_so_far + a[i])

            if max_so_far > ans:
                ans = max_so_far

        return ans
