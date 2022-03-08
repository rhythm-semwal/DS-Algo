from collections import defaultdict
from operator import le


class Solution:
    #SC = O
    def firstUniqChar(self, s: str) -> int:
        hash_map = defaultdict(int)

        for i in range(len(s)):
            hash_map[s[i]] += 1

        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1

if __name__ == '__main__':
    print(Solution().firstUniqChar('aabb'))