# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    # approach 1
    # def inorder_traversal(self, root, result):
    #     if root is None:
    #         return result
    #     self.inorder_traversal(root.left, result)
    #     result.append(root.val)
    #     self.inorder_traversal(root.right, result)
    #
    #     return result
    #
    # def kthsmallest(self, A, B):
    #     result = self.inorder_traversal(A, [])
    #     return result[B-1]

    # approach 2
    def kthsmallest(self, A, B):
        stack = []
        current = A

        # this condition because if we reach the leaf node then current will become none and come out of loop
        # hence we have to check for both stack and current node
        while stack or current:
            if current:
                stack.append(current)
                current = current.left

            else:
                current = stack.pop()
                B -= 1
                if B == 0:
                    return current.val

                current = current.right

        return None

    # approach 3
    def kthsmallest3(self, A, B):
        level_order = []
        queue = []
        queue.append(A)

        while queue:
            for i in range(len(queue)):
                current = queue.pop(0)
                level_order.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        # print(level_order)
        level_order.sort()
        return level_order[B - 1]


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(Solution().kthsmallest(root, 1))
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(7)