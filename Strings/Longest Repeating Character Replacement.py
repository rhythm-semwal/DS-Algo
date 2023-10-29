class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, start = 0, 0
        n = len(s)

        from collections import defaultdict
        freq_dict = defaultdict(int)
        for end in range(n):
            freq_dict[s[end]] += 1

            while (end-start+1) - max(freq_dict.values()) > k:
                freq_dict[s[start]] -= 1
                start += 1

            longest = max(longest, end-start+1)

        return longest

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))