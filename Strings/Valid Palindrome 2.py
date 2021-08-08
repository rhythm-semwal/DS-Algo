class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """

    def is_palindrome(self, s):
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        return True

    def validPalindrome(self, s):
        # Write your code here
        if self.is_palindrome(s):
            return True

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return self.is_palindrome(s[start + 1:end+1]) or self.is_palindrome(s[start:end])

            start += 1
            end -= 1

        return True