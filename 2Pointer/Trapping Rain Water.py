class Solution:
    def trap(self, height) -> int:
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        result = 0

        while left < right:
            if max_left < max_right:
                left += 1
                # calculating max left ensure that result is never negative, else we will have to add check
                max_left = max(max_left, height[left])
                result += max_left - height[left]
                
            else:
                right -= 1
                max_right = max(max_right, height[right])
                result += max_right - height[right]

        return result


if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    print(Solution().trap(height))