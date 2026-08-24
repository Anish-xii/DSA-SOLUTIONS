
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:

            f_digit = l1.val if l1 else 0
            s_digit = l2.val if l2 else 0

            total = f_digit + s_digit + carry

            x = total % 10 # 2nd digit of a two digit sum
            node = ListNode(x)
            curr.next = node
            
            carry = total // 10 # digit we carry forword

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next