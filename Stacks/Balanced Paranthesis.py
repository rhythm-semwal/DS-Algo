# @type of s: string
# @return type: integer
class Solution:
    def checkParentheses(self, s: str) -> bool:
        # write your awesome code here
        left_brackets = []
        LOOKUP = {'{': '}', '[': ']', '(': ')'}

        for ch in s:
            if ch in LOOKUP:
                left_brackets.append(ch)
            elif not left_brackets or LOOKUP[left_brackets.pop()] != ch:
                return 0

        return 0 if left_brackets else 1


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = list()
        hash_map = {']':'[', '}':'{', ')':'('}
        for i in range(len(A)):
            if A[i] == '{' or A[i] == '(' or A[i] == '[':
                stack.append(A[i])
            else:
                if len(stack) == 0:
                    return 0
                if hash_map[A[i]] == stack[-1]:
                    stack.pop()
                else:
                    return 0
        if len(stack) == 0:
            return 1
        return 0

# A = '{([])}'
# A = "(){"
A = '()[]'
print(Solution().solve(A))
