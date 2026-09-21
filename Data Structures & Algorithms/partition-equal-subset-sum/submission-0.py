# for each num in arr, get all comb of pares/trplets/len(n)'s - sum
# if abc: get a,b,c,ab,ac,bc,abc (all sums in set)
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            tmp_dp = set()
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                tmp_dp.add(t)
                tmp_dp.add(t+nums[i])
            
            dp = tmp_dp
        
        return False

        