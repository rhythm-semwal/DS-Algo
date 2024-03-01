from collections import defaultdict


class Solution1:
    def minSteps(self, s: str, t: str) -> int:
        hash_map1, hash_map2 = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            hash_map1[s[i]] += 1
            hash_map2[t[i]] += 1

        print(hash_map1)
        print(hash_map2)

        result = 0

        for key, value in hash_map2.items():
            if key not in hash_map1:
                result += value
            else:
                if value > hash_map1[key]:
                    result += value - hash_map1[key]

        return result


class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        hash_map1, hash_map2 = [0]*26, [0]*26

        for i in range(len(s)):
            hash_map1[ord(s[i]) - ord('a')] += 1
            hash_map2[ord(t[i]) - ord('a')] += 1

        print(hash_map1)
        print(hash_map2)

        result = 0

        for i in range(26):
            result += abs(hash_map1[i] - hash_map2[i])

        return result // 2 # this we are doing because we are also counting the s string array while iterating


s = "leetcode"
t = "practice"
s = "bab"
t = "aba"
s = "gctcxyuluxjuxnsvmomavutrrfb"
t = "qijrjrhqqjxjtprybrzpyfyqtzf"
print(Solution2().minSteps(s, t))

