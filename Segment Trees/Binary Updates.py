class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    """
    Approach 1:
    use arrays and find th 1 every time
    Approach 2:
    create a segment tree and perform binary search every time. TC = O(q*logN(binary search)*logN(segment tree))
    Approach 3:
    create segment tree and check if the y would lie in the left half or right half. TC = O(q*logN)

    """
    def build(self, node, start, end, arr, tree):
        if start == end:
            tree[node] = 1
            return

        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        self.build(left_child, start, mid, arr, tree)
        self.build(right_child, mid+1, end, arr, tree)

        tree[node] = tree[left_child] + tree[right_child]
        return

    def update(self, node, start, end, tree, index, arr):
        if start == end:
            tree[node] = 0
            arr[index] = 0
            return

        mid = (start+end)//2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        if index <= mid:
            self.update(left_child, start, mid, tree, index, arr)
        else:
            self.update(right_child, mid+1, end, tree, index, arr)

        tree[node] = tree[left_child] + tree[right_child]
        return

    def query(self, node, start, end, tree, y):
        if y > tree[node]:
            return -2

        if start == end:
            return start

        mid = (start+end)//2
        left_child = 2*node+1
        right_child = 2*node+2

        # checking if the number of 1 in the left child is > than y, then ans will lie in the left half
        if tree[left_child] >= y:
            return self.query(left_child, start, mid, tree, y)
        # else number of 1 in the left child is < than y, then ans will lie in the right half and we have to search for
        # y - no of 1 in the left half
        else:
            return self.query(right_child, mid+1, end, tree, y-tree[left_child])

    def solve(self, A, B):
        arr = [1]*A

        tree = [0]*(4*A)

        self.build(0, 0, A-1, arr, tree)
        # print(tree)
        result = list()
        for query in B:
            if query[0] == 0:
                self.update(0, 0, A-1, tree, query[1]-1, arr)
                # print("after update = ", tree)
            else:
                ans = (self.query(0, 0, A-1, tree, query[1]))+1
                result.append(ans)

        return result


A = 4
B = [ [1, 2],
       [0, 2],
       [1, 4] ]
A = 5
B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ]
print(Solution().solve(A, B))
