class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums_set = set(nums)
        return len(nums_set) != len(nums)


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().containsDuplicate(nums))

