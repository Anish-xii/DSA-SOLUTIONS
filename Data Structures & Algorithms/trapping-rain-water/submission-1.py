class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 4 pointers: lmax,l & rmax,r
        n = len(height) -1
        l, l_max = 0, height[0] # combo-1
        r, r_max = n, height[n] # combo-2

        res = 0
        # 1. Chose the smaller end of l/r
        # 2. take 1 step and update the max height
        # 3. for cur block add max water - cur height
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]

        return res            

    # as we chose the smaller end of l/r it is garentied we can store
    # exactly that amount water, it now dependes how much of that space
    # is allredy filled by the blocks.