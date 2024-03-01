# # solution 1
# # TC = O(N)
# # SC = O(1)
# # using cycle detection
"""
move slow by 1 and fast by 2. then the point they meet is the entrance of cycle
then start slow from 0 and fast from the intersection point and increment both by 1 . the point where they meet is the
answer
"""


class Solution1:
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


class Solution2:
    def findDuplicate(self, nums) -> int:
        for num in nums:
            index = abs(num)

            if nums[index] < 0:
                return index

            nums[index] *= -1

        return len(nums)


class Solution3:
    # TC = O(N)
    # SC = O(N)
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
                continue
            hash_map[nums[i]] = 1

        for i in range(n):
            if hash_map[nums[i]] > 1:
                return nums[i]


class Solution4:
    # TC = O(N)
    # SC = O(N)
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        hash_set = set()
        for i in range(n):
            if nums[i] in hash_set:
                return nums[i]
            hash_set.add(nums[i])


nums = [3,1,3,4,2]
Solution2().findDuplicate(nums)
