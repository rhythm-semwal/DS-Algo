class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_s = s + s

        return s in new_s[1:-1]
