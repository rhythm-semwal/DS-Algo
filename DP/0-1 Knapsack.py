class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        row, col = len(A)+1, C+1

        lookup_table = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(1, row):
            for j in range(1, col):
                # if i == 0 or j == 0:
                #     lookup_table[i][j] = 0
                if B[i-1] <= j:
                    lookup_table[i][j] = max((A[i-1] + lookup_table[i-1][j-B[i-1]]), lookup_table[i-1][j])
                else:
                    lookup_table[i][j] = lookup_table[i-1][j]

        print(lookup_table[row-1][col-1])

    # recursive
    # def ans(self, n, A, B, C):
    #     if n == 0:
    #         return 0
    #     if C <= 0:
    #         return 0
    #
    #     if B[n-1] <= C:
    #         return max((A[n-1] + self.ans(n-1, A, B, C - B[n-1])), self.ans(n-1, A, B, C))
    #     else:
    #         return self.ans(n-1, A, B, C)
    #
    # def solve(self, A, B, C):
    #     return self.ans(len(A), A, B, C)


A = [60, 100, 120]
B = [10, 20, 30]
C = 50

# A = [10, 20, 30, 40]
# B = [12, 13, 15, 19]
# C = 10
print(Solution().solve(A, B, C))
