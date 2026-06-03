# max heap (modified min-heap with (-))
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            dis = -(x ** 2 + y ** 2)
            heapq.heappush(arr, [dis, x, y])
            # only store k many items
            if len(arr) > k:
                heapq.heappop(arr)

        res = []
        while arr:
            dis, x, y = heapq.heappop(arr)
            res.append([x, y])

        return res 