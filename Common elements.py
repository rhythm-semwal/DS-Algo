class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        count_dict = dict()
        result_list = list()

        for i in A:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        print(count_dict)

        for i in B:
            if i in count_dict:
                if count_dict[i] > 0:
                    result_list.append(i)
                    count_dict[i] -= 1

        print(result_list)


if __name__ == "__main__":
    # A = [1, 2, 2, 1]
    # B = [2, 3, 1, 2]

    A = [2, 1, 4, 10]
    B = [3, 6, 2, 10, 10]

    Solution().solve(A, B)
