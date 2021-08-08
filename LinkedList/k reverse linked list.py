# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if A is None or B == 1:
            return A

        dummy_node = ListNode(0)
        dummy_node.next = A
        """
            prev will be keep a track of the prev element for whom reverse was done
            hence in the start current = prev.next
            current will point to the start of the k node to be reversed and after reversing it will point to the 
            end of the k nodes.
            current.next will point to the next k nodes
        """
        current, next, prev = dummy_node, dummy_node, dummy_node

        length = 0
        temp = A
        while temp is not None:
            length += 1
            temp = temp.next

        while length >= B:
            current = prev.next
            next = current.next

            for i in range(B):
                current.next = next.next
                next.next = prev.next
                prev.next = next
                next = current.next

            prev = current
            length -= B

        return dummy_node.next
