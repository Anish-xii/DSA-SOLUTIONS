
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        
        x, y = l1, l2
        carry = 0

        while x and y:
            total = (x.val + y.val + carry)
            val = total % 10
            carry = total // 10
            curr.next = ListNode(val)
            curr = curr.next
            x, y = x.next, y.next

        remaining = x if x else y

        while remaining:
            total = remaining.val + carry
            val = total % 10
            carry = total // 10
            curr.next = ListNode(val)
            curr = curr.next
            remaining = remaining.next

        if carry: curr.next = ListNode(carry)

        return dummy.next