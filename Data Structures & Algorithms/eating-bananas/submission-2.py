class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            mid = (l+r)//2  # speed/hr

            hr = 0
            # total time with speed (mid), to eat all
            for p in piles:
                hr += math.ceil(p/mid)

            # if under time, try find a greedy relaxed speed
            if hr <= h:
                res = min(res, mid)
                r = mid -1
            # need to eat more per hr
            else:
                l = mid + 1
        
        return res