from collections import defaultdict


class Solution1:
    def frequencySort(self, s: str) -> str:
        # Time Complexity: O(nlogk), where k is the number of distinct character.
        # Space Complexity: O(n)
        hash_dict = defaultdict(int)

        for ch in s:
            hash_dict[ch] += 1

        from heapq import heapify, heappop

        heap = [(-value, key) for key, value in hash_dict.items()]
        heapify(heap)

        result = []
        while heap:
            value, key = heappop(heap)
            result.append(key * (-value))

        return "".join(result)


class Solution2:
    # TC = O(NlogN)
    def frequencySort(self, s: str) -> str:
        hash_dict = defaultdict(int)

        for ch in s:
            hash_dict[ch] += 1

        # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

        sorted_hash_dict = {k: v for k, v in sorted(hash_dict.items(), key=lambda x: x[1], reverse=True)}
        result = ''

        for key, value in sorted_hash_dict.items():
            result += key * value

        return result


s = "tree"
# s = "cccaaa"
# s = "Aabb"
print(Solution1().frequencySort(s))

