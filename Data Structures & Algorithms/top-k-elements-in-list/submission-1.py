class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}  
        for n in nums: count[n] = count.get(n, 0) + 1

        boxes = [[] for _ in range(len(nums)+1)] # list of all posible res
        for key, val in count.items(): boxes[val].append(key)

        res = []
        for i in range(len(boxes) - 1, 0, -1):
            for n in boxes[i]: res.append(n)
            if len(res) == k:
                return res