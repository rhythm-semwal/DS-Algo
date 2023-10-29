class Solution:

    def max_heapify(self, A, index, n):
        left_child = 2*index+1
        right_child = 2*index+2

        if left_child < n and A[left_child] > A[index]:
            largest = left_child
        else:
            largest = index

        if right_child < n and A[right_child] > A[largest]:
            largest = right_child

        if largest != index:
            A[index], A[largest] = A[largest], A[index]
            self.max_heapify(A, largest, n)

    def solve(self, A):
        n = len(A)

        print("Before building heap = ", A)
        start = n//2-1
        for i in range(start, -1, -1):
            self.max_heapify(A, i, n)
        print("after building heap = ", A)


A = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
Solution().solve(A)
