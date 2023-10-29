class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xor = 0
        hash_map = dict()
        count = 0

        for i in range(len(A)):
            xor ^= A[i]

            if xor ^ B in hash_map:
                count += hash_map[xor^B]

            if xor == B:
                count += 1

            if xor in hash_map:
                hash_map[xor] += 1
            else:
                hash_map[xor] = 1

        print(count)


A = [4, 2, 2, 6, 4]
B = 6
A = [5, 6, 7, 8, 9]
B = 5

Solution().solve(A, B)
