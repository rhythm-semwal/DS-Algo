class Solution:
    def parent(self, i):
        return (i-1)//2

    def solve(self, A, index, value):
        if value > A[index]:
            return -1

        # decrease key is possible in min heap
        A[index] = value
        # percolate up because since heap property was already there in all nodes so now just compare with parent
        while index > 0 and A[self.parent(index)] > A[index]:
            A[index], A[self.parent(index)] = A[self.parent(index)], A[index]
            index = self.parent(index)

        print(A)

    def max_heapify(self, A, i, n):
        left_child = 2*i+1
        right_child = 2*i+2

        if left_child < n and A[left_child] > A[i]:
            largest = left_child
        else:
            largest = i

        if right_child < n and A[right_child] > A[largest]:
            largest = right_child

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest, n)

    def decrease_key_max_heap(self, A, index, value):
        n = len(A)

        print("before heapify = ", A)
        start = n//2-1
        for i in range(start, -1, -1):
            self.max_heapify(A, i, n)

        print("after heapify = ", A)

        A[index] = value
        self.max_heapify(A, index, n)
        print("after decreasing key = ", A)



A = [1,4,5,6,3,9,7,8,2]
# for min heap decrease key
# Solution().solve(A, 1, 0)

# for max heap decrease key
Solution().decrease_key_max_heap(A, 1, 0)
