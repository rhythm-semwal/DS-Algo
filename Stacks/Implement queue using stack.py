class MyQueue:

    def __init__(self):
        self.queue = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        popped_element = -1
        if self.queue:
            while self.queue:
                self.helper_stack.append(self.queue.pop())
            popped_element = self.helper_stack.pop()

            while self.helper_stack:
                self.queue.append(self.helper_stack.pop())
            
        return popped_element

    def peek(self) -> int:
        return self.queue[0] if self.queue else -1
        
    def empty(self) -> bool:
        return False if self.queue else True


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())
    obj.push(4)
    print(obj.peek())