class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        int_as_string = str(x)
        left = 0
        right = len(int_as_string) - 1

        while left < right:
            if int_as_string[left] != int_as_string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        