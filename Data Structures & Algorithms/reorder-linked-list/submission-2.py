class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return 

        # get the middle
        slo = fast = head
        while fast and fast.next:
            slo = slo.next
            fast = fast.next.next

        # reverse the second portion
        prev, curr = None, slo.next
        slo.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # connect acordingly
        first, secnd = head, prev

        while secnd:
            tmp1, tmp2 = first.next, secnd.next
            first.next = secnd
            secnd.next = tmp1
            first, secnd = tmp1, tmp2