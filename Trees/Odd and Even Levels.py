# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        # approach 1
        if A is None:
            return 0

        return A.val - self.solve(A.left) - self.solve(A.right)

        # appraoch 2 using level order traversal
        # if A is None:
        #     return None

        # queue = []
        # odd_count = 0
        # even_count = 0

        # queue.append((A, 1))

        # while queue:
        #     current = queue.pop(0)

        #     level = current[1]
        #     node = current[0]
        #     if level % 2 == 0:
        #         even_count += node.val
        #     else:
        #         odd_count += node.val

        #     if node.left:
        #         queue.append((node.left, level + 1))
        #     if node.right:
        #         queue.append((node.right, level + 1))

        # return odd_count - even_count
