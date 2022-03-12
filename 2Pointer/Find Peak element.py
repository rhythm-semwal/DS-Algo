from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start+end)//2

            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid-1]:
                end = mid-1
            else:
                start = mid+1
        
        return end

if __name__ == '__main__':
    nums=  [1,2]
    print(Solution().findPeakElement(nums))