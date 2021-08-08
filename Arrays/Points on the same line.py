class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def gcd(self, A, B):
        if A < B:
            A, B = B, A

        while B:
            A, B = B, A%B

        return A

    def solve(self, A, B):

        # approach 1
        max_points = -1
        for i in range(len(A)):
            slope_hash_map = dict()
            vertical = 1
            horizontal = 0
            current_max = -1
            for j in range(i+1, len(B)):
                if A[i] == A[j] and B[i] == B[j]:
                    horizontal += 1
                elif A[i] == A[j]:
                    vertical += 1
                else:
                    x_diff = A[j]-A[i]
                    y_diff = B[j] - B[i]
                    z = self.gcd(x_diff, y_diff)
                    x_diff = x_diff/z
                    y_diff = y_diff / z

                    if slope_hash_map.get((x_diff, y_diff)) is None:
                        slope_hash_map[(x_diff, y_diff)] = 2
                    else:
                        slope_hash_map[(x_diff, y_diff)] += 1

                    current_max = max(current_max, slope_hash_map[(x_diff, y_diff)])

                current_max = max(current_max, vertical)

            max_points = max(max_points, current_max+horizontal)

        return max_points

        # approach2
        # global_max = 0
        # for i in range(len(A)):
        #     # Keeping track of slopes for a given fixed point
        #     local_slope_dict = {}
        #     # Each point by itself is a vertical line.
        #     vertical = 1
        #     # overlapping points are added in the end in additional to local max.
        #     overlap = 0
        #
        #     for j in range(i + 1, len(A)):
        #
        #         if A[i] == A[j] and B[i] == B[j]:
        #             overlap += 1
        #         elif A[i] == A[j]:
        #             vertical += 1
        #         else:
        #             # In python 2 make sure to use float for high precision
        #             # and to avoid to rounding down.
        #             slope = (B[i] - B[j]) / float(A[i] - A[j])
        #             if slope in local_slope_dict:
        #                 local_slope_dict[slope] = local_slope_dict[slope] + 1
        #             else:
        #                 local_slope_dict[slope] = 2
        #
        #     local_max = 0
        #
        #     for x in local_slope_dict.values():
        #         local_max = max(local_max, x)
        #
        #     local_max = max(local_max, vertical)
        #     # Add any overlapping points
        #     local_max = local_max + overlap
        #
        #     global_max = max(local_max, global_max)
        #
        # return global_max

A = [3, 1, 4, 5, 7, -9, -8, 6]
B = [4, -8, -3, -2, -1, 5, 7, -4]
print(Solution().solve(A, B))