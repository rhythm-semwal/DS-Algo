# https://leetcode.com/problems/merge-k-sorted-lists

#TC = O(Nlogk) where k == lists.length and N is the number of nodes
# SC = O(logk)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two_list(l1, l2):
            current = dummy = ListNode(0)

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                
                current = current.next
            
            current.next = l1 or l2
            return dummy.next

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(merge_two_list(l1, l2))
            
            lists = merged_list

        return lists[0]
