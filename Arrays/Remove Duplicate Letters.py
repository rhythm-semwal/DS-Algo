class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for index, value in enumerate(s):
            last_occurrence[value] = index

        stack = []
        visited_elements = set()

        for index, value in enumerate(s):
            if value in visited_elements:
                continue
            while stack and value < stack[-1] and index < last_occurrence[stack[-1]]:
                visited_elements.remove(stack.pop())
            stack.append(value)
            visited_elements.add(value)

        return "".join(stack)



s = "bcabc"
print(Solution().removeDuplicateLetters(s))