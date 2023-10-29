class Box:
    def __init__(self, h, w, l):
        self.h = h
        self.w = w
        self.l = l

    def __lt__(self, other):
        return self.w * self.l < other.w * other.l


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        """
        1) Generate all 3 rotations of all boxes. The size of rotation array becomes 3 times the
        size of the original array. For simplicity, we consider width as always smaller than or equal to depth.

        2) Sort the above generated 3n boxes in decreasing order of base area.

        3) After sorting the boxes, the problem is same as LIS with following optimal substructure property.
        MSH(i) = Maximum possible Stack Height with box i at top of stack
        MSH(i) = { Max ( MSH(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i).
        If there is no such j then MSH(i) = height(i)

        4) To get overall maximum height, we return max(MSH(i)) where 0 < i < n
        """
        n = len(A)
        box_array = [Box(0, 0, 0) for _ in range(3*n)]

        index = 0
        for i in range(n):

            # original box
            box_array[index].h = A[i][0]
            # length of the box will be the max
            box_array[index].l = max(A[i][1], A[i][2])
            # width of the box will be the min
            box_array[index].w = min(A[i][1], A[i][2])
            index += 1

            box_array[index].h = A[i][1]
            box_array[index].l = max(A[i][0], A[i][2])
            box_array[index].w = min(A[i][0], A[i][2])
            index += 1

            box_array[index].h = A[i][2]
            box_array[index].l = max(A[i][0], A[i][1])
            box_array[index].w = min(A[i][0], A[i][1])
            index += 1

        n *= 3

        # sort it in decreasing order
        box_array.sort(reverse=True)
        # for i in range(n):
        #     print(box_array[i].h, 'x', box_array[i].w, 'x', box_array[i].l)

        lis = [0]*n

        for i in range(n):
            lis[i] = box_array[i].h

        print(lis)

        for i in range(1, n):
            for j in range(i):
                if box_array[j].w > box_array[i].w and box_array[j].l > box_array[i].l:
                    if lis[i] < lis[j] + box_array[i].h:
                        lis[i] = lis[j] + box_array[i].h

        result = -1
        for i in range(n):
            result = max(result, lis[i])

        print(result)


A = [[4, 6, 7], [1, 2, 3],
 [4, 5, 6], [10, 12, 32]]
Solution().solve(A)
