class Solution:
    def tribonacci(self, n: int) -> int:
        result_tree = {0: 0, 1: 1, 2: 1}

        def memoization(n: int):
            if n in result_tree:
                return result_tree[n]

            result = memoization(n - 3) + memoization(n - 2) + memoization(n - 1)
            result_tree[n] = result
            return result

        return memoization(n)


"""
Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
"""
if __name__ == "__main__":
    solution = Solution()
    result = solution.tribonacci(3)

    print(result)

    # print(result)
