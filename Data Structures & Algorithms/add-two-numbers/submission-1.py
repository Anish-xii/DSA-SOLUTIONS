
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            f_val = l1.val if l1 else 0
            s_val = l2.val if l2 else 0
            
            total = (f_val + s_val + carry)
            val = total % 10
            carry = total // 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next