class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # formula (i + (i+1) + (n-x))

        nums.sort() # list sorted
        n = len(nums)
        res = []

        for i in range(n):

            if nums[i] > 0: break     # when no more negetivis
            elif i > 0 and nums[i] == nums[i-1]: continue  # if same as last num seen

            l, r = i+1, n-1

            while l < r:
                
                cur_sum = nums[i] + nums[l] + nums[r]
                
                if cur_sum == 0: 
    
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1

                elif cur_sum > 0: r -= 1
                else: l += 1

        return res        