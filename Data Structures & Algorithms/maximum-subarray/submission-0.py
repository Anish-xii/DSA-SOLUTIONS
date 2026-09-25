# the max sum for each pos 'i' is always that val

# greedy (kadeins-algo)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            # no need to keep negetive bagage 
            if cur_sum < 0: cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        
        return max_sum