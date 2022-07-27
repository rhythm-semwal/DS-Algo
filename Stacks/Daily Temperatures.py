from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], [0]*len(temperatures)

        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                popped_element = stack.pop()
                output[popped_element[1]] = index - popped_element[1]
            stack.append((value, index))

        return output


temperatures = [50,60,70]
print(Solution().dailyTemperatures(temperatures))

