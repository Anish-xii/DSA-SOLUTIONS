class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s): 1}
        
        def dfs(i):
            if i in dp: return dp[i]
            if s[i] == '0': return 0
            
            # 1. try 1 digit combos
            res = dfs(i+1)

            # 2. try 2 ((i, i+1) tigether) digit combos and += res
            if i+1 < len(s):
                # if the combo is valid (1-26)
                if s[i] == '1' or s[i] == '2' and s[i+1] in '0123456':
                    res += dfs(i+2)
                    
            dp[i] = res
            return res
        

        return dfs(0)

