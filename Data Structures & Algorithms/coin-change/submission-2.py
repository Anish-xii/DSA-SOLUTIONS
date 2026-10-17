class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        dp = {}

        def dfs(amount):
            if amount == 0: return 0
            if amount in dp: return dp[amount]

            # (when we keep chosing coins untill we hit 0
            # AND keep chosing diffrent coins) AND repeat
            combo = float('inf')
            for c in coins:
                if amount - c >= 0:
                    combo = min(combo, 1+dfs(amount-c))
            
            dp[amount] = combo
            return combo

        coin_num = dfs(amount)
        return coin_num if coin_num < float('inf') else -1