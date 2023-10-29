class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        """
            Algorithm:
            1. if character is operand, put in output string
            2. if character is ')', push it to stack
            3. if character is '(', pop from stack until you get ')' at the top of stack.Then pop ')' also.
            4. if character is operator then check the precedence.
                a. if character precedence is higher than precedence of operator present at top of stack, push it to stack
                b. else if character precedence is lower than precedence of operator present at top of stack, add it to
                output string and push the character to the stack.
                c. also check for associativity.
            5. reverse the result
        """
        stack = list()
        result = ""
        operators_set = ('+', '-', '/', '*', '^')
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        # if current operator precedence is less than top of stack, then pop from stack and append to ans.
        # pop from stack till stack.top() > current operator
        for i in range(len(A)-1, -1, -1):

            # if current element is an operand or ( add to stack
            if A[i].isalnum():
                result += A[i]

            elif A[i] == ')':
                stack.append(A[i])

            elif A[i] in operators_set:
                while len(stack) != 0 and stack[-1] != ')' and precedence[A[i]] <= precedence[stack[-1]]:
                        result += stack.pop()

                stack.append(A[i])

            elif A[i] == '(':
                while len(stack) != 0 and stack[-1] != ')':
                    result += stack.pop()

                stack.pop()

        while len(stack):
            result += stack.pop()

        print(result[::-1])


# A = "x^y/(a*z)+b"
# A = "A * B + C / D"
A = "(A - B/C) * (A/K-L)"
Solution().solve(A)
