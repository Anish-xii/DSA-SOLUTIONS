# heapq garaunties parent <= child, so res[0]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = []

        for n in nums:
            if len(arr) < k: heapq.heappush(arr, n)
            else: heapq.heappushpop(arr, n)

        return arr[0]  