import sys
class Solution:
    def build(self, node, start, end, arr, tree):
        if start == end:
            tree[node] = arr[start]
            # return arr[start]
            return
        mid = (start+end)//2
        left_child = 2*node + 1
        right_child = 2 * node + 2

        self.build(left_child, start, mid, arr, tree)
        self.build(right_child, mid+1, end, arr, tree)

        # tree[node] = min(tree[left_child], tree[right_child])
        tree[node] = tree[left_child] + tree[right_child]
        # return tree[node]
        return tree

    def update(self, node, start, end, tree, index, new_val, arr):
        """
        There can be 3 scenarios for update.
        1) when index becomes equal to start and end
        2) if index is invalid
        3) if index lies in the range

        the leaf nodes will be updated.
        after updating the leaf nodes we have to update the segment tree
        """
        if start == end:
            arr[index] = new_val
            tree[node] = new_val
            return

        mid = (start + end) // 2
        left_child = (2 * node + 1)
        right_child = (2 * node + 2)
        if index <= mid:
            self.update(left_child, start, mid, index, new_val, arr, tree)
        else:
            self.update(right_child, mid + 1, end, index, new_val, arr, tree)

        tree[node] = min(tree[left_child], tree[right_child])
        return tree

    def query(self, node, start, end, left, right, tree):
        # non overlapping condition. means the ans does not exist in that node
        if end < left or right < start:
            return sys.maxsize
        # we know the ans for some segment of the range out of the larger range given
        if left <= start and right >= end:
            return tree[node]

    def main(self, A):
        from math import ceil, log2
        n = len(A)
        height = int(ceil(log2(n)))
        print(height)
        max_size = 2 * (int(2 ** height))
        tree = [0] * max_size
        self.build(0, 0, n - 1, A, tree)
        print(tree)
        result = []
        for each in B:
            x, y, z = each[0], each[1], each[2]
            if x == 0:
                self.update(0, 0, n - 1, tree, y-1, z, A)
            else:
                result.append(self.query(0, 0, n - 1, y-1, z-1, tree))

        print(result)


A = [1,3,5]
B = [
        [1, 2, 4],
        [0, 1, 2],
        [1, 1, 4]
]
# A = [1, 4, 1, 5]
# B = [
#         [1, 1, 3],
#         [0, 1, 5],
#         [1, 1, 2]
#      ]
Solution().main(A)