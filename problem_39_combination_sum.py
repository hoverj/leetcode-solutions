from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backTrack(current: List[int], index: int, target: int):
            if target == 0:
                answer.append(current.copy())
                return

            if target < 0:
                return

            if len(candidates) == index:
                return

            current_value = candidates[index]
            if current_value <= target:
                current.append(current_value)
                backTrack(current=current, target=target - current_value, index=index)
                current.pop()

            backTrack(current=current, target=target, index=index + 1)

        backTrack(current=[], target=target, index=0)
        return answer


"""
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""

if __name__ == "__main__":
    solution = Solution()
    result = solution.combinationSum(candidates=[2, 3, 6, 7], target=7)

    print(result)

    # print(result)
