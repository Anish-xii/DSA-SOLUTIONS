class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return 

        # get the middle
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        # reverse the second portion
        second = s.next
        s.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # connect
        h1, h2 = head, prev

        while h2:
            tmp1, tmp2 = h1.next, h2.next
            h1.next = h2
            h2.next = tmp1
            h1, h2 = tmp1, tmp2