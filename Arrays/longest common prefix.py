class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        import sys
        min_length_string = sys.maxsize
        for i in range(len(A)):
            if len(A[i]) < min_length_string:
                min_length_string = len(A[i])
                smallest_string = A[i]
                index = i

        A.pop(index)
        # print(min_length_string)
        # print(smallest_string)
        # print(A)
        i = 0
        count = 0
        while i < min_length_string:
            for each in A:
                if each[i] != smallest_string[i]:
                    return smallest_string[:count]
            count += 1
            i += 1
        return smallest_string[:count+1]


A = ['axdc', 'ax', 'axbc']
# A = [ "abcd", "aze" ]
print(Solution().longestCommonPrefix(A))

