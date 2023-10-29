class Solution1:
    """
    T.C = O(n^3)
    """
    def sumOddLengthSubarrays(self, arr) -> int:
        total_sum = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                total_sum += sum(arr[i:j+1])

        return total_sum


class Solution2:
    """
    T.C = O(n^2)
    """
    def sumOddLengthSubarrays(self, arr) -> int:
        total_sum = 0
        for i in range(len(arr)):
            running_sum = 0
            for j in range(i, len(arr)):
                running_sum += arr[j]
                # when the index is odd then add the running sum to the total_sum else
                # continue to add in the running sum
                if (j-i+1) % 2 == 1:
                    total_sum += running_sum

        return total_sum


class Solution3:
    """
    TC = O(N)
    https://leetcode.com/problems/sum-of-all-odd-length-subarrays/solutions/854184/java-c-python-o-n-time-o-1-space/
    """
    def sumOddLengthSubarrays(self, arr) -> int:
        total_sum = 0
        for index, value in enumerate(arr):
            # total no of times each index will occur in a subarray when we consider the subarray of all lengths.
            k = (index+1) * (len(arr) - index)
            # depending on the length of the arr
            if len(arr) % 2 == 0:
                total_sum += (k // 2) * value
            else:
                total_sum += ((k + 1) // 2) * value

        return total_sum


arr = [1,4,2,5,3]
print(Solution3().sumOddLengthSubarrays(arr))