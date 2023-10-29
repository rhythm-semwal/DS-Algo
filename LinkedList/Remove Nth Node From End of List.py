# Definition for singly-linked list.
from typing import Optional


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert node
def insert(root, item):
    temp = ListNode(item)

    if root is None:
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None and n == 1:
            head = None
            return head

        length = 0

        current = head
        while current is not None:
            length += 1
            current = current.next

        if length <= n:
            temp = head
            head = temp.next
            return head

        delete_node = head
        for i in range(length-n-1):
            delete_node = delete_node.next

        delete_node.next = delete_node.next.next
        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    # arr = [1]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
    new_root = Solution().removeNthFromEnd(root, 4)
    display(new_root)
