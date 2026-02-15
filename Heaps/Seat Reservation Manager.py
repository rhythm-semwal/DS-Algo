# https://leetcode.com/problems/seat-reservation-manager/description/?envType=problem-list-v2&envId=heap-priority-queue

# Initial my approach
class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        for i in range(1, n+1):
            self.heap.append(i)
        heapq.heapify(self.heap)
        print(self.heap)

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return 0

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# Optimised approach
class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.next_reserved = 1
        self.max_capacity = n

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        elif self.next_reserved <= self.max_capacity:
            seat = self.next_reserved
            self.next_reserved += 1
            return seat
        else:
            return 0

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
