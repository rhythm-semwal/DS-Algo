class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        current_sum = 0
        left_index, right_index = -1, -1
        left, right = 0, 0
        max_sum = 0

        for i in range(len(A)):
            if A[i] >= 0:
                current_sum += A[i]

                if current_sum > max_sum or (current_sum == max_sum and right-left > right_index-left_index):
                    max_sum = current_sum
                    left_index = left
                    right_index = right
            else:
                current_sum = 0
                left = i+1
            right = i+1

        return A[left_index:right_index+1]

A = [1, 2, 5, -7, 2, 3]
print(Solution().maxset(A))