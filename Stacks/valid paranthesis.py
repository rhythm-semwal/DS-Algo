class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starting_brackets = ['(', '{', '[']
        braces_mapping = {'[':']', '{':'}', '(':')'}

        for i in range(len(s)):
            if s[i] in starting_brackets:
                stack.append(s[i])
            else:
                if stack:
                    current = stack.pop()
                    if braces_mapping[current] != s[i]:
                        return False
                else:
                    return False

        return False if stack else True


if __name__ == "__main__":
    input = ']'
    print(Solution().isValid(input))
