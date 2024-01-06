from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    We reverse the list, and "eat" next elements if value is smaller. Then, we reverse the list again.
    TC = O(N)
    SC = O(N)
    """
    def reverse_ll(self, node):
        prev = None
        current = node

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = self.reverse_ll(head)
        ll = current

        while ll.next:
            if ll.val > ll.next.val:
                ll.next = ll.next.next
            else:
                ll = ll.next

        return self.reverse_ll(current)


class Solution2:
    # add items in stack and then iterate through stack to mark stack top next to be stack popped node
    # TC = O(N)
    # SC = O(N)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            stack.append(head)
            head = head.next

        while len(stack) > 1:
            node = stack.pop()
            stack[-1].next = node

        return stack[-1]