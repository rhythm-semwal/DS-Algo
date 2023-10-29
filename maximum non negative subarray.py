import sys

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = 0
        temp_sum = 0
        start, end = 0, 0
        final_start, final_end = -1, -1

        for index, element in enumerate(A):
            if element >= 0:
                temp_sum += element

                if temp_sum > max_sum or (temp_sum == max_sum and end-start > final_end-final_start):
                    max_sum = temp_sum
                    final_start = start
                    final_end = end

            else:
                temp_sum = 0
                start = index+1

            end = index+1

        if final_start == -1 and final_end == -1:
            return []

        return A[final_start:final_end+1]


if __name__ == "__main__":
    # arr = [1,2,3,4,-10]
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # arr = [-163, -20]
    # arr = [1, 2, 5, -7, 2, 3]
    # arr = [10, -1, 2, 3, -4, 100]
    # arr = [0, 0, -1, 0]
    arr = [ -1, -1, -1, -1, -1 ]
    # arr = [ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ]
    print(Solution().maxset(arr))
