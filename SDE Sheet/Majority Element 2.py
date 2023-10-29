from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        c1, c2 = 0, 0
        n = len(nums)
        for i in range(n):
            if num1 == nums[i]:
                c1 += 1
            elif num2 == nums[i]:
                c2 += 1
            elif c1 == 0:
                num1 = nums[i]
                c1 = 1
            elif c2 == 0:
                num2 = nums[i]
                c2 = 1

            else:
                c1 -= 1
                c2 -= 1

        result = []

        if c1 > 0:
            count = 0
            for i in range(n):
                if nums[i] == num1:
                    count += 1

            if count > n//3:
                result.append(num1)

        if c2 > 0:
            count = 0
            for i in range(n):
                if nums[i] == num2:
                    count += 1

            if count > n // 3:
                result.append(num2)

        print(result)

nums = [0,0,0]
print(Solution().majorityElement(nums))

