# # solution 1
# # TC = O(N)
# # SC = O(1)
# # using cycle detection
"""
move slow by 1 and fast by 2. then the point they meet is the entrance of cycle
then start slow from 0 and fast from the intersection point and increment both by 1 . the point where they meet is the
answer
"""
class Solution:
    def findDuplicate(self, nums) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                return abs(nums[i])

    def findDuplicate(self, nums) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# # solution 2
# # TC = O(N)
# # SC = O(N)
# # using hash_map
# class Solution:
#     def findDuplicate(self, nums) -> int:
#         n = len(nums)
#         hash_map = dict()
#         for i in range(n):
#             if nums[i] in hash_map:
#                 hash_map[nums[i]] += 1
#                 continue
#             hash_map[nums[i]] = 1
#
#         for i in range(n):
#             if hash_map[nums[i]] > 1:
#                 return nums[i]
#
# # solution 2
# # TC = O(N)
# # SC = O(N)
# # using hash set
#
#
# class Solution:
#     def findDuplicate(self, nums) -> int:
#         n = len(nums)
#         hash_set = set()
#         for i in range(n):
#             if nums[i] in hash_set:
#                 return nums[i]
#             hash_set.add(nums[i])
#

class Solution:
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        print(slow)
        print(fast)

nums = [3,1,3,4,2]
Solution().findDuplicate(nums)
