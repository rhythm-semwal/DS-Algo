class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):

        cumulative_sum = 0
        cumulative_sum_array = list()
        left_pointer, right_pointer = -1, -1

        for i in A:
            cumulative_sum += i
            cumulative_sum_array.append(cumulative_sum)

        # print(cumulative_sum_array)
        position_dict = dict()
        position_dict[0] = -1
        ans = -1
        result_list = list()

        for index, value in enumerate(cumulative_sum_array):
            if value in position_dict:
                if index - position_dict[value] > ans:
                    ans = index - position_dict[value]
                    left_pointer = position_dict[value]+1
                    right_pointer = index
            else:
                position_dict[value] = index

        print(A[left_pointer:right_pointer+1])


if __name__ == "__main__":
    # A = [1, 2, -2, 4, -4]
    # A = [4, 2, -6]
    # A = [2, 3, -1, -4, 3, -1, 6, -2, 1, -4, 2, -3, 1]
    A = [ -1, 1, 1, -1, -1, 1, 1, -1 ]
    Solution().lszero(A)
