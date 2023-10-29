"""
S.C = O(N)
but get min operation takes O(1) time
"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(self.max_stack[-1], x))

    def pop(self):
        self.stack.pop()
        self.max_stack.pop()

    def getMax(self):
        return self.max_stack[-1]

"""
S.C = O(1)
but get min operation takes O(N) time
"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_element = float('-inf')

    def push(self, x):
        self.stack.append(x)
        self.max_element = max(self.max_element, x)

    def pop(self):
        if self.stack:
            element = self.stack.pop()

            if element == self.max_element:
                if self.stack:
                    self.max_element = max(self.stack)
                else:
                    self.max_element = float('-inf')

    def getMax(self):
        return self.max_element