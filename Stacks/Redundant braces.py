class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        operands_set = ('+', '-', '/', '*')
        # operand_present = False
        for i in range(len(A)):
            operand_present = False
            if A[i] == ')' and stack[-1] == '(':
                return 1
            elif A[i] == ')':
                while stack and stack[-1] != '(':
                    element = stack.pop()
                    if element in operands_set:
                        operand_present = True

                stack.pop()
                if not operand_present:
                    return 1

            else:
                stack.append(A[i])

        return 0


# class Solution:
#     # @param A : string
#     # @return an integer
#     def braces(self, A):
#         stack = list()
#
#         for i in range(len(A)):
#             if A[i] != ')':
#                 stack.append(A[i])
#             else:
#                 result = ""
#                 element = stack[-1]
#                 while element != '(':
#                     result += stack.pop()
#                     element = stack[-1]
#
#                 stack.pop()
#                 if '+' in result or '-' in result or '*' in result or '/' in result:
#                     continue
#                 else:
#                     return 1
#
#         print(stack)
#         return 0


# A = "(a+(a+b))"
A = "((a+b))"
print(Solution().braces(A))
