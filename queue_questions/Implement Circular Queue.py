class CircularQueue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._queue = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        # check if the queue is full
        if self._num_queue_elements == len(self._queue):  # need to resize the queue
            # before resizing make the queue elements appear consecutively
            self._queue = (self._queue[self.head:] + self._queue[:self.head])

            # reset head and tail pointer
            self._head, self._tail = 0, self._num_queue_elements

            # adding the None values in the already existing self._queue array.
            # Since we are adding in the already exisitng array that is why we are
            # doing subtraction
            self._queue += [None] * (len(self._queue) * CircularQueue.SCALE_FACTOR -
                                     len(self._queue))

        self._enqueue[self._tail] = x
        self._tail = (self._tail + 1) % (len(self._queue))
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError("Queue is Empty")

        element = self._queue[self._head]
        self._head = (self._head + 1) % len(self._queue)
        self._num_queue_elements -= 1
        return element

    def size(self):
        return self._num_queue_elements
