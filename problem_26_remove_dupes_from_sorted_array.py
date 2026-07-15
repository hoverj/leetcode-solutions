from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return (0, nums)

        sortedPointer = 0
        currentPointer = 1

        while currentPointer < len(nums):
            if nums[sortedPointer] == nums[currentPointer]:
                currentPointer += 1
                continue

            sortedPointer += 1
            nums[sortedPointer], nums[currentPointer] = (
                nums[currentPointer],
                nums[sortedPointer],
            )
            currentPointer += 1

        return (sortedPointer + 1, nums)
