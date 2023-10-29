# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None



class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        hash_set = set()

        queue = []
        queue.append(A)
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                hash_set.add(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        queue = []
        queue.append(B)
        result = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.val in hash_set:
                    result += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        print(result)


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.right = TreeNode(3)
root.right.right = TreeNode(15)

root1 = TreeNode(5)
root1.left = TreeNode(2)
root1.right = TreeNode(8)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(15)
Solution().solve(root, root1)

