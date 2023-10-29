class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        row, col = len(A), len(A[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]

        if A[0][0] == 0:
            dp[0][0] = 1

        for i in range(1, col):
            if A[0][i] == 0:
                # this we are doing because we have to check the left cell also if there is obstacle
                # then we can never reach
                dp[0][i] = dp[0][i-1]

        for i in range(1, row):
            if A[i][0] == 0:
                # this we are doing because we have to check the above cell
                # also if there is obstacle then we can never reach
                dp[i][0] = dp[i-1][0]

        for i in range(1, row):
            for j in range(1, col):
                if A[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        print(dp[row-1][col-1])


A = [[1, 0]]
Solution().uniquePathsWithObstacles(A)
