class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        def myRecursion(n: int):

            if n == 0:
                return 1
            if n == 1:
                return x

            # if in is odd it wont divide properly
            if n % 2 == 1:
                half = myRecursion(n // 2)
                return half * half * x
            else:
                half = myRecursion(n=n // 2)
                return half * half

        answer = myRecursion(n=abs(n))

        if n < 0:
            return 1 / answer

        return answer


"""
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
"""

if __name__ == "__main__":
    solution = Solution()
    result = solution.myPow(2.00000, 10)

    print(result)

    # print(result)
