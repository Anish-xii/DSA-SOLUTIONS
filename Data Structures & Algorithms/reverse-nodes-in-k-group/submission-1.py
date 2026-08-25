# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        # count num of nodes
        count = 0
        curr = dummy.next
        while curr:
            count += 1
            curr = curr.next
        
        # while k groups exists to reverse
        prev = dummy
        while count >= k:
            
            curr = prev.next
            nxt = curr.next

            # a-b-c -> b-a-c -> c-b-a
            for _ in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            
            prev = curr
            count -= k
        
        return dummy.next  