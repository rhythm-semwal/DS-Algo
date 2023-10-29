class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach 1 - using sorting
        s1 = "".join(sorted(s1))  # O(NlogN)
        print(s1)
        k = len(s1)

        for i in range(len(s2)):  # O(N)
            sub = s2[i:i+k]  # O(k)
            sub_str = "".join(sorted(sub))  # O(klogk) * O(k)

            if sub_str == s1:
                return True
        return False

        # approach 2 - using hash map O(N*k)
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)

        for i in range(len(s2)):
            sub_str = s2[i:i+k]
            d2 = Counter(sub_str)

            if d1 == d2:  # O(26)
                return True

        return False

        # approach 3 - similar using hash map but no comparision
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)

        d2 = Counter(s2[:k])

        if d1 == d2:
            return True

        for i in range(len(s2)-k):
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1

            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1

            if d1 == d2:
                return True

        return False


s1 = 'ba'
s2 = 'eidaboooa'
print(Solution().checkInclusion(s1, s2))