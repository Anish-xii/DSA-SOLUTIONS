class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort()  # sort by 0idx
        
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res
        