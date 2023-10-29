class Solution:
    def count_vowels(self, word):
        vowels_set = ('a', 'e', 'i', 'o', 'u')
        count = 0
        for each in word:
            if each in vowels_set:
                count += 1
        return count

    def maxVowels(self, s: str, k: int) -> int:
        """
        This will be solved using the sliding window approach
        1. Calculate the number of vowels in the range till k
        2. After that start iterating ffrom k to end of the string.
        3. If the removed word is a vowel then reduce the count.
        4. If the added word is a vowel than add the count
        """
        if len(s) == k:
            return self.count_vowels(s[:k])
          
        vowels_set = ('a', 'e', 'i', 'o', 'u')

        count = self.count_vowels(s[:k])
        result = count

        low = 1
        high = k

        while high < len(s):
            if s[low-1] in vowels_set:
                count -= 1
            if s[high] in vowels_set:
                count += 1
            result = max(count, result)
            high += 1
            low += 1
        if result != float('-inf'):
            return result
        else:
            return 0
