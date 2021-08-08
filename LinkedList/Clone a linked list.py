"""
class ListNode:
    def __init__(x):
        self.val = x
        self.next = None
        self.random = None
"""


def clonelist(A):
    current = A

    # create a copy of the nodes. With original nodes next pointing to the copy of the nodes
    while current is not None:
        new_node = ListNode(current.val)
        temp = current.next
        current.next = new_node
        new_node.next = temp
        current = new_node.next

    # now for the copy nodes point the random pointers to the same nodes as in the original list
    current = A
    while current is not None:
        if current.random is not None:
            current.next.random = current.random.next
        current = current.next.next

    # now change the pointers


    # approach 1
    # dummy_node = ListNode(0)
    # current = dummy_node
    #
    # iter = A
    # while iter is not None:
    #     front = iter.next.next
    #     current.next = iter.next
    #     iter.next = front
    #     current = current.next
    #     iter = iter.next
    #
    # return dummy_node.next

    # approach 2
    dummy_node = ListNode(0)
    cloned_list = dummy_node

    current = A

    while current is not None:
        next = current.next.next
        cloned_list.next = current.next
        current = next
        cloned_list = cloned_list.next

    return dummy_node.next
