class Solution:
    def FindWays(self, n, m, blocked_cells):
        # Code here
        # 		print(blocked_cells)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        if [1, 1] not in blocked_cells:
            dp[0][0] = 1
        else:
            return 0

        for i in range(1, n):
            if [i + 1, 1] not in blocked_cells:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0

        for i in range(1, m):
            if [1, i + 1] not in blocked_cells:
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = 0
        mod = 1000000007
        for i in range(1, n):
            for j in range(1, m):
                if [i + 1, j + 1] not in blocked_cells:
                    dp[i][j] = dp[i - 1][j] % mod + dp[i][j - 1] % mod
                else:
                    dp[i][j] = 0

        return dp[n - 1][m - 1]


# n = 3, m = 3, k = 2,
# blocked_cells = {{1,2},{3,2}}.