class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for i in range(len(nums)):
            hash_map[nums[i]] += 1

        hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
        return list(hash_map.keys())[:k]