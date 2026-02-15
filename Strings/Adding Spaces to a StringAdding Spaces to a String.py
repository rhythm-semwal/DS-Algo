# https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=problem-list-v2&envId=two-pointers

# My approach 1

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        start, end = 0, 0
        result = ''

        for space in spaces:
            while end != space:
                end += 1

            if end == space:
                result += s[start:end] + ' '
                start = end

        result += s[end:]
        return result

# Approach 2: optimised
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        start = 0

        for space in spaces:
            result.append(s[start:space])
            result.append(' ')
            start = space

        result.append(s[start:])
        return "".join(result)
