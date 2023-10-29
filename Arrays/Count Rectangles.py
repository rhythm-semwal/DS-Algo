class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        ans = 0
        hash_set = set()
        for i in range(len(A)):
            hash_set.add((A[i], B[i]))

        for i in range(len(A)):
            for j in range(len(B)):
                if i == j:
                    continue

                if A[i] < A[j] and B[i] < B[j]:
                    x3, y3 = A[j], B[i]
                    x4, y4 = A[i], B[j]
                    if (x3, y3) in hash_set and (x4, y4) in hash_set:
                        ans += 1
        print(ans)


A = [1, 1, 2, 2, 3, 3]
B = [1, 2, 1, 2, 1, 2]
Solution().solve(A, B)