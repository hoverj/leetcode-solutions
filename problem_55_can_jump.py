from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_winning_index = len(nums) - 1
        current_index = current_winning_index - 1

        while current_index >= 0:
            if current_index + nums[current_index] >= current_winning_index:
                current_winning_index = current_index

            current_index -= 1

        return current_winning_index == 0


"""
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

if __name__ == "__main__":
    solution = Solution()
    result = solution.canJump([2, 3, 1, 1, 4])

    print(result)

    # print(result)
