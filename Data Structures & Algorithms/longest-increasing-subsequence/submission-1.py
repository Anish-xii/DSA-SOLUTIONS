# Bottom-up

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [1] * n

        # for each val from end
        for i in range(n-1, -1, -1):
            # max seq is that val and any bigger val we have visted or 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+ dp[j]) 
        
        return max(dp)

        