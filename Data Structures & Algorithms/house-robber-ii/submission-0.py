class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            pos1, pos2 = 0, 0
            for n in houses:
                tmp = max(n + pos1, pos2)
                pos1 = pos2
                pos2 = tmp
            return pos2

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))