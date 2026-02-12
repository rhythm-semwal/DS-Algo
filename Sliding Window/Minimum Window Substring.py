# https://leetcode.com/problems/minimum-window-substring/description/

# TC = O(S+T)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target_count = Counter(t)
        target = len(target_count)
        formed = 0

        start, end = 0,  0
        window_count = defaultdict(int)
        min_length = float("inf")
        min_left = 0

        while end < len(s):
            window_count[s[end]] += 1

            if s[end] in target_count and window_count[s[end]] == target_count[s[end]]:
                formed += 1

            while formed == target and start <= end:
                if end-start+1 < min_length:
                    min_length = end - start + 1
                    min_left = start

                window_count[s[start]] -= 1
                if s[start] in target_count and window_count[s[start]] < target_count[s[start]]:
                    formed -= 1
                start += 1
            end += 1

        return "" if min_length == float("inf") else s[min_left: min_left + min_length]
