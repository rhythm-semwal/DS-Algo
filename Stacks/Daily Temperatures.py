from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], [0]*len(temperatures)

        for index in range(len(temperatures)-1, -1, -1):
            while stack:
                if temperatures[index] < temperatures[stack[-1]]:
                    output[index] = stack[-1] - index
                    stack.append(index)
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append(index)

        return output

    
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], [0]*len(temperatures)

        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                popped_element = stack.pop()
                output[popped_element[1]] = index - popped_element[1]
            stack.append((value, index))

        return output


temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))

