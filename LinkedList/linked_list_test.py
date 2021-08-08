class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # @staticmethod
    # def insert_at_nth_position(prev_node, new_data):
    #     if prev_node is None:
    #         return
    #
    #     new_node = Node(new_data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node

    def insert_at_nth_position(self, new_data, pos):
        # creating a new node
        new_node = Node(new_data)

        if pos == 1:  # this means the new node will be the head node
            new_node.next = self.head
            self.head = new_node
            return

        # if new node is to be inserted at some other position
        temp = self.head  # get the head element

        # this loop will give us the node just before the position where new node is to be inserted
        for i in range(0, pos-2):
            temp = temp.next
            if temp is None:
                return

        if temp is None:
            print("here")
            raise IndexError("Position is not valid")

        new_node.next = temp.next
        temp.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next


def print_linked_list(head):
    temp = head

    while temp is not None:
        print(temp.data, end='->')
        temp = temp.next


def isPalindrome(head):
    # code here
    if head is None:
        return None

    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    temp = slow
    # slow.next = None
    current = head

    prev = None
    while temp is not None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next

    while prev is not None:
        if current.data != prev.data:
            return 0
        current = current.next
        prev = prev.next

    return 1


def removeNthFromEnd(head, n):
    # write your code here
    if head.next is None and n == 1:
        head = None
        return head

    ll_length = 0

    current = head

    while current:
        ll_length += 1
        current = current.next

    if ll_length <= n:
        head = head.next
        return head

    temp = head
    for i in range(ll_length-n-1):
        print("here")
        temp = temp.next

    temp.next = temp.next.next
    return head


llist = LinkedList()
llist.insert_at_start(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)
# llist.insert_at_end(1)
# llist.insert_at_end(1)
llist.print_linked_list()
print()
result = removeNthFromEnd(llist.head, 2)
print_linked_list(result)


