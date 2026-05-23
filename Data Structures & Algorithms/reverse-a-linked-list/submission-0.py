# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = None
        c = head

        while c:
            temp = c.next # 1. save the conection
            c.next = n # 3. new next of curr node
            n = c # 4. new next of next node
            c = temp # 2. same process for next node

        return n      