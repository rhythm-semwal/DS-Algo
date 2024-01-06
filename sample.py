# from typing import List
#
#
# class Solution:
#     # TC = O(k * (n - k))
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         answer = []
#         for i in range(len(nums) - 2):
#
#             if i == 0 or nums[i] != nums[i - 1]:
#
#                 left, right = i + 1, len(nums) - 1
#
#                 while left < right:
#                     current_sum = nums[i] + nums[left] + nums[right]
#
#                     if current_sum == 0:
#                         answer.append([nums[i], nums[left], nums[right]])
#
#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         while right > left and nums[right] == nums[right - 1]:
#                             right -= 1
#
#                         left += 1
#                         right -= 1
#
#                     elif current_sum > 0:
#                         right -= 1
#                     else:
#                         left += 1
#
#         return answer
#
#
# nums = [-1,0,1,2,-1,-4]
# print(Solution().threeSum(nums))
import heapq


def sort012(arr, n) :

	# write your code here
    # don't return anything
    zero, first, second = 0, 0, n-1

    while first < second:
        if arr[first] == 0:
            arr[zero], arr[first] = arr[first], arr[zero]
            zero += 1
            first += 1
        elif arr[first] == 1:
            first += 1
        else:
            arr[first], arr[second] = arr[second], arr[first]
            second -= 1

    print(arr)


arr = [0, 1, 2, 2, 1, 0]
sort012(arr, len(arr))
