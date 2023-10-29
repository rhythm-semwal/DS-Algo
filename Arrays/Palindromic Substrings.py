class Solution:
    def is_palindrome(self, word):
        low, high = 0, len(word)-1
        while low <= high:
            if word[low] != word[high]:
                return False
            low += 1
            high -= 1

        return True

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j+1]):
                    count += 1

        return count


s = 'abc'
print(Solution().countSubstrings(s))