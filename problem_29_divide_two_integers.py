class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        two_multiple = 2
        divisor_sum = 0
        abs_divisor = abs(divisor)
        abs_dividend = abs(dividend)
        dividend_to_subtract = abs_dividend
        current = abs_divisor
        powers = [(1, abs_divisor)]
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        while current < abs_dividend:
            current = abs_divisor * two_multiple
            powers.append((two_multiple, current))
            two_multiple *= 2

        for power, value in reversed(powers):
            if value <= dividend_to_subtract:
                divisor_sum += power
                dividend_to_subtract -= value

        result = divisor_sum

        if (divisor < 0) != (dividend < 0):
            result = -1 * result

        if result >= INT_MAX:
            return INT_MAX

        elif result <= INT_MIN:
            return INT_MIN

        return result


"""
Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
"""
if __name__ == "__main__":
    solution = Solution()
    result = solution.divide(7, -3)

    print(result)

    # print(result)
