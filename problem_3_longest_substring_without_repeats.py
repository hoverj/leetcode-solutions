class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        left = 0
        right = 0
        seenChars = {}
        current_max = 0

        while right < len(s):
            if s[right] in seenChars:
                # no +1 here because right has already been seen, rightfully excluded
                current_max = max([current_max, right - left])
                left = max([left, seenChars[s[right]] + 1])
                seenChars[s[right]] = right

            seenChars[s[right]] = right
            # need +1 here as above eliminated the already seen character so left and right should both be included
            current_max = max(current_max, right - left + 1) 
            right += 1
        

        return current_max