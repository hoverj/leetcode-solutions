class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for char in s[::-1]:
            if char == " " and count > 0:
                return count

            elif char == " ":
                continue

            else:
                count += 1

        return count
