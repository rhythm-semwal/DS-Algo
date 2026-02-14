# https://leetcode.com/problems/k-radius-subarray-averages/description/
# Initial approach by me
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        result = [-1]*len(nums)

        prefix_sum_array = [0] * len(nums)
        running_sum = 0
        for index, num in enumerate(nums):
            running_sum += num
            prefix_sum_array[index] = running_sum

        start = 0
        end = start+k

        while True:
            if end-start == k and len(nums)-end > k:
                total_sum = prefix_sum_array[end] + (prefix_sum_array[end+k] - prefix_sum_array[end])
                if start > 0:
                    total_sum -= prefix_sum_array[start-1]
                result[end] = total_sum//   (k*2+1)

                end += 1
                start += 1
            else:
                break

        return result


# Optimised approach from cursor
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums

        result = [-1]*n
        window_size = 2*k+1

        if n < window_size:
            return result

        window_sum = sum(nums[:window_size])
        result[k] = window_sum//window_size

        for i in range(k+1, n-k):
            window_sum = window_sum - nums[i-k-1] + nums[i+k]
            result[i] = window_sum//window_size

        return result

