class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        
        # get the middle (s.n - end)
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # split into 2 list (head, curr)
        curr = s.next
        s.next = None

        # reverse 2nd list
        prev = None
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # reorder combine
        first, snd = head, prev
        
        while snd:
            tmp1 = first.next
            tmp2 = snd.next
            first.next = snd
            snd.next = tmp1
            first = tmp1
            snd = tmp2