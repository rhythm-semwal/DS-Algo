class Solution:
    def fourSum(self, nums, target: int):
        n = len(nums)

        if n == 0:
            return nums

        hash_set = set()
        result = []
        nums.sort()

        for i in range(n):
            for j in range(i+1, n):
                left = j+1
                right = n-1

                current_sum = nums[i] + nums[j]

                while left < right:
                    if current_sum + nums[left] + nums[right] == target:
                        temp = (nums[i], nums[j], nums[left], nums[right])
                        hash_set.add(temp)
                        left += 1
                        right -= 1

                        # while left < right and nums[left] == temp[2]:
                        #     left += 1
                        #
                        # while left < right and nums[right] == temp[3]:
                        #     right -= 1

                    elif current_sum + nums[left] + nums[right] > target:
                        right -= 1

                    else:
                        left += 1
            #     j += 1
            #     while j+1 < n and nums[j] == nums[j-1]:
            #         j += 1
            # i += 1
            # while i+1 < n and nums[i] == nums[i-1]:
            #     i += 1

        for each in hash_set:
            result.append(list(each))
        return result


nums = [-2,-1,-1,1,1,2,2]
target = 0
print(Solution().fourSum(nums, target))
