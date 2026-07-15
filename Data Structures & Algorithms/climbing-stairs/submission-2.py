class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}

        def dfs(x):
            if x == 1: return 1
            if x == 2: return 2
            
            if x in dp: return dp[x]

            dp[x] = dfs(x-1) + dfs(x-2)

            return dp[x]

        return dfs(n)    