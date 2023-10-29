class Solution:
    # @param A : list of list of integers
    # @return an integer

    # recursive solution
    # def recursive(self, A, row, col):
    #     if row == len(A)-1:
    #         return A[row][col]
    #
    #     current = A[row][col]
    #     left_sum = self.recursive(A, row+1, col)
    #     right_sum = self.recursive(A, row + 1, col+1)
    #
    #     return current + max(left_sum, right_sum)
    #
    # def solve(self, A):
    #     return self.recursive(A, 0, 0)

    # DP solution
    def solve(self, A):
        row, col = len(A), len(A)

        dp = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(col):
            dp[row-1][i] = A[row-1][i]

        for i in range(row-2, -1, -1):
            for j in range(col-1):
                dp[i][j] = A[i][j] + max(dp[i+1][j], dp[i+1][j+1])

        print(dp)




A = [
        [3, 0, 0, 0],
        [7, 4, 0, 0],
        [2, 4, 6, 0],
        [8, 5, 9, 3]
     ]
A = [
        [8, 0, 0, 0],
        [4, 4, 0, 0],
        [2, 2, 6, 0],
        [1, 1, 1, 1]
     ]
print(Solution().solve(A))
