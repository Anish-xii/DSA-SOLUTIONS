class Solution:
    def rob(self, nums: list[int]) -> int:
        pos1, pos2 = 0, 0  # prev.prev, prev

        # [prev.prev, prev, n, n+1, ...]
        for n in nums:
            tmp = max(n + pos1, pos2) #[curr+prev.prev, prev]
            pos1 = pos2
            pos2 = tmp
        
        return pos2