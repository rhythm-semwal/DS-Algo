# https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        result = 0
        sign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append((result, sign))
                sign = 1
                result = 0
            elif ch == ')':
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + (result * prev_sign)
        
        return result + sign * num
