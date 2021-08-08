class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):

        cumulative_sum = 0
        cumulative_sum_set = set()
        cumulative_sum_set.add(0)

        for element in A:
            if element == 0:
                return True
            cumulative_sum += element
            cumulative_sum_set.add(cumulative_sum)

        if len(cumulative_sum_set) == len(A)+1:
            return False
        return True



if __name__ == "__main__":
    # A = [1, 2, -2, 4, -4]
    # A = [4, 2, -6]
    # A = [2, 3, -1, -4, 3, -1, 6, -2, 1, -4, 2, -3, 1]
    A = [ -1, 1, 1, -1, -1, 1, 1, -1 ]
    Solution().lszero(A)
