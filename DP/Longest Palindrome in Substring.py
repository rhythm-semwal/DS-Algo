
# T.C = O(N**2)
# S.C = O(N**2)

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            """
            This condition (i - j <= 2) has been added to check the below condition
            If the substring has a length of 1 or 2, then it's a palindrome. 
            This is because a single character is always a palindrome, 
            and a two-character substring is a palindrome if the characters are the same.
           """
            """
            dp[j + 1][i - 1] - when I am at position i and j , then I am checking if 
            string between j+1 and i-1 is palindrome or not
            """
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > Max_Len:
                        Max_Len = i - j + 1
                        Max_Str = s[j:i + 1]
        return Max_Str


# T.C = O(N**3)
# S.C = O(1)

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_length = 0
        max_substring = s[0]

        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if j-i+1 > max_length and s[i:j+1] == s[i:j+1][::-1]:
                    max_length = j-i+1
                    max_substring = s[i:j+1]

        return max_substring


s = 'babad'
s = 'forgeeksskeegfor'
print(Solution1().longestPalindrome(s))
