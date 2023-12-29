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


if __name__ == "__main__":
    arr = [1,3,4,7,1,2,6]
    # arr = [1,2,3,4]
    # arr = [2,1]
    # arr = [1]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
    # Solution1().deleteMiddle(root)
    Solution2().deleteMiddle(root)
    display(root)