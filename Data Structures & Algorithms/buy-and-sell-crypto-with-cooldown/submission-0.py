class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
            dp[i][1] = max(dp[i + 1][1], dp[i + 2][0] + prices[i])

        return dp[0][0]

"""
For each day:
    Compute the best profit if we are allowed to buy:
either buy today (use next day’s sell profit minus price)
or skip today (keep next day’s buy profit)

Compute the best profit if we are allowed to sell:
either sell today (use profit from two days ahead plus price)
or skip today (keep next day’s sell profit)
"""