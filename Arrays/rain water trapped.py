# this question has 3 solutions

# approach 1: using 2 pointers
class Solution1:
    # @param A : tuple of integers
    # @return an integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0

        left_max, right_max = 0, 0

        left, right = 0, len(heights) - 1
        ans = 0

        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= left_max:
                    left_max = heights[left]
                else:
                    ans += left_max - heights[left]

                left += 1

            else:
                if heights[right] >= right_max:
                    right_max = heights[right]
                else:
                    ans += right_max - heights[right]

                right -= 1

        return ans


# using stacks
class Solution2:
    def trap(self, height) -> int:
        if not height:
            return 0

        class Stack:
            def __init__(self):
                self.items = list()

            def pop(self):
                return self.items.pop()

            def push(self, item):
                return self.items.append(item)

            def peek(self):
                return self.items[-1]

            def isEmpty(self):
                return self.items == []

        ans = 0
        stack = Stack()
        index = 0
        n = len(height)

        while index < n:

            while not stack.isEmpty() and (height[index] > height[stack.peek()]):
                top = stack.pop()

                if stack.isEmpty():
                    break

                distance = index - stack.peek() - 1

                width = min(height[index], height[stack.peek()]) - height[top]

                ans += distance * width

            stack.push(index)
            index += 1
        return ans


# approach 3
class Solution3:
    def trap(self, A):
        max_height_index = -1
        max_height = 0
        result = 0
        for index, value in enumerate(A):
            if value > max_height:
                max_height = value
                max_height_index = index

        current_max = -1
        right_max, left_max = max_height, max_height

        for each in range(0, max_height_index+1):
            current_max = max(A[each], current_max)
            result += min(current_max, right_max) - A[each]

        print(result)

        current_max = -1
        for each in range(len(A)-1, max_height_index, -1):
            current_max = max(A[each], current_max)
            result += min(current_max, left_max) - A[each]

        print(result)


if __name__ == "__main__":
    # arr = [2,1,3,2,1,3,1]
    # arr = [0,1,0,2]
    arr = [1, 2]
    print("here")
    print(Solution1().trap(arr))
