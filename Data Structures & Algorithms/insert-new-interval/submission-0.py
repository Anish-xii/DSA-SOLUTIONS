class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        res = []

        for i in range(len(intervals)):

            # if the interval is before 'newInterval'
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # if the interval is after 'newInterval'
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                                max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res