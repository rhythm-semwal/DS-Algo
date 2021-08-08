class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    # another approach is to sort the array and then implement 2 pointer approach
    def twoSum(self, A, B):
        index_dict = dict()
        # use hashset in case you just need to return true/false
        for index, value in enumerate(A):
             if B - value in index_dict:
                 return [index_dict[B-value]+1, index+1]
             elif value not in index_dict:
                 index_dict[value] = index
        return []

if __name__ == "__main__":
    # nums = [3, 2, 4]
    # target = 6
    # nums = [2, 7, 11, 15]
    # target = 9
    # nums = [3, 3]
    # target = 6
    nums = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
    target = -3
    print(Solution().twoSum(nums, target))

