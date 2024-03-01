from collections import defaultdict, Counter


class Solution1:
    """
    Count the number of characters in each string
    Compare the counts for each character
    If the counts of the characters don't match, add the difference of the counts to answer
    """
    def minSteps(self, s: str, t: str) -> int:
        counter1 = Counter(s)
        counter2 = Counter(t)

        return sum(abs(counter1[ch] - counter2[ch]) for ch in 'abcdefghijklmnopqrstuvwxyz')


class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        hash_map1, hash_map2 = defaultdict(int), defaultdict(int)

        for ch in s:
            hash_map1[ch] += 1

        for ch in t:
            hash_map2[ch] += 1

        print(hash_map1)
        print(hash_map2)

        result = 0

        for key, value in hash_map1.items():
            if key not in hash_map2:
                result += value
            else:
                result += abs(value - hash_map2[key])

        for key, value in hash_map2.items():
            if key not in hash_map1:
                result += value

        return result


s = "leetcode"
t = "coats"

# s = "cotxazilut"
# t = "nahrrmcchxwrieqqdwdpneitkxgnt"
print(Solution1().minSteps(s, t))
