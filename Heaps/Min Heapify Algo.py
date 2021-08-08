class Solution:
    def min_heapify(self, A, n, index):
        left_child = 2*index + 1
        right_child = 2*index + 2

        if left_child < n and A[left_child] < A[index]:
            smallest = left_child
        else:
            smallest = index

        if right_child < n and A[right_child] < A[smallest]:
            smallest = right_child

        if smallest != index:
            A[index], A[smallest] = A[smallest], A[index]
            return self.min_heapify(A, n, smallest)

    def solve(self, A, i):
        print("Before heapify = ", A)
        n = len(A)
        self.min_heapify(A, n, i)
        print("After heapify = ", A)


A = [14, 10, 8, 7, 9, 3, 2, 4, 6, 1]
Solution().solve(A, 0)
