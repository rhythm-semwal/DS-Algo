class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if len(A) == 1:
            return 1

        freq_hash_set = set()

        i, j = 0, 0
        ans = 0

        while j < len(A):
            if A[j] not in freq_hash_set:
                freq_hash_set.add(A[j])
                ans = max(ans, len(freq_hash_set))
                j += 1
            else:
                freq_hash_set.remove(A[i])
                i += 1

        return ans
