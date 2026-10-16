# Permutation: same nums, diffrent orders, (unique orders)
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        sub = []

        l = len(nums)

        def dfs():
            if len(sub) == l:
                res.append(sub.copy())
                return

            # use next num to make unq seq, n thats not alredy used 
            for n in nums:
                if n not in sub:
                    sub.append(n)
                    dfs()
                    sub.pop()

        dfs()
        return res