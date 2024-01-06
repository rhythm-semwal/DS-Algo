class Solution:
    def nextGreaterElement(self, n: int) -> int:

        if n == 0:
            return -1

        nums = list(str(n))
        i = len(nums)-1

        # find the first non increasing sequence from the right
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        # this is the number to be replaced as it is smaller
        # than any other element on the right of it
        i -= 1

        if i < 0:
            return -1

        temp = len(nums)-1

        # look for the min largest number greater than nums[i]
        # and swap it and sort the rest
        while temp > i:
            if nums[i] < nums[temp]:
                break

            temp -= 1
        nums[i], nums[temp] = nums[temp], nums[i]

        # sort rest of the stuff from [i+1, ln-1]
        nums[i+1:] = sorted(nums[i+1:])

        res = int("".join(nums))

        return res if (n < res <= (2 ** 31 - 1)) else -1


n = 21
print(Solution().nextGreaterElement(n))
