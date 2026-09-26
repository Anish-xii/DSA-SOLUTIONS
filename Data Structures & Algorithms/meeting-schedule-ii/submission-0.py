"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count, max_count = 0, 0
        si, ei = 0, 0

        while si < len(intervals):
            # for every new meeting while last meet hase'nt ended room_count+=1
            if start[si] < end[ei]:
                si += 1
                count += 1
            # for every meeting end 1 room gets free
            else:
                ei += 1
                count -= 1
            
            # what point we used max room
            max_count = max(max_count, count)
        
        return max_count
        