class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)

        if len(needle) > haystack_length:
            return -1

        left_pointer = 0
        right_pointer = len(needle) - 1

        while right_pointer < haystack_length:
            if haystack[left_pointer : right_pointer + 1] == needle:
                return left_pointer

            left_pointer += 1
            right_pointer += 1

        return -1
