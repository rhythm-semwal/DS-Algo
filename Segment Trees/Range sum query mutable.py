class NumArray:

    def __init__(self, nums):
        self.arr = nums
        self.segment_tree = [0] * (4 * len(nums))
        self.build(0, nums, 0, len(nums) - 1)
        self.result = []

    def build(self, node, arr, start, end):
        if start == end:
            self.segment_tree[node] = arr[start]
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self.build(left_child, arr, start, mid)
        self.build(right_child, arr, mid + 1, end)

        self.segment_tree[node] = self.segment_tree[left_child] + self.segment_tree[right_child]
        return

    def update_segment_tree(self, node, new_val, index, start, end):
        if start == end:
            self.arr[index] = new_val
            self.segment_tree[node] = new_val
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if index <= mid:
            self.update_segment_tree(left_child, new_val, index, start, mid)
        else:
            self.update_segment_tree(right_child, new_val, index, mid + 1, end)

        self.segment_tree[node] = self.segment_tree[left_child] + self.segment_tree[right_child]
        return

    def update(self, index: int, val: int) -> None:
        self.update_segment_tree(0, val, index, 0, len(self.arr) - 1)

    def get_sum_range(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and right >= end:
            return self.segment_tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        return self.get_sum_range(left_child, start, mid, left, right) + self.get_sum_range(right_child,
                                                                                            mid + 1, end, left, right)

    def sumRange(self, left: int, right: int) -> int:
        # result = []
        return self.get_sum_range(0, 0, len(self.arr) - 1, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)