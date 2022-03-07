class Solution:
    def maxArea(self, height):
        result = 0

        i, j = 0, len(height)-1

        while i < j:
            result = max(result, min(height[i], height[j])*(j-i))

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return result


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Solution().maxArea(height)
