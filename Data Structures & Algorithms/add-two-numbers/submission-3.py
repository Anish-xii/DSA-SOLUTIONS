class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            fnum = l1.val if l1 else 0
            snum = l2.val if l2 else 0

            total = fnum + snum + carry

            carry = total // 10
            use = total % 10
            
            node = ListNode(use)
            curr.next = node

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next