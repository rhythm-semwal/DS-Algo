from ast import List
from operator import le

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):
            p1, p2 = i+1, len(nums)-1
        
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while p1 < p2:
                current_sum = nums[i] + nums[p1] + nums[p2]
                
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum-target) < abs(closest_sum-target):
                    closest_sum = current_sum
                
                if current_sum > target:
                    p2 -= 1
                else:
                    p1 += 1
        
        return closest_sum


if __name__ == "__main__":
    nums = [0,0,0]
    target = 1
    print(Solution().threeSumClosest(nums, target))
