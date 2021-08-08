"""
Here we are only interested in the last value of this lps array because it shows us the largest suffix of the
reversed string that matches the prefix of the original string i.e these many characters already satisfy the
palindrome property. Finally minimum number of character needed to make the string a palindrome is
length of the input string minus last entry of our lps array
"""

    
class Solution:
    # @param A : string
    # @return an integer
    def calculate_LPS_array(self, text):
        n = len(text)
        lps_array = [0]*n

        i, j = 0, 1
        while j < n:
            if text[i] == text[j]:
                i += 1
                lps_array[j] = i
                j += 1
            else:
                if i == 0:
                    lps_array[j] = 0
                    j += 1
                else:
                    i = lps_array[i-1]

        return lps_array

    def solve(self, A):
        reverse_A = A[::-1]

        concat_string = A+'$'+reverse_A
        lps_array = self.calculate_LPS_array(concat_string)

        return len(A) - lps_array[-1]

# A = "bb"
A = "abc"
print(Solution().solve(A))
