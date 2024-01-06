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


class Solution2:
    # TC = O(n**2 * log(M)) where M is the length of the set for the lookup
    # SC = O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()

        for i in range(len(nums)-2):
            temp_set = set()
            for j in range(i+1, len(nums)):
                current_sum = -(nums[i] + nums[j])
                if current_sum in temp_set:
                    result = [nums[i], nums[j], current_sum]
                    result_set.add(tuple(sorted(result)))
                else:
                    temp_set.add(nums[j])

        answer = []
        for each in result_set:
            answer.append(list(each))

        return answer


nums = [-1,0,1,2,-1,-4]
# nums = [1,2,-2,-1]
# nums = [-2,0,1,1,2]
print(Solution().threeSum(nums))
