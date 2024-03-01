# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    # TC = O(N)
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        ll_list = []
        current = head

        while current:
            ll_list.append(current.val)
            current = current.next

        def bst(low, high):
            if low <= high:
                mid = (low + high) // 2

                node = TreeNode(ll_list[mid])
                node.left = bst(low, mid - 1)
                node.right = bst(mid + 1, high)

                return node

        return bst(0, len(ll_list) - 1)


class Solution1:
    """
    TC = O(N * Log(N)) ->
    N is for finding middle element
    log(N) - This binary tree construction process occurs for each level of the recursion,
    and there are log(n) levels in total (where "n" is the number of nodes in the linked list).
    """
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if head.next is None:
            return TreeNode(head.val)

        middle = self.get_middle(head)
        root = TreeNode(middle.val)

        # we are first forming the right subtree because in LL we have access to the next element of middle node
        root.right = self.sortedListToBST(middle.next)
        middle.next = None

        root.left = self.sortedListToBST(head)

        return root

    def get_middle(self, head):
        slow, fast, prev = head, head, None

        while fast and fast.next:
            prev = slow  # this variable will point to the element before the middle element of LL
            slow = slow.next
            fast = fast.next.next

        if prev:  # In this condition since slow will be the middle element, so make prev.next as Null in BST
            prev.next = None

        return slow


