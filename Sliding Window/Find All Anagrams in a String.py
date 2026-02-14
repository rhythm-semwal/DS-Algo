# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window 
# TC = O(N)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        reference_set = Counter(p)
        current_set = defaultdict(int)
        result = []
        start, end = 0, 0
        
        while end < len(s):
            current_set[s[end]] += 1

            if end-start+1 == len(p):
                if current_set == reference_set:
                    result.append(start)
                  
                current_set[s[start]] -= 1
                if current_set[s[start]] == 0:
                    del current_set[s[start]]
                start += 1
            end += 1

        return result
