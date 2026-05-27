# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head
        prev = node
        curr = head
        count = 0
        while curr: 
            count += 1
            curr = curr.next

        while count >= k:
            curr = prev.next
            nxt = curr.next

            for _ in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
            count -= k

        return node.next  