from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.min_num = 1
        self.is_val_in_heap = dict()

    def popSmallest(self) -> int:
        # TC = O(1) for both if and else condition
        if not self.heap:
            smallest = self.min_num
            self.min_num += 1
        else:
            smallest = heappop(self.heap)
            del self.is_val_in_heap[smallest]

        return smallest

    def addBack(self, num: int) -> None:
        # TC = O(log N)
        if num >= self.min_num or num in self.is_val_in_heap:
            return
        elif num == self.min_num - 1:
            self.min_num -= 1
        else:
            heappush(self.heap, num)
            self.is_val_in_heap[num] = True


obj = SmallestInfiniteSet()
print(obj.popSmallest())
obj.addBack(2)
obj.addBack(1)
obj.addBack(3)
print(obj.popSmallest())
print(obj.popSmallest())