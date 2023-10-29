class Solution:
    """
    @param A: a array
    @return: is it monotonous
    """
    def isMonotonic(self, A):
        # Write your code here.
        # An array is monotonic if it is either monotone increasing or monotone decreasing.
        return (all(A[i] <= A[i+1] for i in range(len(A)-1)) or all(A[i] >= A[i+1] for i in range(len(A)-1)))