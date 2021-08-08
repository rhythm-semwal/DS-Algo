class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        # approach 1
        # start, end = 0, 0
        # n = len(A)
        # result = list()
        # max_length = -1
        # left_pointer, right_pointer = 0, 0
        # while end < n:
        #     if A[end] == 0:
        #         B -= 1
        #
        #     if B < 0:
        #         length = end-start
        #         if length > max_length:
        #             max_length = length
        #             left_pointer, right_pointer = start, end-1
        #
        #         if A[start] == 0:
        #             B += 1
        #         start += 1
        #     end += 1
        #
        # length = end - start
        # if length > max_length:
        #     max_length = length
        #     left_pointer, right_pointer = start, end - 1
        #
        # for i in range(left_pointer, right_pointer+1):
        #     result.append(i)
        #
        # return result

        # approach 2
        left = 0
        zero_count = 0
        window = 0
        left_index = 0
        result = []
        for right in range(len(A)):
            if A[right] == 0:
                zero_count += 1

            while zero_count > B:
                if A[left] == 0:
                    zero_count -= 1

                left += 1

            if right-left+1 > window:
                window = right-left+1
                left_index = left

        for i in range(left_index, left_index+window+1):
            result.append(i)

        return result
