class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        
        def backtrack(start: int):
            # Base case: one complete permutation
            if start == n:
                res.append(nums[:])  # append a copy of nums
                return
            
            for i in range(start, n):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recurse to fill the next position
                backtrack(start + 1)
                
                # Swap back to restore the original array
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res             