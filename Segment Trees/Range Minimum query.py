import sys


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def build(self, node, start, end, arr, tree):
        if start == end:
            tree[node] = arr[start]
            return

        mid = (start+end)//2
        left_child = 2*node + 1
        right_child = 2 * node + 2

        self.build(left_child, start, mid, arr, tree)
        self.build(right_child, mid+1, end, arr, tree)
        tree[node] = min(tree[left_child], tree[right_child])
        return tree

    def update(self, node, start, end, index, new_value, arr, tree):

        if start == end:
            arr[index] = new_value
            tree[node] = new_value
            return

        if index < start or index > end:
            return

        mid = (start+end)//2
        left_child = (2 * node + 1)
        right_child = (2 * node + 2)
        if index <= mid:
            self.update(left_child, start, mid, index, new_value, arr, tree)
        else:
            self.update(right_child, mid+1, end, index, new_value, arr, tree)

        tree[node] = min(tree[left_child], tree[right_child])
        return tree

    def find_min(self, node, start, end, left, right, arr, tree):
        if end < left or right < start:
            return sys.maxsize
        if left <= start and right >= end:
            return tree[node]

        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        return min(self.find_min(left_child, start, mid, left, right, arr, tree),
                   self.find_min(right_child, mid+1, end, left, right, arr, tree))

    def solve(self, A, B):
        from math import ceil, log2
        n = len(A)
        height = int(ceil(log2(n)))
        max_size = 2 * pow(2, height)
        # max_size = 2 * (int(2 ** height))
        tree = [0] *(4*n)
        self.build(0, 0, n - 1, A, tree)

        result = []
        for each in B:
            x, y, z = each[0], each[1], each[2]
            if x == 0:
                self.update(0, 0, n-1, y-1, z, A, tree)
            else:
                result.append(self.find_min(0, 0, n-1, y-1, z-1, A, tree))

        return result