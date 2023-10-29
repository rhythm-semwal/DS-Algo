class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:k] == needle:
                return i
            k += 1

        return -1
