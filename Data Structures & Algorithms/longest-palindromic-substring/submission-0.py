# search odd palandroms from inside-out
# find even from left to right

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        max_len = 0

        for i in range(len(s)):

            # odd pares for each char (inside-out)
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                pal_len = r-l+1
                if pal_len > max_len:
                    res = s[l:r+1]
                    max_len = pal_len
                l -= 1
                r += 1
            
            # even pares
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                pal_len = r-l+1
                if pal_len > max_len:
                    res = s[l:r+1]
                    max_len = pal_len
                l -= 1
                r += 1
        
        return res