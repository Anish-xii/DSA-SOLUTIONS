class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = {}
        
        # dfs
        def dfs_cost(n):
            if n >= len(cost):
                return 0
            if n in dp:
                return dp[n]
            
            dp[n] = cost[n] + min(dfs_cost(n+1), dfs_cost(n+2))
            return dp[n]
        
        return min(dfs_cost(0), dfs_cost(1)) # which way returns min cost