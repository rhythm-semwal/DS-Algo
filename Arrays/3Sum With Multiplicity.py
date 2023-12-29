import collections
import itertools
from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        There are 3 cases for i + j + k == target, in which i, j, k are 3 elements from input A:

i, j, k are all equal; That is, i == j && j == k, assume there are cnt is in A, then we have C(cnt, 3) = cnt * (cnt - 1) * (cnt - 2) / 6 possible combinations;
i == j, but k is different from them; assume there are cnt is in A, then we have C(cnt, 2) = cnt * (cnt - 1) / 2 possible combinations of i and j, and times the frequency of j, cnt3, then we have cnt * (cnt - 1) / 2 * cnt3;
i, j, k are all distinct; we just choose each element from cnt is, cnt2 js, and cnt3 ks, respectively; There are cnt * cnt2 * cnt3 combinations.
        """
        c = collections.Counter(arr)
        res = 0

        for i in c:
            for j in c:
                k = target - i - j
                if i == j == k:
                    res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
                elif i == j != k:
                    res += c[i] * (c[i] - 1) // 2 * c[k]
                elif i < j < k:
                    res += c[i] * c[j] * c[k]
        return res % (10 ** 9 + 7)


arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(Solution().threeSumMulti(arr, target))