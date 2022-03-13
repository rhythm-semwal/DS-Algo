from collections import defaultdict
import collections
import heapq
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        print(collections.Counter(arr))
        hp = [(val, key) for key, val in collections.Counter(arr).items()]

        heapq.heapify(hp)
        print(hp)

        while k > 0:
            k -= heapq.heappop(hp)[0]
        return len(hp) + (k < 0) 
        



if __name__ == '__main__':
    arr = [5,5,4]
    k = 1
    print(Solution().findLeastNumOfUniqueInts(arr, k))

