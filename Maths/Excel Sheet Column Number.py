class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = len(columnTitle)-1
        power = 0
        result = 0
        while i >= 0:
            result += (ord(columnTitle[i]) - ord('A') + 1) * (26**power)
            power += 1
            i -= 1

        return result
