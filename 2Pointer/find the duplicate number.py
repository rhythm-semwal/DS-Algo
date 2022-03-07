class Solution:
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

if __name__ == '__main__':
    nums = [3,1,3,4,2]
    print(Solution().findDuplicate(nums))