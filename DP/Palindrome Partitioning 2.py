class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)
        cuts = [0]* (n+1)
        dp = [[False for _ in range(n)] for _ in range(n)]

        # base case
        # when length = 1 ans is 0 because no cuts are required as string of length 1 is palindrome
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n+1):
            for i in range(n-L+1):
                j = L+i-1
                if L == 2:
                    dp[i][j] = (A[i] == A[j])
                else:
                    dp[i][j] = (A[i] == A[j] and dp[i+1][j-1])

        import sys

        for i in range(n):
            if dp[0][i]:
                cuts[i] = 0
            else:
                cuts[i] = sys.maxsize
                for j in range(i):
                    if dp[j+1][i]:
                        cuts[i] = min(cuts[i], 1+cuts[j])

        print(cuts)

    # TC = O(N^3)
    # def minCut(self, A):
    #     n = len(A)
    #     cuts = [[0 for _ in range(n)] for _ in range(n)]
    #     dp = [[False for _ in range(n)] for _ in range(n)]
    #
    #     # base case
    #     # when length = 1 ans is 0 because no cuts are required as string of length 1 is palindrome
    #     for i in range(n):
    #         dp[i][i] = True
    #         cuts[i][i] = 0
    #
    #     import sys
    #     for L in range(2, n+1):
    #         for i in range(n-L+1):
    #             j = L+i-1
    #             if L == 2:
    #                 dp[i][j] = (A[i] == A[j])
    #             else:
    #                 dp[i][j] = (A[i] == A[j] and dp[i+1][j-1])
    #
    #             if dp[i][j]:
    #                 cuts[i][j] = 0
    #             else:
    #                 cuts[i][j] = sys.maxsize
    #
    #                 for k in range(i, j):
    #                     count = 1+cuts[i][k] + cuts[k+1][j]
    #                     cuts[i][j] = min(count, cuts[i][j])
    #
    #     print(dp)
    #     print(cuts[0][n-1])

    # recursive solution
    # def is_palindrome(self,A , start, end):
    #     while start < end:
    #         if A[start] != A[end]:
    #             return False
    #         start +=1
    #         end -= 1
    #
    #     return True
    #
    # def solve(self, A, start, end):
    #     if start >= end or self.is_palindrome(A, start, end):
    #         return 0
    #
    #     ans = float('inf')
    #     for i in range(start, end):
    #         count = 1 + self.solve(A, start, i) + self.solve(A, i+1, end)
    #         ans = min(ans, count)
    #
    #     return ans
    #
    # def minCut(self, A):
    #     return self.solve(A, 0, len(A)-1)


string = "abab"
print(Solution().minCut(string))
