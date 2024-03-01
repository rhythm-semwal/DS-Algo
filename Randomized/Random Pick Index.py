import random
from typing import List
from collections import defaultdict


class Solution:
    def __init__(self, nums: List[int]):
        self.hash_map = defaultdict(list)
        for i in range(len(nums)):
            self.hash_map[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.hash_map[target])


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3, 3])
print(obj.pick(3))
print(obj.pick(1))
print(obj.pick(3))
print(obj.pick(2))
print(obj.pick(3))