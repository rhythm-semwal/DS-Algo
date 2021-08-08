class Solution:
    def lps(self, s):
        n = len(s)
        i, j = 0, 1
        lps = [0] * n

        while j < n:
            if s[i] == s[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i-1]

        print(lps)

# s = "abab"
s = "aaaa"
Solution().lps(s)