class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def hotel_occurences(self, A):
        freq_dict = dict()
        result = list()

        for each in A:
            if each in freq_dict:
                freq_dict[each] += 1
            else:
                freq_dict[each] = 1

        for each in A:
            if freq_dict[each] > 1:
                freq_dict[each] -= 1
            else:
                result.append(each)

        return result


if __name__ == "__main__":
    # A = [1, 2, 3, 2, 5, 3, 2, 4]
    A = [1, 2, 3, 2, 3, 2, 5, 4]
    # A = [1,2,3,4]
    print(Solution().hotel_occurences(A))
