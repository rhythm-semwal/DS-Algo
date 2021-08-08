# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers

    # approach 2
    """
    T.C = O(N)
    S.C = O(N)
    """
    def inorder_traversal(self, node, result):
        if node is None:
            return result

        self.inorder_traversal(node.left, result)
        result.append(node.val)
        self.inorder_traversal(node.right, result)
        return result

    def recoverTree(self, A):
        result = self.inorder_traversal(A, [])
        # this will be O(logN) since the array is almost sorted
        sorted_result = sorted(result)

        for i in range(len(result)):
            if result[i] != sorted_result[i]:
                return [sorted_result[i], result[i]]


root = TreeNode(76)
root.left = TreeNode(77)
root.right = TreeNode(5)
print(Solution().recoverTree(root))
ans = [(1,2)]
print(ans[0][1])
