import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        hash_map = dict()   # key = sum, value=first occurrence index position

        temp_sum = 0
        cum_sum = list()
        for index, value in enumerate(A):
            if value == 0:
                temp_sum -= 1
            else:
                temp_sum += 1

            cum_sum.append(temp_sum)

        ans = -1
        # result_dict = {0:0}
        result_dict = dict()
        for index, value in enumerate(cum_sum):
            if value in result_dict:
                if index-result_dict[value] > ans:
                    ans = index-result_dict[value]
            elif value == 0:
                if index > ans:
                    ans = index+1
            else:
                result_dict[value] = index

        print(ans)


if __name__ == "__main__":
    # A = [1,1,1,0]
    # A = [1, 0, 1, 0, 1]
    # A = [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1 ]
    # A = [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0,
    #     0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
    A =  [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0,
        1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1]

    Solution().solve(A)
