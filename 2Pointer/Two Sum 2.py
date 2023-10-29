class Solution:
    def twoSum(self, numbers, target: int):
        start, end = 0, len(numbers)-1

        while start < end:
            current_sum = numbers[start] + numbers[end]
            if current_sum == target:
                return [start+1, end+1]
            elif current_sum < target:
                start += 1
            else:
                end -= 1
        return []


if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 18
    print(Solution().twoSum(numbers, target))
