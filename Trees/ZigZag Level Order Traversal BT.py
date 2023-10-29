# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        # appraoch 2
        """
        use 2 stacks.
        odd stack contains elements at odd level. add elements from right to left and pop from left to right
        even stack contains elements at even level. add elements from left to right and pop from right to left
        """
        if A is None:
            return None

        result = []
        odd_level_stack, even_level_stack = [], []
        odd_level_stack.append(A)
        level = 1
        while odd_level_stack or even_level_stack:
            temp = []
            if level % 2 == 0:
                for i in range(len(even_level_stack)):
                    node = even_level_stack.pop()
                    temp.append(node.val)
                    if node.right:
                        odd_level_stack.append(node.right)
                    if node.left:
                        odd_level_stack.append(node.left)
            else:
                for i in range(len(odd_level_stack)):
                    node = odd_level_stack.pop()
                    temp.append(node.val)
                    if node.left:
                        even_level_stack.append(node.left)
                    if node.right:
                        even_level_stack.append(node.right)

            result.append(temp)
            level += 1

        return result

        # approach 1
        """
        Do normal level order traversal and for even levels reverse the result 
        """
        # if A is None:
        #     return None
        #
        # result = []
        # queue = []
        # queue.append(A)
        # level = 1
        # while queue:
        #     if level % 2 == 0:
        #         flag = True
        #     else:
        #         flag = False
        #     temp = []
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         # odd level
        #         temp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     if flag:
        #         temp.reverse()
        #     result.append(temp)
        #     level += 1
        #
        # return result


root = TreeNode(1)
root.left = TreeNode(6)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left = TreeNode(9)
root.left.right = TreeNode(10)
print(Solution().zigzagLevelOrder(root))
