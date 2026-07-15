from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        values_equal_or_lower_than_target = 0
        while nums:
            midpoint = len(nums) // 2
            midpoint_value = nums[midpoint]

            if midpoint_value < target:
                nums = nums[midpoint:]
                values_equal_or_lower_than_target += midpoint

            elif midpoint_value > target:
                nums = nums[:midpoint]

            elif midpoint_value == target:
                return values_equal_or_lower_than_target + midpoint

            if len(nums) == 1 and nums[0] < target:
                values_equal_or_lower_than_target += 1
                break
            elif len(nums) == 1 and nums[0] > target:
                break

        return values_equal_or_lower_than_target
