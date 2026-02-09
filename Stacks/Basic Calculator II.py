class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_operator = '+'
        num = 0

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s)-1:
                if prev_operator == '+':
                    stack.append(num)
                elif prev_operator == '-':
                    stack.append(-num)
                elif prev_operator == '*':
                    stack.append(stack.pop() * num)
                elif prev_operator == '/':
                    stack.append(int(stack.pop() / num))

                prev_operator = ch
                num = 0

        return sum(stack)
