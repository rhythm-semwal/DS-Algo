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
    # approach 1
    def constructTree(self, preorder, inorder):
        if not inorder:
            return None

        inorder_index = inorder.index(preorder.pop())
        root = TreeNode(inorder[inorder_index])

        root.left = self.constructTree(preorder, inorder[:inorder_index])
        root.right = self.constructTree(preorder, inorder[inorder_index+1:])

        return root

    def buildTree(self, A, B):
        # A = preorder
        # B = inorder
        A.reverse()
        return self.constructTree(A, B)


    # approach 2
    # def constructTree(self, preorder, inorder, stop):
    #     if not inorder or inorder[-1] == stop:
    #         return None
    #
    #     root_val = preorder.pop()
    #     root = TreeNode(root_val)
    #     root.left = self.constructTree(preorder, inorder, root_val)
    #     inorder.pop()
    #     root.right = self.constructTree(preorder, inorder, stop)
    #
    #     return root
    # def buildTree(self, A, B):
    #     # A = preorder
    #     # B = inorder
    #     A.reverse()
    #     B.reverse()
    #     return self.constructTree(A, B, None)

    def level_order_traversal(self, head):
        if head is None:
            return None

        result = []
        queue = []
        queue.append(head)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                print(node.val)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        print(result)


A = [1, 6, 2, 3]
B = [6, 1, 3, 2]
res = Solution().buildTree(A, B)
Solution().level_order_traversal(res)
