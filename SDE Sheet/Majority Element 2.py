"""
Approach with O(1) space
O(1) space using the Boyer-Moore Voting Algorithm. Let me explain why this works and how to implement it.
Key Mathematical Insight
At most 2 elements can appear more than n/3 times in any array.
n
Why? Proof by contradiction:If 3 elements each appear > n/3 times:  Total count > n/3 + n/3 + n/3 = n  But array only has n elements! Contradiction!Therefore: At most 2 candidates possible.
Boyer-Moore Voting Algorithm
Core idea: Maintain at most 2 candidates with counts. When counts cancel out, change candidates.
The 3-Way Cancellation Rule
If we have 3 DIFFERENT elements, cancel all 3:
  [A, B, C] → removes one of each
  
What remains after all cancellations are the majority elements!
If we have 3 DIFFERENT elements, cancel all 3:  [A, B, C] → removes one of each  What remains after all cancellations are the majority elements!
"""

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

