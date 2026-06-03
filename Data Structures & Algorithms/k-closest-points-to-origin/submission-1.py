class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_q = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(min_q, (distance, point))

        result = []
        for closest in range(k):
            distance, point = heapq.heappop(min_q)
            result.append(point)
        return result