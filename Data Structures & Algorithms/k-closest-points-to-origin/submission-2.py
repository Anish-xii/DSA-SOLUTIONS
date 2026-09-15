class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # get all the distance
        point_distance = []
        for x, y in points:
            d = x**2 + y**2
            point_distance.append((d, x, y))
        
        # order the distances
        heapq.heapify(point_distance)

        # return the k smallest
        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(point_distance)
            res.append([x, y])
        
        return res