class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        print("***original = ", A)
        n = len(A)
        # transpose of the matrix
        for i in range(n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        print("after transpose = ", A)
        # flipping matrix along the vertical axis
        for i in range(n):
            j = 0
            k = n-1

            while j < k:
                temp = A[i][j]
                A[i][j] = A[i][k]
                A[i][k] = temp

                j += 1
                k -= 1

        print("Rotated matrix = ", A)



input =   [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(Solution().solve(input))