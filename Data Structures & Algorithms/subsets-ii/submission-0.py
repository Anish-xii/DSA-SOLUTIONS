class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sub = [], []
        nums.sort()

        def dfs_backtrack(i):
            # base case for recrtion
            if i == n:
                res.append(sub.copy())
                return

            # 1. pic the num -> go next
            sub.append(nums[i])
            dfs_backtrack(i+1)

            # 2. dont-pic/clear -> go next
            sub.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]: i += 1
            dfs_backtrack(i+1)

        dfs_backtrack(0)
        return res 