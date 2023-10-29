class Solution:
    def groupAnagrams(self, strs):
        hash_map = dict()
        for str in strs:
            new_str = list(str)
            new_str.sort()
            key = "".join(new_str)
            if key not in hash_map:
                hash_map[key] = [str]
            else:
                hash_map[key].append(str)

        result = []
        for key, value in hash_map.items():
            result.append(value)
        return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
