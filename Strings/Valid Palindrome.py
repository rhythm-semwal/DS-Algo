import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_characters = set(string.ascii_lowercase + string.digits)

        word = [each for each in s.lower() if each in allowed_characters]

        start, end = 0, len(word)-1

        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -=1
        return True
