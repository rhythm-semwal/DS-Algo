class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {'[': ']', '{': '}', '(': ')'}

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])

            else:
                if not stack:
                    return False
                elif s[i] == hash_map[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
