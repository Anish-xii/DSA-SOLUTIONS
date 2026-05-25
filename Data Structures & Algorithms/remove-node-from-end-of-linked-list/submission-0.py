# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        c = head
        while c: 
            cnt += 1
            c = c.next

        if cnt == 1: return None
        curr = head

        while curr and curr.next:
            if cnt == n:
                head = curr.next
                return head
            elif cnt-1 == n: 
                curr.next = curr.next.next
                return head
            curr = curr.next
            cnt -= 1    
