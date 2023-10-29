from collections import deque


class QueueWithMax:
    def __init(self):
        self._queue = deque()
        self._max_candidate = deque()

    def enqueue(self, x):
        self._queue.append(x)
        if self._max_candidate:
            while self._max_candidate and self._max_candidate[-1] < x:
                self._max_candidate.pop()

        self._max_candidate.append(x)

    def dequeue(self):
        if self._queue:
            element = self._queue.popleft()

            if element == self._max_candidate[0]:
                self._max_candidate.popleft()

        raise IndexError('empty queue')

    def max(self):
        if self._max_candidate:
            return self._max_candidate[0]
        raise IndexError('empty queue')


obj = QueueWithMax()
obj.enqueue(3)
obj.enqueue(1)
obj.enqueue(3)
obj.enqueue(2)
obj.enqueue(0)
obj.enqueue(1)
print(obj.max())
obj.dequeue()
obj.dequeue()
print(obj.max())
obj.enqueue(2)
obj.enqueue(4)
print(obj.max())
obj.dequeue()
print(obj.max())
obj.enqueue(4)
print(obj.max())