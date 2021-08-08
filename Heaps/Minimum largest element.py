class Solution:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, index):
        return (index-1)//2

    def insert(self, input):
        if self.size == 0:
            self.heap.append(input)
            self.size += 1
            return
        else:
            self.heap.append(input)
            self.size += 1

            current = self.size-1
            # print(self.heap[current][0])
            # print(self.heap[self.parent(current)][0])
            while self.heap[current][0] < self.heap[self.parent(current)][0]:
                self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
                current = self.parent(current)

    def min_heapify(self, index, n):
        left_child = 2*index+1
        right_child = 2*index+2

        if left_child < n and self.heap[left_child] < self.heap[index]:
            smallest = left_child
        else:
            smallest = index

        if right_child < n and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            return self.min_heapify(smallest, n)

    def delete(self):
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        self.size = len(self.heap)-1
        self.min_heapify(self.size-1, self.size)

    def solve(self, A, B):
        current_state = A[:]

        n = len(A)

        for i in range(n):
            self.insert((A[i]*2, i))
            print(self.heap)

        print(self.heap)

        while B > 0:
            element, index = self.heap[0][0], self.heap[0][1]
            current_state[index] = element
            self.heap.pop(0)
            self.insert((A[index]+element, index))
            print("after inserting new = ", self.heap)
            B -= 1
        # print(self.heap)



A = [5,1,4,2]
B = 5
Solution().solve(A, B)
