class Solution:
    def climbStairs(self, n: int) -> int:
        tracker = {0: 0}

        def memoization(steps_left: int):
            if steps_left in tracker:
                return tracker[steps_left]

            if steps_left == 0:
                return 0

            if steps_left == 1:
                return 1

            if steps_left == 2:
                return 2

            result = memoization(steps_left - 1) + memoization(steps_left - 2)
            tracker[steps_left] = result
            return result

        return memoization(steps_left=n)


"""
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
if __name__ == "__main__":
    solution = Solution()
    result = solution.climbStairs(3)

    print(result)

    # print(result)
