# @type of s: string
# @return type: integer
class Solution:
    def last_non_repeating_char(self, s: str) -> int:
        # write your awesome code here
        hash_map = dict()

        for i in range(len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1

        print(hash_map)

        for i in range(len(s)-1, -1, -1):
            if hash_map[s[i]] == 1:
                return s[i]
        return -1

s = "GeeksForGeeks"
print(Solution().last_non_repeating_char(s))

