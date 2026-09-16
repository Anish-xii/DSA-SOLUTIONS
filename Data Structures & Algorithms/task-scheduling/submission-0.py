class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()] # custom heap
        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time += 1

            if maxheap:
                cnt = heapq.heappop(maxheap) + 1 # decrease the count
                if cnt != 0:
                    q.append([cnt, time+n]) # [new_cnt, when its avalabele]
            
            # when its time for a q eliment
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(maxheap, cnt) # make count avaleble for use
        
        return time