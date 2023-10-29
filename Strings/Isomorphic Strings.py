from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_mapST, hash_mapTS = dict(), dict()

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in hash_mapST and hash_mapST[c1] != c2) or (c2 in hash_mapTS and hash_mapTS[c2] != c1):
                return False

            hash_mapST[c1] = c2
            hash_mapTS[c2] = c1

        return True

# s = "egg"
# t = "add"

s = "bbbaaaba"
t = "aaabbbba"

print(Solution().isIsomorphic(s, t))