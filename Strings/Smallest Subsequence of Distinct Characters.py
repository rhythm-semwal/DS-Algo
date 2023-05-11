"""
Similar to Remove Duplicate Letters
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {}
        stack = []
        visited = set()

        for index, value in enumerate(s):
            last_occurrence[value] = index

        print(last_occurrence)
        for index, value in enumerate(s):
            if value in visited:
                continue
            while stack and value < stack[-1] and index < last_occurrence[stack[-1]]:
                visited.remove(stack.pop())

            visited.add(value)
            stack.append(value)

        return "".join(stack)


s = 'cbacdcbc'
print(Solution().smallestSubsequence(s))