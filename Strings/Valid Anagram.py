class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_array = [0] * 26

        for i in range(len(s)):
            count_array[ord(s[i]) - ord('a')] += 1
            count_array[ord(t[i]) - ord('a')] -= 1

        for each in count_array:
            if each != 0:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        return s == t
