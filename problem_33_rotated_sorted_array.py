from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # find the sorted sector
            if nums[left] <= nums[mid]:
                # left is sorted

                # can target be in sorted left
                if target >= nums[left] and target < nums[mid]:
                    # target is in the sorted left
                    right = mid - 1
                else:
                    # target cannot be in sorted left
                    left = mid + 1

            else:
                # right is sorted
                if target <= nums[right] and target > nums[mid]:
                    # target is in the sorted right
                    left = mid + 1
                else:
                    # target cannot be in sorted right
                    right = mid - 1

        return -1


"""
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

"""
if __name__ == "__main__":
    solution = Solution()
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 0)

    print(result)

    # print(result)
