class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1, count2 = 0, 0
        i, j = 0, len(s) - 1
        vowel_set = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        while i < j:
            count1 += s[i] in vowel_set
            count2 += s[j] in vowel_set
            i += 1
            j -= 1

        return count1 == count2


class Solution2:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2

        count1, count2 = 0, 0
        vowel_set = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        for i in s[:mid]:
            if i in vowel_set:
                count1 += 1

        for i in s[mid:]:
            if i in vowel_set:
                count2 += 1

        return count1 == count2
