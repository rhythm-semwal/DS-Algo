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

    def insert_at_nth_position(self, new_data, pos):
        new_node = Node(new_data)
        current_node = self.head

        if pos == 1:  # this means the new node will be the head node
            self.head = new_node

        for i in range(pos-2):
            current_node = current_node.next
            if current_node is None:
                return

        if current_node is None:
            print("here")
            raise IndexError("Position is not valid")

        new_node.next = current_node.next
        current_node.next = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        temp = self.head

        if self.head is None:
            self.head = new_node
            return
        while temp.next is not None:
            temp = temp.next
            if temp is None:
                return

        temp.next = new_node

    def print_elements(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.insert_at_start(3)
ll.insert_at_start(4)
ll.insert_at_start(5)
ll.insert_at_end(10)
ll.insert_at_nth_position(15, 3)
