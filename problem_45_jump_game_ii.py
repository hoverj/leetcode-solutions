from typing import List


class Solution:
    # TODO can be solved in O(n) time complexity and O(1) space complexity
    def jump(self, nums: List[int]) -> int:

        def find_min_jumps(starting_index: int) -> int:
            current_index = starting_index - 1
            current_best_index = -1
            while current_index >= 0:
                if current_index + nums[current_index] >= starting_index:
                    current_best_index = current_index

                current_index -= 1

            return current_best_index

        current_min_jumps = 0
        current_goal_index = len(nums) - 1

        while current_goal_index > 0:
            current_goal_index = find_min_jumps(current_goal_index)
            current_min_jumps += 1

        return current_min_jumps


"""
Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

if __name__ == "__main__":
    solution = Solution()
    result = solution.jump([2, 3, 1, 1, 4])

    print(result)

    # print(result)
