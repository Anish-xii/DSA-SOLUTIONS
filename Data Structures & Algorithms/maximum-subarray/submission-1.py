# the max sum for each pos 'i' is always that val

# DP
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        dp = [*nums]  # copy

        for i in range(1, len(nums)):
            new_start = nums[i]
            trailing_sum = dp[i-1] + nums[i]
            dp[i] = max(new_start, trailing_sum)
        
        return max(dp)