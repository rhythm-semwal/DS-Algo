class Solution:
    def evalRPN(self, tokens) -> int:
        operator_list = ['+', '-', '*', '/']
        temp_array = []
        for index, value in enumerate(tokens):
            if value not in operator_list:
                temp_array.append(int(value))
            else:
                if value == '+':
                    ans = temp_array[-1] + temp_array[-2]
                elif value == '*':
                    ans = temp_array[-1] * temp_array[-2]
                elif value == '-':
                    ans = temp_array[-2] - temp_array[-1]
                else:
                    ans = int(temp_array[-2] / temp_array[-1])
                temp_array.pop()
                temp_array.pop()
                temp_array.append(ans)

        return temp_array[0]