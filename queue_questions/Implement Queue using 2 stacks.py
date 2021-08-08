# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Push TC = O(1)
Pop TC = O(1) amortized
"""

class Queue_Two_Stacks():
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                element = self.stack1.pop()
                self.stack2.append(element)

        self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                element = self.stack1.pop()
                self.stack2.append(element)

        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2


def read_command():
    parts = input().strip().split(' ')
    cmd = int(parts[0])

    if len(parts) == 1:
        return (cmd, None)
    else:
        arg = int(parts[1])
        return (cmd, arg)


if __name__ == "__main__":
    query = int(input())
    obj = Queue_Two_Stacks()
    for i in range(query):
        command, arg = read_command()
        if command == 1:
            obj.enqueue(arg)
        elif command == 2:
            obj.dequeue()
        else:
            print(obj.print())
