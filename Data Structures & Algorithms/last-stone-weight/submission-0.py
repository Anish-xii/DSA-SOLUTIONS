class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        arr = [-x for x in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            hs_1 = heapq.heappop(arr)
            hs_2 = heapq.heappop(arr)
            
            # as we comparing netions (-1 > -2)
            if hs_2 > hs_1: 
                heapq.heappush(arr, hs_1 - hs_2)

        # edgecase when all stone smashed
        arr.append(0)
        return abs(arr[0]) 