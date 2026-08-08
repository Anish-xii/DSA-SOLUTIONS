class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        pre = 1
        for i in range(len(res)):
            res[i] = pre
            pre *= nums[i]

        suf = 1
        for j in range(len(res)-1, -1, -1):
            res[j] *= suf
            suf *= nums[j]
        
        return res
        