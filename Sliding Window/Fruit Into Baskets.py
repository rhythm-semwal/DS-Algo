# https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=sliding-window
#TC = O(N)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        from collections import defaultdict
        seen = defaultdict(int)
        result = 0

        for end in range(len(fruits)):
            seen[fruits[end]] += 1

            while len(seen) > 2:
                seen[fruits[start]] -= 1

                if seen[fruits[start]] == 0:
                    del seen[fruits[start]]

                start += 1
            result = max(result, end - start + 1)
        return result


if __name__ == "__main__":
    # fruits = [1, 2, 3, 2, 2]
    fruits = [0, 1, 2, 2]
    fruits = [1, 2, 1]
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    print(Solution().totalFruit(fruits))
