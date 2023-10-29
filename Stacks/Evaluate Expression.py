class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        result = 0
        operators = {'-': lambda x, y: y - x,
                     '+': lambda x, y: x + y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: y // x}
        for i in range(len(A)):
            if A[i] not in operators:
                stack.append(int(A[i]))
            else:
                stack.append(operators[A[i]](stack.pop(), stack.pop()))

        return stack[-1]

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = list()
        operators_set = ('+','-','/','*')
        def add(num1, num2):
            return num1+num2

        def subtract(num1, num2):
            return num2-num1

        def divide(num1, num2):
            return num2//num1

        def multiply(num1, num2):
            return num1*num2

        for i in range(len(A)):
            if A[i] not in operators_set:
                stack.append(A[i])
            else:
                first_operand = int(stack.pop())
                second_operand = int(stack.pop())
                if A[i] == '+':
                    stack.append(add(first_operand, second_operand))
                elif A[i] == '-':
                    stack.append(subtract(first_operand, second_operand))
                elif A[i] == '*':
                    stack.append(multiply(first_operand, second_operand))
                else:
                    stack.append(divide(first_operand, second_operand))

        return stack[-1]


# A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "-"]
print(Solution().evalRPN(A))
