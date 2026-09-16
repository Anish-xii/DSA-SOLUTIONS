# by picking or not picking when we reach the end
# only then we add subset to res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sub = [], []

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
            dfs_backtrack(i+1)

        dfs_backtrack(0)
        return res    

"""Since each element independently is either in or out, I model this as a binary decision tree — at every index, branch into include/exclude, and since both branches always advance the index, no element is ever reused, and every root-to-leaf path corresponds to exactly one unique subset."""