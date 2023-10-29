class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        ans = 0
        x_hash_map = dict()
        y_hash_map = dict()

        for i in range(len(A)):
            if A[i] not in x_hash_map:
                x_hash_map[A[i]] = 1
            else:
                x_hash_map[A[i]] += 1

        for i in range(len(B)):
            if B[i] not in y_hash_map:
                y_hash_map[B[i]] = 1
            else:
                y_hash_map[B[i]] += 1

        for i in range(len(A)):
            ans += (x_hash_map[A[i]] - 1) * (y_hash_map[B[i]] - 1)

        print(ans%(10**9+7))

A = [1, 1, 2, 3, 3]
B = [1, 2, 1, 2, 1]
# A = [1, 1, 2]
# B = [1, 2, 1]
Solution().solve(A, B)
