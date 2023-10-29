class Solution:
    def maxArea(self, height) -> int:
        start, end = 0, len(height) - 1

        ans = 0

        while start < end:
            ans = max(ans, min(height[start], height[end]) * (end - start))

            if height[end] <= height[start]:
                end -= 1
            else:
                start += 1
        return ans


if __name__ == '__main__':
    height = [1, 1]
    print(Solution().maxArea(height))