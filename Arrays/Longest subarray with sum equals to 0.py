class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        start, end = -1, -1
        max_subarray_length = 0
        current_sum = 0
        sum_dict = {0: -1}

        for index, value in enumerate(A):
            current_sum += value

            if current_sum in sum_dict:
                if max_subarray_length < index-sum_dict[current_sum]:
                    max_subarray_length = index - sum_dict[current_sum]
                    start = sum_dict[current_sum]+1
                    end = index
            else:
                sum_dict[current_sum] = index

        return A[start:end+1] if max_subarray_length else []


A = [1 ,2 ,-2 ,4 ,-4]
print(Solution().lszero(A))
