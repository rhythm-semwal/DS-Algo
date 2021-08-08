class Solution:
    def max_heapify(self, A, index, heap_size):
        left_child = 2*index+1
        right_child = 2*index+2

        if left_child < heap_size and A[left_child] > A[index]:
            largest = left_child
        else:
            largest = index

        if right_child < heap_size and A[right_child] > A[largest]:
            largest = right_child

        if largest != index:
            A[index], A[largest] = A[largest], A[index]
            self.max_heapify(A, largest, heap_size)

    def solve(self, A):
        heap_size = len(A)

        max_element = A[0]
        A[0] = A[heap_size-1]
        heap_size -= 1

        self.max_heapify(A, 0, heap_size)

        print(max_element)
        print(A)


A = [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
Solution().solve(A)
Solution().solve(A)
Solution().solve(A)
