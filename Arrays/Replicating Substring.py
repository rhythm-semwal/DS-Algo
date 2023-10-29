class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(B)
        if n % A != 0:
            return -1

        char_freq_hash_map = dict()

        for i in range(n):
            if B[i] not in char_freq_hash_map:
                char_freq_hash_map[B[i]] = 1
            else:
                char_freq_hash_map[B[i]] += 1

        for value in char_freq_hash_map.values():
            if value % A != 0:
                return -1
        return 1
