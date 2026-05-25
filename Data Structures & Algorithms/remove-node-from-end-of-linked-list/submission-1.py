# window+2pointer
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        l = r = head

        for _ in range(n):
            r = r.next
        if not r: return head.next

        while r.next:
            l = l.next # 1 step before n
            r = r.next 

        l.next = l.next.next
        return head  
