import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        # push all the heads (i: to break the tie if same val)
        for i, h in enumerate(lists):
            if h: heapq.heappush(heap, (h.val, i, h))

        # pop-old add-next connect
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            # i: same as its head as we have [h1, h2, h3]
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next