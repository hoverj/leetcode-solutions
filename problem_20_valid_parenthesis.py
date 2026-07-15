class Solution:
    def isValid(self, s: str) -> bool:
        seenChars = []
        openingChars = "([{"

        for char in s:
            if char in openingChars:
                seenChars.append(char)
            
            elif len(seenChars) == 0:
                return False
            
            elif char == ")" and seenChars[-1] == "(":
                seenChars.pop(-1)
            
            elif char == "]" and seenChars[-1] == "[":
                seenChars.pop(-1)

            elif char == "}" and seenChars[-1] == "{":
                seenChars.pop(-1)

            else:
                return False
        
        return len(seenChars) == 0