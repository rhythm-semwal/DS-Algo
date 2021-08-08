# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if A is None:
            return -1

        result = []
        queue = []

        queue.append(A)

        # approach 1
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         result.append(node.val)
        #
        #         if node.val != -1:
        #             if node.left:
        #                 queue.append(node.left)
        #             if node.left is None:
        #                 new_node = TreeNode(-1)
        #                 node.left = new_node
        #                 queue.append(new_node)
        #             if node.right:
        #                 queue.append(node.right)
        #             if node.right is None:
        #                 new_node = TreeNode(-1)
        #                 node.right = new_node
        #                 queue.append(new_node)
        #
        #         else:
        #             continue
        while queue:
            current = queue.pop(0)
            if current is None:
                result.append(-1)
                continue
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)

        print(result)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
Solution().solve(root)
