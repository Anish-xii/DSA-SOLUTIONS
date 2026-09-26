class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        
        last_idx = {}  # chat -> last idx of each char in 's'

        for i, c in enumerate(s):
            last_idx[c] = i
        
        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, last_idx[c])

            # when reached at last idx posible of all 'c' seen so far
            if i == end:
                res.append(size)
                size = 0
        
        return res
        