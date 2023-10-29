class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0

        for i in s:
            c ^= ord(i)
        for i in t:
            c ^= ord(i)
        return chr(c)
        
    def findTheDifference1(self, s: str, t: str) -> str:
        arr1 = [0]*26
        arr2 = [0]*26


        for i in s:
            arr1[ord(i) - ord('a')] += 1
        
        for i in t:
            arr2[ord(i) - ord('a')] += 1
        
        for i in t:
            if arr1[ord(i) - ord('a')] == 0:
                return i
            elif arr1[ord(i) - ord('a')] != arr2[ord(i) - ord('a')]:
                return i
