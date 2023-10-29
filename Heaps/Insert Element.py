class Solution:
    def parent(self, i):
        return (i-1)//2

    def solve(self, A, value):

        A.append(value)
        index = len(A)-1
        # percolate up because since heap property was already there in all nodes so now just compare with parent
        while index > 0 and A[self.parent(index)] < A[index]:
            A[index], A[self.parent(index)] = A[self.parent(index)], A[index]
            index = self.parent(index)

        print(A)


A = [20, 9, 8, 7, 6, 5, 4, 3]
Solution().solve(A, 12)
