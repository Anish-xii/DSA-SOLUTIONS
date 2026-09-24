class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        dp = [0] * (amount+1)
        dp[0] = 1

        for c in coins:
            
            for i in range(c, amount+1):
                dp[i] += dp[i - c]
        
        return dp[amount]

# https://www.youtube.com/watch?v=aH0oqb4mj4Y$0