class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 2 pointer: checks all posible profit margins 
        # 1 traker: saves best posible profit made so far
        l, r = 0, 1
        max_p = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            
            else: l = r # new low price

            r += 1

        return max_p 