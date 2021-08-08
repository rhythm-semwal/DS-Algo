"""
SC = O(1)
but get min operation takes O(N) time
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_element = float('inf')

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        self.min_element = min(self.min_element, x)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            element = self.stack.pop()
            if element == self.min_element:
                if len(self.stack) > 0:
                    self.min_element = min(self.stack)
                else:
                    self.min_element = float('inf')

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    # @return an integer
    def getMin(self):
        if self.stack:
            return self.min_element
        return -1

"""
SC = O(N)
but get min operation takes O(1) time
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))

    # @return nothing
    def pop(self):
        del self.stack[-1]
        del self.min_stack[-1]

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    # @return an integer
    def getMin(self):
        if self.stack:
            return self.min_stack[-1]
        return -1


# class MinStack:
#     # @param x, an integer
#     # @return an integer
#     def __init__(self):
#         self.stack = list()
#         self.min_element = sys.maxsize
#         self.min_stack = list()
#
#     def push(self, x):
#         if len(self.min_stack) == 0:
#             self.min_stack.append(x)
#         elif x < self.min_stack[-1]:
#             self.min_stack.append(x)
#         self.stack.append(x)
#
#     # @return nothing
#     def pop(self):
#         if len(self.stack) == 0:
#             return
#         else:
#             element = self.stack.pop()
#             if element == self.min_stack[-1]:
#                 self.min_stack.pop()
#             return element
#     # @return an integer
#     def top(self):
#
#         return self.stack[-1] if len(self.stack) != 0 else -1
#
#     # @return an integer
#     def getMin(self):
#         return self.min_stack[-1] if len(self.min_stack) != 0 else -1
#
#
# obj = MinStack()
# print(obj.push(1))
# print(obj.push(2))
# print(obj.push(-2))
# print(obj.getMin())
# print(obj.pop())
# print(obj.getMin())
# print(obj.top())

print(obj.getMin())
print(obj.pop())
print(obj.top())
