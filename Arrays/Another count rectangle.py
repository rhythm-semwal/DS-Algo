class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A) == 0:
            return 0

        n = len(A)
        j = n - 1
        ans = 0

        # for i in range(n):
        #     while j >= 0 and A[i] * A[j] >= B:
        #         j -= 1
        #
        #     ans += j + 1

        i = 0
        while i <= j:
            if A[i] * A[j] >= B:
                j -= 1
            else:
                ans += 2*(j-i)+1
                i += 1
        print(ans)
        # return ans % 1000000007


# A = [1, 2, 3, 4, 5, 6, 7, 8, 14]
# B = 12

A = [1, 2]
B = 5
# A = [ 1, 2 ]
# B = 1
Solution().solve(A, B)
