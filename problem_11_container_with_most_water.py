from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current_max = -1

        while left < right:
            rect_height = min(height[left], height[right])
            rect_length = right - left
            current_area = rect_height * rect_length

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

            current_max = max(current_max, current_area)

        return current_max
