from typing import List


class Solution1:
    """
    That's the sum of integers from 1->n ==> 1+2+3+....+n= n*(n+1)/2.
    So let's take an example [1,2,2,4]
    n=4
    a= 1+2+2+4= 9
    b=sum(set(num))= 1+2+4= 7
    s= n(n+1)/2= 1+2+3+4= 10

    therefore, a-b= 9-7=2, s-b= 10-7=3
    ans -> [2,3]
    """
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        s = n*(n+1)//2

        a, b = sum(nums), sum(set(nums))

        return [a-b, s-b]


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []

        visited = set()

        for num in nums:
            if num in visited:
                result.append(num)
            else:
                visited.add(num)

        for index, value in enumerate(nums):
            if index + 1 not in visited:
                result.append(index + 1)
                break

        return result
