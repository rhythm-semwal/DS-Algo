from typing import List


class Solution1:
    def trap(self, height: List[int]) -> int:
        result = 0

        left_max_height, right_max_height = height[0], height[-1]
        left, right = 1, len(height) - 1

        while left <= right:
            if height[left] > left_max_height:
                left_max_height = height[left]

            if height[right] > right_max_height:
                right_max_height = height[right]

            if left_max_height <= right_max_height:
                result += left_max_height - height[left]
                left += 1
            else:
                result += right_max_height - height[right]
                right -= 1

        return result

    
class Solution2:
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