from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_pointer = 0
        list_bounds = 0

        while current_pointer <= len(nums):
            if nums[list_bounds] != val:
                list_bounds += 1
                current_pointer = list_bounds + 1
                continue

            if nums[current_pointer] != val:
                nums[list_bounds], nums[current_pointer] = (
                    nums[current_pointer],
                    nums[list_bounds],
                )
                continue
            current_pointer += 1

        return list_bounds
