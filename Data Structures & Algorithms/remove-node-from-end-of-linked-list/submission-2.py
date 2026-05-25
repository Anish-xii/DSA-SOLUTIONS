# dummy + window 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        a = b = dummy

        for _ in range(n+1):
            a = a.next

        while a:
            a = a.next
            b = b.next

        b.next = b.next.next

        return dummy.next          
