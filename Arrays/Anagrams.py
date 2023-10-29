class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers

    def anagrams(self, A):
        hash_map = dict()
        result = list()
        for i in range(len(A)):
            sorted_word = "".join(sorted(A[i]))
            if sorted_word not in hash_map:
                hash_map[sorted_word] = [i+1]
            else:
                hash_map[sorted_word].append(i+1)
        for values in hash_map.values():
            result.append(values)

        print(result)


A = ['cat', 'dog', 'god','tca']
Solution().anagrams(A)


