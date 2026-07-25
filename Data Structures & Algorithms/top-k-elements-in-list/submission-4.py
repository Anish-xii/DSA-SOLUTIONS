class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        boxes = [[] for _ in range(len(nums) + 1)]
        for n, f in count.items():
            boxes[f].append(n)

        res = []
        for i in range(len(boxes)-1, 0, -1):
            for n in boxes[i]:
                res.append(n)
                if len(res) == k:
                    return res     