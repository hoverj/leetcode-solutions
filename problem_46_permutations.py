from typing import List

class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def backtrack(current: List[int], remaining: List[int]):
            if len(remaining) == 0:
                answer.append(current.copy())
            
            for choice in range(len(remaining)):
                current.append(remaining[choice])
                backtrack(current, remaining = remaining[:choice] + remaining[choice+1:])
                current.pop()
        
        backtrack(current=[], remaining=nums)
        return answer

