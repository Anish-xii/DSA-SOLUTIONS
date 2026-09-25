# for every stage get the maximum jump range
# for every val in that range get the next range (from after the alredy covered range)
# each range is a potential jump
# when we cant jump any further, thats max jump

# BFS: no need to get exact-path, only cheking posibility at each stage
class Solution:
    def jump(self, nums: list[int]) -> int:
        
        res = 0
        l, r = 0, 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            res += 1
        
        return res
            