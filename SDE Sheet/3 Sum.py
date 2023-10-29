# @type of arr: list of integers
# @return type: list of list of integers
class Solution:
    def tripleSum(self, arr: List[int]) -> List[List[int]]:
        # write your awesome code here
        n = len(arr)
        arr.sort()
        result = list()
        for i in range(n - 2):

            if i == 0 or arr[i] != arr[i - 1]:

                left = i + 1
                right = n - 1

                while left < right:

                    current_sum = arr[i] + arr[left] + arr[right]

                    if current_sum == 0:
                        temp = [arr[i], arr[left], arr[right]]
                        result.append(temp)

                        while left < right and arr[left] == temp[1]:
                            left += 1

                        while left < right and arr[right] == temp[2]:
                            right -= 1
                    elif current_sum > 0:
                        right -= 1
                    else:
                        left += 1

        return result