class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        dq = deque()

        l = 0
        for r in range(len(nums)):
           
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            
            dq.append(r)
            if dq[0] < l: dq.popleft()

            if r-l+1 >= k:
                res.append(nums[dq[0]])
                l += 1
        
        return res

# 2 things:
# 1. have a que store only the max nums seen so far for each slide
# 2. from the front remove any pice thats out of range      