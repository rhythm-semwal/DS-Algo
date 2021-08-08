from collections import OrderedDict


class Solution:

    # Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter1(self,s):
        # code here
        hash_map = OrderedDict()

        for chr in s:
            if chr in hash_map:
                hash_map[chr] += 1
            else:
                hash_map[chr] = 1

        for key, value in hash_map.items():
            if value == 1:
                return key

        return -1

    def nonrepeatingCharacter2(self, s):
        count_array = [-1] * 256

        for i in range(len(s)):
            if count_array[ord(s[i])] == -1:
                count_array[ord(s[i])] = i
            else:
                count_array[ord(s[i])] = -2

        result = float('inf')
        for i in range(256):

            if count_array[i] >= 0:
                result = min(result, count_array[i])

        return -1 if result == float('inf') else s[result]

