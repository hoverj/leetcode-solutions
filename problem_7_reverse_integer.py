class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        str_rep = str(x)
        reversed_int = str_rep[::-1]

        isNegative = reversed_int[-1] == "-"

        # drop the negative sign
        if isNegative:
            reversed_int = reversed_int[:-1]

        ans = int(reversed_int) if not isNegative else int(reversed_int) * -1

        if ans > INT_MAX or ans < INT_MIN:
            return 0

        return ans
