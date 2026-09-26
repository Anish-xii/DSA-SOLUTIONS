# Case-1: find how many to remove

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort()

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # when next intervals starts after/= end of lastone
            if start >= prev_end:
                prev_end = end
            # when overlap (take the less-risky/less-reach one)
            else:
                count += 1
                prev_end = min(prev_end, end)  
        
        return count