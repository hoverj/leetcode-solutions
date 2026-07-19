class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        def recursion(n: int, two_power: int):
            if two_power == n:
                return True

            elif two_power > n:
                return False

            else:
                return recursion(n=n, two_power=two_power * 2)

        return recursion(n=n, two_power=1)


"""
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

"""
if __name__ == "__main__":
    solution = Solution()
    result = solution.isPowerOfTwo(3)

    print(result)

    # print(result)
