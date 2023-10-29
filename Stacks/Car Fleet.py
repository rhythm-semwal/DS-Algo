from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # sorting the array so that comparison becomes easy as it won;t have any impact on the position and speed
        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            # if there are 2 elements in stack and top of the stack reaches the target before the second top element
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)