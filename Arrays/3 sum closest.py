class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # TC = O(N^2)
    # SC = O(1)
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        ans = float('inf')
        result = 0
        for i in range(n - 2):

            if i == 0 or A[i] != A[i - 1]:
                left, right = i + 1, n - 1

                while left < right:
                    current_sum = A[i] + A[left] + A[right]

                    if current_sum == B:
                        result = B
                        return result
                    else:
                        diff = abs(current_sum - B)
                        if diff < ans:
                            ans = diff
                            result = current_sum


                    if current_sum > B:
                        right -= 1

                    else:
                        left += 1

        print(result)


A = [ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ]
B = -1

# A = [-1, 2, 1, -4]
# B = -2
print(Solution().threeSumClosest(A, B))
