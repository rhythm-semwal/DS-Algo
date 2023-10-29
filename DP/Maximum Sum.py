class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        prefix_array = [0]*n

        prefix_array[0] = A[0]*B

        for i in range(1, n):
            prefix_array[i] = max(prefix_array[i-1], A[i]*B)

        # print(prefix_array)

        prefix_array[0] = prefix_array[0] + A[0]*C

        for i in range(1, n):
            prefix_array[i] = max(prefix_array[i-1], prefix_array[i]+A[i]*C)

        # print(prefix_array)

        prefix_array[0] = prefix_array[0] + A[0] * D
        for i in range(1, n):
            prefix_array[i] = max(prefix_array[i-1], prefix_array[i]+A[i]*D)

        return prefix_array[-1]
