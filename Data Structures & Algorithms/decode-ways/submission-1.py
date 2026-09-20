# for each pos in s of nums, we find how many 
# valid combos we can find if we deside to chose the number.
# 1. result = posible combo of 'i' + (i & i+1) for the rest of the array for top down
# 2. for bottom up its all combo from last to first combines
    
# Bottom-UP
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n+1)
        # the final-indx(single-digit) of a string-num always has 1 option
        dp[n] = 1 

        for i in range(n-1, -1, -1):
            # i is our start digit i+1 is 2nd of '26' (we have 1-26)
            # there are no options if num starts with '0'
            if s[i] == '0':
                dp[i] = 0
                continue
            
            # result = posible combo of 'i' + (i & i+1) 
            result = dp[i+1] 
            if i + 1 < n:
                if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                    result += dp[i+2]
            
            dp[i] = result
        
        return dp[0]


