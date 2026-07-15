class Solution:
    symbolToInteger = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def grabValue(self, curr: str, nextChar: str):
        value = self.symbolToInteger[curr]
        if nextChar is None:
            return (value, 0)

        if (
            ((nextChar == "V" or nextChar == "X") and curr == "I")
            or ((nextChar == "L" or nextChar == "C") and curr == "X")
            or ((nextChar == "D" or nextChar == "M") and curr == "C")
        ):
            return (self.symbolToInteger[nextChar] - value, 1)

        return (value, 0)

    def romanToInt(self, s: str) -> int:
        finalIndex = len(s)
        sum = 0
        index = 0
        while index < finalIndex:
            if index >= finalIndex - 1:
                sumLocal, _ = self.grabValue(s[index], None)
                sum += sumLocal

            else:
                sumLocal, indexInc = self.grabValue(s[index], s[index + 1])
                sum += sumLocal
                index += indexInc

            index += 1

        return sum
