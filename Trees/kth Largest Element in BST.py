# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'

class Solution:
    def solve(self, node, result):
        if node is None:
            return result

        self.solve(node.left, result)
        result.append(node.data)
        self.solve(node.right, result)

        return result

    def kthLargest(self, root, k):
        if root is None:
            return

        result = self.solve(root, [])

        return result[-k]
