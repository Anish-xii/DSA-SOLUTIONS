class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for n in nums:
            if n not in dict: dict[n] = [1, n]
            else: dict[n][0] += 1

        count = list(dict.values())
        count.sort(reverse=True)

        res = []
        for i in range(k): res.append(count[i][1])

        return res