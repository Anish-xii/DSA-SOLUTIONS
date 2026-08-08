class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for n, cnt in count.items():
            buckets[cnt].append(n)
        
        res = []
        for freq in range(len(buckets)-1, 0, -1):
            for n in buckets[freq]:
                res.append(n)
                if len(res) == k: return res
