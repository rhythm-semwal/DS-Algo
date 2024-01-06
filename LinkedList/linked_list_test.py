import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to insert node
def insert(root, item):
    temp = ListNode(item)

    if root is None:
        root = temp
    else:
        ptr = root
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = temp

    return root


def display(root):
    while (root != None):
        print(root.val, end="->")
        root = root.next
    print()


def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])

    return root


class Solution1:
    def deleteMiddle(self, head):
        if head.next is None:
            return None

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            if fast is not None and fast.next is not None:
                slow = slow.next

        slow.next = slow.next.next
        return head


class Solution2:
    def deleteMiddle(self, head):
        if head.next is None:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        current = dummy_node
        node1, node2 = l1, l2

        carry_sum = 0
        while node1 and node2:
            current_sum = node1.val + node2.val + carry_sum
            current.next = ListNode(current_sum%10)
            carry_sum = current_sum // 10

            current = current.next
            node1 = node1.next
            node2 = node2.next

        while node1:
            current_sum = node1.val + carry_sum
            current.next = ListNode(current_sum % 10)
            carry_sum = current_sum // 10

            current = current.next
            node1 = node1.next

        while node2:
            current_sum = node2.val + carry_sum
            current.next = ListNode(current_sum % 10)
            carry_sum = current_sum // 10

            current = current.next
            node2 = node2.next

        if carry_sum > 0:
            current.next = ListNode(carry_sum)

        return dummy_node.next




if __name__ == "__main__":
    arr = [5,2,13,3,8,5,4]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
    result = Solution1().removeNodes(root)
    display(result)
