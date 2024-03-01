class Solution1:
    # recursive solution
    # TC = O(2^(m + n))
    # SC = O(min(m, n)) =
    #   the maximum depth of the recursion stack is min(m, n), where m and n are the lengths of the input strings.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2, 0, 0)

    def helper(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0

        if s1[i] == s2[j]:
            return 1+self.helper(s1, s2, i+1, j+1)
        else:
            return max(self.helper(s1,s2,i+1,j), self.helper(s1,s2,i,j+1))


class Solution2:
    # TC = O(text1 * text2)
    # SC = O(text1 * text2)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r, c = len(text1), len(text2)

        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
Solution2().longestCommonSubsequence(text1, text2)
