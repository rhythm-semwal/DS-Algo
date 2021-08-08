class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        sorted_list = [''.join(sorted(ele)) for ele in A]
        print(sorted_list)

        words_dict = dict()
        result_list = list()

        for index, value in enumerate(sorted_list):
            if value in words_dict:
                words_dict[value].append(index+1)
            else:
                words_dict[value] = [index+1]

        for key, value in words_dict.items():
            result_list.append(value)

        print(result_list)


if __name__ == "__main__":
    # A = ["cat", "dog", "god", "tca"]
    A = ["rat", "tar", "art"]
    Solution().anagrams(A)
