from collections import defaultdict
from typing import List


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            hash_map[sorted_word].append(word)

        return list(hash_map.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for each in strs:
            sorted_strs.append("".join(sorted(each)))

        hash_dict = dict()
        for index, value in enumerate(sorted_strs):
            if value not in hash_dict:
                hash_dict[value] = [index]
            else:
                hash_dict[value].append(index)

        result = []

        for key, value in hash_dict.items():
            temp = []
            for each in value:
                temp.append(strs[each])

            result.append(temp)

        return result


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution1().groupAnagrams(strs))
