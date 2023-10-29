class Solution:
    def TotalPairs(self, nums, k):
        nums.sort()
        n = len(nums)
        i, j = 1, 0
        temp_set = set()

        while i < n and j < n:
            if i == j:
                if i == n-1:
                    break
                i += 1
            if nums[i] - nums[j] == k:
                i += 1
                j += 1
                temp_set.add((nums[j], nums[i]))

            elif nums[i] - nums[j] > k:
                j += 1
            else:
                i += 1

        return len(temp_set)