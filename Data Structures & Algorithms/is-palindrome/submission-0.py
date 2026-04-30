class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 1. check from both sides atonce
        l, r = 0, len(s)-1

        # 2. check untill the middle
        while l < r:
            
            # 3. skip any non alphanumaric chars
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1

            # 4. compare the alphanumaric chars
            if s[l].lower() != s[r].lower(): return False

            # 5. next chars
            l += 1
            r -= 1

        return True    