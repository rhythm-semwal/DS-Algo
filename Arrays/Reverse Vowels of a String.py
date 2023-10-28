class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        vowels_set = ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')

        s_array = list(s)

        while left < right:
            if s_array[left] in vowels_set and s_array[right] in vowels_set:
                s_array[left], s_array[right] = s_array[right], s_array[left]
                left += 1
                right -= 1
            else:
                if s_array[left] in vowels_set:
                    right -= 1
                elif s_array[right] in vowels_set:
                    left += 1
                else:
                    right -= 1
                    left += 1

        return ''.join(s_array)


class Solution2:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        vowels_set = ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')

        s_array = list(s)

        while left < right:
            if s_array[left] in vowels_set and s_array[right] in vowels_set:
                s_array[left], s_array[right] = s_array[right], s_array[left]
                left += 1
                right -= 1
            elif s_array[left] not in vowels_set:
                left += 1
            elif s_array[right] not in vowels_set:
                right -= 1

        return ''.join(s_array)

s = 'aA'
print(Solution().reverseVowels(s))