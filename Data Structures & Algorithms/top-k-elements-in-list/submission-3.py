class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Sort dictionary items by frequency (value) in descending order
        sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        # Take the top k elements from the sorted list
        for i in range(k):
            res.append(sorted_counts[i][0])

        return res            