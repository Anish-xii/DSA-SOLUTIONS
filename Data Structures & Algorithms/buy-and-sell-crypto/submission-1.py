class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_p = 0
        min_price = prices[0]

        for p in prices:
            max_p = max(max_p, p - min_price)
            min_price = min(min_price, p)

        return max_p    