"""
class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None
"""


# @param root: ListNode
# @return ListNode
def mergeTwoLists(node1, node2):
    dummy_node = ListNode(0)
    current = dummy_node

    while node1 is not None and node2 is not None:
        if node1.val <= node2.val:
            current.down = node1
            current = current.down
            node1 = node1.down
        else:
            current.down = node2
            current = current.down
            node2 = node2.down

    if node1 is not None:
        current.down = node1
    if node2 is not None:
        current.down = node2

    return dummy_node.down


def flatten(root):
    """
    algo:
    merge the last 2 nodes and then continuosly merge the nodes
    """
    if root is None or root.right is None:
        return root

    root.right = flatten(root.right)

    root = mergeTwoLists(root, root.right)

    return root