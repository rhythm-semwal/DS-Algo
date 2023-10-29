class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        for index, value in enumerate(word):
            if value == ch:
                right = index
                break

        left = 0
        result = list(word)

        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        return ''.join(result)


word = "abcdefd"
ch = "d"

word = "xyxzxe"
ch = "z"

word = "abcd"
ch = "z"
print(Solution().reversePrefix(word, ch))
