class Solution:
    """
    Time complexity : O(n)

Although the time complexity appears to be quadratic due to the while loop nested
within the for loop, closer inspection reveals it to be linear.
Because the while loop is reached only when currentNum marks the beginning of a sequence
(i.e. currentNum-1 is not present in nums), the while loop can only run for n iterations throughout
the entire runtime of the algorithm.
This means that despite looking like O(n⋅n) complexity,
 the nested loops actually run in O(n + n) = O(n) time.
 All other computations occur in constant time, so the overall runtime is linear.
    """
    def get_sequence_length(self, hash_set, num):
        count = 1
        while True:
            num += 1
            if num in hash_set:
                count += 1
            else:
                return count

    def longestConsecutive(self, nums) -> int:

        hash_set = set()
        n = len(nums)
        ans = 0
        if n == 1:
            return 1

        for i in range(n):
            hash_set.add(nums[i])

        for i in range(n):
            if nums[i] - 1 in hash_set:
                continue

            else:
                ans = max(ans, self.get_sequence_length(hash_set, nums[i]))

        return ans


nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))
