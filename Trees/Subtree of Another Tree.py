# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
TC = O(m+n)
SC = O(m+n)
"""


class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def serialise(node):
            if not node:
                serial.append("#")
                return
            # , is important if root = 12 and subroot is 2 then if we don't use , than 2 is present in 2
            # but value does not match
            serial.append(',')
            serial.append(str(node.val))
            serialise(node.left)
            serialise(node.right)

        serial = []
        serialise(root)
        # print(serial)
        root_serial = "".join(serial)
        # print("root_serial = ", root_serial)

        serial = []
        serialise(subRoot)
        # print(serial)
        subRoot_serial = "".join(serial)
        # print("subRoot_serial = ", subRoot_serial)

        return subRoot_serial in root_serial
