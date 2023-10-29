# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not A:
            return None

        inorder_index = A.index(B.pop())
        root = TreeNode(A[inorder_index])

        root.right = self.buildTree(A[inorder_index + 1:], B)
        root.left = self.buildTree(A[:inorder_index], B)

        return root

    def level_order_traversal(self, root):
        if root is None:
            return None

        result = []
        queue = []
        queue.append(root)
        # current = root

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        print(result)


A = [6, 1, 3, 2]
B = [6, 3, 2, 1]
res = Solution().buildTree(A, B)
Solution().level_order_traversal(res)