class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) < 2: return max_profit

        i, j = 0, 1

        while j < len(prices):
            
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                j += 1
            else:
                i = j
                j = i + 1
        
        return max_profit