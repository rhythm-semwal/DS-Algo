from typing import List


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        # approach 1
        # return len(set(A))

        # approach 2
        start, end = 0, len(A)-1

        while start < end:
            while start != end and A[start] == A[start+1]:
                count -= 1
                start += 1
            
            while start != end and A[end] == A[end-1]:
                count -= 1
                end -= 1
            
            left += 1
        
        return count



