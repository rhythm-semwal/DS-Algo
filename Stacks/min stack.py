import sys
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_element = min(self.min_element, val)
        return

    def pop(self) -> None:
        if self.stack:
            popped_element = self.stack.pop()
            if popped_element == self.min_element:
                if self.stack:
                    self.min_element = min(self.stack)
                else:
                    self.min_element = sys.maxsize
        return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.stack:
            return self.min_element
        return -1


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())