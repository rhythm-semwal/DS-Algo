# @type of arr: list of integers
# @return type: list of list of integers
class Solution1:
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


class Solution2:
    # TC = O(n**2 * log(M)) where M is the length of the set for the lookup
    # SC = O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()

        for i in range(len(nums)-2):
            temp_set = set()
            for j in range(i+1, len(nums)):
                current_sum = -(nums[i] + nums[j])
                if current_sum in temp_set:
                    result = [nums[i], nums[j], current_sum]
                    result_set.add(tuple(sorted(result)))
                else:
                    temp_set.add(nums[j])

        answer = []
        for each in result_set:
            answer.append(list(each))

        return answer