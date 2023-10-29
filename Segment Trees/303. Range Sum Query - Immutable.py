class NumArray:

    def __init__(self, nums):
        self.arr = nums
        self.size = len(nums)
        if self.size > 0:
            self.segment_tree = [0] * (4 * self.size)
            self.build(0, 0, self.size - 1)

    def build(self, node, start, end):
        if start == end:
            self.segment_tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)

        self.segment_tree[node] = self.segment_tree[left_child] + self.segment_tree[right_child]
        return

    def sum_query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and right >= end:
            return self.segment_tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        return self.sum_query(left_child, start, mid, left, right) + self.sum_query(right_child, mid + 1, end, left,
                                                                                    right)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_query(0, 0, self.size - 1, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)