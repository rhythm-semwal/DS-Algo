from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3:
            return []

        # Measure #1 to avoid the duplicates
        nums.sort()

        for i in range(len(nums)-2):
            # Measure #2 to avoid the duplicates
            if i == 0 or nums[i] != nums[i-1]:
                low = i+1
                high = len(nums)-1
                while low < high:
                    if nums[i] + nums[low] + nums[high] == 0:
                        temp = [nums[i], nums[low], nums[high]]
                        result.append(temp)

                        # Measure #3 to avoid the duplicates
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while high > low and nums[high] == nums[high-1]:
                            high -= 1

                        low += 1
                        high -= 1

                    elif nums[i] + nums[low] + nums[high] > 0:
                        high -= 1
                    else:
                        low += 1
        return result


        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.append([nums[i], nums[j], nums[k]])

        # print(result)


nums = [-1,0,1,2,-1,-4]
# nums = [1,2,-2,-1]
# nums = [-2,0,1,1,2]
print(Solution().threeSum(nums))
