# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, l1, l2):
        dummy_node = ListNode(0)
        current = dummy_node

        node1, node2 = l1, l2
        carry = 0

        while node1 and node2:
            temp_sum = node1.val + node2.val + carry
            carry = temp_sum // 10
            current.next = ListNode(temp_sum % 10)

            current = current.next
            node1 = node1.next
            node2 = node2.next

        if node1:
            while node1:
                temp_sum = node1.val + carry
                carry = temp_sum // 10
                current.next = ListNode(temp_sum % 10)
                current = current.next
                node1 = node1.next

        if node2:
            while node2:
                temp_sum = node2.val + carry
                carry = temp_sum // 10
                current.next = ListNode(temp_sum % 10)
                current = current.next
                node2 = node2.next

        if carry > 0:
            current.next = ListNode(carry)
            current = current.next

        return dummy_node.next

    def addTwoNumbers1(self, A, B):
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
