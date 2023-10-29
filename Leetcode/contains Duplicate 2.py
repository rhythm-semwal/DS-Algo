class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()

        for index, value in enumerate(nums):
            if value not in hash_map:
                hash_map[value] = index + 1
            else:
                if abs(hash_map[value] - (index + 1)) <= k:
                    return True
                hash_map[value] = index + 1
        return False