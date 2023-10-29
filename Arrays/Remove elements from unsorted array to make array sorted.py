# https://www.geeksforgeeks.org/remove-elements-to-make-array-sorted/
class Solution1:
    def remove_elements_to_make_array_sorted(self, arr) -> int:
        """
        SC = O(N)
        TC = O(N)
        """
        result = list()
        result.append(arr[0])

        for i in range(1, len(arr)):
            if arr[i] > result[-1]:
                result.append(arr[i])
        return result


class Solution2:
    def remove_elements_to_make_array_sorted(self, arr) -> int:
        """
        SC = O(N)
        TC = O(N)
        """
        l = 1

        for i in range(1, len(arr)):
            if arr[i] >= arr[l-1]:
                arr[l] = arr[i]
                l += 1

        result = []
        for i in range(l):
            result.append(arr[i])

        return result


input = [1, 2, 4, 3, 5, 7, 8, 6, 9, 10]
print(Solution2().remove_elements_to_make_array_sorted(input))
