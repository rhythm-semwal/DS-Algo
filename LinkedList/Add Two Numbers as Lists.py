# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        # code version 2
        node1, node2 = A, B
        dummy_node = ListNode(0)
        current = dummy_node

        carry = 0
        while node1 is not None or node2 is not None or carry == 1:
            current_sum = 0
            if node1 is not None:
                current_sum += node1.val
                node1 = node1.next
            if node2 is not None:
                current_sum += node2.val
                node2 = node2.next

            current_sum += carry
            carry = current_sum // 10
            new_node = ListNode(current_sum % 10)
            current.next = new_node
            current = new_node

        return dummy_node.next

        # code version 1
        # node1, node2 = A, B
        #
        # dummy_node = ListNode(0)
        # current = dummy_node
        #
        # carry = 0
        # while node1 is not None and node2 is not None:
        #     current_sum = 0
        #     current_sum += node1.val
        #     current_sum += node2.val
        #     current_sum += carry
        #     carry = current_sum // 10
        #     new_node = ListNode(current_sum % 10)
        #     current.next = new_node
        #     current = new_node
        #
        #     node1 = node1.next
        #     node2 = node2.next
        #
        # while node1:
        #     current_sum = 0
        #     current_sum += node1.val
        #     current_sum += carry
        #     new_node = ListNode(current_sum % 10)
        #     carry = current_sum // 10
        #     current.next = new_node
        #     current = new_node
        #     node1 = node1.next
        #
        # while node2:
        #     current_sum = 0
        #     current_sum += node2.val
        #     current_sum += carry
        #     new_node = ListNode(current_sum % 10)
        #     carry = current_sum // 10
        #     current.next = new_node
        #     current = new_node
        #     node2 = node2.next
        #
        # if carry:
        #     new_node = ListNode(carry)
        #     current.next = new_node
        #     # carry -= carry
        #
        # return dummy_node.next