class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        encoded_string = []
        for s in strs:
            len_s = str(len(s))
            encoded_string.append(len_s)
            encoded_string.append('#')
            encoded_string.append(s)

        return "".join(encoded_string)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        result = []
        i = 0
        while i < len(str):
            j = str.find('#', i)
            print(j)
            len_substring = int(str[i:j])
            result.append(s[j+1:j+1+len_substring])
            i = j+1+len_substring

        print(result)


s = ["lint","code","love","you"]
result = Solution().encode(s)
print("encoded = ", result)
print(Solution().decode(result))
