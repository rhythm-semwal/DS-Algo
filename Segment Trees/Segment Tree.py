class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def build(self, node, arr, tree, start, end):
        if start == end:
            tree[node] = arr[start]
            return
        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        self.build(left_child, arr, tree, start, mid)
        self.build(right_child, arr, tree, mid+1, end)

        tree[node] = tree[left_child] + tree[right_child]
        return tree

    def sum_query(self, node, tree, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and right >= end:
            return tree[node]

        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        return self.sum_query(left_child, tree, start, mid, left, right) + \
               self.sum_query(right_child, tree, mid+1, end, left, right)

    def update_query(self, node, tree, arr, start, end, index, new_value):
        if start == end:
            arr[index] = new_value
            tree[node] = new_value
            return

        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        if index <= mid:
            self.update_query(left_child, tree, arr, start, mid, index, new_value)
        else:
            self.update_query(right_child, tree, arr, mid+1, end, index, new_value)

        tree[node] = tree[left_child]+tree[right_child]
        return tree

    def solve(self, A, B):
        from math import ceil, log2
        n = len(A)
        # height = int(ceil(log2(n)))
        # print(height)
        # max_size = 2 * (int(2 ** height))
        tree = [0] * (4*n)
        self.build(0, A, tree, 0, n - 1)
        result = []
        for each in B:
            if each[0] == 1:
                A.append(each[1])
                n += 1
                tree = [0] * (4 * n)
                self.build(0, A, tree, 0, n-1)
            elif each[0] == 2:
                self.update_query(0, tree, A, 0, n-1, each[1]-1, each[2])
            elif each[0] == 3:
                A.pop(each[1]-1)
                n -= 1
                if n > 0:
                    tree = [0] * (4 * n)
                    self.build(0, A, tree, 0, n - 1)
            elif each[0] == 4:
                ans = self.sum_query(0, tree, 0, n-1, each[1]-1, each[2]-1)
                result.append(ans%1000000007)
            print(result)


# A = [ 4924, 6440, 4982, 1310, 3140 ]
# B = [
#   [4, 4, 4],
#   [1, 2793, 0],
#   [4, 5, 6],
#   [3, 1, 0],
#   [2, 4, 9981],
#   [3, 4, 0],
#   [1, 2629, 0],
#   [3, 1, 0],
#   [1, 2386, 0],
#   [1, 3460, 0],
#   [1, 5585, 0],
#   [4, 1, 1],
#   [3, 6, 0],
#   [1, 6681, 0],
#   [3, 1, 0],
#   [2, 2, 9368],
#   [3, 2, 0],
#   [2, 5, 2971],
#   [1, 7272, 0],
#   [4, 2, 3],
#   [1, 9778, 0],
#   [4, 1, 1],
#   [1, 7155, 0],
#   [2, 3, 4335],
#   [3, 2, 0],
#   [4, 6, 6],
#   [4, 1, 7],
#   [4, 7, 7],
#   [2, 4, 6467],
#   [3, 3, 0],
#   [1, 2701, 0],
#   [2, 3, 3043],
#   [1, 3732, 0],
#   [1, 6815, 0],
#   [2, 3, 6460],
#   [1, 7644, 0],
#   [1, 7234, 0],
#   [4, 2, 4],
#   [3, 9, 0],
#   [1, 9433, 0],
#   [2, 11, 4458],
#   [3, 3, 0],
#   [1, 474, 0],
#   [4, 10, 11],
#   [3, 9, 0],
#   [4, 9, 9],
#   [4, 10, 10],
#   [3, 6, 0],
#   [2, 2, 7920],
#   [2, 3, 8614],
#   [4, 3, 5],
#   [4, 1, 3],
#   [4, 6, 8],
#   [1, 5473, 0],
#   [4, 8, 10],
#   [4, 3, 10],
#   [1, 9682, 0],
#   [4, 9, 11],
#   [4, 4, 8],
#   [4, 5, 11],
#   [1, 9622, 0],
#   [3, 9, 0],
#   [3, 2, 0]
# ]
A = [ 2 ]
B =[
  [3, 1, 0],
  [1, 4, 0],
  [4, 1, 1]
]
Solution().solve(A, B)
