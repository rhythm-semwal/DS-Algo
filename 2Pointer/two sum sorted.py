from typing import List


class Solution:
    def hasTwoSumZero(self, A: List[int]) -> bool:
        s, e = 0, len(A)-1

        while s < e:
            sum = A[s] + A[e]
            if sum == 0:
                return True
            elif sum > 0:
                e -= 1
            else:
                s += 1
        
        return False

if __name__ == '__main__':
    A = [-3, 1, 3, 4]
    print(Solution().hasTwoSumZero(A))
