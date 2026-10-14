# dummy + window 
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy = ListNode()
        dummy.next = head

        l = r = dummy

        # get the prev of the one we remove
        for _ in range(n+1):
            r = r.next
        
        # slide the window till the end
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return dummy.next