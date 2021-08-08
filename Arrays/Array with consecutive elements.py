class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # approach 1
        import sys
        min_element = sys.maxsize
        for i in A:
            min_element = min(min_element, i)

        for i in range(len(A)):
            A[i] -= min_element

        hash_map = {}
        for i in A:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        for i in A:
            if 0 <= i <= len(A)-1:
                if hash_map[i] > 1:
                    return False
            else:
                return False

        return True

        # approach 2
        A.sort()
        i, j = 0, 1
        while j < len(A):
            if A[j]-A[i] != 1:
                return False
            i += 1
            j += 1
        return True



input = [4, 3, 2, 6]
print(Solution().solve(input))