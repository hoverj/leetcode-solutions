from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        left_most = -1
        right_most = -1

        def find_left_most(left: int, right: int) -> int:
            answer = right
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1

                else:
                    if nums[mid] == target:
                        answer = mid
                    right = mid - 1

            return answer

        def find_right_most(left: int, right: int) -> int:
            answer = left
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1

                else:
                    if nums[mid] == target:
                        answer = mid
                    left = mid + 1

            return answer

        while right >= left:
            mid = (left + right) // 2

            if nums[mid] == target:
                left_most = find_left_most(left, mid)
                right_most = find_right_most(mid, right)
                break

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return [left_most, right_most]


"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
"""

if __name__ == "__main__":
    solution = Solution()
    result = solution.searchRange([5, 7, 7, 8, 8, 10], 8)

    print(result)

    # print(result)
