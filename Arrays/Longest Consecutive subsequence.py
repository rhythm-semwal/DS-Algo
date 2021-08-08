class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        # approach 1 - sorting
        # T.C = O(N+NlogN) - worst case
        # S.C = O(1)
        A = list(A)
        if len(A) == 1:
            return 1

        A.sort()
        longest_sequence = 1
        current = 1
        for i in range(len(A) - 1):
            if A[i] != A[i+1]:
                if A[i]+1 == A[i+1]:
                    current += 1
                else:
                    longest_sequence = max(longest_sequence, current)
                    current = 1

        return max(current, longest_sequence)

        # approach 2 - using hashing
        # T.C = O(N+N**2) - worst case
        # S.C = O(N)
        A = list(A)

        if len(A) == 1:
            return 1
        hash_set = set(A)
        longest_sequence = 1
        current = 1

        for i in range(len(A)):
            if A[i] - 1 not in hash_set:
                increment_by = 1
                while True:
                    if A[i] + increment_by in hash_set:
                        current += 1
                        increment_by += 1
                    else:
                        longest_sequence = max(longest_sequence, current)
                        current = 1
                        break

        return max(longest_sequence, current)
