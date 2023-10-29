class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def custom_sort_function(self, a, b):
        if a[1] < b[1]:
            return -1
        elif a[1] == b[1]:
            if a[0] == b[0]:
                if a[2] > b[2]:
                    return 1
                else:
                    return -1

            elif a[0] > b[0]:
                return 1
            else:
                return -1
        else:
            return 1

    def maximumMeetings(self, n, start, end):
        # code here
        zipped_array = []
        for i in range(n):
            zipped_array.append((start[i], end[i], i + 1))

        from functools import cmp_to_key
        compare_key = cmp_to_key(self.custom_sort_function)
        zipped_array.sort(key=compare_key)

        print(zipped_array)

        ans = 1
        current_end_time = zipped_array[0][1]
        for i in range(1, len(zipped_array)):
            if zipped_array[i][0] > current_end_time:
                ans += 1
                current_end_time = zipped_array[i][1]
        print(ans)


S = [75250, 50074, 43659, 8931, 11273,27545, 50879, 77924]
F = [112960, 114515, 81825, 93424, 54316,35533, 73383, 160252]
n = len(S)
Solution().maximumMeetings(n, S, F)
