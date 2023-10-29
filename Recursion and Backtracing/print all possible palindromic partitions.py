class Solution:
    def is_palindrome(self, word, start, end):
        while start <= end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True

    def allPalPartUtil(self, string, start, end, result, ds):
        if start >= len(string):
            temp = ds.copy()
            result.append(temp)
            return result

        for i in range(start, end+1):
            if self.is_palindrome(string, start, i):
                ds.append(string[start:i+1])
                self.allPalPartUtil(string, start+1, end, result, ds)
                ds.pop()

    def allPalPartitions(self, string: str):
        n = len(string)

        result = []
        self.allPalPartUtil(string, 0, n-1, result, [])
        print(result)


string = "nitin"
Solution().allPalPartitions(string)
