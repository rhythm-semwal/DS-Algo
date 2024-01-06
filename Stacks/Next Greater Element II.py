class Solution:
    def nextGreaterElements(self, num):
        result = [-1] * len(nums)
        stack = [nums[-1]]

        for i in range(len(nums) - 2, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(nums[i])

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(nums[i])

        return result


nums = [1,2,3,4,3]
print(Solution().nextGreaterElements(nums))
