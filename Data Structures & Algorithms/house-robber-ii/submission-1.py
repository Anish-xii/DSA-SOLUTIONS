class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]

        def house_section(houses):
            if not houses: return 0
            if len(houses) == 1: return houses[0]

            dp = [0] * len(houses)
            dp[0] = houses[0]
            # for each house-infront, we can have money of that house or prev-house
            dp[1] = max(houses[0], houses[1])

            # (rob the house + skip next) / (rob next house) - topdown
            # (money of the house + money of house -2) / (money of prev(-1) house & no-rob)
            for h in range(2, len(houses)):
                dp[h] = max(houses[h] + dp[h-2], dp[h-1])
            return dp[-1] # alyway after all house robbed

        # max rob if skip 1 or last house
        return max(house_section(nums[:-1]), house_section(nums[1:]))