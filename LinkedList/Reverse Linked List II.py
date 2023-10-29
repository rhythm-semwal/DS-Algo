class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


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
    def reverseBetween(self, head, left: int, right: int):
        prev = None
        current = head

        while left > 1:
            prev = current
            current = current.next
            left -= 1
            right -= 1

        left_side = prev
        right_side = current

        while right > 0:
            next = current.next
            current.next = prev
            prev = current
            current = next
            right -= 1

        if left_side is not None:
            left_side.next = prev
        else:
            head = prev

        right_side.next = current
        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    # arr = [1]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
    Solution().reverseBetween(root, 2, 4)