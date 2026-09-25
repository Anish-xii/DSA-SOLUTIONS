class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize: return False

        count = {}  # counter(hand)
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # we need a way to get the smallest item
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # cur smallest num
            first_num = min_heap[0]
            
            # for every "consecative" num from current smallest num
            for n in range(first_num, first_num + groupSize):
                
                # dont have num
                if n not in count:
                    return False
                count[n] -= 1
                
                # dont have next cocesative num after curr-smallest num
                if count[n] == 0:
                    if n != min_heap[0]:
                        return False
                    else:
                        heapq.heappop(min_heap)
        
        return True
        