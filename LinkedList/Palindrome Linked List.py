# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        current = head
        while prev:
            if prev.val != current.val:
                return False
            prev = prev.next
            current = current.next

        return True
