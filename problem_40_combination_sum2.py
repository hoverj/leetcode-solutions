from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def backTrack(current: List[int], target: int, index: int):
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
                backTrack(
                    current=current, target=target - current_value, index=index + 1
                )
                current.pop()

            next_index = index + 1
            while (
                next_index < len(candidates)
                and candidates[next_index] == candidates[index]
            ):
                next_index += 1
            backTrack(current=current, target=target, index=next_index)

        backTrack(current=[], target=target, index=0)
        return answer


"""
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""


if __name__ == "__main__":
    solution = Solution()
    result = solution.combinationSum2(candidates=[1, 1], target=1)

    print(result)

    # print(result)
