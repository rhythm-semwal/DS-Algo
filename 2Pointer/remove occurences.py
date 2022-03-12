from typing import List


class Solution:
    def removeOccurences(self, A: List[int], k: int) -> int:
        count = 0
        for i in range(len(A)):
            if A[i] == k:
                count += 1
        
        return len(A) - count


if __name__ == '__main__':
    A =  [1, 4, 2, 6, 2, 6, 9, 4]
    k = 4
    print(Solution().removeOccurences(A, k))