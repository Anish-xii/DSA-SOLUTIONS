class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, n in enumerate(nums):
        
        # when i is traking values from k+1 window
        # pop that from saved so it only traks k many
            while q and q[0] < i+1 - k:
                q.popleft()
        
        # maintain a high - low que
            while q and nums[q[-1]] < n:
                q.pop()

            q.append(i)

        # start adding max's from q once q has its first k values
            if i+1 >= k: 
                x = nums[q[0]]
                res.append(x)     

        return res      