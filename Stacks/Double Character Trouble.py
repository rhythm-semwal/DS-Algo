class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack = list()
        result = ""
        stack.append(A[-1])
        for i in range(len(A)-2, -1, -1):
            current = A[i]
            if len(stack) == 0:
                stack.append(A[i])
            else:
                if current == stack[-1]:
                    stack.pop()
                else:
                    stack.append(A[i])

        while len(stack) > 0:
            result += stack.pop()
        return result


# A = "abccbc"
A = "ab"
print(Solution().solve(A))
