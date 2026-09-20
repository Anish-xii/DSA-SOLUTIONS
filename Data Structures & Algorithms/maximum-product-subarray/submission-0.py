# goal is to find maxproduct subarray (one or multiple num product)
# 3 cases:-
#   1. posetive val: makes a max with + but min with -
#   2. negetive val: trickster, can get use a max with - but mins our +
#   3. 0: disuster, avoid, restart subarr from there (as sub is contigues)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        res = float('-inf')
        dp_max = dp_min = 1

        for n in nums:
            if n == 0:
                dp_max = dp_min = 1
                res = max(res, 0)
                continue
            # for each pos added get the max and min it causes
            # track both max AND min product ending at this position, because
            # multiplying by a negative number can flip the smallest (most negative)
            # product into the largest one -- so today's min might become tomorrow's max
            choices = (n*dp_max, n*dp_min, n)
            dp_max = max(choices)
            dp_min = min(choices)
            res = max(res, dp_max)
        
        return res
