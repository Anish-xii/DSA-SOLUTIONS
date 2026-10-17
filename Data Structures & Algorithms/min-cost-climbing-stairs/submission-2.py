class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        n = len(cost)
        dp = [0] * (n+1)

        # steping at step 1 and 2 took nothing
        # but from them what it takes to make it to other steps
        # for every stem keep track of the min cost to reach the steps
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[n]