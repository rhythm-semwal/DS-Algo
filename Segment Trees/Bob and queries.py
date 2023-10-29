class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def update(self, node, start, end, tree, index, qtype):
        if start == end:
            if qtype == 1:
                tree[node] += 1
                return tree[node]
            else:
                tree[node] = max(0, tree[node]-1)
                return tree[node]
        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        if index <= mid:
            self.update(left_child, start, mid, tree, index, qtype)
        else:
            self.update(right_child, mid + 1, end, tree, index, qtype)

        tree[node] = tree[left_child] + tree[right_child]
        return

    def query(self, node, start, end, tree, left, right):
        if right < start or end < left:
            return 0

        if left <= start and right >= end:
            return tree[node]

        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        return self.query(left_child, start, mid, tree, left, right) + self.query(
            right_child, mid+1, end, tree, left, right)

    def solve(self, A, B):
        tree = [0]*(4*A)
        result = list()
        for query in B:
            qtype = query[0]
            if qtype != 3:
                index = query[1]-1
                self.update(0, 0, A - 1, tree, index, qtype)
            else:
                left = query[1]-1
                right = query[2]-1
                result.append(self.query(0, 0, A - 1, tree, left, right))

        return result
