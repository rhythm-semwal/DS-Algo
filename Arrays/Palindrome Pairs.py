class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def solve(self, A):
        palindromes = []
        word_to_index = dict()

        for index, value in enumerate(A):
            word_to_index[value] = index

        for index, word in enumerate(A):
            for first_right in range(len(word)+1):
                left, right = word[:first_right], word[first_right:]
                rev_left, rev_right = left[::-1], right[::-1]

                if first_right != 0 and left == rev_left and rev_right in word_to_index and word_to_index[rev_right] != index:
                    palindromes.append([word_to_index[rev_right], index])

                if right == rev_right and rev_left in word_to_index and word_to_index[rev_left] != index:
                    palindromes.append([index, word_to_index[rev_left]])
        print(palindromes)


A = ["abcd", "dcba", "lls", "s", "sssll"]
Solution().solve(A)
