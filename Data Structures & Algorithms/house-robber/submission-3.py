# dp = focus on each step result not each step
class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        # for each house-infront, we can have money of that house or prev-house
        dp[1] = max(nums[0], nums[1])

        # (rob the house + skip next) / (rob next house) - topdown
        # (money of the house + money of house -2) / (money of prev(-1) house & no-rob)
        for h in range(2, len(nums)):
            dp[h] = max(nums[h] + dp[h-2], dp[h-1])

        return dp[-1] # alyway after all house robbed