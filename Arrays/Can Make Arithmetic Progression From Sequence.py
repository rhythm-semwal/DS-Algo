# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
class Solution2:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        '''
        TC = O(N*logN)
        SC = O(N), since the sorting algo in python uses TimSort and it takes an additional space of O(N)
        '''
        if len(arr) == 2:
            return True

        ascending_array = arr.sort()

        i, j = 1, 2
        diff = arr[1] - arr[0]

        while j < len(arr):
            if arr[j] - arr[i] != diff:
                return False

            i += 1
            j += 1

        return True
      

class Solution2:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        '''
        Refer to the above Leetcode link for detailed explaination of the Algo
        TC = O(N)
        SC = O(N)
        '''
        min_value, max_value = min(arr), max(arr)
        n = len(arr)

        # If we have diff = 0, it means that all the numbers in arr are equal, and we can return true directly.
        if max_value - min_value == 0:
            return True
        
        # If max_value - min_value is not divisible by n - 1, it means arr can't form an arithmetic sequence, return false

        if (max_value - min_value) % (n-1):
            return False
        
        diff = (max_value - min_value) // (n-1)

        hash_set = set()

        for i in arr:
            if (i - min_value) % diff:
                return False
            
            hash_set.add(i)
        
        return len(hash_set) == n


