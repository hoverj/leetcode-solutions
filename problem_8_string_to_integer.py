class Solution:
    def myAtoi(self, s: str) -> int:
        readableString = ""
        index = 0
        numbers = "0123456789"
        integer_list = []
        ans = 0

        # Step 1: remove leading white space
        while index < len(s):
            if s[index] != " ":
                readableString = s[index:]
                break
            index += 1

        if len(readableString) == 0:
            return ans

        # Step 2: Find if negative or positive
        isNegative = readableString[0] == "-"
        index = 0

        # Step 3 Skip all leading 0s
        while index < len(readableString):
            if index == 0 and readableString[index] in "+-":
                pass

            elif readableString[index] != 0:
                readableString = readableString[index:]
                break

            index += 1

        # Step 4 Gather the integers until non-numeric
        for char in readableString:
            if char not in numbers:
                break

            integer_list.append(char)

        index = 0
        integer_list_len = len(integer_list)
        while index < integer_list_len:
            value = integer_list[index]
            ans += int(value) * (10 ** (integer_list_len - index - 1))
            index += 1

        if ans >= 2**31:
            return (2**31) - 1 if not isNegative else -(2**31)

        return ans if not isNegative else ans * -1
