class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # def lcs(self, A, la, B, lb):
    #     # base case
    #     if la == 0 or lb == 0:
    #         return 0
    #
    #     if A[la-1] == B[lb-1]:
    #         return 1 + self.lcs(A, la-1, B, lb-1)
    #     else:
    #         return max(self.lcs(A, la, B, lb-1), self.lcs(A, la-1, B, lb))
    #
    # # recursive code
    # def solve(self, A, B):
    #     self.lcs(A, len(A), B, len(B))

    def solve(self, A, B):
        # +1 id for empty string base case
        row, col = len(A)+1, len(B)+1

        dp = [[0 for _ in range(col)] for _ in range(row)]

        i_index = 0
        for i in range(1, row):
            j_index = 0
            for j in range(1, col):
                if A[i_index] == B[j_index]:
                    dp[i][j] = 1+dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                j_index += 1

            i_index += 1

        print(dp[row-1][col-1])

A = "aaaaaa"
B = "ababab"
Solution().solve(A, B)
