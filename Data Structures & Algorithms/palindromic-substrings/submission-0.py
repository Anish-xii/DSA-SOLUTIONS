# on^2
class Solution:
    def countSubstrings(self, s: str) -> int:

        pal_count = 0

        for i in range(len(s)):

            # odd pares for each char (inside-out)
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                pal_len = r-l+1
                pal_count += 1
                l -= 1
                r += 1
            
            # even pares
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                pal_len = r-l+1
                pal_count += 1
                l -= 1
                r += 1
        
        return pal_count