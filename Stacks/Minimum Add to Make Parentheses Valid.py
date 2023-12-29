class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for i in s:
            # if i == ')' and not stack:
            #     stack.append(i)
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack)


s = "())"
s = "((())))"
s = "()))(("
print(Solution().minAddToMakeValid(s))
