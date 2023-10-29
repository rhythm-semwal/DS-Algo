# TC = O(nlogn)
class Solution1:
    def missingNumber(self, nums) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i != nums[i]:
                return i

        return n

# TC = O(n), SC = O(n)
class Solution2:
    def missingNumber(self, nums) -> int:
        nums_set = set(nums)
        current = 0

        while True:
            if current not in nums_set:
                break
            current += 1

        return current

# TC = O(n), SC = O(1)
class Solution3:
    def missingNumber(self, nums) -> int:
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing

class Solution4:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        m = sum(nums)

        return (n*(n+1)//2) - m


nums = [-8,-7,-6]
print(Solution3().missingNumber(nums))
