from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_best_sum = nums[0]
        current_sum = nums[0]

        for value in nums[1:]:

            if current_sum < 0 and value >= current_sum:
                current_sum = value

            else:
                current_sum += value

            if current_sum > current_best_sum:
                current_best_sum = current_sum

        return current_best_sum


"""
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
"""
if __name__ == "__main__":
    solution = Solution()
    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

    print(result)

    # print(result)
