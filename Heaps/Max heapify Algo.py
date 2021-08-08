class Solution:
    # T.C = O(logN)
    # S.C = O(logN)
    def max_heapify(self, A, n, index):
        left_child = 2*index + 1
        right_child = 2*index + 2

        if left_child < n and A[left_child] > A[index]:
            largest = left_child
        else:
            largest = index

        if right_child < n and A[right_child] > A[largest]:
            largest = right_child

        if largest != index:
            A[index], A[largest] = A[largest], A[index]
            return self.max_heapify(A, n, largest)

    def solve(self, A, i):
        print("Before heapify = ", A)
        n = len(A)
        self.max_heapify(A, n, i)
        print("After heapify = ", A)


A = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6]
Solution().solve(A, 0)
