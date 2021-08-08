class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        hash_set = set(A)
        count_dict = dict()
        if len(hash_set) == 1 or len(hash_set) > 2:
            return "LOSE"
        else:
            for each in A:
                if each in count_dict:
                    count_dict[each] += 1
                else:
                    count_dict[each] = 1
            harry = 0
            for values in count_dict.values():
                tom = values
                if tom == harry:
                    return "WIN"
                harry = tom
        return "LOSE"


if __name__ == "__main__":
    # A = [1, 1, 2, 2, 3]
    A = [1,1,2,2]
    # A = [ 20, 20, 30, 30, 20, 20, 20, 30, 30, 20, 20, 30, 30, 30, 30, 20, 30, 30, 30, 30, 20, 20, 30, 30, 30, 20, 30, 20, 30, 20, 30, 20, 20, 20, 30, 20, 20, 20, 30, 30 ]
    print(Solution().solve(A))

