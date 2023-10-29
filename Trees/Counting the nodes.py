# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer

    # approach 1
    def dfs(self, node, max_element):
        if node is None:
            return 0

        count = 0

        if node.val > max_element:
            count = 1

        count += self.dfs(node.left, max(max_element, node.val))
        count += self.dfs(node.right, max(max_element, node.val))
        return count

    def solve(self, A):
        import sys
        max_element = -sys.maxsize
        return self.dfs(A, max_element)

    # approach 2
    def __init__(self):
        self.count = 0

    def dfs(self, node, max_element):
        if node is None:
            return 0

        # global count

        if node.val > max_element:
            self.count += 1

        self.dfs(node.left, max(max_element, node.val))
        self.dfs(node.right, max(max_element, node.val))

    def solve(self, A):
        import sys
        max_element = -sys.maxsize
        self.dfs(A, max_element)
        return self.count
        # if A is None:
        #     return 0

        # count = 0
        # queue = list()
        # queue.append(A)

        # import sys
        # max_element = -sys.maxsize
        # while queue:
        #     node = queue.pop(0)

        #     if node.val > max_element:
        #         count += 1
        #         max_element = node.val

        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        # return count


root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().solve(root))
