class Solution:
    def calculate_z_array(self, input):
        z = [0]*len(input)
        left, right = 0, 0

        for i in range(1, len(input)):
            # calculating z value for each char. No box is found
            if i > right:
                left, right = i, i
                while right < len(input) and input[right] == input[right-left]:
                    right += 1

                z[i] = right-left
                right -= 1

            else:
                # we are operating inside the box
                k = i - left
                # if it i inside the boundary then simply copy the value
                if z[k] < right-i+1:
                    z[i] = z[k]
                else:
                    # if it is outside the boundary then result will be remaining letters + other matches if any
                    # the start of the boundary
                    left = i
                    while right < len(input) and input[right] == input[right-left]:
                        right += 1

                    z[i] = right-left
                    right -= 1
        print(z)


# A = 'abaxabab'
# A = "abababab"
A = "abcaabcaab"
Solution().calculate_z_array(A)

