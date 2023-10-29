class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        matrix = [[0 for _ in range(B+1)] for _ in range(A+1)]

        for i in range(1, A+1):
            print(i)
            for j in range(min(i, B)+1):
                if j == 0 or i == j:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

        return matrix[A][B] % C


A = 4
B = 3
C = 13
print(Solution().solve(A, B, C))
