class Solution:
    def removeDuplicates(self, nums):
        # index = 1
        # for i in range(len(nums)-1):
        #     if nums[i] != nums[i+1]:
        #         nums[index] = nums[i+1]
        #         index += 1
        # return index

        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i+1


nums = [1,1,2]
print(Solution().removeDuplicates(nums))