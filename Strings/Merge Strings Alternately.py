class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer = 0
        result = ''
        for i in range((min(len(word1), len(word2)))):
            result += word1[i] + word2[i]
            pointer += 1
        
        if pointer < len(word1):
            result += word1[pointer:]
        if pointer < len(word2):
            result += word2[pointer:]
        
        return result
