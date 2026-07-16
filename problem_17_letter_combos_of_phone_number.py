from typing import List


class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        answer = []
        digits_posibilities = {
            "2": ["a", "b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }

        def backTrack(current: str, remaining: List[str]):
            if len(remaining) == 0:
                answer.append(current)
                return
            
            for char in remaining[0]:
                current += char
                backTrack(current=current, remaining=remaining[1:])
                current = current[:-1]


        # List of Lists
        backTrack(current = "", remaining=[digits_posibilities[digit] for digit in digits]) 
        return answer