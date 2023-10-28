from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        hash_map = defaultdict(int)

        for i in range(len(s)-9):
            substr = s[i:i+10]

            hash_map[substr] += 1

        result = []
        for key, value in hash_map.items():
            if value > 1:
                result.append(key)

        return result


s = "AAAAAAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences(s))
