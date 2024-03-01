from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = defaultdict(int)

        for i in arr:
            hash_map[i] += 1

        hash_set = set(hash_map.values())

        return len(hash_map) == len(hash_set)

        # OR
        #
        # hash_set = set()
        #
        # for _, value in hash_map.items():
        #     if value in hash_set:
        #         return False
        #     hash_set.add(value)
        #
        # return True
