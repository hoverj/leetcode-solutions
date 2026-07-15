from typing import List


class Solution:
    def plusOneHelper(self, index: int, digits: List[int]):
        if digits[index] < 9:
            digits[index] = digits[index] + 1

        elif digits[index] == 9 and index == 0:
            digits[index] = 0
            digits.insert(0, 1)

        else:
            digits[index] = 0
            return self.plusOneHelper(index - 1, digits)

        return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusOneHelper(len(digits) - 1, digits)
