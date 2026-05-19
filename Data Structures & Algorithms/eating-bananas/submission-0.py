class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = float('inf')

        l, r = 1, max(piles)

        while l <= r:
            per_h = l + ((r-l)//2)
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / per_h)

            if hours <= h:
                k = min(k, per_h)
                r = per_h - 1
            else:
                l = per_h + 1        
        
        return k