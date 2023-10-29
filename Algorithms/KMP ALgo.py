class KMP:
    def get_prefix_array(self, pattern, n):
        prefix_arr = [0]*n
        i, j = 0, 1

        while j < n:
            if pattern[i] == pattern[j]:
                i += 1
                prefix_arr[j] = i
                j += 1
            elif i != 0:
                i = prefix_arr[i-1]
            else:
                prefix_arr[j] = 0
                j += 1

        return prefix_arr

    def KMP_string(self, text, pattern):
        a = len(text)
        b = len(pattern)

        prefix_array = self.get_prefix_array(pattern, b)
        print(prefix_array)
        # i pointer for text
        #  j pointer for pattern
        i, j = 0, 0

        while i < a:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            # if j has reached the end of the pattern, this means pattern exist in the text
            if j == b:
                print("pattern found at index = ", i-j)
                j = prefix_array[j-1]

            # check the text against the pattern
            elif i < a and pattern[j] != text[i]:
                if j == 0:
                    i += 1
                else:
                    j = prefix_array[j-1]


String = "AAAAABAAAAAAAC"
Pattern = "AAAAC"
# String = "Welcome to CodeSpeedy"
# Pattern = "Code"
print(KMP().KMP_string(String, Pattern))

