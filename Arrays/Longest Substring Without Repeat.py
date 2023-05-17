class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = dict()

        start, end = 0, 0
        result = 0

        while end < len(s):
            if s[end] not in hash_map or hash_map[s[end]] == 0:
                hash_map[s[end]] = 1
                result = max(result, end-start+1)
                end += 1
            else:
                while hash_map[s[end]] > 0:
                    hash_map[s[start]] -= 1
                    start += 1
                # This line is not required as the next time end will be at the same position, and it will check
                # if it's present in the hash_map or not so no need for the below lines
                # hash_map[s[end]] += 1
                # end += 1
        return result

    def lengthOfLongestSubstring1(self, A):
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
