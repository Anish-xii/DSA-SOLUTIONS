class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 1. far l and r stores 0 water
        l_wal = r_wal = 0
        n = len(height)

        # 2. for all block track their max l and r block
        max_l = [0] * n
        max_r = [0] * n

        for i in range(n): # l
            j = -i - 1 # r

            # 3. track max walls to l and r
            max_l[i] = l_wal
            max_r[j] = r_wal
            l_wal = max(l_wal, height[i])
            r_wal = max(r_wal, height[j])

        res = 0
        for i in range(n):

            # 4. posible water this space can store
            posbl_water = min(max_l[i], max_r[i])

            # 5. - the block weight
            res += max(0, posbl_water - height[i])

        return res    