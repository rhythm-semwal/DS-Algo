class Solution1:
    # TC = O(N**2)
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        s_arr = list(s)
        print(s_arr)

        i = 0
        while i+1 < len(s_arr):
            if (s_arr[i].lower() == s_arr[i+1].lower()) and (ord(s_arr[i]) != ord(s_arr[i+1])):
                del s_arr[i]
                del s_arr[i]

                i = 0
            else:
                i += 1

        print(s_arr)
        return "".join(s_arr)


class Solution:
    # TC = O(N)
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s

        stack = []

        for ch in s:
            if stack and (ch.lower() == stack[-1].lower()) and (ord(ch) != ord(stack[-1])):
                stack.pop()
            else:
                stack.append(ch)

        return "".join(s_arr)


# s = "leEeetcode"
s = 'abBAcC'
print(Solution().makeGood(s))
