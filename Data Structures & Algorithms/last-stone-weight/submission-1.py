class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)

        # untill thre is 1 or less stone
        while len(maxheap) > 1:
            largest_1 = heapq.heappop(maxheap)
            largest_2 = heapq.heappop(maxheap)

            # when diffrent value (smash)
            if largest_1 != largest_2:
                heapq.heappush(maxheap, largest_1 - largest_2)

        return abs(maxheap[0]) if maxheap else 0