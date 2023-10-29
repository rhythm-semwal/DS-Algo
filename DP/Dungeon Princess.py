class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        row, col = len(A), len(A[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i == row-1 and j == col-1:
                    dp[i][j] = min(0, A[i][j])
                elif i == row-1:
                    dp[i][j] = min(0, A[i][j] + dp[i][j+1])
                elif j == col-1:
                    dp[i][j] = min(0, A[i][j] + dp[i+1][j])
                else:
                    dp[i][j] = min(0, A[i][j] + max(dp[i+1][j], dp[i][j+1]))

        return abs(dp[0][0]) + 1


A = [
       [-2, -3, 3],
       [-5, -10, 1],
       [10, 30, -5]
     ]
A = [
       [1, -1, 0],
       [-1, 1, -1],
       [1, 0, -1]
     ]
print(Solution().calculateMinimumHP(A))
