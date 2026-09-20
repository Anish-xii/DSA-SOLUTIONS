# for each pos in s of nums, we find how many 
# valid combos we can find if we deside to chose the number.

class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        memo = {}

        def dfs(i):
            # how many valid this num at 'i' allows, the final-digit(single) always alows 1
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            # i is our start digit i+1 is 2nd of '26' (we have 1-26)
            if s[i] == '0':
                return 0
            
            # start checking
            result = 0
            result += dfs(i+1) # if we chose only 'i' howmany combo dose [i+1:n] gives
            # if we chose only 'i & i+1' howmany combo dose [i+2:n] gives
            if i+1 <n:
                if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                    result += dfs(i+2)
            
            memo[i] = result

            return result


        return dfs(0)