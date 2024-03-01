from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]

        for a in arr:
            if len(set(a)) < len(a):
                continue

            a = set(a)

            # we use this temp list because previously we were updating directly in the dp list, but then we were
            # comparing the current iteration also. SO to not do that created a temp list
            temp = list()
            for each in dp:
                if a & each:
                    continue
                temp.append(a | each)
            dp.extend(temp)

        return max(len(a) for a in dp)


arr = ["un","iq","ue"]
# arr = ["cha","r","act","ers"]
# arr = ["abcdefghijklmnopqrstuvwxyz"]
print(Solution().maxLength(arr))
