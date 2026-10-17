class Solution:
    def rob(self, nums: list[int]) -> int:
        
        dp = {}

        def dfs(i):
            # just optimisation
            if i >= len(nums): return 0
            if i in dp:
                return dp[i]

            # 2. (rob the house + skip next) / (rob next house)
            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return dp[i]
        
        return dfs(0) # 1. has to start from house 0