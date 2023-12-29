from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr)-1

        while high-low >= k:
            if abs(arr[low]-x) > abs(arr[high]-x):
                low += 1
            else:
                high -= 1

        result = []
        for i in range(low, high+1):
            result.append(arr[i])

        return result

class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        If the starting element is found, [start, start+k] elements can be returned.

Given that k << len(arr); we can always use the hi index as length(arr)-k and lo=0

For cases where the target is off the extremes we'll end up with k elements.
But for the cases where the target is within exactly or sparsely equal to one of the elements in the array; we need to
shuffle lo and hi accordingly

Consider binary search paradigm:

if arr[mid] is farther from target than arr[mid+k] which is k places ahead of mid then we need to pull lo
to mid with 1 offset; otherwise we can pull hi at mid.
at the end we'll end up with a value contained by lo's index which can be the starting index of our solution
        """
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low+high)//2
            if x - arr[mid] > arr[mid+k] - x:
                low = mid+1
            else:
                high = mid

        return arr[low:low+k]


arr = [1,2,3,4,5]
k = 4
x = 3

arr = [1]
k = 1
x = 1
#
# arr = [-2,-1,1,2,3,4,5]
# k = 7
# x = 3
#
arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
print(Solution().findClosestElements(arr, k, x))


