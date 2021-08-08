class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_set = set()
        hash_set.add(0)
        current_sum = 0
        for i in range(len(A)):
            current_sum += A[i]

            hash_set.add(current_sum)

        if len(hash_set) == len(A) + 1:
            return 0
        return 1


A = [2,  2, 1, 1]
print(Solution().solve(A))