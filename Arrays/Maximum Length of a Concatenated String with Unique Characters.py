from typing import List


class Solution1:
    def maxLength(self, arr) -> int:
        dp = [set()]

        for a in arr:
            # if duplicate elements are present then ignore the word
            if len(set(a)) < len(a):
                continue

            a = set(a)

            for each in dp:
                # if there are duplicate words then do not consider it
                if a & each:
                    continue
                # append both words here if no duplicates are there
                dp.append(a | each)

        return max(len(a) for a in dp)


class Solution2:
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
