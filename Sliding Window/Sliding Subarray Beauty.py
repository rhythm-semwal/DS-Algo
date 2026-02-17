# https://leetcode.com/problems/sliding-subarray-beauty
# Time: O(n × 50) = O(n) - constant time per window! Since -50 <= nums[i] <= 50 
# Space: O(50) = O(1) - constant space
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        frequency = [0]*50

        for i in range(k):
            if nums[i] < 0:
                frequency[-nums[i]-1] += 1

        result.append(self.get_xth_smallest_number(frequency, x))

        for i in range(k, len(nums)):
            # Remove the leftmost element from the frequency array
            if nums[i-k] < 0:
                frequency[-nums[i-k]-1] -= 1

            # add the new or the rightmost element in the frequency array
            if nums[i] < 0:
                frequency[-nums[i]-1] += 1

            result.append(self.get_xth_smallest_number(frequency, x))

        return result

    def get_xth_smallest_number(self, frequency, x):
        count = 0
        for i in range(49, -1, -1):
            count += frequency[i]

            if count >= x:
                return -(i+1)

        return 0
        
